"""End-to-end test trade: signal -> risk -> proposal -> simulated execution -> logging -> P/L.

Always runs in PAPER mode, so no buy request is ever sent.
"""

from __future__ import annotations

import asyncio
import dataclasses
import json
import logging
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .api import DerivClient
from .bot import TradingBot
from .config import Config
from .database import TradeDatabase
from .executor import PaperExecutor, Settlement
from .risk import RiskManager
from .strategy import Candle, EmaCrossoverStrategy, Signal, closed_candles

log = logging.getLogger(__name__)

HINTS = {
    "connect": "Check internet access / firewall / proxy (WebSocket upgrades must be allowed) "
               "and that api.endpoint and api.app_id are correct.",
    "market_data": "Check trading.symbol is valid and the market is open "
                   "(synthetic indices trade 24/7; forex does not trade on weekends).",
    "risk": "Balance may be too small for min_stake at the configured risk %, or a risk "
            "limit (daily loss / loss streak / kill-switch file) is active.",
    "proposal": "The contract may be unavailable for this symbol/duration. Try "
                "duration_unit 'm' or a different symbol.",
    "settlement": "No exit tick arrived in time. Check connectivity and contract duration.",
    "verify": "Database write or P/L aggregation mismatch - see traceback.",
}


@dataclass
class StepResult:
    name: str
    ok: bool
    detail: str


@dataclass
class E2EResult:
    success: bool = False
    endpoint: str = ""
    steps: list[StepResult] = field(default_factory=list)
    trade: dict[str, Any] | None = None
    error: str | None = None
    failed_step: str | None = None
    hint: str | None = None
    traceback: str | None = None
    started_at: str = ""
    finished_at: str = ""

    def add(self, name: str, detail: str) -> None:
        self.steps.append(StepResult(name, True, detail))
        log.info("[E2E] %s: %s", name, detail)

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self), indent=2, default=str)


def pick_signal(strategy: EmaCrossoverStrategy, candles: list[Candle]) -> tuple[Signal, str]:
    """Use a fresh crossover if present; otherwise the most recent one in the window
    (clearly labelled), otherwise the current EMA alignment. The e2e test must
    always produce exactly one trade, so it cannot wait indefinitely for a cross."""
    sig = strategy.evaluate(candles)
    if sig:
        return sig, "live crossover on latest closed candle"
    last = strategy.last_crossover(candles)
    if last:
        s, ago = last
        c = candles[-1]
        return (Signal(s.direction, c.epoch, c.close, s.fast_ema, s.slow_ema,
                       f"{s.reason} {ago} candle(s) ago"),
                f"most recent crossover ({ago} candles ago) - no fresh cross right now")
    trend = strategy.trend(candles)
    if trend is None:
        raise RuntimeError("not enough candles to compute EMAs")
    c = candles[-1]
    return (Signal(trend, c.epoch, c.close, float("nan"), float("nan"),
                   "EMA alignment (no crossover in window)"),
            "EMA alignment fallback - no crossover in window")


