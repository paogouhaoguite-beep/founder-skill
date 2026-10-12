# Worked example

All names, inputs and results below are synthetic.

Input: Three US shopping campaigns sell the same SKUs with the same goal; one UK campaign has GBP pricing and UK stock. Expected map investigates overlap among the US campaigns but preserves the UK market boundary. With a $100/day test budget and $40/day reserved for proven demand, new tests have at most $60/day. Do not merge markets merely to reduce campaign count.

## Acceptance scenarios

1. Given two campaigns share names but target disjoint stock or markets, do not call them duplicates.

2. Given purchase events are duplicated across client/server emitters, resolve signal ownership before using those counts to redesign bidding.
