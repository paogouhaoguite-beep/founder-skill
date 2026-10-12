# Synthetic worked example

Input: September USD paid orders O1=100, O2=50; export also includes “Grand Total”=150. O3=40 is cancelled. Metric: average paid-order value before refunds for September by order date.

Valid rows O1/O2; numerator 150 USD; denominator 2 distinct paid orders; AOV 75 USD. Excluded summary row prevents doubling, and cancelled O3 is excluded by the stated definition. This is not customer lifetime value or settlement cash.

Boundary scenario 1: Refund-date and order-date views differ. State which is used and show the difference when material; do not blend them.
Boundary scenario 2: USD and EUR rows share an amount column with no FX table. Return separate currency results; do not sum them into a single money total.
