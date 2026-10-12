---
name: operations-process-handoff-review
description: Use when a DTC merchant needs a measured map of an order, return, purchasing
  or support workflow that is slow or losing handoffs.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=operations-process-handoff-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Operations Process Handoff Review

Built by [ShopChief](https://shopchief.ai/?utm_source=operations-process-handoff-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A measured map of an order, return, purchasing or support workflow that is slow or losing handoffs. Supply case-level stage arrival/start/end timestamps, owner, active work/wait/rework labels, branches, batch size, completed and open cases and the business service objective.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map the actual path with owners, entry/exit conditions, handoff and rework loops. Keep intended future process separate. For parallel stages calculate elapsed critical path from timestamps, not sum overlapping durations.
2. For each completed case reconcile total elapsed time with nonoverlapping active work, wait and rework. Preserve open-case ages and missing events rather than dropping slow cases invisibly.
3. Calculate end-to-end median/percentiles from case-level totals using a stated convention; stage medians or P90 values do not add to an end-to-end percentile. Stage variance shares based only on variances are not total variance attribution when stage durations covary.
4. Compare stage queues, arrival/load, batch cadence and downstream capacity to identify an evidenced constraint. A long elapsed stage may be waiting for an external approval rather than overloaded labor. Separate root-cause hypotheses from measured bottlenecks.
5. For a stable boundary and matching time units, average WIP / throughput estimates average elapsed time under Little’s Law. Do not apply it to a transient surge or use a percentile as the mean. No universal healthy value-add percentage.
6. Propose one bounded intervention with owner, measurable expected mechanism and end-to-end follow-up. Keep safety/quality gates and record whether work merely moved into another queue.
7. Use the constraint sequence: identify an evidenced bottleneck, exploit available capacity, align upstream/downstream work to it, then consider investment and remeasure. If the limiting factor is unproven demand or distribution rather than an operating queue, state that boundary and request matching funnel/distribution evidence; do not assume the largest benchmark gap is causal.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Stage/owner | Case coverage | Active/wait/rework | Handoff evidence | Constraint hypothesis | Proposed intervention | End-to-end measure |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
