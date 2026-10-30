"""Minimal CoinDCX spot client (standard library only) and the live broker.

Works on CoinDCX's rupee markets (BTCINR, ETHINR, SOLINR, ...), so buys are
paid in INR and profit sales pay out INR, which can be withdrawn to a bank.
The API key needs trading permission only; never give it withdrawal rights.

CoinDCX differs from Binance in ways that matter here:
- market orders are sized in coins, not rupees, so the bot works the coin
  amount out from the current asking price;
- an order is accepted first and filled a moment later, so the bot waits
  for the fill and, if it does not see one, checks the same order later;
- the spread between buy and sell prices on INR markets can be about 0.5%,
  so holdings are valued at the price you could actually sell at (the bid).
"""

import hashlib
import hmac
import json
import time
from decimal import Decimal
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from .exchange import ExchangeError, floor_to_step, fmt, refused

FINAL = {"filled", "cancelled", "rejected", "partially_cancelled"}


def dumps(body):
    """Compact JSON with Decimal values written as plain numbers (0.00006, never 6e-05)."""
    raw = {}

    def mark(v):
        if isinstance(v, Decimal):
            key = "@@%d@@" % len(raw)
            raw['"%s"' % key] = fmt(v)
            return key
        return v

    out = json.dumps({k: mark(v) for k, v in body.items()}, separators=(",", ":"))
    for key, num in raw.items():
        out = out.replace(key, num)
    return out


class CoinDCXClient:
    def __init__(self, base_url="https://api.coindcx.com", api_key="", api_secret=""):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.api_secret = api_secret.encode()
        self.cache_seconds = 3600  # market details; re-read hourly so a delisting is noticed
        self.ticker_seconds = 20
        self._markets = (0.0, {})
        self._ticker = (0.0, {})
        self.time_offset = 0  # ms to add to this device's clock to match CoinDCX's

    def _learn_clock(self, date_header):
        """CoinDCX rejects requests whose timestamp is too far off and offers no
        clock to sync with, so read its time from the Date header of each reply.
        It is accurate to about a second, so only a clear drift is corrected."""
        try:
            server = parsedate_to_datetime(date_header).timestamp() * 1000
        except (TypeError, ValueError, IndexError):
            return
        offset = int(server - time.time() * 1000)
        self.time_offset = offset if abs(offset) > 5000 else 0

    def _request(self, method, path, body=None):
        # CoinDCX's firewall rejects Python's default User-Agent (error 1010), so name the bot
        headers = {"Content-Type": "application/json", "User-Agent": "coindcx-weekly-bot/1.0"}
        data = None
        if body is not None:
            if not self.api_key:
                raise ExchangeError("This call needs COINDCX_API_KEY and COINDCX_API_SECRET.")
            body = dict(body, timestamp=int(time.time() * 1000) + self.time_offset)
            payload = dumps(body)
            headers["X-AUTH-APIKEY"] = self.api_key
            headers["X-AUTH-SIGNATURE"] = hmac.new(self.api_secret, payload.encode(), hashlib.sha256).hexdigest()
            data = payload.encode()
        try:
            with urlopen(Request(self.base_url + path, data=data, method=method, headers=headers), timeout=20) as r:
                self._learn_clock((getattr(r, "headers", None) or {}).get("Date"))
                return json.loads(r.read().decode())
        except HTTPError as e:
            self._learn_clock((e.headers or {}).get("Date"))
            raise ExchangeError("%s %s: %s" % (e.code, path, e.read().decode(errors="replace")), e.code) from None

    # ---- market data -------------------------------------------------
    def _market_table(self):
        fetched, table = self._markets
        if time.time() - fetched >= self.cache_seconds:
            table = {m["coindcx_name"]: m for m in self._request("GET", "/exchange/v1/markets_details")}
            self._markets = (time.time(), table)
        return table

    def symbol_info(self, symbol):
        m = self._market_table().get(symbol)
        if m is None:
            raise ExchangeError("404 %s is not a CoinDCX market" % symbol, 404)
        return {
            "base": m["target_currency_short_name"],   # CoinDCX calls the coin "target"
            "quote": m["base_currency_short_name"],    # and the rupee "base"
            "step": float(m["step"]),
            "min_qty": float(m["min_quantity"]),
            "min_notional": float(m["min_notional"]),
            "qty_precision": int(m["target_currency_precision"]),
            "trading": m.get("status") == "active" and "market_order" in m.get("order_types", []),
        }

    def _tick(self, symbol):
        fetched, table = self._ticker
        if time.time() - fetched >= self.ticker_seconds:
            table = {t["market"]: t for t in self._request("GET", "/exchange/ticker")}
            self._ticker = (time.time(), table)
        t = table.get(symbol)
        if t is None:
            raise ExchangeError("404 no price for %s" % symbol, 404)
        return t

    def _positive(self, symbol, *values):
        for v in values:
            try:
                if v is not None and float(v) > 0:
                    return float(v)
            except ValueError:
                pass
        # a zero or missing price happens briefly during maintenance; never trade on it
        raise ExchangeError("CoinDCX shows no valid price for %s right now" % symbol)

    def price(self, symbol):
        return self._positive(symbol, self._tick(symbol).get("last_price"))

    def buy_price(self, symbol):
        t = self._tick(symbol)
        return self._positive(symbol, t.get("ask"), t.get("last_price"))

    def sell_price(self, symbol):
        t = self._tick(symbol)
        return self._positive(symbol, t.get("bid"), t.get("last_price"))

    # ---- account and orders (signed) ----------------------------------
    def balances(self):
        return {b["currency"]: float(b["balance"]) for b in self._request("POST", "/exchange/v1/users/balances", {})}

    def create_order(self, **body):
        res = self._request("POST", "/exchange/v1/orders/create", body)
        return res["orders"][0] if isinstance(res, dict) and "orders" in res else res

    def order_status(self, client_order_id):
        return self._request("POST", "/exchange/v1/orders/status", {"client_order_id": client_order_id})


