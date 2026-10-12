---
name: refund-and-replacement-control
description: Use when a DTC merchant needs a line-level refund and replacement proposal.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=refund-and-replacement-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Refund And Replacement Control

Built by [ShopChief](https://shopchief.ai/?utm_source=refund-and-replacement-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A line-level refund and replacement proposal. Supply captured tenders, prior refunds, refundable item quantities, discounts/tax/shipping allocation, return disposition, requested replacement items/prices and intended payer, with operation authorization.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Reconcile original captured funds minus prior successful refunds by tender and currency. Pending refunds remain pending exposure; order total alone is not remaining refundable cash.
2. Select only requested quantities and allocate actually paid discounted line amounts and supported tax/shipping credits. Compare requested quantities against remaining eligible quantities and total refund against remaining tender amount. Resolve rounding at minor-unit precision.
3. Decide cash refund, ledger-only correction and store credit separately; verify gateway capability before claiming money moved. Do not substitute store credit or retry an uncertain gateway request silently.
4. Prepare replacement as an independent draft: exact requested variant/quantity, current authorized price, tax/shipping treatment, address and inventory. Do not copy every original item or mark paid from the old payment method.
5. Restock only after physical receipt/inspection establishes sellable units; replacement shipment and refund are not receipt evidence. Preserve original and replacement IDs in an audit record.
6. Execute only individually authorized refund/replacement operations, using current native interface or verified connector. Record gateway transaction, actual refunded amount and replacement draft status; a draft/invoice is not payment or shipment.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Original order/line | Remaining quantity | Captured less prior refunds | Proposed refund | Restock evidence | Replacement draft | Actual outcome |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
