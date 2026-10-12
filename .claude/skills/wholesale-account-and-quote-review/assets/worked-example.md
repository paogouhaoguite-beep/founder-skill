# Synthetic worked example

Synthetic company C1 has locations L1/L2. Buyer B1 is authorized only L1, catalogA, MOQ6 with pack 3. Quote Q1 requests 7 units at 10: line 70 but **pack multiple fails**; valid quantity 9 would be 90 only if buyer accepts revision. L2 has no catalog assignment: do not inherit L1 automatically. Accepted Q2 version 2 is 9 units at 10 plus shipping 8 and supplied tax 0 =98; order O2 must link Q2v2, not obsolete Q1.

## Boundary case 1

Company flag exists but buyer contact is unverified. Keep account review pending; do not expose wholesale catalog or other employees’ orders.

## Boundary case 2

Quote shipping is “TBD”. Show merchandise 90 plus shipping unknown, not total 90 or a binding all-in offer.
