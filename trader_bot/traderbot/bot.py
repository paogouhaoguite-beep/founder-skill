"""The trading loop: the eleven-skill pipeline on a timer, with your yes before
every entry.

    scanner -> entry -> exit -> timemachine -> news -> alerts quote -> budget -> risk -> broker
                                                                        your yes ^       | Alpaca
    while a trade is open: fills from Alpaca -> ticket.py fill; flat by flat_by

Every decision is made by the skills' own tools (skills.py runs them); the bot
only moves between them, talks to Alpaca and asks you. The limits that matter
(max loss per trade, daily loss, trades per day, the entry window, a stop on
every order) are trader-risk's, from trader/config.json. On top, the bot:
  - places nothing without your explicit yes for that one order,
  - holds one position at a time,
  - skips a breakout that triggered more than max_trigger_age_min ago,
  - skips a trade the Time Machine says leans toward the stop (min_tm_edge_pts),
  - stops opening trades when the account is down max_daily_loss_usd today,
  - stops opening trades while the file trader/STOP exists (the kill switch),
  - closes what is still open at flat_by (auto_flatten; getting out needs no yes).
"""

import datetime
import json
import os
import re

from .alpaca import BrokerError

DEFAULTS = {
    "symbols": ["AAPL", "MSFT", "NVDA", "AMD", "TSLA", "AMZN", "META", "GOOGL", "NFLX", "AVGO",
                "PLTR", "COIN", "SMCI", "MU", "INTC", "BAC", "JPM", "XOM", "UBER", "SHOP"],
    "max_candidates": 5,
    "interval_s": 60,
    "max_trigger_age_min": 10,
    "stop": "or-mid",
    "target": "2R",
    "replays": 10000,
    "min_tm_edge_pts": 0.0,
    "news": True,
    "approval_timeout_s": 120,
    "auto_flatten": True,
}
BOT_CONFIG = "trader/bot.json"
STATE = "trader/state/bot.json"
LOG = "trader/state/bot.log"
KILL = "trader/STOP"
DONE = ("canceled", "expired", "rejected")


# ---------------------------------------------------------------- New York time (as the skills do it)

def _nth_sunday(year, month, n):
    d = datetime.date(year, month, 1)
    d += datetime.timedelta(days=(6 - d.weekday()) % 7)
    return d + datetime.timedelta(weeks=n - 1)


def eastern_offset(utc):
    y = utc.year
    start = datetime.datetime.combine(_nth_sunday(y, 3, 2), datetime.time(7))
    end = datetime.datetime.combine(_nth_sunday(y, 11, 1), datetime.time(6))
    return datetime.timedelta(hours=-4 if start <= utc < end else -5)


def to_eastern(utc):
    return utc + eastern_offset(utc)


def eastern_to_utc(local):
    guess = local + datetime.timedelta(hours=5)
    return local - eastern_offset(guess)


def parse_ny(text):
    """'2026-10-19 10:15' New York time -> naive UTC."""
    return eastern_to_utc(datetime.datetime.strptime(text.strip(), "%Y-%m-%d %H:%M"))


def hhmm(text):
    m = re.match(r"^\s*(\d{1,2}):(\d{2})\s*([AaPp][Mm])?\s*$", str(text or ""))
    if not m:
        return None
    h, mi = int(m.group(1)), int(m.group(2))
    if m.group(3):
        h = h % 12 + (12 if m.group(3).lower() == "pm" else 0)
    return datetime.time(h, mi)


# ---------------------------------------------------------------- the bot

def time_machine_edge(tm):
    """Percentage points the target beats break-even by, from timemachine.json
    (trader-timemachine's own lean): target / (target + stop) minus 1 / (1 + R)."""
    mc = (tm or {}).get("mc") or {}
    pt, ps = mc.get("p_target") or 0.0, mc.get("p_stop") or 0.0
    if pt + ps <= 0:
        return None
    r = mc.get("r_at_target") or 1.0
    return 100.0 * (pt / (pt + ps) - 1.0 / (1.0 + r))


