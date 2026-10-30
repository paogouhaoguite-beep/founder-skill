# Test Report

**Date:** 2026-10-20. Updated 2026-10-21 (bug review) and 2026-10-30 (future-use review, Deriv API migration) (UTC)
**Environment:** Linux, Python 3.13.16, websockets 17.3, rich 15.0.0, PyYAML 6.0.3,
pytest 9.1.1, ruff 0.16.9, mypy 2.3.1

## Summary

| Check | Result |
|---|---|
| Unit and integration tests (`python -m pytest`) | **135 passed, 0 failed** (~5 s). Stable across 3 consecutive runs. Includes regression tests for every bug in sections 3 and 4. |
| Line coverage (`pytest --cov=derivbot`) | **95%** |
| Soak test, new protocol (120 iterations each in paper and demo-live; injected disconnects, rate limits and a REST login outage) | **33 trades, 0 error-log lines.** Each reconnect logged in with a fresh one-time URL. Balances reconcile to the cent. |
| Lint (`ruff check .`) | **All checks passed** (E, F, W, I, B, UP, SIM rule sets) |
| Types (`mypy`, `strict = true`, package `derivbot`) | **No issues found in 13 source files** |
| E2E test trade, offline simulator (`--e2e-test --mock-server`) | **SUCCESS.** Full lifecycle completed. |
| **E2E test trade, real Deriv servers** (`--e2e-test`) | **SUCCESS (2026-10-30)** on Deriv's new public API with live Volatility 100 prices. The exit tick was checked independently against Deriv's tick history (section 4). |
| Bot main loop, real Deriv servers (`--paper --no-dashboard`) | **Ran cleanly**, 0 errors in the log. |
| Demo-account trading via the new API login | **Not run against a real account.** No token is available in the build environment. It is built from Deriv's published schemas and tested against the simulator. |

## 1. Test suite

All tests run offline. The API, executor, bot and E2E tests use a **real WebSocket
connection** to `derivbot.mock_server.MockDerivServer`, a local server that speaks
Deriv's v3 protocol (`authorize`, `balance`, `ticks_history`, `proposal`, `buy`,
`proposal_open_contract`, `sell`, and error envelopes). Tests can inject rate
limits, refused handshakes and dropped connections. A controllable clock makes
contract expiry deterministic.

| File | Tests | Coverage |
|---|---:|---|
| `test_config.py` | 22 | The shipped `config.yaml` is valid. Defaults. int→float coercion. Rejection of out-of-range risk % (>2%), fast ≥ slow, bad duration unit, min > max stake, non-ws endpoint, small candle_count, bad log level, negative balance. Wrong types, including `bool` given for `int`. Unknown keys and sections. Missing or malformed YAML. No token in the config. |
| `test_strategy.py` | 11 | EMA against a hand calculation (SMA seed). Short input and invalid period. CALL on a bullish cross and PUT on a bearish cross. No signal in a steady trend or with too few candles. A signal fires only on the crossing candle. Gap filter. `last_crossover` / `trend`. Invalid periods. The forming candle is dropped. |
| `test_risk.py` | 17 | Position sizing (1%, 2%, rounding down, the `max_stake` cap, below `min_stake` → skip, zero and negative balance). Stake never exceeds the risk budget. Daily loss limit at its boundary, including open stakes in equity. Daily limit engages the kill switch and stays halted. Pause after N losses and resume after the cooldown. A win resets the streak. Open-position and trades-per-day limits. Balance too small. Kill-switch file. Error counter trips the kill switch, and a success resets it. |
| `test_database.py` | 8 | Open/close roundtrip and double-close protection. All required fields are logged. Win rate, profit factor, gross profit and loss, realized, unrealized and total P/L, current and max drawdown (absolute and %). Empty DB and no-loss profit factor (∞). Paper and live modes are isolated. Daily and weekly summaries. Risk inputs (trailing losses, daily P/L, trades per day, open stakes). Persistence to a file. |
| `test_api.py` | 19 | Connect, authorize, ping, balance, candles, ticks. `app_id` in the URL. Invalid token → `AuthorizationError` with no retry. Auth required for private calls. Rate limit retried with growing backoff, and an error once retries are exhausted. **Reconnect and re-authorize after a server disconnect.** **`buy` is not re-sent after a disconnect (outcome unknown).** Retries after refused handshakes, and gives up with a clear error. Unreachable endpoint. Concurrent requests matched by `req_id`. API error surfaced. Hung server → timeout → reconnects → failure. Real-account token detected. Error-code classification. |
| `test_executor.py` | 6 | Rise/Fall rules (a tie is a loss). **Paper trade never sends `buy`**, uses the proposal price, locks the stake, and settles from the exact tick at expiry. Tick-duration paper contract with mark-to-market. Low payout rejected. Live executor buys, marks unrealized P/L, settles, and reconciles the balance. `close_all` sells. |
| `test_bot.py` | 13 | Full paper cycle: signal → trade → no duplicate on the same candle → settlement → loss streak. **Daily loss limit halts the bot before any signal is evaluated.** Loss streak restored from the DB after a restart. Invalid token → kill switch. Live mode without a token → kill switch. **Real-money account refused by default** and allowed only with an explicit opt-in. Demo live mode sends `buy` and refreshes the balance. `KILL_SWITCH` file stops the run. Repeated errors trip the kill switch. Connection loss trips the kill switch. Kill switch sells live positions when configured. Dashboard and report render all required panels. |
| `test_e2e_and_cli.py` | 8 | E2E succeeds against the simulator through all 7 steps, with no `buy`. E2E failure report names the step and gives a hint and traceback. Signal fallback logic. CLI flag parsing. Bad config → exit 2. `--e2e-test --mock-server` then `--report` via the CLI. Live mode without a token refuses (exit 2). Paper run via the CLI creates its log and DB. |

