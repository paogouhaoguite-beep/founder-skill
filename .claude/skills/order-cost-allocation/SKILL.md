---
name: order-cost-allocation
description: Use when a DTC merchant needs an order-level cost allocation schedule.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=order-cost-allocation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Order Cost Allocation

Built by [ShopChief](https://shopchief.ai/?utm_source=order-cost-allocation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An order-level cost allocation schedule. Supply net merchandise sales after discounts/refunds excluding collected tax, customer shipping revenue, dated COGS, actual label/pick-pack/processor costs, marketing and overhead pools with period/currency and attribution limitations.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Choose order or line grain and ledger period; reconcile revenue and each cost pool before joining. Attach actual direct costs by stable IDs; avoid duplicating an order-level label cost on every line.
2. Separate variable fulfillment/fees, marketing and fixed overhead. Calculate contribution before allocated marketing/overhead so allocation assumptions are visible. Do not call contribution net profit.
3. For a shared pool choose a causal driver documented by merchant: shipment weight for freight, picks for pick fees, or an explicit revenue/order allocation for shared spend. Allocation = pool×row driver/total eligible driver; reconcile sum to pool and assign rounding residual explicitly.
4. Keep unattributed marketing spend in its own bucket unless merchant approves a clearly labeled allocation. Attributed channel sales are not incremental causation; zero driver prevents allocation.
5. Compare equal-order versus revenue-weight allocation as sensitivity. Distinguish orders with negative variable contribution from those negative only after discretionary fixed-cost allocation.
6. Report pool control totals, missing direct cost evidence and the sensitivity of ranking. Proposed price or channel decisions need merchant review, not automatic changes.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Order | Net sales | COGS | Direct variable cost | Contribution | Marketing allocation | Overhead allocation | Allocated result |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
