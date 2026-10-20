import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { Trader } from '../src/trader.js';
import { State } from '../src/state.js';

const LEADER = 'Leader1111111111111111111111111111111111111';
const MINT = 'Meme111111111111111111111111111111111111pump';
const WSOL = 'So11111111111111111111111111111111111111112';

// Fixed price: 1 SOL = 1,000,000 raw tokens, both directions.
function fakeJupiter(price = { tokensPerSol: 1_000_000 }) {
  const calls = [];
  return {
    calls,
    price,
    async quote(input, output, amount) {
      calls.push({ input, output, amount: BigInt(amount) });
      const out = input === WSOL
        ? (BigInt(amount) * BigInt(price.tokensPerSol)) / 1_000_000_000n
        : (BigInt(amount) * 1_000_000_000n) / BigInt(price.tokensPerSol);
      return { outAmount: out.toString() };
    },
  };
}

function setup(over = {}) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'ct-'));
  const cfg = {
    mode: 'paper', sizing: 'fixed', buySol: 0.1, copyRatio: 0.1, maxBuySol: 0.5, minLeaderBuySol: 0.2,
    maxOpenPositions: 2, allowAddToPosition: false, maxSignalAgeSeconds: 60,
    takeProfitPct: 100, stopLossPct: 50, maxHoldMinutes: 0, ...over,
  };
  const state = new State(path.join(dir, 'state.json'));
  const jupiter = fakeJupiter();
  return { cfg, state, jupiter, trader: new Trader({ cfg, connection: null, jupiter, state, keypair: null }) };
}

const now = () => Math.floor(Date.now() / 1000);
const buy = (sol, mint = MINT, owner = LEADER) => ({ side: 'buy', mint, owner, solAmount: sol, quote: 'sol', decimals: 6, blockTime: now(), signature: 's' });
const sell = (fraction, mint = MINT, owner = LEADER) => ({ side: 'sell', mint, owner, sellFraction: fraction, quote: 'sol', blockTime: now(), signature: 's' });

test('copies a buy, then a partial sell, then the rest', async () => {
  const { trader, state } = setup();
  await trader.onLeaderSwap(buy(1), { address: LEADER, label: 'whale' });
  assert.equal(state.positions[MINT].tokensRaw, '100000');
  assert.equal(state.positions[MINT].costSol, 0.1);

  await trader.onLeaderSwap(sell(0.5), { address: LEADER });
  assert.equal(state.positions[MINT].tokensRaw, '50000');
  assert.ok(Math.abs(state.positions[MINT].costSol - 0.05) < 1e-12);

  await trader.onLeaderSwap(sell(1), { address: LEADER });
  assert.equal(state.positions[MINT], undefined);
  assert.equal(state.closed.length, 1);
  assert.ok(Math.abs(state.closed[0].pnlSol) < 1e-9, 'flat price means flat P&L');
});

test('ratio sizing is capped at maxBuySol', async () => {
  const { trader, state } = setup({ sizing: 'ratio', copyRatio: 0.1, maxBuySol: 0.3 });
  await trader.onLeaderSwap(buy(10), { address: LEADER });
  assert.equal(state.positions[MINT].costSol, 0.3);
});

test('skips small, stale, stable-paid, duplicate and over-limit buys', async () => {
  const { trader, state } = setup({ maxOpenPositions: 1 });
  const t = { address: LEADER };
  await trader.onLeaderSwap(buy(0.1), t);
  await trader.onLeaderSwap({ ...buy(5), blockTime: now() - 600 }, t);
  await trader.onLeaderSwap({ ...buy(5), quote: 'stable' }, t);
  assert.equal(state.openCount(), 0);
  await trader.onLeaderSwap(buy(1), t);
  await trader.onLeaderSwap(buy(1), t);
  assert.equal(state.positions[MINT].buys.length, 1);
  await trader.onLeaderSwap(buy(1, 'Other1111'), t);
  assert.equal(state.openCount(), 1);
});

test('ignores sells by a wallet we did not copy into the token', async () => {
  const { trader, state } = setup();
  await trader.onLeaderSwap(buy(1), { address: LEADER });
  await trader.onLeaderSwap(sell(1, MINT, 'SomeoneElse'), { address: 'SomeoneElse' });
  assert.ok(state.positions[MINT]);
});

test('a sell that lands while the buy is still running is applied after it', async () => {
  const { trader, state, jupiter } = setup();
  const slow = jupiter.quote;
  jupiter.quote = async (...a) => { await new Promise((r) => setTimeout(r, 50)); return slow(...a); };
  await Promise.all([
    trader.onLeaderSwap(buy(1), { address: LEADER }),
    trader.onLeaderSwap(sell(1), { address: LEADER }),
  ]);
  assert.equal(state.openCount(), 0);
  assert.equal(state.closed.length, 1);
});

test('take profit and stop loss close the position', async () => {
  const { trader, state, jupiter } = setup();
  await trader.onLeaderSwap(buy(1), { address: LEADER });
  jupiter.price.tokensPerSol = 400_000; // token is now worth 2.5x
  await trader.checkExits();
  assert.equal(state.openCount(), 0);
  assert.match(state.closed[0].reason, /take profit/);
  assert.ok(Math.abs(state.closed[0].pnlSol - 0.15) < 1e-9);

  jupiter.price.tokensPerSol = 1_000_000;
  await trader.onLeaderSwap(buy(1), { address: LEADER });
  jupiter.price.tokensPerSol = 3_000_000; // down 67%
  await trader.checkExits();
  assert.match(state.closed[1].reason, /stop loss/);
});
