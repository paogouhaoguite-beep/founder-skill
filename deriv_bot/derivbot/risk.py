"""Risk engine: position sizing, daily loss limit, loss streak pause, kill switch."""

from __future__ import annotations

import logging
import math
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

from .config import RiskConfig

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class RiskDecision:
    allowed: bool
    reason: str = ""


@dataclass(frozen=True)
class AccountSnapshot:
    """Everything the risk engine needs to judge whether a new trade is allowed."""

    balance: float  # free balance (stakes of open trades already deducted)
    open_stakes: float  # capital currently locked in open contracts
    daily_realized_pnl: float  # realized P/L of trades closed today (UTC)
    trades_today: int
    open_positions: int

    @property
    def equity(self) -> float:
        return self.balance + self.open_stakes


class RiskManager:
    def __init__(self, cfg: RiskConfig, kill_switch_file: str | Path | None = None) -> None:
        self.cfg = cfg
        self.kill_switch_file = Path(kill_switch_file) if kill_switch_file else None
        self.consecutive_losses = 0
        self.paused_until: datetime | None = None
        self.halted = False
        self.halt_reason = ""
        self.critical_errors = 0
        self.last_reset_at: datetime | None = None  # when the last cooldown ended

    # --- position sizing -------------------------------------------------
    def calculate_stake(self, balance: float) -> float:
        """Stake = balance * risk%, rounded DOWN to cents and capped at max_stake.

        For fixed-payout contracts the stake is the maximum loss, so this is the
        amount at risk. Returns 0.0 when even the minimum stake would exceed the
        risk budget: the trade is skipped rather than over-risked.
        """
        if balance <= 0:
            return 0.0
        budget = balance * self.cfg.risk_per_trade_pct / 100.0
        stake = math.floor(min(budget, self.cfg.max_stake) * 100 + 1e-9) / 100.0
        if stake < self.cfg.min_stake:
            return 0.0
        return stake

    # --- daily limit -----------------------------------------------------
    def daily_loss_headroom(self, snap: AccountSnapshot) -> float:
        """How much more can be lost today (counting open stakes as already lost)."""
        day_start_equity = snap.equity - snap.daily_realized_pnl
        limit = day_start_equity * self.cfg.daily_loss_limit_pct / 100.0
        return limit + snap.daily_realized_pnl - snap.open_stakes

    def daily_loss_limit_hit(self, snap: AccountSnapshot) -> bool:
        if snap.daily_realized_pnl >= 0:
            return False
        day_start_equity = snap.equity - snap.daily_realized_pnl
        if day_start_equity <= 0:
            return True
        loss_pct = -snap.daily_realized_pnl / day_start_equity * 100.0
        return loss_pct >= self.cfg.daily_loss_limit_pct - 1e-9

    # --- loss streak -----------------------------------------------------
    def record_result(self, won: bool, now: datetime) -> None:
        if won:
            self.consecutive_losses = 0
            return
        self.consecutive_losses += 1
        if self.consecutive_losses >= self.cfg.max_consecutive_losses:
            self.paused_until = now + timedelta(minutes=self.cfg.cooldown_minutes)
            log.warning(
                "%d consecutive losses: pausing new trades until %s",
                self.consecutive_losses, self.paused_until.isoformat(),
            )

    def restore_streak(self, losses: int, last_loss_at: datetime | None) -> None:
        """Rebuild loss-streak state after a restart so a restart cannot skip a cooldown."""
        self.consecutive_losses = losses
        if losses >= self.cfg.max_consecutive_losses and last_loss_at is not None:
            self.paused_until = last_loss_at + timedelta(minutes=self.cfg.cooldown_minutes)

    def is_paused(self, now: datetime) -> bool:
        if self.paused_until is None:
            return False
        if now >= self.paused_until:
            log.info("Loss-streak cooldown over; resuming")
            self.paused_until = None
            self.consecutive_losses = 0
            self.last_reset_at = now
            return False
        return True

    # --- kill switch -----------------------------------------------------
    def engage_kill_switch(self, reason: str) -> None:
        if not self.halted:
            log.critical("KILL SWITCH ENGAGED: %s", reason)
        self.halted = True
        self.halt_reason = reason

    def kill_file_present(self) -> bool:
        return bool(self.kill_switch_file and self.kill_switch_file.exists())

    def record_error(self, exc: BaseException) -> None:
        self.critical_errors += 1
        log.error("Error %d/%d: %r", self.critical_errors, self.cfg.max_critical_errors, exc)
        if self.critical_errors >= self.cfg.max_critical_errors:
            self.engage_kill_switch(f"{self.critical_errors} consecutive errors (last: {exc!r})")

    def record_success(self) -> None:
        self.critical_errors = 0

    # --- the gate ----------------------------------------------------------
    def check(self, snap: AccountSnapshot, now: datetime) -> RiskDecision:
        """Decide whether a new trade may be opened. May engage the kill switch."""
        if self.kill_file_present():
            self.engage_kill_switch(f"kill-switch file {self.kill_switch_file} present")
        if self.halted:
            return RiskDecision(False, f"halted: {self.halt_reason}")
        if self.daily_loss_limit_hit(snap):
            self.engage_kill_switch(
                f"daily loss limit {self.cfg.daily_loss_limit_pct}% reached "
                f"(today's P/L {snap.daily_realized_pnl:.2f})"
            )
            return RiskDecision(False, f"halted: {self.halt_reason}")
        if self.is_paused(now):
            assert self.paused_until is not None
            return RiskDecision(False, f"paused after {self.consecutive_losses} losses until "
                                       f"{self.paused_until:%H:%M:%S} UTC")
        if snap.open_positions >= self.cfg.max_open_positions:
            return RiskDecision(False, "max open positions reached")
        if snap.trades_today >= self.cfg.max_trades_per_day:
            return RiskDecision(False, "max trades per day reached")
        stake = self.calculate_stake(snap.balance)
        if stake <= 0:
            return RiskDecision(False, "balance too small for minimum stake within risk limit")
        if stake > self.daily_loss_headroom(snap) + 1e-9:
            return RiskDecision(False, "paused for today: losing the next stake could breach "
                                       "the daily loss limit")
        return RiskDecision(True)
