---
name: catalog-collection-and-vendor-hygiene
description: Reconcile collection membership and supplier/vendor labels without breaking
  automated merchandising rules. Use after imports or supplier-name consolidation.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=catalog-collection-and-vendor-hygiene&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Catalog Collection And Vendor Hygiene

Built by [ShopChief](https://shopchief.ai/?utm_source=catalog-collection-and-vendor-hygiene&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Products, stable vendor IDs/labels, collections with manual/automatic rule definitions, membership exports and merchant-approved canonical vendor mapping. Capture status and channel scope.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Normalize vendor comparison keys for review while preserving raw labels. Group likely aliases using merchant evidence such as legal entity or supplier account, not spelling similarity alone.
2. For manual collections, compare intended product-ID sets with actual membership; calculate missing and unexpected IDs. For automatic collections, evaluate the actual rule predicate, including ALL versus ANY and stock/price/type/tag conditions.
3. Simulate vendor/tag changes through dependent collection rules before applying. A vendor merge can remove or add products from rule-based collections even if the catalog edit itself looks harmless.
4. Identify products in no relevant selling collection, but distinguish intentional direct-link, unpublished and excluded products. Do not force all products into arbitrary categories.
5. Return a canonical-label proposal and before/after membership diff; apply only approved mappings and verify rule results on affected collections.

## Deliverable

Deliver alias decisions and membership diffs, including rule dependencies that must change together.

| Product ID | Vendor before/after | Collection | Manual/rule | Expected membership | Actual membership | Change consequence | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
