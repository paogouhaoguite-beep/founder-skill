---
name: landed-cost-model
description: "Allocate confirmed inbound costs to DTC SKU lots and distinguish landed cost, import cash outlay and outbound fulfillment. Use for quote-to-receipt costing with explicit duty and tax assumptions."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=landed-cost-model&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Landed Cost Model

Built by [ShopChief](https://shopchief.ai/?utm_source=landed-cost-model&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Purchase invoice/quantity; accepted usable units and rejects; inbound freight/insurance; duties/brokerage/receiving; currency/rates/dates; delivery terms; tax recoverability evidence; allocation drivers such as value, weight or volume.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Map each charge once to the shipment and responsible payer. Separate recoverable-tax cash from expense and preserve unknown tax treatment for an adviser; do not supply a guessed tariff code/rate.
2. Choose a causal allocation basis for each shared cost: transport weight/volume, declared value, or a documented even-unit convention. Check allocated totals reconcile exactly; preserve rounding residuals in an explicit row or final allocation.
3. Unit landed cost = attributable purchase and nonrecoverable inbound costs / usable units under the selected costing treatment. Report rejected units and recovery/supplier credits separately; do not both expense rejected purchase cost and load it into accepted units without explaining the treatment.
4. Reconcile estimated quote costs with actual invoices, keeping FX/quantity/charge variances separate. Outbound postage and payment processing belong in downstream contribution economics, not inbound cost twice.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Shipment/lot/SKU | usable units | purchase | inbound allocations | nonrecoverable tax | recoverable-tax cash | unit landed cost | basis/evidence | estimate/actual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify purchase orders](https://help.shopify.com/en/manual/products/inventory/purchase-orders/creating-purchase-orders)
- [Shopify profit reporting](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/profit-reports)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
