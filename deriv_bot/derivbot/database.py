"""SQLite trade journal and P/L analytics."""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path

SCHEMA = """
CREATE TABLE IF NOT EXISTS trades (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    mode            TEXT NOT NULL,              -- 'paper' or 'live'
    opened_at       TEXT NOT NULL,              -- ISO-8601 UTC
    closed_at       TEXT,
    symbol          TEXT NOT NULL,
    direction       TEXT NOT NULL,              -- CALL / PUT
    stake           REAL NOT NULL,
    payout          REAL NOT NULL,
    entry_price     REAL,
    exit_price      REAL,
    entry_epoch     INTEGER,
    duration        INTEGER NOT NULL,
    duration_unit   TEXT NOT NULL,
    status          TEXT NOT NULL DEFAULT 'open',   -- open / won / lost
    pnl             REAL,
    unrealized_pnl  REAL NOT NULL DEFAULT 0,
    contract_id     TEXT,
    proposal_id     TEXT,
    strategy        TEXT,
    notes           TEXT
);
CREATE INDEX IF NOT EXISTS idx_trades_mode_status ON trades(mode, status);
CREATE INDEX IF NOT EXISTS idx_trades_closed ON trades(mode, closed_at);
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
"""


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


@dataclass(frozen=True)
class TradeRecord:
    id: int
    mode: str
    opened_at: str
    closed_at: str | None
    symbol: str
    direction: str
    stake: float
    payout: float
    entry_price: float | None
    exit_price: float | None
    entry_epoch: int | None
    duration: int
    duration_unit: str
    status: str
    pnl: float | None
    unrealized_pnl: float
    contract_id: str | None
    proposal_id: str | None
    strategy: str | None
    notes: str | None


@dataclass(frozen=True)
class PerformanceStats:
    total_trades: int
    wins: int
    losses: int
    open_trades: int
    win_rate: float  # percent, 0 when no closed trades
    gross_profit: float
    gross_loss: float  # positive number
    profit_factor: float | None  # None when no closed trades; inf when no losses
    realized_pnl: float
    unrealized_pnl: float
    total_pnl: float
    current_drawdown: float
    current_drawdown_pct: float
    max_drawdown: float
    max_drawdown_pct: float


@dataclass(frozen=True)
class PeriodSummary:
    period: str  # YYYY-MM-DD or YYYY-Www
    trades: int
    wins: int
    losses: int
    win_rate: float
    pnl: float


