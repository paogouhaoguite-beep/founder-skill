export const OWNER = 'Leader1111111111111111111111111111111111111';
export const MINT = 'Meme111111111111111111111111111111111111pump';
export const WSOL = 'So11111111111111111111111111111111111111112';
export const USDC = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';

const bal = (mint, owner, amount, decimals = 6) => ({
  mint, owner, uiTokenAmount: { amount: String(amount), decimals },
});

// A parsed transaction where OWNER is the fee payer. sol values are in lamports.
export function tx({ preSol, postSol, pre = [], post = [], fee = 5000, err = null, blockTime = 1_700_000_000 }) {
  return {
    blockTime,
    slot: 1,
    transaction: { message: { accountKeys: [{ pubkey: OWNER }, { pubkey: 'Pool111' }] } },
    meta: {
      err,
      fee,
      preBalances: [preSol, 0],
      postBalances: [postSol, 0],
      preTokenBalances: pre.map(([m, a, d]) => bal(m, OWNER, a, d)),
      postTokenBalances: post.map(([m, a, d]) => bal(m, OWNER, a, d)),
    },
  };
}
