---
name: keyword-analysis
description: 'Look up keyword metrics for a specific keyword set: monthly search volume,
  12-month trend, keyword difficulty, CPC, paid competition, and search intent. Use
  when the user gives keywords (or a short list) and asks for volume, difficulty,
  CPC, competition, intent, or trend direction. Do not use for content topic selection
  or editorial planning (use seo-content-research), for discovering which keywords
  competitor domains rank for (use competitor-deep-analysis), or for go/no-go product
  validation (use product-opportunity-research). Metric-only requests end here. Product-selection
  keyword discovery/comparison uses product-keyword-research; article keyword plans
  use blog-keyword-research; finished articles from keywords use blog-article-writer.
  Reuse this evidence and use only available skills.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=keyword-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.


# Keyword evidence for commerce

> From [ShopChief](https://shopchief.ai/?utm_source=keyword-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Look up the requested keyword set and support the user's stated decision. For a metric-only request keep delivery compact; for a broader task carry evidence into page, copy or campaign recommendations without a second research pass.

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Resolve market/language from the request, then the current store brief. Reuse fresh matching evidence. Announce scope and select only needed fields.

## Query plan
Start with Keyword Overview when it supplies requested volume, CPC, paid competition, intent and organic keyword difficulty. Inspect the actual returned fields before adding a dedicated volume, difficulty or intent endpoint. Missing organic KD remains N/A; paid competition is never its proxy. Add monthly history/trends if requested or necessary for seasonality; verify supported batch limits and split internally. Use current SERP for shortlisted terms only when ranking intent is uncertain. Expansion is allowed when part of the requested research; do not expand an exact-list lookup silently.

## Interpret and deliver
Preserve keyword identity and duplicates/normalization notes. Table: keyword, market/language, volume with period, monthly trend if available, organic KD, CPC/currency, paid competition, intent, source/date. Distinguish zero from unavailable. For a supplied batch account for every input with a result or explicit unavailable/error status; do not stop at a default 20-word sample.

Add concise fit notes when asked to choose: relevance to the actual product, observed SERP/page type, existing page to improve or new asset to create, priority and verification metric. Low-volume terms are not automatically worthless; judge category, intent and attainable demand. Do not label CPC universally cheap/expensive without margin/conversion context. Use pre-ad contribution per order × an explicitly sourced/assumed conversion rate for break-even CPC scenarios, never a profitability guarantee.

Save/reuse the evidence artifact under the current tenant/store. Missing fields or failed queries stay visible; follow the contract's stop rules.

## Specialist routing
Metric-only requests end here. Product-selection keyword discovery/comparison uses product-keyword-research; article keyword plans use blog-keyword-research; finished articles from keywords use blog-article-writer. Reuse this evidence and use only available skills.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=keyword-analysis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
