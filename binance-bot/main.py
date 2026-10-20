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
from bot.dca import DAYS, WeeklyBuyer

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
    if not os.path.exists(path):
        return {}
    try:
        with open(path) as fh:
            return json.load(fh)
    except ValueError:
        # never start over on top of a damaged history: it is the bot's only record of what it bought
        sys.exit("The history file %s is damaged. Rename it (e.g. add .bak) and start again; the bot will "
                 "begin a new history. Your coins are still in your Binance account." % path)


def check_config(cfg):
    """Plain-language problems with config.json, or an empty list."""
    problems = []
    if str(cfg.get("dca_day", "")).lower() not in DAYS:
        problems.append("dca_day must be a full day name such as \"monday\".")
    amount = cfg.get("dca_amount")
    if not isinstance(amount, (int, float)) or amount < 5:
        problems.append("dca_amount must be a number of USDT, at least 5 (Binance's minimum order).")
    symbols = cfg.get("dca_symbols")
    if not isinstance(symbols, list) or not symbols or not all(
            isinstance(x, str) and x.isupper() and x.endswith("USDT") for x in symbols):
        problems.append("dca_symbols must be a list of Binance pairs like [\"BTCUSDT\", \"ETHUSDT\"].")
    tp = cfg.get("dca_take_profit")
    if tp is not None and (not isinstance(tp, (int, float)) or not 0 < tp <= 5):
        problems.append("dca_take_profit must be a fraction like 0.30 for 30%, or null to never sell.")
    poll = cfg.get("dca_poll_seconds")
    if not isinstance(poll, (int, float)) or poll < 60:
        problems.append("dca_poll_seconds must be at least 60.")
    return problems


def acquire_lock(state_path):
    """Make sure only one copy of the bot uses a history file. Returns a handle
    to keep open while running, or None if another copy already holds it."""
    fh = open(state_path + ".lock", "a+")
    try:
        if os.name == "nt":
            import msvcrt
            fh.seek(0)
            msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        fh.close()
        return None
    return fh


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

    problems = check_config(cfg)
    if problems:
        print("Please fix config.json:\n- " + "\n- ".join(problems))
        return 2
    state_path = os.path.join(HERE, STATE_FILES[1] if args.live else STATE_FILES[0])
    lock = acquire_lock(state_path)
    if lock is None:
        print("Another copy of the bot is already running (check your other Termux sessions). "
              "Running two would buy twice.")
        return 2
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
