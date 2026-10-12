---
name: complaint-theme-and-csat-analysis
description: Use when a DTC merchant needs an explanation of complaint themes or CSAT
  movement.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=complaint-theme-and-csat-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Complaint Theme And Csat Analysis

Built by [ShopChief](https://shopchief.ai/?utm_source=complaint-theme-and-csat-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An explanation of complaint themes or CSAT movement. Supply ticket/survey IDs and dates, raw verbatims, score scale and top-box definition, eligible/invited/responding counts, order/product/lot links, operational event log and comparable period.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Deduplicate repeat contacts about the same issue while retaining contact burden. Preserve all eligible scores including blank comments for score denominators; code nonblank comments separately. Record sampling, invitation and response rates, question/channel changes and missing cohorts.
2. Create two-level theme definitions with inclusion/exclusion examples. Split multi-issue comments for coding but retain original respondent ID; report unique respondent theme incidence so split comments do not inflate denominator. Route agent-only feedback separately without erasing it from CSAT.
3. Calculate theme prevalence as respondents mentioning theme / eligible coded respondents, plus ticket/contact counts and observed handling costs. Compare scores with/without theme as association, not causal impact. Small samples remain descriptive; do not invent significance or universal escalation thresholds.
4. For segment mix changes use exact decomposition: total score change = sum((new weight−old weight)×old rate) + sum(new weight×(new rate−old rate)). Report sample sizes and denominator; compare identical score scales only.
5. Link themes to SKU/lot, carrier, page/policy or process changes using IDs and dated evidence. Build a why-chain where each link is observed, hypothesis or missing evidence. Avoid fabricated churn multipliers, hidden-complaint factors and predicted CSAT gains.
6. Return anonymized representative verbatims, coded rows, rate/mix bridge and prioritized store-side fixes with owner and validation metric. Human escalation remains for safety/refunds; automation is only proposed after policy and data quality are verified.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Theme/L1-L2 | Unique respondents/denominator | Score association | Evidence/alternative explanation | Proposed fix | Owner | Validation metric |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
