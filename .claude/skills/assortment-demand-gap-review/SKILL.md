---
name: assortment-demand-gap-review
description: Use when a DTC merchant needs an evidence-based assortment gap and launch-cohort
  sell-through review.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=assortment-demand-gap-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Assortment Demand Gap Review

Built by [ShopChief](https://shopchief.ai/?utm_source=assortment-demand-gap-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An evidence-based assortment gap and launch-cohort sell-through review. Supply SKU attributes/availability, onsite search and zero-result evidence, competitor matched assortment, receipts/sales/returns by launch cohort, demand windows and supplier/operating constraints.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map current assortment to a shopper decision tree using need, format, size, variant and price attributes relevant to the category. Empty cells are catalog gaps, not yet proven market opportunities.
2. Attach demand evidence to cells: distinct search sessions/queries, zero results, customer requests and dated external measures with their units. Distinguish a taxonomy/search synonym failure from a genuinely missing product.
3. Compare competitor coverage using matched definitions and availability, recording sampled scope. SKU-count ratios do not establish lost demand or an optimal assortment; no universal coverage threshold.
4. For launch cohorts calculate sell-through using a declared available-unit denominator such as opening units plus eligible receipts, with returns and transfers explicitly handled. Compare equivalent launch age and in-stock exposure; censored stockouts and unobserved demand remain separate.
5. For each supported gap assess fulfillment, MOQ, margin and substitution risk using evidence or scenarios. Do not turn target fair share or hypothetical cannibalization into forecast revenue; stage the smallest test and its pass/stop evidence.
6. Deliver decision-tree coverage, demand/search repair versus product-test queue, and cohort evidence. No automatic assortment additions or PO commitments.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Decision-tree cell | Current/competitor coverage | Demand evidence | Search versus product gap | Cohort sell-through | Feasibility | Next test |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
