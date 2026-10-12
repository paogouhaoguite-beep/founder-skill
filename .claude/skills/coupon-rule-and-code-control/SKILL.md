---
name: coupon-rule-and-code-control
description: Validate promotion eligibility, stacking and code lifecycle before generating
  or retiring coupon codes. Use for one-time campaigns, bulk codes and stale-rule
  cleanup.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=coupon-rule-and-code-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Coupon Rule And Code Control

Built by [ShopChief](https://shopchief.ai/?utm_source=coupon-rule-and-code-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Promotion rules, currency/timezone, product/customer scope, active dates, minimum/maximum quantities or spend, usage caps, stacking rules, existing codes and campaign commitments. Merchant-approved maximum discount and sample carts.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Translate each rule into an explicit predicate over cart, customer and time. Resolve whether thresholds apply before/after other discounts, whether tax/shipping count, and whether volume tiers are all-units or graduated.
2. Enumerate boundary carts at just below, at and above each threshold. Calculate rule combinations in the actual sequence; additive 10%+20% and sequential multipliers are different. Mark unsupported stack combinations instead of inventing platform behavior.
3. For bulk codes, enforce requested count, allowed format and uniqueness against both the new batch and existing codes. Record usage limit, eligibility and expiry for every generated code; secrets/codes belong only in the merchant deliverable, never public logs.
4. For hygiene, distinguish expired, disabled, unused and contractually promised codes. A zero-use code may be printed on packaging or committed to a partner; investigate before deletion. Prefer disabling within authorized scope.
5. Create the proposal and test matrix. Reconcile actual created/updated counts and identifiers after authorized execution; a timeout is unknown outcome, so look up state before generating replacement codes.

## Deliverable

Deliver a promotion rule matrix, sample-cart results, code manifest and separately approved cleanup queue.

| Code/rule ID | Eligibility | Tier/stack semantics | Expected discount | Usage cap | Time window | Boundary result | Lifecycle action |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
