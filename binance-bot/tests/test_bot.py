import math
import os
import random
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bot import backtest, learner  # noqa: E402
from bot.binance import BinanceError, PaperBroker, floor_to_step, fmt  # noqa: E402
from bot.dca import WeeklyBuyer, week_and_day  # noqa: E402
from bot.replay import simulate  # noqa: E402
from bot.indicators import atr, ema, highest_prior, rsi, sma  # noqa: E402
from bot.strategies import STRATEGIES  # noqa: E402
from bot.trader import Trader  # noqa: E402
from main import load_config  # noqa: E402

CFG = load_config("/nonexistent")
HOUR = 3_600_000


def make_candles(n, drift=0.0, vol=0.01, seed=1, start=100.0):
    rnd = random.Random(seed)
    out, price = [], start
    for i in range(n):
        o = price
        c = o * math.exp(drift + rnd.gauss(0, vol))
        h = max(o, c) * (1 + abs(rnd.gauss(0, vol / 2)))
        lo = min(o, c) * (1 - abs(rnd.gauss(0, vol / 2)))
        out.append({"t": i * HOUR, "o": o, "h": h, "l": lo, "c": c, "v": 1.0, "close_time": (i + 1) * HOUR - 1})
        price = c
    return out


class Indicators(unittest.TestCase):
    def test_sma_and_ema(self):
        self.assertEqual(sma([1, 2, 3, 4], 2), [None, 1.5, 2.5, 3.5])
        e = ema([1, 2, 3, 4, 5], 3)
        self.assertEqual(e[:2], [None, None])
        self.assertAlmostEqual(e[2], 2.0)
        self.assertAlmostEqual(e[3], 3.0)

    def test_ema_skips_leading_none(self):
        self.assertEqual(ema([None, None, 1, 1, 1], 2)[3], 1.0)

    def test_rsi_extremes(self):
        self.assertEqual(rsi(list(range(1, 20)), 14)[-1], 100.0)
        self.assertLess(rsi(list(range(20, 1, -1)), 14)[-1], 1.0)

    def test_prior_window_excludes_current_bar(self):
        self.assertEqual(highest_prior([1, 5, 2, 9], 2), [None, None, 5, 5])

    def test_atr_positive(self):
        a = atr(make_candles(50), 14)
        self.assertIsNone(a[12])
        self.assertGreater(a[-1], 0)


class Backtest(unittest.TestCase):
    def test_sizing_respects_risk_and_minimum(self):
        cfg = dict(CFG, risk_per_trade=0.01, max_position_pct=0.95, min_notional=5)
        amount = backtest.position_quote_amount(1000, 1000, 100, 95, cfg)
        self.assertAlmostEqual(amount, 200.0)  # 1% of 1000 risked over a 5% stop
        self.assertEqual(backtest.position_quote_amount(10, 10, 100, 99.99, dict(cfg, max_position_pct=0.1)), 0.0)

    def test_fees_cost_money_on_flat_market(self):
        candles = [{"t": i, "o": 100, "h": 100.5, "l": 99.5, "c": 100, "v": 1, "close_time": i} for i in range(300)]

        class Always:
            def signals(self, cs, p):
                return [i % 2 == 0 for i in range(len(cs))], [i % 2 == 1 for i in range(len(cs))]

        res = backtest.run(candles, Always(), {"stop_atr": 3.0}, CFG)
        self.assertGreater(res["trades"], 50)
        self.assertLess(res["total_return"], 0)

    def test_every_strategy_runs(self):
        candles = make_candles(600, drift=0.001)
        for strat in STRATEGIES.values():
            for params in strat.grid():
                res = backtest.run(candles, strat, params, CFG)
                self.assertGreaterEqual(res["end_equity"], 0)
                self.assertLessEqual(res["max_drawdown"], 1)

    def test_compounding_grows_position_with_equity(self):
        small = backtest.position_quote_amount(100, 100, 10, 9, CFG)
        big = backtest.position_quote_amount(200, 200, 10, 9, CFG)
        self.assertAlmostEqual(big, 2 * small)


class Learner(unittest.TestCase):
    def test_report_shape(self):
        history = {"UPUSDT": make_candles(1200, drift=0.0015, seed=3), "NOISEUSDT": make_candles(1200, seed=4)}
        report = learner.learn(history, CFG)
        self.assertIn("rows", report)
        for row in report["rows"]:
            self.assertIn(row["symbol"], history)
        if report["champion"]:
            self.assertTrue(report["champion"]["passed"])
            self.assertGreater(report["champion"]["test"]["total_return"], 0)
        self.assertIsInstance(learner.format_report(report), str)


