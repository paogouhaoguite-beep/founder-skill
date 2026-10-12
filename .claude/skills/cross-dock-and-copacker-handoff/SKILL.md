---
name: cross-dock-and-copacker-handoff
description: Use when a DTC merchant needs a time-and-quantity handoff plan for supplier
  receipts, outsourced packing or direct cross-dock dispatch.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=cross-dock-and-copacker-handoff&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Cross Dock And Copacker Handoff

Built by [ShopChief](https://shopchief.ai/?utm_source=cross-dock-and-copacker-handoff&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A time-and-quantity handoff plan for supplier receipts, outsourced packing or direct cross-dock dispatch. Supply inbound ASN/lot/quantity/ETA, outbound commitments/cutoffs, dock/labor capacity, approved packing BOM and yield, inspection/release rules and ownership/cost terms.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Choose the actual mode: unchanged cross-dock, sorting/deconsolidation, or co-packing transformation. Map input lot and output lot/SKU, ownership and acceptance point rather than treating every transfer as a sale or finished production.
2. Reconcile expected inbound, received, accepted, consumed, scrap and completed outputs. For packing calculate feasible output from BOM and evidenced yield, separating expected yield from actual released output.
3. Lay out inbound arrival, unload, inspection, sorting/packing, staging and outbound departure with shared dock/labor capacity. Goods cannot be promised cross-docked before inspection release or a feasible outbound connection.
4. Identify missing inbound items, late arrivals, packaging shortage and rejected output. Compare hold/store/rebook/partial-shipment options using actual handling/freight and customer consequence; no forced bypass of quality to meet a cutoff.
5. Assign who provides components, owns scrap/rework, verifies lot traceability and pays accessorials under actual agreement. Keep supplier acknowledgment separate from merchant approval of extra cost.
6. Deliver a lot/quantity handoff manifest and exception decisions. No outsourced production release, additional PO, relabeling or shipment booking without authorization.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Inbound lot | Accepted inputs | BOM/yield | Released output | Dock/pack timeline | Outbound commitment | Gap/owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
