---
name: fulfillment-carrier-comparison
description: "Compare DTC fulfillment and carrier offers using actual parcel mix, invoice terms and service evidence. Use for a costed shortlist and pilot plan rather than an unsupported cheapest-provider claim."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=fulfillment-carrier-comparison&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
  upstream: https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/warehouse-optimization/SKILL.md
---

# Fulfillment Carrier Comparison

Built by [ShopChief](https://shopchief.ai/?utm_source=fulfillment-carrier-comparison&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Order/parcel sample by origin, destination and service; packed dimensions/weight; units/order; current invoices and dated rate cards; surcharges, minimums, storage/receiving/returns; tracking performance; delivery constraints.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Normalize eligible services and parcel mix before price comparison. Use the actual carrier contract's dimensional divisor, rounding and billable-weight rule; no universal divisor. Include remote/residential/fuel/peak charges and excluded destinations.
2. Separate fixed monthly charges from variable per-order and per-unit fees. Compute weighted variable cost across the same actual basket; then allocate fixed costs at explicitly stated volume. For minimum charges, apply the contract's offset/addition terms rather than blindly adding them twice.
3. Compare service evidence using consistent delivery intervals, missing scans and cancellation exclusions. Carrier claims are promises, not observed on-time rates. Keep loss/damage and return handling visible; the cheapest mean price may fail required coverage.
4. Show low/base/high volume sensitivity and migration costs. Propose a bounded pilot with comparable parcels and clear hold criteria. Do not purchase labels, move stock, sign a provider contract or promise a delivery date without the requested scope and current service verification.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Provider/service | basket coverage | variable cost/order | fixed/minimum treatment | total at volume | delivery evidence | exclusions | pilot decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify shipping options](https://help.shopify.com/en/manual/fulfillment/setup/shipping-options/setting-up-shipping-options)
- [UPS Canada weight and size reference; use current local contract for rates](https://www.ups.com/assets/resources/webcontent/en_CA/rate_guide_ca.pdf)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

Selected workflow elements adapted from [Nexscope AI](https://github.com/nexscope-ai/eCommerce-Skills/blob/ee0fb29433d02ccc22e3e6cea9ab4586d49fd42e/warehouse-optimization/SKILL.md), MIT; see [LICENSE](LICENSE). DTC scope, evidence gates and worked cases are adapted for this package.
