---
name: merchant-review-mining
description: "Code merchant-supplied or publicly accessible product reviews into evidence-backed fit, quality, delivery and expectation themes. Use for research synthesis, not review solicitation or writing final marketing claims."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=merchant-review-mining&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Merchant review mining

> By [ShopChief](https://shopchief.ai/?utm_source=merchant-review-mining&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Build a usable corpus
Read reviews with stable record ID, product/variant, date, rating, text, source and verification status if supplied. Accept CSV/JSON/text; browsing is optional for bounded public sources. Do not bypass login, purchase a dataset or harvest personal profiles. If supplied text lacks dates or product IDs, label those dimensions unavailable instead of assigning them.

Set the research question and window. Deduplicate syndicated text and repeated reviewer/product records while retaining the original count. Keep deleted/empty rows and excluded languages in a coverage log. A source's displayed total does not prove the export contains every review.

## Code purchase experience, not just sentiment
Use an initial codebook with definition, inclusion/exclusion rule and examples. Distinguish product defect, size/fit, material perception, use-case mismatch, fulfillment problem and expectation set by the page. Add merchant-specific themes from actual text. Allow multiple codes, so totals may exceed review count. Record conflicting evidence and positive tradeoffs as well as complaints.

Every coded row links back to a source ID and a short permitted excerpt. Treat star rating and text sentiment separately. Never infer a demographic, diagnosis or product property from an account name. Count distinct reviewed orders only when order identity is actually available; otherwise the unit is deduplicated review records.

## Rank follow-up work
Report theme prevalence as reviews coded with the theme / reviewed records in the stated corpus; stratify by product/variant and date only where supported. Frequency within a voluntary-review sample is not population incidence. A serious single failure can merit investigation without being called common. Separate count, severity of described outcome, and confidence in interpretation rather than hiding them in a fabricated universal score.

Output a corpus ledger, codebook, theme table (`theme | n/N | products | evidence IDs | contradictions | likely operational owner | next verification`) and a short research conclusion. Product, copy and fulfillment actions should follow evidence; no publishing testimonials, contacting reviewers or modifying ratings is authorized by this analysis.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/customer-research/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/customer-research/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
