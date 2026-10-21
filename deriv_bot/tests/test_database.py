from datetime import date, datetime, timedelta, timezone

import pytest

from derivbot.database import TradeDatabase

T0 = datetime(2026, 10, 19, 9, 0, tzinfo=timezone.utc)  # Monday


def add(db, pnl, when, mode="paper", stake=1.0):
    tid = db.open_trade(mode=mode, symbol="R_100", direction="CALL", stake=stake,
                        payout=stake * 1.95, entry_price=100.0, entry_epoch=0, duration=5,
                        duration_unit="m", opened_at=when)
    if pnl is not None:
        db.close_trade(tid, won=pnl > 0, pnl=pnl, exit_price=101.0, closed_at=when)
    return tid


def test_open_and_close_trade_roundtrip(db):
    tid = add(db, None, T0)
    t = db.get_trade(tid)
    assert t.status == "open" and t.pnl is None and t.closed_at is None
    db.update_unrealized(tid, 0.95)
    assert db.get_trade(tid).unrealized_pnl == 0.95
    db.close_trade(tid, won=True, pnl=0.95, exit_price=101.5, closed_at=T0)
    t = db.get_trade(tid)
    assert (t.status, t.pnl, t.exit_price, t.unrealized_pnl) == ("won", 0.95, 101.5, 0)
    with pytest.raises(ValueError):
        db.close_trade(tid, won=False, pnl=-1, exit_price=1)


def test_all_required_fields_logged(db):
    tid = add(db, -1.0, T0)
    t = db.get_trade(tid)
    for f in ("opened_at", "closed_at", "symbol", "direction", "stake", "entry_price",
              "exit_price", "status", "pnl"):
        assert getattr(t, f) is not None, f


def test_stats_win_rate_profit_factor_drawdown(db):
    # equity from 100: +1 -> 101, -1 -> 100, -1 -> 99, +2 -> 101, -1 -> 100
    for i, p in enumerate([1.0, -1.0, -1.0, 2.0, -1.0]):
        add(db, p, T0 + timedelta(minutes=i))
    open_id = add(db, None, T0 + timedelta(minutes=10))
    db.update_unrealized(open_id, -1.0)
    s = db.stats("paper", 100.0)
    assert (s.wins, s.losses, s.open_trades, s.total_trades) == (2, 3, 1, 6)
    assert s.win_rate == pytest.approx(40.0)
    assert s.gross_profit == 3.0 and s.gross_loss == 3.0
    assert s.profit_factor == pytest.approx(1.0)
    assert s.realized_pnl == 0.0 and s.unrealized_pnl == -1.0 and s.total_pnl == -1.0
    assert s.max_drawdown == pytest.approx(2.0)          # 101 -> 99
    assert s.max_drawdown_pct == pytest.approx(2 / 101 * 100, abs=0.01)
    assert s.current_drawdown == pytest.approx(1.0)      # peak 101, now 100


def test_stats_empty_and_no_losses(db):
    s = db.stats("paper", 100.0)
    assert s.total_trades == 0 and s.profit_factor is None and s.win_rate == 0
    add(db, 0.95, T0)
    assert db.stats("paper", 100.0).profit_factor == float("inf")


def test_modes_are_isolated(db):
    add(db, 5.0, T0, mode="live")
    add(db, -1.0, T0, mode="paper")
    assert db.realized_pnl("live") == 5.0
    assert db.realized_pnl("paper") == -1.0


def test_daily_and_weekly_summaries(db):
    add(db, 1.0, T0)                          # Mon 19th
    add(db, -1.0, T0 + timedelta(hours=1))    # Mon 19th
    add(db, 2.0, T0 + timedelta(days=1))      # Tue 20th
    add(db, -1.0, T0 - timedelta(days=3))     # previous week (Fri 16th)
    daily = db.daily_summary("paper", 7)
    assert [d.period for d in daily] == ["2026-10-20", "2026-10-19", "2026-10-16"]
    assert daily[1].trades == 2 and daily[1].win_rate == 50.0 and daily[1].pnl == 0.0
    weekly = db.weekly_summary("paper", 4)
    assert len(weekly) == 2
    assert weekly[0].trades == 3 and weekly[0].pnl == 2.0
    assert weekly[1].pnl == -1.0


def test_risk_inputs(db):
    add(db, -1.0, T0)
    add(db, 1.0, T0 + timedelta(minutes=1))
    add(db, -1.0, T0 + timedelta(minutes=2))
    add(db, -1.0, T0 + timedelta(minutes=3))
    add(db, None, T0 + timedelta(minutes=4), stake=2.5)
    assert db.trailing_consecutive_losses("paper") == 2
    assert db.daily_realized_pnl("paper", date(2026, 10, 19)) == -2.0
    assert db.daily_realized_pnl("paper", date(2026, 10, 20)) == 0.0
    assert db.trades_opened_on("paper", date(2026, 10, 19)) == 5
    assert db.open_stakes("paper") == 2.5


def test_meta_and_file_persistence(tmp_path):
    path = tmp_path / "sub" / "t.db"
    d = TradeDatabase(path)
    d.set_meta("k", "1")
    d.set_meta("k", "2")
    add(d, 1.0, T0)
    d.close()
    d2 = TradeDatabase(path)
    assert d2.get_meta("k") == "2" and d2.get_meta("missing") is None
    assert d2.realized_pnl("paper") == 1.0
    d2.close()
