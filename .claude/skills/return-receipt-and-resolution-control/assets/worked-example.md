# Synthetic worked example

Synthetic R1 requests 3 fulfilled units. Warehouse receives 2:1 inspected sellable,1 damaged;1 remains in transit. Resolution for received units is exchange 1 plus cash refund 20 for 1. Expected inventory release **1**, not requested 3 or received 2. R1 is **mixed** resolution and remains physically incomplete. R2 was received Oct 1 09:00 and remains unresolved Oct 3 09:00: age 48 h; merchant threshold 36 h → overdue 12 h.

| Case | Sellable release | Pending | Resolution |
|---|---|---|---|
| R1 |1|1 in transit|mixed exchange/refund|
| R2 |unknown|resolution due|48 h open, overdue 12 h|

## Boundary case 1

Original order has 4 units but only 2 shipped and 1 already returned. At most 1 additional fulfilled unit is eligible pending policy, not 3.

## Boundary case 2

An old return is closed without a refund because exchange completed. Use exchange completion as resolution only per declared clock, not a fabricated refund timestamp.
