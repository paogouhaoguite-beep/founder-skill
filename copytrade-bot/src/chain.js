import { Connection, Keypair, PublicKey } from '@solana/web3.js';
import bs58 from 'bs58';

const TOKEN_PROGRAM = new PublicKey('TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA');
const TOKEN_2022_PROGRAM = new PublicKey('TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb');

export function makeConnection(cfg) {
  return new Connection(cfg.rpcUrl, {
    commitment: 'confirmed',
    wsEndpoint: cfg.wsUrl || undefined,
  });
}

export function loadKeypair(secret) {
  const s = secret.trim();
  if (s.startsWith('[')) return Keypair.fromSecretKey(Uint8Array.from(JSON.parse(s)));
  return Keypair.fromSecretKey(bs58.decode(s));
}

export async function fetchParsedTx(connection, signature, attempts = 6) {
  for (let i = 0; i < attempts; i++) {
    const tx = await connection.getParsedTransaction(signature, {
      maxSupportedTransactionVersion: 1,
      commitment: 'confirmed',
    });
    if (tx) return tx;
    await sleep(400 * (i + 1));
  }
  return null;
}

// Raw token balance of `owner` for `mint`, summed over classic and Token-2022 accounts.
export async function tokenBalanceRaw(connection, owner, mint) {
  let total = 0n;
  for (const programId of [TOKEN_PROGRAM, TOKEN_2022_PROGRAM]) {
    const res = await connection.getParsedTokenAccountsByOwner(new PublicKey(owner), {
      mint: new PublicKey(mint),
      programId,
    }).catch(() => ({ value: [] }));
    for (const acc of res.value) total += BigInt(acc.account.data.parsed.info.tokenAmount.amount);
  }
  return total;
}

export async function sendAndConfirm(connection, tx, keypair) {
  tx.sign([keypair]);
  const raw = tx.serialize();
  const latest = await connection.getLatestBlockhash('confirmed');
  const signature = await connection.sendRawTransaction(raw, { skipPreflight: true, maxRetries: 3 });
  const res = await connection.confirmTransaction(
    { signature, blockhash: tx.message.recentBlockhash, lastValidBlockHeight: latest.lastValidBlockHeight },
    'confirmed',
  );
  if (res.value.err) throw new Error(`transaction ${signature} failed: ${JSON.stringify(res.value.err)}`);
  return signature;
}

export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
