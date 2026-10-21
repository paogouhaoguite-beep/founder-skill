"""Trade execution: paper (proposal-priced, simulated) and live (demo account) executors."""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Protocol

from .api import DerivAPIError, DerivClient
from .config import TradingConfig
from .database import TradeDatabase, TradeRecord
from .strategy import Direction, Signal

log = logging.getLogger(__name__)

UNIT_SECONDS = {"s": 1, "m": 60, "h": 3600}


class TradeRejected(Exception):
    """The trade was not placed (e.g. payout too low). Not an error condition."""


@dataclass(frozen=True)
class Settlement:
    trade_id: int
    won: bool
    pnl: float
    entry_price: float | None
    exit_price: float | None


class Executor(Protocol):
    mode: str

    async def open_trade(self, signal: Signal, stake: float, strategy: str) -> TradeRecord: ...

    async def check_trade(self, trade: TradeRecord) -> Settlement | None: ...

    async def balance(self) -> tuple[float, str]: ...

    async def reconcile(self) -> list[str]: ...

    async def close_all(self) -> None: ...


def rise_fall_won(direction: str, entry: float, exit_: float) -> bool:
    """Deriv Rise/Fall: a tie (exit == entry) is a loss."""
    if direction == Direction.CALL.value:
        return exit_ > entry
    return exit_ < entry


class _Base:
    mode = ""

    def __init__(self, client: DerivClient, db: TradeDatabase, cfg: TradingConfig,
                 clock: Callable[[], float] = time.time) -> None:
        self.client = client
        self.db = db
        self.cfg = cfg
        self._clock = clock

    def now(self) -> float:
        return float(self._clock())

    async def _priced_proposal(self, signal: Signal, stake: float) -> dict[str, Any]:
        proposal = await self.client.get_proposal(
            symbol=self.cfg.symbol, contract_type=signal.direction.value, amount=stake,
            currency=self.cfg.currency, duration=self.cfg.contract_duration,
            duration_unit=self.cfg.duration_unit,
        )
        ask = float(proposal["ask_price"])
        payout = float(proposal["payout"])
        ratio = (payout - ask) / ask if ask else 0.0
        log.info("Proposal %s %s stake=%.2f payout=%.2f (ratio %.2f) spot=%s",
                 signal.direction.value, self.cfg.symbol, ask, payout, ratio,
                 proposal.get("spot"))
        if ratio < self.cfg.min_payout_ratio:
            raise TradeRejected(f"payout ratio {ratio:.2f} below minimum "
                                f"{self.cfg.min_payout_ratio:.2f}")
        return proposal


