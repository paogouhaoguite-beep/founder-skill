"""Live-broker behaviour against a pretend exchange (no network)."""

import os
import socket
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bot.binance import BinanceError, LiveBroker  # noqa: E402
from bot.dca import WeeklyBuyer  # noqa: E402
from bot.trader import Trader  # noqa: E402
from test_bot import HOUR, make_candles  # noqa: E402
from main import load_config  # noqa: E402

CFG = load_config("/nonexistent")


class FakeExchange:
    def __init__(self, price=100.0, usdt=100.0):
        self.p = price
        self.bal = {"USDT": usdt, "BTC": 0.0}
        self.locked = {"BTC": 0.0}
        self.orders = {}
        self.next_id = 1
        self.timeout_next_order = False
        self.reject_next_order = False
        self.drop_next_order = False
        self.time_offset = 0
        self.candles, self.i = [], 0

    def sync_time(self):
        pass

    def price(self, symbol):
        return self.p

    def symbol_info(self, symbol):
        return {"base": "BTC", "quote": "USDT", "step": 0.00001, "min_qty": 0.00001, "tick": 0.01,
                "min_notional": 5.0, "quote_precision": 8}

    def balances(self):
        return dict(self.bal)

    def closed_klines(self, symbol, interval, total):
        return self.candles[max(0, self.i - total):self.i]

    def order(self, **p):
        if self.reject_next_order:
            self.reject_next_order = False
            raise BinanceError("400 Account has insufficient balance.", 400)
        if self.drop_next_order:
            self.drop_next_order = False
            raise ConnectionResetError("connection reset")  # never reached Binance
        oid = self.next_id
        self.next_id += 1
        o = {"orderId": oid, "clientOrderId": p.get("newClientOrderId", "x%d" % oid), "status": "NEW",
             "executedQty": "0", "cummulativeQuoteQty": "0", "fills": [], **p}
        if p["type"] == "MARKET" and p["side"] == "BUY":
            spent = float(p["quoteOrderQty"])
            qty = spent / self.p
            self.bal["USDT"] -= spent
            self.bal["BTC"] += qty * 0.999
            o.update(status="FILLED", executedQty=str(qty), cummulativeQuoteQty=str(spent),
                     fills=[{"commission": str(qty * 0.001), "commissionAsset": "BTC"}])
        elif p["type"] == "MARKET" and p["side"] == "SELL":
            q = float(p["quantity"])
            assert q <= self.bal["BTC"] + 1e-12, "selling more than held"
            self.bal["BTC"] -= q
            self.bal["USDT"] += q * self.p * 0.999
            o.update(status="FILLED", executedQty=str(q), cummulativeQuoteQty=str(q * self.p))
        else:  # STOP_LOSS_LIMIT rests on the book and locks the coins
            q = float(p["quantity"])
            self.bal["BTC"] -= q
            self.locked["BTC"] += q
        self.orders[oid] = o
        if self.timeout_next_order:
            self.timeout_next_order = False
            raise socket.timeout("timed out")  # order went through, reply was lost
        return o

    def fill_stop(self, oid, fraction=1.0, price=None):
        o = self.orders[oid]
        q = float(o["quantity"]) * fraction
        px = price or float(o["price"])
        self.locked["BTC"] -= q
        self.bal["USDT"] += q * px * 0.999
        o.update(status="FILLED" if fraction == 1.0 else "PARTIALLY_FILLED",
                 executedQty=str(q), cummulativeQuoteQty=str(q * px))

    def cancel_order(self, symbol, oid):
        o = self.orders[oid]
        if o["status"] == "FILLED":
            raise BinanceError("400 Unknown order sent.", 400)
        rest = float(o["quantity"]) - float(o["executedQty"])
        self.locked["BTC"] -= rest
        self.bal["BTC"] += rest
        o["status"] = "CANCELED"
        return o

    def get_order(self, symbol, oid=None, client_order_id=None):
        if client_order_id is not None:
            for o in self.orders.values():
                if o["clientOrderId"] == client_order_id:
                    return o
            raise BinanceError("400 Order does not exist.", 400)
        return self.orders[oid]


def open_position(ex, broker, amount=50.0):
    qty, avg = broker.buy("BTCUSDT", amount)
    pos = {"symbol": "BTCUSDT", "qty": qty, "stop": 95.0, "cost": amount}
    pos["stop_id"] = broker.place_stop("BTCUSDT", qty, pos["stop"])
    return pos


