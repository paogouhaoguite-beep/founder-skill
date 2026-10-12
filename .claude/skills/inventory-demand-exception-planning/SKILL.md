---
name: inventory-demand-exception-planning
description: Use when a DTC merchant needs a time-phased inventory exception plan
  when recent sales, seasonal demand or inbound timing disagree.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=inventory-demand-exception-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Inventory Demand Exception Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=inventory-demand-exception-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A time-phased inventory exception plan when recent sales, seasonal demand or inbound timing disagree. Supply daily sales and available days, promo/bulk-order annotations, usable stock/backlog, dated receipts and transfers, lead/review horizons, costs/pack/MOQ and service/cash constraints.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Compute 7-day and 28-day observed velocities with in-stock exposure shown. Remove proven one-off/promotional distortion only from baseline, retaining raw demand. Zero sales during stockout is censored; new/intermittent items may have no reliable rate.
2. Use the higher reliable recent rate as an explicit stress stockout scenario, and selected baseline for quantity sizing; do not mechanically buy at a temporary spike. Seasonal/promo lift needs comparable history or merchant-labeled scenario, not a universal multiplier.
3. Build daily/weekly available balance = prior available + usable arrivals − demand − still-outstanding commitments, defining non-overlap so backlog is not subtracted twice. Upstream/DC stock and downstream stock are separate; an inter-node transfer does not create network stock and cannot arrive before transit.
4. Compare time-phased order alternatives including order/setup cost and holding cost of early units. Evaluate only feasible pack/MOQ/capacity/cash choices, include end-horizon inventory and dates; no untested optimization-code claim.
5. Report expedited gaps separately from normal buy quantities, as a late PO cannot prevent an earlier stockout. Zero-velocity in-stock items go to no-buy/seasonal watch with cost exposure, not infinite-cover ranking.
6. Deliver scenario ledger and exception decisions with selected rate, stockout evidence, receipt dependency and cost. Draft purchase groups only; no vendor messages or financial commitment.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| SKU/node | 7d/28d exposure-rate | Selected baseline/stress | Dated gap | Receipt constraint | Lot alternative/cost | Decision |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
