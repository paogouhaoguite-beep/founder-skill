import test from 'node:test';
import assert from 'node:assert/strict';
import { summarize } from '../src/analyze.js';

const sw = (side, mint, sol, delta, t) => ({ side, mint, solAmount: sol, tokenDeltaRaw: BigInt(delta), blockTime: t, quote: 'sol' });

test('pairs buys with sells into closed trades and scores them', () => {
  const r = summarize([
    sw('buy', 'A', 1, 100, 0), sw('sell', 'A', 3, -100, 600),          // +2, held 10 min
    sw('buy', 'B', 1, 100, 0), sw('sell', 'B', 0.5, -95, 60),          // -0.5 (95% sold counts as closed)
    sw('buy', 'C', 1, 100, 0), sw('sell', 'C', 0.2, -10, 60),          // still holding 90%
    sw('sell', 'D', 5, -100, 10),                                      // bought before window: ignored
  ]);
  assert.equal(r.tokens, 3);
  assert.equal(r.closedTrades, 2);
  assert.equal(r.openTrades, 1);
  assert.equal(r.winRatePct, 50);
  assert.equal(r.realizedPnlSol, 1.5);
  assert.equal(r.best.mint, 'A');
  assert.equal(r.worst.mint, 'B');
  assert.equal(r.medianHoldMinutes, 5.5);
});

test('empty history', () => {
  const r = summarize([]);
  assert.equal(r.closedTrades, 0);
  assert.equal(r.winRatePct, 0);
  assert.equal(r.medianRoiPct, null);
});
