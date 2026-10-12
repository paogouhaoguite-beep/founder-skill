---
name: cash-flow-inventory-planning
description: "Build a dated DTC cash plan for inventory commitments, supplier deposits, receipts and operating outflows. Use to expose funding gaps even when an order or business appears profitable."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=cash-flow-inventory-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Cash Flow Inventory Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=cash-flow-inventory-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Opening available cash by currency/date; payout schedule and reserves; open PO deposit/balance dates; freight/import/receiving payments; payroll/rent/ad charges; refunds/tax liabilities; approved credit availability; merchant minimum buffer.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Map cash by actual expected settlement date, not sales booking or inventory receipt date. Separate restricted reserves and unapproved credit from spendable cash. Record tax and duty payments with evidence without assuming the amount is a final expense.
2. For each period, ending cash = opening cash + actual/expected inflows - due outflows; carry it forward. Within-period timing matters: weekly closing cash can conceal an earlier overdraft, so increase resolution around large commitments.
3. Model base and explicitly assumed delayed-payout, supplier-delay and slower-sales scenarios. Track already committed versus proposed purchase payments to avoid double counting deposits as well as a full balance.
4. Calculate funding gap against the merchant's chosen minimum buffer and the date it occurs. Compare quantity, order timing, negotiated terms and authorized funding alternatives without assuming credit approval. A forecast does not authorize borrowing, moving money, placing an order or changing tax treatment.
5. At each roll, freeze the prior version with forecast as-of time, expected cash date and amount per named receipt/payment. Match actuals by stable document/transaction references. Bridge the difference into receipt/payment timing, amount changes, newly discovered obligations and unresolved items; do not use a general plug. Update remaining expectations explicitly, carry actual closing spendable cash forward and add the next period. Preserve the original forecast for evaluation; overwriting it destroys the comparison. Reconcile overlapping weekly and monthly views instead of assuming either granularity is automatically correct.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Date/week/currency | opening spendable cash | inflows/status | committed outflows | proposed buys | ending cash | buffer gap | scenario/action |
| --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify sales discrepancies](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/sales-discrepancies)
- [Shopify purchase orders](https://help.shopify.com/en/manual/products/inventory/purchase-orders/creating-purchase-orders)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.

The rolling forecast feedback method was adapted with [fixed source records, changes and retained licenses](references/source.md).
