---
name: inventory-cost-and-valuation-audit
description: Use when a DTC merchant needs an inventory cost-coverage and valuation
  review.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=inventory-cost-and-valuation-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Inventory Cost And Valuation Audit

Built by [ShopChief](https://shopchief.ai/?utm_source=inventory-cost-and-valuation-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An inventory cost-coverage and valuation review. Supply as-of physical quantity by SKU/location/stock state, variant identity, dated receipt cost layers including allocable landed costs, costing policy supplied by finance, currency and existing ledger totals.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Fix as-of cutoff, unit of measure, ownership and cost basis. Distinguish owned stock in transit, reserved stock, consignment and quarantined goods. Avoid counting both parent-product stock and its variants or repeating a SKU in multiple categories.
2. Validate missing, zero and currency-mismatched unit costs separately. An unknown cost remains unknown; present known-value subtotal and uncovered units/SKUs. Retail price times missing-cost quantity is only retail exposure, never the missing cost or replacement value.
3. Where approved cost layers exist, compute FIFO issue cost from earliest eligible layers or the supplied weighted-average policy. Preserve receipt quantities, dated landed-cost allocations and residual rounding so layer totals reconcile. Do not overwrite historical cost with current catalog cost.
4. Compute remaining owned quantity × supported cost for each layer/location. Show units and cost movement bridge from opening through receipts, issues, returns and adjustments. Returns need evidenced original cost and condition; damaged stock needs a separate finance decision.
5. Compare known-cost subtotal and completeness with the accounting ledger on the same policy/cutoff. Explain quantity, scope, valuation-method and timing differences before concluding an error. This working schedule is not an insurance or audited balance-sheet valuation.
6. Deliver cost-gap requests to procurement/finance and a reconciled valuation schedule; no automatic zero fill or revaluation journal.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| SKU | Location/state | Quantity | Cost basis/date | Currency | Known value | Uncosted units | Difference reason |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
