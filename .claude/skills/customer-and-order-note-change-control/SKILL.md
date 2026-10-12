---
name: customer-and-order-note-change-control
description: Preview and reconcile scoped notes and tags on customer or order records
  while preserving existing content. Use for operational annotations, not automated
  risk judgments or customer messaging.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=customer-and-order-note-change-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Customer And Order Note Change Control

Built by [ShopChief](https://shopchief.ai/?utm_source=customer-and-order-note-change-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Stable customer/order IDs, existing notes/tags, exact selection rule, approved annotation text, append/replace operation, visibility type and timestamp. Include original values and fields used by automations.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Evaluate the selection rule against fresh records and emit the exact IDs/count before modification. Merchant-selected order-value thresholds must use the declared currency and status.
2. Distinguish internal note, customer-visible note and email notification. Unknown visibility is a blocking field; never turn an internal annotation into a customer communication.
3. For append, preserve prior text and attach a deduplication marker/date or equivalent record of the intended annotation. For tags, calculate explicit add/remove sets. Replace requires the entire desired content and explicit scope.
4. Check whether tags trigger fulfillment, risk, CRM or marketing automations; preview the downstream effect. A label based on a review queue must not imply confirmed fraud.
5. Apply only approved records with concurrency checks, then reconcile before/after and actual outcomes. Idempotent retry means the note or tag appears once, not once per attempted request.

## Deliverable

Deliver a complete annotation preview, excluded records and a per-record execution/readback ledger when execution is authorized.

| Record ID/type | Selection evidence | Before | Intended note/tag | Visibility | Downstream effect | Result | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
