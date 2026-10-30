# Weekly crypto buy bot (CoinDCX or Binance)

Buys a fixed amount of crypto every week, taking turns between BTC, ETH and
SOL. When everything it bought is worth 30% more than the money put in (after
fees and TDS), it sells it all and starts a new round.

It runs on **CoinDCX in rupees** by default: buys are paid in INR and profit
sales pay out INR you can withdraw to your bank. It can also run on Binance
in USDT (`"exchange": "binance"`).

**No bot can promise profit.** This one only makes money if the coins are
worth more when it sells than the average price it paid. Crypto can fall by
half and stay down for a year or more. Only use money you can afford to lose.

## How it works

1. Every week, on `dca_day` (Monday by default, UTC), it buys `dca_amount`
   rupees (500 by default) of the next coin in `dca_symbols`.
2. If the bot is off on the buy day, it buys later the same week. A week that
   passes entirely while it is off is skipped, never doubled up.
3. Every hour it checks the value of everything bought this round. Once that
   is `dca_take_profit` (30%) above the money put in, after the selling fee
   and the 1% TDS, it sells it all. The rupees stay in your CoinDCX INR wallet.
4. The next buy day starts a fresh round.

Buying the same amount every week means you buy more coins when the price is
low and fewer when it is high. That helps when prices dip and recover; it does
not help if prices fall and stay down.

## Setup

Needs only Python 3.9+, no extra packages.

```
cd binance-bot
cp config.example.json config.json      # change coins, amount, day, profit target
python main.py dca                      # practice: pretend money, real prices
python main.py status                   # buys so far, money put in, what it is worth now
```

Stop it with Ctrl+C (on Android in Termux: Volume Down + C). It remembers
everything when you start it again.

Every message is shown with its date and time and also saved in `bot.log`
in the same folder, so you can look back at what the bot did and when.

### Real money on CoinDCX

1. In the CoinDCX website, open the API dashboard (under your profile or
   settings) and create an API key. Give it trading access only: if it offers
   a withdrawal permission, leave it off. Bind it to your IP address if that
   option is offered. Save the key and secret somewhere private.
2. Put them in environment variables (never in a file you share):
   ```
   export COINDCX_API_KEY=...
   export COINDCX_API_SECRET=...
   ```
   (Windows Command Prompt: `set COINDCX_API_KEY=...`)
3. Keep enough rupees in your CoinDCX INR wallet for the weekly buys. If there
   is not enough, the bot waits and retries rather than buying less.
4. In `config.json` set `"live_trading_acknowledged": true`.
5. `python main.py dca --live`

Keep the device's clock on automatic time if you can. CoinDCX rejects
requests whose time is too far off; the bot corrects a drifting clock using
the time in CoinDCX's replies.

### Using Binance instead

Set `"exchange": "binance"`, `"dca_amount": 6` (USDT) and
`"dca_symbols": ["BTCUSDT", "ETHUSDT", "SOLUSDT"]` in `config.json`. Create a
Binance API key with **Enable Spot & Margin Trading** ON and **Enable
Withdrawals OFF**, and set `BINANCE_API_KEY` and `BINANCE_API_SECRET`. Each
exchange keeps its own history file, so the two never mix.

The bot only needs to run at least once each week, so a phone with Termux works.

## Settings

