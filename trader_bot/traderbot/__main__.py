"""python -m traderbot init | run | status

    python -m traderbot init                 # trader/config.json (the skills' limits) + trader/bot.json
    python -m traderbot run --dry-run        # the whole loop, a simulated broker, no keys
    python -m traderbot run                  # Alpaca PAPER (ALPACA_API_KEY / ALPACA_SECRET_KEY)
    python -m traderbot run --once           # one pass, then exit
    python -m traderbot run --live           # real money: also needs "paper": false in trader/config.json
    python -m traderbot run   (with "auto_approve": true in trader/bot.json: no yes asked)
    python -m traderbot status               # the open trade and today's decisions
    touch trader/STOP                        # the kill switch: no new entries until you delete it
"""

import argparse
import json
import os
import shutil
import sys
import time

from .alpaca import Alpaca, BrokerError
from .approval import AutoApprover, TerminalApprover
from .bot import BOT_CONFIG, DEFAULTS, KILL, STATE, Bot
from .sim import SimBroker
from .skills import SKILLS_DIR, Skills


class SetupError(Exception):
    pass


def load_settings(skills):
    path = skills.path(BOT_CONFIG)
    if not os.path.exists(path):
        return dict(DEFAULTS)
    with open(path, encoding="utf-8") as fh:
        return dict(DEFAULTS, **json.load(fh))


def cmd_init(a):
    os.makedirs(os.path.join(a.workdir, "trader"), exist_ok=True)
    cfg = os.path.join(a.workdir, "trader", "config.json")
    if os.path.exists(cfg):
        print("Kept your %s." % cfg)
    else:
        shutil.copy(os.path.join(SKILLS_DIR, "trader-budget", "config.example.json"), cfg)
        print("Wrote %s: paper trading, $5,000 budget, $50 max loss a trade, $150 a day. Edit it first." % cfg)
    bot = os.path.join(a.workdir, BOT_CONFIG)
    if os.path.exists(bot):
        print("Kept your %s." % bot)
    else:
        with open(bot, "w", encoding="utf-8") as fh:
            json.dump(DEFAULTS, fh, indent=2)
            fh.write("\n")
        print("Wrote %s: the symbols to scan, stop/target rules, the Time Machine gate." % bot)
    return 0


def preflight(skills, live, dry_run):
    """The broker to use, after checking that config, flags and account agree."""
    cfg = skills.read("trader/config.json")
    if cfg is None:
        raise SetupError("no trader/config.json: run python -m traderbot init and set your limits")
    paper = bool(cfg.get("paper", True))
    if live and paper:
        raise SetupError('--live but trader/config.json says "paper": true. Set it to false to trade real money.')
    if not live and not paper:
        raise SetupError('trader/config.json says "paper": false (real money) but --live was not given.')
    for k in ("max_loss_per_trade_usd", "max_daily_loss_usd", "max_trades_per_day"):
        if not cfg.get(k):
            raise SetupError("trader/config.json needs %s" % k)
    if not cfg.get("require_stop", True):
        raise SetupError('the bot only trades with a stop: set "require_stop": true')
    if dry_run:
        if live:
            raise SetupError("--dry-run and --live together make no sense")
        return SimBroker(cash=float(cfg.get("budget", 5000)))
    broker = Alpaca(paper=not live)
    if live and broker.key.startswith("PK"):
        raise SetupError("--live with what looks like a PAPER key (PK...). Use your live keys, or drop --live.")
    acct = broker.account()
    if acct.get("trading_blocked") or acct.get("status") != "ACTIVE":
        raise SetupError("the Alpaca account is not ready to trade (status %s)" % acct.get("status"))
    budget = float(cfg.get("budget", 0))
    if budget > float(acct.get("cash") or 0):
        raise SetupError("budget $%.2f in trader/config.json is more than the account's cash $%s"
                         % (budget, acct.get("cash")))
    return broker


def pick_approver(settings, live):
    if not settings.get("auto_approve"):
        return TerminalApprover(timeout=int(settings["approval_timeout_s"]))
    if live and not settings.get("auto_approve_live"):
        raise SetupError('"auto_approve" is on but this is real money: set "auto_approve_live": true in '
                         'trader/bot.json as well to place live orders without asking you, or turn auto_approve off')
    return AutoApprover()


def cmd_run(a):
    skills = Skills(a.workdir)
    try:
        broker = preflight(skills, a.live, a.dry_run)
    except (SetupError, BrokerError) as e:
        print("traderbot: %s" % e, file=sys.stderr)
        return 2
    settings = load_settings(skills)
    try:
        approver = pick_approver(settings, a.live)
    except SetupError as e:
        print("traderbot: %s" % e, file=sys.stderr)
        return 2
    bot = Bot(skills, broker, approver, settings,
              check_market=not a.dry_run)
    mode = "LIVE MONEY" if a.live else ("DRY RUN (simulated broker)" if a.dry_run else "Alpaca PAPER")
    who = ("Entries are AUTO-APPROVED (auto_approve)" if isinstance(approver, AutoApprover)
           else "Every entry waits for your yes")
    bot.log("traderbot started: %s. %s. Kill switch: touch %s. Ctrl+C stops." % (mode, who, KILL))
    every = a.interval or int(settings["interval_s"])
    try:
        while True:
            try:
                bot.cycle()
            except Exception as e:  # keep watching an open trade whatever one pass hit
                bot.log("This pass failed, trying again next pass: %r" % e)
            if a.once:
                return 0
            time.sleep(every)
    except KeyboardInterrupt:
        bot.log("Stopped by you. %s" % ("A trade is still OPEN in %s: its stop and target stay at Alpaca."
                                        % bot.state["open"]["symbol"] if bot.state.get("open") else
                                        "No open trade."))
        return 0


def cmd_status(a):
    skills = Skills(a.workdir)
    st = skills.read(STATE, {}) or {}
    print(json.dumps(st, indent=2) if st else "No bot state yet.")
    print(skills.run("ticket", "log").text())
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="traderbot", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", default=".", help="the project folder that holds trader/ (default .)")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("init")
    p = sub.add_parser("run")
    p.add_argument("--once", action="store_true")
    p.add_argument("--live", action="store_true", help="real money (also needs \"paper\": false)")
    p.add_argument("--dry-run", action="store_true", help="a simulated broker, no keys, no orders anywhere")
    p.add_argument("--interval", type=int, help="seconds between passes (default bot.json interval_s)")
    sub.add_parser("status")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 1
    return {"init": cmd_init, "run": cmd_run, "status": cmd_status}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
