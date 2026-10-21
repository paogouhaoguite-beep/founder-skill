import dataclasses
from datetime import datetime, timezone

import pytest
from rich.console import Console

from derivbot.api import DerivClient
from derivbot.bot import TradingBot
from derivbot.config import StrategyConfig
from derivbot.dashboard import render_dashboard, render_report
from derivbot.executor import LiveExecutor, PaperExecutor
from derivbot.mock_server import DEMO_TOKEN, REAL_TOKEN, MockDerivServer
from derivbot.risk import RiskManager
from derivbot.strategy import Direction, EmaCrossoverStrategy, Signal


class ScriptedStrategy(EmaCrossoverStrategy):
    """Returns a fixed signal (or raises) regardless of market data."""

    def __init__(self, signal=None, error=None):
        super().__init__(StrategyConfig())
        self.signal, self.error, self.calls = signal, error, 0

    def evaluate(self, candles):
        self.calls += 1
        if self.error:
            raise self.error
        return self.signal


def call_signal(epoch=1):
    return Signal(Direction.CALL, epoch, 1000.0, 1.0, 0.0, "scripted")


@pytest.fixture
async def srv(clock):
    async with MockDerivServer(clock=clock) as s:
        yield s


def make_bot(cfg, db, clock, srv, *, mode="paper", token=DEMO_TOKEN, strategy=None,
             kill_file=None, **cfg_overrides):
    cfg = dataclasses.replace(cfg, api=dataclasses.replace(cfg.api, endpoint=srv.url),
                              **cfg_overrides)
    client = DerivClient(cfg.api, token)
    ex = (PaperExecutor(client, db, cfg.trading, cfg.paper.starting_balance, clock=clock)
          if mode == "paper" else LiveExecutor(client, db, cfg.trading, clock=clock))
    return TradingBot(cfg, client, db, ex, strategy or ScriptedStrategy(call_signal()),
                      RiskManager(cfg.risk, kill_file), clock=clock)


async def test_full_paper_cycle(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv)
    await bot.start()
    assert bot.state.status == "RUNNING" and "demo" in bot.state.account
    await bot.step()
    trades = db.open_trades("paper")
    assert len(trades) == 1 and trades[0].stake == 1.0  # 1% of 100
    await bot.step()  # same candle epoch -> no duplicate trade
    assert len(db.recent_trades("paper")) == 1
    clock.advance(301)
    await bot.step()
    closed = db.closed_trades("paper")
    assert len(closed) == 1
    assert bot.risk.consecutive_losses == (0 if closed[0].status == "won" else 1)
    assert not any("buy" in r for r in srv.requests)
    await bot.shutdown()


async def test_daily_loss_limit_halts_bot(cfg, db, clock, srv):
    now = datetime.now(timezone.utc)
    for _ in range(6):
        tid = db.open_trade(mode="paper", symbol="R_100", direction="CALL", stake=1.0,
                            payout=1.95, entry_price=1.0, entry_epoch=0, duration=5,
                            duration_unit="m", opened_at=now)
        db.close_trade(tid, won=False, pnl=-1.0, exit_price=0.9, closed_at=now)
    strategy = ScriptedStrategy(call_signal())
    bot = make_bot(cfg, db, clock, srv, strategy=strategy)
    await bot.run(max_iterations=5)
    assert bot.state.status == "HALTED" and "daily loss limit" in bot.state.halt_reason
    assert strategy.calls == 0 and db.open_trades("paper") == []


async def test_loss_streak_restored_from_db(cfg, db, clock, srv):
    now = datetime.now(timezone.utc)
    for _ in range(3):
        tid = db.open_trade(mode="paper", symbol="R_100", direction="CALL", stake=0.5,
                            payout=1.0, entry_price=1.0, entry_epoch=0, duration=5,
                            duration_unit="m", opened_at=now)
        db.close_trade(tid, won=False, pnl=-0.5, exit_price=0.9, closed_at=now)
    bot = make_bot(cfg, db, clock, srv)
    await bot.start()
    assert bot.risk.consecutive_losses == 3
    await bot.shutdown()


async def test_invalid_token_engages_kill_switch(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live", token="bad")
    await bot.run(max_iterations=3)
    assert bot.state.status == "HALTED" and "InvalidToken" in bot.state.halt_reason


async def test_live_mode_requires_token(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live", token=None)
    await bot.run(max_iterations=1)
    assert bot.state.status == "HALTED" and "token" in bot.state.halt_reason


async def test_real_account_refused_by_default(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live", token=REAL_TOKEN)
    await bot.run(max_iterations=1)
    assert bot.state.status == "HALTED" and "REAL-money" in bot.state.halt_reason
    assert not any("buy" in r for r in srv.requests)


async def test_real_account_allowed_only_when_opted_in(cfg, db, clock, srv):
    safety = dataclasses.replace(cfg.safety, allow_real_account=True)
    bot = make_bot(cfg, db, clock, srv, mode="live", token=REAL_TOKEN, safety=safety)
    await bot.start()
    assert "REAL" in bot.state.account
    await bot.shutdown()


async def test_demo_live_mode_places_buy(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv, mode="live")
    await bot.start()
    await bot.step()
    assert sum(1 for r in srv.requests if "buy" in r) == 1
    assert bot.state.balance == 990.0  # 1000 - 1% stake, refreshed from the account
    await bot.shutdown()


async def test_kill_switch_file_stops_run(cfg, db, clock, srv, tmp_path):
    f = tmp_path / "KILL_SWITCH"
    f.touch()
    bot = make_bot(cfg, db, clock, srv, kill_file=f)
    await bot.run(max_iterations=10)
    assert bot.state.status == "HALTED" and bot.state.iterations == 1
    assert db.open_trades("paper") == []


async def test_repeated_errors_trip_kill_switch(cfg, db, clock, srv):
    strategy = ScriptedStrategy(error=RuntimeError("boom"))
    bot = make_bot(cfg, db, clock, srv, strategy=strategy)
    await bot.run(max_iterations=50)
    assert bot.state.status == "HALTED"
    assert strategy.calls == cfg.risk.max_critical_errors


async def test_connection_loss_trips_kill_switch(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv)
    await bot.start()
    srv.drop_after_messages = 0
    srv.reject_connections = 100
    await bot.step()
    assert bot.risk.halted and "connection lost" in bot.risk.halt_reason
    await bot.shutdown()


async def test_kill_switch_sells_open_live_positions_when_configured(cfg, db, clock, srv):
    safety = dataclasses.replace(cfg.safety, close_positions_on_kill=True)
    bot = make_bot(cfg, db, clock, srv, mode="live", safety=safety)
    await bot.start()
    await bot.step()
    bot.risk.engage_kill_switch("test")
    await bot.shutdown()
    assert any("sell" in r for r in srv.requests)


async def test_dashboard_and_report_render(cfg, db, clock, srv):
    bot = make_bot(cfg, db, clock, srv)
    await bot.start()
    await bot.step()
    con = Console(record=True, width=140)
    con.print(render_dashboard(bot))
    out = con.export_text()
    for needle in ("PAPER", "RUNNING", "Balance", "99.00", "Open Positions", "Recent Trades",
                   "Today's P/L", "Win rate", "Educational use only"):
        assert needle in out, needle
    con.print(render_report(db, "paper", 100.0))
    assert "Daily (last 7)" in con.export_text()
    await bot.shutdown()
