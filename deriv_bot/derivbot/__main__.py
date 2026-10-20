"""Command-line entry point: python -m derivbot [--paper] [--report] [--e2e-test] ..."""

from __future__ import annotations

import argparse
import asyncio
import dataclasses
import logging
import os
import sys
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from logging.handlers import RotatingFileHandler
from pathlib import Path

from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from .api import DerivClient
from .bot import TradingBot
from .config import Config, ConfigError, load_config
from .dashboard import DISCLAIMER, render_dashboard, render_report
from .database import TradeDatabase
from .e2e import E2EResult, run_e2e, save_result
from .executor import Executor, LiveExecutor, PaperExecutor
from .mock_server import DEMO_TOKEN, MockDerivServer
from .risk import RiskManager
from .strategy import EmaCrossoverStrategy

console = Console()


def setup_logging(cfg: Config, to_console: bool) -> None:
    root = logging.getLogger()
    root.setLevel(cfg.logging.level.upper())
    for h in list(root.handlers):
        root.removeHandler(h)
    fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s: %(message)s")
    if cfg.logging.file:
        Path(cfg.logging.file).parent.mkdir(parents=True, exist_ok=True)
        fh = RotatingFileHandler(cfg.logging.file, maxBytes=5_000_000, backupCount=5,
                                 encoding="utf-8")
        fh.setFormatter(fmt)
        root.addHandler(fh)
    if to_console:
        sh = logging.StreamHandler(sys.stderr)
        sh.setFormatter(fmt)
        root.addHandler(sh)
    logging.getLogger("websockets").setLevel(logging.WARNING)


def load_dotenv(path: str = ".env") -> None:
    """Minimal .env loader (KEY=VALUE lines). Existing env vars win."""
    p = Path(path)
    if not p.is_file():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip("'\""))


@asynccontextmanager
async def maybe_mock(cfg: Config, use_mock: bool) -> AsyncIterator[tuple[Config, str | None]]:
    """Yield (config, token). With --mock-server, point the bot at a local simulator."""
    token = os.environ.get(cfg.api.token_env) or None
    if not use_mock:
        yield cfg, token
        return
    async with MockDerivServer() as srv:
        mocked = dataclasses.replace(cfg, api=dataclasses.replace(cfg.api, endpoint=srv.url))
        yield mocked, DEMO_TOKEN


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="derivbot",
        description="Deriv EMA-crossover trading bot. " + DISCLAIMER)
    p.add_argument("--config", default="config.yaml", help="path to config.yaml")
    p.add_argument("--paper", action="store_true",
                   help="paper trading: price via proposal, never send buy requests")
    p.add_argument("--report", action="store_true", help="print P/L report and exit")
    p.add_argument("--e2e-test", action="store_true",
                   help="run one end-to-end paper test trade and exit (0 = success)")
    p.add_argument("--e2e-duration", type=int, default=5, help="e2e contract duration")
    p.add_argument("--e2e-unit", default="t", choices=["t", "s", "m", "h"],
                   help="e2e contract duration unit (default ticks, for a fast test)")
    p.add_argument("--e2e-db", default="data/e2e_trades.db", help="database for the e2e test")
    p.add_argument("--e2e-output", default="data/e2e_result.json",
                   help="where to write the e2e JSON result")
    p.add_argument("--mock-server", action="store_true",
                   help="use the built-in local Deriv simulator instead of the real API "
                        "(offline testing)")
    p.add_argument("--no-dashboard", action="store_true", help="plain log output instead")
    p.add_argument("--max-iterations", type=int, default=None, help=argparse.SUPPRESS)
    return p.parse_args(argv)


def print_e2e(res: E2EResult) -> None:
    lines = Text()
    for s in res.steps:
        lines.append("  ✔ " if s.ok else "  ✘ ", style="green" if s.ok else "red")
        lines.append(f"{s.name:<12}", style="bold")
        lines.append(f"{s.detail}\n")
    if res.success:
        console.print(Panel(lines, title="[bold green]E2E TEST TRADE: SUCCESS",
                            border_style="green"))
    else:
        lines.append(f"\nFailed step: {res.failed_step}\nError: {res.error}\n", style="red")
        lines.append(f"Hint: {res.hint}\n", style="yellow")
        tb_tail = "\n".join((res.traceback or "").strip().splitlines()[-6:])
        lines.append(f"\nTraceback (last lines; full trace in the JSON result):\n{tb_tail}",
                     style="dim")
        console.print(Panel(lines, title="[bold red]E2E TEST TRADE: FAILED",
                            border_style="red"))


async def main_async(args: argparse.Namespace, cfg: Config) -> int:
    if args.report:
        db = TradeDatabase(cfg.database.path)
        for mode in ("paper", "live"):
            v = db.get_meta(f"initial_balance_{mode}")
            initial = float(v) if v else cfg.paper.starting_balance
            console.print(render_report(db, mode, initial, cfg.trading.currency))
        db.close()
        return 0

    async with maybe_mock(cfg, args.mock_server) as (run_cfg, token):
        if args.e2e_test:
            db = TradeDatabase(args.e2e_db)
            res = await run_e2e(run_cfg, DerivClient(run_cfg.api, token), db,
                                duration=args.e2e_duration, duration_unit=args.e2e_unit)
            if args.mock_server:
                res.endpoint = f"{res.endpoint} (local mock server)"
            save_result(res, args.e2e_output)
            db.close()
            print_e2e(res)
            return 0 if res.success else 1

        if not args.paper and not token:
            console.print(f"[red]Live/demo mode needs ${run_cfg.api.token_env}. "
                          "Use --paper to trade without a token.")
            return 2

        db = TradeDatabase(run_cfg.database.path)
        client = DerivClient(run_cfg.api, token)
        executor: Executor = (
            PaperExecutor(client, db, run_cfg.trading, run_cfg.paper.starting_balance)
            if args.paper else LiveExecutor(client, db, run_cfg.trading))
        risk = RiskManager(run_cfg.risk, run_cfg.safety.kill_switch_file)
        strategy = EmaCrossoverStrategy(run_cfg.strategy)

        if args.no_dashboard:
            bot = TradingBot(run_cfg, client, db, executor, strategy, risk)
            await bot.run(args.max_iterations)
        else:
            with Live(console=console, refresh_per_second=2, screen=False) as live:
                bot = TradingBot(run_cfg, client, db, executor, strategy, risk,
                                 on_update=lambda b: live.update(render_dashboard(b)))
                await bot.run(args.max_iterations)
        db.close()
        if bot.state.halt_reason:
            console.print(f"[bold red]Stopped by kill switch: {bot.state.halt_reason}")
            return 3
        return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    load_dotenv()
    try:
        cfg = load_config(args.config)
    except ConfigError as exc:
        console.print(f"[red]{exc}")
        return 2
    setup_logging(cfg, to_console=args.no_dashboard or args.e2e_test)
    console.print(f"[dim italic]{DISCLAIMER}")
    try:
        return asyncio.run(main_async(args, cfg))
    except KeyboardInterrupt:
        console.print("Interrupted - stopping.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
