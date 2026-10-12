# Synthetic worked example

Synthetic as-of Oct 4 12:00: O1 ready Oct 2 12:00, promised ship Oct 3 12:00, unshipped → **24 h past promise**,48 h ready age. P2 label created Oct 1 but no acceptance → awaiting handoff evidence, not 3-day transit. P3 accepted Oct 1 12:00 delivered Oct 3 12:00 → **48 h observed transit**. Delivered sample n1; P2 remains open and is not included in that average.

| Record | Status | Action |
|---|---|---|
| O1 |24 h late to ship|warehouse check|
| P2 |acceptance unknown|obtain carrier scan|
| P3 |48 h delivered transit|retain measured row|

## Boundary case 1

Order note edited yesterday but carrier scan stale 5 days. Use carrier event age 5 days; order update does not reset parcel staleness.

## Boundary case 2

Only first 25 of 100 overdue orders were exported. Report sample 25 and unknown complete total until full export; do not call 25 all overdue.
