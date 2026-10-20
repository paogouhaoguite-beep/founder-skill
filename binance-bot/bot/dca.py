"""Weekly buy mode: spend a fixed amount on the same weekday every week.

With `dca_take_profit` set (0.20 = 20%), it sells everything it bought once
the holdings, after the selling fee, are worth that much more than the money
put in since the last sale. Then it starts a fresh round of weekly buys. Set
it to null to never sell.

If the bot is off on the buy day it buys at the next check later that same
week. A week that passes entirely while the bot is off is skipped, never
doubled up. With several symbols it rotates: one coin per week, in order.
A coin Binance stops trading (delisted or halted) is skipped for buying, and
coins the bot can no longer price or sell are set aside as "stranded" for you
to deal with in the Binance app, so the rest keeps working.
"""

import json
import os
import time
from datetime import datetime, timezone

from .binance import BinanceError

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
        state.setdefault("sales", [])
        state.setdefault("realized", 0.0)
        state.setdefault("total_invested", state["invested"])
        state.setdefault("stranded", {})

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

    def prices(self):
        """Current price of every held coin. Coins Binance has stopped trading are
        left out: it keeps showing a frozen last price for them that nobody can sell at."""
        out = {}
        for s, q in self.state["holdings"].items():
            if q:
                try:
                    if not self.client.symbol_info(s).get("trading", True):
                        self.log("%s is no longer trading on Binance; its price is not counted." % s)
                        continue
                    out[s] = self.client.price(s)
                except BinanceError as e:
                    if (e.status or 500) >= 500:
                        raise
                    self.log("Cannot get a price for %s (%s). It may have been delisted." % (s, e))
        return out

    def value(self):
        return sum(self.state["holdings"][s] * p for s, p in self.prices().items())

    def take_profit(self, now):
        target = self.cfg.get("dca_take_profit")
        invested = self.state["invested"]
        if not target or invested <= 0:
            return False
        prices = self.prices()
        value = sum(self.state["holdings"][s] * p for s, p in prices.items())
        if value * (1 - self.cfg["fee_rate"]) * (1 - self.cfg["slippage"]) < invested * (1 + target):
            return False
        proceeds = 0.0
        for s, q in self.state["holdings"].items():
            if not q:
                continue
            try:
                if s not in prices:
                    raise BinanceError("no price", 400)
                proceeds += self.broker.sell(s, q)
            except BinanceError as e:
                if (e.status or 500) >= 500:
                    raise
                self.state["stranded"][s] = self.state["stranded"].get(s, 0.0) + q
                self.log("Could not sell %s (%s); left in your account for you to handle in the Binance app." % (s, e))
        profit = proceeds - invested
        self.state["sales"].append({"time": int(now), "invested": invested, "proceeds": proceeds, "profit": profit})
        self.state["realized"] += profit
        self.state["invested"] = 0.0
        self.state["holdings"] = {}
        self.save()
        self.log("Take profit: sold everything for %.2f USDT, profit %+.2f (%+.1f%%). Starting a new round." % (
            proceeds, profit, 100 * profit / invested))
        return True

    def step(self, now=None):
        now = now or time.time()
        self.take_profit(now)
        if not self.due(now):
            return False
        symbols = self.cfg["dca_symbols"]
        amount = float(self.cfg["dca_amount"])
        for _ in range(len(symbols)):
            symbol = symbols[self.state["next_index"] % len(symbols)]
            try:
                info = self.client.symbol_info(symbol)
            except BinanceError as e:
                if (e.status or 500) >= 500:
                    raise
                info = {"trading": False}
            if info.get("trading", True):
                break
            self.log("%s is not trading on Binance (delisted or halted); buying the next coin instead." % symbol)
            self.state["next_index"] += 1
        else:
            self.log("None of %s can be bought right now." % ", ".join(symbols))
            return False
        minimum = info["min_notional"]
        if amount < minimum:
            self.log("dca_amount %.2f is below Binance's minimum order of %.2f for %s." % (amount, minimum, symbol))
            return False
        if self.broker.live and self.broker.quote_balance() < amount:
            self.log("Not enough USDT for this week's %.2f buy; will retry at the next check." % amount)
            return False
        qty, price = self.broker.buy(symbol, amount)
        self.state["holdings"][symbol] = self.state["holdings"].get(symbol, 0.0) + qty
        self.state["invested"] += amount
        self.state["total_invested"] += amount
        self.state["last_week"] = week_and_day(now)[0]
        self.state["next_index"] += 1
        self.state["buys"].append({"time": int(now), "symbol": symbol, "spent": amount, "qty": qty, "price": price})
        self.save()
        self.log("Weekly buy: %.2f USDT of %s at %.6g" % (amount, symbol, price))
        return True

    def summary(self):
        invested, value = self.state["invested"], self.value()
        ret = (value / invested - 1) if invested else 0.0
        lines = ["this round: put in %.2f, worth now %.2f (%+.1f%%), holdings %s" % (
            invested, value, 100 * ret, {s: round(q, 8) for s, q in self.state["holdings"].items()})]
        target = self.cfg.get("dca_take_profit")
        if target and invested:
            lines.append("sells everything when worth %.2f (+%.0f%% after fees)" % (
                invested * (1 + target) / ((1 - self.cfg["fee_rate"]) * (1 - self.cfg["slippage"])), 100 * target))
        if self.state["stranded"]:
            lines.append("STRANDED (could not be priced or sold, check the Binance app): %s" % self.state["stranded"])
        lines.append("all time: %d buys, %.2f put in, %d profit sales, %+.2f profit taken" % (
            len(self.state["buys"]), self.state["total_invested"], len(self.state["sales"]), self.state["realized"]))
        return "\n".join(lines)

    def run(self):
        mode = "LIVE" if self.broker.live else "PAPER"
        target = self.cfg.get("dca_take_profit")
        selling = "Sells all at +%.0f%% profit." % (100 * target) if target else "Never sells."
        self.log("Weekly buy mode (%s): %.2f USDT every %s (UTC) into %s. %s Ctrl+C to stop." % (
            mode, float(self.cfg["dca_amount"]), self.cfg["dca_day"].capitalize(), ", ".join(self.cfg["dca_symbols"]), selling))
        while True:
            try:
                self.step()
            except KeyboardInterrupt:
                raise
            except Exception as e:  # keep running through network blips
                self.log("Error: %s" % e)
            time.sleep(self.cfg["dca_poll_seconds"])