| Key | Default | Meaning |
|---|---|---|
| `exchange` | `coindcx` | `coindcx` (rupees) or `binance` (USDT) |
| `dca_amount` | `500` | rupees spent each week (CoinDCX's minimum order is 100) |
| `dca_symbols` | `["BTCINR", "ETHINR", "SOLINR"]` | coins to buy, one per week, in turn |
| `dca_day` | `monday` | buy day (UTC) |
| `dca_take_profit` | `0.30` | sell everything at this profit (0.30 = 30%) after fees; `null` = never sell |
| `dca_poll_seconds` | `3600` | how often it checks |

Fees are set by the bot for each exchange and are not read from `config.json`:
CoinDCX 0.59% per trade plus 1% TDS on sales, Binance 0.1% per trade. Holdings
are valued at the price you could sell at right now (on CoinDCX's INR markets
the gap between buy and sell prices is often about 0.5%), so the bot usually
shows a small loss right after a buy.

## Safety details

- **Never buys twice, never sells your own coins.** Every order is saved
  with its ID in the history file before it is sent. If the reply is lost,
  the exchange is down, or the phone dies mid-order, the next check asks the
  exchange about that exact order instead of sending another. A profit sale that
  stops halfway resumes coin by coin. The bot only ever sells what it bought,
  so coins you hold yourself in the same account are safe.
- **One copy at a time.** Starting the bot while another copy is already
  running (say, in a second Termux window) is refused, because two copies
  would buy twice.
- **Orders that fill a moment later.** CoinDCX accepts an order first and
  fills it a moment later. The bot waits for the fill; if it cannot confirm
  it, it keeps the order ID and checks again at the next run.
- **Rate limits.** If the exchange says "too many requests", the bot waits
  and checks again; it never takes that as "the order does not exist".
- **Delisted coins.** If a coin stops trading (EOS was delisted from Binance
  in 2025), the bot notices within an hour, skips it for buying, ignores the
  frozen price the exchange may keep showing for it, and lists anything it
  could not sell as STRANDED in `status` for you to handle in the exchange app.
- **Sales that do not go through.** If the exchange rejects a sale or only
  part of it fills (CoinDCX warns market orders can be rejected after being
  accepted; Binance ones can expire half-filled), the unsold coins stay
  tracked and are tried again at the next check. After 5 failed tries they
  are listed as STRANDED for you. No weekly buy happens until a sale has
  finished, so two rounds never mix. If you sold some of the bot's coins
  yourself in the app, the bot notices they are gone and carries on.
- **Small leftovers.** If one coin's share is under the exchange's minimum order
  when it is time to sell, it is kept and carried into the next round.
- **Unfilled buys** (no sellers at that moment) are not recorded and are
  retried later the same week.
- **Clock drift.** On Binance, if the clock drifts and requests are rejected,
  the bot resyncs with Binance's clock by itself. On CoinDCX the bot reads the
  time from CoinDCX's replies and corrects a drift of more than 5 seconds.
- **Mistakes in config.json** are listed in plain words at start-up. A damaged
  history file is reported and never overwritten.

## How it did on past prices

Real Binance prices, 6 USDT every Monday, starting in every week since 2018.
Each cell: share of start weeks losing money / median result. Sold USDT is
kept as cash, not reinvested.

BTC only, by profit target:

| Kept buying for | Never sell | Sell at +20% | Sell at +30% |
|---|---|---|---|
| 1 year | 28% / +25% | 23% / +13% | 24% / +18% |
| 2 years | 29% / +80% | 17% / +16% | 16% / +25% |
| 3 years | 7% / +85% | 4% / +18% | 3% / +25% |

Selling at a target lost money less often, but capped the gains: the best
3-year result at +30% was +33%, against +609% for never selling.

By coins, selling at +30%:

| Coins | 2 years | 3 years (worst start) |
|---|---|---|
| BTC only | 16% / +25% | 3% / +25% (-2%) |
| BTC + ETH | 6% / +24% | 0% / +25% (+5%) |
| BTC + ETH + SOL (default) | 12% / +24% | 0% / +25% (+1%) |
| Today's top 5: BTC ETH BNB SOL XRP | 8% / +25% | 0% / +26% (+3%) |
| 2018's top 6: BTC ETH XRP LTC ADA EOS | 33% / +21% | 9% / +19% (-10%) |

"Today's top 5" looks good partly because we already know those coins did
well. "2018's top 6" is what someone picking coins with potential back then
would have bought, and it did worse. Adding SOL left the median unchanged but
made the bad cases worse (worst 1-year start -54% against -43% for BTC + ETH);
remove `"SOLINR"` (or `"SOLUSDT"` on Binance) for the lower-risk pair.

With CoinDCX's costs instead of Binance's (0.59% fee per trade, about 0.25%
lost to the buy/sell price gap each way, 1% TDS on sales), the default BTC +
ETH + SOL mix:

| Kept buying for | Binance costs | CoinDCX costs |
|---|---|---|
| 1 year | 19% / +21% (worst -54%) | 20% / +21% (worst -54%) |
| 2 years | 12% / +24% (worst -16%) | 16% / +23% (worst -23%) |
| 3 years | 0% / +25% (worst +1%) | 3% / +25% (worst -5%) |

The CoinDCX column counts the TDS as lost; you can claim it back against your
tax when you file, so real results are a little better. These use Binance's
USDT prices; INR prices on CoinDCX track them, but also move with the
rupee-dollar rate.

Bad stretches were real: someone who started in mid-2021 was down about half
a year or two later. Past results do not promise future ones.

**India:** gains are taxed at 30% (plus cess), with 1% TDS withheld when you
sell, and each profit sale counts. Losses cannot be set off against gains.

## Why there is no trading bot

An earlier version also had a chart-reading trading bot. Tested on three
years of real Binance prices it lost money (-7% to -10%) while simply holding
BTC returned about +200%, so it was removed. It is still in this repository's
git history.

## Tests

```
python -m unittest discover -s tests
```
