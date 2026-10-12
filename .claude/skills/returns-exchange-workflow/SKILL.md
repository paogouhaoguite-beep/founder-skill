---
name: returns-exchange-workflow
description: "Design or carry out an authorized DTC return or exchange using actual order, policy, payment and inventory states. Use for an auditable case workflow, keeping approval, receipt, refund and restock separate."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=returns-exchange-workflow&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Returns Exchange Workflow

Built by [ShopChief](https://shopchief.ai/?utm_source=returns-exchange-workflow&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Order/line/quantity and payment IDs; current fulfillment and previous returns/refunds; policy version shown at purchase; market and dates; customer request; replacement stock/location; fees and tax/shipping evidence.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Establish eligibility from the actual policy and relevant current official rules where legal questions arise. Highlight ambiguity for review rather than inventing an entitlement or denying a right from an internal policy alone.
2. Model each transition: requested → reviewed → authorized → in transit → inspected → disposition; separately track financial settlement and replacement fulfillment. Physical inspection can place goods in unavailable stock; receipt does not imply sellable restock.
3. Compute settlement from the original allocated net line amount, applicable shipping/tax adjustments, permitted fees and replacement charge. Track refundable balance and previous settlements to prevent duplicate refunds. Store credit and cash are distinct outcomes.
4. Prepare a case-specific action preview. Issue labels, send customer messages, refund, collect payment or dispatch a replacement only within actual authorization. Before retries read back transaction and return status; do not repeat a monetary action on timeout.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Case/order/line | requested units | eligibility evidence | physical state | original credit | replacement debit | net settlement | stock disposition | action/status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify returns and exchanges](https://help.shopify.com/en/manual/orders/refunds-returns/exchanges)
- [Shopify inventory states](https://help.shopify.com/en/manual/products/inventory/fundamentals/inventory-states)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
