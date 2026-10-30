"""Weekly buy bot for CoinDCX (rupees) or Binance (USDT).

    python main.py dca            buy with pretend money at real prices (practice)
    python main.py dca --live     buy with real money (needs API keys + config flag)
    python main.py status         buys so far, money put in, what it is worth now
"""

import argparse
import json
import os
import sys
import time

from bot.binance import BinanceClient, LiveBroker, PaperBroker
from bot.coindcx import CoinDCXBroker, CoinDCXClient
from bot.dca import DAYS, WeeklyBuyer

HERE = os.path.dirname(os.path.abspath(__file__))

EXCHANGES = {
    # name: currency, smallest weekly amount, key variables, default fee settings
    "coindcx": {"currency": "INR", "minimum": 100, "keys": ("COINDCX_API_KEY", "COINDCX_API_SECRET"),
                "fee_rate": 0.0059, "slippage": 0.001, "tds_rate": 0.01},
    "binance": {"currency": "USDT", "minimum": 5, "keys": ("BINANCE_API_KEY", "BINANCE_API_SECRET"),
                "fee_rate": 0.001, "slippage": 0.0005, "tds_rate": 0.0},
}


def state_files(exchange):
    """History files. Binance keeps its original names so earlier history carries over."""
    if exchange == "binance":
        return "state.dca.paper.json", "state.dca.live.json"
    return "state.dca.%s.paper.json" % exchange, "state.dca.%s.live.json" % exchange


def exchange_settings(cfg):
    """Set the chosen exchange's currency and fees. These always come from the
    exchange, never from config.json, so an old config copied over from the
    Binance version cannot leave Binance's fee in place for CoinDCX."""
    ex = EXCHANGES.get(cfg.get("exchange"))
    if ex:
        cfg["currency"] = ex["currency"]
        for k in ("fee_rate", "slippage", "tds_rate"):
            cfg[k] = ex[k]
    return cfg


def make_client(cfg):
    if cfg["exchange"] == "coindcx":
        key, secret = EXCHANGES["coindcx"]["keys"]
        return CoinDCXClient(cfg.get("coindcx_url", "https://api.coindcx.com"),
                             os.environ.get(key, ""), os.environ.get(secret, ""))
    key, secret = EXCHANGES["binance"]["keys"]
    return BinanceClient(cfg.get("binance_url") or cfg.get("base_url") or "https://api.binance.com",
                         os.environ.get(key, ""), os.environ.get(secret, ""))


def make_logger(path):
    """Print each message with the date and time, and keep a copy in bot.log,
    so weeks later you can still see what the bot did and when."""
    def log(message):
        line = "%s  %s" % (time.strftime("%Y-%m-%d %H:%M"), message)
        print(line, flush=True)
        try:
            with open(path, "a") as fh:
                fh.write(line + "\n")
        except OSError:
            pass
    return log


def load_config(path, exchange=None):
    with open(os.path.join(HERE, "config.example.json")) as fh:
        cfg = json.load(fh)
    if os.path.exists(path):
        with open(path) as fh:
            cfg.update(json.load(fh))
    if exchange:
        cfg["exchange"] = exchange
    return exchange_settings(cfg)


def load_state(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path) as fh:
            return json.load(fh)
    except ValueError:
        # never start over on top of a damaged history: it is the bot's only record of what it bought
        sys.exit("The history file %s is damaged. Rename it (e.g. add .bak) and start again; the bot will "
                 "begin a new history. Your coins are still in your exchange account." % path)


def check_config(cfg):
    """Plain-language problems with config.json, or an empty list."""
    problems = []
    ex = EXCHANGES.get(cfg.get("exchange"))
    if ex is None:
        return ["exchange must be \"coindcx\" or \"binance\"."]
    cur = ex["currency"]
    if str(cfg.get("dca_day", "")).lower() not in DAYS:
        problems.append("dca_day must be a full day name such as \"monday\".")
    amount = cfg.get("dca_amount")
    if not isinstance(amount, (int, float)) or amount < ex["minimum"]:
        problems.append("dca_amount must be a number of %s, at least %d (the smallest order on %s)." % (
            cur, ex["minimum"], cfg["exchange"]))
    symbols = cfg.get("dca_symbols")
    if not isinstance(symbols, list) or not symbols or not all(
            isinstance(x, str) and x.isupper() and x.endswith(cur) for x in symbols):
        problems.append("dca_symbols must be a list of %s pairs like [\"BTC%s\", \"ETH%s\"]." % (
            cfg["exchange"], cur, cur))
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

    if args.command == "status":
        found = False
        for exchange in EXCHANGES:
            ecfg = exchange_settings(dict(cfg, exchange=exchange))
            for name in state_files(exchange):
                p = os.path.join(HERE, name)
                if os.path.exists(p):
                    found = True
                    print("== %s, %s ==" % (exchange, "real money" if ".live." in name else "practice"))
                    print(WeeklyBuyer(ecfg, make_client(ecfg), None, load_state(p), log=lambda *_: None).summary())
        if not found:
            print("No buys yet. Start with: python main.py dca")
        return 0

    problems = check_config(cfg)
    if problems:
        print("Please fix config.json:\n- " + "\n- ".join(problems))
        return 2
    client = make_client(cfg)
    paper_file, live_file = state_files(cfg["exchange"])
    state_path = os.path.join(HERE, live_file if args.live else paper_file)
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
        key, secret = EXCHANGES[cfg["exchange"]]["keys"]
        if not (os.environ.get(key) and os.environ.get(secret)):
            print("Set %s and %s first." % (key, secret))
            return 2
        broker = CoinDCXBroker(client, cfg) if cfg["exchange"] == "coindcx" else LiveBroker(client, cfg)
    else:
        broker = PaperBroker(client, cfg)

    try:
        WeeklyBuyer(cfg, client, broker, state, state_path, log=make_logger(os.path.join(HERE, "bot.log"))).run()
    except KeyboardInterrupt:
        print("\nStopped. History saved in %s" % state_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
