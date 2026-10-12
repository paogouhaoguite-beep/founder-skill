---
name: nps-followup-priority-planning
description: Use when a DTC merchant needs an NPS distribution and follow-up plan.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=nps-followup-priority-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Nps Followup Priority Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=nps-followup-priority-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An NPS distribution and follow-up plan. Supply respondent IDs/scores on 0–10 scale, survey purpose/window, verbatims, invitation and response coverage, prior comparable sample and merchant contact policy.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Compute promoters 9–10, passives 7–8 and detractors 0–6 over valid responses; NPS=100×(promoters−detractors)/N. Report invalid/missing and the full distribution, not only the headline.
2. Separate comparable cohorts and survey touchpoints. Compare promoter and detractor rates, sample/response composition and actual comments before diagnosing changes.
3. Code actionable issues by respondent group while avoiding the assumption that every detractor is a churn risk or every promoter willing to endorse. Prioritize unresolved material issues with named service owners.
4. For migration scenarios hold denominator constant and state exact moves. Moving one detractor to promoter changes net numerator by 2; detractor to passive changes by 1. Scenario uplift is not a prediction or financial causal estimate.
5. Draft scoped recovery/follow-up queue with permission, duplicate-contact checks, owner and merchant response target. Do not cherry-pick public review requests based on score or publish respondent quotes without appropriate permission.
6. Define process outcomes (issue resolved, contact response) separately from later score/retention observations. No guaranteed recovery rate, universal 48 h SLA or automatic customer messaging.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Group | Count/denominator | Themes | Action | Owner | Permission | Follow-up outcome |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
