---
name: ai-search-visibility-audit
description: "Measure brand mentions, recommendations and citations across a fixed set of buyer questions and repeated AI-search observations. Use for an AI visibility baseline or before/after study; site-wide technical SEO and schema implementation are separate tasks."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=ai-search-visibility-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# AI search visibility study

> By [ShopChief](https://shopchief.ai/?utm_source=ai-search-visibility-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Define the observation, then measure
Get the store domain and brand aliases, selling market/language, product category, priority buyer questions, target answer surfaces, and dates. Establish a fixed query set covering category discovery, fit questions, comparisons, and branded support; do not pad it with invented demand. Freeze wording and competitor entities before comparing runs.

Use an available authorized browser/API for each named surface. Record the actual model/surface, search on/off, region, language, date, login/personalization context and run number. Search-engine results are a retrieval proxy, never a transcript of ChatGPT, Gemini or Perplexity. If the surface is unavailable, accept exported answers/screenshots with provenance or mark that surface unobserved.

## Evidence ledger
For each query-run, save the answer artifact and separately code: brand mentioned; explicitly recommended for a use case; own-domain URL cited; third-party URL discussing the brand cited. Resolve citations to actual URLs where accessible. A named brand without a link is not a citation. A failed request, empty answer and a valid answer with no brand are three different states.

Compute each rate as positive eligible observations / successful eligible observations for the same platform, intent and window. Show numerator, denominator, failed/omitted runs and both per-run and per-query coverage. If repetitions differ, show per-query rates before aggregation so frequently repeated queries do not dominate. These are sampled visibility rates, not market share or stable rankings.

## Turn observations into work
Inspect the cited pages and the merchant's relevant pages for verifiable product identity, fit facts, original evidence and answers to the sampled questions. Tie each content recommendation to a specific missing buyer answer. Check crawler policy only against current provider documentation; training opt-out and search retrieval are separate. A robots change, llms.txt file or schema addition cannot be presented as a guaranteed citation fix. Broad crawlability and schema remediation belong in a separate scoped audit.

Deliver the frozen query sheet, observation ledger, rates by platform/intent, evidence-linked gaps and a repeatable follow-up protocol. Compare like-for-like cohorts after a content change; record simultaneous product/model changes as confounders. Publishing content or altering crawler rules requires the user's actual scope. No synthetic searches, paid calls or recurring jobs are implicitly authorized.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [maxbuildog/skills / skills/ai-answer-audit/SKILL.md](https://github.com/maxbuildog/skills/blob/13a0d2ff54699e44455fd19c942a917def6fae19/skills/ai-answer-audit/SKILL.md); [coreyhaines31/marketingskills / skills/ai-seo/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/ai-seo/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
