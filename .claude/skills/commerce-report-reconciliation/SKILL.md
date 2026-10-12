---
name: commerce-report-reconciliation
description: Use when a DTC merchant needs a reconciliation of conflicting channel,
  location, discount, cancellation or operating reports.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=commerce-report-reconciliation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Commerce Report Reconciliation

Built by [ShopChief](https://shopchief.ai/?utm_source=commerce-report-reconciliation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A reconciliation of conflicting channel, location, discount, cancellation or operating reports. Supply report definitions, filters/timezones/currencies, order/line/payment/refund/fulfillment events, category mappings, cost coverage and the totals being compared.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Write a metric contract for each report: event/recognition date, grain, inclusions, currency basis, refund handling and denominator. Sales, payments, payouts, contribution and accounting profit are different measures; a dashboard label does not reconcile them.
2. Reconstruct order/line grain and deduplicate stable IDs before joins. Allocate order-level amounts once using a stated driver; retain unallocated amounts. For discounts distinguish line allocation, order discount, shipping discount and code association; multiple codes cannot each receive the entire order discount.
3. For channel sales use the recorded selling channel, not acquisition attribution. For location revenue choose a supplied line/fulfilled-quantity attribution method, allow split orders and reconcile allocations to original net sales; no full order revenue repeated at every location.
4. For cancellation rates use a defined creation cohort and observation cutoff, comparing like maturity. Separate cancellation event volume from cohort cancellation rate and reason missingness; flag observed changes with counts rather than a universal anomaly multiple.
5. Reconcile revenue through supplied COGS/direct costs to contribution, keeping missing costs and allocation assumptions visible. For operational KPIs preserve order/unit/parcel grain and eligible event denominators; do not multiply on-time and in-full rates to obtain joint OTIF.
6. Deliver a difference bridge, corrected report table and source/owner for unresolved residuals. Do not auto-post journals, infer fraud from anomalies or claim causation from dashboard trends.
7. For landing-page reports state whether sessions are entrances or any page views, use the report’s actual conversion numerator/window, and retain page type/path. Rank high-exposure gaps against merchant/comparable baseline with device/source/stock context; do not classify every page below a universal 2% conversion threshold as defective. A before/after week alone does not isolate page-change causality.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Metric/report | Grain/date/currency | Source total | Rebuilt total | Explained difference | Residual/gap | Owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
