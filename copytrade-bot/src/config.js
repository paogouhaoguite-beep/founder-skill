import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';

const DEFAULTS = {
  // "paper" simulates every trade with live Jupiter quotes; "live" spends real SOL.
  mode: 'paper',
  rpcUrl: 'https://api.mainnet-beta.solana.com',
  wsUrl: null,
  jupiterBaseUrl: 'https://lite-api.jup.ag/swap/v1',
  pollIntervalMs: 1500,

  // Sizing. "fixed" spends buySol per copied buy; "ratio" spends
  // copyRatio x the leader's SOL, never more than maxBuySol.
  sizing: 'fixed',
  buySol: 0.05,
  copyRatio: 0.1,
  maxBuySol: 0.25,
  minLeaderBuySol: 0.2,
  maxOpenPositions: 5,
  allowAddToPosition: false,

  slippageBps: 1500,
  priorityFeeMaxLamports: 2_000_000,
  maxSignalAgeSeconds: 45,

  // Exits of our own, so a leader that never sells cannot leave us holding a rug.
  takeProfitPct: 150,
  stopLossPct: 40,
  maxHoldMinutes: 240,
  priceCheckSeconds: 20,

  stateFile: 'state.json',
  targets: [],
};

export function loadConfig(file = process.env.COPYTRADE_CONFIG || 'config.json') {
  const resolved = path.resolve(file);
  let fromFile = {};
  if (fs.existsSync(resolved)) {
    fromFile = JSON.parse(fs.readFileSync(resolved, 'utf8'));
  }
  const cfg = { ...DEFAULTS, ...fromFile };
  if (process.env.RPC_URL) cfg.rpcUrl = process.env.RPC_URL;
  if (process.env.WS_URL) cfg.wsUrl = process.env.WS_URL;
  if (process.env.JUPITER_BASE_URL) cfg.jupiterBaseUrl = process.env.JUPITER_BASE_URL;
  if (process.env.MODE) cfg.mode = process.env.MODE;
  cfg.jupiterApiKey = process.env.JUPITER_API_KEY || null;
  cfg.privateKey = process.env.PRIVATE_KEY || null;

  cfg.targets = (cfg.targets || []).map((t) => (typeof t === 'string' ? { address: t } : t));
  validate(cfg);
  return cfg;
}

function validate(cfg) {
  if (!['paper', 'live'].includes(cfg.mode)) throw new Error(`mode must be "paper" or "live", got "${cfg.mode}"`);
  if (!['fixed', 'ratio'].includes(cfg.sizing)) throw new Error(`sizing must be "fixed" or "ratio", got "${cfg.sizing}"`);
  if (cfg.mode === 'live' && !cfg.privateKey) throw new Error('live mode needs PRIVATE_KEY in .env');
  for (const n of ['buySol', 'maxBuySol', 'slippageBps', 'maxOpenPositions']) {
    if (!(Number(cfg[n]) > 0)) throw new Error(`${n} must be a positive number`);
  }
}
