---
name: site-seo-audit
description: Use for store-wide search audits, coordinating page and content specialists,
  search competitor gaps, single AI mention checks, backlinks and brand facts, and
  normal post-optimization reviews. Diagnostic requests stay read-only; optimization
  continues into reviewable changes within actual authorization. Reuse one evidence
  ledger and baseline; demonstrated decline uses content-decay-diagnosis.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=site-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Store search health: diagnose, improve, review

> From [ShopChief](https://shopchief.ai/?utm_source=site-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Read [the shared workflow](references/seo-workflow.md), [rule baseline](references/seo-rule-baseline.md) and [DataForSEO contract](references/dataforseo-contract.md). This skill owns five-dimensional coordination and normal follow-up review, using existing specialists rather than creating a separate runtime.

## Scope and intent
Resolve the current store/domain, selected pages, market/language and objective. A full-store task starts with all five dimensions; a focused technical, AI or backlink request runs only that direction plus necessary prerequisites. Enumerate known page types (home, collection, product/variant/stock states, blog, policy/support), requested vs discovered vs fetched pages and excluded areas. Call a sample a sample, never a complete crawl. Diagnosis is read-only; optimization continues into reviewable content and authorized fixes with separate backend and storefront verification.

## Five-dimensional ownership across three phases

| Dimension | Diagnose and basic repair | Specialist optimization | Review |
| --- | --- | --- | --- |
| Technical access and indexing | HTTP, robots, canonical, sitemap, rendering; distinguish indexability from verified GSC index status | crawl-index-audit; cwv-performance-audit; international-seo-audit; site-migration-seo only for migrations | Repeat affected technical checks and index evidence; field and lab performance separately |
| Search demand and content strategy | Existing pages, audience questions, search intent and coverage | seo-content-research owns topic clusters/new content link plans; keyword-analysis; blog-keyword-research; programmatic-seo-planner when justified | Matched query/page/market trends against saved baseline |
| Page expression and factual evidence | Real product/brand facts, helpful headings/copy and extracted structured data | product-page-seo; collection-page-seo; blog-article-writer; schema-markup-designer; copywriting for other page copy | Field readback, visible rendering, factual accuracy and available page performance |
| Site structure and internal links | Discoverability, navigation, existing links and sampled orphan candidates | internal-link-audit; keyword-cannibalization; seo-content-research for new topic links | Verify exact source/target links, crawl coverage and remaining issues |
| Off-site reputation and brand information | Backlinks, verified brand profiles, cited sources and inconsistent facts | This skill owns backlink gaps and actionable brand-source corrections; commercial intelligence remains competitor-deep-analysis only when requested | Recheck named sources, comparable backlink evidence and fixed AI sample |

Use one issue ledger with stable IDs, dimension, SEO/GEO impact, page/evidence, priority, repair and acceptance. Merge shared issues across specialists. Do not invent an overall score. Prioritize material access/fact failures and important pages using observed impact, scope and feasibility.

## Focused technical route
Inspect public HTML/DOM and authorized existing reports first. Documented OnPage Instant Pages can supplement metadata/status; Content Parsing can supplement text/links but does not prove raw structured markup coverage. Extract JSON-LD/microdata explicitly. Lighthouse provides laboratory evidence; INP/real experience require appropriate field/interaction data. Label absent data unverified and retain successful partial findings without repeated paid retries.

## Focused AI mention route
Fix platform, market, language, brand/aliases, questions and observation timestamp before comparing. Keep supplier mention-library data, actual search-interface sampling and ordinary model API answers separate. Documented LLM Mentions families, ChatGPT Scraper and AI keyword demand are capability hints, not tool names. Check exact current documentation, eligibility, expense and task completion first. Extract brand presence, cited URL, supporting passage and correct/incorrect/unknown facts per question, with sample denominators. One sample is not general search exposure, persistent monitoring, a ranking or future citation guarantee. When unavailable, audit source clarity and brand facts with existing evidence; mark AI observation unverified.

## Focused backlink and competitor route
Use comparable dates and domain scope for documented backlink summary, referring domains and intersections. Record missing/empty/zero distinctly. Provider spam/rank metrics are estimates, not proof of a penalty or grounds for automatic disavowal. Search competitors can differ from business competitors. Compare actual ranking/content/citation gaps, not all commercial intelligence. Deliver source URL, inaccurate/missing brand fact, proposed correction, owner/channel and acceptance method. Prepare useful original resources and truthful brand profile corrections; outreach, buying links and publication require actual authorization and are never automatic audit steps.

## Deliver and review
Deliver concise findings, five-dimensional coverage, one issue/repair register, completed changes with readback, missing evidence and the saved baseline. If a report is useful, save a complete HTML file and expose the stable saved result in chat. Offer the current-task review follow-up carrying actual artifact and issue references. Follow [the review procedure](references/review-procedure.md) for normal technical/SEO/AI/business review. Only demonstrated performance decline calls for content-decay-diagnosis; no forced new research when evidence remains suitable.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=site-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
