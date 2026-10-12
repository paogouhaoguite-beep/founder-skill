---
name: catalog-image-alt-text-review
description: Use when a DTC merchant needs a review and proposed backfill of catalog
  image text alternatives.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=catalog-image-alt-text-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Catalog Image Alt Text Review

Built by [ShopChief](https://shopchief.ai/?utm_source=catalog-image-alt-text-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A review and proposed backfill of catalog image text alternatives. Supply image IDs and visible images, the pages/contexts where each is used, existing alt values, approved product facts and the requested overwrite policy; no API access is required for a review table.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Inventory actual image identity and every known use context; distinguish missing alt attribute, intentionally empty decorative alt and nonempty text. Missing information is not permission to overwrite existing text.
2. Inspect the image before describing it. Use only visible details and confirmed product facts; do not infer hidden materials, certification, medical benefit or exact dimensions from appearance.
3. Choose text according to purpose: informative product view, linked control/function, diagram or decorative image. Describe meaningful differences between variant/detail shots without keyword stuffing or redundant “image of” phrasing; complex diagrams may need adjacent text.
4. Check shared-file reuse: one centrally stored alt value may appear in unrelated page contexts. If a proposed value would misdescribe another use, flag context-specific rendering instead of globally overwriting it.
5. Prepare exact-ID before/proposed/reason table, preserving existing nonempty values unless rewriting was requested. Native UI/export is acceptable; verify actual API/schema and permissions before any optional bulk write.
6. For authorized changes re-read current values, apply only approved IDs, preserve a rollback snapshot and verify rendered alt in affected contexts. A stored value alone does not prove template output or accessibility compliance.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Image ID/context | Observed image | Existing alt state | Proposed text | Evidence | Shared-use conflict | Write/readback status |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
