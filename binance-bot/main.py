"""Command line for the Binance bot.

    python main.py learn          study the charts and show which strategy wins
    python main.py run            trade with pretend money (paper mode, default)
    python main.py run --live     trade real money (needs API keys + config flag)
    python main.py dca            weekly buy mode with pretend money: buy a fixed amount every week, never sell
    python main.py dca --live     weekly buy mode with real money
    python main.py simulate       replay the last 3 years of real prices through the bot (minutes, not weeks)
    python main.py status         show balance, open position and trade history
    python main.py reset-halt     clear the kill switch after you have reviewed why it fired
"""

import argparse
import json
import os
import sys

from bot import learner
from bot.dca import WeeklyBuyer
from bot.binance import INTERVAL_MS, BinanceClient, LiveBroker, PaperBroker
from bot.replay import simulate
from bot.trader import Trader

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config(path):
    with open(os.path.join(HERE, "config.example.json")) as fh:
        cfg = json.load(fh)
    if os.path.exists(path):
        with open(path) as fh:
            cfg.update(json.load(fh))
    return cfg


def load_state(path):
    if os.path.exists(path):
        with open(path) as fh:
            return json.load(fh)
    return {}


def run_simulation(cfg, years):
    # public market data mirror; works even where api.binance.com is blocked
    client = BinanceClient("https://data-api.binance.vision")
    total = int(years * 365 * 86_400_000 / INTERVAL_MS[cfg["interval"]]) + cfg["learn_candles"]
    print("Downloading %d candles per coin ..." % total)
    history = {s: client.closed_klines(s, cfg["interval"], total) for s in cfg["symbols"]}
    print("Replaying (this takes a few minutes) ...")
    state, curve = simulate(history, cfg, cfg["learn_candles"])
    start, end = cfg["start_equity"], curve[-1][1]
    peak, max_dd = start, 0.0
    for _, eq in curve:
        peak = max(peak, eq)
        max_dd = max(max_dd, (peak - eq) / peak)
    trades = state["trades"]
    wins = [t for t in trades if t["pnl"] > 0]
    print("\nStart %.2f -> end %.2f (%+.1f%%), worst drop %.1f%%" % (start, end, 100 * (end / start - 1), 100 * max_dd))
    print("Trades %d, won %d (%.0f%%)%s" % (len(trades), len(wins), 100 * len(wins) / max(len(trades), 1),
                                           ", KILL SWITCH FIRED" if state["halted"] else ""))
    first = curve[0][0]
    for s in cfg["symbols"]:
        cs = [c for c in history[s] if c["t"] >= first]
        if cs:
            print("Buy and hold %s over the same period: %+.1f%%" % (s, 100 * (cs[-1]["c"] / cs[0]["o"] - 1)))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["learn", "run", "dca", "simulate", "status", "reset-halt"])
    ap.add_argument("--years", type=float, default=3.0, help="how far back `simulate` replays")
    ap.add_argument("--live", action="store_true", help="trade real money")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    live = args.command in ("run", "dca") and args.live
    prefix = "state.dca." if args.command == "dca" else "state."
    state_path = os.path.join(HERE, prefix + ("live.json" if live else "paper.json"))
    state = load_state(state_path)
    client = BinanceClient(cfg["base_url"], os.environ.get("BINANCE_API_KEY", ""),
                           os.environ.get("BINANCE_API_SECRET", ""))

    if args.command == "learn":
        history = {s: client.closed_klines(s, cfg["interval"], cfg["learn_candles"]) for s in cfg["symbols"]}
        print(learner.format_report(learner.learn(history, cfg)))
        return 0

    if args.command == "simulate":
        return run_simulation(cfg, args.years)

    if args.command == "reset-halt":
        for name in ("state.paper.json", "state.live.json"):
            p = os.path.join(HERE, name)
            if os.path.exists(p):
                s = load_state(p)
                s["halted"], s["peak_equity"] = False, None
                with open(p, "w") as fh:
                    json.dump(s, fh, indent=2)
        print("Kill switch cleared.")
        return 0

    if args.command == "status":
        for name in ("state.paper.json", "state.live.json"):
            p = os.path.join(HERE, name)
            if not os.path.exists(p):
                continue
            s = load_state(p)
            trades = s.get("trades", [])
            wins = sum(1 for t in trades if t["pnl"] > 0)
            print("== %s ==" % name)
            if "paper_cash" in s:
                print("paper cash: %.4f" % s["paper_cash"])
            print("vault (locked profit): %.4f" % s.get("vault", 0.0))
            print("open position: %s" % (s.get("position") or "none"))
            print("trades: %d, wins: %d, total pnl: %+.4f" % (len(trades), wins, sum(t["pnl"] for t in trades)))
            print("halted: %s" % s.get("halted", False))
        for name in ("state.dca.paper.json", "state.dca.live.json"):
            p = os.path.join(HERE, name)
            if os.path.exists(p):
                print("== %s ==" % name)
                print(WeeklyBuyer(cfg, client, None, load_state(p), log=None).summary())
        return 0

    if live:
        if not cfg.get("live_trading_acknowledged"):
            print("Refusing to trade real money: set \"live_trading_acknowledged\": true in config.json "
                  "after you have run paper mode and read the README risks section.")
            return 2
        if not os.environ.get("BINANCE_API_KEY"):
            print("Set BINANCE_API_KEY and BINANCE_API_SECRET first.")
            return 2
        broker = LiveBroker(client, cfg, state)
    else:
        broker = PaperBroker(client, cfg, state)

    try:
        if args.command == "dca":
            WeeklyBuyer(cfg, client, broker, state, state_path).run()
        else:
            Trader(cfg, client, broker, state, state_path).run()
    except KeyboardInterrupt:
        print("\nStopped. State saved in %s" % state_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
