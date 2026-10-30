"""Second review: problems that would show up in months of real use."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bot.coindcx import CoinDCXBroker  # noqa: E402
from bot.dca import WeeklyBuyer  # noqa: E402
from bot.exchange import ExchangeError  # noqa: E402
from test_coindcx import CFG, MON, WEEK, FakeCoinDCX  # noqa: E402
from test_problems import CFG as BINANCE_CFG  # noqa: E402
from test_problems import Exchange, live_buyer  # noqa: E402


class SellDesk(FakeCoinDCX):
    """CoinDCX that can reject market sells after accepting them, as its docs warn."""

    def __init__(self):
        super().__init__()
        self.reject_sells = 0

    def _fill(self, rec):
        if rec["side"] == "sell" and self.reject_sells:
            self.reject_sells -= 1
            rec.update(status="rejected")  # nothing filled
            return
        super()._fill(rec)


def cdx_buyer(ex, **over):
    cfg = dict(CFG, dca_symbols=["BTCINR"], dca_take_profit=0.30, **over)
    state = {}
    b = WeeklyBuyer(cfg, ex, CoinDCXBroker(ex, cfg, wait_seconds=5, sleep=lambda s: None), state, log=lambda *_: None)
    return b, state


def two_buys_then_rally(ex, b):
    b.step(MON)
    b.step(MON + WEEK)
    ex.bid = ex.ask * 1.40


class Review(unittest.TestCase):
    def test_rejected_sale_keeps_the_coins_and_retries(self):
        ex = SellDesk()
        b, state = cdx_buyer(ex)
        two_buys_then_rally(ex, b)
        held = ex.bal["BTC"]
        ex.reject_sells = 1
        b.step(MON + WEEK + 3600)
        self.assertEqual(state["sales"], [])                       # not recorded as sold
        self.assertAlmostEqual(state["holdings"]["BTCINR"], held)   # coins still tracked
        b.step(MON + WEEK + 7200)                                  # next check sells for real
        self.assertEqual(len(state["sales"]), 1)
        self.assertGreater(state["sales"][0]["proceeds"], 0)
        self.assertLess(ex.bal["BTC"], 1e-9)

    def test_a_sale_that_keeps_failing_is_handed_to_you_not_retried_forever(self):
        ex = SellDesk()
        b, state = cdx_buyer(ex)
        two_buys_then_rally(ex, b)
        ex.reject_sells = 99
        for h in range(1, 10):
            b.step(MON + WEEK + h * 3600)
        self.assertEqual(len(state["sales"]), 1)
        self.assertIn("BTCINR", state["stranded"])

    def test_coins_you_sold_yourself_do_not_block_the_bot(self):
        ex = SellDesk()
        b, state = cdx_buyer(ex)
        two_buys_then_rally(ex, b)
        ex.bal["BTC"] /= 2  # you sold half in the CoinDCX app
        b.step(MON + WEEK + 3600)
        self.assertEqual(len(state["sales"]), 1)
        self.assertNotIn("selling", state)
        self.assertTrue(b.step(MON + 2 * WEEK))  # and weekly buying carries on

    def test_no_weekly_buy_in_the_middle_of_an_unfinished_sale(self):
        ex = SellDesk()
        b, state = cdx_buyer(ex)
        b.step(MON)
        ex.bid = ex.ask * 1.40
        ex.reject_sells = 1
        orders_before = len(ex.orders)
        self.assertFalse(b.step(MON + WEEK))  # sale fails this time, and it is buy day
        buys = [o for o in list(ex.orders.values())[orders_before:] if o["side"] == "buy"]
        self.assertEqual(buys, [])

    def test_nothing_big_enough_to_sell_means_no_fake_sale(self):
        ex = Exchange()
        b, state = live_buyer(ex, dca_symbols=["SOLUSDT"], dca_take_profit=0.30)
        b.step(MON)                     # 6 USDT of SOL
        ex.p["SOLUSDT"] = 0.85          # worth 5.1: still above the 5 minimum
        ex.p["SOLUSDT"] = 0.80          # worth 4.8: below it
        b.cfg["dca_take_profit"] = 0.0001
        state["invested"] = 3.0         # pretend it is "up", but nothing can be sold
        b.step(MON + 3600)
        self.assertEqual(state["sales"], [])

    def test_empty_order_lookup_does_not_freeze_the_bot(self):
        ex = FakeCoinDCX()
        b, state = cdx_buyer(ex)
        state["pending_buy"] = {"id": "botlost", "symbol": "BTCINR", "week": "2026-W44", "time": MON}
        real = ex.order_status
        ex.order_status = lambda cid: {} if cid == "botlost" else real(cid)  # an answer with no order in it
        self.assertTrue(b.step(MON))
        self.assertNotIn("pending_buy", state)

    def test_zero_price_does_not_crash_a_buy(self):
        ex = FakeCoinDCX()
        ex.ask = 0.0
        b, state = cdx_buyer(ex)
        with self.assertRaises(ExchangeError):
            b.step(MON)
        self.assertEqual(ex.orders, {})

    def test_status_works_without_internet(self):
        ex = FakeCoinDCX()
        b, state = cdx_buyer(ex)
        b.step(MON)

        def offline(*a):
            raise OSError("no internet")

        ex.sell_price = offline
        text = b.summary()
        self.assertIn("unavailable", text)
        self.assertIn("1 buys", text)


    def test_binance_sale_that_expires_half_filled_sells_the_rest_later(self):
        ex = Exchange()
        b, state = live_buyer(ex, dca_symbols=["BTCUSDT"], dca_amount=20, dca_take_profit=0.30)
        b.step(MON)
        ex.p["BTCUSDT"] = 150.0
        real_order = ex.order

        def half_filled(**o):
            if o["side"] == "SELL":
                q = float(o["quantity"])
                rec = real_order(**dict(o, quantity=str(q / 2)))
                rec.update(status="EXPIRED", origQty=str(q))  # no more buyers at that moment
                return rec
            return real_order(**o)

        ex.order = half_filled
        b.step(MON + 3600)
        self.assertEqual(state["sales"], [])
        self.assertGreater(state["holdings"]["BTCUSDT"], 0)
        ex.order = real_order
        b.step(MON + 7200)
        self.assertEqual(len(state["sales"]), 1)
        self.assertLess(ex.bal["BTC"], 1e-4)
        self.assertGreater(state["sales"][0]["proceeds"], 20 * 1.3)


if __name__ == "__main__":
    unittest.main()
