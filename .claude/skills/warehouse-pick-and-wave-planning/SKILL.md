---
name: warehouse-pick-and-wave-planning
description: Use when a DTC merchant needs a feasible warehouse pick/wave plan.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=warehouse-pick-and-wave-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Warehouse Pick And Wave Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=warehouse-pick-and-wave-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A feasible warehouse pick/wave plan. Supply released order lines, bin locations, SKU quantities/weights, picker/cart/zone capacity, measured travel/service times, carrier cutoffs, packing throughput and restricted handling rules.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Validate stock release, holds, bin identity and remaining order quantities. Group compatible orders by cutoff/zone/product handling while preserving item-to-order tote identity.
2. Estimate each batch pick+travel time from measured route segments; compare candidate routes rather than claiming exact shortest path. Use real aisle access and directional restrictions; no straight-line paths through racks.
3. Limit batch by cart/tote weight/volume/order-separation and zone labor capacity. Total wave line load must fit picking plus packing and staging before carrier cutoff; optimize bottleneck, not picker speed alone.
4. Create wave start, picker/zone assignment, SKU/bin sequence and downstream handoff. Keep rush insertion and replenishment conflicts visible; protect already released waves unless scoped override.
5. Reconcile picked units and completed order lines; short pick returns to exception queue. Labels/fulfilled status do not replace scan/packing/hand-off evidence. Deliver plan, not an executed WMS release.
6. Before releasing a pick wave check authorized paid/approved order eligibility, actual carrier cutoff, packing/label capacity and required inspection. Prioritize by merchant-approved promise/age rules rather than arbitrary VIP scores. Record picked, packed, handed-to-carrier and exceptions independently; do not mark shipment complete at label generation.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Wave/batch | Orders/totes | Bin sequence | Pick/travel minutes | Pack/stage minutes | Cutoff | Capacity exception |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
