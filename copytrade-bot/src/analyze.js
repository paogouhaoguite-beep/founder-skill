import { PublicKey } from '@solana/web3.js';
import { detectSwap } from './detect.js';
import { sleep } from './chain.js';

// Replays a wallet's recent swaps and scores it as a copy target: win rate,
// realised SOL P&L, hold times. Only tokens both bought and sold inside the
// window count as closed trades.
export async function analyzeWallet(connection, address, { maxTxs = 500, onProgress } = {}) {
  const owner = new PublicKey(address);
  const signatures = [];
  let before;
  while (signatures.length < maxTxs) {
    const page = await connection.getSignaturesForAddress(owner, { before, limit: Math.min(1000, maxTxs - signatures.length) });
    if (!page.length) break;
    signatures.push(...page.filter((s) => !s.err).map((s) => s.signature));
    before = page[page.length - 1].signature;
  }

  const swaps = [];
  for (let i = 0; i < signatures.length; i++) {
    const tx = await getTx(connection, signatures[i]);
    const swap = detectSwap(tx, address, signatures[i]);
    if (swap) swaps.push(swap);
    onProgress?.(i + 1, signatures.length);
  }
  return summarize(swaps, signatures.length);
}

async function getTx(connection, sig) {
  for (let i = 0; i < 5; i++) {
    try {
      return await connection.getParsedTransaction(sig, { maxSupportedTransactionVersion: 1 });
    } catch (err) {
      if (!/429|Too Many/i.test(err.message)) throw err;
      await sleep(1000 * 2 ** i);
    }
  }
  return null;
}

// Pure: turns a list of detected swaps into per-token trades and totals.
export function summarize(swaps, txCount = swaps.length) {
  const byMint = new Map();
  for (const s of [...swaps].sort((a, b) => (a.blockTime ?? 0) - (b.blockTime ?? 0))) {
    if (s.quote !== 'sol') continue;
    let t = byMint.get(s.mint);
    if (!t) {
      if (s.side === 'sell') continue; // bought before the window; cost unknown
      t = { mint: s.mint, solIn: 0, solOut: 0, bought: 0n, sold: 0n, firstBuy: s.blockTime, lastSell: null, buys: 0, sells: 0 };
      byMint.set(s.mint, t);
    }
    if (s.side === 'buy') { t.solIn += s.solAmount; t.bought += s.tokenDeltaRaw; t.buys++; }
    else { t.solOut += s.solAmount; t.sold += -s.tokenDeltaRaw; t.sells++; t.lastSell = s.blockTime; }
  }

  const trades = [...byMint.values()].map((t) => {
    const closed = t.bought > 0n && t.sold * 100n >= t.bought * 90n;
    const pnl = t.solOut - t.solIn;
    return {
      mint: t.mint,
      closed,
      solIn: t.solIn,
      solOut: t.solOut,
      pnlSol: pnl,
      roiPct: t.solIn > 0 ? (pnl / t.solIn) * 100 : 0,
      holdMinutes: closed && t.firstBuy != null && t.lastSell != null ? (t.lastSell - t.firstBuy) / 60 : null,
      buys: t.buys,
      sells: t.sells,
    };
  });

  const closed = trades.filter((t) => t.closed);
  const wins = closed.filter((t) => t.pnlSol > 0);
  const times = swaps.map((s) => s.blockTime).filter(Boolean);
  const spanDays = times.length > 1 ? (Math.max(...times) - Math.min(...times)) / 86_400 : 0;

  return {
    txScanned: txCount,
    swaps: swaps.length,
    tokens: trades.length,
    closedTrades: closed.length,
    openTrades: trades.length - closed.length,
    winRatePct: closed.length ? (wins.length / closed.length) * 100 : 0,
    realizedPnlSol: closed.reduce((s, t) => s + t.pnlSol, 0),
    medianRoiPct: median(closed.map((t) => t.roiPct)),
    medianHoldMinutes: median(closed.map((t) => t.holdMinutes).filter((x) => x != null)),
    avgBuySol: avg(trades.filter((t) => t.solIn > 0).map((t) => t.solIn)),
    spanDays,
    best: [...closed].sort((a, b) => b.pnlSol - a.pnlSol)[0] || null,
    worst: [...closed].sort((a, b) => a.pnlSol - b.pnlSol)[0] || null,
    trades,
  };
}

const avg = (xs) => (xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : 0);
function median(xs) {
  if (!xs.length) return null;
  const s = [...xs].sort((a, b) => a - b);
  const m = Math.floor(s.length / 2);
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
}
