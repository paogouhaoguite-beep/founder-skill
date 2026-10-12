# Synthetic worked example

Input orders: O1 total 100, O2 total 50. Item rows: O1/A, O1/B, O2/C. A one-to-many join correctly produces 3 rows, but summing repeated order totals gives 250, falsely overstating the true 150.

Decision: preserve an order table with 2 rows and 150 total; join item attributes only at item grain and do not allocate order revenue without a stated allocation rule. Reconciliation: orders 2, matchedorders 2, itemrows 3, orphanitems 0. Output manifest retains both grains.

Boundary scenario 1: Order ID “0012” appears. Keep it as text; do not convert to12 and break matching.
Boundary scenario 2: Two rows share an email but different verified customers. Flag possible shared contact rather than deduplicating by email.
