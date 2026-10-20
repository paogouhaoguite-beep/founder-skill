"""Minimal Binance spot REST client (standard library only) and the two brokers.

PaperBroker trades with pretend money against real live prices.
LiveBroker places real orders. It needs an API key with SPOT TRADING ONLY:
never enable withdrawals on the key the bot uses.
"""

import hashlib
import hmac
import json
import time
from decimal import ROUND_DOWN, Decimal
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

INTERVAL_MS = {"15m": 900_000, "30m": 1_800_000, "1h": 3_600_000, "2h": 7_200_000,
               "4h": 14_400_000, "6h": 21_600_000, "12h": 43_200_000, "1d": 86_400_000}


class BinanceError(Exception):
    pass


def floor_to_step(value, step):
    step_d = Decimal(str(step))
    if step_d <= 0:
        return Decimal(str(value))
    return (Decimal(str(value)) / step_d).to_integral_value(rounding=ROUND_DOWN) * step_d


def fmt(d):
    s = format(Decimal(d).normalize(), "f")
    return s if s not in ("-0", "") else "0"


class BinanceClient:
    def __init__(self, base_url="https://api.binance.com", api_key="", api_secret=""):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.api_secret = api_secret.encode()
        self.time_offset = 0
        self._symbol_cache = {}

    def _request(self, method, path, params=None, signed=False):
        params = dict(params or {})
        if signed:
            if not self.api_key:
                raise BinanceError("This call needs BINANCE_API_KEY and BINANCE_API_SECRET.")
            params["timestamp"] = int(time.time() * 1000) + self.time_offset
            params["recvWindow"] = 5000
        query = urlencode(params)
        if signed:
            sig = hmac.new(self.api_secret, query.encode(), hashlib.sha256).hexdigest()
            query += "&signature=" + sig
        headers = {"X-MBX-APIKEY": self.api_key} if self.api_key else {}
        url = self.base_url + path + ("?" + query if query else "")
        try:
            with urlopen(Request(url, method=method, headers=headers), timeout=20) as resp:
                return json.loads(resp.read().decode())
        except HTTPError as e:
            raise BinanceError("%s %s: %s" % (e.code, path, e.read().decode(errors="replace"))) from None

    def sync_time(self):
        server = self._request("GET", "/api/v3/time")["serverTime"]
        self.time_offset = server - int(time.time() * 1000)

    # ---- market data -------------------------------------------------
    def klines(self, symbol, interval, limit=500, end_time=None):
        params = {"symbol": symbol, "interval": interval, "limit": min(limit, 1000)}
        if end_time is not None:
            params["endTime"] = end_time
        rows = self._request("GET", "/api/v3/klines", params)
        return [{"t": r[0], "o": float(r[1]), "h": float(r[2]), "l": float(r[3]), "c": float(r[4]),
                 "v": float(r[5]), "close_time": r[6]} for r in rows]

    def closed_klines(self, symbol, interval, total):
        """The most recent `total` CLOSED candles (the still-forming one is dropped)."""
        now = int(time.time() * 1000)
        out, end = [], None
        while len(out) < total + 1:
            page = self.klines(symbol, interval, min(1000, total + 1 - len(out)), end)
            if not page:
                break
            out = page + out
            end = page[0]["t"] - 1
            if len(page) < 2:
                break
        out = [c for c in out if c["close_time"] < now]
        return out[-total:]

    def price(self, symbol):
        return float(self._request("GET", "/api/v3/ticker/price", {"symbol": symbol})["price"])

    def symbol_info(self, symbol):
        if symbol not in self._symbol_cache:
            data = self._request("GET", "/api/v3/exchangeInfo", {"symbol": symbol})["symbols"][0]
            f = {x["filterType"]: x for x in data["filters"]}
            notional = f.get("NOTIONAL") or f.get("MIN_NOTIONAL") or {}
            self._symbol_cache[symbol] = {
                "base": data["baseAsset"],
                "quote": data["quoteAsset"],
                "step": float(f["LOT_SIZE"]["stepSize"]),
                "min_qty": float(f["LOT_SIZE"]["minQty"]),
                "tick": float(f["PRICE_FILTER"]["tickSize"]),
                "min_notional": float(notional.get("minNotional", 5.0)),
                "quote_precision": int(data.get("quoteAssetPrecision", 8)),
            }
        return self._symbol_cache[symbol]

    # ---- account and orders (signed) ----------------------------------
    def balances(self):
        acct = self._request("GET", "/api/v3/account", signed=True)
        return {b["asset"]: float(b["free"]) for b in acct["balances"]}

    def order(self, **params):
        params.setdefault("newOrderRespType", "FULL")
        return self._request("POST", "/api/v3/order", params, signed=True)

    def cancel_order(self, symbol, order_id):
        return self._request("DELETE", "/api/v3/order", {"symbol": symbol, "orderId": order_id}, signed=True)

    def get_order(self, symbol, order_id):
        return self._request("GET", "/api/v3/order", {"symbol": symbol, "orderId": order_id}, signed=True)


