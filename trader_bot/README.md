# traderbot: the eleven trader skills on autopilot, with your yes

> **Not financial advice. Most day traders lose money.** This bot automates the
> Day Trader skills; it does not give them an edge they do not have. Run it on
> `--dry-run` and Alpaca **paper** for weeks before you even think about
> `--live`, and never trade money you cannot afford to lose.

`traderbot` runs the `skills/trader-*` pipeline on a timer, by itself, and
stops at one place: before every entry it shows you the ticket and waits for
you to type `yes`. Silence is a no.

```
every interval_s, while the market is open and you have no open trade:
  trader-scanner   opening-range breakouts in your symbols
  trader-entry     confirm the breakout on closed 5-minute bars (skip it if stale)
  trader-exit      stop and target before the entry
  trader-timemachine  10,000 replays; skip it if it leans toward the stop
  trader-news      the last 12 hours of headlines, shown on the ticket
  trader-alerts    a fresh quote for sizing and the risk check
  trader-budget    shares from your max loss per trade, one bracket order
  trader-risk      PASS or BLOCK against every limit in trader/config.json
  trader-broker    the ticket -> YOUR YES -> Alpaca (paper by default)
while it is open:
  Alpaca fills -> ticket.py fill; the bracket's stop or target closes it,
  or the bot cancels the bracket and sells at flat_by (15:55 by default)
```

The decisions are the skills' own tools, run as subprocesses from your
project folder, so every step leaves the same `trader/*.json` files you get
from the slash commands. You can open any of them, or ask Claude about them.

## Run it

Python 3.8+, standard library only. From the repo root:

```bash
cd trader_bot
python3 -m traderbot --workdir ~/trading init         # trader/config.json + trader/bot.json
# edit ~/trading/trader/config.json: budget, max_loss_per_trade_usd, max_daily_loss_usd, ...
python3 -m traderbot --workdir ~/trading run --dry-run # simulated broker, no keys, nothing sent anywhere
```

Alpaca paper trading (make **paper** API keys in the Alpaca dashboard):

```bash
export ALPACA_API_KEY=PK...  ALPACA_SECRET_KEY=...
python3 -m traderbot --workdir ~/trading run           # loops until Ctrl+C
python3 -m traderbot --workdir ~/trading run --once    # one pass
python3 -m traderbot --workdir ~/trading status        # the open trade and today's decisions
touch ~/trading/trader/STOP                            # kill switch: no new entries until you delete it
```

Real money needs **both** `"paper": false` in `trader/config.json` **and**
`--live`, with your live keys. Either one alone refuses to start, and so
does a paper key (`PK...`) with `--live`.

## What protects you

| guard | where |
| --- | --- |
| your explicit `yes` for that one order ("ok", "sure", "yes to all" are a no); no answer in `approval_timeout_s` is a no | trader-broker `ticket.py approve` |
| a stop on every order, max loss per trade, daily loss at the stops, trades per day, the entry window, position size, cash | trader-risk |
| one position at a time; each symbol tried once a day | the bot |
| a breakout older than `max_trigger_age_min` (10) is skipped | the bot |
| the Time Machine must not lean toward the stop (`min_tm_edge_pts`, 0) | the bot |
| no new entries when the account is down `max_daily_loss_usd` today | the bot, from Alpaca's equity |
| `trader/STOP` stops new entries | the bot |
| flat by `flat_by`: cancel the bracket, market sell (`auto_flatten`) | the bot (exits need no yes) |
| budget over the account's cash, `require_stop` off, paper/live mismatch: refuses to start | the bot |

If you stop the bot with a trade open, its stop-loss and take-profit stay at
Alpaca, but nothing flattens it at the close: do that yourself.

## trader/bot.json

| key | default | |
| --- | --- | --- |
| `symbols` | 20 liquid US stocks | what the scanner checks each pass (`null` = the whole universe, slow) |
| `interval_s` | 60 | seconds between passes |
| `max_candidates` | 5 | breakouts looked at per pass, newest first |
| `max_trigger_age_min` | 10 | skip a breakout that closed longer ago |
| `stop`, `target` | `or-mid`, `1R` | trader-exit's rules (`or-low`, `pct:1`, `atr:1.5`; `1.5R`, `2R`) |
| `replays` | 10000 | Time Machine replays |
| `min_tm_edge_pts` | 0 | points the target must beat break-even by in the replays |
| `news` | true | show the last 12 hours of headlines on the ticket |
| `approval_timeout_s` | 120 | seconds to answer before it counts as a no |
| `auto_flatten` | true | sell what is open at `flat_by` |

The limits themselves (`max_loss_per_trade_usd`, `max_daily_loss_usd`,
`max_trades_per_day`, `no_entries_before`, `no_entries_after`, `flat_by`, ...)
live in `trader/config.json`, where the skills read them. The bot logs every
decision to `trader/state/bot.log`.

## Limits worth knowing

- Quotes and bars are Yahoo's free, delayed, unofficial data. Good enough to
  practise, a handicap for minute-level timing.
- Long only, US stocks, opening-range breakouts: the setups the pack trades.
- Alpaca only. Another broker means another class with the same methods as
  `traderbot/alpaca.py` (account, clock, place, order, open_orders, cancel,
  position, close_position) on that broker's official API. Driving a broker's
  app or website instead breaks most brokers' terms and gets accounts frozen.
- The US pattern-day-trader rule may apply to a margin account under $25,000;
  `"pdt_guard": true` in trader/config.json makes trader-risk count day trades.

## Tests

```bash
cd trader_bot && python3 -m unittest discover -s tests -v
```

Offline: they replay the README trade (TSLA, October 19 2026, 10:15 AM ET)
through the real skill tools and a simulated broker. They check that it lands
on the skills' numbers (8 shares, stop 358.32, target 370.04) and that every
guard above holds.
