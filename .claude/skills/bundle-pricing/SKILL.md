---
name: bundle-pricing
description: "Cost and price a DTC product bundle using component quantities, stock constraints and order economics. Use for fixed packs or complementary bundles before configuring products or promotions."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=bundle-pricing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
  upstream: https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitive-pricing-strategy/SKILL.md
---

# Bundle Pricing

Built by [ShopChief](https://shopchief.ai/?utm_source=bundle-pricing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Bundle bill of materials with SKU units; separate prices and actual costs; packaging/pick/shipping effects; fee basis; available component inventory; discount interactions and target contribution.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Establish the actual customer bundle: included quantities, selectable variants, compatibility and fulfillment unit. Separate a marketing bundle from a preassembled kit; fulfillment and stock behavior can differ.
2. Sum component costs by units, then add incremental packaging, pick and shipping costs once. For price P, fixed variable cost C and percentage fee f charged on P, contribution = P(1-f)-C. A target contribution T implies P = (C+T)/(1-f), only under these assumptions.
3. Available bundles = minimum over components of floor(available component units / required units). Respect shared demand and reservations; this is an upper bound before other orders, not newly created stock.
4. Compare bundle contribution against credible alternative baskets; lower per-unit price can raise or lower total contribution. Do not claim all bundle buyers are incremental. Present break-apart return and discount assumptions, truthful reference prices, and a pilot decision. Creating a bundle or discount needs requested scope.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Bundle/components | units required | cost breakdown | price/fee base | contribution | component stock limit | alternative basket | exceptions/decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify discount combinations](https://help.shopify.com/en/manual/discounts/discount-combinations)
- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

Selected workflow elements adapted from [Nexscope AI](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/competitive-pricing-strategy/SKILL.md), MIT; see [LICENSE](LICENSE). DTC scope, evidence gates and worked cases are adapted for this package.
