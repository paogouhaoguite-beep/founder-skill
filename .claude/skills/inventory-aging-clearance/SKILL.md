---
name: inventory-aging-clearance
description: "Identify aging DTC inventory by receipt lot and compare retain, markdown, bundle, return-to-vendor and disposal options using recoverable cash and remaining costs."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=inventory-aging-clearance&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Inventory Aging Clearance

Built by [ShopChief](https://shopchief.ai/?utm_source=inventory-aging-clearance&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

SKU and lot receipt dates; quantity by usable/held state; unit cost; shelf life or season cutoff; observed unit sales and price; carrying charges; feasible clearance channels, fees and restrictions.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Reconstruct remaining receipt lots from movement history using the merchant's recorded lot method. When only a current stock snapshot exists, age is unknown; days of cover is not age. Distinguish expiry from inventory age.
2. Group by merchant-relevant dates such as season end, expiry or contract return deadline. Do not copy marketplace aged-stock penalties into an independent store.
3. Compare future recoverable cash = expected proceeds - remaining fulfillment, fees, return/disposal and holding costs. Show probability/volume assumptions separately. Historical purchase cost is relevant to full margin and reporting, but is sunk for a choice among future clearance paths; show both views.
4. Identify stock unavailable for sale, product safety constraints and channel restrictions before a price action. Present bounded quantities and a review date; an aging flag does not authorize liquidation or a claim that all stock will sell.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| SKU/lot | receipt evidence | units/age | cutoff | option | future cash/unit | full-cost margin | volume assumption | action owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)
- [Shopify inventory reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/inventory-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
