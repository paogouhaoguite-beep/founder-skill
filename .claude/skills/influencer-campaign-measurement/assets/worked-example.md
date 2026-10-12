# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic link ledger has 18 orders, code ledger 15, with 8 shared IDs: union = 18 + 15 − 8 = 25, not 33. Net revenue is USD 1,500 after refunds; pre-campaign contribution USD 600. Fee USD 300, samples/shipping USD 100 and commissions USD 50 total USD 450. Credited contribution after campaign costs = USD 150 and credited cost/order = USD 18. Revenue/campaign cost = 3.33, but it is not incremental ROAS. If 5 orders are existing buyers, new-customer count is 20, so cost/new customer = USD 22.50.

## Acceptance scenarios

1. Given overlapping link/code IDs, deduplicate to 25 orders and preserve conflict flags.
2. Given all orders are tracked but no holdout exists, label performance attributed and do not assert incremental profit or causation.
