---
name: support-workload-capacity-planning
description: Use when a DTC merchant needs a support staffing and surge-capacity plan.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=support-workload-capacity-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Support Workload Capacity Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=support-workload-capacity-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A support staffing and surge-capacity plan. Supply daily/intraday ticket arrivals by channel/skill, active handling-time distribution, backlog and deadlines, agent schedules, shrinkage, ramp/attrition assumptions, concurrency evidence and approved service targets.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define queue boundaries and comparable time intervals; distinguish tickets, contacts and reopened work. Measure demand distribution and peak context rather than planning only to the average; sparse history supports scenarios, not precise tail probabilities.
2. Convert arrivals and backlog clearance into active workload minutes using observed handling times. Treat simultaneous chat work only with measured effective concurrency; do not count the same agent fully available in multiple queues.
3. Calculate productive minutes = scheduled minutes × (1−documented shrinkage) × effective ramp, adjusting for actual overlap and skills. Compare workload with capacity across merchant-selected base/peak scenarios; missing schedule or handling time leaves sizing unresolved.
4. Separate arithmetic load from response-time guarantees. Workload/capacity is not an SLA breach probability; Erlang-C requires its queue assumptions and validated inputs, and is not supplied here as a black-box promise.
5. Build hiring/coverage timing from start dates, ramp and attrition, retaining manager/QA/training time and single-person skill dependencies. A new hire is not immediately one productive FTE; avoid universal utilization or manager-span targets.
6. Deliver scenario gaps and a practical surge choice: cross-trained coverage, approved temporary staffing, backlog window or explicitly approved service change. No staffing commitment or customer promise without owner decision.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Queue/day scenario | Demand/backlog minutes | Scheduled minutes | Shrinkage/ramp | Productive minutes | Gap | Coverage decision |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
