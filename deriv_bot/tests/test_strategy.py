import math

import pytest

from derivbot.config import StrategyConfig
from derivbot.strategy import Candle, Direction, EmaCrossoverStrategy, ema


def candles_from(closes, start=0, g=60):
    return [Candle(start + i * g, c, c, c, c) for i, c in enumerate(closes)]


def make(fast=3, slow=5, gap=0.0):
    return EmaCrossoverStrategy(StrategyConfig(fast_period=fast, slow_period=slow,
                                               candle_count=20, min_ema_gap_pct=gap))


def test_ema_matches_hand_calculation():
    out = ema([1, 2, 3, 4, 5], 3)
    assert math.isnan(out[0]) and math.isnan(out[1])
    assert out[2] == pytest.approx(2.0)          # SMA seed
    assert out[3] == pytest.approx(3.0)          # 4*0.5 + 2*0.5
    assert out[4] == pytest.approx(4.0)


def test_ema_short_input_and_bad_period():
    assert all(math.isnan(v) for v in ema([1, 2], 3))
    with pytest.raises(ValueError):
        ema([1, 2, 3], 0)


def test_call_on_bullish_cross():
    closes = [10.0] * 8 + [9.0, 8.5, 8.0, 8.0, 12.0]
    sig = make().evaluate(candles_from(closes))
    assert sig is not None and sig.direction is Direction.CALL
    assert sig.candle_epoch == 12 * 60 and sig.price == 12.0
    assert sig.fast_ema > sig.slow_ema


def test_put_on_bearish_cross():
    closes = [10.0] * 8 + [11.0, 11.5, 12.0, 12.0, 8.0]
    sig = make().evaluate(candles_from(closes))
    assert sig is not None and sig.direction is Direction.PUT
    assert sig.fast_ema < sig.slow_ema


def test_no_signal_in_steady_trend():
    closes = [float(i) for i in range(1, 30)]
    assert make().evaluate(candles_from(closes)) is None


def test_no_signal_with_too_few_candles():
    assert make().evaluate(candles_from([1.0, 2.0, 3.0])) is None


def test_crossover_only_fires_on_the_crossing_candle():
    closes = [10.0] * 8 + [9.0, 8.5, 8.0, 8.0, 12.0, 13.0]
    assert make().evaluate(candles_from(closes)) is None  # cross was one candle earlier


def test_gap_filter_blocks_marginal_cross():
    closes = [10.0] * 8 + [9.99, 9.98, 9.97, 9.97, 10.01]
    assert make().evaluate(candles_from(closes)) is not None
    assert make(gap=1.0).evaluate(candles_from(closes)) is None


def test_last_crossover_and_trend():
    closes = [10.0] * 8 + [9.0, 8.5, 8.0, 8.0, 12.0, 13.0, 14.0]
    s = make()
    found = s.last_crossover(candles_from(closes))
    assert found is not None
    sig, ago = found
    assert sig.direction is Direction.CALL and ago == 2
    assert s.trend(candles_from(closes)) is Direction.CALL
    assert s.last_crossover(candles_from([float(i) for i in range(1, 30)])) is None


def test_invalid_periods():
    with pytest.raises(ValueError):
        EmaCrossoverStrategy(StrategyConfig(fast_period=21, slow_period=9))
