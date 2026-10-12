---
name: storefront-path-and-eligibility-review
description: Use when a DTC merchant needs a review of account, filter, currency,
  payment eligibility and cross-channel handoffs along a real shopping path.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=storefront-path-and-eligibility-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Storefront Path And Eligibility Review

Built by [ShopChief](https://shopchief.ai/?utm_source=storefront-path-and-eligibility-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A review of account, filter, currency, payment eligibility and cross-channel handoffs along a real shopping path. Supply sampled pages or recordings, shopper task/market/device, approved account/payment/offer rules, basket/variant states and redacted events; browser access is optional.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define concrete paths: guest versus returning account, filter selection/back navigation, currency switch/variant change, eligible payment method and support/pickup handoff. Offline captures support only observed states, not a full interactive acceptance claim.
2. Test filter semantics and state persistence: within/across-group AND/OR as configured, contextual counts, no-result recovery, clear-all, keyboard/focus behavior and URL/back state. Do not impose a generic mobile breakpoint or alter canonical/indexing rules here.
3. For account paths verify the intended guest policy, authorized order visibility and address behavior using test identities. Same email text alone does not authorize linking another person’s orders; never infer account merge capability.
4. For currency/payment paths reconcile shown currency/minor units, variant/cart/checkout amount, actual accepted payment currency and provider-approved installment terms. Preserve presentment and settlement separately; do not apply generic provider fee/eligibility ranges or tell customers financing is guaranteed.
5. Inspect accessible task completion using keyboard, labels, focus, errors and text alternatives with actual observations. Record automated versus manual coverage; this review is not WCAG or legal certification.
6. Trace channel handoffs only via authorized deterministic links or explicit supplied evidence. Preserve unlinked journeys; do not fingerprint customers or infer causation from higher conversion of longer paths. Deliver reproducible defects and proposed copy/state fixes without publishing or payment execution.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Path/state | Market/device | Expected rule | Observed evidence | Blocked buyer task | Proposed correction | Retest |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
