"""The whole loop, offline: the README's trade (TSLA, Monday October 19 2026,
10:15 AM ET) through the real skill tools, a simulated broker and a scripted yes."""

import io
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from traderbot import __main__ as cli  # noqa: E402
from traderbot.alpaca import order_body  # noqa: E402
from traderbot.approval import ScriptedApprover, TerminalApprover  # noqa: E402
from traderbot.bot import Bot, hhmm, parse_ny, time_machine_edge  # noqa: E402
from traderbot.sim import SimBroker  # noqa: E402
from traderbot.skills import SKILLS_DIR, Skills  # noqa: E402

FIX = os.path.normpath(os.path.join(HERE, "..", "..", "tests", "fixtures"))
NOW = "2026-10-19 10:15"
OFFLINE = {
    "scan": {"orb": ["--offline", os.path.join(FIX, "trader-scanner", "wall5m-2026-10-19.json.gz"),
                     "--min-price", "0"]},
    "entry": {"check": ["--offline", os.path.join(FIX, "trader-entry", "TSLA-2026-10-19-5m.json")]},
    "timemachine": {"run": ["--offline", os.path.join(FIX, "trader-timemachine", "TSLA-60d5m.json.gz")]},
    "news": {"": ["--offline", os.path.join(FIX, "trader-news"), "--no-sec"]},
    "alerts": {"quote": ["--offline", os.path.join(FIX, "trader-alerts")]},
}
SETTINGS = {"symbols": ["TSLA"], "target": "1R", "replays": 2000}


class Base(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.dir, "trader"))
        shutil.copy(os.path.join(SKILLS_DIR, "trader-budget", "config.example.json"),
                    os.path.join(self.dir, "trader", "config.json"))
        self.lines = []

    def tearDown(self):
        shutil.rmtree(self.dir)

    def bot(self, replies=("yes",), settings=None, broker=None, now=NOW):
        self.skills = Skills(self.dir, extra_args=OFFLINE, now=now)
        self.broker = broker or SimBroker(cash=5000.0)
        self.approver = ScriptedApprover(replies)
        return Bot(self.skills, self.broker, self.approver, dict(SETTINGS, **(settings or {})),
                   clock=lambda: parse_ny(now), out=self.lines.append, check_market=False)

    def read(self, rel):
        with open(os.path.join(self.dir, rel), encoding="utf-8") as fh:
            return json.load(fh)

    def log(self):
        return "\n".join(self.lines)


class ReplayTheReel(Base):
    def test_finds_plans_asks_and_places_the_tsla_trade(self):
        bot = self.bot()
        self.assertEqual(bot.cycle(), "placed", self.log())
        # the skills' own numbers from the README: 8 shares, stop 358.32, target 370.04 (1R)
        (sent, cid), = self.broker.placed
        self.assertEqual(sent["symbol"], "TSLA")
        self.assertEqual(sent["qty"], "8")
        self.assertEqual(sent["stop_loss_stop_price"], "358.32")
        self.assertEqual(sent["take_profit_limit_price"], "370.04")
        self.assertEqual(sent["order_class"], "bracket")
        self.assertTrue(cid.startswith("tb-2026-10-19-TSLA-"))
        # you were shown the ticket and the Time Machine before anything was sent
        self.assertEqual(len(self.approver.asked), 1)
        self.assertIn("PAPER", self.approver.asked[0])
        self.assertIn("Time Machine:", self.approver.asked[0])
        # trader-broker recorded the yes and the placement
        statuses = [r["status"] for r in self.read("trader/state/broker.json")["orders"]]
        self.assertEqual(statuses[:2], ["approved", "placed"])
        self.assertEqual(self.read("trader/state/bot.json")["open"]["symbol"], "TSLA")

    def test_fill_then_target_closes_the_trade(self):
        bot = self.bot()
        bot.cycle()
        self.assertEqual(bot.cycle(), "holding")  # the entry fill is recorded
        self.assertTrue(bot.state["open"]["entry_filled"])
        pf = self.read("trader/portfolio.json")
        self.assertIn("TSLA", json.dumps(pf))
        self.broker.fill_leg("TSLA", "limit")
        bot.cycle()
        self.assertNotIn("open", bot.state)
        self.assertIn("take-profit filled", self.log())

    def test_does_not_retry_a_symbol_the_same_day(self):
        bot = self.bot(replies=("no",))
        self.assertEqual(bot.cycle(), "idle")
        self.assertEqual(bot.cycle(), "idle")
        self.assertEqual(len(self.approver.asked), 1)


