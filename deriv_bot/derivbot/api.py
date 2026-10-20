"""Async client for Deriv's WebSocket API (v3) with reconnection and rate-limit handling."""

from __future__ import annotations

import asyncio
import contextlib
import itertools
import json
import logging
from collections.abc import Awaitable, Callable
from typing import Any

from websockets.asyncio.client import connect as ws_connect
from websockets.exceptions import ConnectionClosed, InvalidHandshake, InvalidStatus

from .config import ApiConfig

log = logging.getLogger(__name__)

JSON = dict[str, Any]
ConnectFn = Callable[[str], Awaitable[Any]]
SleepFn = Callable[[float], Awaitable[None]]

AUTH_ERROR_CODES = frozenset({
    "InvalidToken", "AuthorizationRequired", "PermissionDenied", "InvalidAppID",
    "DisabledClient", "AccountDisabled", "SelfExclusion",
})
RATE_LIMIT_CODES = frozenset({"RateLimit", "TooManyRequests"})


class DerivAPIError(Exception):
    def __init__(self, code: str, message: str, msg_type: str | None = None) -> None:
        super().__init__(f"[{code}] {message}")
        self.code = code
        self.message = message
        self.msg_type = msg_type


class AuthorizationError(DerivAPIError):
    """Token invalid/missing scope. Not retryable: the kill switch should fire."""


class RateLimitError(DerivAPIError):
    """Too many requests; retried with backoff."""


class ConnectionLostError(ConnectionError):
    """WebSocket unavailable after all reconnection attempts (or mid-request)."""


def _default_connect(url: str) -> Awaitable[Any]:
    conn: Awaitable[Any] = ws_connect(
        url, ping_interval=20, ping_timeout=20, open_timeout=15, max_size=2**22)
    return conn


def describe(exc: BaseException) -> str:
    """Short, log-friendly description of a connection error."""
    if isinstance(exc, InvalidStatus):
        return f"handshake rejected with HTTP {exc.response.status_code}"
    return f"{type(exc).__name__}: {exc}" if str(exc) else type(exc).__name__


def raise_for_error(msg: JSON) -> None:
    err = msg.get("error")
    if not err:
        return
    code = str(err.get("code", "UnknownError"))
    text = str(err.get("message", ""))
    mtype = msg.get("msg_type")
    if code in AUTH_ERROR_CODES:
        raise AuthorizationError(code, text, mtype)
    if code in RATE_LIMIT_CODES:
        raise RateLimitError(code, text, mtype)
    raise DerivAPIError(code, text, mtype)


