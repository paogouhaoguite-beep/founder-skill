# Synthetic checkout
Cart merchandise USD 80, discount USD 8, shipping USD 6, tax USD 5.40 gives USD 83.40. The payment screen shows USD 89.40 because shipping appears twice. Record exact inputs and total mismatch; do not complete payment to demonstrate it.

## Acceptance scenarios
1. A postcode yields no delivery option. Distinguish a supported-region configuration defect from an intentionally excluded market using shipping rules.
2. Order submission times out. Check whether an order already exists before any retry; no duplicate charge attempt.
