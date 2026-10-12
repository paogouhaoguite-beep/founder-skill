---
name: promotion-incremental-economics-review
description: Use when a DTC merchant needs a promotion or flash-sale economic and
  readiness review.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=promotion-incremental-economics-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Promotion Incremental Economics Review

Built by [ShopChief](https://shopchief.ai/?utm_source=promotion-incremental-economics-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A promotion or flash-sale economic and readiness review. Supply baseline units, promotion units/prices, variable costs/fees, trade or campaign spend, before/after demand, overlapping channels, stock/capacity and approved offer start/end/timezone.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define baseline counterfactual and evidence, including seasonality, distribution, stockouts and overlapping offers. Observed uplift over last week is not necessarily incremental demand.
2. Calculate promotion contribution on actual promoted volume/prices/costs and compare with baseline contribution. Subtract incremental spend once; discount loss already reflected in net price must not be deducted again.
3. Show cannibalization, post-promotion pull-forward and halo as separate supported estimates/scenarios. Do not assume all apparent lift persists or double-count lost revenue and lost contribution.
4. For trade spend reconcile funded allowances, retailer deductions and approved claims against actual event/SKU/period; planned spend, accrued spend and paid cash are separate. ROI denominator is stated incremental investment, with zero-investment ROI undefined.
5. Check offer terms, price rounding, inventory allocations, checkout capacity, code stacking, timezone/end state and rollback. Use staged functional review; no fake urgency, unsupported sales benchmarks or untested automatic restart.
6. Deliver economic bridge and go/hold conditions. Launching offers, spend or messages requires exact scope and verified setup; no automatic restock or discount changes.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Event/SKU | Baseline/promo units | Net unit price/cost | Contribution delta | Incremental spend | Pull-forward scenario | Readiness decision |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
