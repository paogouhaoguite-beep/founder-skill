"""CoinDCX connection: request format, and order handling against a pretend CoinDCX."""

import hashlib
import hmac
import json
import os
import sys
import unittest
from decimal import Decimal
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main  # noqa: E402
from bot.coindcx import CoinDCXBroker, CoinDCXClient, dumps  # noqa: E402
from bot.dca import WeeklyBuyer  # noqa: E402
from bot.exchange import ExchangeError  # noqa: E402

CFG = main.load_config("/nonexistent")  # the shipped defaults: CoinDCX, rupees
MON = 1792972800  # 2026-10-26 00:00 UTC, a Monday
WEEK = 7 * 86400

# copied from CoinDCX's live API (markets_details and ticker), October 2026
BTCINR_MARKET = {"coindcx_name": "BTCINR", "base_currency_short_name": "INR", "target_currency_short_name": "BTC",
                 "base_currency_precision": 1, "target_currency_precision": 5, "min_quantity": 1e-05,
                 "max_quantity": 2, "min_notional": 100, "step": 1e-05,
                 "order_types": ["limit_order", "market_order"], "status": "active"}
BTCINR_TICKER = {"market": "BTCINR", "last_price": "8259814.2000000000", "bid": "8220631.7000000000",
                 "ask": "8260740.3000000000", "timestamp": 1792502198}


class RequestFormat(unittest.TestCase):
    def test_small_quantities_are_plain_numbers(self):
        out = dumps({"total_quantity": Decimal("0.00006"), "market": "BTCINR", "timestamp": 1})
        self.assertEqual(out, '{"total_quantity":0.00006,"market":"BTCINR","timestamp":1}')
        self.assertEqual(json.loads(out)["total_quantity"], 0.00006)

    def test_signature_is_hmac_of_the_exact_body_sent(self):
        sent = {}

        class Resp:
            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

            def read(self):
                return b'[{"currency":"INR","balance":"1234.5","locked_balance":"0"}]'

        def fake_urlopen(req, timeout):
            sent["req"] = req
            return Resp()

        c = CoinDCXClient(api_key="k", api_secret="s")
        with mock.patch("bot.coindcx.urlopen", fake_urlopen):
            self.assertEqual(c.balances()["INR"], 1234.5)
        req = sent["req"]
        self.assertEqual(req.get_method(), "POST")
        self.assertTrue(req.full_url.endswith("/exchange/v1/users/balances"))
        body = req.data
        self.assertIn(b'"timestamp":', body)
        expected = hmac.new(b"s", body, hashlib.sha256).hexdigest()
        self.assertEqual(req.get_header("X-auth-signature"), expected)
        self.assertEqual(req.get_header("X-auth-apikey"), "k")
        self.assertNotIn("Python-urllib", req.get_header("User-agent", ""))  # blocked by CoinDCX's firewall

    def test_market_details_and_prices_are_read_correctly(self):
        c = CoinDCXClient()
        inactive = dict(BTCINR_MARKET, coindcx_name="OLDINR", status="inactive")
        responses = {"/exchange/v1/markets_details": [BTCINR_MARKET, inactive], "/exchange/ticker": [BTCINR_TICKER]}
        with mock.patch.object(c, "_request", lambda m, path, body=None: responses[path]):
            info = c.symbol_info("BTCINR")
            self.assertEqual((info["base"], info["quote"], info["min_notional"], info["trading"]), ("BTC", "INR", 100.0, True))
            self.assertFalse(c.symbol_info("OLDINR")["trading"])
            self.assertEqual(c.sell_price("BTCINR"), 8220631.7)   # what you could sell at
            self.assertEqual(c.buy_price("BTCINR"), 8260740.3)    # what you would pay
            with self.assertRaises(ExchangeError):
                c.symbol_info("NOPEINR")


class FakeCoinDCX:
    """Behaves like CoinDCX's docs: orders start as 'init' and fill a moment later."""

    def __init__(self):
        self.bid, self.ask = 8_220_000.0, 8_260_000.0
        self.bal = {"INR": 10_000.0, "BTC": 0.0}
        self.orders = {}
        self.polls_until_filled = 1
        self.create_error = None        # raise this on create (after placing, if placed_anyway)
        self.placed_anyway = False
        self.status_error = None        # raise this on status lookups
        self.never_fill = False

    def symbol_info(self, s):
        return {"base": "BTC", "quote": "INR", "step": 1e-05, "min_qty": 1e-05, "min_notional": 100.0,
                "qty_precision": 5, "trading": True}

    def price(self, s):
        return (self.bid + self.ask) / 2

    def buy_price(self, s):
        return self.ask

    def sell_price(self, s):
        return self.bid

    def balances(self):
        return dict(self.bal)

    def create_order(self, **o):
        q = float(o["total_quantity"])
        if self.create_error and not self.placed_anyway:
            e, self.create_error = self.create_error, None
            raise e
        if o["side"] == "buy" and q * self.ask * 1.0059 > self.bal["INR"]:
            raise ExchangeError("400 Insufficient funds", 400)
        rec = {"client_order_id": o["client_order_id"], "market": o["market"], "side": o["side"],
               "status": "init", "total_quantity": q, "remaining_quantity": q, "avg_price": 0, "fee_amount": 0,
               "polls": 0}
        self.orders[o["client_order_id"]] = rec
        if self.create_error:
            e, self.create_error = self.create_error, None
            raise e  # it was placed, but the reply failed
        return dict(rec)

    def _fill(self, rec):
        q = rec["total_quantity"]
        if rec["side"] == "buy":
            px = self.ask
            fee = q * px * 0.0059
            self.bal["INR"] -= q * px + fee
            self.bal["BTC"] += q
        else:
            px = self.bid
            fee = q * px * 0.0059
            self.bal["BTC"] -= q
            self.bal["INR"] += q * px - fee - q * px * 0.01  # fee and 1% TDS withheld
        rec.update(status="filled", remaining_quantity=0, avg_price=px, fee_amount=fee)

    def order_status(self, cid):
        if self.status_error:
            raise self.status_error
        rec = self.orders.get(cid)
        if rec is None:
            raise ExchangeError("404 Order not found", 404)
        rec["polls"] += 1
        if rec["status"] == "init" and not self.never_fill and rec["polls"] >= self.polls_until_filled:
            self._fill(rec)
        return dict(rec)


