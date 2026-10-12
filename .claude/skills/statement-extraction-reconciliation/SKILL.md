---
name: statement-extraction-reconciliation
description: "Extract statement transactions with page-level provenance and verify balances, row counts and number formats before bookkeeping use."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Statement Extraction Reconciliation

## Inputs and tools
Use original statements with period, currency, account type and printed totals. Prefer a text layer; use OCR for image-only pages and visual verification for uncertain spans. A local PDF/table reader and spreadsheet are sufficient. No bundled upstream extractor is required. Without readable source pages, return an unresolved-row queue, not invented amounts.

## Extraction and proof
Preserve original strings, parsed date/amount, signed convention, page and row or coordinate location. Identify decimal/thousands conventions and debit/credit meaning from the actual statement. Separate transaction rows from headers, balances and subtotals, and split multiple statement periods.

Check independently sourced opening balance + signed transaction sum = printed closing balance. Check every available running-balance transition, page carried/brought-forward continuity, stated debit/credit totals and printed row count. A derived opening balance does not independently verify the first row. Arithmetic alone cannot catch consistent 100× scale errors; compare parsed values with printed locale formatting.

If a check fails, locate the first broken page or running-balance interval. Consider sign reversal (difference twice the amount), duplicate/missing row, decimal shift, column misalignment or incorrect balance transcription as hypotheses. Confirm the actual page before changing any number. Preserve the before/after extraction log and re-run all controls; offsetting errors can hide in final totals.

## Deliver
Return extracted CSV/table, source coordinates, per-control proof, unresolved spans and a qualified status: checked within the available controls or not reconciled. Do not claim a fully proven extraction when control totals are absent. No ledger import or original-file overwrite is authorized by extraction.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=statement-extraction-reconciliation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
