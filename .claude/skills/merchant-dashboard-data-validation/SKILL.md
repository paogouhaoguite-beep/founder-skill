---
name: merchant-dashboard-data-validation
description: "Specify and validate dashboard measures at the correct data grain, filter context and grand-total semantics."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Dashboard Data Validation

## Model contract
Obtain the BI platform/version, table grains, keys, relationships, date/calendar policy, formula, visual rows/columns and filters. A platform-neutral metric specification plus hand calculation is the fallback; do not invent connector availability or claim a formula ran.

## Source and dashboard contract
Document every source grain, refresh timestamp, timezone, currency and owner. Define numerators, denominators, exclusions and attribution model before designing the chart. Preaggregate compatible sources to a common grain; retain separate panels if an allocation or valid join is unavailable. Reconcile each source total before and after blending, checking join cardinality. Filters must apply to intended numerator and denominator populations consistently, ratio totals recompute from totals, and stale/unavailable sources must remain visibly stale or unavailable. A mockup does not prove a live refresh.

## Context-first analysis
State what one visual cell includes and what the total should mean. Distinct-customer counts, percentages and inventory balances are often nonadditive: totals may require recomputation rather than summing rows. Identify many-to-many relationships and repeated parent values before writing measures.

Choose implementation for the actual engine. In DAX, explain filter replacement/intersection, row versus filter context and date relationships. In Tableau, distinguish row calculations, LOD expressions and post-aggregation table calculations; check relevant filter order. In Looker, state measure grain, join fanout and where aggregation occurs. Verify current syntax against the installed version before delivering executable code.

Construct a small fixture that includes duplicate entities across groups, nulls, zero denominators and relevant filters. Calculate expected cell and total values independently, then compare with the engine if available. For balances, define last valid snapshot within the period rather than summing daily stock. Review performance only after semantic correctness, documenting high-cardinality iteration or expensive context operations.

## Deliver
Return metric definition, relationship/context diagram in text, proposed formula or pseudocode, hand-check table and runtime status. Do not publish a model or change relationships without authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-dashboard-data-validation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
