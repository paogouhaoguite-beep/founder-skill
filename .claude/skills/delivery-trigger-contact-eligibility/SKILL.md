---
name: delivery-trigger-contact-eligibility
description: Build a delivery-event-based survey eligibility file with explicit time
  windows, split-shipment completion, previous-contact suppression and channel permission
  checks.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=delivery-trigger-contact-eligibility&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Delivery Trigger Contact Eligibility

Built by [ShopChief](https://shopchief.ai/?utm_source=delivery-trigger-contact-eligibility&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Supply as-of timestamp/timezone, merchant event and inclusive min/max elapsed time, per-package delivered/accepted/fulfilled timestamps, remaining items, customer/contact ID, channel permission, campaign send/history IDs, cooldown and refund/cancellation policy. Do not presume a universal 7–14-day window.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define exact trigger event and window. For delivery-trigger surveys use evidenced delivery, not order updatedAt or first fulfillment creation. For split orders choose explicit item-specific or all-required-items-delivered policy. Missing delivery remains unknown unless merchant approves a separately labeled proxy cohort.
2. Exclude future/inverted timestamps and duplicate carrier events. Compute elapsed time consistently against as-of and apply inclusive/exclusive bounds as declared. Review refunded, cancelled or complaint cases under merchant survey purpose; do not erase dissatisfied customers simply to improve results.
3. Resolve recipient identity, then join campaign contact history and cooldown. A previous export is not proof of sending, but reserve/queued/sent states may suppress duplicates according to the declared policy. Missing history prevents asserting never contacted.
4. Apply channel-specific permission and suppression after event qualification; guest checkout with verified contact can be eligible. Marketing permission is not inferred from paid order, and one channel permission does not authorize another.
5. Produce eligible/excluded/unknown rows with reason, trigger timestamp, history source and stable dedup key. Export only authorized minimum contact fields. Sending or uploading is a separate action; check fresh suppression immediately before an authorized send.

## Deliverable

Deliver a segment definition, row-level eligibility ledger and requested minimal contact export with counts that reconcile to the input.

| Recipient reference | Order/package | Trigger time | Elapsed | Contact history | Channel permission | Eligibility/reason | Dedup key |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
