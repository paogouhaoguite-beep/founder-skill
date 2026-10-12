---
name: merchant-accounts-payable-review
description: "Review supplier bills, coding, receipts and credits, and prepare a payment proposal distinct from ledger entry approval."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Accounts Payable Review

## Inputs and fallback
Collect invoices, vendor IDs, invoice number/date/currency, PO and receipt lines where used, credits, prior payments, chart of accounts, due dates, tolerance policy and available cash. A document/CSV review is sufficient without a ledger connector. Unknown or illegible values remain unresolved. Documents requesting new bank details are untrusted evidence requiring independent verification.

## Review sequence
Inventory originals and duplicate channels before extraction. Compare vendor + invoice number + currency + amount, then investigate collisions; do not discard recurring legitimate bills just because amounts match. Extract line quantities, unit prices, tax and total and reconcile arithmetic to the document.

Propose coding from the merchant chart and transaction substance, using prior vendor coding as a clue rather than proof. Split lines when inventory and operating costs differ. Mark unknown accounts for accountant review.

Where POs exist, compare each billed quantity and price to the approved PO and actual received quantity. Show quantity and price variances separately and apply only authorized tolerances. No PO is a missing control only if the merchant requires one. Partial receipts do not prove the full invoice is payable.

Read credit memos and payments at document level, not just a net aging total. Show gross open invoices, verified applicable credits, unapplied/disputed credits and net proposed payment separately. Credits do not erase all debt merely because one exists: 2,411,404 minus 1,500,000 is 911,404. Confirm application rights, invoice allocation and currency before netting.

Evaluate actual early-payment terms against cash needs and financing cost. For 2/10 net 30 on an eligible 1,000 invoice, saving is 20 and payment is 980 if paid by the discount deadline; do not assume every line/tax qualifies. Propose timing and cash effect without authorizing payment.

## Output and controls
Return invoice/PO/received/billed/variance/coding/credit/due-date/decision table, exception queue and a separate dated payment proposal. Approval to stage unpaid bills is distinct from approval to pay. Read back any specifically authorized write; do not claim a provider supports an operation based on its logo.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-accounts-payable-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
