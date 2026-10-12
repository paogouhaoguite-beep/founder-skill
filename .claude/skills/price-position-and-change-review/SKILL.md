---
name: price-position-and-change-review
description: Use when a DTC merchant needs a comparable-price and proposed price-change
  decision.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=price-position-and-change-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Price Position And Change Review

Built by [ShopChief](https://shopchief.ai/?utm_source=price-position-and-change-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A comparable-price and proposed price-change decision. Supply current/effective price and reference-price history, competitor observations with URLs/date/pack/delivery terms, cost/fee assumptions, inventory, merchant price guardrails and any measured elasticity evidence.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Match exact GTIN/variant or label an equivalent comparison with its differences. Normalize pack/unit, currency/date, tax/shipping inclusion, subscription/member/coupon conditions and availability; unavailable or conditional competitor prices are not unconditional parity targets.
2. Calculate unit-price gaps and a weighted index only over comparable observations with a stated weighting basis. Show unmatched share and snapshot date; do not impose universal parity bands or automatically follow the lowest price.
3. For a proposed price compute unit contribution after supplied variable costs and percentage fees. Model volume scenarios separately; elasticity is used only if merchant supplies a defensible estimate/range and model horizon, not invented from one price comparison.
4. Calculate break-even volume change from contribution per unit and current volume, keeping fixed/incremental costs explicit. Large linear elasticity extrapolation or stock-constrained demand is a scenario limitation, not a forecast.
5. Validate reference/compare-at price against actual dated price evidence and approved market guidance. A catalog updatedAt date is not a price-history timestamp. Do not clear or inflate reference prices solely due to age or current price arithmetic.
6. Deliver proposed price/reference change set, margin scenarios and evidence gaps with rollback and merchant decision. No live repricing, misleading savings claim or implied legality approval.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| SKU/match | Comparable unit price | Current/proposed | Unit contribution | Volume scenario | Reference evidence | Decision |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
