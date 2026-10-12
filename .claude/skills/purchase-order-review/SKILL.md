---
name: purchase-order-review
description: "Reconcile a draft DTC purchase order against an approved quote, variants, commercial terms and delivery plan before sending or accepting changes."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=purchase-order-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Purchase Order Review

Built by [ShopChief](https://shopchief.ai/?utm_source=purchase-order-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Draft PO/version; approved supplier quote and specification; SKU/variant quantities; case packs and prices; currency/tax treatment; freight/tooling; deposit/balance terms; ship-to, lead-time milestones and receiving plan.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Match line identifiers, units of measure and specifications to the approved quote. Compare ordered units with required full cases; list changed lines rather than silently rewriting a PO.
2. Recalculate extensions, charges, discounts and document total. Establish the base for each deposit and balance; show payable dates and conditions. Do not assume every deposit applies to freight or tax.
3. Compare quantity/price/date changes with approval scope and document revision. Detect duplicate PO numbers or overlapping supplier acknowledgments. Shipment, accepted receipt and supplier invoicing can differ; keep reconciliation states separate.
4. Deliver a redline register and send-ready draft when requested. Open quality, duty or cancellation clauses remain explicit issues. A PO draft is not sent, contractually accepted, paid or received. External sending, acceptance and payment each need the corresponding scope.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| PO/line | quote reference | SKU/spec | quantity/UOM | unit price | extension | variance | term/due date | blocker | proposed correction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify purchase orders](https://help.shopify.com/en/manual/products/inventory/purchase-orders/creating-purchase-orders)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
