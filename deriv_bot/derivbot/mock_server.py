"""Local Deriv-protocol simulator for tests and offline end-to-end runs.

It speaks the subset of Deriv's WebSocket API the bot uses (ping, balance,
ticks_history, proposal, buy, proposal_open_contract, sell, portfolio,
profit_table) in either protocol:

* ``new`` (default): Deriv's current Options API. A small REST endpoint serves
  ``GET /trading/v1/options/accounts`` and ``POST .../accounts/{id}/otp``; the
  WebSocket is authenticated by the single-use ``otp`` query parameter, there is
  no ``authorize`` call, and ``proposal`` requires ``underlying_symbol``.
* ``legacy``: the old v3 API with ``authorize`` and ``symbol``.

Prices come from a deterministic synthetic index: the same epoch always yields
the same price, so tests are reproducible. It never touches a real account.
"""

from __future__ import annotations

import asyncio
import dataclasses
import hashlib
import itertools
import json
import math
import time
import uuid
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import parse_qs, urlsplit

from websockets.asyncio.server import Server, ServerConnection, serve
from websockets.exceptions import ConnectionClosed

from .config import ApiConfig

JSON = dict[str, Any]
UNIT_SECONDS = {"s": 1, "m": 60, "h": 3600, "t": 1}  # simulator ticks once per second

DEMO_TOKEN = "demo-token"
REAL_TOKEN = "real-token"
MOCK_APP_ID = "mock-app"
ACCOUNTS = {  # token -> the Options accounts it can see (new protocol)
    DEMO_TOKEN: [{"account_id": "DOT90000001", "account_type": "demo"}],
    REAL_TOKEN: [{"account_id": "ROT90000001", "account_type": "real"}],
}


def synthetic_price(epoch: int, seed: str = "R_100") -> float:
    """Deterministic, trending-and-noisy price path (gives regular EMA crossovers)."""
    h = hashlib.sha256(f"{seed}:{epoch}".encode()).digest()
    noise = (int.from_bytes(h[:4], "big") / 2**32 - 0.5) * 0.6
    return round(1000 + 25 * math.sin(epoch / 900) + 9 * math.sin(epoch / 211)
                 + 3 * math.sin(epoch / 37) + noise, 2)


@dataclass
class _Contract:
    contract_id: int
    contract_type: str
    stake: float
    payout: float
    start: int
    expiry: int
    entry: float
    symbol: str
    sold: bool = False
    profit: float = 0.0
    exit: float | None = None


