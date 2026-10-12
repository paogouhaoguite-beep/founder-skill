---
name: merchant-data-quality-controls
description: "Audit merchant analysis inputs and define actionable quality controls for completeness, keys, freshness, joins and metric interpretation."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Data Quality Controls

## Inputs
Collect datasets and grain, data dictionary, expected arrival cadence, business-valid ranges/statuses, reference totals, owners and the decisions consuming them. Local tables are sufficient. No dbt installation is required; deliver checks as a specification or simple spreadsheet queries.

## Controls with consequences
Profile missing values, uniqueness, parsing, distributions, outliers, date coverage and referential integrity. Compare expected versus observed rows and source timestamps; a recent file timestamp does not prove the latest business events arrived. Check known rules without assuming negative revenue or zero-priced orders are always invalid.

For each check, define population, numerator/denominator, tolerance chosen for the business, severity, owner and response. Distinguish blocking identity/total failures from review-worthy distribution changes. Do not use universal percentage thresholds or infer a missing-data mechanism such as MCAR from null rates alone.

Before sharing analysis, verify comparable periods and populations, stable denominator definitions, timezone boundaries, join cardinality and refund/status treatment. Look for survivorship, selection bias and incomplete-period comparisons. Outliers may be real important orders; investigate before deletion. Average-of-averages and duplicated parent totals require recalculation at the correct grain.

## Deliver
Return the profile, rule register, failing rows/counts, downstream impact and revised analysis status: ready, ready with specified caveats, or needs correction. Controls are not proof that every real-world fact is accurate. Do not change records, block a production pipeline or export personal data without authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-data-quality-controls&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
