#!/usr/bin/env node
import { loadConfig } from './config.js';
import { makeConnection, loadKeypair } from './chain.js';
import { Jupiter } from './jupiter.js';
import { State } from './state.js';
import { Trader, short, fmt } from './trader.js';
import { Watcher } from './watcher.js';
import { analyzeWallet } from './analyze.js';
import { log } from './log.js';

const [cmd = 'run', ...args] = process.argv.slice(2);

const commands = {
  async run() {
    const cfg = loadConfig();
    if (!cfg.targets.length) throw new Error('no targets: add wallet addresses to "targets" in config.json');
    const connection = makeConnection(cfg);
    const keypair = cfg.privateKey ? loadKeypair(cfg.privateKey) : null;
    const state = new State(cfg.stateFile);
    const jupiter = new Jupiter({
      baseUrl: cfg.jupiterBaseUrl,
      apiKey: cfg.jupiterApiKey,
      slippageBps: cfg.slippageBps,
      priorityFeeMaxLamports: cfg.priorityFeeMaxLamports,
    });
    const trader = new Trader({ cfg, connection, jupiter, state, keypair });

    log.info(`mode: ${cfg.mode.toUpperCase()}${keypair ? `, wallet ${keypair.publicKey.toBase58()}` : ''}`);
    if (cfg.mode === 'live') {
      const bal = await connection.getBalance(keypair.publicKey);
      log.info(`balance: ${fmt(bal / 1e9)} SOL`);
      if (bal < cfg.maxBuySol * 1e9) log.warn('balance is below maxBuySol; buys may fail');
    }
    log.info(`open positions: ${state.openCount()}`);

    const watcher = new Watcher({ cfg, connection, onSwap: (swap, target) => {
      log.info(`signal: ${target.label || short(swap.owner)} ${swap.side.toUpperCase()} ${short(swap.mint)} ` +
        (swap.side === 'buy' ? `for ${fmt(swap.solAmount)} ${swap.quote === 'sol' ? 'SOL' : 'USD'}` : `${(swap.sellFraction * 100).toFixed(0)}% of bag`) +
        `${swap.blockTime ? `, ${Math.max(0, Date.now() / 1000 - swap.blockTime).toFixed(0)}s after leader` : ''} (${swap.signature})`);
      return trader.onLeaderSwap(swap, target);
    } });
    await watcher.start();

    const exitTimer = setInterval(() => trader.checkExits(), cfg.priceCheckSeconds * 1000);
    const shutdown = () => { log.info('stopping'); watcher.stop(); clearInterval(exitTimer); state.save(); process.exit(0); };
    process.on('SIGINT', shutdown);
    process.on('SIGTERM', shutdown);
  },

  async analyze() {
    const wallets = args.filter((a) => !a.startsWith('--'));
    const maxArg = args.find((a) => a.startsWith('--txs='));
    const maxTxs = maxArg ? Number(maxArg.split('=')[1]) : 300;
    if (!wallets.length) throw new Error('usage: npm run analyze -- <wallet> [<wallet> ...] [--txs=300]');
    const cfg = loadConfig();
    const connection = makeConnection(cfg);
    for (const w of wallets) {
      process.stderr.write(`\nanalyzing ${w}\n`);
      const r = await analyzeWallet(connection, w, {
        maxTxs,
        onProgress: (i, n) => { if (i % 25 === 0 || i === n) process.stderr.write(`  ${i}/${n} txs\r`); },
      });
      printReport(w, r);
    }
  },

  async status() {
    const cfg = loadConfig();
    const state = new State(cfg.stateFile);
    const open = Object.values(state.positions);
    console.log(`Open positions (${open.length})`);
    for (const p of open) {
      const val = p.lastValueSol != null ? `${fmt(p.lastValueSol)} SOL now` : 'not priced yet';
      console.log(`  ${p.mint}  cost ${fmt(p.costSol)} SOL, ${val}, copying ${p.leaderLabel}`);
    }
    const pnl = state.closed.reduce((s, c) => s + c.pnlSol, 0);
    const wins = state.closed.filter((c) => c.pnlSol > 0).length;
    console.log(`\nClosed trades: ${state.closed.length}, wins ${wins}, realised P&L ${pnl >= 0 ? '+' : ''}${fmt(pnl)} SOL`);
    for (const c of state.closed.slice(-15)) {
      console.log(`  ${short(c.mint)}  ${c.pnlSol >= 0 ? '+' : ''}${fmt(c.pnlSol)} SOL  (${c.reason})`);
    }
  },
};

function printReport(wallet, r) {
  const pct = (x) => (x == null ? 'n/a' : `${x.toFixed(0)}%`);
  console.log(`\n=== ${wallet}`);
  console.log(`  scanned ${r.txScanned} txs over ${r.spanDays.toFixed(1)} days: ${r.swaps} swaps across ${r.tokens} tokens`);
  console.log(`  closed trades:      ${r.closedTrades}   (still holding ${r.openTrades})`);
  console.log(`  win rate:           ${pct(r.winRatePct)}`);
  console.log(`  realised P&L:       ${r.realizedPnlSol >= 0 ? '+' : ''}${fmt(r.realizedPnlSol)} SOL`);
  console.log(`  median ROI / trade: ${pct(r.medianRoiPct)}`);
  console.log(`  median hold:        ${r.medianHoldMinutes == null ? 'n/a' : `${r.medianHoldMinutes.toFixed(1)} min`}`);
  console.log(`  avg buy size:       ${fmt(r.avgBuySol)} SOL`);
  if (r.best) console.log(`  best:  ${short(r.best.mint)} ${r.best.pnlSol >= 0 ? '+' : ''}${fmt(r.best.pnlSol)} SOL`);
  if (r.worst) console.log(`  worst: ${short(r.worst.mint)} ${fmt(r.worst.pnlSol)} SOL`);
  const flags = [];
  if (r.closedTrades < 15) flags.push('too few closed trades to trust the win rate');
  if (r.medianHoldMinutes != null && r.medianHoldMinutes < 2) flags.push('holds under 2 min: likely a bot or sniper, you will buy after the move');
  if (r.realizedPnlSol > 0 && r.best && r.best.pnlSol > r.realizedPnlSol) flags.push('profit comes from one trade; the rest lose');
  for (const f of flags) console.log(`  ! ${f}`);
}

const fn = commands[cmd];
if (!fn) {
  console.error(`unknown command "${cmd}". Use: run | analyze <wallet...> | status`);
  process.exit(1);
}
fn().catch((err) => { log.error(err.message); process.exit(1); });
