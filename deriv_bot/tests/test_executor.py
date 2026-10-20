import dataclasses

import pytest

from derivbot.api import DerivClient
from derivbot.executor import LiveExecutor, PaperExecutor, TradeRejected, rise_fall_won
from derivbot.mock_server import DEMO_TOKEN, MockDerivServer, synthetic_price
from derivbot.strategy import Direction, Signal


def sig(direction=Direction.CALL):
    return Signal(direction, 0, 1000.0, 1.0, 0.0, "test")


@pytest.fixture
async def env(cfg, clock):
    async with MockDerivServer(clock=clock) as srv:
        api = dataclasses.replace(cfg.api, endpoint=srv.url)
        client = DerivClient(api, DEMO_TOKEN)
        await client.connect()
        yield srv, client
        await client.close()


def test_rise_fall_rules():
    assert rise_fall_won("CALL", 1.0, 1.1) and not rise_fall_won("CALL", 1.0, 0.9)
    assert rise_fall_won("PUT", 1.0, 0.9) and not rise_fall_won("PUT", 1.0, 1.1)
    assert not rise_fall_won("CALL", 1.0, 1.0) and not rise_fall_won("PUT", 1.0, 1.0)


async def test_paper_trade_never_buys_and_settles_at_expiry(cfg, db, clock, env):
    srv, client = env
    ex = PaperExecutor(client, db, cfg.trading, 100.0, clock=clock)  # 5 minute contracts
    t = await ex.open_trade(sig(), 1.0, "ema")
    assert t.status == "open" and t.stake == 1.0 and t.payout == 1.95
    assert t.entry_price == synthetic_price(int(clock()))
    assert (await ex.balance())[0] == 99.0  # stake locked
    assert await ex.check_trade(db.get_trade(t.id)) is None  # not expired yet
    clock.advance(5 * 60 + 1)
    s = await ex.check_trade(db.get_trade(t.id))
    exit_price = synthetic_price(t.entry_epoch + 300)
    assert s.exit_price == exit_price
    assert s.won == (exit_price > t.entry_price)
    assert s.pnl == (0.95 if s.won else -1.0)
    assert db.get_trade(t.id).status == ("won" if s.won else "lost")
    assert (await ex.balance())[0] == pytest.approx(100.0 + s.pnl)
    assert not any("buy" in r for r in srv.requests), "paper mode must never send buy"
    assert any("proposal" in r for r in srv.requests)


async def test_paper_tick_contract(cfg, db, clock, env):
    _, client = env
    trading = dataclasses.replace(cfg.trading, contract_duration=3, duration_unit="t")
    ex = PaperExecutor(client, db, trading, 100.0, clock=clock)
    t = await ex.open_trade(sig(Direction.PUT), 1.0, "ema")
    clock.advance(1)
    assert await ex.check_trade(db.get_trade(t.id)) is None
    assert db.get_trade(t.id).unrealized_pnl in (0.95, -1.0)  # marked to market
    clock.advance(5)
    s = await ex.check_trade(db.get_trade(t.id))
    assert s is not None and s.exit_price == synthetic_price(t.entry_epoch + 3)


async def test_low_payout_is_rejected(cfg, db, clock, env):
    srv, client = env
    srv.payout_ratio = 0.5
    ex = PaperExecutor(client, db, cfg.trading, 100.0, clock=clock)
    with pytest.raises(TradeRejected):
        await ex.open_trade(sig(), 1.0, "ema")
    assert db.open_trades("paper") == []


async def test_live_executor_buys_and_settles(cfg, db, clock, env):
    srv, client = env
    ex = LiveExecutor(client, db, cfg.trading, clock=clock)
    t = await ex.open_trade(sig(), 1.0, "ema")
    assert t.contract_id is not None and t.mode == "live"
    assert srv.balance == 999.0
    assert await ex.check_trade(db.get_trade(t.id)) is None
    assert db.get_trade(t.id).unrealized_pnl == pytest.approx(round(1.95 * 0.5, 2) - 1.0)
    clock.advance(301)
    s = await ex.check_trade(db.get_trade(t.id))
    assert s is not None and db.get_trade(t.id).status in ("won", "lost")
    assert (await ex.balance())[0] == pytest.approx(1000.0 + s.pnl)


async def test_live_close_all_sells(cfg, db, clock, env):
    srv, client = env
    ex = LiveExecutor(client, db, cfg.trading, clock=clock)
    await ex.open_trade(sig(), 1.0, "ema")
    await ex.close_all()
    assert any("sell" in r for r in srv.requests)