class LiveExits(unittest.TestCase):
    def setUp(self):
        self.ex = FakeExchange()
        self.broker = LiveBroker(self.ex, CFG, {})

    def test_exit_after_stop_already_filled_reports_real_proceeds(self):
        pos = open_position(self.ex, self.broker)
        self.ex.fill_stop(pos["stop_id"])  # stop fills between two checks
        proceeds = self.broker.exit_position(pos)
        self.assertGreater(proceeds, 40)  # not recorded as a total loss

    def test_gap_through_stop_limit_is_sold_at_market(self):
        pos = open_position(self.ex, self.broker)
        self.ex.p = 80.0  # crashed straight past the stop AND its limit; order sits unfilled
        proceeds = self.broker.stop_fill(pos, 80.0)
        self.assertIsNotNone(proceeds)
        self.assertLess(self.ex.bal["BTC"] + self.ex.locked["BTC"], 1e-4)

    def test_partial_stop_fill_counts_both_parts(self):
        pos = open_position(self.ex, self.broker)
        self.ex.fill_stop(pos["stop_id"], fraction=0.5, price=94.9)
        self.ex.p = 80.0
        proceeds = self.broker.stop_fill(pos, 80.0)
        self.assertGreater(proceeds, 0.5 * pos["qty"] * 94.9 * 0.99)

    def test_lost_reply_does_not_double_buy(self):
        self.ex.timeout_next_order = True
        qty, avg = self.broker.buy("BTCUSDT", 50.0)
        self.assertGreater(qty, 0)
        self.assertEqual(len(self.ex.orders), 1)

    def test_rejected_order_is_not_retried(self):
        self.ex.reject_next_order = True
        with self.assertRaises(BinanceError):
            self.broker.buy("BTCUSDT", 50.0)
        self.assertEqual(self.ex.orders, {})

    def test_order_that_never_arrived_raises(self):
        self.ex.drop_next_order = True
        with self.assertRaises(OSError):
            self.broker.buy("BTCUSDT", 50.0)
        self.assertEqual(self.ex.orders, {})


class LiveTraderEndToEnd(unittest.TestCase):
    def test_books_match_the_exchange(self):
        up = make_candles(250, drift=0.004, vol=0.004, seed=5)
        down = make_candles(250, drift=-0.004, vol=0.004, seed=6, start=up[-1]["c"])
        candles = up + down
        for i, c in enumerate(candles):
            c["t"], c["close_time"] = i * HOUR, (i + 1) * HOUR - 1
        ex = FakeExchange(usdt=60.0)
        ex.candles = candles
        state = {"report": {"learned_at": 10 ** 12, "rows": [], "champion": {
            "symbol": "BTCUSDT", "strategy": "turtle", "inspired_by": "",
            "params": {"entry_n": 20, "exit_n": 10, "stop_atr": 2.0}}}}
        cfg = dict(CFG, max_drawdown=0.9)
        trader = Trader(cfg, ex, LiveBroker(ex, cfg, state), state, log=lambda *_: None)
        for i in range(200, 500):
            ex.i = i
            ex.p = candles[i - 1]["c"]
            for oid, o in list(ex.orders.items()):  # resting stops fill when price trades through
                if o["type"] == "STOP_LOSS_LIMIT" and o["status"] == "NEW" and candles[i - 1]["l"] <= float(o["stopPrice"]):
                    ex.fill_stop(oid, price=float(o["stopPrice"]))
            trader.step(now=10 ** 12)
        self.assertGreater(len(state["trades"]), 0)
        reasons = {t["reason"] for t in state["trades"]}
        self.assertTrue(reasons & {"stop-loss", "strategy exit"})
        pnl = sum(t["pnl"] for t in state["trades"])
        open_cost = state["position"]["cost"] if state["position"] else 0.0
        # cash on the exchange = start + realised pnl - money tied up in the open trade
        self.assertAlmostEqual(ex.bal["USDT"], 60.0 + pnl - open_cost, delta=0.05)


class LiveWeeklyBuy(unittest.TestCase):
    def test_lost_reply_is_still_recorded_once(self):
        ex = FakeExchange()
        state = {}
        b = WeeklyBuyer(CFG, ex, LiveBroker(ex, CFG, state), state, log=lambda *_: None)
        ex.timeout_next_order = True
        self.assertTrue(b.step(1792972800))
        self.assertEqual(len(ex.orders), 1)
        self.assertAlmostEqual(state["invested"], 6.0)


if __name__ == "__main__":
    unittest.main()