class YourYes(Base):
    def test_no_answer_sends_nothing(self):
        bot = self.bot(replies=())
        self.assertEqual(bot.cycle(), "idle")
        self.assertEqual(self.broker.placed, [])
        self.assertIn("no yes, declined", self.log())

    def test_only_an_explicit_yes_counts(self):
        for reply in ("ok", "sure", "yes to all", "yes but wait", "yes 20 shares"):
            self.tearDown()
            self.setUp()
            bot = self.bot(replies=(reply,))
            self.assertEqual(bot.cycle(), "idle", reply)
            self.assertEqual(self.broker.placed, [], reply)

    def test_yes_with_the_right_numbers_counts(self):
        bot = self.bot(replies=("yes, buy 8 TSLA",))
        self.assertEqual(bot.cycle(), "placed", self.log())

    def test_terminal_approver_times_out_to_no(self):
        r, w = os.pipe()
        try:
            with os.fdopen(r) as fin:
                out = io.StringIO()
                self.assertIsNone(TerminalApprover(timeout=0, stream_in=fin, stream_out=out).ask("ticket"))
                self.assertIn("declined", out.getvalue())
        finally:
            os.close(w)


class Guards(Base):
    def test_kill_switch_stops_new_entries(self):
        open(os.path.join(self.dir, "trader", "STOP"), "w").close()
        bot = self.bot()
        self.assertEqual(bot.cycle(), "idle")
        self.assertEqual(self.approver.asked, [])
        self.assertIn("kill switch", self.log())

    def test_daily_loss_on_the_account_stops_new_entries(self):
        bot = self.bot(broker=SimBroker(cash=5000.0, equity=4840.0, last_equity=5000.0))
        self.assertEqual(bot.cycle(), "idle")
        self.assertIn("max_daily_loss_usd", self.log())

    def test_a_stale_breakout_is_skipped(self):
        bot = self.bot(now="2026-10-19 10:45")
        bot.cycle()
        self.assertEqual(self.broker.placed, [])
        self.assertIn("stale", self.log())

    def test_time_machine_gate(self):
        bot = self.bot(settings={"min_tm_edge_pts": 50})
        self.assertEqual(bot.cycle(), "idle")
        self.assertEqual(self.approver.asked, [])
        self.assertIn("Time Machine says no edge", self.log())

    def test_trader_risk_blocks_go_unasked(self):
        cfg = self.read("trader/config.json")
        cfg["max_daily_loss_usd"] = 40  # under this trade's $46.88 at the stop: only trader-risk checks it
        with open(os.path.join(self.dir, "trader", "config.json"), "w") as fh:
            json.dump(cfg, fh)
        bot = self.bot()
        self.assertEqual(bot.cycle(), "idle")
        self.assertEqual(self.approver.asked, [])
        self.assertIn("BLOCKED by trader-risk", self.log())

    def test_flat_by_closes_what_is_open(self):
        bot = self.bot()
        bot.cycle()
        bot.cycle()
        late = self.bot(now="2026-10-19 15:55", broker=self.broker)
        late.state = bot.state
        late.cycle()
        self.assertIn("flat_by 15:55 reached", self.log())
        late.cycle()
        self.assertNotIn("open", late.state)


class Pieces(unittest.TestCase):
    def test_rest_body_nests_the_bracket(self):
        body = order_body({"symbol": "TSLA", "side": "buy", "qty": "8", "type": "market", "time_in_force": "day",
                           "order_class": "bracket", "take_profit_limit_price": "370.04",
                           "stop_loss_stop_price": "358.32"}, "cid-1")
        self.assertEqual(body["take_profit"], {"limit_price": "370.04"})
        self.assertEqual(body["stop_loss"], {"stop_price": "358.32"})
        self.assertEqual(body["client_order_id"], "cid-1")
        self.assertNotIn("take_profit_limit_price", body)

    def test_edge(self):
        self.assertAlmostEqual(time_machine_edge({"mc": {"p_target": 0.294, "p_stop": 0.255, "r_at_target": 1}}),
                               100 * (0.294 / 0.549 - 0.5), places=6)
        self.assertIsNone(time_machine_edge({"mc": {"p_target": 0, "p_stop": 0}}))

    def test_hhmm(self):
        self.assertEqual(str(hhmm("10:15 AM")), "10:15:00")
        self.assertEqual(str(hhmm("3:55 PM")), "15:55:00")
        self.assertEqual(str(hhmm("15:55")), "15:55:00")


class Preflight(Base):
    def setUp(self):
        super().setUp()
        self.skills = Skills(self.dir)

    def test_paper_config_refuses_live(self):
        with self.assertRaises(cli.SetupError):
            cli.preflight(self.skills, live=True, dry_run=False)

    def test_live_config_refuses_paper_run(self):
        cfg = self.read("trader/config.json")
        cfg["paper"] = False
        with open(os.path.join(self.dir, "trader", "config.json"), "w") as fh:
            json.dump(cfg, fh)
        with self.assertRaises(cli.SetupError):
            cli.preflight(self.skills, live=False, dry_run=True)

    def test_dry_run_needs_no_keys(self):
        self.assertIsInstance(cli.preflight(self.skills, live=False, dry_run=True), SimBroker)

    def test_requires_a_stop(self):
        cfg = self.read("trader/config.json")
        cfg["require_stop"] = False
        with open(os.path.join(self.dir, "trader", "config.json"), "w") as fh:
            json.dump(cfg, fh)
        with self.assertRaises(cli.SetupError):
            cli.preflight(self.skills, live=False, dry_run=True)


if __name__ == "__main__":
    unittest.main()
