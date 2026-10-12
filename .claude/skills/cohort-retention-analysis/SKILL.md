---
name: cohort-retention-analysis
description: "Build repeat-purchase cohorts with explicit observation windows, stable customer identity and censoring. Use for customer return behavior over time; subscription churn and projected lifetime value require separate models."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=cohort-retention-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Commerce cohort retention analysis

> By [ShopChief](https://shopchief.ai/?utm_source=cohort-retention-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Fix the cohort definition
Read order/customer keys, order and refund timestamps, status, currency, observation cutoff and available history start. Use CSV/SQL exports locally; authorized data access is optional. Missing stable customer identity prevents person-level retention: do not substitute email guesses or treat every order as a new person.

Define first eligible purchase and cohort grain, timezone, returns/cancellations treatment and period style. Calendar months and rolling days since acquisition answer different questions; choose one explicitly. A customer first seen after an incomplete history start is newly observed, not proven newly acquired.

## Build the denominator once
Deduplicate orders and join customers consistently. For each cohort show original eligible customer count. Count each customer at most once per activity period regardless of orders. Define retention as a subsequent eligible purchase within that period divided by the original cohort population that has fully reached that observation age. For a fully mature cohort this is the fixed original size; disclose partial eligibility if using individual rolling windows.

Keep period retention (purchase during period), cumulative repeat (any second purchase by age) and continuous survival distinct. Someone absent in month 1 may buy in month 2; ordinary retail absence is not permanent churn. Blank future/unmatured cells are censored, not zero. Compare cohorts only at the same mature age and note promotion/category/seasonality composition.

## Deliver inspectable analysis
Return data-quality exclusions, cohort/customer denominators, count matrix, rate matrix and optional heatmap with masked incomplete cells. Show whether row 0 denotes acquisition rather than repeat. Break down by acquisition product/channel only when attribution fields are trustworthy; small segments remain descriptive without invented significance.

Provide evidence-based patterns, alternative explanations and a follow-up research question. Do not infer why customers left from a curve alone. Any generated script should preserve raw input and allow the cutoff/definitions to be reproduced. Contacting customers or enabling retention campaigns is a separate authorized action.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [phuryn/pm-skills / pm-data-analytics/skills/cohort-analysis/SKILL.md](https://github.com/phuryn/pm-skills/blob/8607e3b077817f89bf4a9b623246219734ac3be0/pm-data-analytics/skills/cohort-analysis/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
