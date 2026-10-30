"""Weekly buyer: spend a fixed amount on the same weekday every week.

With `dca_take_profit` set (0.30 = 30%), it sells everything it bought once
the holdings, after the selling fee, are worth that much more than the money
put in since the last sale. Then it starts a fresh round of weekly buys. Set
it to null to never sell.

If the bot is off on the buy day it buys at the next check later that same
week. A week that passes entirely while the bot is off is skipped, never
doubled up. With several symbols it rotates: one coin per week, in order.
A coin the exchange stops trading (delisted or halted) is skipped for buying, and
coins the bot can no longer price or sell are set aside as "stranded" for you
to deal with in the exchange's app, so the rest keeps working.

Every order is written to the history file, with its ID, BEFORE it is sent.
If anything fails halfway (network, exchange outage, phone dying), the next
check asks the exchange what happened to that exact order instead of sending
another one. So a hiccup can never buy twice or sell coins the bot did not buy.
"""

import json
import os
import time
import uuid
from datetime import datetime, timezone

from .exchange import ExchangeError, refused

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
SELL_TRIES = 5  # a coin whose sale fails this many checks in a row is handed to you


def week_and_day(now):
    """ISO week key ("2026-W43") and weekday (0 = Monday), in UTC."""
    y, w, d = datetime.fromtimestamp(now, timezone.utc).isocalendar()
    return "%d-W%02d" % (y, w), d - 1


def new_order_id():
    return "bot" + uuid.uuid4().hex[:24]


