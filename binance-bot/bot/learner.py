"""Walk-forward learning: tune on older candles, then prove it on newer ones.

For every symbol and strategy the learner grid-searches the settings on the
first part of the history (train) and then runs the single best setting on
the most recent part it has never seen (test). Only a strategy that also made
money on the unseen part, with an acceptable drawdown and enough trades, can
become the champion. If nothing passes, the bot does not trade at all.
"""

import time

from . import backtest
from .strategies import STRATEGIES, params_to_json


def learn(history, cfg):
    rows = []
    split_frac = cfg["train_fraction"]
    for symbol, candles in history.items():
        split = int(len(candles) * split_frac)
        if split < 250 or len(candles) - split < 50:
            continue
        train = candles[:split]
        for strat in STRATEGIES.values():
            best, best_score = None, None
            for params in strat.grid():
                res = backtest.run(train, strat, params, cfg)
                s = backtest.score(res, cfg["min_trades_train"])
                if s is not None and (best_score is None or s > best_score):
                    best, best_score = (params, res), s
            if best is None:
                continue
            params, train_res = best
            test_res = backtest.run(candles, strat, params, cfg, start=split)
            passed = (
                train_res["total_return"] > 0
                and train_res["profit_factor"] >= cfg["min_profit_factor"]
                and test_res["trades"] >= cfg["min_trades_test"]
                and test_res["total_return"] > 0
                and test_res["profit_factor"] >= cfg["min_profit_factor"]
                and test_res["max_drawdown"] <= cfg["max_test_drawdown"]
            )
            rows.append({
                "symbol": symbol,
                "strategy": strat.name,
                "inspired_by": strat.inspired_by,
                "params": params_to_json(params),
                "train": train_res,
                "test": test_res,
                "test_score": backtest.score(test_res, 1) or 0.0,
                "passed": passed,
            })

    rows.sort(key=lambda r: (r["passed"], r["test_score"]), reverse=True)
    champion = rows[0] if rows and rows[0]["passed"] else None
    return {"learned_at": int(time.time()), "champion": champion, "rows": rows}


def format_report(report):
    lines = ["%-10s %-11s %8s %8s %7s %6s %6s %s" % (
        "symbol", "strategy", "train", "test", "max_dd", "trades", "pf", "verdict")]
    for r in report["rows"]:
        t = r["test"]
        lines.append("%-10s %-11s %7.1f%% %7.1f%% %6.1f%% %6d %6.2f %s" % (
            r["symbol"], r["strategy"], 100 * r["train"]["total_return"], 100 * t["total_return"],
            100 * t["max_drawdown"], t["trades"], t["profit_factor"], "PASS" if r["passed"] else "fail"))
    champ = report["champion"]
    if champ:
        lines.append("\nChampion: %s on %s (%s) params=%s" % (
            champ["strategy"], champ["symbol"], champ["inspired_by"], champ["params"]))
        lines.append("Unseen-data result: %+.1f%% vs buy-and-hold %+.1f%%" % (
            100 * champ["test"]["total_return"], 100 * champ["test"]["buy_and_hold"]))
    else:
        lines.append("\nNo strategy passed on unseen data. The bot will stay out of the market.")
    return "\n".join(lines)
