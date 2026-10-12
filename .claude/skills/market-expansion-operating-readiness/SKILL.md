---
name: market-expansion-operating-readiness
description: Use when a DTC merchant needs a go/hold evidence review for entering
  a new selling market.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=market-expansion-operating-readiness&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Market Expansion Operating Readiness

Built by [ShopChief](https://shopchief.ai/?utm_source=market-expansion-operating-readiness&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A go/hold evidence review for entering a new selling market. Supply target products/market, dated demand and competitor evidence, actual shipping/payment/localization/returns capability, qualified regulatory/tax instructions, partner quotes, entry costs and merchant scenario assumptions.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define the initial market/product scope and measurable pilot objective. Distinguish addressable demand evidence from projected store share; no market-size threshold automatically justifies entry.
2. Check hard operating gates: product eligibility evidence, qualified labeling/tax/import review, supported payments/currency, delivery/returns path, customer support and available stock. Missing mandatory evidence cannot be offset by a high composite score.
3. Build unit contribution from actual price/currency, landed goods, payment/fulfillment/returns and channel costs. Separate one-time entry investment, recurring costs, working capital and revenue recognition; preserve unknown costs.
4. Compare bounded demand/FX/lead-time scenarios and cash requirements. Discounted cash flow is shown only with finance-supplied cash-flow timing and rate, not contribution mislabeled as cash; no invented probabilities.
5. Assess partner capacity and alternatives, commercial cannibalization and localization needs with specific owner/evidence/date. Keep unknown regulatory burden or supplier proximity out of fake numerical risk scores.
6. Deliver pilot/hold decision with evidence gates, downside exposure, trigger and owner. No country launch, regulatory filing, spend or partner commitment without scope.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Market/product | Mandatory gate | Evidence/date | Unit economics | Pilot cost/cash | Downside scenario | Decision/owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
