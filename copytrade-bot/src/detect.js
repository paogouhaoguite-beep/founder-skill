import { STABLE_MINTS, WSOL_MINT, LAMPORTS_PER_SOL } from './constants.js';

// Reads one parsed transaction and decides whether `owner` bought or sold a
// token in it. Works from balance changes rather than program instructions, so
// it covers pump.fun, Raydium, Meteora, Orca, Jupiter and any other venue
// without decoding each one.
//
// Returns null when the transaction is not a clean swap of a single token
// against SOL, USDC or USDT (failed txs, transfers, airdrops, token-to-token
// swaps, liquidity moves).
export function detectSwap(tx, owner, signature = null) {
  if (!tx || !tx.meta || tx.meta.err) return null;

  const keys = accountKeys(tx);
  const ownerIndex = keys.indexOf(owner);
  if (ownerIndex === -1) return null;

  const pre = balancesByMint(tx.meta.preTokenBalances, owner);
  const post = balancesByMint(tx.meta.postTokenBalances, owner);
  const mints = new Set([...pre.keys(), ...post.keys()]);

  const solLamportsDelta =
    BigInt(tx.meta.postBalances[ownerIndex]) - BigInt(tx.meta.preBalances[ownerIndex]);
  let wsolDelta = 0n;
  let stableDelta = 0; // in USD, UI units
  const tokenMoves = [];

  for (const mint of mints) {
    const a = pre.get(mint) || { raw: 0n, decimals: post.get(mint)?.decimals ?? 0 };
    const b = post.get(mint) || { raw: 0n, decimals: a.decimals };
    const delta = b.raw - a.raw;
    if (delta === 0n) continue;
    if (mint === WSOL_MINT) wsolDelta += delta;
    else if (STABLE_MINTS.has(mint)) stableDelta += Number(delta) / 10 ** b.decimals;
    else tokenMoves.push({ mint, delta, preRaw: a.raw, postRaw: b.raw, decimals: b.decimals });
  }

  if (tokenMoves.length !== 1) return null;
  const move = tokenMoves[0];

  // SOL spent or received, counting wrapped SOL, before the network fee the
  // owner paid (fee is only charged to the fee payer).
  const feeLamports = ownerIndex === 0 ? BigInt(tx.meta.fee || 0) : 0n;
  const quoteLamports = solLamportsDelta + wsolDelta + feeLamports;
  const solDelta = Number(quoteLamports) / LAMPORTS_PER_SOL;

  // Ignore dust SOL movement (rent for a new token account is ~0.002 SOL).
  const paidSol = solDelta < -0.0025;
  const gotSol = solDelta > 0.0001;
  const paidStable = stableDelta < -0.01;
  const gotStable = stableDelta > 0.01;

  let side = null;
  if (move.delta > 0n && (paidSol || paidStable)) side = 'buy';
  else if (move.delta < 0n && (gotSol || gotStable)) side = 'sell';
  if (!side) return null;

  const sold = move.delta < 0n ? -move.delta : 0n;
  const sellFraction = side === 'sell' && move.preRaw > 0n ? Number((sold * 10_000n) / move.preRaw) / 10_000 : 0;

  return {
    signature,
    owner,
    side,
    mint: move.mint,
    decimals: move.decimals,
    tokenDeltaRaw: move.delta,
    preTokenRaw: move.preRaw,
    postTokenRaw: move.postRaw,
    sellFraction,
    // Quote side: what the leader spent (buy) or received (sell).
    solAmount: Math.abs(solDelta),
    stableAmount: Math.abs(stableDelta),
    quote: paidStable || gotStable ? 'stable' : 'sol',
    blockTime: tx.blockTime ?? null,
    slot: tx.slot ?? null,
  };
}

function accountKeys(tx) {
  const msg = tx.transaction.message;
  const raw = msg.accountKeys || msg.staticAccountKeys || [];
  const keys = raw.map((k) => (typeof k === 'string' ? k : (k.pubkey ?? k).toString()));
  // Unparsed v0 transactions list lookup-table addresses separately.
  const loaded = tx.meta.loadedAddresses;
  if (loaded && !msg.accountKeys?.[0]?.pubkey) {
    for (const k of [...(loaded.writable || []), ...(loaded.readonly || [])]) keys.push(k.toString());
  }
  return keys;
}

function balancesByMint(list, owner) {
  const out = new Map();
  for (const b of list || []) {
    if (b.owner !== owner) continue;
    const raw = BigInt(b.uiTokenAmount.amount);
    const prev = out.get(b.mint);
    out.set(b.mint, { raw: (prev?.raw ?? 0n) + raw, decimals: b.uiTokenAmount.decimals });
  }
  return out;
}
