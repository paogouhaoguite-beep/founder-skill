---
name: catalog-publication-retirement-control
description: Review channel visibility and safely plan publication, archival or retirement
  of catalog records. Use when products are unexpectedly missing, obsolete drafts
  accumulate or a catalog cleanup is requested.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=catalog-publication-retirement-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Catalog Publication Retirement Control

Built by [ShopChief](https://shopchief.ai/?utm_source=catalog-publication-retirement-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Product ID/status, channel publication state, stock, open orders, subscriptions, URLs, app/metafield dependencies, last change and explicit retirement criteria. Include merchant decisions about sold-out pages and redirects.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Build a state matrix: active/draft/archived is separate from channel publication and sellability. Identify desired visibility per channel; inventory zero alone is not authorization to unpublish.
2. Classify anomalies as unpublished, missing channel access, scheduled/not-yet-live, archived or data unknown. Verify a sample on the actual channel and distinguish cached storefront state from current admin state.
3. Classify a continuing material change, phase-out without replacement, or replacement with a successor. Document which version each customer will receive, remaining inventory, subscriber/dealer notice and hard cutover versus overlap. Do not silently swap subscribers or transfer reviews to a materially different product; prepare truthful opt-in transition copy and support-page/redirect decisions. Recall or safety withdrawal follows the qualified recall owner and approved notice, never routine clearance.
4. For retirement, check open orders, subscriptions, replacement products, incoming stock, backlinks and support records. Preserve purchase history and identifiers; prefer a reversible state change where suitable.
5. For app debris, confirm the app is removed and the specific fields/rendering path are unneeded. A matching namespace alone does not establish that every value is disposable.
6. Prepare exact record IDs, original/desired state, reason and impact. Separate archival from deletion and visibility from redirect changes. Execute only the approved set, then read back and verify the affected surface.

## Deliverable

Deliver publication discrepancies and a reversible retirement proposal with a blocked-dependency queue.

| Product ID | Current state | Channel state | Desired state | Business evidence | Dependency block | Authorized action | Readback |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
