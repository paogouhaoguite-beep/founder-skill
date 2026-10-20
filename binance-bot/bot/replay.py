"""Replay real historical candles through the real Trader, one candle at a time.

This is how to see in minutes what weeks of paper trading would show: the
bot re-learns on schedule, only ever sees candles that had closed at that
moment, pays fees and slippage, and a stop-loss fills when a candle's low
trades through it (as the resting exchange stop order would).
"""

from .binance import PaperBroker
from .trader import Trader


class ReplayClient:
    def __init__(self, history):
        self.history = history
        self.now_ms = 0

    def _closed_count(self, symbol):
        cs, lo, hi = self.history[symbol], 0, len(self.history[symbol])
        while lo < hi:
            mid = (lo + hi) // 2
            if cs[mid]["close_time"] < self.now_ms:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def closed_klines(self, symbol, interval, total):
        n = self._closed_count(symbol)
        return self.history[symbol][max(0, n - total):n]

    def current(self, symbol):
        n = self._closed_count(symbol)
        return self.history[symbol][n - 1] if n else None

    def price(self, symbol):
        return self.current(symbol)["c"]

    def symbol_info(self, symbol):
        return {"min_notional": 5.0}


class ReplayBroker(PaperBroker):
    def stop_fill(self, position, last_price):
        c = self.client.current(position["symbol"])
        if c["l"] > position["stop"]:
            return None
        fill = min(c["o"], position["stop"])
        proceeds = position["qty"] * fill * (1 - self.cfg["slippage"]) * (1 - self.cfg["fee_rate"])
        self.state["paper_cash"] += proceeds
        return proceeds


def simulate(history, cfg, warmup_candles, log=lambda *_: None):
    """Returns (state, equity_curve). equity_curve is a list of (time_ms, equity)."""
    client = ReplayClient(history)
    state = {}
    trader = Trader(cfg, client, ReplayBroker(client, cfg, state), state, log=log)
    timeline = sorted({c["close_time"] + 1 for cs in history.values() for c in cs})
    curve = []
    for t in timeline[warmup_candles:]:
        client.now_ms = t
        trader.step(now=t / 1000)
        curve.append((t, trader.equity()))
        if state["halted"]:
            break
    return state, curve
