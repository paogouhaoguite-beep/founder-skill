---
name: supplier-quote-comparison
description: "Normalize supplier quotes for a DTC purchase by specification, quantity, delivery responsibility and landed-cost scope. Use to compare actual offers, excluding supplier contact or order placement unless requested."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=supplier-quote-comparison&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Quote Comparison

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-quote-comparison&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Dated quotes; exact SKU/material/quality specification; quantities/MOQs/pack size; price/currency; delivery terms and named place; shipping, duties and payment timing; lead-time evidence, samples and inspection costs.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Build a comparable basket. Reject apparent savings from smaller packs, different materials or missing tooling. Separate quote validity, promised production time, transport time and total available-for-sale lead time.
2. Normalize currency with a dated supplied or verified rate. Mark included/excluded/unknown costs per offer. Delivery terms determine responsibilities but are not a duty rate; do not infer tariff classification or recoverable tax treatment.
3. Calculate a scenario total including purchase, freight, inspection and evidenced nonrecoverable import/receiving costs. Amortize tooling only across explicitly assumed units. Show deposit/balance timing separately from unit economics.
4. Compare commercial fit and risks alongside price: defect evidence, minimum commitment, cash exposure, lead-time reliability and remediation terms. An attractive quote is not verified factory capability. Draft clarification questions for material exclusions; do not contact suppliers or place a PO merely to complete comparison.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Supplier/quote date | matched spec | units/MOQ | currency/rate | included costs | total scenario | usable-unit cost | payment dates | unresolved terms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify purchase orders](https://help.shopify.com/en/manual/products/inventory/purchase-orders/creating-purchase-orders)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
