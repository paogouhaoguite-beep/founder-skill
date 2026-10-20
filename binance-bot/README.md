# Binance weekly buy bot

Buys a fixed amount of crypto on Binance every week, taking turns between
BTC, ETH and SOL. When everything it bought is worth 30% more than the money
put in (after fees), it sells it all and starts a new round.

**No bot can promise profit.** This one only makes money if the coins are
worth more when it sells than the average price it paid. Crypto can fall by
half and stay down for a year or more. Only use money you can afford to lose.

## How it works

1. Every week, on `dca_day` (Monday by default, UTC), it buys `dca_amount`
   USDT (6 by default) of the next coin in `dca_symbols`.
2. If the bot is off on the buy day, it buys later the same week. A week that
   passes entirely while it is off is skipped, never doubled up.
3. Every hour it checks the value of everything bought this round. Once that
   is `dca_take_profit` (30%) above the money put in, after the selling fee,
   it sells it all. The USDT stays in your Binance Spot wallet.
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

### Real money

1. On Binance, create an API key with **Enable Spot & Margin Trading** ON and
   **Enable Withdrawals OFF**. Restrict it to your IP address if you can.
2. Put the keys in environment variables (never in a file you share):
   ```
   export BINANCE_API_KEY=...
   export BINANCE_API_SECRET=...
   ```
   (Windows Command Prompt: `set BINANCE_API_KEY=...`)
3. Keep enough USDT in your Spot wallet for the weekly buys. If there is not
   enough, the bot waits and retries rather than buying less.
4. In `config.json` set `"live_trading_acknowledged": true`.
5. `python main.py dca --live`

The bot only needs to run at least once each week, so a phone with Termux works.

## Settings

| Key | Default | Meaning |
|---|---|---|
| `dca_amount` | `6` | USDT spent each week (Binance's minimum order is about 5) |
| `dca_symbols` | `["BTCUSDT", "ETHUSDT", "SOLUSDT"]` | coins to buy, one per week, in turn |
| `dca_day` | `monday` | buy day (UTC) |
| `dca_take_profit` | `0.30` | sell everything at this profit (0.30 = 30%) after fees; `null` = never sell |
| `dca_poll_seconds` | `3600` | how often it checks |

## Safety details

- **Never buys twice, never sells your own coins.** Every order is saved
  with its ID in the history file before it is sent. If the reply is lost,
  Binance is down, or the phone dies mid-order, the next check asks Binance
  about that exact order instead of sending another. A profit sale that
  stops halfway resumes coin by coin. The bot only ever sells what it bought,
  so coins you hold yourself in the same account are safe.
- **One copy at a time.** Starting the bot while another copy is already
  running (say, in a second Termux window) is refused, because two copies
  would buy twice.
- **Delisted coins.** If a coin stops trading on Binance (EOS was delisted in
  2025), the bot notices within an hour, skips it for buying, ignores the
  frozen price Binance keeps showing for it, and lists anything it could not
  sell as STRANDED in `status` for you to handle in the Binance app.
- **Small leftovers.** If one coin's share is under Binance's 5 USDT minimum
  when it is time to sell, it is kept and carried into the next round.
- **Unfilled buys** (no sellers at that moment) are not recorded and are
  retried later the same week.
- **Clock drift.** If the phone's clock drifts and Binance rejects requests,
  the bot resyncs with Binance's clock by itself.
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
remove `"SOLUSDT"` for the lower-risk pair.

Bad stretches were real: someone who started in mid-2021 was down about half
a year or two later. Past results do not promise future ones.

**India:** gains are taxed at 30%, plus 1% TDS when you sell, and each
profit sale counts. Fees are 0.1% per buy and per sell.

## Why there is no trading bot

An earlier version also had a chart-reading trading bot. Tested on three
years of real Binance prices it lost money (-7% to -10%) while simply holding
BTC returned about +200%, so it was removed. It is still in this repository's
git history.

## Tests

```
python -m unittest discover -s tests
```
