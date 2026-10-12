---
name: category-revenue-driver-bridge
description: Use when a DTC merchant needs an explainable revenue-change bridge for
  a category or content-to-purchase funnel.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=category-revenue-driver-bridge&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Category Revenue Driver Bridge

Built by [ShopChief](https://shopchief.ai/?utm_source=category-revenue-driver-bridge&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An explainable revenue-change bridge for a category or content-to-purchase funnel. Supply comparable period sessions, orders, units and net revenue with matched scope, category assignments, price/product mix, change log and attribution evidence.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Confirm the multiplicative identity using matching scope: revenue = sessions × orders/sessions × units/orders × revenue/units. Zero denominators or missing cross-device identity require an alternative valid bridge, not invented rates.
2. Choose and disclose a replacement order for an exact sequential bridge. With T,C,U,P, compute traffic=(T1−T0)C0U0P0; conversion=T1(C1−C0)U0P0; units=T1C1(U1−U0)P0; price/mix=T1C1U1(P1−P0). Sum must equal observed revenue difference.
3. Keep ASP change as price/mix until matched-SKU price and quantity shares support separation. Category and subcategory contributions must be mutually exclusive or explicitly allocated; no repeated order revenue.
4. For content funnel diagnostics trace observed impressions, click-through, landing sessions, product engagement and purchases under each system’s definition/window. Content edits, promotions, stock and channel mix are hypotheses, not causal proof from dates alone.
5. Rank explanations by measured contribution, evidence and missing tests; negative or offsetting components can exceed 100% of net change. Do not multiply an arbitrary confidence factor by revenue gap and call it recoverable revenue.
6. Deliver exact bridge, alternative explanation table and next measurement. Avoid promising that restoring a metric automatically recovers all modeled revenue.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Driver | Prior/current basis | Sequential contribution | Evidence | Alternative causes | Next check |
| --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
