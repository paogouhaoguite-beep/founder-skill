---
name: payment-payout-reconciliation
description: Use when a DTC merchant needs a reconciliation of a named payout to its
  settlement transactions and bank deposit.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=payment-payout-reconciliation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Payment Payout Reconciliation

Built by [ShopChief](https://shopchief.ai/?utm_source=payment-payout-reconciliation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A reconciliation of a named payout to its settlement transactions and bank deposit. Supply payout ID, currency, status, payout transaction export with stable transaction IDs and signed gross/fee/net, processor charge/refund IDs, order payment ledger, bank deposit ID and amount, report dates and timezone.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Inventory report coverage and settlement currency. Preserve balance-transaction ID, payment/charge ID, order ID and payout ID separately. Match payout membership from its own transaction detail, never from nearby order dates; date windows only locate evidence.
2. Normalize each row to signed balance movements: positive increases funds available to merchant, negative decreases. Define net = signed gross + signed fee component. If provider fee is a positive charge magnitude, convert it to a negative component once. A fee reversal is positive only when evidence says it was reversed. Prefer reported net and flag inconsistent gross/fee decomposition.
3. Deduplicate identical transaction IDs; conflicting duplicates block totals. Include captured charges, refunds, disputes, reserves, adjustments and fee reversals as documented. Do not count the payout transfer itself again among the transactions funding that payout.
4. Sum linked transaction net by currency and compare with payout amount. Separately match payout transfer to bank deposit, documenting bank fees, FX, split deposits and timing. Use unexplained difference, not overpaid/underpaid, until the cause is proven.
5. Reconcile order payment events by their processor references, including partial captures and multiple tenders. Keep missing order linkage as unknown: a correctly reconciled payout can contain an unmatched order. A paid order does not establish settlement membership.
6. Produce three controls: settlement-to-payout, payout-to-bank and processor-to-order linkage. Put each unresolved ID, required document and owner in the exception queue; do not auto-post a balancing journal.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Payout ID | Transaction ID | Order linkage | Signed gross | Signed fee | Net | Currency | Exception |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