async def run_e2e(
    cfg: Config,
    client: DerivClient,
    db: TradeDatabase,
    *,
    duration: int,
    duration_unit: str,
    settle_timeout: float | None = None,
    poll: float = 1.0,
) -> E2EResult:
    res = E2EResult(endpoint=cfg.api.endpoint,
                    started_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    trading = dataclasses.replace(cfg.trading, contract_duration=duration,
                                  duration_unit=duration_unit)
    executor = PaperExecutor(client, db, trading, cfg.paper.starting_balance)
    strategy = EmaCrossoverStrategy(cfg.strategy)
    risk = RiskManager(cfg.risk)
    step = "connect"
    try:
        await client.connect()
        auth = client.authorized
        res.add("connect", f"connected to {cfg.api.endpoint}; "
                + (f"authorized {auth.get('loginid')} (virtual={auth.get('is_virtual')})"
                   if auth else "no token - unauthenticated paper mode"))

        step = "market_data"
        s = cfg.strategy
        raw = await client.get_candles(trading.symbol, s.granularity, s.candle_count + 1)
        candles = closed_candles(
            [Candle(int(c["epoch"]), float(c["open"]), float(c["high"]), float(c["low"]),
                    float(c["close"])) for c in raw], s.granularity, time.time())
        if len(candles) < strategy.min_candles:
            raise RuntimeError(f"only {len(candles)} closed candles; need {strategy.min_candles}")
        res.add("market_data", f"{len(candles)} closed {s.granularity}s candles for "
                f"{trading.symbol}; last close {candles[-1].close}")

        step = "signal"
        signal, source = pick_signal(strategy, candles)
        res.add("signal", f"{signal.direction.value} - {signal.reason} [{source}]")

        step = "risk"
        balance_before, currency = await executor.balance()
        db_before = db.realized_pnl("paper")
        snap = await TradingBot(cfg, client, db, executor, strategy, risk).snapshot()
        decision = risk.check(snap, datetime.now(timezone.utc))
        if not decision.allowed:
            raise RuntimeError(f"risk engine blocked the trade: {decision.reason}")
        stake = risk.calculate_stake(snap.balance)
        res.add("risk", f"paper balance {balance_before:.2f} {currency}; "
                f"risk {cfg.risk.risk_per_trade_pct}% -> stake {stake:.2f}")

        step = "proposal"
        trade = await executor.open_trade(signal, stake, s.name)
        res.add("proposal", f"proposal priced; simulated execution logged as trade "
                f"#{trade.id}: {trade.direction} stake {trade.stake:.2f} payout "
                f"{trade.payout:.2f} entry {trade.entry_price} "
                f"({duration}{duration_unit})")

        step = "settlement"
        timeout = settle_timeout or (duration * {"t": 3, "s": 1, "m": 60, "h": 3600}
                                     [duration_unit] + 60)
        deadline = time.monotonic() + timeout
        settlement: Settlement | None = None
        while settlement is None:
            if time.monotonic() > deadline:
                raise TimeoutError(f"trade not settled within {timeout:.0f}s")
            await asyncio.sleep(poll)
            fresh = db.get_trade(trade.id)
            assert fresh is not None
            settlement = await executor.check_trade(fresh)
        res.add("settlement", f"{'WON' if settlement.won else 'LOST'}: entry "
                f"{settlement.entry_price} exit {settlement.exit_price} "
                f"P/L {settlement.pnl:+.2f}")

        step = "verify"
        rec = db.get_trade(trade.id)
        assert rec is not None and rec.status in ("won", "lost"), "trade not closed in DB"
        assert rec.pnl is not None and abs(rec.pnl - settlement.pnl) < 1e-9, "P/L mismatch"
        delta = db.realized_pnl("paper") - db_before
        assert abs(delta - settlement.pnl) < 1e-6, f"realized P/L moved {delta}, expected pnl"
        balance_after, _ = await executor.balance()
        assert abs(balance_after - (balance_before + settlement.pnl)) < 0.011, \
            "paper balance not updated by trade P/L"
        st = db.stats("paper", cfg.paper.starting_balance)
        res.add("verify", f"DB row #{rec.id} status={rec.status} pnl={rec.pnl:+.2f}; "
                f"balance {balance_before:.2f} -> {balance_after:.2f}; total realized "
                f"{st.realized_pnl:+.2f}, win rate {st.win_rate:.1f}% over "
                f"{st.wins + st.losses} closed paper trade(s)")
        res.trade = dataclasses.asdict(rec)
        res.success = True
    except Exception as exc:
        res.success = False
        res.failed_step = step
        res.error = f"{type(exc).__name__}: {exc}"
        res.hint = HINTS.get(step, "")
        res.traceback = traceback.format_exc()
        res.steps.append(StepResult(step, False, res.error))
        log.error("[E2E] FAILED at %s: %s", step, res.error)
    finally:
        await client.close()
        res.finished_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return res


def save_result(res: E2EResult, path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(res.to_json(), encoding="utf-8")
