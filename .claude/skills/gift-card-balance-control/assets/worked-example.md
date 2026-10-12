# Synthetic worked example

Synthetic card G1 / 1234 is USD, paid origin, opening 100. Ledger contains redemption R1 −30, refund credit C1 +10 and redemption R2 −15. Closing = 100−30+10−15 = **65**, matching export. Gross redemptions are **45**, not initial value minus balance (35). G2 promotional card has balance 20 and is disabled: show it in a separate disabled/promotional bucket, not remove it.

| Card | Expected | Reported | Decision |
|---|---|---|---|
| G1 / 1234 | USD 65 | USD 65 | reconciled |
| G2 / 7788 | USD 20 | USD 20 | classification review; no writeoff |

## Boundary case 1

Same last4 occurs on two cards. Keep both stable card IDs; last4 is a display hint, not a unique key.

## Boundary case 2

A 25 USD issuance call times out without a receipt. Status is unknown; search for its request/recipient record before any retry. Never report issued or delivered without evidence.
