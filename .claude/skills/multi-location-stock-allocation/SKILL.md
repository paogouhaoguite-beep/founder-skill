---
name: multi-location-stock-allocation
description: "Plan DTC stock transfers and location allocations against local demand, shipping reach, reservations and transfer lead time. Use for a reviewable allocation sheet, not silently synchronizing inventories."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=multi-location-stock-allocation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Multi Location Stock Allocation

Built by [ShopChief](https://shopchief.ai/?utm_source=multi-location-stock-allocation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

SKU/location state snapshots with timestamps; regional demand and ship eligibility; incoming transfers; transfer cost/time; location capacity, minimum stock and fulfillment cutoff constraints.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Reconcile all locations to one snapshot and preserve reserved or quality-held units. A transfer changes placement, not network supply. Do not make the same incoming transfer available at two locations.
2. Project each location to transfer arrival using local demand. Compare a shortage with transferable surplus after the source location's own horizon and buffer; total network stock can mask a regional service failure.
3. Allocate scarce units by merchant priorities such as promised orders, expiry and service cost. Show an explicit ranking or optimization objective; do not invent a universal equal split. Compare transfer cost with credible avoided expedite/lost-contribution scenarios, without declaring every unfilled unit a lost sale.
4. Prepare exact from/to, SKU, quantity, ship/arrival date and inventory states. Creation, shipment and receipt are different events. If execution is requested, inspect current tool schema and re-read quantities before a scoped transfer; reconcile an uncertain write instead of repeating it.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| SKU | from/to | source stock after demand | destination projected gap | transfer units | ETA | cost | commitments protected | authorization/status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)
- [Shopify purchase orders](https://help.shopify.com/en/manual/products/inventory/purchase-orders/creating-purchase-orders)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
