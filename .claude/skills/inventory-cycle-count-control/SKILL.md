---
name: inventory-cycle-count-control
description: Use when a DTC merchant needs a cycle-count plan and discrepancy investigation.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=inventory-cycle-count-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Inventory Cycle Count Control

Built by [ShopChief](https://shopchief.ai/?utm_source=inventory-cycle-count-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A cycle-count plan and discrepancy investigation. Supply SKU/bin/lot ledger as-of, count observations with counter/time, movements during count, unit cost and merchant count priority/tolerance rules.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Select count scope from actual value/movement/error history and random/process-triggered samples. Keep merchant-defined count cadence; no fixedABC percentages or accuracy targets.
2. Prepare blind count instructions by bin/lot/unit, marking sealed cases versus loose units. Record count cutoff and movements; do not give counter expected quantity as a prompt to confirm.
3. Bridge ledger to count time using receipts/picks/transfers. Difference = physical minus comparable book quantity. Recount material discrepancies independently before proposing a correction.
4. Classify evidence-supported receiving, picking, unit conversion, location, sync or damage causes. An unexplained shortage is not proof of theft; avoid accusing individuals from risk scores.
5. Calculate exact-match count accuracy and absolute-unit variance with explicit denominator; value variance uses known cost and isolates missing costs. Deliver adjustment proposals and prevention owner, never auto-post on first count.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| SKU/bin | Book at cutoff | Cutoff movements | Physical count | Variance | Recount | Cause evidence | Proposed action |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
