---
name: market-basket-affinity-analysis
description: Use when a DTC merchant needs a product-pair affinity analysis and evidence-based
  recommendation candidate list.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=market-basket-affinity-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Market Basket Affinity Analysis

Built by [ShopChief](https://shopchief.ai/?utm_source=market-basket-affinity-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A product-pair affinity analysis and evidence-based recommendation candidate list. Supply complete eligible order baskets including single-product orders, product/variant identity, returns/cancellations policy, dates, promotion/bundle flags, current compatibility/stock and optional consented segment definitions.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define the eligible basket universe including single-product orders, then deduplicate each product within each order. Multiple units of A are one presence of A; exclude artifacts under a declared policy and preserve full line pagination/export coverage.
2. For A/B compute counts N, nA, nB and nAB over the same universe. Support=nAB/N; confidence A→B=nAB/nA; reverse confidence=nAB/nB; lift=(nAB/N)/((nA/N)(nB/N)). Zero denominators are undefined.
3. Rank using merchant minimum count/stability needs and show all raw counts. High lift from a rare pair is not statistical certainty or incremental lift; promotional bundles, preselected recommendations and stock constraints can generate co-purchase mechanically.
4. Check pair usefulness, variant compatibility, current margin and eligible stock before proposing a placement. Separate evidence-backed “bought together” wording from a curated complement that lacks purchase evidence.
5. For personalized proposals use only authorized segment evidence; provide a contextual/nonpersonal fallback when identity or permission is absent. Avoid sensitive inferences and do not expose individual purchase history.
6. Deliver ranked candidates and a bounded holdout experiment proposal with contribution/checkout guardrails. No recommendation engine installation, customer profiling or live merchandising change is implied.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Pair | N/nA/nB/nAB | Support | Confidence each way | Lift | Confounder/compatibility | Candidate action |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
