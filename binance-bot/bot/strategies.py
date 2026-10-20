"""Rule sets taken from well-known, publicly documented trading methods.

Each strategy turns a list of closed candles into two lists of booleans:
`entries[i]` means "buy at the next candle's open" and `exits[i]` means
"sell at the next candle's open". The bot only ever buys and sells spot
(no shorting, no leverage), and every trade also carries an ATR stop-loss
that the backtester and the live trader both enforce.
"""

from itertools import product

from .indicators import ema, highest_prior, lowest_prior, rsi, sma

STOP_ATR_CHOICES = (2.0, 3.0)


def _crossed_above(a, b, i):
    return None not in (a[i], b[i], a[i - 1], b[i - 1]) and a[i - 1] <= b[i - 1] and a[i] > b[i]


def _crossed_below(a, b, i):
    return None not in (a[i], b[i], a[i - 1], b[i - 1]) and a[i - 1] >= b[i - 1] and a[i] < b[i]


class Strategy:
    name = ""
    inspired_by = ""
    idea = ""
    base_grid = {}

    def grid(self):
        keys = list(self.base_grid) + ["stop_atr"]
        values = list(self.base_grid.values()) + [STOP_ATR_CHOICES]
        for combo in product(*values):
            params = dict(zip(keys, combo))
            if self.valid(params):
                yield params

    def valid(self, params):
        return True

    def signals(self, candles, p):
        raise NotImplementedError


class Turtle(Strategy):
    name = "turtle"
    inspired_by = "Richard Dennis and the Turtle Traders"
    idea = "Buy a breakout above the N-candle high, sell a break below the M-candle low."
    base_grid = {"entry_n": (20, 55), "exit_n": (10, 20)}

    def valid(self, p):
        return p["exit_n"] < p["entry_n"]

    def signals(self, candles, p):
        highs = [c["h"] for c in candles]
        lows = [c["l"] for c in candles]
        closes = [c["c"] for c in candles]
        hi = highest_prior(highs, p["entry_n"])
        lo = lowest_prior(lows, p["exit_n"])
        entries = [hi[i] is not None and closes[i] > hi[i] for i in range(len(candles))]
        exits = [lo[i] is not None and closes[i] < lo[i] for i in range(len(candles))]
        return entries, exits


class TrendEMA(Strategy):
    name = "trend_ema"
    inspired_by = "Trend followers such as Ed Seykota"
    idea = "Buy when the fast EMA crosses above the slow EMA in a long-term uptrend (price above EMA 200)."
    base_grid = {"fast": (9, 12, 20), "slow": (26, 50)}

    def signals(self, candles, p):
        closes = [c["c"] for c in candles]
        fast, slow, trend = ema(closes, p["fast"]), ema(closes, p["slow"]), ema(closes, 200)
        entries, exits = [False] * len(closes), [False] * len(closes)
        for i in range(1, len(closes)):
            up = trend[i] is not None and closes[i] > trend[i]
            entries[i] = up and _crossed_above(fast, slow, i)
            exits[i] = _crossed_below(fast, slow, i)
        return entries, exits


class RSI2(Strategy):
    name = "rsi2"
    inspired_by = "Larry Connors (RSI-2 pullback)"
    idea = "In an uptrend (price above SMA 200), buy a sharp dip when RSI(2) is very low; sell on a bounce above a short SMA."
    base_grid = {"buy_below": (5, 10, 15), "exit_sma": (5, 10)}

    def signals(self, candles, p):
        closes = [c["c"] for c in candles]
        r, trend, exit_ma = rsi(closes, 2), sma(closes, 200), sma(closes, p["exit_sma"])
        entries = [None not in (r[i], trend[i]) and closes[i] > trend[i] and r[i] < p["buy_below"]
                   for i in range(len(closes))]
        exits = [exit_ma[i] is not None and closes[i] > exit_ma[i] for i in range(len(closes))]
        return entries, exits


class MACDTrend(Strategy):
    name = "macd_trend"
    inspired_by = "Gerald Appel (MACD) with a 200 EMA trend filter"
    idea = "Buy when MACD crosses above its signal line while price is above EMA 200; sell on the opposite cross."
    base_grid = {"setting": ((12, 26, 9), (8, 21, 5))}

    def signals(self, candles, p):
        closes = [c["c"] for c in candles]
        f, s, sig = p["setting"]
        fast, slow, trend = ema(closes, f), ema(closes, s), ema(closes, 200)
        macd = [None if None in (a, b) else a - b for a, b in zip(fast, slow)]
        signal = ema(macd, sig)
        entries, exits = [False] * len(closes), [False] * len(closes)
        for i in range(1, len(closes)):
            up = trend[i] is not None and closes[i] > trend[i]
            entries[i] = up and _crossed_above(macd, signal, i)
            exits[i] = _crossed_below(macd, signal, i)
        return entries, exits


STRATEGIES = {s.name: s for s in (Turtle(), TrendEMA(), RSI2(), MACDTrend())}


def params_to_json(params):
    return {k: list(v) if isinstance(v, tuple) else v for k, v in params.items()}


def params_from_json(params):
    return {k: tuple(v) if isinstance(v, list) else v for k, v in params.items()}
