---
name: return-policy-economic-review
description: Use when a DTC merchant needs a comparison of return-policy economics.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=return-policy-economic-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Return Policy Economic Review

Built by [ShopChief](https://shopchief.ai/?utm_source=return-policy-economic-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A comparison of return-policy economics. Supply completed order cohorts, return request/receipt dates, actual refund and recovered inventory cost, reverse freight/labor/fees, policy versions, eligible jurisdictions and merchant-approved legal constraints.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Choose mature sale cohorts and show outstanding return-window exposure. Compute returned units/orders against corresponding sold cohorts; compare category/reason/condition and policy versions without mixing refund-date counts and sale-date denominators.
2. Separate refunded revenue from incremental return expense and inventory recovery. State original contribution and revised contribution so refund dollars are not double-counted as both revenue reduction and extra cost.
3. Model each policy option from actual observed costs or labeled assumptions: reverse freight, inspection, repackaging, lost outbound freight, unreversed processing fees and evidenced write-down. Use original cost, not current catalog cost; stated reason alone does not establish damaged disposition.
4. Compare return-window, shipping payer and exchange choices using transparent low/base/high behavioral scenarios. Do not assume generous policies cause higher retention or high return-rate customers are abusive.
5. Document mandatory rights and published promises supplied by merchant/counsel before proposing changes. No automatic shorter window, forced credit or blocked refunds based on a customer score.
6. Deliver policy options, margin sensitivity, unresolved evidence and a reversible prospective test proposal. Publishing policy or changing live return entitlements requires separate authorization.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Policy/cohort | Return exposure | Refunded revenue | Incremental costs | Recovered cost | Contribution change | Assumptions | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