### Bugs found and fixed during testing

1. **Stale dashboard balance after opening a trade.** The balance shown was the
   pre-trade snapshot until the next loop iteration. The bot now refreshes the
   balance right after a trade is placed. Covered by `test_dashboard_and_report_render`
   and `test_demo_live_mode_places_buy`.
2. **Unreadable connection errors.** A rejected handshake logged the entire HTTP
   response, headers included. Errors are now summarized, e.g. "handshake rejected
   with HTTP 520".
3. Lint and type issues flagged by ruff and mypy were fixed: missing `zip(strict=)`,
   long lines, nested `if`, and an `Any` return from the connect factory.

## 2. Automatic end-to-end test trade

The E2E command always runs in **paper mode**, so no `buy` request is ever sent.
It uses the configured strategy and risk engine and checks every stage of the
lifecycle: signal generation → proposal request → simulated execution → result
logging → P/L update.

### 2a. Offline simulator: SUCCESS

```
$ python -m derivbot --e2e-test --mock-server
╭────────────────────────── E2E TEST TRADE: SUCCESS ───────────────────────────╮
│   ✔ connect     connected to ws://127.0.0.1:41521/websockets/v3; authorized  │
│ VRTC0000001 (virtual=1)                                                      │
│   ✔ market_data 100 closed 60s candles for R_100; last close 1019.69         │
│   ✔ signal      CALL - EMA9 crossed above EMA21 5 candle(s) ago [most recent │
│ crossover (5 candles ago) - no fresh cross right now]                        │
│   ✔ risk        paper balance 100.00 USD; risk 1.0% -> stake 1.00            │
│   ✔ proposal    proposal priced; simulated execution logged as trade #1:     │
│ CALL stake 1.00 payout 1.95 entry 1018.17 (5t)                               │
│   ✔ settlement  LOST: entry 1018.17 exit 1018.1 P/L -1.00                    │
│   ✔ verify      DB row #1 status=lost pnl=-1.00; balance 100.00 -> 99.00;    │
│ total realized -1.00, win rate 0.0% over 1 closed paper trade(s)             │
╰──────────────────────────────────────────────────────────────────────────────╯
exit=0
```

The trade row in `data/e2e_trades.db` was: `id=1, opened 13:57:33Z, closed 13:57:38Z,
R_100 CALL, stake 1.00, payout 1.95, entry 1018.17, exit 1018.10, lost, P/L −1.00`.
The trade lost, which is a legitimate outcome. The test checks that the lifecycle
works, not that the trade makes money. The `verify` step confirmed that the DB row
was closed, that the stored P/L matches the settlement, that realized P/L moved by
exactly −1.00, and that the paper balance went from 100.00 to 99.00.

An earlier run in this session caught a *fresh* crossover on the latest closed
candle (PUT) and also completed. When no fresh cross exists, the E2E test uses
the most recent crossover in the window and labels it, so that a single test
trade always happens. The normal bot loop **never** does this: it trades only on
a fresh cross.

### 2b. Real Deriv API, 2026-10-20: could not connect from the build sandbox (superseded by section 4)

