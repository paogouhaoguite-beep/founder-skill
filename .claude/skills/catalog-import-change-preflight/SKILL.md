---
name: catalog-import-change-preflight
description: Prepare and reconcile a minimal catalog update file with a reversible
  before/after manifest. Use for bulk price, tag or field edits, imports and migrations
  where blank cells or repeated rows could overwrite data.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=catalog-import-change-preflight&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Catalog Import Change Preflight

Built by [ShopChief](https://shopchief.ai/?utm_source=catalog-import-change-preflight&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Current authoritative export, intended update list keyed by stable ID, target importer and current template, field semantics, currency precision, tax-inclusive basis and tag operations. Preserve a backup and source-row counts.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Select only the entity and fields authorized for change. Validate identity resolution using IDs first; ambiguous handles/titles are blocked. Preserve variants/images grouped under their parent where the importer requires adjacent rows.
2. Define three distinct input states: omitted field means no proposed change, explicit value means set, explicit clear means delete/reset. Verify the actual importer semantics; never assume every blank cell safely skips or every MERGE operation is harmless.
3. For prices, calculate from the agreed base: percentage or amount, rounding rule and floor/ceiling. Keep original price and proposed final price; do not compound a retry on an already adjusted value. Flag compare-at and tax-display effects separately.
4. For tags, implement add/remove/replace as explicit set operations. Adding a tag preserves all other tags; replacement requires the entire intended set. Detect an add/remove contradiction before generating the file.
5. Create the minimum-column import plus change manifest and a small dry-run/sample review. Confirm whether absent IDs create records; use update-existing semantics when creation is outside scope.
6. After authorized import, reconcile importer results and fresh records against the manifest. Classify success, unchanged, conflicted and unknown; retry only proven failures using the same intended final value. A rollback file must explicitly restore original values, not merely omit rows.
7. For SEO metadata backfill, bind product/collection/page/article owner and field explicitly, preserve existing nonempty values under missing-only scope, use approved brand/product facts and log each old/new value. Re-read stored values after an authorized update and separately verify rendered storefront output; a correct Admin value does not guarantee the theme renders it. Treat length as an editorial preview constraint, not a fixed Google ranking limit.

## Deliverable

Deliver a backup reference, import-ready proposal in the actual verified format, row-level change manifest and post-import reconciliation. If the target format is unavailable, produce a normalized proposal, not a falsely import-ready file.

| Entity ID | Field | Before | Operation | After | Validation | Import result | Readback | Rollback value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
