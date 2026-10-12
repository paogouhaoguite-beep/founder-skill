---
name: wholesale-account-and-quote-review
description: Use when a DTC merchant needs a wholesale company/location and quote-to-order
  readiness review for a DTC brand.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=wholesale-account-and-quote-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Wholesale Account And Quote Review

Built by [ShopChief](https://shopchief.ai/?utm_source=wholesale-account-and-quote-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A wholesale company/location and quote-to-order readiness review for a DTC brand. Supply verified company/contact/location mapping, buyer permissions, effective catalog/pricing/MOQ/terms, quote versions, approved tax handling and account-order ledger.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Identify wholesale accounts using the merchant’s authoritative company mapping or documented role/flag. A company name or arbitrary customer tag alone is not proof of approved wholesale eligibility.
2. Reconcile contacts to company locations and buyer roles. Keep shipping location, billing entity, catalog assignment, payment terms and approval-to-draft setting distinct; one location’s access must not be assumed for all company buyers.
3. Summarize order count/net sales and last order from scoped transactions with refunds/currency/time coverage. Do not assume platform customer fields expose complete lifetime spend or use consumer RFM to grant wholesale privileges.
4. For each quote calculate exact line quantity × quoted unit price, authorized discount, shipping and supplied tax. Check MOQ/pack multiples, currency, validity period, inventory promise and PO reference. Unknown required charge stays unpriced.
5. Trace quote version and buyer acceptance to created order/invoice. A revised quote supersedes prior totals only when accepted; no automatic order creation from a viewed link or company registration.
6. Deliver account-configuration gaps and quote exceptions with owner. No company onboarding, price entitlement, tax exemption, credit or order approval without explicit scope and evidence.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Company/location | Buyer authorization | Catalog/terms | Quote/version | Quantity/pricing checks | Order linkage | Gap/owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
