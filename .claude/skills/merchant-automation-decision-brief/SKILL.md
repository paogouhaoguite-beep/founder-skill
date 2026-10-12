---
name: merchant-automation-decision-brief
description: Use when a DTC merchant needs a bounded automation opportunity decision
  for a recurring merchant operations problem.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=merchant-automation-decision-brief&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Merchant Automation Decision Brief

Built by [ShopChief](https://shopchief.ai/?utm_source=merchant-automation-decision-brief&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A bounded automation opportunity decision for a recurring merchant operations problem. Supply one recent concrete incident, trigger and desired end state, decision owner, evidence sources/freshness, action alternatives, cost/consequence and reversibility.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Reconstruct the operating moment before discussing tools: what happened, who decided, when a response was needed and what observable outcome mattered. Replace broad topics like “automate inventory” with a single decision.
2. Separate fact collection, option comparison and consequential commitment. Map each to inputs, quality checks, exception owner and authority; the agent does not inherit authority to spend or change orders from permission to analyze.
3. Test readiness gates: stable IDs, adequate data, known policy, accountable owner, bounded error consequence, reversible action or approved human release. Missing ownership or unreliable evidence can yield not ready.
4. Choose the smallest supported delegation level: summarize, recommend, prepare a change or execute inside explicitly approved rules. Describe stop conditions, duplicate/timeout handling and verification receipt rather than vague human-in-the-loop wording.
5. Define a pilot on real historical cases with expected decisions and failure cases, comparison baseline and monitoring owner. Do not invent volume savings, ROI or accuracy to justify a pilot.
6. Deliver a decision brief or a not-ready repair plan; no automation setup or recurring task until requested.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Decision/trigger | Owner | Facts/options/commitment | Data readiness | Delegation level | Stop/readback | Pilot cases |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
