# Synthetic worked example

Synthetic October USD tax ledger: sale S1 product 8+shipping 1; refund R1 credits product−2 from a September sale; sale S2 product 4. Net recorded October tax =8+1−2+4 = **11**. This is a collected-tax schedule, not the amount legally due. Two rate rows share country/state but cover postal 10001 vs 10002: **not proven duplicates**.

| Evidence | Result | Next action |
|---|---|---|
| October tax events | USD 11 | hand off to tax owner |
| Postal predicates differ | distinct scopes | retain pending approved rule comparison |

## Boundary case 1

A partially refunded order has original tax 10 but refund tax is unavailable. Do not subtract 10 or omit silently; show known subtotal and refund-tax gap.

## Boundary case 2

Merchant supplies an old nexus threshold with no effective date. Record unverified rule, request current authority/adviser review and make no registration or rate change.
