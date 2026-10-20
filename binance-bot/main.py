"""Weekly buy bot for Binance.

    python main.py dca            buy with pretend money at real prices (practice)
    python main.py dca --live     buy with real money (needs API keys + config flag)
    python main.py status         buys so far, money put in, what it is worth now
"""

import argparse
import json
import os
import sys

from bot.binance import BinanceClient, LiveBroker, PaperBroker
from bot.dca import WeeklyBuyer

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_FILES = ("state.dca.paper.json", "state.dca.live.json")


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
    ap.add_argument("command", choices=["dca", "status"])
    ap.add_argument("--live", action="store_true", help="buy with real money")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    args = ap.parse_args(argv)

    cfg = load_config(args.config)
    client = BinanceClient(cfg["base_url"], os.environ.get("BINANCE_API_KEY", ""),
                           os.environ.get("BINANCE_API_SECRET", ""))

    if args.command == "status":
        found = False
        for name in STATE_FILES:
            p = os.path.join(HERE, name)
            if os.path.exists(p):
                found = True
                print("== %s ==" % ("real money" if "live" in name else "practice"))
                print(WeeklyBuyer(cfg, client, None, load_state(p), log=lambda *_: None).summary())
        if not found:
            print("No buys yet. Start with: python main.py dca")
        return 0

    state_path = os.path.join(HERE, STATE_FILES[1] if args.live else STATE_FILES[0])
    state = load_state(state_path)
    if args.live:
        if not cfg.get("live_trading_acknowledged"):
            print("Refusing to use real money: set \"live_trading_acknowledged\": true in config.json "
                  "after you have run practice mode and read the README.")
            return 2
        if not os.environ.get("BINANCE_API_KEY"):
            print("Set BINANCE_API_KEY and BINANCE_API_SECRET first.")
            return 2
        broker = LiveBroker(client, cfg)
    else:
        broker = PaperBroker(client, cfg)

    try:
        WeeklyBuyer(cfg, client, broker, state, state_path).run()
    except KeyboardInterrupt:
        print("\nStopped. History saved in %s" % state_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
