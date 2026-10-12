# Synthetic worked example

Input: Customers A and B bought in January; A and C bought in February. Visual shows distinct customers by month, with a two-month total.

Expected January 2, February 2, total 3, not 4. The total recomputes DISTINCTCOUNT across the selected window. A percent-of-total measure must state whether the denominator is all customers, selected customers or month customers; those are different metrics.

Boundary scenario 1: A region slicer is active. Verify whether the denominator should respect it before removing filters.
Boundary scenario 2: A daily stock table holds 10 units Monday and 8 Tuesday. End-of-period stock is 8 if Tuesday is the required valid snapshot, not 18.

## Join and freshness fixture

CampaignC/dayD spend 100 USD; the declared attribution model assigns exactly 150 USD net order revenue to that same campaign/day. Its one order has three item rows. Joining spend directly to item rows repeats 100 three times, falsely summing 300. Preaggregate the attributed order revenue to campaign/day first, then join one spend row to one revenue row: spend 100, credited revenue 150, model-reported ROAS 1.5×. Without the declared campaign/day attribution,150/100 is only a revenue/spend ratio and cannot be labeled campaign ROAS. If the ad source refresh failed, show its actual last-success timestamp instead of calling it live.
