# copytrade-bot

Follows Solana meme coin traders you choose. When one of them buys a token, the
bot buys it too. When they sell, it sells the same share of its position.

- Works on any venue (pump.fun, Raydium, Meteora, Orca, Jupiter...) because it
  reads the wallet's balance changes, not each DEX's instructions.
- Trades through Jupiter, which also routes pump.fun bonding-curve tokens.
- **Paper mode by default**: every trade is priced with a live Jupiter quote but
  nothing is sent, so you can see how copying a wallet would have gone first.
- Has its own take-profit, stop-loss and max-hold timer, because a leader who
  never sells (or whose sell you miss) would otherwise leave you holding.
- `analyze` scores a wallet before you follow it: win rate, realised P&L, hold
  times, and warnings for wallets that are not worth copying.

## Read this before you put money in

- **You always buy after them, at a worse price.** Their buy has to confirm
  before you can see it, so you land a second or more later. On a fresh pump.fun
  coin that can already be +20% or more. A trader who makes money on
  30-second flips can lose you money on the same trades.
- **Copy-trade targets get farmed.** Wallets with big public win rates are
  watched by many bots. Some traders know this and buy, let the copiers pump
  the price, then dump on them.
- **Win rate alone lies.** A wallet that wins 80% of tiny trades and loses
  everything on the other 20% has a great win rate. Look at realised P&L,
  median ROI, and whether one lucky trade carries all the profit. `analyze`
  flags these.
- Most meme coins go to zero. Use a fresh wallet holding only what you can
  afford to lose. Run paper mode for a few days first. This is not financial
  advice.

## Setup

Needs Node.js 20 or newer.

```bash
cd copytrade-bot
npm install
cp config.example.json config.json
cp .env.example .env
```

Put a paid RPC URL in `.env` (Helius, QuickNode, Triton; free tiers exist).
The public endpoint works for trying it out but rate-limits hard and adds lag.

## 1. Find traders worth copying

Get candidate wallet addresses from GMGN, Birdeye, Cielo, Solscan's top
traders on coins you know ran, or Kolscan-style leaderboards. Then check them:

```bash
npm run analyze -- <wallet> [<wallet> ...] --txs=500
```

```
=== 7xKX...
  scanned 500 txs over 6.2 days: 312 swaps across 88 tokens
  closed trades:      81   (still holding 7)
  win rate:           58%
  realised P&L:       +41.2034 SOL
  median ROI / trade: 12%
  median hold:        34.0 min
  avg buy size:       1.8200 SOL
  ! holds under 2 min: likely a bot or sniper, you will buy after the move
```

What you want: lots of closed trades, positive realised P&L that is not all
from one trade, and hold times of many minutes (so the lag of copying matters
less). Skip wallets the tool flags as sub-2-minute snipers.

## 2. Configure

Paste the wallets into `targets` in `config.json`. The main settings:

| Setting | What it does |
|---|---|
| `mode` | `paper` (simulate) or `live` (real trades) |
| `sizing` | `fixed`: spend `buySol` per copied buy. `ratio`: spend `copyRatio` x what the leader spent |
| `buySol`, `copyRatio` | size per trade for the mode above |
| `maxBuySol` | hard cap on any single buy |
| `minLeaderBuySol` | ignore leader buys smaller than this (test buys, dust) |
| `maxOpenPositions` | stop opening new positions past this many |
| `allowAddToPosition` | copy a leader's second buy of a token you already hold |
| `slippageBps` | 1500 = 15%. Meme coins need high slippage or buys fail |
| `priorityFeeMaxLamports` | most you pay per tx to get in faster (2,000,000 = 0.002 SOL) |
| `maxSignalAgeSeconds` | don't copy trades older than this (avoids buying old pumps after a restart or lag) |
| `takeProfitPct` / `stopLossPct` | sell everything at +X% / -X%. Set to 0 to turn off |
| `maxHoldMinutes` | sell anything held longer than this. 0 = off |

Any target can override `buySol`, `sizing`, `copyRatio`, `maxBuySol` and
`minLeaderBuySol` for itself.

## 3. Run

```bash
npm start          # runs in the mode set in config.json
npm run status     # open positions, closed trades, total P&L
```

```
2026-10-20 13:31:53 signal: w6 BUY Zb5H..G8jC for 1.0015 SOL, 1s after leader (52e9QB...)
2026-10-20 13:31:54 [PAPER] BUY  Zb5H..G8jC for 0.0500 SOL (copying w6, who spent 1.0015 SOL)
```

Positions are saved to `state.json`, so you can stop and restart. On start the
bot only acts on new trades; it never replays a leader's history.

### Going live

1. Create a new wallet just for this (`solana-keygen new -o bot.json`, or a new
   Phantom account) and send it a small amount of SOL.
2. Put its key in `.env` as `PRIVATE_KEY` (base58 string, or the `[..]` array
   from the keygen file). Never commit `.env`.
3. Set `"mode": "live"` in `config.json` and start it.

Keep it running on a server or VPS close to your RPC for the lowest lag.

## How it works

1. **Watch.** For each target, a websocket log subscription fires the moment
   they sign something, with a polling loop as backup.
2. **Detect.** For each transaction, compare the wallet's token and SOL
   balances before and after. One token up and SOL/USDC down is a buy; one
   token down and SOL/USDC up is a sell, and the share of their bag they sold
   is recorded. Anything else (transfers, airdrops, token-to-token swaps,
   failed txs) is ignored.
3. **Trade.** Buys get a Jupiter quote and swap from SOL. Sells sell the same
   fraction of our position (95%+ counts as "sold everything"). Only the leader
   whose buy we copied can trigger the sell. Trades on the same token run one
   after another, so a fast buy-then-sell is copied in order.
4. **Protect.** Every `priceCheckSeconds` each position is valued with a sell
   quote and closed if it hits take-profit, stop-loss or max hold time.

## Limits

- Only copies buys paid in SOL. Buys paid in USDC/USDT are detected and logged
  but skipped.
- Some bots trade from one wallet but hold tokens in another account; their
  trades don't show up as balance changes on the signer and are ignored.
- If a token is rugged so there is no route left to sell, stop-loss can't
  fire. You'll see `price check ... failed` warnings.

## Tests

```bash
npm test
```
