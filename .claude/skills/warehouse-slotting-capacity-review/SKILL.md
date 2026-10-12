---
name: warehouse-slotting-capacity-review
description: Use when a DTC merchant needs a sku-to-bin slotting and space-capacity
  proposal.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=warehouse-slotting-capacity-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Warehouse Slotting Capacity Review

Built by [ShopChief](https://shopchief.ai/?utm_source=warehouse-slotting-capacity-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A SKU-to-bin slotting and space-capacity proposal. Supply pick counts/order affinity, SKU dimensions/weight/cube, bin capacities/access restrictions, replenishment data and actual travel distances, plus approved facility safety constraints.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Use observed picks, cube-per-pick and co-pick evidence to rank candidate moves; do not assume 20% SKUs make 80% picks. Preserve temperature, hazardous separation, ergonomics and load-rating gates.
2. Check each SKU fits usable bin dimensions, weight and reserve/replenishment capacity. Fast-moving bulky stock may need more replenishment and staging, not just the closest slot.
3. Estimate travel change from actual path distances×pick frequency, and include replenishment trips, congestion and one-time relocation work. Savings are a modeled scenario until measured.
4. Compare storage/pick/pack/receiving/staging areas against observed peak occupancy and throughput. No generic aisle/rack dimensions substitute for qualified site design and approved safety rules.
5. Deliver before/after slot map, capacity exceptions and phased pilot with baseline, measurement window and rollback. No rack changes or physical move instructions beyond reviewed authorized plan.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| SKU | Picks | Cube/weight | Current/candidate bin | Fit constraints | Travel delta | Replenishment effect | Pilot decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
