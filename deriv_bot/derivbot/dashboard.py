"""Rich-based terminal dashboard and P/L report rendering."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

from rich.console import Group, RenderableType
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .database import PerformanceStats, PeriodSummary, TradeDatabase, TradeRecord

if TYPE_CHECKING:
    from .bot import TradingBot

STATUS_STYLE = {"RUNNING": "bold green", "PAUSED": "bold yellow", "HALTED": "bold red",
                "STOPPED": "bold white", "CONNECTING": "cyan", "STARTING": "cyan"}

DISCLAIMER = ("Educational use only. Not financial advice. Trading carries a high risk of "
              "loss. Comply with Deriv's Terms of Service.")


def fmt_pnl(v: float | None) -> Text:
    if v is None:
        return Text("-")
    return Text(f"{v:+.2f}", style="green" if v > 0 else "red" if v < 0 else "")


def fmt_pf(pf: float | None) -> str:
    if pf is None:
        return "-"
    return "∞" if pf == float("inf") else f"{pf:.2f}"


def trades_table(trades: list[TradeRecord], title: str) -> Table:
    t = Table(title=title, expand=True, show_lines=False)
    for col in ("#", "Opened (UTC)", "Symbol", "Dir", "Stake", "Entry", "Exit", "Result", "P/L"):
        t.add_column(col, justify="right" if col in ("Stake", "Entry", "Exit", "P/L") else "left")
    for tr in trades:
        pnl = tr.pnl if tr.status != "open" else tr.unrealized_pnl
        result_style = {"won": "green", "lost": "red"}.get(tr.status, "yellow")
        t.add_row(str(tr.id), tr.opened_at[5:19].replace("T", " "), tr.symbol, tr.direction,
                  f"{tr.stake:.2f}", f"{tr.entry_price}" if tr.entry_price else "-",
                  f"{tr.exit_price}" if tr.exit_price else "-",
                  Text(tr.status.upper(), style=result_style), fmt_pnl(pnl))
    if not trades:
        t.add_row(*(["-"] * 9))
    return t


def stats_table(s: PerformanceStats, currency: str) -> Table:
    t = Table.grid(padding=(0, 2))
    t.add_column(style="bold")
    t.add_column()
    t.add_row("Realized P/L", fmt_pnl(s.realized_pnl))
    t.add_row("Unrealized P/L", fmt_pnl(s.unrealized_pnl))
    t.add_row("Total P/L", fmt_pnl(s.total_pnl))
    t.add_row("Trades (W/L/open)", f"{s.total_trades} ({s.wins}/{s.losses}/{s.open_trades})")
    t.add_row("Win rate", f"{s.win_rate:.1f}%")
    t.add_row("Profit factor", fmt_pf(s.profit_factor))
    t.add_row("Drawdown (cur/max)",
              f"{s.current_drawdown:.2f} {currency} ({s.current_drawdown_pct:.1f}%) / "
              f"{s.max_drawdown:.2f} ({s.max_drawdown_pct:.1f}%)")
    return t


def summary_table(rows: list[PeriodSummary], title: str) -> Table:
    t = Table(title=title, expand=True)
    for col in ("Period", "Trades", "W", "L", "Win %", "P/L"):
        t.add_column(col, justify="left" if col == "Period" else "right")
    for r in rows:
        t.add_row(r.period, str(r.trades), str(r.wins), str(r.losses), f"{r.win_rate:.1f}",
                  fmt_pnl(r.pnl))
    if not rows:
        t.add_row("-", "0", "0", "0", "-", "-")
    return t


def render_dashboard(bot: TradingBot) -> RenderableType:
    st = bot.state
    db = bot.db
    today = datetime.now(timezone.utc).date()
    today_rows = [r for r in db.daily_summary(bot.mode, 1) if r.period == today.isoformat()]
    today_sum = today_rows[0] if today_rows else None

    header = Table.grid(expand=True)
    header.add_column()
    header.add_column(justify="right")
    header.add_row(
        Text.assemble(("DERIV BOT ", "bold cyan"), (f"[{st.mode.upper()}] ", "bold magenta"),
                      (st.status, STATUS_STYLE.get(st.status, ""))),
        Text(f"{st.symbol} | {st.account} | iter {st.iterations}"),
    )

    acct = Table.grid(padding=(0, 2))
    acct.add_column(style="bold")
    acct.add_column()
    acct.add_row("Balance", f"{st.balance:,.2f} {st.currency}")
    acct.add_row("Today's P/L", fmt_pnl(today_sum.pnl if today_sum else 0.0))
    acct.add_row("Today's win rate",
                 f"{today_sum.win_rate:.1f}% ({today_sum.trades} trades)" if today_sum else "-")
    acct.add_row("Loss streak", f"{bot.risk.consecutive_losses}/"
                                f"{bot.risk.cfg.max_consecutive_losses}")
    acct.add_row("Last signal", st.last_signal)
    acct.add_row("Message", st.message or "-")
    if st.halt_reason:
        acct.add_row(Text("KILL SWITCH", style="bold red"), Text(st.halt_reason, style="red"))

    stats = bot.performance()
    top = Table.grid(expand=True)
    top.add_column(ratio=1)
    top.add_column(ratio=1)
    top.add_row(Panel(acct, title="Account & Status"),
                Panel(stats_table(stats, st.currency), title="Performance"))

    return Group(
        Panel(header),
        top,
        trades_table(db.open_trades(bot.mode), "Open Positions"),
        trades_table(db.recent_trades(bot.mode, 10), "Recent Trades"),
        Text(DISCLAIMER, style="dim italic"),
    )


def render_report(db: TradeDatabase, mode: str, initial_balance: float,
                  currency: str = "USD") -> RenderableType:
    stats = db.stats(mode, initial_balance)
    return Group(
        Panel(stats_table(stats, currency), title=f"P/L Report [{mode.upper()}]"),
        summary_table(db.daily_summary(mode, 7), "Daily (last 7)"),
        summary_table(db.weekly_summary(mode, 4), "Weekly (last 4)"),
        trades_table(db.recent_trades(mode, 15), "Recent Trades"),
        Text(DISCLAIMER, style="dim italic"),
    )
