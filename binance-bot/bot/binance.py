"""Minimal Binance spot REST client (standard library only) and the two brokers.

PaperBroker buys and sells with pretend money at real live prices.
LiveBroker places real orders. It needs an API key with SPOT TRADING ONLY:
never enable withdrawals on the key the bot uses.
"""

import hashlib
import hmac
import json
import time
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .exchange import ExchangeError, floor_to_step, fmt, refused

BinanceError = ExchangeError


class BinanceClient:
    def __init__(self, base_url="https://api.binance.com", api_key="", api_secret=""):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.api_secret = api_secret.encode()
        self.time_offset = 0
        self.cache_seconds = 3600  # re-read coin details hourly, so a delisting is noticed
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
            raise BinanceError("%s %s: %s" % (e.code, path, e.read().decode(errors="replace")), e.code) from None

    def sync_time(self):
        server = self._request("GET", "/api/v3/time")["serverTime"]
        self.time_offset = server - int(time.time() * 1000)

    def price(self, symbol):
        p = float(self._request("GET", "/api/v3/ticker/price", {"symbol": symbol})["price"])
        if p <= 0:
            raise ExchangeError("Binance shows no valid price for %s right now" % symbol)
        return p

    def _signed(self, method, path, params=None):
        try:
            return self._request(method, path, params, signed=True)
        except BinanceError as e:
            if "-1021" not in str(e):
                raise
            # this device's clock drifted away from Binance's; resync and try once more
            self.sync_time()
            return self._request(method, path, params, signed=True)

    def symbol_info(self, symbol):
        cached = self._symbol_cache.get(symbol)
        if cached is None or time.time() - cached[0] >= self.cache_seconds:
            data = self._request("GET", "/api/v3/exchangeInfo", {"symbol": symbol})["symbols"][0]
            f = {x["filterType"]: x for x in data["filters"]}
            notional = f.get("NOTIONAL") or f.get("MIN_NOTIONAL") or {}
            self._symbol_cache[symbol] = (time.time(), {
                "base": data["baseAsset"],
                "quote": data["quoteAsset"],
                "step": float(f["LOT_SIZE"]["stepSize"]),
                "min_qty": float(f["LOT_SIZE"]["minQty"]),
                "min_notional": float(notional.get("minNotional", 5.0)),
                "quote_precision": int(data.get("quoteAssetPrecision", 8)),
                "trading": data.get("status", "TRADING") == "TRADING",
            })
        return self._symbol_cache[symbol][1]

    # ---- account and orders (signed) ----------------------------------
    def balances(self):
        acct = self._signed("GET", "/api/v3/account")
        return {b["asset"]: float(b["free"]) for b in acct["balances"]}

    def order(self, **params):
        params.setdefault("newOrderRespType", "FULL")
        return self._signed("POST", "/api/v3/order", params)

    def get_order(self, symbol, client_order_id):
        params = {"symbol": symbol, "origClientOrderId": client_order_id}
        return self._signed("GET", "/api/v3/order", params)


class PaperBroker:
    """Pretend money at real prices: nothing is sent to Binance."""

    live = False

    def __init__(self, client, cfg):
        self.client, self.cfg = client, cfg

    def buy(self, symbol, quote_amount, order_id=None):
        """Returns (quantity received after fee, average price, quote spent)."""
        price = getattr(self.client, "buy_price", self.client.price)(symbol) * (1 + self.cfg["slippage"])
        return quote_amount / price * (1 - self.cfg["fee_rate"]), price, quote_amount

    def sell(self, symbol, qty, order_id=None):
        """Returns (money received, coins sold, coins sent)."""
        price = getattr(self.client, "sell_price", self.client.price)(symbol) * (1 - self.cfg["slippage"])
        return qty * price * (1 - self.cfg["fee_rate"]) * (1 - self.cfg.get("tds_rate", 0.0)), qty, qty

    def recover_buy(self, symbol, order_id):
        return None

    def recover_sell(self, symbol, order_id):
        return None


class LiveBroker:
    """Real market orders on Binance spot."""

    live = True

    def __init__(self, client, cfg):
        self.client, self.cfg = client, cfg
        try:
            client.sync_time()
        except (ExchangeError, OSError):
            pass  # no connection yet; requests resync by themselves if the clock is off

    def quote_balance(self, symbol):
        quote = self.client.symbol_info(symbol)["quote"]
        return self.client.balances().get(quote, 0.0)

    def _place(self, order_id, **params):
        """Send an order. If the reply is lost (timeout, dropped connection,
        Binance 5xx) look the order up by its ID instead of guessing, so a
        lost reply never turns into a second order. If even the lookup fails,
        the error is raised and the caller keeps the ID to check later."""
        params["newClientOrderId"] = order_id
        try:
            return self.client.order(**params)
        except (OSError, BinanceError) as e:
            if isinstance(e, BinanceError) and (e.status or 0) < 500:
                raise  # Binance rejected it; nothing was placed
            for _ in range(3):
                time.sleep(1)
                try:
                    return self.client.get_order(params["symbol"], order_id)
                except BinanceError as lookup:
                    if refused(lookup):
                        raise e from None  # the order never reached Binance
                except OSError:
                    pass
            raise

    def _lookup(self, symbol, order_id):
        try:
            order = self.client.get_order(symbol, order_id)
        except BinanceError as e:
            if refused(e):
                return None  # Binance has no such order: it was never placed
            raise
        if not isinstance(order, dict) or "status" not in order:
            return None
        return order

    def _buy_result(self, symbol, res):
        info = self.client.symbol_info(symbol)
        filled = float(res["executedQty"])
        spent = float(res["cummulativeQuoteQty"])
        fee_in_base = sum(float(f["commission"]) for f in res.get("fills", []) if f["commissionAsset"] == info["base"])
        if not res.get("fills") and filled:
            fee_in_base = filled * self.cfg["fee_rate"]  # a looked-up order has no fill details
        return filled - fee_in_base, (spent / filled if filled else 0.0), spent

    def buy(self, symbol, quote_amount, order_id):
        """Returns (quantity received after fee, average price, quote spent).
        Quantity is 0 if Binance could not fill the order."""
        info = self.client.symbol_info(symbol)
        decimals = 2 if info["quote"] in ("USDT", "USDC", "FDUSD") else min(info["quote_precision"], 8)
        amount = floor_to_step(quote_amount, 10 ** -decimals)
        res = self._place(order_id, symbol=symbol, side="BUY", type="MARKET", quoteOrderQty=fmt(amount))
        return self._buy_result(symbol, res)

    def sell(self, symbol, qty, order_id):
        info = self.client.symbol_info(symbol)
        held = self.client.balances().get(info["base"], 0.0)
        q = floor_to_step(min(qty, held), info["step"])
        if q <= 0 or float(q) < info["min_qty"]:
            return 0.0, 0.0, float(q)
        res = self._place(order_id, symbol=symbol, side="SELL", type="MARKET", quantity=fmt(q))
        return self._sell_result(res)

    def _sell_result(self, res):
        """(USDT received, coins sold, coins sent). A market order that expired
        unfilled (no buyers) sold nothing."""
        got = float(res["cummulativeQuoteQty"]) * (1 - self.cfg["fee_rate"])
        return got, float(res["executedQty"]), float(res.get("origQty") or res["executedQty"])

    def recover_buy(self, symbol, order_id):
        res = self._lookup(symbol, order_id)
        return None if res is None else self._buy_result(symbol, res)

    def recover_sell(self, symbol, order_id):
        res = self._lookup(symbol, order_id)
        return None if res is None else self._sell_result(res)
