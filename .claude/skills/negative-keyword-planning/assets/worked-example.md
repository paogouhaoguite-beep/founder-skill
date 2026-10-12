# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

A store sells travel pouches and free shipping on orders above USD 60. Observed query “free sewing pattern for travel pouch” is irrelevant; “travel pouch free shipping” is valuable. A broad negative “free” blocks both. An exact negative [free sewing pattern for travel pouch] blocks the observed unwanted query while preserving the shipping query. It will not necessarily catch spelling variants. If the store also sells sewing patterns in another campaign, even “sewing pattern” requires campaign-level rather than account-wide consideration.

## Acceptance scenarios

1. Given “free shipping” among protected queries, reject the blanket negative “free” and show a narrower candidate.
2. Given a shared list attached to three campaigns and one relevant sewing-pattern product line, enumerate collateral scope before any import; do not silently apply account-wide.
