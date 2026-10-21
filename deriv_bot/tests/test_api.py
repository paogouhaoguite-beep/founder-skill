import asyncio
import dataclasses
import json
import socket

import pytest

from derivbot.api import (
    AuthorizationError,
    ConnectionLostError,
    DerivAPIError,
    DerivClient,
    RateLimitError,
    raise_for_error,
)
from derivbot.mock_server import DEMO_TOKEN, REAL_TOKEN, MockDerivServer


def api_for(cfg, url, **kw):
    return dataclasses.replace(cfg.api, endpoint=url, **kw)


@pytest.fixture
async def server():
    async with MockDerivServer() as srv:
        yield srv


async def test_connect_authorize_and_basic_calls(cfg, server):
    c = DerivClient(api_for(cfg, server.url), DEMO_TOKEN)
    await c.connect()
    try:
        assert c.authorized["is_virtual"] == 1 and c.authorized["loginid"].startswith("VRTC")
        assert await c.ping()
        bal, cur = await c.get_balance()
        assert bal == 1000.0 and cur == "USD"
        candles = await c.get_candles("R_100", 60, 30)
        assert len(candles) == 30 and {"epoch", "open", "high", "low", "close"} <= set(candles[0])
        ticks = await c.get_ticks("R_100", count=5)
        assert len(ticks) == 5 and all(isinstance(p, float) for _, p in ticks)
        sent = server.requests[1]
        assert "req_id" in sent  # every request is tagged for correlation
    finally:
        await c.close()


async def test_url_includes_app_id(cfg, server):
    c = DerivClient(api_for(cfg, server.url, app_id=4242))
    assert c.cfg.url.endswith("?app_id=4242")


async def test_invalid_token_is_authorization_error_and_not_retried(cfg, server):
    c = DerivClient(api_for(cfg, server.url), "bad-token")
    with pytest.raises(AuthorizationError) as ei:
        await c.connect()
    assert ei.value.code == "InvalidToken"
    assert server.connections == 1


async def test_auth_required_for_private_calls(cfg, server):
    c = DerivClient(api_for(cfg, server.url))
    await c.connect()
    with pytest.raises(AuthorizationError):
        await c.get_balance()
    await c.close()


async def test_rate_limit_is_retried_with_backoff(cfg, server):
    sleeps = []

    async def fake_sleep(s):
        sleeps.append(s)

    c = DerivClient(api_for(cfg, server.url), sleep=fake_sleep)
    await c.connect()
    server.rate_limit_next = 2
    assert await c.ping()
    assert len(sleeps) == 2 and sleeps[1] > sleeps[0]  # linear backoff grows
    await c.close()


async def test_rate_limit_gives_up_after_max_retries(cfg, server):
    c = DerivClient(api_for(cfg, server.url))
    await c.connect()
    server.rate_limit_next = 100
    with pytest.raises(RateLimitError):
        await c.ping()
    await c.close()


async def test_reconnects_and_reauthorizes_after_disconnect(cfg, server):
    c = DerivClient(api_for(cfg, server.url), DEMO_TOKEN)
    await c.connect()
    server.drop_after_messages = 0  # server closes the socket on the next message
    assert await c.ping()
    assert c.reconnects == 1 and server.connections == 2
    assert sum(1 for r in server.requests if "authorize" in r) == 2
    await c.close()


async def test_buy_is_never_resent_after_disconnect(cfg, server):
    c = DerivClient(api_for(cfg, server.url), DEMO_TOKEN)
    await c.connect()
    p = await c.get_proposal(symbol="R_100", contract_type="CALL", amount=1, currency="USD",
                             duration=5, duration_unit="t")
    server.drop_after_messages = 0
    with pytest.raises(ConnectionLostError, match="outcome unknown"):
        await c.buy(p["id"], p["ask_price"])
    assert sum(1 for r in server.requests if "buy" in r) == 1
    await c.close()


async def test_connect_retries_rejected_handshakes(cfg, server):
    server.reject_connections = 2
    c = DerivClient(api_for(cfg, server.url, max_retries=3), DEMO_TOKEN)
    await c.connect()
    assert c.connected
    await c.close()


async def test_connect_gives_up(cfg, server):
    server.reject_connections = 100
    c = DerivClient(api_for(cfg, server.url, max_retries=2))
    with pytest.raises(ConnectionLostError, match="3 attempts"):
        await c.connect()


async def test_unreachable_endpoint(cfg):
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    c = DerivClient(api_for(cfg, f"ws://127.0.0.1:{port}", max_retries=1))
    with pytest.raises(ConnectionLostError):
        await c.connect()


async def test_concurrent_requests_are_correlated(cfg, server):
    c = DerivClient(api_for(cfg, server.url))
    await c.connect()
    now = int(server.clock())
    ends = [now - i * 10 for i in range(10)]
    results = await asyncio.gather(*(c.get_ticks("R_100", end=e, count=1) for e in ends))
    assert [r[0][0] for r in results] == ends
    await c.close()


async def test_api_error_surfaces(cfg, server):
    c = DerivClient(api_for(cfg, server.url))
    await c.connect()
    with pytest.raises(DerivAPIError) as ei:
        await c.get_proposal(symbol="R_100", contract_type="CALL", amount=0.01,
                             currency="USD", duration=5, duration_unit="t")
    assert ei.value.code == "ContractBuyValidationError"
    await c.close()


class SilentWS:
    """Fake socket that accepts sends and never answers (simulates a hung server)."""

    def __init__(self):
        self.sent = []
        self.closed = asyncio.Event()

    async def send(self, raw):
        self.sent.append(json.loads(raw))

    async def close(self):
        self.closed.set()

    def __aiter__(self):
        return self

    async def __anext__(self):
        await self.closed.wait()
        raise StopAsyncIteration


async def test_request_timeout_triggers_reconnect_then_failure(cfg):
    sockets = []

    async def connect(url):
        ws = SilentWS()
        sockets.append(ws)
        return ws

    api = dataclasses.replace(cfg.api, request_timeout=0.05, max_retries=2)
    c = DerivClient(api, connect=connect)
    await c.connect()
    with pytest.raises(ConnectionLostError, match="after retries"):
        await c.ping()
    assert len(sockets) == 3  # initial + 2 reconnects
    await c.close()


async def test_real_account_token_reports_not_virtual(cfg, server):
    c = DerivClient(api_for(cfg, server.url), REAL_TOKEN)
    await c.connect()
    assert c.authorized["is_virtual"] == 0
    await c.close()


@pytest.mark.parametrize("code, exc", [
    ("InvalidToken", AuthorizationError),
    ("AuthorizationRequired", AuthorizationError),
    ("RateLimit", RateLimitError),
    ("MarketIsClosed", DerivAPIError),
])
def test_error_classification(code, exc):
    with pytest.raises(exc) as ei:
        raise_for_error({"msg_type": "x", "error": {"code": code, "message": "m"}})
    assert ei.value.code == code
    raise_for_error({"msg_type": "ping", "ping": "pong"})  # no error -> no raise