class PaperExecutor(_Base):
    """Prices trades with the real `proposal` endpoint, never calls `buy`, and settles
    them from the actual tick at expiry."""

    mode = "paper"

    def __init__(self, client: DerivClient, db: TradeDatabase, cfg: TradingConfig,
                 starting_balance: float, clock: Callable[[], float] = time.time) -> None:
        super().__init__(client, db, cfg, clock)
        self.starting_balance = starting_balance

    async def balance(self) -> tuple[float, str]:
        bal = (self.starting_balance + self.db.realized_pnl(self.mode)
               - self.db.open_stakes(self.mode))
        return round(bal, 2), self.cfg.currency

    async def open_trade(self, signal: Signal, stake: float, strategy: str) -> TradeRecord:
        proposal = await self._priced_proposal(signal, stake)
        entry = float(proposal["spot"])
        entry_epoch = int(proposal.get("spot_time") or self.now())
        trade_id = self.db.open_trade(
            mode=self.mode, symbol=self.cfg.symbol, direction=signal.direction.value,
            stake=float(proposal["ask_price"]),
            payout=float(proposal["payout"]),
            entry_price=entry, entry_epoch=entry_epoch,
            duration=self.cfg.contract_duration, duration_unit=self.cfg.duration_unit,
            proposal_id=str(proposal.get("id")), strategy=strategy, notes=signal.reason,
        )
        log.info("[PAPER] Opened trade #%d %s @ %.4f stake %.2f", trade_id,
                 signal.direction.value, entry, stake)
        rec = self.db.get_trade(trade_id)
        assert rec is not None
        return rec

    def expiry_epoch(self, trade: TradeRecord) -> int | None:
        if trade.duration_unit == "t" or trade.entry_epoch is None:
            return None
        return trade.entry_epoch + trade.duration * UNIT_SECONDS[trade.duration_unit]

    async def check_trade(self, trade: TradeRecord) -> Settlement | None:
        """Settle from Deriv's own tick timestamps, never the local clock, so clock
        drift can neither settle a trade early nor pick the wrong exit tick."""
        assert trade.entry_price is not None and trade.entry_epoch is not None
        latest = await self.client.get_ticks(trade.symbol, count=1)
        if not latest:
            return None
        server_now, spot = latest[-1]
        exit_price: float | None = None
        if trade.duration_unit == "t":
            # Tick contracts last at most 10 ticks, so a bounded window starting at
            # entry always contains the exit tick, however late we look.
            window_end = min(server_now, trade.entry_epoch + max(120, trade.duration * 30))
            ticks = await self.client.get_ticks(trade.symbol, start=trade.entry_epoch + 1,
                                                end=window_end, count=5000)
            ticks = [t for t in ticks if t[0] > trade.entry_epoch]
            if len(ticks) >= trade.duration:
                exit_price = ticks[trade.duration - 1][1]
        else:
            expiry = self.expiry_epoch(trade)
            assert expiry is not None
            if server_now >= expiry:
                ticks = await self.client.get_ticks(trade.symbol, end=expiry, count=1)
                if ticks:
                    exit_price = ticks[-1][1]
        if exit_price is None:
            self._mark(trade, spot)
        if exit_price is None:
            return None
        won = rise_fall_won(trade.direction, trade.entry_price, exit_price)
        pnl = round(trade.payout - trade.stake, 2) if won else -trade.stake
        self.db.close_trade(trade.id, won=won, pnl=pnl, exit_price=exit_price)
        log.info("[PAPER] Trade #%d %s: entry %.4f exit %.4f P/L %+.2f", trade.id,
                 "WON" if won else "LOST", trade.entry_price, exit_price, pnl)
        return Settlement(trade.id, won, pnl, trade.entry_price, exit_price)

    def _mark(self, trade: TradeRecord, spot: float) -> None:
        # Intrinsic mark: what the contract would pay if it expired at the current spot.
        assert trade.entry_price is not None
        winning = rise_fall_won(trade.direction, trade.entry_price, spot)
        self.db.update_unrealized(trade.id, (trade.payout - trade.stake) if winning
                                  else -trade.stake)

    async def reconcile(self) -> list[str]:
        return []  # paper trades never call buy, so nothing can be lost in flight

    async def close_all(self) -> None:
        log.info("[PAPER] Open paper trades will settle at expiry; nothing to sell")


