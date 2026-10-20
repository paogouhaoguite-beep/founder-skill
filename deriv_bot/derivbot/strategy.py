"""Rule-based signal generation: EMA crossover on closed candles."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from enum import Enum

from .config import StrategyConfig


class Direction(str, Enum):
    CALL = "CALL"  # Rise
    PUT = "PUT"  # Fall


@dataclass(frozen=True)
class Candle:
    epoch: int
    open: float
    high: float
    low: float
    close: float


@dataclass(frozen=True)
class Signal:
    direction: Direction
    candle_epoch: int
    price: float
    fast_ema: float
    slow_ema: float
    reason: str


def ema(values: Sequence[float], period: int) -> list[float]:
    """Exponential moving average seeded with the SMA of the first `period` values.

    Returns a list aligned with `values`; entries before the seed are NaN.
    """
    if period < 1:
        raise ValueError("period must be >= 1")
    out = [float("nan")] * len(values)
    if len(values) < period:
        return out
    k = 2.0 / (period + 1)
    prev = sum(values[:period]) / period
    out[period - 1] = prev
    for i in range(period, len(values)):
        prev = values[i] * k + prev * (1 - k)
        out[i] = prev
    return out


class EmaCrossoverStrategy:
    """CALL when the fast EMA crosses above the slow EMA on the latest closed candle,
    PUT when it crosses below. Optional gap filter rejects marginal crosses."""

    def __init__(self, cfg: StrategyConfig) -> None:
        if cfg.fast_period >= cfg.slow_period:
            raise ValueError("fast_period must be smaller than slow_period")
        self.cfg = cfg

    @property
    def min_candles(self) -> int:
        return self.cfg.slow_period + 1

    def _emas(self, candles: Sequence[Candle]) -> tuple[list[float], list[float]]:
        closes = [c.close for c in candles]
        return ema(closes, self.cfg.fast_period), ema(closes, self.cfg.slow_period)

    def evaluate(self, candles: Sequence[Candle]) -> Signal | None:
        """Evaluate the most recent candle in `candles` (which must all be closed)."""
        if len(candles) < self.min_candles:
            return None
        fast, slow = self._emas(candles)
        return self._cross_at(candles, fast, slow, len(candles) - 1)

    def _cross_at(
        self, candles: Sequence[Candle], fast: list[float], slow: list[float], i: int
    ) -> Signal | None:
        if i < self.cfg.slow_period:  # need slow EMA at i-1 and i
            return None
        prev_diff = fast[i - 1] - slow[i - 1]
        diff = fast[i] - slow[i]
        gap_pct = abs(diff) / slow[i] * 100 if slow[i] else 0.0
        if gap_pct < self.cfg.min_ema_gap_pct:
            return None
        c = candles[i]
        if prev_diff <= 0 < diff:
            return Signal(Direction.CALL, c.epoch, c.close, fast[i], slow[i],
                          f"EMA{self.cfg.fast_period} crossed above EMA{self.cfg.slow_period}")
        if prev_diff >= 0 > diff:
            return Signal(Direction.PUT, c.epoch, c.close, fast[i], slow[i],
                          f"EMA{self.cfg.fast_period} crossed below EMA{self.cfg.slow_period}")
        return None

    def last_crossover(self, candles: Sequence[Candle]) -> tuple[Signal, int] | None:
        """Most recent crossover in the window and how many candles ago it happened."""
        if len(candles) < self.min_candles:
            return None
        fast, slow = self._emas(candles)
        for i in range(len(candles) - 1, self.cfg.slow_period - 1, -1):
            sig = self._cross_at(candles, fast, slow, i)
            if sig:
                return sig, len(candles) - 1 - i
        return None

    def trend(self, candles: Sequence[Candle]) -> Direction | None:
        """Current EMA alignment (fast above slow = CALL)."""
        if len(candles) < self.cfg.slow_period:
            return None
        fast, slow = self._emas(candles)
        if fast[-1] > slow[-1]:
            return Direction.CALL
        if fast[-1] < slow[-1]:
            return Direction.PUT
        return None


def closed_candles(candles: Sequence[Candle], granularity: int, now_epoch: float) -> list[Candle]:
    """Drop the still-forming candle (Deriv returns it as the last element)."""
    return [c for c in candles if c.epoch + granularity <= now_epoch]
