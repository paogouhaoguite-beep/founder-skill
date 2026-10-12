# Synthetic worked example

Input: Five order rows: O1 twice identically; O2 amount 50; O3 amount blank; O4 amount−10 marked refund. Merchant says refunds may be negative.

Quality register: duplicate-key rows 2/5 (one extra duplicate); missing amount 1/5; negative value 1/5 is valid under refund semantics and is not automatically removed. Decision: deduplicate O1 only after identical-record evidence is confirmed, resolve O3 before reporting complete revenue, retain O4 as a refund. Source freshness is unknown without extraction/event dates.

Boundary scenario 1: Order volume doubles during a documented promotion. Treat a baseline anomaly as a review signal, not proof the load is corrupt.
Boundary scenario 2: A report excludes all returned orders. Flag survivorship bias if the question is overall customer/order performance.