class Bot(object):
    def __init__(self, skills, broker, approver, settings=None, clock=None, out=print, check_market=True):
        self.s = skills
        self.broker = broker
        self.approver = approver
        self.cfg = dict(DEFAULTS, **(settings or {}))
        self.clock = clock or (lambda: datetime.datetime.utcnow().replace(microsecond=0))
        self.out = out
        self.check_market = check_market
        self.state = self.s.read(STATE, {}) or {}

    # -- plumbing

    def log(self, msg):
        now = to_eastern(self.clock()).strftime("%Y-%m-%d %H:%M:%S ET")
        line = "%s  %s" % (now, msg)
        self.out(line)
        path = self.s.path(LOG)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")

    def save(self):
        path = self.s.path(STATE)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path + ".tmp", "w", encoding="utf-8") as fh:
            json.dump(self.state, fh, indent=2)
            fh.write("\n")
        os.replace(path + ".tmp", path)

    def today(self):
        return to_eastern(self.clock()).date().isoformat()

    def roll_day(self):
        if self.state.get("date") != self.today():
            keep = self.state.get("open")
            self.state = {"date": self.today(), "tried": [], "placed": 0}
            if keep:
                self.state["open"] = keep
                self.log("Carried over an open trade in %s from an earlier day." % keep["symbol"])

    def trader_config(self):
        return self.s.read("trader/config.json", {}) or {}

    # -- one pass

    def cycle(self):
        self.roll_day()
        try:
            if self.state.get("open"):
                self.manage_open()
            if self.state.get("open"):
                return "holding"
            why = self.no_entries_reason()
            if why:
                self.log("No new entries: %s." % why)
                return "idle"
            return self.look_for_trade()
        finally:
            self.save()

    def no_entries_reason(self):
        if os.path.exists(self.s.path(KILL)):
            return "the kill switch %s is there (delete it to resume)" % KILL
        if self.check_market:
            try:
                clk = self.broker.clock()
                if not clk.get("is_open"):
                    return "the market is closed (next open %s)" % clk.get("next_open")
            except BrokerError as e:
                return "cannot read the market clock: %s" % e
        limit = self.trader_config().get("max_daily_loss_usd")
        if limit:
            try:
                acct = self.broker.account()
                day = float(acct["equity"]) - float(acct["last_equity"])
            except (BrokerError, KeyError, TypeError, ValueError):
                day = None
            if day is not None and day <= -float(limit):
                return "the account is down $%.2f today, at or over max_daily_loss_usd $%.2f" % (-day, float(limit))
        return None

    # -- finding a trade

    def look_for_trade(self):
        args = ["orb", "--quiet"]
        if self.cfg.get("symbols"):
            args += ["--symbols", ",".join(self.cfg["symbols"])]
        r = self.s.run("scan", *args)
        doc = self.s.read("trader/watchlist.json", {}) or {}
        hits = [h for h in doc.get("hits", []) if doc.get("mode") == "orb"]
        if not r.ok and not hits:
            self.log("Scanner: no opening-range breakouts%s." % (
                "" if r.code == 1 and not r.err.strip() else " (%s)" % r.text().splitlines()[-1]))
            return "idle"
        tried = set(self.state.get("tried", []))
        fresh = [h["symbol"] for h in reversed(hits) if h["symbol"] not in tried]  # newest breakout first
        self.log("Scanner: %d breakout(s) %s, %d not tried yet today." % (len(hits), doc.get("as_of", ""), len(fresh)))
        for sym in fresh[:int(self.cfg["max_candidates"])]:
            self.state.setdefault("tried", []).append(sym)
            if self.consider(sym):
                return "placed"
        return "idle"

    def consider(self, sym):
        s = self.s
        r = s.run("entry", "check", sym, "--write")
        e = s.read("trader/entry.json", {}) or {}
        if not r.ok or e.get("symbol") != sym or e.get("status") != "triggered":
            self.log("%s: entry %s." % (sym, e.get("status") or r.text()[-200:]))
            return False
        age = self.trigger_age(e)
        if age is not None and age > float(self.cfg["max_trigger_age_min"]):
            self.log("%s: the breakout closed at %s, %d min ago (over max_trigger_age_min %s); stale, skipped."
                     % (sym, e.get("time"), age, self.cfg["max_trigger_age_min"]))
            return False

        r = s.run("exit", "plan", "--stop", self.cfg["stop"], "--target", self.cfg["target"], "--write")
        plan = s.read("trader/plan.json", {}) or {}
        if not r.ok or plan.get("symbol") != sym:
            self.log("%s: no exit plan: %s" % (sym, r.text()[-300:]))
            return False

        tm_args = ["run", "--write", "--replays", self.cfg["replays"]]
        if plan.get("flat_by"):
            tm_args += ["--until", plan["flat_by"]]
        r = s.run("timemachine", *tm_args)
        tm = s.read("trader/timemachine.json", {}) or {}
        if not r.ok or (tm.get("plan") or {}).get("symbol") != sym:
            self.log("%s: the Time Machine could not replay it, skipped: %s" % (sym, r.text()[-300:]))
            return False
        edge = time_machine_edge(tm)
        if edge is None or edge < float(self.cfg["min_tm_edge_pts"]):
            self.log("%s: Time Machine says no edge (%s), skipped. %s" % (
                sym, "n/a" if edge is None else "%+.1f pts" % edge, tm.get("verdict", "")))
            return False

        news = ""
        if self.cfg.get("news"):
            r = s.run("news", "--tickers", sym, "--hours", "12", "--no-moves", "--dry-run", now=False)
            news = r.out.strip()

        s.run("alerts", "quote", sym, "--write")
        r = s.run("size", "--write")
        orders = (s.read("trader/orders.json", {}) or {}).get("orders") or []
        if not r.ok or not orders or orders[0].get("symbol") != sym:
            self.log("%s: trader-budget wrote no order: %s" % (sym, r.text()[-300:]))
            return False
        r = s.run("risk")
        if not r.ok:
            self.log("%s: BLOCKED by trader-risk:\n%s" % (sym, r.text()))
            return False
        r = s.run("ticket", "show", "--index", "1", "--json")
        try:
            ticket = r.json()
            ticket = ticket[0] if isinstance(ticket, list) else ticket
        except ValueError:
            self.log("%s: no ticket: %s" % (sym, r.text()[-300:]))
            return False
        if not ticket.get("ready"):
            self.log("%s: ticket not ready: %s" % (sym, ticket.get("status")))
            return False
        return self.ask_and_place(sym, ticket, tm, news)

    def trigger_age(self, entry):
        t = hhmm(entry.get("time"))
        if t is None or not entry.get("date"):
            return None
        trig = datetime.datetime.combine(datetime.date.fromisoformat(entry["date"]), t)
        return (to_eastern(self.clock()) - trig).total_seconds() / 60.0

    # -- your yes, then Alpaca

    def ask_and_place(self, sym, ticket, tm, news):
        s = self.s
        shown = s.run("ticket", "show", "--index", "1").out.strip()
        text = "\n".join(x for x in (
            "=" * 72, "PROPOSED %s ORDER (%s)" % ("PAPER" if ticket.get("paper", True) else "LIVE MONEY", sym),
            shown, "", "Time Machine: %s" % tm.get("verdict", "n/a"),
            ("News, last 12 hours:\n" + news) if news else "", "=" * 72) if x is not None)
        reply = self.approver.ask(text)
        if not reply:
            s.run("ticket", "decline", "--index", "1", "--reply", "no answer")
            self.log("%s: no yes, declined. Nothing was sent." % sym)
            return False
        r = s.run("ticket", "approve", "--index", "1", "--reply", reply)
        if not r.ok:
            s.run("ticket", "decline", "--index", "1", "--reply", reply)
            self.log("%s: not a yes for this order (%s). Nothing was sent." % (sym, r.text()))
            return False
        cid = "tb-%s-%s-%s" % (self.today(), sym, ticket["fingerprint"][:8])
        try:
            placed = self.broker.place(ticket["tool_input"], client_order_id=cid)
        except BrokerError as e:
            s.run("ticket", "result", "--index", "1", "--status", "failed", "--note", str(e)[:200])
            self.log("%s: Alpaca refused the order: %s" % (sym, e))
            return False
        s.run("ticket", "result", "--index", "1", "--status", "placed", "--broker-id", placed["id"])
        plan = (s.read("trader/orders.json", {}) or {}).get("orders", [{}])[0].get("plan") or {}
        self.state["open"] = {"symbol": sym, "order_id": placed["id"], "qty": ticket["tool_input"].get("qty"),
                              "flat_by": plan.get("flat_by"), "entry_filled": False, "exits": []}
        self.state["placed"] = self.state.get("placed", 0) + 1
        s.run("alerts", "add", "--from-plan")
        self.log("%s: PLACED %s (Alpaca order %s)." % (sym, ticket.get("plain"), placed["id"]))
        return True

    # -- while a trade is open

    def manage_open(self):
        o = self.state["open"]
        sym = o["symbol"]
        try:
            order = self.broker.order(o["order_id"])
        except BrokerError as e:
            self.log("%s: cannot read the order: %s" % (sym, e))
            return
        flat_by = hhmm(o.get("flat_by"))
        late = bool(flat_by) and to_eastern(self.clock()).time() >= flat_by
        if not o["entry_filled"]:
            filled = float(order.get("filled_qty") or 0)
            if order.get("status") == "filled" or (order.get("status") in DONE and filled):
                self.record_fill(sym, "buy", order)  # a partial fill that was then canceled still counts
                o["entry_filled"] = True
            elif order.get("status") in DONE:
                self.log("%s: the entry was %s with nothing filled; no position." % (sym, order["status"]))
                self.state.pop("open")
                return
            elif late:
                try:
                    self.broker.cancel(o["order_id"])
                except BrokerError as e:
                    self.log("%s: could not cancel the unfilled entry, CHECK ALPACA: %s" % (sym, e))
                    return
                self.log("%s: the entry never filled by flat_by %s; canceled it." % (sym, o.get("flat_by")))
                return
        for leg in order.get("legs") or []:
            if leg.get("status") == "filled" and leg["id"] not in o["exits"]:
                self.record_fill(sym, "sell", leg)
                o["exits"].append(leg["id"])
                self.log("%s: %s filled, trade closed." % (sym, "take-profit" if leg.get("type") == "limit" else "stop-loss"))
                self.state.pop("open")
                return
        if o.get("flatten_id"):
            try:
                f = self.broker.order(o["flatten_id"])
            except BrokerError as e:
                self.log("%s: cannot read the closing order: %s" % (sym, e))
                return
            if f.get("status") == "filled":
                self.record_fill(sym, "sell", f)
                self.log("%s: flat by %s, trade closed." % (sym, o.get("flat_by")))
                self.state.pop("open")
            return
        if o["entry_filled"] and late:
            self.flatten(o)

    def flatten(self, o):
        sym = o["symbol"]
        if not self.cfg.get("auto_flatten"):
            self.log("%s: past flat_by %s and auto_flatten is off: CLOSE IT YOURSELF." % (sym, o.get("flat_by")))
            return
        try:
            for x in self.broker.open_orders(sym) or []:
                self.broker.cancel(x["id"])
            if self.broker.position(sym) is None:
                self.log("%s: no position left at flat_by." % sym)
                self.state.pop("open")
                return
            close = self.broker.close_position(sym)
        except BrokerError as e:
            self.log("%s: could not flatten, CHECK ALPACA NOW: %s" % (sym, e))
            return
        o["flatten_id"] = close["id"]
        self.log("%s: flat_by %s reached: canceled the bracket and sent a market sell (order %s)."
                 % (sym, o.get("flat_by"), close["id"]))

    def record_fill(self, sym, side, order):
        qty, price = order.get("filled_qty"), order.get("filled_avg_price")
        r = self.s.run("ticket", "fill", "--symbol", sym, "--side", side, "--qty", qty, "--price", price)
        self.log("%s: %s %s at %s filled. %s" % (sym, side, qty, price, r.text().splitlines()[-1] if r.text() else ""))
