---
name: keyword-cannibalization
description: Use when several URLs on a store may be competing for the same query
  or search intent and the user wants a diagnosis and fix. Grades each group as confirmed
  (ranking-swap evidence in the uploaded GSC pages-x-queries export) or potential
  (structural similarity without swap evidence); selects the primary page; decides
  keep-separated / re-target / merge+301 / canonical / noindex per URL; outputs a
  URL action map and a 2/4/8-week monitoring plan. Candidate pages are verified live
  with OnPage Instant Pages. Shopify hotspots (tag pages, filter pages, variant URLs)
  are covered. Do not use for site-wide indexability (use site-seo-audit) or for keyword
  metrics (use keyword-analysis).
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=keyword-cannibalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Keyword Cannibalization

> From [ShopChief](https://shopchief.ai/?utm_source=keyword-cannibalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

This skill answers two questions: (1) are multiple URLs on this site competing for the same query or intent, and (2) if so, which page to keep and how to handle the rest. Grading follows evidence strength: **confirmed cannibalization** requires behavioral evidence — multiple URLs swapping rankings for the same query (from the uploaded GSC pages×queries export) or clearly identical intent; structural similarity without swap evidence is graded **potential cannibalization**.

## Scope boundary

- Site-wide technical indexability (crawl, sitemap, robots) → `site-seo-audit`.
- Search volume / KD / CPC metrics for the keywords themselves → `keyword-analysis`.
- One page decaying with no competing sibling → `content-decay-diagnosis`.

## Input contract (GSC = connected data or supplied export)

Inspect actual authorized Search Console access; if absent use supplied exports:

| File | Format | Minimum columns | Used for |
| --- | --- | --- | --- |
| GSC Performance, Pages×Queries view | connected rows or CSV export | page URL, query, clicks, impressions, position (≥ 3 months) | which URLs alternate under the same query |
| GSC Performance, Pages view (optional) | connected rows or CSV export | page URL, clicks, impressions, position | overall baseline per candidate |

Handling rules: state the export's date range; normalize URLs (http/https, trailing slash, parameters) before counting and say so; never fabricate ranking data absent from the export.

**No export supplied:** only a **potential** grading is possible (from live checks and SERP observation); the output must state that upgrading to "confirmed" requires the pages×queries export.

## Required flow

1. **Bound the competing groups.** From the export, find every query (or tight query cluster) where ≥ 2 URLs appear; without an export, work from the user's candidate URL list via the potential path.
2. **Verify candidates live.** OnPage Instant Pages per candidate URL: status code, canonical target, Title, H1, body gist, indexability signals. Respect the budget cap (default ≤ 15 URLs) in the cost contract.
3. **Grade: confirmed vs potential.**
   - **Confirmed:** the export shows ≥ 2 URLs alternating rankings for the same query across dates (cite the specific rows), or two live pages share identical core intent and both have been indexed.
   - **Potential:** intents overlap heavily, templates/titles are similar, but no swap evidence exists.
4. **Select the primary page.** In order: the page with stronger current rankings and clicks; the page closest to the core conversion intent; the more complete and current one; the URL better suited to long-term ownership. Give reasons; when export data is thin, rank on live evidence plus business reasoning and say so.
5. **Handling decision**, one per non-primary URL:
   - **Keep separated:** intents are actually different (e.g. buy page vs tutorial); adjust Title/H1 and internal-link anchors to pull the positioning apart.
   - **Re-target:** aim the page at an adjacent, distinct query.
   - **Merge + 301:** fold content into the primary page and 301 the old URL.
   - **Canonical:** content must stay reachable but should not rank independently (e.g. filtered views) → canonical to the primary page.
   - **Noindex:** purely functional pages (sort, pagination, tag aggregations) with no search value → noindex.
6. **URL action map** — one row per URL: current state | action | target | execution note (301 / canonical / noindex / edit).
7. **Monitoring plan (2/4/8 weeks):** week 2 (301/canonical/noindex live, no 4xx/5xx), week 4 (primary page rankings and impressions recovering), week 8 (competing queries converge to a single URL, compared against the export baseline). Each checkpoint names its metric and baseline.

## Shopify hotspots

Tag pages (`/tagged/`), filter parameter URLs, and product variant pages are the high-incidence zones:
- Tag pages re-serve product content → default noindex or canonical to the collection, unless the tag page is itself a content asset.
- Filter/sort parameters → canonical to the canonical collection URL, keep parameter handling consistent for crawlers.
- Variant pages / `?variant=` URLs → canonical to the main product page.
These are default starting points; always confirm the site's actual configuration with a live check before concluding.

## Output format

1. **Competing groups** — query/intent | involved URLs | grade (confirmed/potential) | evidence.
2. **Primary selection** — primary page and reasons per group.
3. **URL action map.**
4. **2/4/8-week monitoring plan** with baselines.

## Failure handling

- No matching GSC data: grade everything as potential and state the upgrade condition.
- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- Inconsistent URL formats in the export: normalize and say so; do not silently drop rows.
- Never invent rankings, dates, or indexation status.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=keyword-cannibalization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
