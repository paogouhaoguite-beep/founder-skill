---
name: merchant-month-end-close-pack
description: "Coordinate a merchant close checklist and evidence packet across ledger, inventory, payments and accruals, without silently posting or locking books."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Month End Close Pack

## Close contract
Establish entity, accounting basis, currency, target period/timezone, reporting deadline, responsible preparer/reviewer, materiality policy and authoritative ledger. Inventory, payment and expense systems are supporting sources, not totals to add again to the books. Use exports when connectors are absent and identify missing accounts.

## Dependency-aware checklist
Agree cutoffs for sales, refunds, receipts, inventory movements, payroll, AP and AR. Collect late documents and recurring-entry schedules. Propose journals only with documentary support and reviewer sign-off; estimate labels do not make unsupported numbers acceptable.

Reconcile relevant subledgers and bank/processor balances to control accounts. Account for fees, chargebacks, deposits, transfers, partial settlements and timing without counting gross sales and payouts as two income streams. Inspect report detail when summaries appear inconsistent; do not assume every provider has the same reporting defect.

Review inventory/COGS, accruals, prepayments and customer liabilities under the merchant’s accounting policy. A balanced trial balance is necessary but does not prove correct recognition. Trace material period changes to actual drivers and keep unexplained differences in the exception list. Do not declare a variance “timing” without its expected settlement period and evidence.

Maintain staged statuses: evidence collected, reconciliation completed, adjustment proposed, reviewed, posted if authorized, and period locked only by an authorized operator. A correction after review invalidates affected checks and must be rechecked; do not impose a universal fifth-day deadline or a rigid lock-before-reconciliation rule.

## Deliver
Produce the close calendar, account/control checklist, reconciliation and proposed-journal attachments, flux explanations, unresolved questions and a sign-off record. No accountant distribution, journal posting, account connection or period lock occurs merely because the packet is prepared.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-month-end-close-pack&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
