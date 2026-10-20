"""Bot orchestration: market data -> strategy -> risk gate -> execution -> settlement."""

from __future__ import annotations

import asyncio
import logging
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone

from .api import AuthorizationError, ConnectionLostError, DerivAPIError, DerivClient
from .config import Config
from .database import PerformanceStats, TradeDatabase
from .executor import Executor, Settlement, TradeRejected
from .risk import AccountSnapshot, RiskManager
from .strategy import Candle, EmaCrossoverStrategy, Signal, closed_candles

log = logging.getLogger(__name__)


class UnsafeAccountError(RuntimeError):
    """Refusing to trade: the authorized account is a real-money account."""


@dataclass
class BotState:
    mode: str
    symbol: str
    status: str = "STARTING"
    balance: float = 0.0
    currency: str = "USD"
    account: str = "-"
    last_signal: str = "-"
    message: str = ""
    halt_reason: str = ""
    iterations: int = 0
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class TradingBot:
    def __init__(
        self,
        cfg: Config,
        client: DerivClient,
        db: TradeDatabase,
        executor: Executor,
        strategy: EmaCrossoverStrategy,
        risk: RiskManager,
        *,
        clock: Callable[[], float] = time.time,
        on_update: Callable[[TradingBot], None] | None = None,
    ) -> None:
        self.cfg = cfg
        self.client = client
        self.db = db
        self.executor = executor
        self.strategy = strategy
        self.risk = risk
        self.clock = clock
        self.on_update = on_update
        self.mode = executor.mode
        self.state = BotState(mode=self.mode, symbol=cfg.trading.symbol)
        self._last_signal_epoch: int | None = None
        self._initial_balance_key = f"initial_balance_{self.mode}"

    # --- helpers -----------------------------------------------------------
    def now(self) -> datetime:
        return datetime.fromtimestamp(self.clock(), timezone.utc)

    @property
    def initial_balance(self) -> float:
        v = self.db.get_meta(self._initial_balance_key)
        return float(v) if v is not None else self.cfg.paper.starting_balance

    def performance(self) -> PerformanceStats:
        return self.db.stats(self.mode, self.initial_balance)

    async def snapshot(self) -> AccountSnapshot:
        balance, currency = await self.executor.balance()
        self.state.balance, self.state.currency = balance, currency
        today = self.now().date()
        return AccountSnapshot(
            balance=balance,
            open_stakes=self.db.open_stakes(self.mode),
            daily_realized_pnl=self.db.daily_realized_pnl(self.mode, today),
            trades_today=self.db.trades_opened_on(self.mode, today),
            open_positions=len(self.db.open_trades(self.mode)),
        )

    def _notify(self) -> None:
        if self.on_update:
            try:
                self.on_update(self)
            except Exception:  # the dashboard must never take the bot down
                log.exception("Dashboard update failed")

    # --- lifecycle ---------------------------------------------------------
    async def start(self) -> None:
        self.state.status = "CONNECTING"
        self._notify()
        await self.client.connect()
        auth = self.client.authorized
        if self.mode == "live":
            if not auth:
                raise AuthorizationError("AuthorizationRequired",
                                         "live/demo mode needs an API token", "authorize")
            if not auth.get("is_virtual") and not self.cfg.safety.allow_real_account:
                raise UnsafeAccountError(
                    f"account {auth.get('loginid')} is a REAL-money account. Use a demo "
                    "(virtual) token, or set safety.allow_real_account: true at your own risk.")
        if auth:
            kind = "demo" if auth.get("is_virtual") else "REAL"
            self.state.account = f"{auth.get('loginid')} ({kind})"
        else:
            self.state.account = "unauthenticated (paper)"
        balance, _ = await self.executor.balance()
        if self.db.get_meta(self._initial_balance_key) is None:
            self.db.set_meta(self._initial_balance_key, str(balance))
        self.risk.consecutive_losses = self.db.trailing_consecutive_losses(self.mode)
        self.state.status = "RUNNING"
        log.info("Bot started in %s mode on %s; balance %.2f", self.mode.upper(),
                 self.cfg.trading.symbol, balance)
        self._notify()

    async def fetch_candles(self) -> list[Candle]:
        s = self.cfg.strategy
        raw = await self.client.get_candles(self.cfg.trading.symbol, s.granularity,
                                            s.candle_count + 1)
        candles = [Candle(int(c["epoch"]), float(c["open"]), float(c["high"]),
                          float(c["low"]), float(c["close"])) for c in raw]
        return closed_candles(candles, s.granularity, self.clock())

    async def settle_open_trades(self) -> list[Settlement]:
        settled = []
        for trade in self.db.open_trades(self.mode):
            result = await self.executor.check_trade(trade)
            if result:
                self.risk.record_result(result.won, self.now())
                settled.append(result)
        return settled

    async def place_trade(self, signal: Signal, stake: float) -> int | None:
        try:
            rec = await self.executor.open_trade(signal, stake, self.cfg.strategy.name)
        except TradeRejected as exc:
            self.state.message = f"Trade skipped: {exc}"
            log.info(self.state.message)
            return None
        self.state.message = (f"Opened #{rec.id} {rec.direction} stake {rec.stake:.2f} "
                              f"@ {rec.entry_price}")
        self.state.balance, _ = await self.executor.balance()
        return rec.id

    async def step(self) -> None:
        """One loop iteration. Errors are classified; critical ones fire the kill switch."""
        self.state.iterations += 1
        try:
            await self.settle_open_trades()
            snap = await self.snapshot()
            decision = self.risk.check(snap, self.now())
            if not decision.allowed:
                self.state.message = decision.reason
                if self.risk.halted:
                    self.state.status = "HALTED"
                    self.state.halt_reason = self.risk.halt_reason
                elif "paused" in decision.reason:
                    self.state.status = "PAUSED"
                else:
                    self.state.status = "RUNNING"
            else:
                self.state.status = "RUNNING"
                candles = await self.fetch_candles()
                signal = self.strategy.evaluate(candles)
                if signal and signal.candle_epoch != self._last_signal_epoch:
                    self._last_signal_epoch = signal.candle_epoch
                    self.state.last_signal = (f"{signal.direction.value} @ {signal.price} "
                                              f"({signal.reason})")
                    log.info("Signal: %s", self.state.last_signal)
                    stake = self.risk.calculate_stake(snap.balance)
                    await self.place_trade(signal, stake)
                else:
                    self.state.message = "No new signal"
            self.risk.record_success()
        except AuthorizationError as exc:
            self.risk.engage_kill_switch(f"authorization error: {exc}")
        except ConnectionLostError as exc:
            self.risk.engage_kill_switch(f"connection lost: {exc}")
        except UnsafeAccountError as exc:
            self.risk.engage_kill_switch(str(exc))
        except DerivAPIError as exc:
            self.state.message = f"API error: {exc}"
            self.risk.record_error(exc)
        except Exception as exc:
            log.exception("Unexpected error in bot loop")
            self.state.message = f"Unexpected error: {exc!r}"
            self.risk.record_error(exc)
        if self.risk.halted:
            self.state.status = "HALTED"
            self.state.halt_reason = self.risk.halt_reason
        self._notify()

    async def run(self, max_iterations: int | None = None) -> None:
        try:
            await self.start()
        except (AuthorizationError, UnsafeAccountError, ConnectionLostError) as exc:
            self.risk.engage_kill_switch(f"startup failed: {exc}")
            self.state.status = "HALTED"
            self.state.halt_reason = self.risk.halt_reason
            self._notify()
            return
        try:
            while not self.risk.halted:
                await self.step()
                if max_iterations is not None and self.state.iterations >= max_iterations:
                    break
                if self.risk.halted:
                    break
                await asyncio.sleep(self.cfg.trading.poll_interval)
        finally:
            await self.shutdown()

    async def shutdown(self) -> None:
        if self.risk.halted and self.cfg.safety.close_positions_on_kill:
            try:
                await self.executor.close_all()
            except Exception:
                log.exception("close_all failed during kill switch")
        if self.state.status != "HALTED":
            self.state.status = "STOPPED"
        await self.client.close()
        log.info("Bot stopped (%s)", self.state.halt_reason or "normal shutdown")
        self._notify()
