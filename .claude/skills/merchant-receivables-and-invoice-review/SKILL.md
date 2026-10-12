---
name: merchant-receivables-and-invoice-review
description: Use when a DTC merchant needs an invoice aging, payment allocation and
  credit-exposure review for wholesale sales alongside a DTC store.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=merchant-receivables-and-invoice-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Merchant Receivables And Invoice Review

Built by [ShopChief](https://shopchief.ai/?utm_source=merchant-receivables-and-invoice-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An invoice aging, payment allocation and credit-exposure review for wholesale sales alongside a DTC store. Supply issued invoices and credit notes, dated payments and their allocations, dispute status, approved due-date/discount terms, committed uninvoiced orders, currency, account limits and as-of date.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Preserve invoice/customer/order/PO identifiers and issued-document snapshots. Reconcile quantity × unit price, discounts, supplied tax and total. A confirmation email is not automatically a compliant invoice; compare required fields with the merchant accounting owner’s dated instructions. Keep corrections and credit notes linked to the original instead of silently rewriting it.
2. For each invoice compute open amount = issued amount − applied credits − settled allocated payments. Separate unapplied cash, pending payments and disputed amounts; do not use order paid status as proof of invoice allocation. Trace negative balances and duplicate document or payment references.
3. Compute overdue days from the agreed due date to as-of date, with not-yet-due separate. Apply merchant-selected aging buckets to open balances, never original invoice face value. Missing due date is unknown, not current.
4. Compute proposed credit exposure from open receivables plus committed uninvoiced orders without counting the same obligation twice. Compare a proposed new order with the supplied limit; this is an exception request, not an inferred creditworthiness score.
5. For an early-payment offer use its exact eligible basis and payment timing. Cost of receiving cash sooner is discount/(eligible amount−discount), with a labeled simple annualization ×365/days accelerated. Compare actual financing alternatives; never assert a 2% discount is always cheaper than borrowing.
6. Draft a specific payment query/reminder only for reconciled, undisputed overdue balances using merchant tone and approved cadence. Return evidence and owner for disputed or unapplied amounts; do not send, change terms, write off or release credit holds automatically.
7. Group reminder-eligible invoices by verified customer and currency into one statement. Read prior contact stage/date, promised payment and dispute before drafting; repeated runs must not resend the same stage. Preserve each invoice balance and hold the reminder when unallocated cash could settle it. A proposed cadence does not authorize scheduled sends.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Account/invoice | Currency | Issued | Credits | Settled allocated | Open | Due date/age | Dispute | Proposed action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
