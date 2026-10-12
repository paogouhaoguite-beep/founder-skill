---
name: price-test-planning
description: "Design a controlled DTC price experiment with contribution guardrails, stable assignment and a stopping plan. Use to learn price response rather than implement automatic repricing or claim an optimal price."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=price-test-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
  upstream: https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/dynamic-pricing-ecommerce/SKILL.md
---

# Price Test Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=price-test-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

SKU/market, current and candidate prices, fee/cost structure, stock and promotions, eligible traffic and purchase history, customer assignment capability, existing orders/subscriptions and approved test constraints.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. State the decision and protect existing contractual prices. Establish price floors from actual costs and merchant objectives. Do not invent reference prices or personalize prices using sensitive traits.
2. Select a comparison design with a defined assignment unit and persistent exposure. If simultaneous price experiments are not operationally suitable, propose a time-based pilot with explicit seasonality/traffic confounding; do not call it randomized evidence.
3. Use contribution per eligible visitor/customer as a primary outcome when costs are reliable, with conversion, cancellations, complaints and returns as diagnostics. Plan sample and observation duration from the baseline, commercially meaningful effect and chosen statistical method; price elasticity cannot be inferred from two uncontrolled points.
4. Model promotion overlap, stockout and stale-cost scenarios; hold when guardrail data is missing. Freeze the stopping rule before launch and retain assignment records. Define approved bounds, rollback and owner. Deliver a design, not live price changes; enabling or reverting prices requires the corresponding scope.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Arm/price | population/assignment | realized revenue | cost/contribution | exposure window | primary metric | guardrails | stop/rollback | uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify discount combinations](https://help.shopify.com/en/manual/discounts/discount-combinations)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)
- [Forecast evaluation, Forecasting: Principles and Practice](https://otexts.com/fpp3/accuracy.html)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

Selected workflow elements adapted from [Nexscope AI](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/dynamic-pricing-ecommerce/SKILL.md), MIT; see [LICENSE](LICENSE). DTC scope, evidence gates and worked cases are adapted for this package.
