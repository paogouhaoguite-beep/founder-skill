import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.binance import BinanceError, PaperBroker, floor_to_step, fmt  # noqa: E402
from bot.dca import WeeklyBuyer, week_and_day  # noqa: E402
from main import load_config  # noqa: E402

CFG = dict(load_config("/nonexistent", exchange="binance"), dca_amount=6, dca_symbols=["BTCUSDT", "ETHUSDT", "SOLUSDT"])


class Rounding(unittest.TestCase):
    def test_floor_to_step(self):
        self.assertEqual(fmt(floor_to_step(0.123456, 0.001)), "0.123")
        self.assertEqual(fmt(floor_to_step(12.9, 1)), "12")


class FixedPriceClient:
    def __init__(self, price=100.0, minimum=5.0):
        self.p, self.minimum = price, minimum
        self.delisted = set()  # removed entirely: Binance answers "Invalid symbol"
        self.halted = set()    # how Binance really shows a delisted coin: listed, not trading, frozen price

    def price(self, symbol):
        if symbol in self.delisted:
            raise BinanceError("400 Invalid symbol.", 400)
        return 0.78 if symbol in self.halted else self.p

    def symbol_info(self, symbol):
        if symbol in self.delisted:
            raise BinanceError("400 Invalid symbol.", 400)
        return {"min_notional": self.minimum, "trading": symbol not in self.halted}


class Broke:
    live = True

    def quote_balance(self, symbol):
        return 1.0


MON = 1792972800  # 2026-10-26 00:00 UTC, a Monday
DAY = 86400


class WeeklyBuy(unittest.TestCase):
    def buyer(self, **over):
        client = FixedPriceClient()
        state = {}
        cfg = dict(CFG, **over)
        return WeeklyBuyer(cfg, client, PaperBroker(client, cfg), state, log=lambda *_: None), state

    def test_monday_is_monday(self):
        self.assertEqual(week_and_day(MON)[1], 0)

    def test_buys_once_per_week_and_catches_up_later_in_week(self):
        b, state = self.buyer(dca_day="wednesday", dca_symbols=["BTCUSDT"])
        self.assertFalse(b.step(MON + DAY))         # Tuesday: not yet
        self.assertTrue(b.step(MON + 4 * DAY))      # bot was off Wednesday, buys Friday
        self.assertFalse(b.step(MON + 5 * DAY))     # not twice in a week
        self.assertTrue(b.step(MON + 9 * DAY))      # next Wednesday
        self.assertEqual(len(state["buys"]), 2)
        self.assertAlmostEqual(state["invested"], 12.0)
        self.assertAlmostEqual(state["holdings"]["BTCUSDT"], 2 * 6 / (100 * 1.0005) * 0.999)

    def test_rotates_symbols(self):
        b, state = self.buyer(dca_symbols=["BTCUSDT", "ETHUSDT"])
        for w in range(3):
            b.step(MON + w * 7 * DAY)
        self.assertEqual([x["symbol"] for x in state["buys"]], ["BTCUSDT", "ETHUSDT", "BTCUSDT"])

    def test_take_profit_sells_at_target_after_fees_and_restarts(self):
        b, state = self.buyer(dca_take_profit=0.20)
        b.step(MON)
        b.client.p = 100 * 1.20  # +20% price is not enough once fees and slippage are paid
        b.step(MON + DAY)
        self.assertEqual(state["sales"], [])
        b.client.p = 100 * 1.25
        b.step(MON + DAY)
        self.assertEqual(len(state["sales"]), 1)
        self.assertGreaterEqual(state["sales"][0]["profit"], 6 * 0.20)
        self.assertEqual((state["invested"], state["holdings"]), (0.0, {}))
        b.step(MON + 7 * DAY)  # next week: a fresh round starts
        self.assertAlmostEqual(state["invested"], 6.0)
        self.assertAlmostEqual(state["total_invested"], 12.0)
        self.assertIn("profit sales", b.summary())

    def test_delisted_coin_is_skipped_and_stranded(self):
        b, state = self.buyer(dca_symbols=["BTCUSDT", "EOSUSDT", "ETHUSDT"], dca_take_profit=0.30)
        for w in range(3):
            b.step(MON + w * 7 * DAY)
        self.assertEqual([x["symbol"] for x in state["buys"]], ["BTCUSDT", "EOSUSDT", "ETHUSDT"])
        b.client.delisted.add("EOSUSDT")
        b.step(MON + 3 * 7 * DAY)
        b.step(MON + 4 * 7 * DAY)  # EOS's turn: skipped, ETH bought instead
        self.assertEqual([x["symbol"] for x in state["buys"]][3:], ["BTCUSDT", "ETHUSDT"])
        b.client.p = 200.0  # the coins it can still price are up enough to sell
        b.step(MON + 4 * 7 * DAY + DAY)
        self.assertEqual(len(state["sales"]), 1)
        self.assertIn("EOSUSDT", state["stranded"])
        self.assertEqual(state["holdings"], {})
        self.assertIn("STRANDED", b.summary())

    def test_halted_coin_with_frozen_price_is_not_counted(self):
        b, state = self.buyer(dca_symbols=["BTCUSDT", "EOSUSDT"], dca_take_profit=0.30)
        b.step(MON)
        b.step(MON + 7 * DAY)
        b.client.halted.add("EOSUSDT")
        state["holdings"]["EOSUSDT"] = 1000.0  # a frozen price that would look like a big gain
        b.step(MON + 7 * DAY + DAY)
        self.assertEqual(state["sales"], [])
        b.step(MON + 14 * DAY)  # BTC's turn
        b.step(MON + 21 * DAY)  # EOS's turn: halted, so BTC is bought instead
        self.assertEqual([x["symbol"] for x in state["buys"]][2:], ["BTCUSDT", "BTCUSDT"])

    def test_never_sells_when_disabled(self):
        b, state = self.buyer(dca_take_profit=None)
        b.step(MON)
        b.client.p = 1000.0
        b.step(MON + DAY)
        self.assertEqual(state["sales"], [])

    def test_skips_below_minimum_and_without_funds(self):
        b, state = self.buyer(dca_amount=3)
        self.assertFalse(b.step(MON))
        client, st = FixedPriceClient(), {}
        live = WeeklyBuyer(CFG, client, Broke(), st, log=lambda *_: None)
        self.assertFalse(live.step(MON))
        self.assertEqual(st["buys"], [])


    def test_status_survives_a_delisted_coin(self):
        b, state = self.buyer(dca_symbols=["BTCUSDT", "EOSUSDT"])
        b.step(MON)
        b.step(MON + 7 * DAY)
        b.client.delisted.add("EOSUSDT")
        quiet = WeeklyBuyer(CFG, b.client, None, state, log=lambda *_: None)
        self.assertIn("this round", quiet.summary())


if __name__ == "__main__":
    unittest.main()
