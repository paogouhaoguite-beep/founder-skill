from datetime import datetime, timedelta, timezone

import pytest

from derivbot.config import RiskConfig
from derivbot.risk import AccountSnapshot, RiskManager

NOW = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)


def snap(balance=100.0, open_stakes=0.0, daily=0.0, trades=0, open_pos=0):
    return AccountSnapshot(balance, open_stakes, daily, trades, open_pos)


def rm(**kw):
    return RiskManager(RiskConfig(**kw))


@pytest.mark.parametrize("balance, pct, expected", [
    (100.0, 1.0, 1.00),
    (100.0, 2.0, 2.00),
    (57.89, 1.0, 0.57),      # rounds DOWN, never risks more than the budget
    (1234.56, 1.5, 18.51),
    (10_000.0, 2.0, 50.00),  # capped by max_stake
    (20.0, 1.0, 0.0),        # 0.20 < min_stake 0.35 -> skip, don't over-risk
    (0.0, 1.0, 0.0),
    (-5.0, 1.0, 0.0),
])
def test_position_sizing(balance, pct, expected):
    assert rm(risk_per_trade_pct=pct).calculate_stake(balance) == pytest.approx(expected)


def test_stake_never_exceeds_risk_budget():
    r = rm(risk_per_trade_pct=2.0, max_stake=1e9)
    for bal in [17.5, 33.33, 99.99, 250.01, 1000.0]:
        assert r.calculate_stake(bal) <= bal * 0.02 + 1e-9


def test_daily_loss_limit():
    r = rm(daily_loss_limit_pct=5.0)
    assert not r.daily_loss_limit_hit(snap(balance=96.0, daily=-4.0))   # 4% of 100
    assert r.daily_loss_limit_hit(snap(balance=95.0, daily=-5.0))       # exactly 5%
    assert r.daily_loss_limit_hit(snap(balance=90.0, daily=-10.0))
    assert not r.daily_loss_limit_hit(snap(balance=110.0, daily=10.0))
    # open stakes count toward equity (day-start equity = 95 + 1 + 4 = 100)
    assert not r.daily_loss_limit_hit(snap(balance=95.0, open_stakes=1.0, daily=-4.0))


def test_daily_loss_limit_engages_kill_switch():
    r = rm(daily_loss_limit_pct=5.0)
    d = r.check(snap(balance=94.0, daily=-6.0), NOW)
    assert not d.allowed and r.halted
    assert "daily loss limit" in r.halt_reason
    assert not r.check(snap(), NOW).allowed  # stays halted


def test_consecutive_losses_pause_then_resume():
    r = rm(max_consecutive_losses=3, cooldown_minutes=30)
    r.record_result(False, NOW)
    r.record_result(False, NOW)
    assert r.check(snap(), NOW).allowed
    r.record_result(False, NOW)
    d = r.check(snap(), NOW + timedelta(minutes=10))
    assert not d.allowed and "paused" in d.reason
    assert r.check(snap(), NOW + timedelta(minutes=30)).allowed
    assert r.consecutive_losses == 0


def test_win_resets_streak():
    r = rm(max_consecutive_losses=2)
    r.record_result(False, NOW)
    r.record_result(True, NOW)
    r.record_result(False, NOW)
    assert r.consecutive_losses == 1 and r.check(snap(), NOW).allowed


def test_position_and_trade_count_limits():
    r = rm(max_open_positions=1, max_trades_per_day=2)
    assert not r.check(snap(open_pos=1), NOW).allowed
    assert not r.check(snap(trades=2), NOW).allowed
    assert r.check(snap(trades=1), NOW).allowed


def test_small_balance_blocks():
    d = rm().check(snap(balance=10.0), NOW)
    assert not d.allowed and "minimum stake" in d.reason


def test_kill_switch_file(tmp_path):
    f = tmp_path / "KILL_SWITCH"
    r = RiskManager(RiskConfig(), f)
    assert r.check(snap(), NOW).allowed
    f.touch()
    assert not r.check(snap(), NOW).allowed and r.halted


def test_error_counter_triggers_kill_switch():
    r = rm(max_critical_errors=3)
    r.record_error(RuntimeError("a"))
    r.record_error(RuntimeError("b"))
    r.record_success()
    r.record_error(RuntimeError("c"))
    assert not r.halted
    r.record_error(RuntimeError("d"))
    r.record_error(RuntimeError("e"))
    assert r.halted and "consecutive errors" in r.halt_reason
