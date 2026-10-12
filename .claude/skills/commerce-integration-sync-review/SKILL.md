---
name: commerce-integration-sync-review
description: Use when a DTC merchant needs an export-based diagnosis of order, stock
  or customer sync discrepancies.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=commerce-integration-sync-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Commerce Integration Sync Review

Built by [ShopChief](https://shopchief.ai/?utm_source=commerce-integration-sync-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An export-based diagnosis of order, stock or customer sync discrepancies. Supply system identities, authoritative field owners, source and destination exports with cutoffs, external-ID mappings, event/attempt logs, connector configuration metadata and redacted failed-job records.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map each object/field to its authoritative system and intended direction. Do not assume the store is always inventory master or that bidirectional sync resolves conflicts. Keep POS location and online allocation distinct.
2. Reconcile records using stable external IDs plus tenant/store/location scope; SKU alone may be ambiguous. Compare snapshots only after aligning known sync lag, timezone and event cutoffs. Separate missing record, duplicate record, value mismatch and unknown coverage.
3. Trace source event ID/version through queue, attempts, destination record and final readback. A successful webhook HTTP response proves receipt only; connector enabled status does not prove downstream processing. Missing delivery logs mean unknown health, not zero failures.
4. For inventory bridge sales, returns, receipts, transfers and reservations since the earlier snapshot. Respect actual available/on-hand definitions; do not repeatedly apply both a sale delta and a later absolute stock snapshot as independent depletion.
5. Prepare replay candidates only after checking whether the destination mutation already happened. Preserve original event/idempotency identity; quarantine out-of-order or conflicting versions and verify owner before any manual overwrite.
6. Deliver a scoped repair plan, field mapping and verification sample. Do not install connectors, expose secrets, re-enable all webhooks, replay or change source-of-truth configuration automatically.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Object/source ID | Field owner | Source cutoff/value | Destination ID/cutoff/value | Trace status | Discrepancy | Safe next action |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
