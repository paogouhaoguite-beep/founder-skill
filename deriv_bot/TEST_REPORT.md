# Test Report

**Date:** 2026-10-20, updated 2026-10-21 after a post-merge bug review (UTC)
**Environment:** Linux, Python 3.13.16, websockets 17.3, rich 15.0.0, PyYAML 6.0.3,
pytest 9.1.1, ruff 0.16.9, mypy 2.3.1

## Summary

| Check | Result |
|---|---|
| Unit and integration tests (`python -m pytest`) | **117 passed, 0 failed** (~5 s). Stable across 3 consecutive runs. Includes 13 regression tests for the bugs in section 3. |
| Line coverage (`pytest --cov=derivbot`) | **95%** (1678 statements) |
| Soak test (120 iterations each, paper and demo-live, injected disconnect and rate limits) | **31 trades, 0 error-log lines.** Balances reconcile to the cent. |
| Lint (`ruff check .`) | **All checks passed** (E, F, W, I, B, UP, SIM rule sets) |
| Types (`mypy`, `strict = true`, package `derivbot`) | **No issues found in 12 source files** |
| E2E test trade, offline simulator (`--e2e-test --mock-server`) | **SUCCESS.** Full lifecycle completed. |
| E2E test trade, real Deriv API (`--e2e-test`) | **Not completed from the build sandbox.** The sandbox's egress proxy rejects WebSocket upgrades (HTTP 520 from `ws.binaryws.com`). The bot produced the expected detailed failure report. **Run this command on your own machine.** |

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

### 2b. Real Deriv API: could not connect from the build sandbox

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

## Reproducing this report

```bash
python -m pytest -v                       # suite
python -m pytest --cov=derivbot -q        # coverage (needs pytest-cov)
ruff check . && mypy                      # static analysis
python -m derivbot --e2e-test --mock-server
python -m derivbot --e2e-test
```
