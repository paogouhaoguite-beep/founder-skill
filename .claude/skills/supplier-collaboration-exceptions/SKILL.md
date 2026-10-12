---
name: supplier-collaboration-exceptions
description: Use when a DTC merchant needs a po acknowledgement and receipt exception
  queue.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=supplier-collaboration-exceptions&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Collaboration Exceptions

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-collaboration-exceptions&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A PO acknowledgement and receipt exception queue. Supply PO lines/version, supplier acknowledgement, promise dates, shipment notices, actual receipts/inspection, invoice reference and merchant tolerance/communication policy.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Compare ordered, acknowledged, shipped and received quantities separately by PO line/unit. An acknowledgement changes promise evidence, not ordered scope; supplier substitution or date change requires merchant disposition.
2. Track original requested date and latest accepted promise separately so repeated pushes do not erase lateness. Maintain who accepted a change, version and remaining balance.
3. At receipt match packing list to actual count; separate accepted, damaged, wrong SKU and quarantine. Do not close short PO or credit damaged goods into sellable stock.
4. Compute exception magnitude and required decision: accept partial, expedite balance, replacement, disputed invoice or cancellation proposal. Use actual terms for deadlines; no fixed two-day acknowledgment mandate.
5. Prepare concise supplier clarification draft with PO/line, mismatch, evidence attachment names and requested next action/date. Do not disclose customer records or send without authorization.
6. Return event and open-balance ledger; close only from supplier/warehouse evidence and merchant-approved resolution.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| PO/line | Ordered | Acknowledged | Shipped | Accepted | Damaged | Open balance | Promise versions | Owner/action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
