import { WSOL_MINT, LAMPORTS_PER_SOL } from './constants.js';
import { tokenBalanceRaw, sendAndConfirm } from './chain.js';
import { log } from './log.js';

// Turns a leader's detected swap into our own buy or sell, in paper or live mode.
export class Trader {
  constructor({ cfg, connection, jupiter, state, keypair }) {
    this.cfg = cfg;
    this.connection = connection;
    this.jupiter = jupiter;
    this.state = state;
    this.keypair = keypair;
    this.locks = new Map(); // mint -> tail of that mint's trade chain
  }

  // Runs trades on the same mint one after another, so a quick buy-then-sell
  // by the leader is copied in order instead of being dropped.
  withLock(mint, fn) {
    const prev = this.locks.get(mint) || Promise.resolve();
    const next = prev.then(fn, fn);
    this.locks.set(mint, next);
    next.finally(() => { if (this.locks.get(mint) === next) this.locks.delete(mint); });
    return next;
  }

  get live() { return this.cfg.mode === 'live'; }

  async onLeaderSwap(swap, target) {
    const label = target.label || short(swap.owner);
    const age = swap.blockTime ? Date.now() / 1000 - swap.blockTime : 0;
    if (age > this.cfg.maxSignalAgeSeconds) {
      log.info(`skip ${swap.side} ${short(swap.mint)} by ${label}: signal is ${age.toFixed(0)}s old`);
      return;
    }
    await this.withLock(swap.mint, async () => {
      try {
        if (swap.side === 'buy') await this.copyBuy(swap, target, label);
        else await this.copySell(swap, label);
      } catch (err) {
        log.error(`${swap.side} ${short(swap.mint)} failed: ${err.message}`);
      }
    });
  }

  buySizeSol(swap, target) {
    if (swap.quote !== 'sol') return null;
    if (swap.solAmount < (target.minLeaderBuySol ?? this.cfg.minLeaderBuySol)) return null;
    const sizing = target.sizing || this.cfg.sizing;
    const size = sizing === 'ratio'
      ? swap.solAmount * (target.copyRatio ?? this.cfg.copyRatio)
      : (target.buySol ?? this.cfg.buySol);
    return Math.min(size, target.maxBuySol ?? this.cfg.maxBuySol);
  }

  async copyBuy(swap, target, label) {
    const existing = this.state.positions[swap.mint];
    if (existing && !this.cfg.allowAddToPosition) {
      log.info(`skip buy ${short(swap.mint)} by ${label}: already holding`);
      return;
    }
    if (!existing && this.state.openCount() >= this.cfg.maxOpenPositions) {
      log.info(`skip buy ${short(swap.mint)} by ${label}: at maxOpenPositions (${this.cfg.maxOpenPositions})`);
      return;
    }
    const sizeSol = this.buySizeSol(swap, target);
    if (!sizeSol) {
      log.info(`skip buy ${short(swap.mint)} by ${label}: leader spent ${fmt(swap.solAmount)} SOL ${swap.quote === 'sol' ? '(below minLeaderBuySol)' : '(paid in stables)'}`);
      return;
    }

    const lamports = BigInt(Math.floor(sizeSol * LAMPORTS_PER_SOL));
    const quote = await this.jupiter.quote(WSOL_MINT, swap.mint, lamports);
    let tokensRaw = BigInt(quote.outAmount);
    let signature = null;

    if (this.live) {
      const before = await tokenBalanceRaw(this.connection, this.keypair.publicKey.toBase58(), swap.mint);
      const tx = await this.jupiter.buildSwap(quote, this.keypair.publicKey.toBase58());
      signature = await sendAndConfirm(this.connection, tx, this.keypair);
      const after = await tokenBalanceRaw(this.connection, this.keypair.publicKey.toBase58(), swap.mint);
      if (after > before) tokensRaw = after - before;
    }

    const pos = existing || {
      mint: swap.mint,
      leader: swap.owner,
      leaderLabel: label,
      decimals: swap.decimals,
      tokensRaw: '0',
      costSol: 0,
      openedAt: Date.now(),
      buys: [],
    };
    pos.tokensRaw = (BigInt(pos.tokensRaw) + tokensRaw).toString();
    pos.costSol += sizeSol;
    pos.buys.push({ at: Date.now(), sol: sizeSol, tokensRaw: tokensRaw.toString(), leaderSig: swap.signature, sig: signature });
    this.state.positions[swap.mint] = pos;
    this.state.save();
    log.info(`${this.tag()} BUY  ${short(swap.mint)} for ${fmt(sizeSol)} SOL (copying ${label}, who spent ${fmt(swap.solAmount)} SOL)${signature ? ` tx ${signature}` : ''}`);
  }

