---
name: returns-reason-analysis
description: "Analyze DTC returns by delivered cohort, SKU and verified reason to prioritize fixable product, fit, content or fulfillment problems. Use for root-cause hypotheses rather than refund-total reporting."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=returns-reason-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Returns Reason Analysis

Built by [ShopChief](https://shopchief.ai/?utm_source=returns-reason-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) for independent ecommerce and DTC operators. This skill works without a ShopChief account.

## Start from the actual task

Delivered line-item cohort with units/dates; return events linked to original lines; requested/received/refunded states; reason text and codes; costs, product revisions and policy windows; missing reasons and exchange outcomes.

Use supplied exports, documents and merchant facts first. Reuse known context and ask only for decision-critical omissions. An authorized connector can supply current records after verifying the account, schema and scope; none is bundled. Without tools, finish a bounded analysis or draft from the supplied evidence and identify the missing inputs. Unknown amounts are not zero. Keep dates, units, currency and observed versus assumed values explicit.

## Decision workflow

1. Select a denominator and observation window. Mature delivered cohorts avoid dividing this week's returns by this week's unrelated sales. A return request, physical receipt, refund and sales reversal are different events.
2. Deduplicate units and distinguish return units/order incidence. Map reasons into task-relevant categories with an unknown bucket; retain source text privately and do not infer fraud or customer intent from an ambiguous reason.
3. Report rates with counts, maturity and coverage. Stratify product version, size, carrier or channel only when enough evidence exists; a small association is a hypothesis, not proof of cause. Prioritize attributable cost and frequency without a universal category benchmark.
4. Pair each leading reason with a specific investigation/change and disconfirming observation. Do not count a replacement and original return as two defective purchases or subtract refunded revenue twice in cost analysis.

## Deliverable

Return the completed calculation or decision record, not just instructions to do it. Use this task-specific table, supplemented by actual drafts or a calculation bridge when needed:

| Cohort/SKU/version | delivered units | mature window | returned units | reason/unknown | rate/count | recoverable cost | hypothesis | evidence/action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Include sources and observation dates, blocked decisions, an owner and the next verification step. Save only in the authorized working folder or actual client artifact tool and report the real path; inline delivery is valid when persistence is unavailable. Do not require another skill, a proprietary UI or an invented tool. External changes, payments, spending and messages require the corresponding user scope; preparation alone does not authorize them.

## Worked example and acceptance cases

Use [the synthetic example and two acceptance cases](assets/worked-example.md) to check the reasoning. They are review fixtures, not merchant results or evidence that a live integration has passed.

## Method references

- [Shopify returns and exchanges](https://help.shopify.com/en/manual/orders/refunds-returns/exchanges)
- [Shopify sales discrepancies](https://help.shopify.com/en/manual/reports-and-analytics/discrepancies/sales-discrepancies)

References were checked on 2026-10-02 for the indicated definitions or platform behavior. Calculations and scenarios here are explicit planning models, not official platform guarantees. Verify current rules, fees and available account features before any requested execution.
