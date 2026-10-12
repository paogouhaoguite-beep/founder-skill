---
name: fulfillment-backlog-and-tracking-review
description: Use when a DTC merchant needs a fulfillment backlog and parcel-delay
  report.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=fulfillment-backlog-and-tracking-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Fulfillment Backlog And Tracking Review

Built by [ShopChief](https://shopchief.ai/?utm_source=fulfillment-backlog-and-tracking-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A fulfillment backlog and parcel-delay report. Supply order/line remaining quantity, release and promised-ship time, holds, fulfillment/package IDs, carrier acceptance/last-scan/delivery evidence, service/lane and merchant SLA calendar with an as-of timestamp.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Normalize paid, on-hold, partially fulfilled and unfulfilled states against actual remaining line quantities. Keep counts of distinct orders, fulfillment jobs and parcels separate; document pagination and capped lists.
2. Calculate age from the declared clock: order age, ready-to-ship delay and hold duration are separate. Compare with customer promise or merchant-specific threshold; no universal day limit.
3. For shipped parcels use last carrier event, not order updatedAt or tracking-number existence. Label created is not carrier acceptance; fulfillment createdAt is not necessarily transit start.
4. Compute transit duration acceptance→delivery for evidenced delivered parcels by service/lane. Show undelivered parcel count and age distribution separately so excluding slow open parcels does not imply better service.
5. Prioritize missed promise, stuck handoff, missing tracking evidence and carrier exception with owner and next evidence needed. Draft status wording distinguishes confirmed event from inference; do not promise delivery dates without evidence.
6. Return complete backlog totals and clearly labeled display subset, plus a package-level exception queue. No carrier/customer contact without explicit authorization.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Order/package | Remaining qty | Promise/clock | Last evidenced event | Age | Exception | Owner | Next check |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
