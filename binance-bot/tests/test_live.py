"""Live-broker behaviour against a pretend exchange (no network)."""

import os
import socket
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot.binance import BinanceError, LiveBroker  # noqa: E402
from bot.dca import WeeklyBuyer  # noqa: E402
from main import load_config  # noqa: E402

CFG = load_config("/nonexistent")
MON = 1792972800  # 2026-10-26 00:00 UTC, a Monday
WEEK = 7 * 86400


class FakeExchange:
    """Market orders only, with Binance's fee and error behaviour."""

    def __init__(self, price=100.0, usdt=100.0):
        self.p = price
        self.bal = {"USDT": usdt, "BTC": 0.0}
        self.orders = []
        self.timeout_next_order = False
        self.reject_next_order = False
        self.drop_next_order = False

    def sync_time(self):
        pass

    def price(self, symbol):
        return self.p

    def symbol_info(self, symbol):
        return {"base": "BTC", "quote": "USDT", "step": 0.00001, "min_qty": 0.00001,
                "min_notional": 5.0, "quote_precision": 8, "trading": True}

    def balances(self):
        return dict(self.bal)

    def order(self, **p):
        if self.reject_next_order:
            self.reject_next_order = False
            raise BinanceError("400 Account has insufficient balance.", 400)
        if self.drop_next_order:
            self.drop_next_order = False
            raise ConnectionResetError("connection reset")  # never reached Binance
        o = {"clientOrderId": p["newClientOrderId"], "status": "FILLED", "fills": [], **p}
        if p["side"] == "BUY":
            spent = float(p["quoteOrderQty"])
            qty = spent / self.p
            self.bal["USDT"] -= spent
            self.bal["BTC"] += qty * 0.999
            o.update(executedQty=str(qty), cummulativeQuoteQty=str(spent),
                     fills=[{"commission": str(qty * 0.001), "commissionAsset": "BTC"}])
        else:
            q = float(p["quantity"])
            assert q <= self.bal["BTC"] + 1e-12, "selling more than held"
            self.bal["BTC"] -= q
            self.bal["USDT"] += q * self.p * 0.999
            o.update(executedQty=str(q), cummulativeQuoteQty=str(q * self.p))
        self.orders.append(o)
        if self.timeout_next_order:
            self.timeout_next_order = False
            raise socket.timeout("timed out")  # order went through, reply was lost
        return o

    def get_order(self, symbol, client_order_id):
        for o in self.orders:
            if o["clientOrderId"] == client_order_id:
                return o
        raise BinanceError("400 Order does not exist.", 400)


class LiveOrders(unittest.TestCase):
    def setUp(self):
        self.ex = FakeExchange()
        self.broker = LiveBroker(self.ex, CFG)

    def test_lost_reply_does_not_double_buy(self):
        self.ex.timeout_next_order = True
        qty, avg, spent = self.broker.buy("BTCUSDT", 50.0, "id1")
        self.assertGreater(qty, 0)
        self.assertEqual(len(self.ex.orders), 1)

    def test_rejected_order_is_not_retried(self):
        self.ex.reject_next_order = True
        with self.assertRaises(BinanceError):
            self.broker.buy("BTCUSDT", 50.0, "id1")
        self.assertEqual(self.ex.orders, [])

    def test_order_that_never_arrived_raises(self):
        self.ex.drop_next_order = True
        with self.assertRaises(OSError):
            self.broker.buy("BTCUSDT", 50.0, "id1")
        self.assertEqual(self.ex.orders, [])

    def test_buy_quantity_is_net_of_fee(self):
        qty, avg, spent = self.broker.buy("BTCUSDT", 50.0, "id1")
        self.assertAlmostEqual(qty, self.ex.bal["BTC"])
        self.assertAlmostEqual(avg, 100.0)

    def test_sell_never_exceeds_what_is_held(self):
        self.broker.buy("BTCUSDT", 50.0, "id1")
        self.assertGreater(self.broker.sell("BTCUSDT", 10.0, "id2"), 0)  # asks for far more than held
        self.assertLess(self.ex.bal["BTC"], 1e-4)


class LiveWeeklyBuy(unittest.TestCase):
    def buyer(self, **over):
        ex = FakeExchange()
        state = {}
        cfg = dict(CFG, dca_symbols=["BTCUSDT"], **over)
        return WeeklyBuyer(cfg, ex, LiveBroker(ex, cfg), state, log=lambda *_: None), ex, state

    def test_lost_reply_is_still_recorded_once(self):
        b, ex, state = self.buyer()
        ex.timeout_next_order = True
        self.assertTrue(b.step(MON))
        self.assertEqual(len(ex.orders), 1)
        self.assertAlmostEqual(state["invested"], 6.0)

    def test_waits_when_wallet_is_short(self):
        b, ex, state = self.buyer()
        ex.bal["USDT"] = 4.0
        self.assertFalse(b.step(MON))
        ex.bal["USDT"] = 50.0
        self.assertTrue(b.step(MON + 3600))  # retried later the same week
        self.assertEqual(len(ex.orders), 1)

    def test_take_profit_sells_real_holdings(self):
        b, ex, state = self.buyer(dca_take_profit=0.30)
        b.step(MON)
        b.step(MON + WEEK)
        ex.p = 140.0
        b.step(MON + WEEK + 86400)
        self.assertEqual(len(state["sales"]), 1)
        self.assertLess(ex.bal["BTC"], 1e-4)  # only dust left
        self.assertAlmostEqual(ex.bal["USDT"], 100 - 12 + state["sales"][0]["proceeds"], delta=0.05)
        self.assertGreater(state["realized"], 12 * 0.30)


if __name__ == "__main__":
    unittest.main()
