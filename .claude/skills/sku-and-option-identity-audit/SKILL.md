---
name: sku-and-option-identity-audit
description: Detect conflicting SKU/barcode identities and inconsistent variant options
  before imports or channel sync. Produce a reviewed normalization map without merging
  products by guesswork.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=sku-and-option-identity-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Sku And Option Identity Audit

Built by [ShopChief](https://shopchief.ai/?utm_source=sku-and-option-identity-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Variant IDs, parent products, SKUs/barcodes as text, ordered option names/values, bundle status, archived state and inventory linkage. Merchant-approved naming dictionary and allowed option combinations; never infer size equivalence across brands.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Keep a raw identity column and a comparison key. Trim surrounding whitespace for comparison only; preserve case and leading zeroes in identifiers unless the merchant confirms the system treats them equivalently.
2. Group nonblank SKU and barcode keys; identify distinct variant IDs sharing a key. Distinguish repeated export rows, intentionally shared fulfillment identities and actual collisions. Blank IDs are incomplete data, not one giant duplicate group.
3. Within each product, normalize option labels through an explicit dictionary. Compute proposed tuples and detect collisions: two variants becoming the same tuple must be resolved before writes. Preserve option order, localization and inventory references.
4. For proposed variant matrices, enumerate only permitted combinations. Calculate candidate count from combinations then remove prohibited/unavailable combinations explicitly; missing combinations are not automatically missing products.
5. Return a row-level before/after map and exceptions. Require a stable ID for changes; inspect inventory, media, price and channel consequences before creating/deleting variants. Re-query or re-export to confirm uniqueness after an authorized change.

## Deliverable

Deliver the duplicate groups, safe normalization rows, blocked collisions and an explicit permitted-combination matrix.

| Variant ID | Raw identity | Comparison key | Collision group | Raw options | Proposed tuple | Action | Unresolved dependency |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
