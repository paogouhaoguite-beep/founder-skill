---
name: product-attribute-schema-audit
description: Reconcile product attribute definitions and values against a typed catalog
  schema. Use for metafields, category attributes and PIM mappings before product
  filters or channel exports fail.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=product-attribute-schema-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Product Attribute Schema Audit

Built by [ShopChief](https://shopchief.ai/?utm_source=product-attribute-schema-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Products with stable IDs/category IDs, attribute definitions (namespace/key/type/owner), current values, approved taxonomy version and source-of-truth mapping by locale/channel. Include controlled vocabulary IDs and the target exporter/importer schema.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Separate categories, free-form product types, options and typed attributes. Map each merchant requirement to the actual owner/type and source. A product-level material value must not overwrite a variant-specific material without evidence.
2. Check definition/value compatibility: scalar versus list, units, allowed values, empty versus unknown and object-reference IDs. Retain labels for humans but resolve controlled references through authoritative IDs; never fabricate a taxonomy or metaobject ID.
3. For category-bound attributes, verify that the product is in the required category and that the value reference belongs to the required vocabulary/type. Match by verified meaning, not a similarly spelled label alone.
4. For each PIM field define direction, locale/scope fallback, transformation and conflict owner. Sync only validated attributes; a failed product remains in a retry queue, and the high-water mark must not permanently skip it.
5. Produce create-definition, fill-missing, type-mismatch, orphaned and conflict queues. Do not delete apparently unused definitions without checking storefront, filters, integrations and historic content.
6. Preview value changes, backup affected attributes and inspect destination readback after authorized application. Treat source timestamps as concurrency guards; stale storefront rendering is not an authoritative write failure.

## Deliverable

Return the typed schema matrix, row-level validation exceptions and scoped migration/sync plan with failed-record reconciliation.

| Product/owner ID | Category | Namespace/key | Expected type | Raw value | Normalized value/reference | Source locale | Conflict | Proposed action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
