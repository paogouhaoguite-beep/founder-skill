---
name: discount-profitability
description: "Calculate contribution and break-even volume for a DTC promotion, including eligible baskets, seller funding and discount stacking. Use to evaluate an offer before creating discount rules."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=discount-profitability&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
  upstream: https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitive-pricing-strategy/SKILL.md
---

# Discount Profitability

Built by [ShopChief](https://shopchief.ai/?utm_source=discount-profitability&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Baseline realized price/quantity, discount type/eligibility, product and order combinations, shipping promotion, variable costs/fee bases, return assumptions, budget and target contribution.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Model actual eligible line items and basket qualification. Distinguish seller-funded from reimbursed offers and promotional price from a reference price. Inspect current store discount capabilities rather than assume every class stacks.
2. Apply discount sequence to its actual base. Two successive 10% reductions produce 19% off, not 20%; separate fixed-amount, free-item and shipping effects. Allocate order discounts to units when comparing SKU contribution.
3. Contribution/order = net merchandise plus retained shipping revenue minus landed goods and relevant variable selling costs. Recalculate percentage fees on their documented base; fixed costs remain fixed. Show uncertainty in returns and free-shipping uptake.
4. If positive, break-even volume ratio = baseline contribution/order / promotion contribution/order under unchanged mix. It is a required volume response, not a forecast. If promotional contribution is zero or negative, no finite positive sales uplift restores baseline contribution through that same unit economics. Prepare a scoped offer with expiry and spend guardrail, not an enabled discount.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Offer/basket | effective discount | net revenue | variable costs | contribution/order | required volume ratio | funding/stack assumptions | decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify discount combinations](https://help.shopify.com/en/manual/discounts/discount-combinations)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

Selected workflow elements adapted from [Nexscope AI](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitive-pricing-strategy/SKILL.md), MIT; see [LICENSE](LICENSE). DTC scope, evidence gates and worked cases are adapted for this package.
