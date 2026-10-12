# Synthetic worked example

Synthetic order O1: two lines net sales 60 and 40, shared order discount already allocated in those net amounts. Fulfillment assigns line 60 toA and 40 toB. Correct location sales A60+B40=100; repeating order total 100 at each would overstate 200. Channel is online store even if campaign source was social. Cohort 100 orders has 8 cancelled by day 30:8%; a newer 100-order cohort has 3 by day 2 and is immature, so no proven decline to 3%.

Report bridge: order sales 100; cash captured 110 includes shipping 5+tax 5. Difference 10 is explained; payout 107 after fee 3 is a separate cash-settlement measure.

## Boundary case 1

Two discount codes appear but actual allocation by code is unavailable. Show order discount once in multi-code/unallocated bucket; never attribute full discount to each code.

## Boundary case 2

An order has partial fulfillment and an unassigned line. Keep unallocated location revenue visible so totals reconcile; do not redistribute it silently.
