---
name: sku-portfolio-rationalization
description: "Review DTC assortment for keep, replenish, repair, seasonal hold or retirement using contribution, inventory investment and customer role. Use when deciding which SKUs deserve resources, not just sorting revenue."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=sku-portfolio-rationalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
  upstream: https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/warehouse-optimization/SKILL.md
---

# Sku Portfolio Rationalization

Built by [ShopChief](https://shopchief.ai/?utm_source=sku-portfolio-rationalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

SKU/variant sales, realized net revenue and variable costs over matched periods; average inventory at cost; availability and returns; bundles/substitutes; range commitments and lifecycle stage.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Reconcile SKU identities, variants and availability windows. Revenue ranks can prioritize attention but are not profitability grades. A recent launch or repeatedly out-of-stock item needs a separate comparison cohort.
2. Compute contribution dollars from net revenue minus landed COGS and relevant variable selling costs. Show contribution per available selling day where defensible. Inventory return proxy = period contribution / average inventory investment; label its period and avoid calling it annual ROI.
3. Review operational role: attach item, size completeness, replacement part or traffic driver. Distinguish observed basket association from proof that removing an item preserves the basket.
4. Recommend one action per SKU with disconfirming evidence: fix cost/fit, reduce future buys, seasonal hold, limited clearance or retirement. Do not automatically delete low-revenue variants. Simulate the contribution and residual stock consequence of removal before suggesting execution.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| SKU | cohort/availability | net revenue | contribution | average stock cost | period contribution/stock | basket role | decision | evidence needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify inventory reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/inventory-reports)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

Selected workflow elements adapted from [Nexscope AI](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/warehouse-optimization/SKILL.md), MIT; see [LICENSE](LICENSE). DTC scope, evidence gates and worked cases are adapted for this package.
