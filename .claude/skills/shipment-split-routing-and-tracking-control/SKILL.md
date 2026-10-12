---
name: shipment-split-routing-and-tracking-control
description: Use when a DTC merchant needs a feasible shipment allocation and tracking
  change set.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=shipment-split-routing-and-tracking-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Shipment Split Routing And Tracking Control

Built by [ShopChief](https://shopchief.ai/?utm_source=shipment-split-routing-and-tracking-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A feasible shipment allocation and tracking change set. Supply unfulfilled line IDs and quantities, order reservations, location eligible inventory/capabilities, ship promises, carrier/package tracking records, warehouse release states and proposed notification choice.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Build one shared inventory pool across all candidate orders and locations, honoring existing reservations and protected commitments. Do not compare each order independently to the same stock and allocate it repeatedly.
2. Allocate by merchant priority and service promise with a running stock ledger. For each line, shipped+cancelled+allocated+unallocated must reconcile to ordered quantity. Sum quantities across every proposed split group before testing the remaining line balance.
3. Compare one-shipment wait versus split-now/later with incremental freight, handling, customer promise and location capability. A plan can identify alternatives without claiming globally optimal routing.
4. For a location move verify destination eligible stock, shipping/service capability, hold status and warehouse handoff before requesting reassignment. Do not move in-progress work without warehouse acknowledgement.
5. Map each package to exact fulfillment and line quantities; check tracking carrier/format and preserve multiple tracking numbers. On Woo treat tracking fields as extension-specific; do not invent universal metadata keys.
6. Create/update only authorized fulfillment/tracking records with explicit customer-notification choice and post-write readback. A fulfillment record or label is not carrier acceptance/delivery; uncertain outcomes need duplicate lookup before retries.
7. Compare single-node versus split fulfillment with actual stock, pick/pack capacity, promised service and total shipment cost; proximity alone does not establish fastest delivery. For pickup, preserve reservation, ready-for-pickup and verified collection as separate events, with pickup expiry and return-to-stock only under supplied policy. Keep backordered lines visible and communicate separate parcel contents/ETAs through authorized drafts; a location outage requires revalidation of only unfulfilled lines.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Order/line | Remaining qty | Allocated location | Ship-now qty | Backlog qty | Package/tracking | Incremental cost | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
