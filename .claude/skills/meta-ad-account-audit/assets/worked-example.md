# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic Meta export: USD 1,200 spend, 60 credited purchases and USD 3,600 credited revenue. Reported CPA = USD 20 and ROAS = 3.0. Merchant records show 50 unique orders; this discrepancy does not by itself prove ten duplicate Meta events because attribution populations differ. At USD 25 pre-ad contribution/order, the 60-credit scenario leaves USD 300 after ads; the 50-order scenario leaves USD 50. Neither is a verified incremental profit estimate. If a supplied browser/server log shows the same order sent twice without a shared deduplication identifier, record that specific verified configuration fault separately.

## Acceptance scenarios

1. Given Meta 60 and Google 40 credited purchases against 70 merchant orders, do not report 100 acquired orders or calculate blended CPA with 100.
2. Given missing event diagnostics but complete ad spend, return unknown tracking status, computed reported CPA, and the exact evidence needed; do not fail tracking solely because access is absent.
