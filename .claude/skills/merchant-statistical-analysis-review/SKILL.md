---
name: merchant-statistical-analysis-review
description: "Analyze merchant distributions and comparisons with explicit assumptions, uncertainty and limits beyond a simple significance label."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Statistical Analysis Review

## Study contract
Collect the decision, observational unit, population, data window, sampling/assignment mechanism, outcomes and planned comparisons. Use trusted statistical tools when available; descriptive calculations and a method plan are the fallback. Never fabricate a p-value or confidence interval without calculation.

## Describe then infer
Inspect data quality, missingness, censoring, skew, repeated customers and outliers before selecting a method. Report sample size and an appropriate center/spread; revenue may need both mean and median because tails matter. Zero, negative and bounded metrics need appropriate treatment. Do not infer normality or randomness merely from a large sample.

Define the estimand and comparison: difference in means, proportion, median or relationship. State assumptions, independence/unit of assignment, unequal variance and any clustering. Choose parametric, exact, rank-based or resampling methods according to the actual question and assumptions; a nonparametric test is not automatically a test of medians.

Report effect size and uncertainty alongside any test result, with method, confidence level and multiplicity treatment. A confidence interval is not a probability statement about the realized parameter; a nonsignificant test is not proof of no difference. Observational association does not establish causation. Pre/post changes can reflect seasonality and selection.

For prospective comparisons, state baseline, absolute or relative minimum detectable effect, alpha, desired power, allocation and clustering before computing sample size. Translate the required independent units into feasible traffic and calendar time. Predeclare stopping and multiplicity handling; extending a fixed-horizon test after seeing its p-value requires a valid revised design rather than a casual “collect more until significant”. Separate practical business materiality from statistical detectability.

## Deliver
Return data summary, method rationale, calculation or reproducible code, effect/interval if computed, sensitivity checks and decision limitations. If there is insufficient information, state what would permit inference rather than invent a universal sample threshold.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-statistical-analysis-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
