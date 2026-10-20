"""Things that could go wrong in months of real use, each reproduced first."""

import json
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main  # noqa: E402
from bot.binance import BinanceClient, BinanceError, LiveBroker  # noqa: E402
from bot.dca import WeeklyBuyer  # noqa: E402

CFG = dict(main.load_config("/nonexistent", exchange="binance"), dca_amount=6, dca_symbols=["BTCUSDT", "ETHUSDT", "SOLUSDT"])
MON = 1792972800  # 2026-10-26 00:00 UTC, a Monday
WEEK = 7 * 86400
BASE = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL"}


class Exchange:
    """Several coins, Binance-style filters and failures."""

    def __init__(self):
        self.p = {"BTCUSDT": 100.0, "ETHUSDT": 10.0, "SOLUSDT": 1.0}
        self.bal = {"USDT": 1000.0, "BTC": 0.0, "ETH": 0.0, "SOL": 0.0}
        self.orders = []
        self.fail_sell = set()      # symbols whose sell gets a 503 that never reached the book
        self.no_fill_buy = False    # market buy expires unfilled (no liquidity)
        self.lose_reply = False     # order executes, reply never arrives
        self.lookup_down = False    # and Binance cannot be reached to ask about it

    def sync_time(self):
        pass

    def price(self, s):
        return self.p[s]

    def symbol_info(self, s):
        return {"base": BASE[s], "quote": "USDT", "step": 0.00001, "min_qty": 0.00001,
                "min_notional": 5.0, "quote_precision": 8, "trading": True}

    def balances(self):
        return dict(self.bal)

    def order(self, **o):
        s, base = o["symbol"], BASE[o["symbol"]]
        if o["side"] == "SELL" and s in self.fail_sell:
            raise BinanceError("503 Service unavailable", 503)
        if o["side"] == "BUY":
            if self.no_fill_buy:
                rec = {**o, "status": "EXPIRED", "executedQty": "0", "cummulativeQuoteQty": "0", "fills": []}
                self.orders.append(rec)
                return rec
            spent = float(o["quoteOrderQty"])
            q = spent / self.p[s]
            self.bal["USDT"] -= spent
            self.bal[base] += q * 0.999  # Binance takes its 0.1% fee in the coin bought
            rec = {**o, "status": "FILLED", "executedQty": str(q), "cummulativeQuoteQty": str(spent),
                   "fills": [{"commission": str(q * 0.001), "commissionAsset": base}]}
        else:
            q = float(o["quantity"])
            if q * self.p[s] < 5.0:
                raise BinanceError("400 Filter failure: NOTIONAL", 400)
            assert q <= self.bal[base] + 1e-9
            self.bal[base] -= q
            self.bal["USDT"] += q * self.p[s]
            rec = {**o, "status": "FILLED", "executedQty": str(q), "cummulativeQuoteQty": str(q * self.p[s]), "fills": []}
        rec["clientOrderId"] = o["newClientOrderId"]
        self.orders.append(rec)
        if self.lose_reply:
            self.lose_reply = False
            raise ConnectionResetError("connection reset")
        return rec

    def get_order(self, symbol, client_order_id):
        if self.lookup_down:
            raise ConnectionResetError("network down")
        for r in self.orders:
            if r["clientOrderId"] == client_order_id:
                return r
        raise BinanceError("400 Order does not exist.", 400)


def live_buyer(ex, **over):
    cfg = dict(CFG, **over)
    state = {}
    return WeeklyBuyer(cfg, ex, LiveBroker(ex, cfg), state, log=lambda *_: None), state