class Rounding(unittest.TestCase):
    def test_floor_to_step(self):
        self.assertEqual(fmt(floor_to_step(0.123456, 0.001)), "0.123")
        self.assertEqual(fmt(floor_to_step(12.9, 1)), "12")


class FakeClient:
    """Serves a scripted price path one candle per step."""

    def __init__(self, candles):
        self.all, self.i = candles, 400

    def closed_klines(self, symbol, interval, total):
        return self.all[max(0, self.i - total):self.i]

    def price(self, symbol):
        return self.all[self.i - 1]["c"]

    def symbol_info(self, symbol):
        return {"min_notional": 5.0}


class TraderLoop(unittest.TestCase):
    def champion_report(self, now):
        return {"learned_at": now, "rows": [], "champion": {
            "symbol": "XUSDT", "strategy": "turtle", "inspired_by": "", "params": {"entry_n": 20, "exit_n": 10, "stop_atr": 2.0}}}

    def test_paper_trades_and_keeps_state_consistent(self):
        up = make_candles(250, drift=0.004, vol=0.004, seed=5)
        down = make_candles(250, drift=-0.004, vol=0.004, seed=6, start=up[-1]["c"])
        candles = up + down
        for i, c in enumerate(candles):
            c["t"], c["close_time"] = i * HOUR, (i + 1) * HOUR - 1
        client = FakeClient(candles)
        state = {}
        cfg = dict(CFG, max_drawdown=0.9)
        trader = Trader(cfg, client, PaperBroker(client, cfg, state), state, log=lambda *_: None)
        state["report"] = self.champion_report(10 ** 12)
        client.i = 200
        for _ in range(299):
            client.i += 1
            trader.step(now=10 ** 12)
        self.assertGreater(len(state["trades"]), 0)
        total_pnl = sum(t["pnl"] for t in state["trades"])
        equity = trader.equity()
        self.assertAlmostEqual(equity, cfg["start_equity"] + total_pnl + (
            state["position"]["qty"] * client.price("X") - state["position"]["cost"] if state["position"] else 0), places=6)

    def test_kill_switch_halts(self):
        candles = make_candles(500, seed=7)
        client = FakeClient(candles)
        state = {"peak_equity": 1000.0}
        trader = Trader(CFG, client, PaperBroker(client, CFG, state), state, log=lambda *_: None)
        state["report"] = self.champion_report(10 ** 12)
        trader.step(now=10 ** 12)
        self.assertTrue(state["halted"])

    def test_vault_keeps_part_of_profit(self):
        client = FakeClient(make_candles(500, seed=8))
        state = {}
        cfg = dict(CFG, reinvest_pct=0.5)
        trader = Trader(cfg, client, PaperBroker(client, cfg, state), state, log=lambda *_: None)
        state["position"] = {"symbol": "X", "strategy": "turtle", "cost": 10.0, "opened": 0}
        trader.close_position(14.0, "test")
        self.assertAlmostEqual(state["vault"], 2.0)


class Replay(unittest.TestCase):
    def test_replay_uses_only_closed_candles_and_reconciles(self):
        history = {"AUSDT": make_candles(700, drift=0.002, seed=11), "BUSDT": make_candles(700, seed=12)}
        cfg = dict(CFG, symbols=list(history), learn_candles=400, relearn_hours=24 * 7, max_drawdown=0.9)
        state, curve = simulate(history, cfg, warmup_candles=400)
        self.assertEqual(len(curve), 300)
        pnl = sum(t["pnl"] for t in state["trades"])
        if not state["position"]:
            self.assertAlmostEqual(curve[-1][1], cfg["start_equity"] + pnl, places=6)


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

    def quote_balance(self):
        return 1.0


MON = 1792972800  # 2026-10-26 00:00 UTC, a Monday
DAY = 86400


class WeeklyBuy(unittest.TestCase):
    def buyer(self, **over):
        client = FixedPriceClient()
        state = {}
        cfg = dict(CFG, **over)
        return WeeklyBuyer(cfg, client, PaperBroker(client, cfg, state), state, log=lambda *_: None), state

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
        self.assertAlmostEqual(state["paper_cash"], 60 - 6 + state["sales"][0]["proceeds"])
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


if __name__ == "__main__":
    unittest.main()
