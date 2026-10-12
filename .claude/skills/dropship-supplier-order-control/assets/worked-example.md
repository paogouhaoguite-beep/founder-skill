# Synthetic worked example

Synthetic SKU A maps to supplier S1/A-blue-M. S1 delta feed contains no A row: stock **unknown/unchanged under feed semantics**, not 0. S2 quotes item 12+freight 6, S3 quotes item 14+freight 2; same confirmed service gives costs 18 versus 16. Selling price 30 and other variable fee 1 gives contribution 11 versus 13. S3 is cheaper all-in despite higher item price, pending actual allocation. RequestR 1 timeout with supplier order P8 found: retain P8, do not submit again.

## Boundary case 1

Supplier says “blue” but size is unmapped. Block route until exact variant identity is resolved.

## Boundary case 2

Customer refund 30 succeeds but supplier recovery 16 is pending. Report cash outflow 30 and contingent recovery 16, not net refund 14 as completed.