class Problems(unittest.TestCase):
    def test_failed_sale_midway_never_sells_your_own_coins(self):
        ex = Exchange()
        b, state = live_buyer(ex, dca_symbols=["BTCUSDT", "ETHUSDT"])
        b.step(MON)
        b.step(MON + WEEK)
        ex.bal["BTC"] += 1.0          # BTC you bought yourself, outside the bot
        ex.p["BTCUSDT"], ex.p["ETHUSDT"] = 200.0, 20.0
        ex.fail_sell = {"ETHUSDT"}    # Binance hiccups halfway through the sale
        with self.assertRaises(BinanceError):
            b.step(MON + WEEK + 3600)
        ex.fail_sell = set()
        b.step(MON + WEEK + 7200)     # next hourly check finishes the job
        self.assertAlmostEqual(ex.bal["BTC"], 1.0, places=6)  # your own BTC untouched
        self.assertLess(ex.bal["ETH"], 1e-4)  # only rounding dust left
        self.assertEqual(len(state["sales"]), 1)
        self.assertAlmostEqual(state["sales"][0]["proceeds"], 24.0 * 0.999 * 0.999, delta=0.01)

    def test_small_leftover_is_carried_over_not_stranded(self):
        ex = Exchange()
        b, state = live_buyer(ex, dca_symbols=["BTCUSDT", "SOLUSDT", "ETHUSDT"])
        for w in range(3):
            b.step(MON + w * WEEK)
        ex.p["BTCUSDT"], ex.p["ETHUSDT"], ex.p["SOLUSDT"] = 200.0, 20.0, 0.7  # SOL worth 4.2, under the minimum
        b.step(MON + 2 * WEEK + 3600)
        self.assertEqual(len(state["sales"]), 1)
        self.assertEqual(state["stranded"], {})
        self.assertIn("SOLUSDT", state["holdings"])           # kept for the next round
        self.assertAlmostEqual(state["invested"], state["holdings"]["SOLUSDT"] * 0.7, places=6)

    def test_unfilled_buy_is_not_recorded_as_a_buy(self):
        ex = Exchange()
        b, state = live_buyer(ex, dca_symbols=["BTCUSDT"])
        ex.no_fill_buy = True
        self.assertFalse(b.step(MON))
        self.assertEqual((state["buys"], state["invested"]), ([], 0.0))
        ex.no_fill_buy = False
        self.assertTrue(b.step(MON + 3600))  # tries again later the same week

    def test_delisting_while_running_is_noticed(self):
        status = ["TRADING"]

        class C(BinanceClient):
            def _request(self, method, path, params=None, signed=False):
                return {"symbols": [{"baseAsset": "EOS", "quoteAsset": "USDT", "status": status[0], "filters": [
                    {"filterType": "LOT_SIZE", "stepSize": "0.1", "minQty": "0.1"},
                    {"filterType": "NOTIONAL", "minNotional": "5"}]}]}

        c = C()
        c.cache_seconds = 0
        self.assertTrue(c.symbol_info("EOSUSDT")["trading"])
        status[0] = "BREAK"
        self.assertFalse(c.symbol_info("EOSUSDT")["trading"])

    def test_clock_drift_is_fixed_automatically(self):
        calls = []

        class C(BinanceClient):
            def _request(self, method, path, params=None, signed=False):
                calls.append(path)
                if path == "/api/v3/time":
                    return {"serverTime": 0}
                if len(calls) == 1:
                    raise BinanceError('400 /api/v3/account: {"code":-1021,"msg":"Timestamp for this request '
                                       'is outside of the recvWindow."}', 400)
                return {"balances": [{"asset": "USDT", "free": "7"}]}

        self.assertEqual(C(api_key="k", api_secret="s").balances()["USDT"], 7.0)

    def test_second_copy_of_the_bot_refuses_to_start(self):
        with tempfile.TemporaryDirectory() as d:
            first = main.acquire_lock(os.path.join(d, "state.json"))
            self.assertIsNotNone(first)
            self.assertIsNone(main.acquire_lock(os.path.join(d, "state.json")))

    def test_bad_settings_are_reported_clearly(self):
        bad = dict(CFG, dca_day="mon", dca_amount=3, dca_symbols=[], dca_take_profit=30)
        problems = " ".join(main.check_config(bad))
        for word in ("dca_day", "dca_amount", "dca_symbols", "dca_take_profit"):
            self.assertIn(word, problems)
        self.assertEqual(main.check_config(CFG), [])

    def test_corrupt_history_file_is_reported_not_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "state.json")
            with open(p, "w") as fh:
                fh.write('{"buys": [')  # cut off, e.g. phone died while saving an older version
            with self.assertRaises(SystemExit):
                main.load_state(p)
            with open(p) as fh:
                self.assertEqual(fh.read(), '{"buys": [')


@mock.patch("bot.binance.time.sleep", lambda s: None)
class UnknownOutcomes(unittest.TestCase):
    def restart(self, b, ex, cfg_over):
        """Simulate the phone dying: rebuild the bot from the saved history file."""
        state = json.loads(json.dumps(b.state))
        cfg = dict(CFG, **cfg_over)
        return WeeklyBuyer(cfg, ex, LiveBroker(ex, cfg), state, log=lambda *_: None), state

    def test_buy_with_unknown_outcome_is_checked_not_repeated(self):
        ex = Exchange()
        over = {"dca_symbols": ["BTCUSDT"]}
        b, state = live_buyer(ex, **over)
        ex.lose_reply = ex.lookup_down = True
        with self.assertRaises(OSError):
            b.step(MON)
        self.assertIn("pending_buy", state)
        b, state = self.restart(b, ex, over)
        ex.lookup_down = False
        b.step(MON + 3600)
        self.assertEqual(len([o for o in ex.orders if o["side"] == "BUY"]), 1)  # bought once, not twice
        self.assertEqual(len(state["buys"]), 1)
        self.assertAlmostEqual(state["holdings"]["BTCUSDT"], ex.bal["BTC"], places=9)

    def test_buy_that_never_happened_is_retried(self):
        ex = Exchange()
        b, state = live_buyer(ex, dca_symbols=["BTCUSDT"])
        ex.lookup_down = True
        with mock.patch.object(ex, "order", side_effect=ConnectionResetError("reset")):
            with self.assertRaises(OSError):
                b.step(MON)
        ex.lookup_down = False
        self.assertTrue(b.step(MON + 3600))
        self.assertEqual(len(ex.orders), 1)

    def test_sale_with_unknown_outcome_never_sells_your_own_coins(self):
        ex = Exchange()
        over = {"dca_symbols": ["BTCUSDT"]}
        b, state = live_buyer(ex, **over)
        b.step(MON)
        ex.bal["BTC"] += 1.0  # yours, bought outside the bot
        ex.p["BTCUSDT"] = 200.0
        ex.lose_reply = ex.lookup_down = True
        with self.assertRaises(OSError):
            b.step(MON + 3600)
        b, state = self.restart(b, ex, over)
        ex.lookup_down = False
        b.step(MON + 7200)
        self.assertEqual(len([o for o in ex.orders if o["side"] == "SELL"]), 1)
        self.assertAlmostEqual(ex.bal["BTC"], 1.0, places=4)
        self.assertEqual(len(state["sales"]), 1)
        self.assertGreater(state["sales"][0]["profit"], 5)


if __name__ == "__main__":
    unittest.main()
