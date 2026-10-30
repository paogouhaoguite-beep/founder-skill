"""Alpaca's Trading API v2 over HTTPS, standard library only.

Paper by default: https://paper-api.alpaca.markets. The live endpoint is used
only when the bot was started with --live AND trader/config.json says
"paper": false (bot.py checks both before it builds this client).
Keys come from the environment, never from a file the bot writes:
ALPACA_API_KEY and ALPACA_SECRET_KEY."""

import json
import os
import urllib.error
import urllib.parse
import urllib.request

PAPER_URL = "https://paper-api.alpaca.markets"
LIVE_URL = "https://api.alpaca.markets"


class BrokerError(Exception):
    pass


def order_body(tool_input, client_order_id=None):
    """trader-broker's place_stock_order arguments -> the REST /v2/orders body.
    The MCP tool takes flat bracket fields; REST nests them."""
    t = dict(tool_input)
    body = {k: t.pop(k) for k in ("symbol", "side", "qty", "notional", "type", "time_in_force", "limit_price",
                                  "stop_price", "trail_price", "trail_percent", "extended_hours", "order_class")
            if k in t}
    if "take_profit_limit_price" in t:
        body["take_profit"] = {"limit_price": t.pop("take_profit_limit_price")}
    if "stop_loss_stop_price" in t:
        body["stop_loss"] = {"stop_price": t.pop("stop_loss_stop_price")}
        if "stop_loss_limit_price" in t:
            body["stop_loss"]["limit_price"] = t.pop("stop_loss_limit_price")
    cid = t.pop("client_order_id", None) or client_order_id
    if cid:
        body["client_order_id"] = cid
    return body


class Alpaca(object):
    def __init__(self, key=None, secret=None, paper=True, base_url=None, timeout=20):
        self.key = key or os.environ.get("ALPACA_API_KEY", "")
        self.secret = secret or os.environ.get("ALPACA_SECRET_KEY", "")
        if not self.key or not self.secret:
            raise BrokerError("set ALPACA_API_KEY and ALPACA_SECRET_KEY in the environment "
                              "(paper keys from the Alpaca dashboard)")
        self.paper = paper
        self.base_url = (base_url or (PAPER_URL if paper else LIVE_URL)).rstrip("/")
        self.timeout = timeout

    def _call(self, method, path, body=None, query=None):
        url = self.base_url + path + ("?" + urllib.parse.urlencode(query) if query else "")
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "APCA-API-KEY-ID": self.key, "APCA-API-SECRET-KEY": self.secret,
            "Content-Type": "application/json", "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                raw = r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            raise BrokerError("Alpaca %s %s: HTTP %d %s" % (method, path, e.code, detail))
        except (urllib.error.URLError, OSError) as e:
            raise BrokerError("Alpaca %s %s: %s" % (method, path, e))
        return json.loads(raw) if raw.strip() else None

    def account(self):
        return self._call("GET", "/v2/account")

    def clock(self):
        return self._call("GET", "/v2/clock")

    def place(self, tool_input, client_order_id=None):
        return self._call("POST", "/v2/orders", order_body(tool_input, client_order_id))

    def order(self, order_id):
        return self._call("GET", "/v2/orders/%s" % order_id, query={"nested": "true"})

    def open_orders(self, symbol):
        return self._call("GET", "/v2/orders", query={"status": "open", "symbols": symbol, "nested": "true"})

    def cancel(self, order_id):
        return self._call("DELETE", "/v2/orders/%s" % order_id)

    def position(self, symbol):
        try:
            return self._call("GET", "/v2/positions/%s" % symbol)
        except BrokerError as e:
            if "HTTP 404" in str(e):
                return None
            raise

    def close_position(self, symbol):
        return self._call("DELETE", "/v2/positions/%s" % symbol)
