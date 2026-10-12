---
name: customs-document-consistency-review
description: Use when a DTC merchant needs a customs broker handoff and shipment-document
  consistency review.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=customs-document-consistency-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Customs Document Consistency Review

Built by [ShopChief](https://shopchief.ai/?utm_source=customs-document-consistency-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A customs broker handoff and shipment-document consistency review. Supply commercial invoice, packing list, transport document, product composition/use, origin evidence, quantities/weights/currency, stated trade term with named place/version, and broker-approved classification/valuation instructions.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Identify importer/exporter, shipment, destination and responsible broker. Record each document version and actual product identity; do not infer origin from shipping country or supplier address.
2. Cross-check item description, SKU/lot, quantity/UOM, package count, gross/net weight, invoice currency/value and parties across documents. Preserve supported differences such as multiple invoices in one consolidated shipment with an explicit mapping.
3. Prepare classification questions from material, function and composition and attach existing approved codes with jurisdiction/version. Do not choose a tariff code from title alone or label it binding; unresolved classification goes to the broker/qualified authority.
4. Compare valuation components and trade-term responsibilities to supplied current broker instructions, recording included/excluded freight/insurance/assists/royalties as applicable evidence. There is no universal freight inclusion rule and a trade term alone does not determine customs value.
5. Inventory origin/preference, permits/restrictions and screening evidence required by the responsible owner. Missing certificate or an automated possible match requires resolution, not an inferred exemption or cleared-party verdict.
6. Deliver discrepancy questions and a reconciled broker packet. No declaration filing, duty guarantee, undervaluation, origin alteration or clearance promise.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Document/line | Identity/quantity/value | Cross-document match | Classification/origin basis | Unresolved question | Broker owner |
| --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
