---
name: dropship-supplier-order-control
description: Use when a DTC merchant needs a supplier-stock and order-routing control
  for dropship goods.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=dropship-supplier-order-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Dropship Supplier Order Control

Built by [ShopChief](https://shopchief.ai/?utm_source=dropship-supplier-order-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A supplier-stock and order-routing control for dropship goods. Supply internal-to-supplier variant mappings, feed completeness/cutoff, supplier acknowledgment and availability, costs/freight/duties responsibility, promised service, current orders/shipments and exception policy.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Resolve supplier SKU/variant to the merchant item without title-only matching. Record feed timestamp and full-versus-delta semantics; a missing row in a partial/delta feed is not proof of zero stock or discontinuation.
2. Compare supplier stock claims with freshness, allocation commitment and service evidence. Supplier on-hand is not a reservation for this merchant; do not promise immediate availability without applicable confirmation.
3. For each order line evaluate candidates on confirmed quantity, actual delivery capability, landed variable cost, return responsibility and product equivalence. Cheapest quoted item alone is insufficient; do not substitute an unapproved supplier/variant.
4. Trace merchant order/line through supplier request, acknowledgment, supplier order ID, shipment and tracking. An accepted request is not shipment; unknown timeout requires lookup before another submission.
5. Calculate contribution with supplier item cost, freight, processing and supported return/fee scenarios. Keep refunds to customer distinct from recovery from supplier; unknown costs stay unknown.
6. Deliver routing proposal and exception owner, using minimum address data only in an authorized supplier handoff. No purchase submission, stock overwrite or customer promise without scope/readback.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Merchant line | Supplier mapping/feed time | Confirmed quantity | All-in cost | Service/return terms | Request/ack/shipment | Action |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
