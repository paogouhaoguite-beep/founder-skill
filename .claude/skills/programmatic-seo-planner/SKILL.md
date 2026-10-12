---
name: programmatic-seo-planner
description: 'Use when a store owner wants to assess a programmatic SEO play built
  on e-commerce page patterns — product x attribute pages, brand x category collection
  pages, use-case / scenario landing pages, comparison pages (product A vs product
  B), and buyer guides — and, if viable, design the page template set: validate the
  keyword pattern and combination count against the product catalog, audit the catalog/attribute
  dataset, decide per URL class generate / consolidate / noindex / canonical, and
  produce URL, Title, H1, body module, FAQ, and Schema templates plus pilot, scale,
  and stop conditions with explicit quality-gate assertions. Evidence uses low-cost
  DataForSEO keyword data (Labs keyword ideas, bulk keyword difficulty) on at most
  20 sampled combinations. Do not use for deep editorial research on one topic (use
  seo-content-research) or for technical issues on already published pages (use site-seo-audit).'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=programmatic-seo-planner&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Programmatic SEO Planner

> From [ShopChief](https://shopchief.ai/?utm_source=programmatic-seo-planner&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

This skill answers two questions in order: (1) is this programmatic play worth building for this store, and (2) if yes, what exactly does the page template look like and what conditions stop it from scaling into thin content. The core rule enforced throughout: **a keyword plus a variable is not unique content.** A page earns an indexable URL only if it delivers information a shopper could not reconstruct by editing one variable in another page — for a store, that usually means real catalog data (specs, availability, price, fit, reviews) or genuine curated guidance.

The deliverable is a decision document with templates, not the generated pages themselves.

## Scope boundary

- Deep research on a single chosen topic into an editorial brief → `seo-content-research`.
- Technical problems on pages that already exist (indexation, canonicals, performance) → `site-seo-audit`.
- Pillar-Cluster editorial content strategies → `seo-content-research`.

## In-scope page patterns (DTC store context)

| Pattern | Example | Typical data source |
| --- | --- | --- |
| Product × attribute | "{product} in {material}" / "{product} {size} {color}" | product catalog attributes |
| Brand × category collection | "{brand} {category}" collection pages | catalog + brand facet |
| Use-case / scenario landing | "{product type} for {activity or scenario}" | catalog attributes + curated curation |
| Comparison | "{product A} vs {product B}" | spec tables, review data |
| Buyer guide | "how to choose {category}", "{category} sizing guide" | catalog attributes + category expertise |

Out of scope: local-service patterns ("{city} × {service}"), directory-style B2B patterns, and content-site plays — this skill only plans store page patterns for DTC shops.

## Required inputs

| Input | Required | Default if missing |
| --- | --- | --- |
| Keyword pattern (e.g. "{product type} for {use case}") | yes | ask |
| The catalog/attribute dataset feeding the variables (source, field list, sample rows) | yes | ask; without a dataset the verdict cannot exceed "Pilot, low confidence" |
| Platform (Shopify assumed) | recommended | state assumption |
| Competitor pSEO page URLs if the user has them | optional | fetch SERP evidence via web search instead |

## Required flow

1. **Pattern validation.** Decompose the pattern into head term × variables. Enumerate the realistic combination count from the catalog (not the theoretical cross-product of attributes). Evidence: low-cost DataForSEO on up to 20 sampled combinations (DataForSEO Labs Google keyword ideas for demand shape, DataForSEO Labs Google bulk keyword difficulty where the user wants difficulty). Record market and date per metric; missing values are `N/A`.
2. **Catalog dataset audit.** For each attribute/field: completeness (how many products have it), uniqueness (do values actually differ between combinations), freshness (price/stock volatility), and whether its values change the page's information for a shopper. Output per-field pass / warn / fail. Note Shopify specifics: variant-level attributes, metafields as the attribute source, and collection-filter availability.
3. **Uniqueness assertion.** For each URL class, state what content is combination-specific (spec comparisons, availability, fit guidance) versus template boilerplate. If the specific part reduces to swapping one attribute value, that class is a **noindex** or **consolidate** candidate.
4. **Verdict: Go / Pilot / No-Go with confidence level** (high / medium / low), justified by (1)-(3). Suggested bars: Go = enough combinations with real demand AND catalog data that produces genuinely distinct pages; Pilot = demand shown but catalog quality unproven; No-Go = thin-content risk or negligible demand.
5. **Per-URL-class decision:** generate / consolidate (merge into the collection or product parent) / noindex / canonical-to-parent, with the reason.
6. **Template set per generated class:** URL pattern, Title, H1, body module list (which modules are catalog-data-driven vs static), FAQ (questions must be derivable from catalog data or real buyer questions, not invented), Schema type (JSON-LD: Product, ItemList, FAQPage, BreadcrumbList as appropriate). Variables shown as `{placeholder}`.
7. **Rollout plan:** pilot set (10-20 pages), success metrics, scale condition, and stop conditions (indexation rate, engagement thresholds, manual-action risk).
8. **Quality-gate assertions.** Concrete, testable statements each pilot page must pass before scaling, e.g. "≥ 3 catalog-specific data points per page", "no two pages share > 60% body text". These are assertions to verify at review time, not fabricated measurements.

## Output format

1. **Verdict block** — Go / Pilot / No-Go + confidence + the three justifying findings.
2. **Combination table** — sampled combination | demand evidence | difficulty (if queried) | decision.
3. **Catalog audit table** — attribute/field | completeness | uniqueness | freshness | verdict.
4. **Template set** — per generated URL class.
5. **Rollout plan** — pilot → scale → stop conditions.
6. **Quality-gate assertions.**

## Failure handling

- No catalog dataset provided: cap the verdict at "Pilot, low confidence" and say which catalog fields are needed.
- Keyword endpoints empty or unavailable: mark demand columns `N/A`, fall back to SERP evidence from web search, and state the downgrade in the verdict.
- configured DataForSEO tools unavailable: say so; do not invent volumes or difficulty values.
- Do not generate actual page content in this skill; that belongs to the content pipeline.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=programmatic-seo-planner&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