class PaperBroker:
    """Pretend money, real prices. Balances live in the bot's state file."""

    live = False

    def __init__(self, client, cfg, state):
        self.client, self.cfg, self.state = client, cfg, state
        state.setdefault("paper_cash", float(cfg["start_equity"]))

    def quote_balance(self):
        return self.state["paper_cash"]

    def buy(self, symbol, quote_amount):
        price = self.client.price(symbol) * (1 + self.cfg["slippage"])
        qty = quote_amount / price * (1 - self.cfg["fee_rate"])
        self.state["paper_cash"] -= quote_amount
        return qty, price

    def sell(self, symbol, qty):
        price = self.client.price(symbol) * (1 - self.cfg["slippage"])
        proceeds = qty * price * (1 - self.cfg["fee_rate"])
        self.state["paper_cash"] += proceeds
        return proceeds

    def place_stop(self, symbol, qty, stop_price):
        return None

    def cancel_stop(self, symbol, stop_id):
        pass

    def stop_fill(self, position, last_price):
        """Proceeds if the stop was hit, else None."""
        if last_price > position["stop"]:
            return None
        proceeds = position["qty"] * last_price * (1 - self.cfg["slippage"]) * (1 - self.cfg["fee_rate"])
        self.state["paper_cash"] += proceeds
        return proceeds


class LiveBroker:
    """Real orders on Binance spot. Every position also gets a resting
    STOP_LOSS_LIMIT order on the exchange, so the stop still works if your
    computer or the bot goes offline."""

    live = True

    def __init__(self, client, cfg, state):
        self.client, self.cfg, self.state = client, cfg, state
        client.sync_time()

    def _quote_asset(self):
        return self.client.symbol_info(self.cfg["symbols"][0])["quote"]

    def quote_balance(self):
        return self.client.balances().get(self._quote_asset(), 0.0)

    def buy(self, symbol, quote_amount):
        info = self.client.symbol_info(symbol)
        decimals = 2 if info["quote"] in ("USDT", "USDC", "FDUSD") else min(info["quote_precision"], 8)
        amount = floor_to_step(quote_amount, 10 ** -decimals)
        res = self.client.order(symbol=symbol, side="BUY", type="MARKET", quoteOrderQty=fmt(amount))
        filled = float(res["executedQty"])
        fee_in_base = sum(float(f["commission"]) for f in res.get("fills", []) if f["commissionAsset"] == info["base"])
        avg = float(res["cummulativeQuoteQty"]) / filled if filled else 0.0
        return filled - fee_in_base, avg

    def sell(self, symbol, qty):
        info = self.client.symbol_info(symbol)
        held = self.client.balances().get(info["base"], 0.0)
        q = floor_to_step(min(qty, held), info["step"])
        if q <= 0 or float(q) < info["min_qty"]:
            return 0.0
        res = self.client.order(symbol=symbol, side="SELL", type="MARKET", quantity=fmt(q))
        return float(res["cummulativeQuoteQty"]) * (1 - self.cfg["fee_rate"])

    def place_stop(self, symbol, qty, stop_price):
        info = self.client.symbol_info(symbol)
        q = floor_to_step(qty, info["step"])
        stop = floor_to_step(stop_price, info["tick"])
        limit = floor_to_step(stop_price * (1 - self.cfg["stop_limit_buffer"]), info["tick"])
        if q <= 0 or limit <= 0:
            return None
        res = self.client.order(symbol=symbol, side="SELL", type="STOP_LOSS_LIMIT", timeInForce="GTC",
                                quantity=fmt(q), stopPrice=fmt(stop), price=fmt(limit))
        return res["orderId"]

    def cancel_stop(self, symbol, stop_id):
        if stop_id is None:
            return
        try:
            self.client.cancel_order(symbol, stop_id)
        except BinanceError:
            pass  # already filled or gone; stop_fill() will notice

    def stop_fill(self, position, last_price):
        stop_id = position.get("stop_id")
        if stop_id is None:
            if last_price <= position["stop"]:
                return self.sell(position["symbol"], position["qty"])
            return None
        o = self.client.get_order(position["symbol"], stop_id)
        if o["status"] == "FILLED":
            return float(o["cummulativeQuoteQty"]) * (1 - self.cfg["fee_rate"])
        if o["status"] in ("CANCELED", "EXPIRED", "REJECTED"):
            position["stop_id"] = None
        return None
