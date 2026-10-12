# Synthetic worked example

Synthetic owned layers are 10 units at USD 5 and 20 units at USD 8. Finance supplies FIFO. Issue 12 costs 10×5+2×8 = **66**; remaining 18 units value 18×8 = **144**. Opening receipts total 210 = issued 66+ending 144. Another SKU has 4 units and missing cost: report **known value 144 plus 4 uncosted units**, not total 144 with implied zero cost. Retail price 12 for those units implies retail exposure 48, not cost 48.

## Boundary case 1

Catalog quantity is parent 30 and child variants 10+20. Confirm who owns stock; do not count 60. If unresolved, block aggregate valuation.

## Boundary case 2

Cost currency EUR and stock report currency USD with no dated conversion. Keep EUR value separate and request finance conversion basis rather than using a current rate.
