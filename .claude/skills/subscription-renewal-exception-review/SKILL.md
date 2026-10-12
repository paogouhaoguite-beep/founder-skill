---
name: subscription-renewal-exception-review
description: Use when a DTC merchant needs a renewal, payment and fulfillment exception
  queue.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=subscription-renewal-exception-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Subscription Renewal Exception Review

Built by [ShopChief](https://shopchief.ai/?utm_source=subscription-renewal-exception-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A renewal, payment and fulfillment exception queue. Supply subscription/customer IDs, plan and price versions, next renewal dates/timezone, cancellation or pause requests, invoice/payment attempts, entitlement and shipment records, and the merchant-approved retry/proration/notice policy.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map the subscription, renewal invoice, payment attempt and shipment as separate objects. A subscription marked active does not prove this renewal was paid or shipped; retain stable IDs and event times.
2. Build the ordered timeline for each renewal: scheduled charge, actual attempt, provider result, cancellation/pause request, effective change and fulfillment. Detect duplicate attempts, unknown outcomes and paid renewals with no shipment without treating expected future events as missing.
3. Compare effective cancellation/pause time with the authorized renewal cutoff and actual charge time. Where timezones or policy versions conflict mark review required; do not invent a universal cancellation or cooling-off rule.
4. For a plan change calculate a preview only from supplied billing basis and exact remaining units of service. Separate service-time credit from physical goods already fulfilled, fees and taxes. Never impose a SaaS daily proration formula on a box of goods.
5. Prepare retry candidates only for documented retryable failures within the approved schedule, excluding pending or successful attempts and stopped subscriptions. A card token or consent must stay in its secure system; do not request or display it.
6. Deliver exception owner, proposed remedy and evidence. Charging, cancellation, refunds, replacement shipments and customer notices each require their authorized scope and a receipt/readback; an uncertain charge must be looked up before retry.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Subscription | Renewal/invoice | Charge evidence | Effective state | Shipment | Exception | Proposed remedy | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