@dataclass
class MockDerivServer:
    protocol: str = "new"
    balance: float = 1000.0
    currency: str = "USD"
    payout_ratio: float = 0.95
    clock: Callable[[], float] = time.time
    # fault injection
    rate_limit_next: int = 0  # respond RateLimit to the next N requests
    reject_connections: int = 0  # refuse the next N handshakes (HTTP 503)
    drop_after_messages: int | None = None  # close the socket after N more messages
    lose_reply_to: str | None = None  # execute this request type, then close without replying
    rest_fail_next: int = 0  # answer the next N REST calls with HTTP 503
    requests: list[JSON] = field(default_factory=list)
    rest_calls: list[str] = field(default_factory=list)
    connections: int = 0

    _server: Server | None = None
    _rest: asyncio.Server | None = None
    _otps: dict[str, str] = field(default_factory=dict)
    _proposals: dict[str, JSON] = field(default_factory=dict)
    _contracts: dict[int, _Contract] = field(default_factory=dict)
    _ids: itertools.count[int] = field(default_factory=lambda: itertools.count(1000))

    @property
    def _ws_base(self) -> str:
        assert self._server is not None
        host, port = list(self._server.sockets)[0].getsockname()[:2]
        return f"ws://{host}:{port}"

    @property
    def url(self) -> str:
        if self.protocol == "new":
            return f"{self._ws_base}/trading/v1/options/ws/public"
        return f"{self._ws_base}/websockets/v3"

    @property
    def rest_url(self) -> str:
        assert self._rest is not None
        host, port = list(self._rest.sockets)[0].getsockname()[:2]
        return f"http://{host}:{port}"

    def api_config(self, base: ApiConfig, **overrides: Any) -> ApiConfig:
        """`base` pointed at this simulator (endpoint, REST base, protocol, app id)."""
        return dataclasses.replace(base, protocol=self.protocol, endpoint=self.url,
                                   rest_base=self.rest_url, app_id=MOCK_APP_ID, **overrides)

    async def __aenter__(self) -> MockDerivServer:
        await self.start()
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.stop()

    async def start(self) -> None:
        self._server = await serve(self._handler, "127.0.0.1", 0,
                                   process_request=self._process_request)
        self._rest = await asyncio.start_server(self._rest_handler, "127.0.0.1", 0)

    async def stop(self) -> None:
        if self._server is not None:
            self._server.close()
            await self._server.wait_closed()
            self._server = None
        if self._rest is not None:
            self._rest.close()
            await self._rest.wait_closed()
            self._rest = None

    # --- REST (new protocol login) -------------------------------------------
    async def _rest_handler(self, reader: asyncio.StreamReader,
                            writer: asyncio.StreamWriter) -> None:
        try:
            head = await reader.readuntil(b"\r\n\r\n")
            lines = head.decode("latin-1").split("\r\n")
            method, path, _ = lines[0].split(" ", 2)
            headers = {k.strip().lower(): v.strip()
                       for k, v in (ln.split(":", 1) for ln in lines[1:] if ":" in ln)}
            length = int(headers.get("content-length", "0") or 0)
            if length:
                await reader.readexactly(length)
            status, body = self._rest_route(method, path, headers)
            data = json.dumps(body).encode()
            writer.write(f"HTTP/1.1 {status} X\r\nContent-Type: application/json\r\n"
                         f"Content-Length: {len(data)}\r\nConnection: close\r\n\r\n"
                         .encode() + data)
            await writer.drain()
        finally:
            writer.close()

    @staticmethod
    def _rest_err(status: int, code: str, message: str) -> tuple[int, JSON]:
        return status, {"errors": [{"status": status, "code": code, "message": message}]}

    def _rest_route(self, method: str, path: str, headers: dict[str, str]) -> tuple[int, JSON]:
        self.rest_calls.append(f"{method} {path}")
        if self.rest_fail_next > 0:
            self.rest_fail_next -= 1
            return self._rest_err(503, "ServiceUnavailable", "try again")
        token = headers.get("authorization", "").removeprefix("Bearer ")
        if token not in ACCOUNTS:
            return self._rest_err(401, "Unauthorized", "Invalid or missing authentication")
        if headers.get("deriv-app-id") != MOCK_APP_ID:
            return self._rest_err(401, "Unauthorized",
                                  "Deriv-App-ID header is required for PAT tokens")
        accounts: list[dict[str, Any]] = [{**a, "balance": self.balance, "currency": self.currency,
                     "group": "row", "status": "active"} for a in ACCOUNTS[token]]
        if method == "GET" and path == "/trading/v1/options/accounts":
            return 200, {"data": accounts}
        parts = path.strip("/").split("/")
        if method == "POST" and len(parts) == 6 and parts[-1] == "otp":
            acct = next((a for a in accounts if a["account_id"] == parts[-2]), None)
            if acct is None:
                return self._rest_err(400, "ValidationError", "Invalid account ID format")
            otp = uuid.uuid4().hex
            self._otps[otp] = str(acct["account_type"])
            return 200, {"data": {"url": f"{self._ws_base}/trading/v1/options/ws/"
                                         f"{acct['account_type']}?otp={otp}"}}
        return self._rest_err(404, "NotFound", path)

    def _process_request(self, connection: ServerConnection, request: Any) -> Any:
        if self.reject_connections > 0:
            self.reject_connections -= 1
            return connection.respond(503, "Service Unavailable\n")
        if self.protocol == "new" and "otp=" in request.path:
            otp = parse_qs(urlsplit(request.path).query).get("otp", [""])[0]
            if self._otps.pop(otp, None) is None:  # single use, like Deriv's
                return connection.respond(401, "Invalid or missing OTP\n")
        return None

    def now(self) -> int:
        return int(self.clock())

    async def _handler(self, ws: ServerConnection) -> None:
        self.connections += 1
        # new protocol: an OTP-bearing URL (validated in _process_request) is the login
        authorized = self.protocol == "new" and "otp=" in ws.request.path if ws.request else False
        try:
            async for raw in ws:
                req: JSON = json.loads(raw)
                self.requests.append(req)
                if self.drop_after_messages is not None:
                    if self.drop_after_messages <= 0:
                        self.drop_after_messages = None
                        await ws.close()
                        return
                    self.drop_after_messages -= 1
                resp, authorized = self._dispatch(req, authorized)
                if self.lose_reply_to and self.lose_reply_to in req:
                    self.lose_reply_to = None
                    await ws.close()  # the request ran, but the client never hears back
                    return
                resp["req_id"] = req.get("req_id")
                resp.setdefault("echo_req", req)
                await ws.send(json.dumps(resp))
        except ConnectionClosed:
            pass

    @staticmethod
    def _err(msg_type: str, code: str, message: str) -> JSON:
        return {"msg_type": msg_type, "error": {"code": code, "message": message}}

    def _dispatch(self, req: JSON, authorized: bool) -> tuple[JSON, bool]:
        mtype = next((k for k in req if k not in ("req_id", "passthrough")), "unknown")
        if self.rate_limit_next > 0:
            self.rate_limit_next -= 1
            return self._err(mtype, "RateLimit", "You have reached the rate limit"), authorized
        handler = getattr(self, f"_h_{mtype}", None)
        if handler is None:
            return self._err(mtype, "UnrecognisedRequest", "Unrecognised request"), authorized
        private = ("balance", "buy", "sell", "proposal_open_contract", "portfolio", "profit_table")
        if mtype in private and not authorized:
            return self._err(mtype, "AuthorizationRequired", "Please log in."), authorized
        if mtype == "authorize":
            if self.protocol == "new":
                return self._err(mtype, "UnknownMethod", "no recognized method in request"), \
                    authorized
            resp = self._h_authorize(req)
            return resp, "error" not in resp
        result: JSON = handler(req)
        return result, authorized

    # --- handlers ----------------------------------------------------------
    def _h_ping(self, req: JSON) -> JSON:
        return {"msg_type": "ping", "ping": "pong"}

    def _h_authorize(self, req: JSON) -> JSON:
        token = req["authorize"]
        if token not in (DEMO_TOKEN, REAL_TOKEN):
            return self._err("authorize", "InvalidToken", "The token is invalid.")
        virtual = token == DEMO_TOKEN
        return {"msg_type": "authorize", "authorize": {
            "loginid": "VRTC0000001" if virtual else "CR0000001", "is_virtual": int(virtual),
            "balance": self.balance, "currency": self.currency}}

    def _h_balance(self, req: JSON) -> JSON:
        return {"msg_type": "balance",
                "balance": {"balance": round(self.balance, 2), "currency": self.currency}}

    def _h_ticks_history(self, req: JSON) -> JSON:
        sym = req["ticks_history"]
        end = self.now() if req.get("end") in (None, "latest") else int(req["end"])
        end = min(end, self.now())
        count = int(req.get("count", 5000))
        start = req.get("start")
        if req.get("style") == "candles":
            g = int(req.get("granularity", 60))
            last_bucket = end - end % g
            candles = []
            for b in range(last_bucket - (count - 1) * g, last_bucket + 1, g):
                hi = min(b + g - 1, end)
                prices = [synthetic_price(e, sym) for e in range(b, hi + 1)]
                candles.append({"epoch": b, "open": prices[0], "high": max(prices),
                                "low": min(prices), "close": prices[-1]})
            return {"msg_type": "candles", "candles": candles}
        first = end - count + 1
        if start is not None:
            first = max(first, int(start))
        times = list(range(first, end + 1))
        return {"msg_type": "history", "history": {
            "times": times, "prices": [synthetic_price(t, sym) for t in times]}}

    def _symbol(self, req: JSON) -> str | None:
        field_name = "underlying_symbol" if self.protocol == "new" else "symbol"
        value = req.get(field_name)
        return str(value) if value else None

    def _h_proposal(self, req: JSON) -> JSON:
        if self.protocol == "new" and "symbol" in req:
            return self._err("proposal", "InputValidationFailed",
                             "Input validation failed: symbol, underlying_symbol")
        sym = self._symbol(req)
        if sym is None:
            return self._err("proposal", "InputValidationFailed", "symbol is required")
        req = {**req, "symbol": sym}
        if req.get("contract_type") not in ("CALL", "PUT"):
            return self._err("proposal", "InputValidationFailed", "bad contract_type")
        amount = float(req["amount"])
        if amount < 0.35:
            return self._err("proposal", "ContractBuyValidationError", "Stake below minimum")
        now = self.now()
        pid = uuid.uuid4().hex
        payout = round(amount * (1 + self.payout_ratio), 2)
        self._proposals[pid] = {**req, "payout": payout, "spot_time": now}
        return {"msg_type": "proposal", "proposal": {
            "id": pid, "ask_price": amount, "payout": payout,
            "spot": synthetic_price(now, req["symbol"]), "spot_time": now,
            "longcode": f"Win payout if {req['symbol']} rises/falls."}}

    def _h_buy(self, req: JSON) -> JSON:
        prop = self._proposals.pop(req["buy"], None)
        if prop is None:
            return self._err("buy", "InvalidContractProposal", "Proposal expired")
        stake = float(prop["amount"])
        if stake > self.balance:
            return self._err("buy", "InsufficientBalance", "Insufficient balance")
        self.balance -= stake
        now = self.now()
        cid = next(self._ids)
        dur = int(prop["duration"]) * UNIT_SECONDS[prop["duration_unit"]]
        self._contracts[cid] = _Contract(cid, prop["contract_type"], stake, prop["payout"],
                                         now, now + dur, synthetic_price(now, prop["symbol"]),
                                         prop["symbol"])
        return {"msg_type": "buy", "buy": {
            "contract_id": cid, "buy_price": stake, "payout": prop["payout"],
            "start_time": now, "transaction_id": cid * 10, "balance_after": self.balance}}

    def _settle(self, c: _Contract, exit_price: float) -> None:
        won = exit_price > c.entry if c.contract_type == "CALL" else exit_price < c.entry
        c.sold, c.exit = True, exit_price
        c.profit = round(c.payout - c.stake, 2) if won else -c.stake
        self.balance += c.payout if won else 0.0

    def _settle_expired(self) -> None:
        for c in self._contracts.values():
            if not c.sold and self.now() >= c.expiry:
                self._settle(c, synthetic_price(c.expiry, c.symbol))

    def _h_portfolio(self, req: JSON) -> JSON:
        self._settle_expired()
        return {"msg_type": "portfolio", "portfolio": {"contracts": [
            {"contract_id": c.contract_id, "contract_type": c.contract_type,
             "buy_price": c.stake, "payout": c.payout,
             ("underlying_symbol" if self.protocol == "new" else "symbol"): c.symbol,
             "date_start": c.start, "expiry_time": c.expiry}
            for c in self._contracts.values() if not c.sold]}}

    def _h_profit_table(self, req: JSON) -> JSON:
        self._settle_expired()
        since = int(req.get("date_from", 0))
        rows = [{"contract_id": c.contract_id, "buy_price": c.stake, "payout": c.payout,
                 "sell_price": round(c.stake + c.profit, 2), "purchase_time": c.start,
                 "sell_time": c.expiry,
                 "shortcode": f"{c.contract_type}_{c.symbol}_{c.payout}_{c.start}_{c.expiry}_S0P_0"}
                for c in self._contracts.values() if c.sold and c.start >= since]
        return {"msg_type": "profit_table",
                "profit_table": {"count": len(rows), "transactions": rows}}

    def _h_proposal_open_contract(self, req: JSON) -> JSON:
        c = self._contracts.get(int(req["contract_id"]))
        if c is None:
            return self._err("proposal_open_contract", "ContractNotFound", "No such contract")
        if not c.sold and self.now() >= c.expiry:
            self._settle(c, synthetic_price(c.expiry, c.symbol))
        spot = synthetic_price(self.now(), c.symbol)
        poc: JSON = {"contract_id": c.contract_id, "buy_price": c.stake, "payout": c.payout,
                     "entry_spot": c.entry, "current_spot": spot, "is_sold": int(c.sold)}
        if c.sold:
            poc.update(status="won" if c.profit > 0 else "lost", profit=c.profit,
                       exit_tick=c.exit, sell_price=c.payout if c.profit > 0 else 0)
        else:
            poc.update(status="open", bid_price=round(c.payout * 0.5, 2))
        return {"msg_type": "proposal_open_contract", "proposal_open_contract": poc}

    def _h_sell(self, req: JSON) -> JSON:
        c = self._contracts.get(int(req["sell"]))
        if c is None or c.sold:
            return self._err("sell", "InvalidSellContractProposal", "Cannot sell")
        c.sold, c.exit = True, synthetic_price(self.now(), c.symbol)
        price = round(c.payout * 0.5, 2)
        c.profit = round(price - c.stake, 2)
        self.balance += price
        return {"msg_type": "sell", "sell": {"contract_id": c.contract_id, "sold_for": price}}

