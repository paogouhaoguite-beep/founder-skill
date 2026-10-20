"""The trading loop.

Each step it:
1. re-learns the best strategy every `relearn_hours` (walk-forward, see learner.py),
2. checks the kill switch (stops everything after `max_drawdown` from the peak),
3. manages the open position (stop-loss, strategy exit),
4. opens a new position when the champion strategy signals on a freshly closed candle.

Sizing is a fraction of current equity, so every profit makes the next trade
bigger (compounding). `reinvest_pct` below 1.0 locks part of each profit away
in a "vault" the bot never trades again.
"""

import json
import os
import time

from . import learner
from .backtest import position_quote_amount
from .indicators import atr
from .strategies import STRATEGIES, params_from_json


class Trader:
    def __init__(self, cfg, client, broker, state, state_path=None, log=print):
        self.cfg, self.client, self.broker, self.state = cfg, client, broker, state
        self.state_path, self.log = state_path, log
        state.setdefault("position", None)
        state.setdefault("vault", 0.0)
        state.setdefault("peak_equity", None)
        state.setdefault("halted", False)
        state.setdefault("trades", [])
        state.setdefault("report", None)
        state.setdefault("last_entry_bar", None)

    # ---- helpers -----------------------------------------------------
    def save(self):
        if not self.state_path:
            return
        tmp = self.state_path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(self.state, fh, indent=2)
        os.replace(tmp, self.state_path)

    def candles(self, symbol):
        return self.client.closed_klines(symbol, self.cfg["interval"], self.cfg["signal_candles"])

    def equity(self):
        cash = self.broker.quote_balance()
        pos = self.state["position"]
        if pos:
            cash += pos["qty"] * self.client.price(pos["symbol"])
        return cash

    # ---- learning ----------------------------------------------------
    def needs_learning(self, now):
        report = self.state["report"]
        return report is None or now - report["learned_at"] >= self.cfg["relearn_hours"] * 3600

    def relearn(self):
        self.log("Studying the charts for %s ..." % ", ".join(self.cfg["symbols"]))
        history = {s: self.client.closed_klines(s, self.cfg["interval"], self.cfg["learn_candles"])
                   for s in self.cfg["symbols"]}
        report = learner.learn(history, self.cfg)
        self.state["report"] = report
        self.log(learner.format_report(report))

    # ---- trading -----------------------------------------------------
    def close_position(self, proceeds, reason):
        pos = self.state["position"]
        pnl = proceeds - pos["cost"]
        if pnl > 0:
            self.state["vault"] += pnl * (1 - self.cfg["reinvest_pct"])
        self.state["trades"].append({"symbol": pos["symbol"], "strategy": pos["strategy"], "reason": reason,
                                     "cost": pos["cost"], "proceeds": proceeds, "pnl": pnl,
                                     "opened": pos["opened"], "closed": int(time.time())})
        self.state["position"] = None
        self.log("SELL %s (%s): pnl %+.4f" % (pos["symbol"], reason, pnl))

    def manage_position(self):
        pos = self.state["position"]
        last_price = self.client.price(pos["symbol"])
        proceeds = self.broker.stop_fill(pos, last_price)
        if proceeds is not None:
            self.close_position(proceeds, "stop-loss")
            return
        candles = self.candles(pos["symbol"])
        if not candles or candles[-1]["t"] == pos["last_bar"]:
            return
        pos["last_bar"] = candles[-1]["t"]
        strat = STRATEGIES[pos["strategy"]]
        _, exits = strat.signals(candles, params_from_json(pos["params"]))
        if exits[-1]:
            self.broker.cancel_stop(pos["symbol"], pos.get("stop_id"))
            self.close_position(self.broker.sell(pos["symbol"], pos["qty"]), "strategy exit")

    def maybe_enter(self):
        champ = (self.state["report"] or {}).get("champion")
        if not champ:
            return
        symbol = champ["symbol"]
        candles = self.candles(symbol)
        if not candles or candles[-1]["t"] == self.state["last_entry_bar"]:
            return
        self.state["last_entry_bar"] = candles[-1]["t"]
        strat = STRATEGIES[champ["strategy"]]
        params = params_from_json(champ["params"])
        entries, _ = strat.signals(candles, params)
        if not entries[-1]:
            return
        atr_now = atr(candles, 14)[-1]
        price = self.client.price(symbol)
        if atr_now is None:
            return
        stop = price - params["stop_atr"] * atr_now
        vault = self.state["vault"]
        cash = self.broker.quote_balance() - vault
        sizing = dict(self.cfg, min_notional=max(self.cfg["min_notional"], self._exchange_min(symbol)))
        amount = position_quote_amount(cash, cash, price, stop, sizing)
        if amount <= 0:
            self.log("Signal on %s but the trade would be below Binance's minimum order size; skipped." % symbol)
            return
        qty, fill = self.broker.buy(symbol, amount)
        self.state["position"] = {"symbol": symbol, "strategy": strat.name, "params": champ["params"],
                                  "qty": qty, "entry": fill, "stop": stop, "stop_id": None,
                                  "cost": amount, "opened": int(time.time()), "last_bar": candles[-1]["t"]}
        self.save()
        try:
            self.state["position"]["stop_id"] = self.broker.place_stop(symbol, qty, stop)
        except Exception as e:  # the bot then watches the stop price itself
            self.log("Could not place the exchange stop-loss (%s); the bot will enforce it." % e)
        self.log("BUY %s via %s: %.4f spent, stop %.6g" % (symbol, strat.name, amount, stop))

    def _exchange_min(self, symbol):
        try:
            return self.client.symbol_info(symbol)["min_notional"]
        except Exception:
            return 0.0

    def step(self, now=None):
        now = now or time.time()
        if self.state["halted"]:
            self.log("Bot is halted by the kill switch. Run `python main.py reset-halt` to resume.")
            return
        if self.needs_learning(now):
            self.relearn()

        equity = self.equity()
        peak = max(self.state["peak_equity"] or equity, equity)
        self.state["peak_equity"] = peak
        if peak and (peak - equity) / peak >= self.cfg["max_drawdown"]:
            pos = self.state["position"]
            if pos:
                self.broker.cancel_stop(pos["symbol"], pos.get("stop_id"))
                self.close_position(self.broker.sell(pos["symbol"], pos["qty"]), "kill switch")
            self.state["halted"] = True
            self.log("KILL SWITCH: equity fell %.1f%% from its peak. Trading stopped." % (100 * (peak - equity) / peak))
            self.save()
            return

        if self.state["position"]:
            self.manage_position()
        if not self.state["position"]:
            self.maybe_enter()
        self.save()

    def run(self):
        mode = "LIVE" if self.broker.live else "PAPER"
        self.log("Starting in %s mode. Ctrl+C to stop." % mode)
        while True:
            try:
                self.step()
            except KeyboardInterrupt:
                raise
            except Exception as e:  # keep running through network blips
                self.log("Error: %s" % e)
            time.sleep(self.cfg["poll_seconds"])
