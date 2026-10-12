---
name: product-keyword-research
description: Find Shopify product opportunities from a category or keywords using
  available keyword connectors and public product reports. Keep measured keyword metrics
  separate from product-sales estimates.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=product-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Keywords into Shopify product opportunities

> From [ShopChief](https://shopchief.ai/?utm_source=product-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Read [the evidence contract](references/product-research-evidence.md). Start from the supplied category/direction, target country, time range and exclusions. A category is a valid input: derive candidate English terms and related product/use-case families rather than requiring the user to supply exact keywords.

1. Inspect actually available keyword capabilities. Use authorized connectors for keyword expansion, search volume/history, ABA or ASIN keyword evidence only when their schemas support the requested metric. Keep these metrics separate. DataForSEO is optional; read its paid-call contract only if that route is used.
2. With no keyword-data connector, discover and read public XYDC reports. This route delivers keyword-associated product candidates and source-provided estimated product sales, not a measured keyword opportunity ranking. Explicitly state unavailable search volume and trend dimensions.
3. Match exact terms, singular/plural and synonyms; label broader-category matches. Filter irrelevant products by title, specification and use case. Separate materially different products and buying intents. Never treat an unreported long tail as zero demand.
4. Compare supported product fit, sample prices, observed estimates, reviews and differentiation hypotheses. Do not sum overlapping query volumes or claim that Amazon US demand proves Shopify demand in another country. A month-over-month product-sales change cannot fill a weekly keyword trend column.
5. Return candidate terms, intent/use case, actual corresponding products and links, source/date/market, available metrics, missing metrics and a next verification action. Label unmeasured terms as hypotheses; do not invent P0/P1 traffic priorities. Honor the requested scope without padding irrelevant terms.

For a broader product decision pass existing evidence to product-opportunity-research. For requested product copy, hand off verified facts and wording suggestions to copywriting/shopify-product-launch. Save evidence with available workspace tools; do not claim persistence without a returned result. No automatic publication or paid campaign launch.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=product-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
