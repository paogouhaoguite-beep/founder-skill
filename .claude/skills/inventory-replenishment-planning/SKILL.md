---
name: inventory-replenishment-planning
description: "Calculate a time-phased reorder proposal for a DTC SKU using available inventory, demand, inbound dates, supplier lead time and pack constraints. Use for purchase quantities and stockout exposure, not an automatic purchase order."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=inventory-replenishment-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
  upstream: https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/warehouse-optimization/SKILL.md
---

# Inventory Replenishment Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=inventory-replenishment-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

SKU/location; dated available, committed and unavailable quantities; daily units and stockout days; open orders and their allocation status; confirmed incoming quantities and arrival dates; lead/review times; case pack, MOQ, budget and merchant-selected buffer.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Reconcile inventory states. If starting from available units, do not subtract the same commitments again. Identify demand already represented by commitments before adding backlog. Incoming supply covers demand only after receipt and release; list uncertain arrivals separately.
2. Forecast demand across lead time plus review interval. Project daily or weekly receipts and depletion to expose a stockout before a later replenishment; a positive ending balance can hide that gap.
3. For a simplified regular-demand proposal, target = demand across the protection period + explicit buffer. Net requirement = max(0, target - usable available units - confirmed receipts within that horizon + unallocated backlog). Round up to case packs and then check MOQ, cash, shelf life and storage limits. Show excess caused by rounding.
4. A buffer is a merchant choice or an estimate from demand/lead-time uncertainty, not a universal number of weeks. If applying a statistical service-level method, state stationarity, independence, lead-time assumptions and whether the target concerns cycle service or fill rate. With censored stockout sales, give a range instead of treating zero sales as zero demand.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| SKU/location | demand window | usable stock | dated receipts | buffer basis | raw requirement | rounded order | earliest shortage | cash need | evidence/unknowns |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)
- [Shopify inventory reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/inventory-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

Selected workflow elements adapted from [Nexscope AI](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/warehouse-optimization/SKILL.md), MIT; see [LICENSE](LICENSE). DTC scope, evidence gates and worked cases are adapted for this package.
