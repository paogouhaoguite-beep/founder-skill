---
name: gift-card-balance-control
description: Use when a DTC merchant needs a masked gift-card balance and issuance
  control.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=gift-card-balance-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Gift Card Balance Control

Built by [ShopChief](https://shopchief.ai/?utm_source=gift-card-balance-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A masked gift-card balance and issuance control. Supply stable card ID, last four characters only, issue date, currency, paid/promotional origin, beginning balance, event IDs and signed amounts, ending balance, enabled/expiry state, and separately authorized issuance request if any.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Remove full redeemable codes from working reports, prompts, URLs and logs. Identify cards by ID plus last four; obtain native balance export or a merchant-prepared ledger, not an assumed full-code export.
2. For each card and currency reconcile beginning balance + issuance/top-ups + evidenced credits − redemptions − evidenced removals = ending balance. Deduplicate event IDs. Initial value minus current balance is not reliable redeemed value when credits or adjustments exist.
3. Report all balances by currency, issue cohort and enabled/expired status; do not silently remove a balance because a card is disabled. Separate paid cards, promotional awards and store credit according to supplied records.
4. Flag apparent expiry, dormancy and stale balances for policy/accounting review. A date or disabled flag alone is not permission to recognize breakage or erase obligations. Do not prescribe expiry law or accounting treatment.
5. For an authorized issuance prepare recipient reference, exact denomination/currency, business reason, duplicate-request key and delivery channel. Verify actual account capability and current native interface; issue only within requested scope and capture masked receipt/status. A refund must not silently become gift-card credit.
6. Compare authorized amount, actual issuance record and delivery receipt separately. Do not generate full codes yourself or reissue after an uncertain timeout before looking up the first attempt.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Card ID / last4 | Origin | Currency | Opening | Credits | Debits | Expected closing | Reported closing | Exception |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
