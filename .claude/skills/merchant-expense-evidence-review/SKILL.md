---
name: merchant-expense-evidence-review
description: "Match merchant expense receipts to statement rows, verify extracted amounts and prepare a policy-based review queue."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Expense Evidence Review

## Intake
Collect receipt images/PDFs, statements, expense exports, currency, company policy and chart of accounts. Use OCR or manual transcription with a row-level confidence flag; no third-party scripts are bundled. Keep originals and source locations. An illegible amount is unknown.

## Evidence workflow
Inventory files, identify duplicates and distinguish invoices, receipts, statements and credit notes. Extract date, merchant, invoice/receipt reference, line totals, tax, currency and payment evidence. Check line/subtotal/tax/grand-total arithmetic without silently correcting the source.

Match receipts to statement charges by stable references and constrained amount/date/counterparty, allowing documented split or combined payments. Multiple plausible matches remain unresolved. Separate missing receipts, unrecorded receipts, true duplicate charges and duplicate file copies. Do not call a repeated monthly charge fraud.

Propose categories based on transaction substance and the merchant’s chart. Compare expenses to actual policy with evidence for exceptions; do not invent limits. Record foreign-currency amount and actual settlement amount/fees separately, using a documented rate only when needed. Tax deductibility and capitalization are accountant questions, not automatic labels.

## Deliver
Return expense register with source file/page, date, original and settlement currency, amount, proposed category, matched statement ID, evidence status and policy exception. Summarize supported totals by currency and missing-document value separately. Draft queries if needed; do not send, reimburse, post entries or delete files without authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-expense-evidence-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
