---
name: store-resource-retirement-review
description: Use when a DTC merchant needs a dependency-aware review of old draft
  orders or apparently unused store files.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=store-resource-retirement-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Store Resource Retirement Review

Built by [ShopChief](https://shopchief.ai/?utm_source=store-resource-retirement-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A dependency-aware review of old draft orders or apparently unused store files. Supply resource IDs/URLs, ages/status, current references across catalog/content/theme/metafields/apps, draft payment/invoice/reservation activity, business owner and retention instructions.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Fix scope and snapshot time; use age only to select candidates. Open draft age does not prove abandonment, and unreferenced in products/pages alone does not prove a file is unused.
2. For drafts check active customer quote/invoice, pending payment, stock reservation, company approval and staff owner. Record expiry/retention policy and latest interaction separately from creation date.
3. For files normalize identities without stripping significant version parameters; inspect theme/sections, metaobjects/metafields, rich content, apps, emails and external embeds as available. Classify confirmed referenced, no reference within audited surfaces, and coverage incomplete.
4. For each candidate document consequence, dependency coverage, recoverable backup/export and owner decision. Prefer retirement/archive/unpublication where supported and appropriate before irreversible deletion.
5. Prepare exact-ID change preview with current state, expected impact and verification/restore path. Re-read references and draft activity immediately before any authorized action; changed state invalidates the preview.
6. Deliver a candidate register, exclusions and unresolved surfaces. Never bulk-delete solely from old age or an incomplete orphan scan.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Resource ID | Age/status | References/activity | Coverage gaps | Retention/owner | Proposed disposition | Restore evidence |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
