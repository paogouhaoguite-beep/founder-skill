---
name: weekly-store-performance-review
description: "Prepare a DTC operating review that reconciles sales, contribution, inventory, fulfillment and customer issues into specific decisions. Use for weekly management actions, not a dashboard of unrelated KPIs."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=weekly-store-performance-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Weekly Store Performance Review

Built by [ShopChief](https://shopchief.ai/?utm_source=weekly-store-performance-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Current and comparable prior period with timezone/currency; order/sales/payment exports; refunds/returns; variable costs and ad spend; inventory availability; fulfillment exceptions; support issues and previous action log.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Reconcile definitions and coverage before comparisons: booked sales, collected payments and payouts differ; returns may be processed in a different week from sale. Keep physical returns separate from financial reversals and do not mix tax-inclusive totals with net merchandise revenue.
2. Build bridges for material movement. Revenue change can arise from order count, realized order value and mix; do not call it a channel effect without attribution evidence. Separate paid acquisition spend from complete new-customer CAC when other acquisition costs are missing.
3. Compute pre/post-ad contribution on matched populations and show cost completeness. Surface stockouts, delayed fulfillment and unresolved customer issues alongside revenue. Compare aligned complete weeks and label promotions, holidays or partial periods.
4. Convert evidence into a small action register with owner, proposed change, expected mechanism, verification date and stop condition. Carry forward unresolved actions; an improving dashboard is not proof that a prior action caused the change. Do not publish reports externally or schedule ongoing jobs without scope.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Area/metric definition | current/prior | absolute/relative change | source/coverage | mechanism/uncertainty | action/owner | check date | prior action status |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify sales discrepancies](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/sales-discrepancies)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)
- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
