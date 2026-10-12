---
name: local-delivery-route-and-slot-review
description: Use when a DTC merchant needs a feasible local-delivery route and booking-slot
  plan.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=local-delivery-route-and-slot-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Local Delivery Route And Slot Review

Built by [ShopChief](https://shopchief.ai/?utm_source=local-delivery-route-and-slot-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A feasible local-delivery route and booking-slot plan. Supply depot/stop locations, approved road travel-time matrix, stop service times/windows, vehicle capacity, driver shifts/breaks, load/access constraints, existing commitments and local cutoff/timezone.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Validate that each address is serviceable and belongs to the actual delivery zone. Straight-line distance or a convex hull of coordinates is not a driving-time or service-area guarantee.
2. Build candidate stop sequences using supplied road travel times. For each leg compute arrival, waiting until window opens, service completion and next departure; include depot departure/return, breaks and traffic scenarios.
3. Check capacity through the route, including pickups and unloading access. Reject sequences violating a hard window, driver shift, vehicle/load or qualified safety constraint; do not turn a hard violation into a weighted score.
4. For booking slots subtract existing accepted commitments from evidence-backed capacity. Account for picking/ready time and booking cutoff in the business timezone. A nominal number of drivers is not confirmed slot availability.
5. Compare feasible routes by actual time/cost and customer promise, clearly labeling manual heuristic rather than claiming optimality. Document reserve/slack selected by merchant and the fallback for failed delivery.
6. Deliver conditional route manifest and slot status. No booking acceptance, driver dispatch, customer SMS or change of delivery promise without scoped authorization and latest capacity recheck.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Route/stop | Window | Travel/wait/service | Arrival/departure | Load | Constraint/slack | Slot decision |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
