"""Weekly buy mode: spend a fixed amount on the same weekday every week and never sell.

If the bot is off on the buy day it buys at the next check later that same
week. A week that passes entirely while the bot is off is skipped, never
doubled up. With several symbols it rotates: one coin per week, in order.
"""

import json
import os
import time
from datetime import datetime, timezone

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def week_and_day(now):
    """ISO week key ("2026-W43") and weekday (0 = Monday), in UTC."""
    y, w, d = datetime.fromtimestamp(now, timezone.utc).isocalendar()
    return "%d-W%02d" % (y, w), d - 1


class WeeklyBuyer:
    def __init__(self, cfg, client, broker, state, state_path=None, log=print):
        self.cfg, self.client, self.broker, self.state = cfg, client, broker, state
        self.state_path, self.log = state_path, log
        state.setdefault("buys", [])
        state.setdefault("holdings", {})
        state.setdefault("invested", 0.0)
        state.setdefault("last_week", None)
        state.setdefault("next_index", 0)

    def save(self):
        if not self.state_path:
            return
        tmp = self.state_path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(self.state, fh, indent=2)
        os.replace(tmp, self.state_path)

    def due(self, now):
        week, day = week_and_day(now)
        return day >= DAYS.index(self.cfg["dca_day"].lower()) and self.state["last_week"] != week

    def value(self):
        return sum(q * self.client.price(s) for s, q in self.state["holdings"].items() if q)

    def step(self, now=None):
        now = now or time.time()
        if not self.due(now):
            return False
        symbols = self.cfg["dca_symbols"]
        symbol = symbols[self.state["next_index"] % len(symbols)]
        amount = float(self.cfg["dca_amount"])
        minimum = self.client.symbol_info(symbol)["min_notional"]
        if amount < minimum:
            self.log("dca_amount %.2f is below Binance's minimum order of %.2f for %s." % (amount, minimum, symbol))
            return False
        if self.broker.live and self.broker.quote_balance() < amount:
            self.log("Not enough USDT for this week's %.2f buy; will retry at the next check." % amount)
            return False
        qty, price = self.broker.buy(symbol, amount)
        self.state["holdings"][symbol] = self.state["holdings"].get(symbol, 0.0) + qty
        self.state["invested"] += amount
        self.state["last_week"] = week_and_day(now)[0]
        self.state["next_index"] += 1
        self.state["buys"].append({"time": int(now), "symbol": symbol, "spent": amount, "qty": qty, "price": price})
        self.save()
        self.log("Weekly buy: %.2f USDT of %s at %.6g" % (amount, symbol, price))
        return True

    def summary(self):
        invested, value = self.state["invested"], self.value()
        ret = (value / invested - 1) if invested else 0.0
        return "buys %d, invested %.2f, worth now %.2f (%+.1f%%), holdings %s" % (
            len(self.state["buys"]), invested, value, 100 * ret,
            {s: round(q, 8) for s, q in self.state["holdings"].items()})

    def run(self):
        mode = "LIVE" if self.broker.live else "PAPER"
        self.log("Weekly buy mode (%s): %.2f USDT every %s (UTC) into %s. Never sells. Ctrl+C to stop." % (
            mode, float(self.cfg["dca_amount"]), self.cfg["dca_day"].capitalize(), ", ".join(self.cfg["dca_symbols"])))
        while True:
            try:
                self.step()
            except KeyboardInterrupt:
                raise
            except Exception as e:  # keep running through network blips
                self.log("Error: %s" % e)
            time.sleep(self.cfg["dca_poll_seconds"])
