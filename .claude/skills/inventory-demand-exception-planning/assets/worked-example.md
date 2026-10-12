# Synthetic worked example

Synthetic SKU X sells 28 in 7 in-stock days (4/day) and 56 in 28 (2/day); merchant confirms short campaign caused the spike. Available 20, confirmed receipt 10 at start day 8. Stress 4/day exhausts afterday 5, causing 8 units unmet ondays 6–7; baseline 2/day leaves 6 beforeday 8 receipt, so no early gap. Report stress expedite need separately; do not silently size a long buy at 4/day.

Two-period deterministic demand 10/10; order fee 5 each, holding 1 per unit for one period, purchase cost equal. Two orders cost 10 setup vs one 20-unit order cost 5 setup+10 holding=15: two orders cheaper by 5 if both feasible. This is a two-option comparison, not a global optimization guarantee.

## Boundary case 1

Last 7 days had 3 stockout days and only 4 selling days with 8 sales. Observed available-day rate 2/day;7-day calendar rate 1.14 is suppressed, not lower proven demand.

## Boundary case 2

DC has 100 units but store needs 20 tomorrow and transfer takes 3 days. Network surplus cannot meet tomorrow; show lead-time gap and no false availability.