def buyer(ex, **over):
    cfg = dict(CFG, dca_symbols=["BTCINR"], **over)
    broker = CoinDCXBroker(ex, cfg, wait_seconds=5, sleep=lambda s: None)
    state = {}
    return WeeklyBuyer(cfg, ex, broker, state, log=lambda *_: None), state


class CoinDCXOrders(unittest.TestCase):
    def test_weekly_500_rupee_buy(self):
        ex = FakeCoinDCX()
        b, state = buyer(ex)
        self.assertTrue(b.step(MON))
        buy = state["buys"][0]
        self.assertAlmostEqual(buy["qty"], 0.00006)              # 500 rupees of BTC, rounded down to CoinDCX's step
        self.assertLessEqual(buy["spent"], 500.0)                 # price plus fee stays within the 500
        self.assertAlmostEqual(10_000 - ex.bal["INR"], buy["spent"], places=6)
        self.assertAlmostEqual(state["holdings"]["BTCINR"], ex.bal["BTC"])

    def test_waits_for_the_fill(self):
        ex = FakeCoinDCX()
        ex.polls_until_filled = 3
        b, state = buyer(ex)
        self.assertTrue(b.step(MON))
        self.assertEqual(len(ex.orders), 1)

    def test_unconfirmed_order_is_checked_later_not_repeated(self):
        ex = FakeCoinDCX()
        ex.never_fill = True
        b, state = buyer(ex)
        with mock.patch("bot.coindcx.time.time", side_effect=[0, 0] + [100] * 50):
            with self.assertRaises(ExchangeError):
                b.step(MON)
        self.assertIn("pending_buy", state)
        ex.never_fill = False
        b.step(MON + 3600)
        self.assertEqual(len(ex.orders), 1)
        self.assertEqual(len(state["buys"]), 1)

    def test_outage_after_the_order_was_placed_does_not_double_buy(self):
        ex = FakeCoinDCX()
        ex.create_error, ex.placed_anyway = ExchangeError("502 Bad gateway", 502), True
        b, state = buyer(ex)
        self.assertTrue(b.step(MON))
        self.assertEqual(len(ex.orders), 1)

    def test_rate_limited_lookup_is_not_mistaken_for_no_order(self):
        ex = FakeCoinDCX()
        ex.never_fill = True
        b, state = buyer(ex)
        with mock.patch("bot.coindcx.time.time", side_effect=[0, 0] + [100] * 50):
            with self.assertRaises(ExchangeError):
                b.step(MON)
        ex.never_fill = False
        ex.status_error = ExchangeError("429 Too Many Requests", 429)
        with self.assertRaises(ExchangeError):
            b.step(MON + 3600)  # cannot check yet: must not buy again
        ex.status_error = None
        b.step(MON + 7200)
        self.assertEqual(len(ex.orders), 1)
        self.assertEqual(len(state["buys"]), 1)

    def test_too_small_amount_is_refused_not_recorded(self):
        ex = FakeCoinDCX()
        b, state = buyer(ex, dca_amount=50)
        self.assertFalse(b.step(MON))  # below CoinDCX's 100-rupee minimum
        self.assertEqual(ex.orders, {})

    def test_profit_sale_pays_out_rupees_after_fee_and_tds(self):
        ex = FakeCoinDCX()
        b, state = buyer(ex, dca_take_profit=0.30)
        b.step(MON)
        b.step(MON + WEEK)
        invested = state["invested"]
        ex.bid = 8_260_000.0 * 1.30   # +30% on the price alone is not enough after fee and TDS
        b.step(MON + WEEK + 3600)
        self.assertEqual(state["sales"], [])
        ex.bid = 8_260_000.0 * 1.34
        inr_before = ex.bal["INR"]
        b.step(MON + WEEK + 7200)
        self.assertEqual(len(state["sales"]), 1)
        received = ex.bal["INR"] - inr_before
        self.assertAlmostEqual(state["sales"][0]["proceeds"], received, places=6)
        self.assertGreaterEqual(received, invested * 1.30)   # +30% really arrived
        self.assertLess(ex.bal["BTC"], 1e-9)


class Settings(unittest.TestCase):
    def test_defaults_are_coindcx_in_rupees(self):
        self.assertEqual((CFG["exchange"], CFG["currency"]), ("coindcx", "INR"))
        self.assertEqual(main.check_config(CFG), [])

    def test_old_binance_config_gets_clear_messages(self):
        old = dict(CFG, dca_amount=6, dca_symbols=["BTCUSDT", "ETHUSDT"], fee_rate=0.001)
        problems = " ".join(main.check_config(old))
        self.assertIn("BTCINR", problems)
        self.assertIn("at least 100", problems)

    def test_fees_always_come_from_the_exchange(self):
        cfg = main.exchange_settings(dict(CFG, fee_rate=0.001))
        self.assertEqual(cfg["fee_rate"], 0.0059)


if __name__ == "__main__":
    unittest.main()
