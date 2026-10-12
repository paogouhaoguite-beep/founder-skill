---
name: blog-keyword-research
description: 'Independently research blog keywords, intent clusters, topic priorities
  and handoff briefs. Planning only: no article writing, final image selection or
  Shopify writes.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=blog-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.
# A writing-ready blog keyword plan

> From [ShopChief](https://shopchief.ai/?utm_source=blog-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Turn a catalog, product collection, supplied keyword list or editorial goal into useful article opportunities. This skill plans articles; blog-article-writer writes them when requested. General collection/PDP SEO planning remains with seo-content-research. Read [query contract](references/dataforseo-contract.md) before paid calls and [handoff and acceptance](references/delivery.md) before delivery.

## Ground the plan in the store
Read current product names, materials, functions, public product/collection URLs, relevant existing blog articles. Paginate within scope; state catalog/site coverage if incomplete. Resolve publication language separately from conversation language. Missing connection permits public site/catalog reads or supplied files; never invent catalog access. Existing URLs and article titles are evidence, not assumptions from handles.

## Discover and select
- Expand relevant informational and commercial-investigation questions: selection criteria, care, use cases, comparisons and buyer objections. Use actual product differences; don't invent certifications or material attributes to match demand.
- Reuse market-matched DataForSEO evidence; query documented related/suggestion or competitor keyword routes only to fill gaps. Batch overview metrics; add history for seasonal topics and current SERPs for shortlisted article intents. Distinguish zero, missing and estimated values. Do not query all endpoint families for each topic.
- Confirm that SERPs support an article. A shopping query dominated by category/product pages may belong on an existing money page; flag it rather than force it into a blog. Prioritize product relevance, reader value, current page opportunities, competition and evidence strength; volume/KD alone do not decide priority.
- Cluster synonyms and questions by shared intent and SERP overlap. Give one primary query/intent to each planned article; secondary terms belong in that same article where they answer the same need. One keyword does not automatically mean one new article.
- Compare planned clusters with existing products, collections and blog pages. Choose create, refresh, merge-proposal or skip with an exact existing URL where applicable. Similar terms alone do not prove cannibalization; record page/intent/SERP evidence. Do not merge/delete pages during planning.

## Deliver
Lead with the prioritized plan and a copyable primary-keyword list in the target search language. Each row includes cluster ID, primary term, secondary terms/questions, search intent, volume/period, organic KD, CPC/currency if relevant, trend, proposed title/angle, create/refresh decision, target or existing page, product fit and confidence. Keep proposed handles explicitly proposed. A request for 100 keywords means account for 100 terms, not silently promise 100 distinct articles; explain grouping. Report evidence shortfalls honestly rather than invent topics or metrics.

For each selected article, return the assignment fields in [Blog brief v1](references/blog-brief-contract.md): selected keyword, intent, market/language, topic angle and evidence. Related products and candidate internal-link targets are optional planning hints. Detailed article outlines, final SEO fields, image selection and link placement belong to the writer; they are not gates for keyword delivery.

Persist the dated keyword plan/brief in the current tenant/store, or return it inline with a not-saved note. This skill stops at the completed plan. If the user requested both keywords and articles, the coordinating assistant passes the selected briefs to the separate writing skill; this skill does not write articles or call the writer itself.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=blog-keyword-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
