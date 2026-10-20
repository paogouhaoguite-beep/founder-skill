"""Minimal Binance spot REST client (standard library only) and the two brokers.

PaperBroker buys and sells with pretend money at real live prices.
LiveBroker places real orders. It needs an API key with SPOT TRADING ONLY:
never enable withdrawals on the key the bot uses.
"""

import hashlib
import hmac
import json
import time
import uuid
from decimal import ROUND_DOWN, Decimal
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class BinanceError(Exception):
    def __init__(self, message, status=None):
        super().__init__(message)
        self.status = status


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
            raise BinanceError("%s %s: %s" % (e.code, path, e.read().decode(errors="replace")), e.code) from None

    def sync_time(self):
        server = self._request("GET", "/api/v3/time")["serverTime"]
        self.time_offset = server - int(time.time() * 1000)

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
                "min_notional": float(notional.get("minNotional", 5.0)),
                "quote_precision": int(data.get("quoteAssetPrecision", 8)),
                "trading": data.get("status", "TRADING") == "TRADING",
            }
        return self._symbol_cache[symbol]

    # ---- account and orders (signed) ----------------------------------
    def balances(self):
        acct = self._request("GET", "/api/v3/account", signed=True)
        return {b["asset"]: float(b["free"]) for b in acct["balances"]}

    def order(self, **params):
        params.setdefault("newOrderRespType", "FULL")
        return self._request("POST", "/api/v3/order", params, signed=True)

    def get_order(self, symbol, client_order_id):
        params = {"symbol": symbol, "origClientOrderId": client_order_id}
        return self._request("GET", "/api/v3/order", params, signed=True)


class PaperBroker:
    """Pretend money at real prices: nothing is sent to Binance."""

    live = False

    def __init__(self, client, cfg):
        self.client, self.cfg = client, cfg

    def buy(self, symbol, quote_amount):
        price = self.client.price(symbol) * (1 + self.cfg["slippage"])
        return quote_amount / price * (1 - self.cfg["fee_rate"]), price

    def sell(self, symbol, qty):
        price = self.client.price(symbol) * (1 - self.cfg["slippage"])
        return qty * price * (1 - self.cfg["fee_rate"])


class LiveBroker:
    """Real market orders on Binance spot."""

    live = True

    def __init__(self, client, cfg):
        self.client, self.cfg = client, cfg
        client.sync_time()

    def quote_balance(self):
        quote = self.client.symbol_info(self.cfg["dca_symbols"][0])["quote"]
        return self.client.balances().get(quote, 0.0)

    def _place(self, **params):
        """Send an order. If the reply is lost (timeout, dropped connection,
        Binance 5xx) look the order up by its client id instead of guessing,
        so a lost reply never turns into a second order."""
        params["newClientOrderId"] = "bot" + uuid.uuid4().hex[:24]
        try:
            return self.client.order(**params)
        except (OSError, BinanceError) as e:
            if isinstance(e, BinanceError) and (e.status or 0) < 500:
                raise  # Binance rejected it; nothing was placed
            for _ in range(3):
                time.sleep(1)
                try:
                    return self.client.get_order(params["symbol"], params["newClientOrderId"])
                except BinanceError as lookup:
                    if (lookup.status or 0) < 500:
                        raise e from None  # the order never reached Binance
                except OSError:
                    pass
            raise

    def buy(self, symbol, quote_amount):
        info = self.client.symbol_info(symbol)
        decimals = 2 if info["quote"] in ("USDT", "USDC", "FDUSD") else min(info["quote_precision"], 8)
        amount = floor_to_step(quote_amount, 10 ** -decimals)
        res = self._place(symbol=symbol, side="BUY", type="MARKET", quoteOrderQty=fmt(amount))
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
        res = self._place(symbol=symbol, side="SELL", type="MARKET", quantity=fmt(q))
        return float(res["cummulativeQuoteQty"]) * (1 - self.cfg["fee_rate"])
