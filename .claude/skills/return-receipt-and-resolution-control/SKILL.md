---
name: return-receipt-and-resolution-control
description: Use when a DTC merchant needs a return case register from request through
  physical disposition and resolution.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=return-receipt-and-resolution-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Return Receipt And Resolution Control

Built by [ShopChief](https://shopchief.ai/?utm_source=return-receipt-and-resolution-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A return case register from request through physical disposition and resolution. Supply fulfilled line quantities, previous returns, request/authorization/receipt/inspection/refund/exchange event times, merchant policy and clock definition, case IDs and destination.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Validate each requested unit against fulfilled and already-returned quantities; partially fulfilled orders can have eligible fulfilled lines. A custom order status or note is only a case record, not proof that a return label, refund or physical return exists.
2. Track request, approval, in-transit, receipt, inspection and resolution separately. Assign RMA/case ID and match warehouse receipt by original line/lot; prevent duplicate receipts and duplicate stock credits.
3. Classify received units into sellable, quarantine, repair and disposal with inspection evidence. Customer-stated reason alone does not authorize available stock increase. Preserve missing variant/location as unresolved.
4. Classify resolution at line/amount level: exchange, cash refund, credit, mixed, rejected or pending. A return containing one exchange is not wholly exchange; show denominator and unresolved cases for ratios.
5. Compute separate request-to-authorization, receipt-to-inspection and eligible-start-to-resolution clocks using merchant calendar/pause rules. Report completed duration alongside open-case age; do not drop open overdue cases or label all returns refunded.
6. Deliver case work queue and quantity/value control totals. Authorization, labels, notifications, refunds and stock releases are separate scoped actions with actual receipts.
7. Map return label requested/created/used, parcel receipt, inspection disposition and customer refund/exchange as separate events, with actual policy triggers. An unused label is not a returned item; a refund can follow a specifically approved instant-refund policy and must not be categorically forced to receipt. Keep authorized customer status drafts consistent with actual event evidence.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Case/line | Requested/received | Disposition | Resolution components | Clock start/end | Open age | Owner/action |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
