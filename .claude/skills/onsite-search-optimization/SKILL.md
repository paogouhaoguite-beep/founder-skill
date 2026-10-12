---
name: onsite-search-optimization
description: "Improve a store internal search experience using query logs, result relevance and catalog facts. Use for zero-result queries, synonyms and ranking rules; external search-engine SEO is outside this workflow."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=onsite-search-optimization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# On-site search optimization

> By [ShopChief](https://shopchief.ai/?utm_source=onsite-search-optimization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Diagnose the actual query journey
Inputs are internal search query/event exports, result counts, selected product IDs, catalog/stock/variant data, dates and store language. Optional browsing reproduces selected queries; no search connector is required if exports and screenshots exist. Without logs deliver a bounded relevance audit, not a lost-revenue estimate.

Normalize case/whitespace for grouping but retain the raw query. Do not merge sizes, model numbers or materials that change intent. Remove test/bot queries only with documented evidence. Distinguish no results, irrelevant results, unavailable variants, filter dead ends and successful result clicks. Inspect both high-volume queries and a sample of problematic long-tail queries.

## Propose rules that preserve product truth
Map each query to intent, legitimate synonyms and required product attributes. Use one-way synonyms where equivalence is asymmetric; "waterproof" must not map to "water-resistant" without substantiation. A redirect to a collection is suitable only when the collection satisfies the query. For an unstocked requested item, explain availability and offer genuinely relevant alternatives; do not silently change size/material.

Evaluate ranking against relevance first, then declared stock and merchandising rules. Keep the original ordering and proposed rule per query. Check typo handling, empty query, punctuation, language variants, mobile search overlay, result labels and the return-to-results state. A search result click is not a purchase or proof of relevance.

Deliver a query opportunity table (`query | search sessions | failure evidence | catalog truth | proposed rule | counterexample | owner`), proposed synonym/redirect configuration and a replay set. Metrics use declared units: zero-result search events / all search events, or search sessions with zero results / search sessions; never mix them. Conversion among search users is observational because they self-select.

Save a draft rule set. Publishing a search configuration requires authorized scope; read back the exact query/locale/stock scenarios after a change and retain a rollback copy.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/cro/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/cro/SKILL.md); [coreyhaines31/marketingskills / skills/customer-research/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/customer-research/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
