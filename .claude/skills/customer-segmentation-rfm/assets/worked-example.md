# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic as-of 2026-10-01, 90-day window, full refunds excluded from F and last-order eligibility. A: paid USD 100 on Sep 21 and USD 50 on Sep 26 with USD 10 partial refund → R=5, F=2, M=140. B: paid USD 80 on Sep 11, fully refunded → no qualifying order, F=0, M=0 and R undefined. C: paid USD 140 on Sep 26 → R=5, F=1, M=140. A and C tie on R and M; preserve those ties. If A has opted out of email, “recent repeat” is still its behavioral segment but promotional eligibility is false.

## Acceptance scenarios

1. Given two line items sharing an order ID, count one order for F and reconcile line revenue once.
2. Given tied R/M values and an unsubscribed high-value customer, preserve equal scores and exclude that customer from marketing activation.
