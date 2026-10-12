---
name: shipment-load-feasibility-review
description: Use when a DTC merchant needs a packing and load feasibility review before
  booking inbound stock or local delivery.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=shipment-load-feasibility-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Shipment Load Feasibility Review

Built by [ShopChief](https://shopchief.ai/?utm_source=shipment-load-feasibility-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A packing and load feasibility review before booking inbound stock or local delivery. Supply actual carton/pallet dimensions and gross weights, allowed orientations/stacking, container/vehicle door and internal dimensions, payload/axle/floor limits, tare, destination sequence and qualified securing rules.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Normalize dimensions/weight units and actual equipment specifications; do not use generic container/vehicle figures as certified limits. Include pallets, dunnage and packing weight in payload.
2. For homogeneous cartons test allowed rectangular layer orientations with floor(length/carton length) × floor(width/carton width), then height and payload constraints. State this is a feasible block arrangement, not global 3D optimization; forbid overhang unless explicitly permitted.
3. For mixed loads record a coordinate/zone or layer plan and check physical overlap, support, stack strength, door clearance, temperature/incompatibility and unload access. Volume and total weight alone cannot prove fit or safe loading.
4. Check shipment/destination grouping and loading order so early stops can unload without moving prohibited cargo. Verify floor/axle/center-of-gravity and restraint requirements with the qualified operator, leaving unverified safety constraints unresolved.
5. Compare feasible equipment counts/costs and utilization using actual loaded volume/weight and usable capacities, including unfilled space caused by constraints. Never declare a load safe from a simple average front/rear weight split.
6. Deliver packing manifest and conditional booking recommendation for operator signoff. No load dispatch, dangerous-goods decision or physical securing instruction beyond supplied qualified rules.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Load/pallet | Carton orientation/layers | Units/gross weight | Cube | Door/stack/route limits | Unverified safety checks | Disposition |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
