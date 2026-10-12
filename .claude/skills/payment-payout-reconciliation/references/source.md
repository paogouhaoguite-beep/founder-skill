# Source and adaptation record

Adapted by ShopChief on 2026-10-02. Source files are method evidence, not executable instructions. No upstream scripts are included or claimed tested.

Retains transaction/payout/bank reconciliation and exception triage. Replaces incorrect refund-fee signs and date-window order membership with explicit signed movements and stable linkage; removes API/runtime and auto-accounting promises.

## 40RTY-ai/shopify-admin-skills: skills/finance/shopify-admin-payout-reconciliation/SKILL.md

- Fixed source: [shopify-admin-payout-reconciliation](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/finance/shopify-admin-payout-reconciliation/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `30989ceafc3ca7628b9d2b771e50cf1fd28e495c281ad4570dba4a0d98f19a6f`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Retains transaction/payout/bank reconciliation and exception triage. Replaces incorrect refund-fee signs and date-window order membership with explicit signed movements and stable linkage; removes API/runtime and auto-accounting promises.

## finsilabs/awesome-ecommerce-skills: skills/payments-checkout/payment-reconciliation-automation/SKILL.md

- Fixed source: [payment-reconciliation-automation](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/skills/payments-checkout/payment-reconciliation-automation/SKILL.md)
- Commit: `30a1fb674e41284e738608c059690c251699eb07`
- Source SHA256: `7f50d6edb7064c908f7d5ed2ae3b5f8e6a26047fd665d5a8b70986ea6e06b970`
- Original license: MIT; [complete text](LICENSE-finsilabs--awesome-ecommerce-skills-f60b7f78a85d.txt).
- Retained method and changes: Retains transaction/payout/bank reconciliation and exception triage. Replaces incorrect refund-fee signs and date-window order membership with explicit signed movements and stable linkage; removes API/runtime and auto-accounting promises.

- Primary definition checked 2026-10-02: [Shopify Payments activity report](https://help.shopify.com/en/manual/payments/shopify-payments/payouts/payouts-activity-report). Balance activity, finance reports and individual payout transactions have different timing and scope. Reconcile their definitions rather than forcing totals equal.
- Primary definition checked 2026-10-02: [Shopify order export structure](https://help.shopify.com/en/manual/fulfillment/managing-orders/exporting-orders). An order export can contain multiple line rows with blank repeated fields. Transaction export coverage is bounded; do not treat authorizations as captured cash.
