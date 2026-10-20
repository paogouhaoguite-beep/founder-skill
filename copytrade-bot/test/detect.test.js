import test from 'node:test';
import assert from 'node:assert/strict';
import { detectSwap } from '../src/detect.js';
import { tx, OWNER, MINT, WSOL, USDC } from './helpers.js';

test('SOL spent and token received is a buy', () => {
  const s = detectSwap(tx({ preSol: 5e9, postSol: 4e9 - 5000, post: [[MINT, 1_000_000]] }), OWNER, 'sig');
  assert.equal(s.side, 'buy');
  assert.equal(s.mint, MINT);
  assert.equal(s.quote, 'sol');
  assert.ok(Math.abs(s.solAmount - 1) < 1e-9, `fee is excluded, got ${s.solAmount}`);
  assert.equal(s.tokenDeltaRaw, 1_000_000n);
});

test('token sent and SOL received is a sell, with the fraction of the bag', () => {
  const s = detectSwap(tx({ preSol: 1e9, postSol: 1.5e9, pre: [[MINT, 1000]], post: [[MINT, 250]] }), OWNER);
  assert.equal(s.side, 'sell');
  assert.equal(s.sellFraction, 0.75);
});

test('selling the whole bag gives fraction 1', () => {
  const s = detectSwap(tx({ preSol: 1e9, postSol: 2e9, pre: [[MINT, 1000]], post: [] }), OWNER);
  assert.equal(s.sellFraction, 1);
});

test('wrapped SOL counts as SOL', () => {
  const s = detectSwap(tx({ preSol: 1e9, postSol: 1e9 - 5000, pre: [[WSOL, 3e9, 9]], post: [[WSOL, 1e9, 9], [MINT, 42]] }), OWNER);
  assert.equal(s.side, 'buy');
  assert.ok(Math.abs(s.solAmount - 2) < 1e-9);
});

test('buy paid in USDC is flagged as a stable quote', () => {
  const s = detectSwap(tx({ preSol: 1e9, postSol: 1e9 - 5000, pre: [[USDC, 100e6]], post: [[USDC, 50e6], [MINT, 5]] }), OWNER);
  assert.equal(s.side, 'buy');
  assert.equal(s.quote, 'stable');
  assert.equal(s.stableAmount, 50);
});

test('ignores failed txs, airdrops, transfers and token-to-token swaps', () => {
  assert.equal(detectSwap(tx({ preSol: 5e9, postSol: 4e9, post: [[MINT, 1]], err: { x: 1 } }), OWNER), null);
  assert.equal(detectSwap(tx({ preSol: 5e9, postSol: 5e9 - 5000, post: [[MINT, 1]] }), OWNER), null, 'airdrop');
  assert.equal(detectSwap(tx({ preSol: 5e9, postSol: 5e9 - 5000, pre: [[MINT, 10]], post: [[MINT, 1]] }), OWNER), null, 'transfer out');
  assert.equal(detectSwap(tx({ preSol: 5e9, postSol: 5e9 - 5000, pre: [[MINT, 10]], post: [['Other1111', 5]] }), OWNER), null, 'token-to-token');
  assert.equal(detectSwap(tx({ preSol: 5e9, postSol: 4e9, post: [[MINT, 1]] }), 'SomeoneElse'), null, 'not a signer');
});

test('rent for a new token account alone is not a buy', () => {
  assert.equal(detectSwap(tx({ preSol: 5e9, postSol: 5e9 - 2_039_280 - 5000, post: [[MINT, 1]] }), OWNER), null);
});
