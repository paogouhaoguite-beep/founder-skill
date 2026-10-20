import { PublicKey } from '@solana/web3.js';
import { detectSwap } from './detect.js';
import { fetchParsedTx, sleep } from './chain.js';
import { log } from './log.js';

// Watches each target wallet and hands every detected swap to `onSwap`.
// A websocket log subscription gives the fastest signal; a polling loop over
// getSignaturesForAddress backs it up so nothing is missed if the socket drops.
export class Watcher {
  constructor({ cfg, connection, onSwap }) {
    this.cfg = cfg;
    this.connection = connection;
    this.onSwap = onSwap;
    this.seen = new Set();
    this.queue = Promise.resolve();
    this.stopped = false;
  }

  async start() {
    for (const target of this.cfg.targets) {
      // Start from "now": older history is never replayed as fresh signals.
      const recent = await this.connection.getSignaturesForAddress(new PublicKey(target.address), { limit: 25 });
      for (const s of recent) this.seen.add(s.signature);
      try {
        this.connection.onLogs(new PublicKey(target.address), (logs) => {
          if (!logs.err) this.handle(target, logs.signature);
        }, 'confirmed');
      } catch (err) {
        log.warn(`websocket unavailable for ${target.address}, polling only: ${err.message}`);
      }
      log.info(`watching ${target.label || target.address}`);
    }
    this.pollLoop();
  }

  async pollLoop() {
    while (!this.stopped) {
      for (const target of this.cfg.targets) {
        try {
          await this.poll(target);
        } catch (err) {
          log.warn(`poll ${target.label || target.address}: ${err.message}`);
        }
      }
      await sleep(this.cfg.pollIntervalMs);
    }
  }

  async poll(target) {
    // No `until` cursor: load-balanced RPCs often reject a signature another
    // node has not seen yet. The seen-set does the de-duplication instead.
    const sigs = await this.connection.getSignaturesForAddress(new PublicKey(target.address), { limit: 25 });
    for (const s of sigs.reverse()) {
      if (!s.err) this.handle(target, s.signature);
    }
  }

  // Processes signatures one at a time, in arrival order, each only once.
  handle(target, signature) {
    if (this.seen.has(signature)) return;
    this.seen.add(signature);
    if (this.seen.size > 50_000) this.seen = new Set([...this.seen].slice(-10_000));
    this.queue = this.queue.then(async () => {
      try {
        const tx = await fetchParsedTx(this.connection, signature);
        const swap = detectSwap(tx, target.address, signature);
        if (swap) this.onSwap(swap, target); // trades run on their own; keep reading
      } catch (err) {
        log.warn(`tx ${signature}: ${err.message}`);
      }
    });
  }

  stop() { this.stopped = true; }
}