```
$ python -m derivbot --e2e-test
WARNING derivbot.api: Connect attempt 1 failed (handshake rejected with HTTP 520); retrying in 1.0s
...  (attempts 2-5, backoff 2s, 4s, 8s, 16s)
ERROR   derivbot.e2e: [E2E] FAILED at connect: ConnectionLostError: could not connect to
        wss://ws.binaryws.com/websockets/v3 after 6 attempts: handshake rejected with HTTP 520
╭─────────────────────────── E2E TEST TRADE: FAILED ───────────────────────────╮
│   ✘ connect     ConnectionLostError: could not connect to                    │
│ wss://ws.binaryws.com/websockets/v3 after 6 attempts: handshake rejected     │
│ with HTTP 520                                                                │
│ Failed step: connect                                                         │
│ Hint: Check internet access / firewall / proxy (WebSocket upgrades must be   │
│ allowed) and that api.endpoint and api.app_id are correct.                   │
╰──────────────────────────────────────────────────────────────────────────────╯
exit=1
```

**Why:** the sandbox where this was built sends all outbound traffic through an
HTTPS proxy that does not support WebSocket upgrades. A plain `websockets.connect`
to both `ws.binaryws.com` and `ws.derivws.com` failed with the same 520 outside
the bot. This is an environment restriction, not a bot defect. It does show that
the reconnect and backoff logic and the failure report work as designed.

**To complete this step yourself** (no token needed, because paper mode uses only
public endpoints):

```bash
cd deriv_bot && pip install -r requirements.txt
python -m derivbot --e2e-test          # ~10-20 s with the default 5-tick contract
cat data/e2e_result.json               # full machine-readable result
```

If you set `DERIV_API_TOKEN` (demo), the E2E test also verifies authorization and
reports `virtual=1`. Before running demo-account trading, confirm that Deriv's
current minimum stake for your currency matches `risk.min_stake`.

## 3. Post-merge bug review (2026-10-21)

I re-read the merged code for behaviour that real Deriv conditions would expose
but the first test suite didn't cover. For each bug, I first wrote a test that
**failed on the merged code** (13 of the 14 new tests failed). Then I fixed the
code until every test passed.

| # | Bug | Impact | Fix |
|---|---|---|---|
| 1 | Restarting the bot reset the loss-streak cooldown | After 3 losses you could restart and trade straight away, bypassing the pause | The cooldown is restored from the journal (time of the last loss). The time a cooldown ends is saved so a later restart doesn't re-pause. |
| 2 | A restart within the same candle re-traded the same signal | Duplicate trade on one signal | The last traded candle is saved in the DB |
| 3 | A trade could push today's loss past the daily limit | With 1% stakes, today's loss could end at about 5.9% against a 5% limit | A trade is refused if losing its stake (plus open stakes) would breach the limit |
| 4 | Paper settlement used the local clock | A fast clock settled trades **early on a stale tick**, giving wrong results | Expiry is judged from Deriv's latest tick timestamp |
| 5 | Tick contracts settled long after expiry could use the wrong tick | Wrong exit price after downtime | Tick history is requested over a bounded window from entry |
| 6 | The forming candle was detected with the local clock | A fast clock let the strategy act on an unfinished candle | The last candle (always the forming one) is dropped by position |
| 7 | A failed startup left the WebSocket open, and unexpected startup errors escaped | Leaked connection or crash instead of a clean halt | Any startup error halts cleanly and closes the socket |
| 8 | Weekly summary used `%W`, which restarts at week 00 on 1 January | A week spanning New Year was split in two | ISO weeks |
| 9 | A `buy` whose reply was lost (dropped connection) was never journaled | A real demo contract went untracked, so P/L, limits and open positions were wrong | Pending-buy marker plus reconciliation from `portfolio` and `profit_table` on the next start |
| 10 | "Future exception was never retrieved" logged when the socket died mid-send | Noisy error log during reconnects | The exception on the failed future is consumed |

After the fixes: 117 tests passed (3 runs), ruff and mypy are clean, and the
offline E2E test trade succeeded again. The soak test above exercised all of
this together.

## 4. Future-use review (2026-10-30)

### 4a. Deriv is retiring the API the bot was built on

Deriv now runs a new Options API at `api.derivws.com`. Its docs describe the
legacy options platform as "read-only access to a user's pre-upgrade options
trading data" and say the legacy endpoints "will be removed once all users have
been fully migrated". I tested the new API's public endpoint from the build
environment (it is reachable, unlike the legacy one):