  async copySell(swap, label) {
    const pos = this.state.positions[swap.mint];
    if (!pos) return; // we never bought it
    if (pos.leader !== swap.owner) return; // only the leader we copied can trigger the exit
    const fraction = swap.sellFraction >= 0.95 ? 1 : swap.sellFraction;
    await this.sell(pos, fraction, `${label} sold ${(swap.sellFraction * 100).toFixed(0)}%`);
  }

  // Sells `fraction` (0..1] of a position and books the realised P&L.
  async sell(pos, fraction, reason) {
    let held = BigInt(pos.tokensRaw);
    if (this.live) held = await tokenBalanceRaw(this.connection, this.keypair.publicKey.toBase58(), pos.mint);
    if (held === 0n) {
      this.close(pos, 0, reason, null);
      return;
    }
    const amount = fraction >= 1 ? held : (held * BigInt(Math.round(fraction * 10_000))) / 10_000n;
    if (amount === 0n) return;

    const quote = await this.jupiter.quote(pos.mint, WSOL_MINT, amount);
    let solOut = Number(quote.outAmount) / LAMPORTS_PER_SOL;
    let signature = null;
    if (this.live) {
      const balBefore = await this.connection.getBalance(this.keypair.publicKey);
      const tx = await this.jupiter.buildSwap(quote, this.keypair.publicKey.toBase58());
      signature = await sendAndConfirm(this.connection, tx, this.keypair);
      const balAfter = await this.connection.getBalance(this.keypair.publicKey);
      solOut = Math.max(0, (balAfter - balBefore) / LAMPORTS_PER_SOL);
    }

    const share = Number(amount) / Number(held);
    const costPart = pos.costSol * Math.min(1, share);
    const pnl = solOut - costPart;
    log.info(`${this.tag()} SELL ${short(pos.mint)} ${fraction >= 1 ? 'all' : `${(fraction * 100).toFixed(0)}%`} for ${fmt(solOut)} SOL, P&L ${pnl >= 0 ? '+' : ''}${fmt(pnl)} SOL (${reason})${signature ? ` tx ${signature}` : ''}`);

    if (fraction >= 1 || amount >= held) {
      this.close(pos, solOut, reason, signature, costPart);
    } else {
      pos.tokensRaw = (BigInt(pos.tokensRaw) - amount).toString();
      pos.costSol -= costPart;
      pos.realizedSol = (pos.realizedSol || 0) + pnl;
      this.state.save();
    }
  }

  close(pos, solOut, reason, signature, costPart = pos.costSol) {
    const pnl = solOut - costPart + (pos.realizedSol || 0);
    this.state.closed.push({
      mint: pos.mint,
      leader: pos.leader,
      leaderLabel: pos.leaderLabel,
      openedAt: pos.openedAt,
      closedAt: Date.now(),
      investedSol: pos.buys.reduce((s, b) => s + b.sol, 0),
      pnlSol: pnl,
      reason,
      sig: signature,
    });
    delete this.state.positions[pos.mint];
    this.state.save();
  }

  // Our own take-profit, stop-loss and time limit, valued with a live sell quote.
  async checkExits() {
    for (const pos of Object.values(this.state.positions)) {
      if (this.locks.has(pos.mint)) continue; // a copied trade is already running on it
      await this.withLock(pos.mint, () => this.checkExit(pos.mint));
    }
  }

  async checkExit(mint) {
    const pos = this.state.positions[mint];
    if (!pos) return;
    try {
      const quote = await this.jupiter.quote(pos.mint, WSOL_MINT, BigInt(pos.tokensRaw));
      const value = Number(quote.outAmount) / LAMPORTS_PER_SOL;
      const changePct = ((value - pos.costSol) / pos.costSol) * 100;
      const heldMin = (Date.now() - pos.openedAt) / 60_000;
      pos.lastValueSol = value;
      let reason = null;
      if (this.cfg.takeProfitPct && changePct >= this.cfg.takeProfitPct) reason = `take profit at +${changePct.toFixed(0)}%`;
      else if (this.cfg.stopLossPct && changePct <= -this.cfg.stopLossPct) reason = `stop loss at ${changePct.toFixed(0)}%`;
      else if (this.cfg.maxHoldMinutes && heldMin >= this.cfg.maxHoldMinutes) reason = `held ${heldMin.toFixed(0)} min`;
      if (reason) await this.sell(pos, 1, reason);
      else this.state.save();
    } catch (err) {
      log.warn(`price check ${short(pos.mint)}: ${err.message}`);
    }
  }

  tag() { return this.live ? '[LIVE]' : '[PAPER]'; }
}

export const short = (s) => (s ? `${s.slice(0, 4)}..${s.slice(-4)}` : '?');
export const fmt = (n) => Number(n).toFixed(4);
