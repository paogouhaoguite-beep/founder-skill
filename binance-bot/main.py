"""Command line for the Binance bot.

    python main.py learn          study the charts and show which strategy wins
    python main.py run            trade with pretend money (paper mode, default)
    python main.py run --live     trade real money (needs API keys + config flag)
    python main.py status         show balance, open position and trade history
    python main.py reset-halt     clear the kill switch after you have reviewed why it fired
"""

import argparse
import json
import os
import sys

from bot import learner
from bot.binance import BinanceClient, LiveBroker, PaperBroker
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["learn", "run", "status", "reset-halt"])
    ap.add_argument("--live", action="store_true", help="trade real money")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    live = args.command == "run" and args.live
    state_path = os.path.join(HERE, "state.live.json" if live else "state.paper.json")
    state = load_state(state_path)
    client = BinanceClient(cfg["base_url"], os.environ.get("BINANCE_API_KEY", ""),
                           os.environ.get("BINANCE_API_SECRET", ""))

    if args.command == "learn":
        history = {s: client.closed_klines(s, cfg["interval"], cfg["learn_candles"]) for s in cfg["symbols"]}
        print(learner.format_report(learner.learn(history, cfg)))
        return 0

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
        Trader(cfg, client, broker, state, state_path).run()
    except KeyboardInterrupt:
        print("\nStopped. State saved in %s" % state_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
