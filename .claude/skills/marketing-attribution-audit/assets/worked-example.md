# Synthetic conflicting reports
Store has 100 eligible paid orders. Ads A claims 70 conversions; Ads B claims 60; GA4 matches 80 distinct transaction IDs. These are not 210 orders. Windows differ and 20 ledger IDs lack GA4 records. Report each count and investigate known joins; do not split the 100 into 70+30 or label all unmatched orders organic.

## Acceptance scenarios
1. Spend uses interaction date but orders use conversion date. Align the reporting basis or present the mismatch explicitly before calculating ROAS.
2. Only campaign totals exist. Deliver a definition audit and aggregate comparison, not invented multi-touch paths or causal credit.