class DerivClient:
    def __init__(
        self,
        cfg: ApiConfig,
        token: str | None = None,
        *,
        connect: ConnectFn = _default_connect,
        sleep: SleepFn = asyncio.sleep,
    ) -> None:
        self.cfg = cfg
        self._token = token
        self._connect_fn = connect
        self._sleep = sleep
        self._ws: Any = None
        self._reader: asyncio.Task[None] | None = None
        self._pending: dict[int, asyncio.Future[JSON]] = {}
        self._ids = itertools.count(1)
        self._lock = asyncio.Lock()
        self.authorized: JSON | None = None
        self.reconnects = 0

    # --- connection management ------------------------------------------
    @property
    def connected(self) -> bool:
        return self._ws is not None and self._reader is not None and not self._reader.done()

    async def connect(self) -> None:
        """Open the socket (with retries) and authorize if a token was given."""
        async with self._lock:
            await self._connect_with_retries()

    async def _connect_with_retries(self) -> None:
        last: BaseException | None = None
        for attempt in range(self.cfg.max_retries + 1):
            try:
                await self._open()
                if self._token:
                    msg = await self._request_once({"authorize": self._token})
                    self.authorized = msg["authorize"]
                    log.info("Authorized as %s (virtual=%s)", self.authorized.get("loginid"),
                             self.authorized.get("is_virtual"))
                return
            except AuthorizationError:
                await self._drop()
                raise
            except (OSError, asyncio.TimeoutError, ConnectionClosed, InvalidHandshake,
                    ConnectionLostError) as exc:
                last = exc
                await self._drop()
                if attempt >= self.cfg.max_retries:
                    break
                delay = min(self.cfg.reconnect_base_delay * 2**attempt,
                            self.cfg.reconnect_max_delay)
                log.warning("Connect attempt %d failed (%s); retrying in %.1fs",
                            attempt + 1, describe(exc), delay)
                await self._sleep(delay)
        raise ConnectionLostError(
            f"could not connect to {self.cfg.endpoint} after "
            f"{self.cfg.max_retries + 1} attempts: {describe(last) if last else '?'}")

    async def _open(self) -> None:
        log.debug("Connecting to %s", self.cfg.endpoint)
        self._ws = await asyncio.wait_for(self._connect_fn(self.cfg.url),
                                          self.cfg.request_timeout)
        self._reader = asyncio.create_task(self._read_loop())

    async def _drop(self) -> None:
        ws, self._ws = self._ws, None
        reader, self._reader = self._reader, None
        if reader and not reader.done():
            reader.cancel()
            with contextlib.suppress(asyncio.CancelledError, Exception):
                await reader
        if ws is not None:
            with contextlib.suppress(Exception):
                await ws.close()
        self._fail_pending(ConnectionLostError("connection dropped"))

    async def close(self) -> None:
        await self._drop()

    def _fail_pending(self, exc: BaseException) -> None:
        pending, self._pending = self._pending, {}
        for fut in pending.values():
            if not fut.done():
                fut.set_exception(exc)

    async def _read_loop(self) -> None:
        try:
            async for raw in self._ws:
                try:
                    msg = json.loads(raw)
                except (TypeError, ValueError):
                    log.warning("Discarding non-JSON message: %r", raw[:200])
                    continue
                req_id = msg.get("req_id")
                fut = self._pending.pop(req_id, None) if isinstance(req_id, int) else None
                if fut is not None and not fut.done():
                    fut.set_result(msg)
                else:
                    log.debug("Unsolicited message: %s", msg.get("msg_type"))
        except ConnectionClosed as exc:
            log.warning("WebSocket closed: %s", exc)
        except asyncio.CancelledError:
            raise
        except Exception:  # pragma: no cover - defensive
            log.exception("Reader crashed")
        finally:
            self._fail_pending(ConnectionLostError("connection closed"))

    # --- requests ----------------------------------------------------------
    async def _request_once(self, payload: JSON) -> JSON:
        if self._ws is None:
            raise ConnectionLostError("not connected")
        req_id = next(self._ids)
        fut: asyncio.Future[JSON] = asyncio.get_running_loop().create_future()
        self._pending[req_id] = fut
        try:
            await self._ws.send(json.dumps({**payload, "req_id": req_id}))
            msg = await asyncio.wait_for(fut, self.cfg.request_timeout)
        except ConnectionClosed as exc:
            raise ConnectionLostError(str(exc)) from exc
        finally:
            self._pending.pop(req_id, None)
        raise_for_error(msg)
        return msg

    async def request(self, payload: JSON, *, idempotent: bool = True) -> JSON:
        """Send a request and return the response, transparently reconnecting.

        Non-idempotent requests (buy/sell) are never re-sent after a connection
        failure because the server may already have executed them.
        """
        attempt = 0
        while True:
            try:
                if not self.connected:
                    async with self._lock:
                        if not self.connected:
                            self.reconnects += 1
                            log.warning("Reconnecting (#%d)...", self.reconnects)
                            await self._connect_with_retries()
                return await self._request_once(payload)
            except RateLimitError as exc:
                attempt += 1
                if attempt > self.cfg.max_retries:
                    raise
                delay = self.cfg.rate_limit_backoff * attempt
                log.warning("Rate limited (%s); backing off %.1fs", exc.message, delay)
                await self._sleep(delay)
            except (ConnectionLostError, asyncio.TimeoutError, OSError) as exc:
                await self._drop()
                if not idempotent:
                    raise ConnectionLostError(
                        f"connection failed during non-idempotent request "
                        f"{next(iter(payload))!r}; outcome unknown: {describe(exc)}") from exc
                attempt += 1
                if attempt > self.cfg.max_retries:
                    raise ConnectionLostError(
                        f"request failed after retries: {describe(exc)}") from exc
                delay = min(self.cfg.reconnect_base_delay * 2 ** (attempt - 1),
                            self.cfg.reconnect_max_delay)
                log.warning("Request failed (%s); retrying in %.1fs", describe(exc), delay)
                await self._sleep(delay)

    # --- typed helpers -----------------------------------------------------
    async def ping(self) -> bool:
        return (await self.request({"ping": 1})).get("ping") == "pong"

    async def get_balance(self) -> tuple[float, str]:
        b = (await self.request({"balance": 1}))["balance"]
        return float(b["balance"]), str(b["currency"])

    async def get_candles(self, symbol: str, granularity: int, count: int) -> list[JSON]:
        msg = await self.request({
            "ticks_history": symbol, "end": "latest", "count": count,
            "style": "candles", "granularity": granularity, "adjust_start_time": 1,
        })
        return list(msg.get("candles", []))

    async def get_ticks(
        self, symbol: str, *, end: int | str = "latest", count: int = 1, start: int | None = None
    ) -> list[tuple[int, float]]:
        payload: JSON = {"ticks_history": symbol, "end": end, "count": count, "style": "ticks"}
        if start is not None:
            payload["start"] = start
        hist = (await self.request(payload)).get("history", {})
        return [(int(t), float(p)) for t, p in
                zip(hist.get("times", []), hist.get("prices", []), strict=False)]

    async def get_proposal(
        self, *, symbol: str, contract_type: str, amount: float, currency: str,
        duration: int, duration_unit: str,
    ) -> JSON:
        msg = await self.request({
            "proposal": 1, "amount": amount, "basis": "stake", "contract_type": contract_type,
            "currency": currency, "duration": duration, "duration_unit": duration_unit,
            "symbol": symbol,
        })
        return dict(msg["proposal"])

    async def buy(self, proposal_id: str, price: float) -> JSON:
        msg = await self.request({"buy": proposal_id, "price": price}, idempotent=False)
        return dict(msg["buy"])

    async def get_contract(self, contract_id: int | str) -> JSON:
        msg = await self.request({"proposal_open_contract": 1, "contract_id": int(contract_id)})
        return dict(msg["proposal_open_contract"])

    async def sell(self, contract_id: int | str, price: float = 0) -> JSON:
        msg = await self.request({"sell": int(contract_id), "price": price}, idempotent=False)
        return dict(msg["sell"])
