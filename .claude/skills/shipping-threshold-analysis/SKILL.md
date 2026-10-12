---
name: shipping-threshold-analysis
description: "Evaluate a DTC free-shipping threshold using actual basket distribution, contribution and delivery costs. Use to compare candidate thresholds without assuming an AOV increase is profit."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=shipping-threshold-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Shipping Threshold Analysis

Built by [ShopChief](https://shopchief.ai/?utm_source=shipping-threshold-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Order-level discounted merchandise subtotal; shipping charged and shipping cost by zone; variable product margin; additional-item shipping cost; returns; current thresholds and discount interactions; proposed markets and exclusions.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Define threshold eligibility: currency, market, discounted subtotal and product exclusions under the actual checkout rules. Segment oversized or costly destinations instead of averaging away losses.
2. Replay historical baskets unchanged to estimate subsidy on orders already eligible. This is a static cost exposure, not a behavioral forecast. Explicitly model an additional-item scenario separately from conversion gain or lost carts.
3. Incremental contribution for a topping-up order = contribution from added merchandise - shipping revenue forgone - incremental fulfillment/shipping/fee/return costs. Existing carrier cost may already be in the baseline; avoid subtracting it twice.
4. Report contribution per eligible visitor or session when reliable traffic data exists. Select a pilot threshold with spend cap and checkout checks, not a universal AOV multiplier. Prepare settings and copy only; changing live rates requires scope.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Market/threshold | eligible historical orders | baseline shipping revenue | subsidy exposure | added-basket assumption | incremental contribution | excluded zones | pilot rule |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify shipping options](https://help.shopify.com/en/manual/fulfillment/setup/shipping-options/setting-up-shipping-options)
- [Shopify discount combinations](https://help.shopify.com/en/manual/discounts/discount-combinations)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
