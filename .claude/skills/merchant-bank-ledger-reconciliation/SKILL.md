---
name: merchant-bank-ledger-reconciliation
description: "Reconcile bank statement balances to the bookkeeping ledger with explicit timing items and no balancing plugs."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Bank Ledger Reconciliation

## Evidence required
Obtain each account’s statement opening/closing balance and dates, statement rows, ledger balance and rows back to the oldest uncleared item, chart of accounts and previous reconciliation. Cash, card and loan accounts may use different sign conventions. A spreadsheet is enough; no source scripts are bundled. An incomplete feed cannot substitute for a bank statement’s printed balances.

## Reconcile
Normalize both sides to a documented signed convention and currency, preserving raw values and IDs. Deduplicate proven imports, not recurring identical payments. Match by stable references first, then constrained amount/date/counterparty candidates, recording ambiguous matches rather than choosing the nearest date.

Identify deposits in transit and outstanding payments, including those originated before this month. Separate timing items from book omissions such as bank fees or duplicated entries. Transfers between merchant-owned accounts require paired evidence and are not sales revenue. Batched deposits may match several transactions; document the bridge without double counting processor fees.

Build two independent proofs: adjusted bank balance after valid timing items, and adjusted book balance after supported proposed corrections. Display any unexplained difference. Do not delete rows, force a suspense entry or “plug” cash to balance. Tax-sensitive coding and stale items go to the accountant.

## Deliver
Provide reconciliation bridge, matched rows, aged reconciling items, missing evidence and proposed journals with debit/credit, amount, source, preparer and reviewer. Posting journals or marking a platform reconciled is outside a preparation request. State which accounts and periods were not verified.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-bank-ledger-reconciliation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