| Check against the real new API | Result | Effect on the bot as merged |
|---|---|---|
| `proposal` with `symbol` | `InputValidationFailed: "symbol": "field is not allowed"` | **Every trade would fail.** The new API requires `underlying_symbol`. |
| `authorize` call | `UnknownMethod` | **Demo-trading login would fail.** Login is now REST: list accounts, then request a single-use WebSocket URL (one-time password, valid 120 s). |
| `portfolio` symbol field | renamed `underlying_symbol` (per Deriv's comparison docs) | Interrupted-buy recovery would skip the contract |
| Minimum stake | `validation_params.stake.min = "0.35"` | Matches `risk.min_stake` |
| Candles | the forming candle is still the last element | `drop_forming` is correct |

**Fix:** `api.protocol: new` is now the default. The client logs in with
`GET /trading/v1/options/accounts` and `POST .../accounts/{id}/otp` (Bearer token
plus `Deriv-App-ID`), fetches a **fresh** one-time URL on every reconnect, and
sends `underlying_symbol`. Recovery reads either field name. `protocol: legacy`
keeps the old flow for accounts that haven't migrated. The simulator now speaks
both protocols, including single-use OTPs and the REST login, so the whole test
suite exercises the new flow.

### 4b. First test trade on Deriv's real servers: SUCCESS

```
$ python -m derivbot --e2e-test          # no token, paper mode, 2026-10-30 17:55 UTC
   ✔ connect     connected to wss://api.derivws.com/trading/v1/options/ws/public
   ✔ market_data 100 closed 60s candles for R_100; last close 590.42
   ✔ signal      CALL - EMA9 crossed above EMA21 14 candle(s) ago [most recent crossover]
   ✔ risk        paper balance 100.00 USD; risk 1.0% -> stake 1.00
   ✔ proposal    simulated execution logged as trade #1: CALL stake 1.00 payout 1.95
                 entry 591.06 (5t)
   ✔ settlement  LOST: entry 591.06 exit 590.94 P/L -1.00
   ✔ verify      DB row closed, P/L matches, balance 100.00 -> 99.00
exit=0
```

**Independent check** against Deriv's tick history for R_100: the entry tick at
epoch 1793382910 was 591.06. The ticks after it were 590.89, 590.92, 591.19,
590.90 and **590.94** (5th), so the 5-tick CALL correctly lost. The bot's main loop
(`--paper --no-dashboard`, 4 iterations) also ran against the real servers with 0
errors.

### 4c. Other problems that would hinder future use, now fixed

| # | Problem | Impact | Fix |
|---|---|---|---|
| 11 | Closed market counted as an error | Trading forex (e.g. `frxEURUSD`): at the weekend, 5 refused proposals fired the **kill switch** | `MarketIsClosed` is treated as "skip and wait", with no error count |
| 12 | Account currency not checked | A non-USD account: every proposal fails, or stakes and limits are in the wrong currency | The bot refuses to start and explains the mismatch |
| 13 | File paths relative to the *current folder* | Started from cron, a service or another folder, the bot silently used a **new, empty journal**: risk limits and loss streak reset, history missing | Paths in `config.yaml`, `.env` and the E2E outputs resolve against the config file's folder |
| 14 | Two copies could run at once | Double trades, and each copy applies the daily limit separately (2× the intended risk) | OS-level single-instance lock per journal and mode (Linux, macOS, Windows), exit code 4 |
| 15 | Recovery filtered contract types `CALL`/`PUT` | Deriv renamed contract types in the new API, so an interrupted buy could stay untracked | Adopts any contract on the configured symbol |
| 16 | Dependencies had no upper bounds | A future major release of `websockets`, `rich` or `PyYAML` could break installs | Bounded to tested major versions |
| 17 | The bot was not an installable package | `python -m derivbot` only worked from inside `deriv_bot/` (`No module named derivbot` elsewhere), which undermined #13 | `pip install -e .` adds a `derivbot` command. Verified from `/tmp` against Deriv's real servers: E2E SUCCESS (a CALL that **won** +0.95), with files written next to `config.yaml`. |

### 4d. Risks that remain (not code bugs)

- **No proven edge.** On random synthetic indices with a 95% payout, the expected
  result per trade is about −2.5% of the stake.
- **New-API demo login untested on a real account.** Run one demo session and
  check the first trade.
- **The legacy protocol will stop working** whenever Deriv completes migration.
- **Regulation.** For Indian residents, Deriv may appear on the RBI Alert List of unauthorised forex platforms. Check RBI's current list
  before depositing.

## Reproducing this report

```bash
python -m pytest -v                       # suite
python -m pytest --cov=derivbot -q        # coverage (needs pytest-cov)
ruff check . && mypy                      # static analysis
python -m derivbot --e2e-test --mock-server   # offline
python -m derivbot --e2e-test                 # real Deriv servers, no token needed
```
