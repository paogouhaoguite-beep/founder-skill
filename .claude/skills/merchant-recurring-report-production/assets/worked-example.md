# Synthetic worked example

Synthetic definition sales-v1: USD net merchandise sales by store, order-completion date, full Monday–Sunday UTC, refunds in period subtracted; excludes tax/shipping. Current A 1000 / B 500/unallocated 100, prior A 800 / B 400/unallocated 0. Current source complete; payment processor separately shows 1500 settled and is not added.

Finished report: **Net merchandise sales USD 1600, up USD 400 (33.3%) from USD 1200.** Store A:1000 vs 800 (+25%); B:500 vs 400 (+25%); unallocated 100 needs store mapping review. Store subtotals 1500 plus unallocated 100 reconcile to 1600. No attribution to a campaign is established.
Workbook layout: Summary with these totals/comparison; Stores with A/B/unallocated; Definitions with sales-v1; Sources with dated export references. HTML filter A must show 1000/current and 800/prior; all-stores returns 1600/1200. Run record: sales-v1, period Sep 21–27, extraction Sep 28, status complete-data/draft-output; next requested period Sep 28–Oct 4. No scheduler or generated file is claimed by this fixture.

Boundary 1: B export fails → show B missing and partial total 1100, not B=0 or complete 1600.
Boundary 2: prior total 0 → absolute difference shown, percentage growth undefined; rerun same period must not add a second history point.
