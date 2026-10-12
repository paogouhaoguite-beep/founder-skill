---
name: packaging-label-proof-review
description: Use when a DTC merchant needs a packaging artwork proof against an approved
  specification.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=packaging-label-proof-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Packaging Label Proof Review

Built by [ShopChief](https://shopchief.ai/?utm_source=packaging-label-proof-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A packaging artwork proof against an approved specification. Supply final artwork panels at actual dimensions, SKU/formula/BOM version, approved legal copy and target-market requirements, barcode master data, lot/date rules and print proof.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Inventory all panels and associate each text block with its approved specification/version: identity, quantity, ingredients/materials, instructions, warnings, claims, responsible business and traceability fields where applicable.
2. Compare exact spelling, units, decimal placement, allergen/ingredient or material wording and translation to approved source. Missing source is a review gap, not permission to invent required text.
3. Measure typography, placement and legibility against supplied applicable requirements at real print scale. Do not apply a universal food-label font or panel rule to cosmetics, textiles or other products.
4. Validate barcode data/type and check digit where method is known; match it to correct variant master. Passing arithmetic is not barcode print verification. Request actual scan/print-quality evidence including quiet zones per relevant standard.
5. Check batch/date placeholders and production variable fields, artwork revision and vendor proof. Compare digital PDP packaging image with approved final artwork so old formula claims do not persist.
6. Return panel-by-panel redlines, blocking factual mismatches, unresolved regulatory approvals and print-release checklist. Do not approve manufacturing or invent certifications.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Panel/field | Artwork value | Approved value/version | Mismatch | Evidence | Owner | Release state |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
