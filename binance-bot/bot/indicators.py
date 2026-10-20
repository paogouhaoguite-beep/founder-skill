"""Plain-Python indicators.

Every function returns a list the same length as its input, with None wherever
there is not enough history yet.
"""


def sma(values, n):
    out = [None] * len(values)
    total = 0.0
    for i, v in enumerate(values):
        total += v
        if i >= n:
            total -= values[i - n]
        if i >= n - 1:
            out[i] = total / n
    return out


def ema(values, n):
    """Exponential moving average. Leading None values are skipped."""
    out = [None] * len(values)
    first = next((i for i, v in enumerate(values) if v is not None), None)
    if first is None or len(values) - first < n:
        return out
    k = 2.0 / (n + 1)
    prev = sum(values[first:first + n]) / n
    out[first + n - 1] = prev
    for i in range(first + n, len(values)):
        prev = values[i] * k + prev * (1 - k)
        out[i] = prev
    return out


def _rsi_value(avg_gain, avg_loss):
    if avg_loss == 0:
        return 100.0
    return 100.0 - 100.0 / (1.0 + avg_gain / avg_loss)


def rsi(closes, n):
    """Wilder's RSI."""
    out = [None] * len(closes)
    if len(closes) <= n:
        return out
    gains = losses = 0.0
    for i in range(1, n + 1):
        d = closes[i] - closes[i - 1]
        gains += max(d, 0.0)
        losses += max(-d, 0.0)
    avg_gain, avg_loss = gains / n, losses / n
    out[n] = _rsi_value(avg_gain, avg_loss)
    for i in range(n + 1, len(closes)):
        d = closes[i] - closes[i - 1]
        avg_gain = (avg_gain * (n - 1) + max(d, 0.0)) / n
        avg_loss = (avg_loss * (n - 1) + max(-d, 0.0)) / n
        out[i] = _rsi_value(avg_gain, avg_loss)
    return out


def atr(candles, n=14):
    """Wilder's Average True Range."""
    out = [None] * len(candles)
    if len(candles) < n:
        return out
    tr = []
    for i, c in enumerate(candles):
        if i == 0:
            tr.append(c["h"] - c["l"])
        else:
            pc = candles[i - 1]["c"]
            tr.append(max(c["h"] - c["l"], abs(c["h"] - pc), abs(c["l"] - pc)))
    prev = sum(tr[:n]) / n
    out[n - 1] = prev
    for i in range(n, len(candles)):
        prev = (prev * (n - 1) + tr[i]) / n
        out[i] = prev
    return out


def highest_prior(values, n):
    """Highest of the n values before index i (the current bar is excluded)."""
    out = [None] * len(values)
    for i in range(n, len(values)):
        out[i] = max(values[i - n:i])
    return out


def lowest_prior(values, n):
    """Lowest of the n values before index i (the current bar is excluded)."""
    out = [None] * len(values)
    for i in range(n, len(values)):
        out[i] = min(values[i - n:i])
    return out
