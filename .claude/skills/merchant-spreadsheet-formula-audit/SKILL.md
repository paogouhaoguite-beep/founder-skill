---
name: merchant-spreadsheet-formula-audit
description: "Review a merchant workbook\u2019s formulas, dependencies, scenario behavior and controls without silently rewriting the model."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Spreadsheet Formula Audit

## Inputs
Require the workbook, intended decision, formula/cached-value access, expected results, input definitions and target application. If only screenshots or values exist, state that formula inspection is limited. Preserve the original and keep suggested repairs in a separate copy or issue register.

## Audit passes
Inventory sheets, hidden ranges, named ranges, external links, formulas, inputs and overrides. Trace decision outputs back to assumptions and source data. Check unit/currency/period consistency, sign conventions, denominator definitions, range boundaries and copied-formula patterns. A different formula may be intentional; verify before calling it a defect.

Compare formulas with cached values and actual recalculation status. Check missing inputs, suppressed errors, circularity, brittle references, totals, scenario switches and cross-sheet links. Inspect boundary cases such as zero volume, negative margin, missing dates and partial periods.

Independently recompute a small decision-critical fixture, including row values and totals. Perform sensitivity checks: changing one input should affect only justified dependent outputs. A reasonable-looking result is not evidence the formula is right.

## Deliver
Return cell/range, observed formula/value, expected logic, evidence, impact, severity and minimal proposed fix. Distinguish confirmed calculation errors from unsupported assumptions and untested behavior. If repair is authorized, log before/after values, recalculate and rerun affected controls; do not claim the entire workbook is correct from a few checks.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-spreadsheet-formula-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
