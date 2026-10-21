"""Regression tests for bugs found in the post-merge review."""

import dataclasses
from datetime import datetime, timedelta, timezone

import pytest

from derivbot.api import DerivClient
from derivbot.config import RiskConfig
from derivbot.database import TradeDatabase
from derivbot.executor import PaperExecutor
from derivbot.mock_server import REAL_TOKEN, MockDerivServer, synthetic_price
from derivbot.risk import AccountSnapshot, RiskManager
from derivbot.strategy import Candle, Direction, Signal, drop_forming
from tests.test_bot import ScriptedStrategy, call_signal, make_bot


def lose(db, when, mode="paper"):
    tid = db.open_trade(mode=mode, symbol="R_100", direction="CALL", stake=1.0, payout=1.95,
                        entry_price=1.0, entry_epoch=0, duration=5, duration_unit="m",
                        opened_at=when)
    db.close_trade(tid, won=False, pnl=-1.0, exit_price=0.9, closed_at=when)


@pytest.fixture
async def srv(clock):
    async with MockDerivServer(clock=clock) as s:
        yield s


# Bug 1: restarting the bot skipped the loss-streak cooldown.
async def test_restart_does_not_skip_loss_streak_cooldown(cfg, db, clock, srv):
    now = datetime.now(timezone.utc)
    for _ in range(3):
        lose(db, now)
    strategy = ScriptedStrategy(call_signal())
    bot = make_bot(cfg, db, clock, srv, strategy=strategy)
    await bot.start()
    await bot.step()
    assert bot.state.status == "PAUSED"
    assert db.open_trades("paper") == [] and strategy.calls == 0
    await bot.shutdown()


async def test_finished_cooldown_is_remembered_across_restarts(cfg, db, clock, srv):
    old = datetime.now(timezone.utc) - timedelta(hours=3)
    for _ in range(3):
        lose(db, old)
    bot = make_bot(cfg, db, clock, srv)
    await bot.start()
    await bot.step()  # cooldown (60 min) already over -> trades, and records the reset
    assert len(db.open_trades("paper")) == 1
    await bot.shutdown()
    bot2 = make_bot(cfg, db, clock, srv)
    await bot2.start()
    assert bot2.risk.consecutive_losses == 0
    await bot2.shutdown()


# Bug 2: a restart inside the same candle re-traded the same signal.
async def test_restart_does_not_retrade_same_signal(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv)
    await bot.start()
    await bot.step()
    (t,) = db.open_trades("paper")
    db.close_trade(t.id, won=True, pnl=0.95, exit_price=2.0)
    await bot.shutdown()
    bot2 = make_bot(cfg, db, clock, srv)
    await bot2.start()
    await bot2.step()
    assert db.open_trades("paper") == []
    await bot2.shutdown()


# Bug 3: a new trade could push today's loss past the daily limit.
def test_trade_blocked_when_its_max_loss_would_breach_daily_limit():
    r = RiskManager(RiskConfig(daily_loss_limit_pct=5.0))
    now = datetime.now(timezone.utc)
    # day start 100.1, limit 5.005, lost 4.6 -> 0.405 headroom < 0.95 stake
    d = r.check(AccountSnapshot(95.5, 0.0, -4.6, 5, 0), now)
    assert not d.allowed and not r.halted and "daily loss" in d.reason
    # open stake also counts against headroom
    d = r.check(AccountSnapshot(96.0, 1.0, -3.5, 5, 0), now)  # 3.5 + 1 + .96 > 5.025
    assert not d.allowed
    assert r.check(AccountSnapshot(100.0, 0.0, -1.0, 5, 0), now).allowed


# Bug 4: paper settlement trusted the local clock; a fast local clock settled early
# on a stale tick.
async def test_paper_settlement_uses_server_time_not_local_clock(cfg, db, clock, srv):
    client = DerivClient(dataclasses.replace(cfg.api, endpoint=srv.url))
    await client.connect()
    fast = lambda: clock() + 1000  # noqa: E731 - local clock 1000 s ahead of server
    ex = PaperExecutor(client, db, cfg.trading, 100.0, clock=fast)
    t = await ex.open_trade(Signal(Direction.CALL, 0, 1.0, 1.0, 0.0, "x"), 1.0, "ema")
    assert await ex.check_trade(db.get_trade(t.id)) is None  # server not at expiry yet
    clock.advance(301)
    s = await ex.check_trade(db.get_trade(t.id))
    assert s is not None and s.exit_price == synthetic_price(t.entry_epoch + 300)
    await client.close()