class TradeDatabase:
    def __init__(self, path: str | Path) -> None:
        self.path = str(path)
        if self.path != ":memory:":
            Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    @contextmanager
    def _tx(self) -> Iterator[sqlite3.Connection]:
        try:
            yield self.conn
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

    # --- meta --------------------------------------------------------------
    def get_meta(self, key: str) -> str | None:
        row = self.conn.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
        return None if row is None else str(row["value"])

    def set_meta(self, key: str, value: str) -> None:
        with self._tx() as c:
            c.execute("INSERT INTO meta(key, value) VALUES(?, ?) "
                      "ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value))

    # --- writes ------------------------------------------------------------
    def open_trade(
        self,
        *,
        mode: str,
        symbol: str,
        direction: str,
        stake: float,
        payout: float,
        entry_price: float | None,
        entry_epoch: int | None,
        duration: int,
        duration_unit: str,
        contract_id: str | None = None,
        proposal_id: str | None = None,
        strategy: str | None = None,
        notes: str | None = None,
        opened_at: datetime | None = None,
    ) -> int:
        with self._tx() as c:
            cur = c.execute(
                """INSERT INTO trades (mode, opened_at, symbol, direction, stake, payout,
                   entry_price, entry_epoch, duration, duration_unit, contract_id,
                   proposal_id, strategy, notes)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (mode, iso(opened_at or utcnow()), symbol, direction, stake, payout,
                 entry_price, entry_epoch, duration, duration_unit, contract_id,
                 proposal_id, strategy, notes),
            )
            assert cur.lastrowid is not None
            return int(cur.lastrowid)

    def close_trade(
        self,
        trade_id: int,
        *,
        won: bool,
        pnl: float,
        exit_price: float | None,
        entry_price: float | None = None,
        closed_at: datetime | None = None,
    ) -> None:
        with self._tx() as c:
            cur = c.execute(
                """UPDATE trades SET status=?, pnl=?, exit_price=?, closed_at=?,
                   unrealized_pnl=0, entry_price=COALESCE(?, entry_price)
                   WHERE id=? AND status='open'""",
                ("won" if won else "lost", round(pnl, 2), exit_price,
                 iso(closed_at or utcnow()), entry_price, trade_id),
            )
            if cur.rowcount != 1:
                raise ValueError(f"trade {trade_id} not found or already closed")

    def update_unrealized(self, trade_id: int, unrealized_pnl: float) -> None:
        with self._tx() as c:
            c.execute("UPDATE trades SET unrealized_pnl=? WHERE id=? AND status='open'",
                      (round(unrealized_pnl, 2), trade_id))

    # --- reads -------------------------------------------------------------
    @staticmethod
    def _rec(row: sqlite3.Row) -> TradeRecord:
        return TradeRecord(**{k: row[k] for k in row.keys()})  # noqa: SIM118 (Row iterates values)

    def get_trade(self, trade_id: int) -> TradeRecord | None:
        row = self.conn.execute("SELECT * FROM trades WHERE id=?", (trade_id,)).fetchone()
        return None if row is None else self._rec(row)

    def open_trades(self, mode: str) -> list[TradeRecord]:
        rows = self.conn.execute(
            "SELECT * FROM trades WHERE mode=? AND status='open' ORDER BY id", (mode,))
        return [self._rec(r) for r in rows]

    def recent_trades(self, mode: str, limit: int = 10) -> list[TradeRecord]:
        rows = self.conn.execute(
            "SELECT * FROM trades WHERE mode=? ORDER BY id DESC LIMIT ?", (mode, limit))
        return [self._rec(r) for r in rows]

    def closed_trades(self, mode: str) -> list[TradeRecord]:
        rows = self.conn.execute(
            "SELECT * FROM trades WHERE mode=? AND status!='open' ORDER BY closed_at, id",
            (mode,))
        return [self._rec(r) for r in rows]

    def realized_pnl(self, mode: str) -> float:
        row = self.conn.execute(
            "SELECT COALESCE(SUM(pnl), 0) AS s FROM trades WHERE mode=? AND status!='open'",
            (mode,)).fetchone()
        return float(row["s"])

    def open_stakes(self, mode: str) -> float:
        row = self.conn.execute(
            "SELECT COALESCE(SUM(stake), 0) AS s FROM trades WHERE mode=? AND status='open'",
            (mode,)).fetchone()
        return float(row["s"])

    def daily_realized_pnl(self, mode: str, day: date) -> float:
        row = self.conn.execute(
            "SELECT COALESCE(SUM(pnl), 0) AS s FROM trades "
            "WHERE mode=? AND status!='open' AND substr(closed_at, 1, 10)=?",
            (mode, day.isoformat())).fetchone()
        return float(row["s"])

    def trades_opened_on(self, mode: str, day: date) -> int:
        row = self.conn.execute(
            "SELECT COUNT(*) AS n FROM trades WHERE mode=? AND substr(opened_at, 1, 10)=?",
            (mode, day.isoformat())).fetchone()
        return int(row["n"])

    def trailing_consecutive_losses(self, mode: str) -> int:
        n = 0
        for t in reversed(self.closed_trades(mode)):
            if t.status != "lost":
                break
            n += 1
        return n

    # --- analytics ---------------------------------------------------------
    def stats(self, mode: str, initial_balance: float) -> PerformanceStats:
        closed = self.closed_trades(mode)
        open_ = self.open_trades(mode)
        wins = [t for t in closed if t.status == "won"]
        losses = [t for t in closed if t.status == "lost"]
        gross_profit = sum(t.pnl or 0.0 for t in closed if (t.pnl or 0) > 0)
        gross_loss = -sum(t.pnl or 0.0 for t in closed if (t.pnl or 0) < 0)
        realized = sum(t.pnl or 0.0 for t in closed)
        unrealized = sum(t.unrealized_pnl for t in open_)

        if not closed:
            pf: float | None = None
        elif gross_loss == 0:
            pf = float("inf") if gross_profit > 0 else None
        else:
            pf = gross_profit / gross_loss

        equity = peak = initial_balance
        max_dd = max_dd_pct = 0.0
        for t in closed:
            equity += t.pnl or 0.0
            peak = max(peak, equity)
            dd = peak - equity
            if dd > max_dd:
                max_dd = dd
                max_dd_pct = dd / peak * 100 if peak > 0 else 0.0
        cur_dd = peak - equity
        cur_dd_pct = cur_dd / peak * 100 if peak > 0 else 0.0

        return PerformanceStats(
            total_trades=len(closed) + len(open_),
            wins=len(wins),
            losses=len(losses),
            open_trades=len(open_),
            win_rate=len(wins) / len(closed) * 100 if closed else 0.0,
            gross_profit=round(gross_profit, 2),
            gross_loss=round(gross_loss, 2),
            profit_factor=pf,
            realized_pnl=round(realized, 2),
            unrealized_pnl=round(unrealized, 2),
            total_pnl=round(realized + unrealized, 2),
            current_drawdown=round(cur_dd, 2),
            current_drawdown_pct=round(cur_dd_pct, 2),
            max_drawdown=round(max_dd, 2),
            max_drawdown_pct=round(max_dd_pct, 2),
        )

    def _summaries(self, mode: str, key_sql: str, limit: int) -> list[PeriodSummary]:
        rows = self.conn.execute(
            f"""SELECT {key_sql} AS period, COUNT(*) AS trades,
                       SUM(status='won') AS wins, SUM(status='lost') AS losses,
                       COALESCE(SUM(pnl), 0) AS pnl
                FROM trades WHERE mode=? AND status!='open'
                GROUP BY period ORDER BY period DESC LIMIT ?""",
            (mode, limit))
        out = []
        for r in rows:
            trades = int(r["trades"])
            wins = int(r["wins"] or 0)
            out.append(PeriodSummary(str(r["period"]), trades, wins, int(r["losses"] or 0),
                                     wins / trades * 100 if trades else 0.0,
                                     round(float(r["pnl"]), 2)))
        return out

    def daily_summary(self, mode: str, days: int = 7) -> list[PeriodSummary]:
        return self._summaries(mode, "substr(closed_at, 1, 10)", days)

    def weekly_summary(self, mode: str, weeks: int = 4) -> list[PeriodSummary]:
        # SQLite's %W is Monday-based week of year; prefix with %Y for sorting.
        return self._summaries(mode, "strftime('%Y-W%W', substr(closed_at, 1, 19))", weeks)