class CoinDCXBroker:
    """Real market orders on CoinDCX."""

    live = True

    def __init__(self, client, cfg, wait_seconds=30, sleep=time.sleep):
        self.client, self.cfg = client, cfg
        self.wait_seconds, self.sleep = wait_seconds, sleep

    def quote_balance(self, symbol):
        return self.client.balances().get(self.client.symbol_info(symbol)["quote"], 0.0)

    def _lookup(self, order_id):
        try:
            order = self.client.order_status(order_id)
        except ExchangeError as e:
            if refused(e):
                return None  # CoinDCX has no such order: it was never placed
            raise
        if not isinstance(order, dict) or "status" not in order:
            return None  # an answer with no order in it: there is no such order
        return order

    def _place_and_wait(self, order_id, **body):
        """Place an order and wait for it to finish filling. If the outcome cannot
        be confirmed, raise; the caller keeps the order ID and checks it later."""
        try:
            order = self.client.create_order(client_order_id=order_id, **body)
        except ExchangeError as e:
            if refused(e) or e.status == 429:
                raise  # refused or rate limited: nothing was placed
            order = None  # outage: it may or may not have been placed
        except OSError:
            order = None
        deadline = time.time() + self.wait_seconds
        while True:
            if order is not None and order.get("status") in FINAL:
                return order
            if time.time() >= deadline:
                raise ExchangeError("order %s not confirmed yet; will check it at the next run" % order_id)
            self.sleep(2)
            try:
                found = self._lookup(order_id)
            except (ExchangeError, OSError):
                continue
            if found is None:
                continue  # not visible yet; if it never appears, the next run's check settles it
            order = found

    def _filled(self, order):
        qty = float(order.get("total_quantity", 0)) - float(order.get("remaining_quantity", 0))
        return max(qty, 0.0), float(order.get("avg_price") or 0), float(order.get("fee_amount") or 0)

    def _buy_result(self, order):
        qty, avg, fee = self._filled(order)
        return qty, avg, qty * avg + fee  # the fee on rupee markets is charged in rupees

    def _sell_result(self, order):
        """(rupees received, coins sold, coins sent). Rupees are after the fee and
        the 1% TDS CoinDCX withholds on sales. A rejected order sold nothing."""
        qty, avg, fee = self._filled(order)
        got = qty * avg - fee - qty * avg * self.cfg.get("tds_rate", 0.0)
        return got, qty, float(order.get("total_quantity", qty))

    def buy(self, symbol, quote_amount, order_id):
        """Returns (coins received, average price, rupees spent). Coins is 0 if unfilled."""
        info = self.client.symbol_info(symbol)
        ask = self.client.buy_price(symbol)
        if not ask > 0:
            raise ExchangeError("no valid price for %s right now; not buying" % symbol)
        budget = quote_amount / (1 + self.cfg["fee_rate"] + self.cfg["slippage"])
        qty = floor_to_step(floor_to_step(budget / ask, info["step"]), 10 ** -info["qty_precision"])
        if float(qty) < info["min_qty"] or float(qty) * ask < info["min_notional"]:
            raise ExchangeError("400 %s INR is too little to buy %s" % (quote_amount, symbol), 400)
        order = self._place_and_wait(order_id, side="buy", order_type="market_order", market=symbol,
                                     total_quantity=qty)
        return self._buy_result(order)

    def sell(self, symbol, qty, order_id):
        info = self.client.symbol_info(symbol)
        held = self.client.balances().get(info["base"], 0.0)
        q = floor_to_step(floor_to_step(min(qty, held), info["step"]), 10 ** -info["qty_precision"])
        if float(q) < info["min_qty"]:
            return 0.0, 0.0, float(q)
        order = self._place_and_wait(order_id, side="sell", order_type="market_order", market=symbol,
                                     total_quantity=q)
        return self._sell_result(order)

    def _recover(self, order_id):
        order = self._lookup(order_id)
        if order is not None and order.get("status") not in FINAL:
            raise ExchangeError("order %s is still being filled; will check again" % order_id)
        return order

    def recover_buy(self, symbol, order_id):
        order = self._recover(order_id)
        return None if order is None else self._buy_result(order)

    def recover_sell(self, symbol, order_id):
        order = self._recover(order_id)
        return None if order is None else self._sell_result(order)
