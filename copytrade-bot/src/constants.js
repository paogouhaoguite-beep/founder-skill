export const WSOL_MINT = 'So11111111111111111111111111111111111111112';
export const USDC_MINT = 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v';
export const USDT_MINT = 'Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB';

// Mints a trader pays with. A swap that moves one of these against another
// token is treated as a buy or sell of that other token.
export const QUOTE_MINTS = new Set([WSOL_MINT, USDC_MINT, USDT_MINT]);
export const STABLE_MINTS = new Set([USDC_MINT, USDT_MINT]);

export const LAMPORTS_PER_SOL = 1_000_000_000;
