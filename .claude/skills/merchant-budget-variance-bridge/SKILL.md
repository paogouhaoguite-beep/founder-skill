---
name: merchant-budget-variance-bridge
description: "Explain merchant budget versus actual results with a reconciled price-volume bridge and evidence-based timing classifications."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Budget Variance Bridge

## Inputs
Use budget and actuals on the same accounting basis, period, currency and account/SKU grain. Request units and realized net prices for revenue analysis, plus known promotions, returns and timing items. A spreadsheet or supplied table is sufficient; absent drivers remain unexplained rather than invented.

## Calculation
For each line, variance = actual − budget. Define favorable/unfavorable separately for income and expense. Percentage variance uses the stated budget denominator; for zero budgets report the absolute change and mark percentage undefined. Agree materiality in absolute and relative terms with the merchant rather than applying a universal threshold.

For comparable SKU rows, choose a bridge convention and show it: volume effect = (actual quantity − budget quantity) × budget price; price effect = actual quantity × (actual price − budget price). Their sum exactly reconciles row revenue difference. For portfolio mix analysis, disclose the common volume/mix definition and avoid counting SKU-level volume effects again as a separate mix increment.

Investigate material differences using invoices, order data, promotion dates or staffing records. Classify a timing difference only when the displaced period and supporting event are known. Structural, volume and one-off labels require evidence; residual unexplained effects stay visible. Separate a proposed reforecast from the approved budget.

## Deliver
Return actual/budget/absolute/percent/favorability table, driver bridge, evidence, recurring-versus-timing assessment, owner and revised scenario impact. Missing data is not zero. This management analysis does not authorize accounting corrections or budget changes.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-budget-variance-bridge&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