# Bug 5: a tick contract settled long after expiry used the wrong tick.
async def test_tick_contract_settles_correctly_after_long_downtime(cfg, db, clock, srv):
    client = DerivClient(dataclasses.replace(cfg.api, endpoint=srv.url))
    await client.connect()
    trading = dataclasses.replace(cfg.trading, contract_duration=5, duration_unit="t")
    ex = PaperExecutor(client, db, trading, 100.0, clock=clock)
    t = await ex.open_trade(Signal(Direction.PUT, 0, 1.0, 1.0, 0.0, "x"), 1.0, "ema")
    clock.advance(10_000)  # bot was down ~3 hours
    s = await ex.check_trade(db.get_trade(t.id))
    assert s is not None and s.exit_price == synthetic_price(t.entry_epoch + 5)
    await client.close()


# Bug 6: the still-forming candle was detected with the local clock; a fast clock
# let the strategy read a candle that had not closed.
def test_drop_forming_always_removes_last_candle():
    cs = [Candle(i * 60, 1, 1, 1, 1) for i in range(5)]
    assert [c.epoch for c in drop_forming(cs)] == [0, 60, 120, 180]
    assert drop_forming([]) == []


async def test_bot_ignores_forming_candle_even_with_fast_clock(cfg, db, clock, srv):
    fast = lambda: clock() + 120  # noqa: E731
    bot = make_bot(cfg, db, clock, srv)
    bot.clock = fast
    await bot.start()
    candles = await bot.fetch_candles()
    server_now = int(clock())
    assert candles[-1].epoch + 60 <= server_now  # every candle returned has closed
    await bot.shutdown()


# Bug 7: a failed startup left the WebSocket open.
async def test_failed_startup_closes_connection(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live", token=REAL_TOKEN)
    await bot.run(max_iterations=1)
    assert bot.state.status == "HALTED" and not bot.client.connected
    assert bot.client._ws is None


async def test_unexpected_startup_error_is_contained(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv)

    async def boom():
        raise RuntimeError("balance service down")

    bot.executor.balance = boom
    await bot.run(max_iterations=1)
    assert bot.state.status == "HALTED" and "balance service down" in bot.state.halt_reason
    assert not bot.client.connected


# Bug 8: weekly summary split ISO weeks at the new year (%W restarts at 00).
def test_weekly_summary_uses_iso_weeks_across_new_year():
    db = TradeDatabase(":memory:")
    for day in (datetime(2026, 12, 31, tzinfo=timezone.utc),
                datetime(2027, 1, 1, tzinfo=timezone.utc)):  # Thu + Fri, ISO 2026-W53
        lose(db, day)
    weeks = db.weekly_summary("paper", 4)
    assert [(w.period, w.trades) for w in weeks] == [("2026-W53", 2)]
    db.close()


# Bug 9: if the connection dropped during `buy`, a contract that did execute was
# never recorded. On the next start the bot must find and adopt it.
async def test_ambiguous_buy_is_reconciled_on_restart(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live")
    await bot.start()
    srv.lose_reply_to = "buy"  # buy executes, then the socket dies before replying
    await bot.step()
    assert bot.risk.halted and "outcome unknown" in bot.risk.halt_reason
    assert db.open_trades("live") == []
    await bot.shutdown()

    bot2 = make_bot(cfg, db, clock, srv, mode="live")
    await bot2.start()
    (t,) = db.open_trades("live")
    assert t.contract_id is not None and "reconciled" in (t.notes or "")
    assert "reconciled" in bot2.state.message
    clock.advance(301)
    await bot2.step()
    assert db.get_trade(t.id).status in ("won", "lost")
    await bot2.shutdown()


async def test_ambiguous_buy_already_settled_is_reconciled(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live")
    await bot.start()
    srv.lose_reply_to = "buy"
    await bot.step()
    await bot.shutdown()
    clock.advance(600)  # contract expired while the bot was down
    bot2 = make_bot(cfg, db, clock, srv, mode="live")
    await bot2.start()
    (t,) = db.closed_trades("live")
    assert t.status in ("won", "lost") and t.pnl is not None
    await bot2.shutdown()


async def test_no_reconcile_without_pending_buy(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live")
    await bot.start()
    assert not any("portfolio" in r for r in srv.requests)
    await bot.shutdown()


