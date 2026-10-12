---
name: subscription-unit-economics
description: "Calculate observed cohort contribution and acquisition payback for physical DTC subscriptions, separating paid shipments, skips, cancellations and failed renewals."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=subscription-unit-economics&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Subscription Unit Economics

Built by [ShopChief](https://shopchief.ai/?utm_source=subscription-unit-economics&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Acquisition cohorts and cost, contract/customer identifiers, scheduled and paid renewals, shipment dates, revenue/refunds, variable product/fulfillment/payment costs, skips/pauses/cancellations and observation cutoff.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Define cohort unit: customer, contract or subscription shipment. Multiple subscriptions per customer must not duplicate acquisition cost or customer counts. Scheduled renewal revenue is not collected revenue.
2. Track period eligibility, paid renewals, skipped orders, failures recovered and cancellations separately. State denominators and right-censor younger cohorts; active contracts alone do not establish retention or future revenue.
3. Observed contribution = collected revenue net of refunds minus attributable product, shipment, payment and support costs. Cumulative contribution per initially acquired customer = cohort contribution to cutoff / original cohort size. Payback occurs when that cumulative amount reaches acquisition cost on the same basis.
4. Forecast only with explicit retention, reorder frequency, cost and discount assumptions; do not use a perpetual revenue/churn shortcut as observed profit LTV. Show cash settlement and inventory prepayment pressure separately. Do not alter subscription pricing, retry payments or message subscribers from an analysis request.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Cohort/cutoff | original customers | eligible renewals | paid shipments | skip/failure/cancel | net receipts | contribution | cumulative/customer | CAC/payback state |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify Subscriptions analytics](https://help.shopify.com/en/manual/products/purchase-options/subscriptions/shopify-subscriptions/analytics)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