class LiveExecutor(_Base):
    """Places real `buy` orders. The bot only allows this on a virtual (demo) account
    unless safety.allow_real_account is explicitly enabled."""

    mode = "live"

    async def balance(self) -> tuple[float, str]:
        return await self.client.get_balance()

    @property
    def _pending_key(self) -> str:
        return f"pending_buy_{self.mode}"

    async def open_trade(self, signal: Signal, stake: float, strategy: str) -> TradeRecord:
        proposal = await self._priced_proposal(signal, stake)
        # If the connection dies mid-buy the contract may exist without a DB row;
        # this marker lets the next start find and adopt it (see reconcile()).
        self.db.set_meta(self._pending_key, str(int(self.now()) - 60))
        try:
            bought = await self.client.buy(str(proposal["id"]), float(proposal["ask_price"]))
        except DerivAPIError:
            self.db.delete_meta(self._pending_key)  # server refused: nothing was bought
            raise
        trade_id = self.db.open_trade(
            mode=self.mode, symbol=self.cfg.symbol, direction=signal.direction.value,
            stake=float(bought["buy_price"]), payout=float(bought["payout"]),
            entry_price=float(proposal["spot"]),
            entry_epoch=int(bought.get("start_time") or self.now()),
            duration=self.cfg.contract_duration, duration_unit=self.cfg.duration_unit,
            contract_id=str(bought["contract_id"]), proposal_id=str(proposal["id"]),
            strategy=strategy, notes=signal.reason,
        )
        self.db.delete_meta(self._pending_key)
        log.info("[LIVE] Bought contract %s (trade #%d) %s stake %.2f",
                 bought["contract_id"], trade_id, signal.direction.value, stake)
        rec = self.db.get_trade(trade_id)
        assert rec is not None
        return rec

    async def check_trade(self, trade: TradeRecord) -> Settlement | None:
        assert trade.contract_id is not None
        poc = await self.client.get_contract(trade.contract_id)
        if not poc.get("is_sold"):
            bid = poc.get("bid_price")
            if bid is not None:
                self.db.update_unrealized(trade.id, float(bid) - trade.stake)
            return None
        profit = float(poc.get("profit", 0.0))
        won = poc.get("status") == "won" or profit > 0
        entry = poc.get("entry_spot") or poc.get("entry_tick")
        exit_ = poc.get("exit_tick") or poc.get("sell_spot")
        entry_f = float(entry) if entry is not None else None
        exit_f = float(exit_) if exit_ is not None else None
        self.db.close_trade(trade.id, won=won, pnl=profit, exit_price=exit_f, entry_price=entry_f)
        log.info("[LIVE] Contract %s %s P/L %+.2f", trade.contract_id,
                 "WON" if won else "LOST", profit)
        return Settlement(trade.id, won, profit, entry_f, exit_f)

    async def reconcile(self) -> list[str]:
        """After a buy whose outcome was unknown, adopt any contract that was bought."""
        since = self.db.get_meta(self._pending_key)
        if since is None:
            return []
        known = {t.contract_id for t in self.db.open_trades(self.mode)}
        known |= {t.contract_id for t in self.db.closed_trades(self.mode)}
        notes: list[str] = []
        for c in await self.client.portfolio():
            cid = str(c.get("contract_id"))
            if (cid in known or c.get("symbol") != self.cfg.symbol
                    or int(c.get("date_start", 0)) < int(since)
                    or c.get("contract_type") not in ("CALL", "PUT")):
                continue
            start = int(c["date_start"])
            self.db.open_trade(
                mode=self.mode, symbol=self.cfg.symbol, direction=str(c["contract_type"]),
                stake=float(c["buy_price"]), payout=float(c["payout"]), entry_price=None,
                entry_epoch=start, duration=max(1, int(c.get("expiry_time", start)) - start),
                duration_unit="s", contract_id=cid, notes="reconciled from portfolio")
            known.add(cid)
            notes.append(f"open contract {cid}")
        for c in await self.client.profit_table(int(since)):
            cid = str(c.get("contract_id"))
            code = str(c.get("shortcode", ""))
            direction = code.split("_", 1)[0]
            if cid in known or direction not in ("CALL", "PUT") \
                    or f"_{self.cfg.symbol}_" not in code:
                continue
            buy, sell = float(c["buy_price"]), float(c.get("sell_price") or 0.0)
            tid = self.db.open_trade(
                mode=self.mode, symbol=self.cfg.symbol, direction=direction, stake=buy,
                payout=float(c.get("payout") or sell), entry_price=None,
                entry_epoch=int(c.get("purchase_time", 0)), duration=1, duration_unit="s",
                contract_id=cid, notes="reconciled from profit_table")
            self.db.close_trade(tid, won=sell > buy, pnl=round(sell - buy, 2), exit_price=None)
            known.add(cid)
            notes.append(f"closed contract {cid} ({sell - buy:+.2f})")
        self.db.delete_meta(self._pending_key)
        for n in notes:
            log.warning("[LIVE] Reconciled %s from an interrupted buy", n)
        return notes

    async def close_all(self) -> None:
        for t in self.db.open_trades(self.mode):
            try:
                await self.client.sell(t.contract_id or "0", 0)
                log.warning("[LIVE] Sold contract %s at market", t.contract_id)
            except Exception as exc:  # sell can be refused (e.g. too close to expiry)
                log.error("[LIVE] Could not sell contract %s: %r", t.contract_id, exc)