class WeeklyBuyer:
    def __init__(self, cfg, client, broker, state, state_path=None, log=print):
        self.cfg, self.client, self.broker, self.state = cfg, client, broker, state
        self.state_path, self.log = state_path, log
        self.currency = cfg.get("currency", "USDT")
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
        """Current price of every held coin. Coins the exchange has stopped trading are
        left out: it keeps showing a frozen last price for them that nobody can sell at."""
        out = {}
        for s, q in self.state["holdings"].items():
            if q:
                try:
                    if not self.client.symbol_info(s).get("trading", True):
                        self.log("%s is no longer trading on the exchange; its price is not counted." % s)
                        continue
                    # value at the price it could be sold at right now (the bid, where known)
                    out[s] = getattr(self.client, "sell_price", self.client.price)(s)
                except ExchangeError as e:
                    if not refused(e):
                        raise
                    self.log("Cannot get a price for %s (%s). It may have been delisted." % (s, e))
        return out

    def _keep(self):
        """Share of the sale value that actually arrives: after fee, slippage and TDS."""
        return (1 - self.cfg["fee_rate"]) * (1 - self.cfg["slippage"]) * (1 - self.cfg.get("tds_rate", 0.0))

    def value(self):
        return sum(self.state["holdings"][s] * p for s, p in self.prices().items())

    # ---- selling -----------------------------------------------------
    def take_profit(self, now):
        if not self.state.get("selling"):
            target = self.cfg.get("dca_take_profit")
            invested = self.state["invested"]
            if not target or invested <= 0:
                return False
            prices = self.prices()
            value = sum(self.state["holdings"][s] * p for s, p in prices.items())
            if value * self._keep() < invested * (1 + target):
                return False
            if not any(self.state["holdings"][s] * p >= self.client.symbol_info(s)["min_notional"]
                       for s, p in prices.items()):
                return False  # every coin is under the exchange's minimum order: nothing can be sold yet
            self.state["selling"] = {"invested": invested, "proceeds": 0.0, "carried": {},
                                     "carried_value": 0.0, "pending": {}, "tries": {}}
            self.save()
        return self._finish_sale(now)

    def _settle(self, s, q, price, result):
        """Book one coin's sale. Returns True if that coin is done, False if part
        of it did not sell and should be tried again at the next check."""
        sale, holdings = self.state["selling"], self.state["holdings"]
        got, sold, sent = result
        sale["proceeds"] += got
        if q - sent > 1e-12:
            self.log("%.8g %s was no longer in your account (sold or moved outside the bot); left out." % (
                q - sent, s))
        unsold = sent - sold
        if unsold <= 1e-12:
            del holdings[s]
            self.save()
            return True
        if price is None or unsold * price < self.client.symbol_info(s)["min_notional"]:
            # too little left for the exchange to sell: keep it for the next round
            sale["carried"][s] = sale["carried"].get(s, 0.0) + unsold
            sale["carried_value"] += unsold * (price or 0.0)
            del holdings[s]
            self.save()
            return True
        tries = sale.setdefault("tries", {})
        tries[s] = tries.get(s, 0) + 1
        if tries[s] >= SELL_TRIES:
            holdings[s] = unsold
            self._strand(s, unsold, "the exchange did not fill the sale %d times" % tries[s])
            return True
        holdings[s] = unsold
        self.save()
        self.log("The exchange did not fill all of the %s sale; will try again at the next check." % s)
        return False

    def _finish_sale(self, now):
        """Sell coin by coin, saving after each one, so an interrupted sale
        resumes where it stopped instead of selling anything twice."""
        sale, holdings = self.state["selling"], self.state["holdings"]
        prices = self.prices()
        finished = True
        for s in list(holdings):
            q = holdings[s]
            pending = sale["pending"].get(s)
            if pending:  # a sell was sent but its outcome is unknown: ask the exchange
                result = self.broker.recover_sell(s, pending)
                del sale["pending"][s]
                if result is not None:
                    finished &= self._settle(s, q, prices.get(s), result)
                    continue
                self.save()
            if not q:
                del holdings[s]
                continue
            if s not in prices:
                self._strand(s, q, "cannot be priced")
                continue
            if q * prices[s] < self.client.symbol_info(s)["min_notional"]:
                # the exchange will not sell this little; keep it for the next round
                sale["carried"][s] = q
                sale["carried_value"] += q * prices[s]
                del holdings[s]
                self.save()
                continue
            oid = new_order_id()
            sale["pending"][s] = oid
            self.save()
            try:
                result = self.broker.sell(s, q, oid)
            except Exception as e:
                if not refused(e):
                    raise  # outcome unknown; the order id is saved and checked next time
                del sale["pending"][s]
                self._strand(s, q, str(e))
                continue
            del sale["pending"][s]
            finished &= self._settle(s, q, prices[s], result)

        if not finished:
            return False
        invested = sale["invested"]
        profit = sale["proceeds"] + sale["carried_value"] - invested
        self.state["sales"].append({"time": int(now), "invested": invested, "proceeds": sale["proceeds"],
                                    "carried_over": sale["carried_value"], "profit": profit})
        self.state["realized"] += profit
        self.state["holdings"] = dict(sale["carried"])
        self.state["invested"] = sale["carried_value"]
        del self.state["selling"]
        self.save()
        self.log("Take profit: sold for %.2f %s, profit %+.2f (%+.1f%%). Starting a new round." % (
            sale["proceeds"], self.currency, profit, 100 * profit / invested))
        return True

    def _strand(self, s, q, why):
        self.state["stranded"][s] = self.state["stranded"].get(s, 0.0) + q
        del self.state["holdings"][s]
        self.save()
        self.log("Could not sell %s (%s); left in your account for you to handle in the exchange app." % (s, why))

    # ---- buying ------------------------------------------------------
    def _record_buy(self, when, week, symbol, qty, price, spent):
        self.state["holdings"][symbol] = self.state["holdings"].get(symbol, 0.0) + qty
        self.state["invested"] += spent
        self.state["total_invested"] += spent
        self.state["last_week"] = week
        self.state["next_index"] += 1
        self.state["buys"].append({"time": int(when), "symbol": symbol, "spent": spent, "qty": qty, "price": price})
        self.save()
        shown = "%.2f" % price if price >= 1 else "%.8f" % price  # 7843830.00, never 7.84383e+06
        self.log("Weekly buy: %.2f %s of %s at %s" % (spent, self.currency, symbol, shown))

    def _resolve_pending_buy(self):
        """A buy was sent but its outcome is unknown: ask the exchange about that exact order."""
        pb = self.state["pending_buy"]
        got = self.broker.recover_buy(pb["symbol"], pb["id"])
        del self.state["pending_buy"]
        self.save()
        if got and got[0] > 0:
            self._record_buy(pb["time"], pb["week"], pb["symbol"], *got)

    def step(self, now=None):
        now = now or time.time()
        if self.state.get("pending_buy"):
            self._resolve_pending_buy()
        self.take_profit(now)
        if self.state.get("selling"):
            return False  # finish the sale before buying again, so the two rounds never mix
        if not self.due(now):
            return False
        symbols = self.cfg["dca_symbols"]
        amount = float(self.cfg["dca_amount"])
        for _ in range(len(symbols)):
            symbol = symbols[self.state["next_index"] % len(symbols)]
            try:
                info = self.client.symbol_info(symbol)
            except ExchangeError as e:
                if not refused(e):
                    raise
                info = {"trading": False}
            if info.get("trading", True):
                break
            self.log("%s is not trading on the exchange (delisted or halted); buying the next coin instead." % symbol)
            self.state["next_index"] += 1
        else:
            self.log("None of %s can be bought right now." % ", ".join(symbols))
            return False
        minimum = info["min_notional"]
        if amount < minimum:
            self.log("dca_amount %.2f is below the exchange's minimum order of %.2f for %s." % (amount, minimum, symbol))
            return False
        if self.broker.live and self.broker.quote_balance(symbol) < amount:
            self.log("Not enough %s for this week's %.2f buy; will retry at the next check." % (self.currency, amount))
            return False
        week = week_and_day(now)[0]
        oid = new_order_id()
        self.state["pending_buy"] = {"id": oid, "symbol": symbol, "week": week, "time": int(now)}
        self.save()
        try:
            qty, price, spent = self.broker.buy(symbol, amount, oid)
        except Exception as e:
            if refused(e):
                del self.state["pending_buy"]
                self.save()
            raise  # otherwise the order id stays saved and is checked at the next step
        del self.state["pending_buy"]
        if qty <= 0:
            self.save()
            self.log("The exchange could not fill the %s buy (no sellers at that moment); will retry." % symbol)
            return False
        self._record_buy(now, week, symbol, qty, price, spent)
        return True

    def summary(self):
        invested = self.state["invested"]
        holdings = {s: round(q, 8) for s, q in self.state["holdings"].items()}
        try:
            value = self.value()
        except (ExchangeError, OSError):
            lines = ["this round: put in %.2f, worth now: unavailable (could not reach the exchange), "
                     "holdings %s" % (invested, holdings)]
        else:
            ret = (value / invested - 1) if invested else 0.0
            lines = ["this round: put in %.2f, worth now %.2f (%+.1f%%), holdings %s" % (
                invested, value, 100 * ret, holdings)]
        target = self.cfg.get("dca_take_profit")
        if target and invested:
            lines.append("sells everything when worth %.2f (+%.0f%% after fees)" % (
                invested * (1 + target) / self._keep(), 100 * target))
        if self.state.get("selling") or self.state.get("pending_buy"):
            lines.append("an order was interrupted; it will be checked with the exchange at the next run")
        if self.state["stranded"]:
            lines.append("STRANDED (could not be priced or sold, check the exchange app): %s" % self.state["stranded"])
        lines.append("all time: %d buys, %.2f put in, %d profit sales, %+.2f profit taken" % (
            len(self.state["buys"]), self.state["total_invested"], len(self.state["sales"]), self.state["realized"]))
        return "\n".join(lines)

    def run(self):
        mode = "LIVE" if self.broker.live else "PAPER"
        target = self.cfg.get("dca_take_profit")
        selling = "Sells all at +%.0f%% profit." % (100 * target) if target else "Never sells."
        self.log("Weekly buy mode (%s, %s): %.2f %s every %s (UTC) into %s. %s Ctrl+C to stop." % (
            mode, self.cfg.get("exchange", "binance"), float(self.cfg["dca_amount"]), self.currency, self.cfg["dca_day"].capitalize(), ", ".join(self.cfg["dca_symbols"]), selling))
        while True:
            try:
                self.step()
            except KeyboardInterrupt:
                raise
            except Exception as e:  # keep running through network blips
                hint = ""
                if isinstance(e, ExchangeError) and e.status == 401:
                    hint = " (the exchange rejected the API key: check the key, secret and any IP restriction)"
                self.log("Error: %s%s" % (e, hint))
            time.sleep(self.cfg["dca_poll_seconds"])
