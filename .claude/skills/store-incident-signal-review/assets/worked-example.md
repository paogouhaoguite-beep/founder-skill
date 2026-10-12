# Synthetic worked example

Synthetic baseline 200 payment attempts has 190 successes (95%). Current 100 attempts has 70 successes (70%); failed 30 comprise 20 gateway timeouts,5 issuer declines and 5 unknown. This is an observed 25 percentage-point drop in attempt success, not 30 proven lost orders. All 20 timeouts start after a connector change; hypothesis merits trace review, not proven cause. Alert draft: merchant-supplied minimum 50 attempts and sustained 10 minutes, success below its approved 85% tolerance, only if source lag under its approved 2 minutes; route once to Payments owner with runbook.

## Boundary case 1

Current event feed is 30 minutes stale. Fire or propose data-freshness incident, not a zero-sales outage conclusion.

## Boundary case 2

One customer retries five times then succeeds. Attempt failure rate and unique-checkout outcome must remain distinct; do not count five lost customers.
