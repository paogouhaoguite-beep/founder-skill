---
name: content-decay-diagnosis
description: Use when a store money page — a collection page, product page, or key
  landing page — shows search-performance decay (falling clicks, impressions, or rankings
  over time) and the user wants the cause and a fix. GSC and GA4 data are connected
  data or supplied files (the input contract specifies the CSV formats; they are optional
  — without them only a shallow "potential decay" diagnosis is possible and must be
  labeled). Live page state (status, canonical, Title, H1, content) is checked with
  DataForSEO OnPage Instant Pages. Update briefs cover new Title/Description/H1, page
  module and merchandising edits, and Schema; consolidation covers collection merges
  with a 301 map. Do not use for site-wide technical problems (use site-seo-audit)
  or for multiple URLs competing for the same query (use keyword-cannibalization).
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=content-decay-diagnosis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Content Decay Diagnosis

> From [ShopChief](https://shopchief.ai/?utm_source=content-decay-diagnosis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

This skill diagnoses why one money page (or a small set, default ≤ 10) is losing search performance and produces the recovery plan: the decay cause, an update brief, any consolidation decisions with a 301 map, and a dated verification plan. Diagnosis-first: no update brief before a cause is named, and every cause claim traces to evidence from the uploaded exports, the live page check, or SERP observation.

The primary objects are **money pages** — collection pages, product pages, and key landing pages (homepage sub-pages, campaign landing pages, comparison landing pages). Editorial blog decay is handled by the same method, but the default focus and the update brief templates are merchandising-oriented.

## Scope boundary

- Site-wide technical health, indexability, AI visibility → `site-seo-audit`.
- Multiple URLs competing for the same query or intent → `keyword-cannibalization`.
- Planning new content around clusters → `seo-content-research`.

## Input contract (GSC / GA4 = connected data or supplied exports; optional)

Inspect available authorized connections first; use GA4 directly when available and GSC only if actually connected. Otherwise use supplied exports:

| File | Format | Minimum columns | Used for |
| --- | --- | --- | --- |
| GSC Performance, Pages view | connected rows or CSV export | page URL, clicks, impressions, position, date range (monthly granularity preferred, ≥ 6 months) | decay shape: when it started, which metric decayed first |
| GSC Performance, Pages×Queries view | connected rows or CSV export | page URL, query, clicks, impressions, position | which queries decayed, whether the page still ranks for its core intent |
| GA4 Landing page report (optional) | connected rows or CSV export | landing page, sessions, engaged sessions, conversions, date range | whether traffic decay is engagement-driven |

Rules for handling uploads: state the export's date range in the diagnosis; if the file lacks monthly granularity, say what analysis is impossible; never fabricate numbers not present in the file.

**No matching connected data or exports available:** only a shallow "potential decay" diagnosis is possible — based on the live page check and SERP observation — and the output must say explicitly that cause classification and the verification baseline require the GSC export.

## Required flow

1. **Confirm the decay.** From the exports: decay start month, which metric decayed (clicks / impressions / position / conversions), and the shape (cliff = event; slope = gradual; seasonal dip vs true decay — compare to the same month last year if the range allows). For store pages, check whether the decay coincides with a merchandising event (collection rules changed, products delisted, price changes, theme relaunch).
2. **Check the live page.** OnPage Instant Pages on the target URL: status code, canonical, Title, H1, meta description, visible content (product counts on collections, availability on products), schema presence. Respect the cap in the cost contract.
3. **Classify the cause** into the nine categories, each with its evidence:
   1. Content/merchandising staleness (out-of-stock heroes, outdated copy, stale collection rules, expired claims).
   2. SERP shift (new result types or formats now win the query — verify via web search; category and product queries are especially sensitive to shopping surfaces).
   3. Cannibalization (a newer collection or variant page took over — hand off to `keyword-cannibalization` with the evidence).
   4. Technical regression (noindex/redirect/canonical error, broken render, Core Web Vitals collapse, collection filter changes creating duplicate or blocked URLs).
   5. Title/meta mismatch (page drifted from what ranks; snippet no longer matches intent).
   6. Lost links or authority (requires relevant dated backlink evidence from existing data or a budgeted DataForSEO query; otherwise mark unverified).
   7. Query demand decline (volume fell — use existing keyword history or query it within the requested diagnosis and contract; without evidence label as hypothesis).
   8. Seasonality (pattern repeats annually — common for seasonal collections).
   9. Intent mismatch (the page answers a different question than the query now means — e.g. a brand-hub page ranking for a "how to choose" query).
   Multiple causes may coexist; rank them.
4. **Update brief** (only for causes 1, 2, 5, 9, and fixable 4): new Title (concise, accurate; length is an editorial preview consideration), new meta description (accurate, useful summary; no fixed ranking cutoff), new H1, module-level edits (which sections to add, cut, or rewrite — intro copy, comparison tables, buying criteria, FAQ; for collections: curated product selection and ordering rules), and required Schema type (Product, ItemList, BreadcrumbList, FAQPage). Tie every change to the named cause.
5. **Consolidation map** (if the page overlaps a stronger sibling — e.g. two overlapping collections): survivor URL, merged URL(s), 301 target, what content moves.
6. **Verification plan:** day 7 (indexation + no regression), day 28 (impressions/position trend vs pre-decay baseline from the export), day 90 (clicks recovery or escalate). Each checkpoint names the metric and its baseline value from the export.

## Output format

1. **Decay confirmation** — start month, decayed metrics, shape, with the export date range cited.
2. **Cause classification** — ranked causes, each with evidence; `N/A` where data is missing.
3. **Update brief** — Title / Description / H1 / module edits / Schema.
4. **Consolidation 301 map** (if applicable).
5. **7/28/90-day verification plan** with baselines.

## Failure handling

- No matching GSC data: run the shallow diagnosis, label every cause as potential, state the missing input.
- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- Exports with mismatched URL formats (http/https, trailing slash, collection parameter variants): normalize and say so; do not silently drop rows.
- Never invent positions, clicks, or ranking dates.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=content-decay-diagnosis&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
