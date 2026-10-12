---
name: shipment-exception-claim-preparation
description: Use when a DTC merchant needs a delayed, lost, damaged or short shipment
  evidence and response file.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=shipment-exception-claim-preparation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Shipment Exception Claim Preparation

Built by [ShopChief](https://shopchief.ai/?utm_source=shipment-exception-claim-preparation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A delayed, lost, damaged or short shipment evidence and response file. Supply shipment/package IDs, BOL or manifest, tracking event history with timestamps/source, order promises, POD, photos/inspection, item quantities/values, carrier contract/claim instructions and authorized customer remedies.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Reconstruct an event timeline with source and timezone. Separate label creation, carrier acceptance, scans, estimated delivery and confirmed POD; a stale scan is an evidence gap, not proof of loss. Detect one missing parcel within a multi-parcel order.
2. Classify the observed exception and affected units: delayed, shortage, damage, wrong destination, failed delivery or unknown. Compare condition/quantity at dispatch and receipt, retaining packaging and evidence when applicable under supplied instructions.
3. Build options with actual costs and promised timing: trace request, reroute, replacement, customer resolution or hold for evidence. Separate original goods cost, incremental replacement cost and potential claim recovery; unapproved recovery is not guaranteed cash.
4. Extract claim eligibility, deadline, required forms, valuation basis and exclusions from the actual contract/current carrier guidance. Record ambiguous legal applicability for a qualified owner; never assume a single global claim period or reimburse retail value by default.
5. Draft a factual claim packet and customer update with evidence references, requested remedy and next checkpoint. Avoid saying delivered or refunded without evidence; minimize address and customer PII outside authorized channels.
6. Link carrier case, merchant action and customer remedy separately. Do not double replace/refund after a delayed original arrives; reconcile actual outcomes. Submitting a claim or message, booking rescue transport and issuing compensation require their scope.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Shipment/parcel | Observed exception | Evidence timeline | Affected units/value | Contract deadline source | Proposed remedy/cost | Owner/status |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
