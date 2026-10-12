---
name: merchant-spreadsheet-question-answering
description: "Answer a specific merchant data question with a declared metric, reproducible filtering and an evidence trail to source rows."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Spreadsheet Question Answering

## Define before calculating
Collect the question, source exports, observation date, timezone, currency and relevant status/refund definitions. A spreadsheet calculation is sufficient; SQL or dataframes are optional. If a decisive definition is unknowable, show the alternatives and ask for the needed field rather than choose silently.

## Evidence pipeline
Profile each sheet’s grain, keys, hidden rows, totals/footer rows, text-stored numbers, dates and missingness. Exclude summary rows from detail sums with an explicit rule. Preserve identifiers and keep currencies separate without a documented conversion basis.

Write the metric contract: numerator, denominator, eligibility, period boundary, event date basis and refund treatment. Apply cleaning, filtering, joins, derivation and aggregation as separately logged steps. Check row counts, join fanout and unmatched records after each step. Distinct orders, customers and sessions are different units.

Reconcile the result to a trusted control or explain why no control exists. Hand-check a small set of contributing and excluded rows. Do not average group averages when group sizes differ; compute totals at the required grain. Unknown or unparseable amounts are not zeros.

## Deliver
Give the actual answer, unit/window, calculation/query or spreadsheet formula, filter log, row counts, contributing-row reference and limitations. If data is insufficient, deliver a bounded result and exact missing fields. Read-only analysis does not authorize changing source values or publishing a dashboard.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-spreadsheet-question-answering&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
