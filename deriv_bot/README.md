# Deriv EMA-Crossover Trading Bot (educational)

> **Disclaimer.** This project is for **educational purposes only**. It is not
> financial advice. Trading binary options and synthetic indices carries a high
> risk of losing money, and past or simulated results do not predict future
> results. You alone are responsible for how you use it, and you must comply with
> [Deriv's Terms and Conditions](https://deriv.com/terms-and-conditions) and the
> rules of your jurisdiction. Develop and validate on a **demo (virtual)
> account** or in `--paper` mode. The bot refuses to trade on a real-money account
> unless you explicitly opt in.

An autonomous Python bot that trades Deriv Rise/Fall (CALL/PUT) contracts through
Deriv's official WebSocket API (`wss://ws.binaryws.com/websockets/v3`). It is built
to **preserve capital first**: small fixed-fraction stakes, a daily loss limit,
a pause after a losing streak, and a kill switch.

## Features

| Area | What it does |
|---|---|
| API | Async WebSocket client with `req_id` request matching, authorization, exponential-backoff reconnect plus re-authorize, rate-limit backoff and request timeouts. A `buy` or `sell` is **never re-sent** after a dropped connection, because it may already have executed. |
| Strategy | EMA 9/21 crossover on **closed** candles. CALL when the fast EMA crosses above the slow one, PUT when it crosses below. Optional gap filter against whipsaws. Each candle produces at most one signal. All parameters are configurable. |
| Risk | Stake = balance × risk % (hard cap 2%), rounded **down**, with min/max stake. If the minimum stake would exceed the risk budget, the trade is **skipped** rather than over-risked. Also: daily loss limit (kill switch), and a new trade is refused if losing its stake could push today's loss past that limit (open stakes count as already lost). Pause after N consecutive losses with a cooldown that survives restarts, max trades per day, max open positions, and a minimum payout ratio. |
| Kill switch | Stops trading immediately on a daily loss limit, an authorization error, a lost connection, an ambiguous buy, repeated errors, or when a `KILL_SWITCH` file is created. Can optionally sell open live contracts. |
| Journal | Every trade goes to SQLite with timestamps, symbol, direction, stake, payout, entry and exit price, result and P/L. Reports cover realized and unrealized P/L, win rate, profit factor, current and max drawdown, and daily and ISO-weekly summaries. Risk state (loss streak, cooldown, last traded signal) is rebuilt from the DB after a restart. |
| Interrupted buys | If the connection drops during a `buy`, the bot stops. On the next start it checks `portfolio` and `profit_table` and adopts any contract that did execute, so the trade isn't lost from the journal. |
| Paper mode | `--paper` prices every trade with the real `proposal` endpoint, **never calls `buy`**, and settles from the real tick at expiry. Settlement uses Deriv's tick timestamps, so drift in your computer's clock can't settle a trade early or on the wrong tick. |
| Dashboard | A `rich` live view showing balance, status, today's P/L and win rate, open positions, recent trades, performance, and the kill-switch reason. |
| Offline simulator | `--mock-server` runs a local server that speaks Deriv's protocol, for testing without network access or an account. |

## Project layout

```
deriv_bot/
├── config.yaml             # strategy, risk, symbol, duration, safety settings
├── requirements.txt
├── .env.example            # DERIV_API_TOKEN=... (copy to .env, never commit)
├── derivbot/
│   ├── __main__.py         # CLI (python -m derivbot)
│   ├── config.py           # YAML -> validated dataclasses
│   ├── api.py              # Deriv WebSocket client (reconnect, rate limits, errors)
│   ├── strategy.py         # EMA crossover signals
│   ├── risk.py             # position sizing, limits, kill switch
│   ├── database.py         # SQLite journal + P/L analytics
│   ├── executor.py         # PaperExecutor / LiveExecutor
│   ├── bot.py              # main loop and error classification
│   ├── dashboard.py        # rich dashboard + report
│   ├── e2e.py              # automatic end-to-end test trade
│   └── mock_server.py      # local Deriv-protocol simulator (tests / offline)
├── tests/                  # pytest suite (117 tests)
└── TEST_REPORT.md
```

## Setup

```bash
cd deriv_bot
python -m venv .venv && source .venv/bin/activate     # Python 3.10+
pip install -r requirements.txt
cp .env.example .env    # then paste your DEMO account token
```

To create the token, log in to your **demo** account at
<https://app.deriv.com/account/api-token> and create a token with the **Read** and
**Trade** scopes. The bot reads it from the environment variable named in
`api.token_env` (default `DERIV_API_TOKEN`) or from `.env`. Never put a token in
`config.yaml`. For production use, register your own `app_id` at
<https://api.deriv.com> and set `api.app_id`.

## Usage

```bash
# 1. Run the automatic end-to-end test trade (paper; exits 0 on success, 1 on failure)
python -m derivbot --e2e-test                  # against the real Deriv API
python -m derivbot --e2e-test --mock-server    # offline, against the local simulator

# 2. Paper trading. No token needed, no buy requests ever sent.
python -m derivbot --paper

# 3. Demo-account trading. Needs DERIV_API_TOKEN from a VIRTUAL account.
python -m derivbot

# Reports and options
python -m derivbot --report          # P/L, win rate, profit factor, drawdown, daily/weekly
python -m derivbot --paper --no-dashboard   # plain log output (e.g. under systemd)
touch KILL_SWITCH                    # emergency stop; delete the file to allow restarts
```

Exit codes: `0` normal, `1` E2E failed, `2` config error or missing token, `3`
stopped by the kill switch, `130` Ctrl-C.

Logs go to `logs/bot.log` (rotating). Trades go to `data/trades.db`, with paper
and live trades kept apart by a `mode` column. The E2E test uses its own
`data/e2e_trades.db` and writes `data/e2e_result.json`.

## Configuration (`config.yaml`)

| Key | Default | Meaning |
|---|---|---|
| `trading.symbol` | `R_100` | Volatility 100 Index. Forex example: `frxEURUSD` (closed on weekends). |
| `trading.contract_duration` / `duration_unit` | `5` / `m` | Contract length. Units: `t`, `s`, `m`, `h`. |
| `trading.min_payout_ratio` | `0.75` | Skip a trade if (payout − stake) / stake is lower. |
| `strategy.fast_period` / `slow_period` | `9` / `21` | EMA periods. |
| `strategy.granularity` | `60` | Candle size in seconds. |
| `strategy.min_ema_gap_pct` | `0.0` | Whipsaw filter after a cross. |
| `risk.risk_per_trade_pct` | `1.0` | Stake as % of balance. Validated to (0, 2]. |
| `risk.daily_loss_limit_pct` | `5.0` | Kill switch once today's realized loss reaches this % of day-start equity (UTC day). |
| `risk.max_consecutive_losses` / `cooldown_minutes` | `3` / `60` | Pause after a losing streak. |
| `risk.min_stake` / `max_stake` | `0.35` / `50` | Stake bounds. Check Deriv's current minimum for your currency. |
| `risk.max_trades_per_day` / `max_open_positions` | `20` / `1` | Exposure limits. |
| `risk.max_critical_errors` | `5` | Consecutive unexpected errors before the kill switch fires. |
| `paper.starting_balance` | `100` | Virtual balance for `--paper`. |
| `safety.allow_real_account` | `false` | Trading on a non-virtual account is refused unless this is `true`. |
| `safety.kill_switch_file` | `KILL_SWITCH` | If this file exists, the bot halts. |
| `safety.close_positions_on_kill` | `false` | In live mode, try to sell open contracts when the kill switch fires. |

Unknown keys, wrong types and out-of-range values are rejected at startup with
a clear message.

## How a trade happens

1. **Settle** open trades. In paper mode this uses the tick at expiry (time
   durations) or the Nth tick after entry (tick durations). In live mode it uses
   `proposal_open_contract`. Results update the loss-streak counter.
2. **Risk gate**: kill-switch file, halted state, daily loss limit, cooldown, open
   positions, trades per day, minimum-stake affordability, and whether losing
   this stake could breach today's loss limit.
3. **Signal**: fetch candles, drop the candle that is still forming (always the
   last one Deriv returns), then evaluate the EMA crossover on the latest closed
   candle. Each candle is traded at most once, even across restarts.
4. **Size**: `floor(balance × risk%)`, capped at `max_stake`. Skipped if below
   `min_stake`.
5. **Price** with `proposal`. Rejected if the payout ratio is too low.
6. **Execute**: `--paper` logs the trade at the proposal spot. Demo or live mode
   sends `buy` using the proposal id and price.
7. **Log** to SQLite. The dashboard and P/L update.

**Paper-mode approximation.** Paper entry uses the proposal's spot, while a real
contract enters on the next tick. Ties count as losses, as with Deriv Rise/Fall.
Unrealized P/L for an open paper trade is its intrinsic value at the current spot
(payout − stake if it is winning, −stake if it is losing).

## Development

```bash
pip install -r requirements.txt
python -m pytest            # 117 tests, ~5 s, fully offline (uses the local simulator)
ruff check .                # lint (flake8-compatible rules + bugbear, pyupgrade, isort)
mypy                        # strict type-check of the derivbot package
```

See [TEST_REPORT.md](TEST_REPORT.md) for the latest results.

## Honest limitations

- A 9/21 EMA crossover has **no proven edge** on synthetic indices, which are
  random by design. Rise/Fall payouts below 100% mean that a random strategy loses
  slowly over time. The risk controls limit how fast you can lose. They cannot
  make a losing strategy profitable. Paper-trade for a long time before even
  considering real money.
- Only one strategy is implemented. `EmaCrossoverStrategy` is the extension point.
- Daily limits use UTC days, matching Deriv's GMT trading day.
