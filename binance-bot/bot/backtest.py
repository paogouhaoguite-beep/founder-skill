"""Candle-by-candle simulator used both to learn and to sanity-check strategies.

Rules that keep it honest:
- A signal on candle i is filled at the OPEN of candle i+1 (no peeking ahead).
- Every fill pays the exchange fee and slippage.
- The stop-loss is hit whenever a candle's low trades through it.
- Position size is a fraction of CURRENT equity, so profits are reinvested
  (compounded) and losses shrink the next trade automatically.
"""

from .indicators import atr


def position_quote_amount(equity, cash, price, stop, cfg):
    """How much quote currency (e.g. USDT) to spend on a new trade, or 0."""
    risk_per_unit = price - stop
    if risk_per_unit <= 0 or equity <= 0:
        return 0.0
    qty = equity * cfg["risk_per_trade"] / risk_per_unit
    amount = min(qty * price, equity * cfg["max_position_pct"], cash / (1 + cfg["fee_rate"]))
    if amount < cfg["min_notional"]:
        return 0.0
    return amount


def run(candles, strategy, params, cfg, start=0, start_equity=None):
    entries, exits = strategy.signals(candles, params)
    atr_v = atr(candles, 14)
    fee, slip = cfg["fee_rate"], cfg["slippage"]
    cash = equity = float(start_equity if start_equity is not None else cfg["start_equity"])
    start_value = cash
    qty = stop = entry_cost = 0.0
    pending_entry = pending_exit = False
    peak, max_dd = equity, 0.0
    trades = []

    def close(price):
        nonlocal cash, qty
        proceeds = qty * price * (1 - fee)
        cash += proceeds
        trades.append(proceeds - entry_cost)
        qty = 0.0

    first = max(start, 1)
    for i in range(first, len(candles)):
        c = candles[i]
        if pending_exit and qty:
            close(c["o"] * (1 - slip))
        elif pending_entry and not qty and atr_v[i - 1] is not None:
            price = c["o"] * (1 + slip)
            stop = price - params["stop_atr"] * atr_v[i - 1]
            amount = position_quote_amount(cash, cash, price, stop, cfg)
            if amount > 0:
                qty = amount / price
                entry_cost = amount * (1 + fee)
                cash -= entry_cost
        pending_entry = pending_exit = False

        if qty and c["l"] <= stop:
            close(min(c["o"], stop) * (1 - slip))

        equity = cash + qty * c["c"]
        peak = max(peak, equity)
        max_dd = max(max_dd, (peak - equity) / peak if peak else 0.0)

        if qty and exits[i]:
            pending_exit = True
        elif not qty and entries[i]:
            pending_entry = True

    wins = [t for t in trades if t > 0]
    losses = [-t for t in trades if t <= 0]
    gross_loss = sum(losses)
    window = candles[first:] or candles
    return {
        "start_equity": start_value,
        "end_equity": equity,
        "total_return": equity / start_value - 1 if start_value else 0.0,
        "max_drawdown": max_dd,
        "trades": len(trades),
        "win_rate": len(wins) / len(trades) if trades else 0.0,
        "profit_factor": (sum(wins) / gross_loss) if gross_loss else (99.0 if wins else 0.0),
        "buy_and_hold": window[-1]["c"] / window[0]["o"] - 1 if window else 0.0,
    }


def score(result, min_trades):
    """Return per unit of pain (a Calmar-style ratio), or None if too few trades to trust."""
    if result["trades"] < min_trades:
        return None
    return result["total_return"] / max(result["max_drawdown"], 0.03)
