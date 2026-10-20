# Binance spot trading bot

A small Binance spot bot. It studies recent charts, picks whichever famous
trading method has actually worked lately, trades it with a stop-loss on every
position, and reinvests its gains so the next trade gets bigger.

**Read this first: no bot can promise profit.** Markets change, fees eat small
accounts, and anything that "always makes money" is a scam. This bot is built
to *refuse to trade* when it cannot find an edge, and to cut losses short when
it is wrong. Expect losing trades and losing weeks. Only use money you can
afford to lose completely.

## What it does

1. **Reads the charts.** It downloads the last 1500 four-hour candles for each
   coin in `symbols` (BTC, ETH, SOL, BNB by default).
2. **Learns from famous traders.** It tests four published rule sets:

   | Strategy | Inspired by | Idea |
   |---|---|---|
   | `turtle` | Richard Dennis, the Turtle Traders | buy breakouts above the 20/55-candle high |
   | `trend_ema` | trend followers such as Ed Seykota | buy when a fast EMA crosses a slow one, in an uptrend |
   | `rsi2` | Larry Connors | buy sharp dips inside an uptrend, sell the bounce |
   | `macd_trend` | Gerald Appel (MACD) | buy MACD crosses above the 200 EMA |

3. **Proves it before using it (walk-forward test).** Each method is tuned on
   the older 70% of the chart and then run on the newest 30%, which it has
   never seen. It only becomes the "champion" if it made money in both parts,
   with at least 10 trades, a profit factor of 1.5 or better, and a drawdown under 20%,
   all after fees and slippage. If nothing passes, **the bot does not trade.**
   It re-learns every 24 hours.
4. **Trades the champion.** On every newly closed candle it checks for a buy
   signal. Each buy gets an ATR stop-loss that is also placed on Binance itself,
   so it still works if your computer goes off.
5. **Compounds.** Each trade risks 1% of *current* equity. After a win the
   account is bigger, so the next trade is bigger; after a loss it shrinks.
   Set `reinvest_pct` below `1.0` to lock part of each profit in a "vault" the
   bot will never trade again.
6. **Kill switch.** If equity falls 25% from its peak, it sells everything and
   stops until you run `reset-halt`.

How strict is step 3? On computer-generated random charts (where no real edge
exists) the filter was still fooled about 3 times in 25, and on charts with real
trends it found one 21 times in 25. A champion is a good sign, not a guarantee.

## Small accounts (under 5,000 rupees)

5,000 INR is roughly 55 to 60 USDT, which is enough: Binance's minimum order is
about 5 USDT. Set `start_equity` to your USDT amount for paper mode. With 1%
risk per trade the bot risks about 0.6 USDT per trade, so growth is slow and
steady by design. Things that eat into a small account:

- **Fees**: 0.1% per buy and per sell. Paying fees in BNB with the BNB discount
  turned on lowers this.
- **Indian tax**: 30% tax on crypto gains plus 1% TDS on sells. Losses cannot be
  offset against gains. Count this before you count profit.
- Raising `risk_per_trade` makes it grow faster **and** lose faster. Do not go
  above 0.02 (2%).

## Setup

Needs only Python 3.9+, no extra packages.

```
cd binance-bot
cp config.example.json config.json      # edit symbols, start_equity, etc.
python main.py learn                    # see what it learned (no account needed)
python main.py run                      # paper trading: pretend money, real prices
python main.py status                   # balance, open position, trade history
```

Run paper mode for **at least 2 to 4 weeks** before thinking about real money.

### Going live

1. On Binance, create an API key with **Enable Spot & Margin Trading** ON and
   **Enable Withdrawals OFF**. Restrict it to your IP address.
2. Put the keys in environment variables (never in a file you share):
   ```
   export BINANCE_API_KEY=...
   export BINANCE_API_SECRET=...
   ```
3. Hold USDT in your Spot wallet.
4. In `config.json` set `"live_trading_acknowledged": true`.
5. `python main.py run --live`

To practise with fake money on Binance's own test exchange first, set
`"base_url": "https://testnet.binance.vision"` and use testnet API keys.

The bot must stay running to trade (a computer that stays on, or a small cloud
server). If it stops, the stop-loss order already on Binance still protects an
open position.

## Settings

| Key | Default | Meaning |
|---|---|---|
| `symbols` | BTC/ETH/SOL/BNB vs USDT | coins it may trade (one position at a time) |
| `interval` | `4h` | candle size; shorter means more trades and more fees |
| `risk_per_trade` | `0.01` | fraction of equity lost if the stop is hit |
| `max_position_pct` | `0.95` | most of the account one trade may use (no leverage) |
| `reinvest_pct` | `1.0` | share of each profit reinvested; the rest is locked away |
| `max_drawdown` | `0.25` | kill-switch level |
| `relearn_hours` | `24` | how often it re-studies the charts |

## Tests

```
python -m unittest discover -s tests
```
