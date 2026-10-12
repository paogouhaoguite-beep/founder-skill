---
name: tax-records-and-configuration-review
description: Use when a DTC merchant needs a tax collection evidence schedule and
  configuration exception review.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=tax-records-and-configuration-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Tax Records And Configuration Review

Built by [ShopChief](https://shopchief.ai/?utm_source=tax-records-and-configuration-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A tax collection evidence schedule and configuration exception review. Supply transaction/refund tax lines with event dates, destination, product tax class, shipping tax, rate identifiers, currencies, configuration export including postal/city/priority/compound predicates, and merchant-approved current jurisdiction guidance.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define collected-tax event period and timezone, distinguishing sale date from refund event date. Include partial-refund tax lines and prior-period sales refunded now; do not subtract the entire order based on its current refunded status.
2. Aggregate signed product and shipping tax by rate/jurisdiction identifiers and currency. Deduplicate event IDs, show unknown tax allocations and reconcile order tax totals against line totals without counting shipping tax twice.
3. Prepare configuration test cases using actual destination/postcode, product tax class, tax-inclusive/exclusive display, shipping tax, exemption evidence and compound priority. These are configuration observations, not a determination of legally applicable rates.
4. Identify overlapping predicates only after comparing all location, class, priority and compound settings. Multiple rates in one state may be intentional; do not automatically delete a lower-priority rate.
5. Compare configured expected amounts only with merchant-provided dated authority or qualified adviser instructions. Record jurisdiction, effective date, unresolved applicability and owner. Never infer nexus registration, exemptions, filing deadlines or retroactive liability from generic thresholds.
6. Reconcile transaction sync evidence in the tax provider, distinguishing committed sale, partial credit and cancellation/void. A partial refund is not automatically a full void. Deliver to the merchant tax owner; do not register, file or remit.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Jurisdiction/rate ID | Currency | Sale tax | Refund tax | Net recorded tax | Coverage gap | Config evidence | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
