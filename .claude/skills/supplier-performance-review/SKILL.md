---
name: supplier-performance-review
description: Use when a DTC merchant needs a supplier performance and dependency review.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=supplier-performance-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Performance Review

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-performance-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A supplier performance and dependency review. Supply PO due/receipt quantities and dates, inspection results, contract metric definitions, invoices/credits, incidents and corrective actions, supplier/parent/sub-tier/route evidence, buffer and alternative qualification data.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define denominator and window for on-time, in-full and OTIF. OTIF counts the same PO satisfying both conditions, not the product or average of separate rates. Separate unit defects from lot rejection and sample from population.
2. Compare each actual metric to the agreed contract target with evidence/coverage, not a universal score. Show trend and unresolved credits only when contractual criteria and claim windows are verified.
3. Map dependency by SKU/component, direct supplier, known upstream factory, geography and port/route. Explicitly mark visibility boundary; two direct vendors sharing one factory or port may not diversify risk.
4. Compare days of evidenced usable buffer with realistic qualification+transition lead time for alternatives. An unqualified quote is not an available backup. Model interruption scenarios without inventing likelihoods or fixed spend multipliers as financial exposure.
5. Build periodic review agenda from previous actions, delivery/quality/service gaps, commercial leakage, incidents and notice deadlines. Require supplier claim versus buyer-verified evidence distinction and named owners for root-cause proof.
6. Recommend keep/review/qualify alternative based on specific gates and consequences. Define corrective action evidence and follow-up dates; do not automatically terminate or contact suppliers.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Supplier/node | Metric numerator/denominator | Contract target | Evidence | Dependency/visibility | Alternative lead time | Action/owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
