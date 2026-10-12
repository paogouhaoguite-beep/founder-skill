---
name: supplier-spend-analysis
description: Use when a DTC merchant needs a supplier/category spend and consolidation
  review.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=supplier-spend-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Spend Analysis

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-spend-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A supplier/category spend and consolidation review. Supply invoice/credit transaction IDs, legal supplier/parent evidence, tax/currency basis, categories, PO request/approval/receipt/payment dates, contracts/renewal notices and usage/need records.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Retain original rows; deduplicate transaction IDs, keep credits negative, separate currencies and periods. Proposed supplier aliases/parent links require legal or contract evidence; similar names do not prove same entity.
2. Classify spend by merchant taxonomy with confidence/unknowns; reconcile category and supplier totals back to source. Rank cumulative spend concentration from actual distribution without assuming 80/20.
3. Compare category spend/volume/rate changes and contracted/off-contract evidence; missing contract reference means unknown, not misconduct. Detect duplicate invoice candidates and renewal clusters for review.
4. Calculate request→approval→PO→receipt→payment intervals from actual case records, including open ages. Compare medians/quantiles by category as diagnostic context; slow categories may reflect mandatory qualification, not an automatic bottleneck.
5. Evaluate overlapping suppliers/tools against actual usage, capability and switching/exit/qualification cost. Classify supply risk versus commercial impact using explicit evidence and merchant definitions, not arbitrary Kraljic scores.
6. Propose consolidation only with a tested continuity alternative for critical items and realistic qualification lead time. Show gross potential saving, transition cost and unresolved risk; do not promise 72-hour recovery or cancel subscriptions.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Category/supplier | Net spend/currency | Share | Alias evidence | Contract/notice | Cycle evidence | Overlap/continuity | Action |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
