---
name: store-incident-signal-review
description: Use when a DTC merchant needs a diagnosis and actionable alert specification
  for a suspected store checkout or order-processing incident.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=store-incident-signal-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Store Incident Signal Review

Built by [ShopChief](https://shopchief.ai/?utm_source=store-incident-signal-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A diagnosis and actionable alert specification for a suspected store checkout or order-processing incident. Supply timestamped sessions/payment attempts/order events, error/decline codes, data freshness, comparable baseline, deployment/promotion history and escalation owners.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Confirm whether the underlying source is fresh and complete before interpreting zeros. Separate no traffic, event pipeline failure, actual checkout failure and a report delay.
2. Compute scoped funnel/payment rates with numerator/denominator, market/device/payment-method and period. Distinguish attempts, unique checkouts and completed orders; repeated retries can inflate attempt counts.
3. Split payment failures by observed provider outcome and system error, preserving unknowns. Do not equate issuer decline codes with confirmed fraud or infer infrastructure root cause from symptoms alone.
4. Trace a representative affected path with redacted evidence, comparing before/after changes and control segments. A successful homepage request does not prove checkout works; do not run a real purchase without permission.
5. Propose an alert using merchant baseline/impact tolerance, minimum evidence volume, sustained duration, dedup/cooldown, data-freshness gate and runbook owner. Never copy a universal 90% success or fixed latency threshold.
6. Deliver observed incident scope, competing hypotheses, immediate safe checks and alert acceptance cases. No live monitoring deployment, rollback or external incident message is implied.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Signal/window | Numerator/denominator | Freshness | Affected scope | Observed error | Hypothesis | Owner/action |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
