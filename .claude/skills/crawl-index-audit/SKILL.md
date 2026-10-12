---
name: crawl-index-audit
description: Diagnose why pages are not discovered, not rendered, not eligible for
  indexing, or not actually indexed. Judges the four states separately instead of
  conflating them, and checks robots conflicts, sitemap quality, noindex, parameter/pagination/filter
  URLs, host and trailing-slash variants, soft 404s, redirect chains, orphan pages,
  and JS-render discoverability. Crawl and render evidence comes from DataForSEO on_page
  tools on a bounded URL sample; index status comes from actual GSC evidence; logs
  establish crawl activity, not indexation, and is marked N/A without them. Use when
  the user asks why pages are not indexed, reports crawl or sitemap problems, or suspects
  wasted crawl budget on faceted or paginated URLs. Do not use for page speed or Core
  Web Vitals (use cwv-performance-audit) or for duplicate-content and keyword cannibalization
  analysis (use keyword-cannibalization).
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=crawl-index-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Crawl & Index Audit

> From [ShopChief](https://shopchief.ai/?utm_source=crawl-index-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

This skill answers one question: which pages can Google reach, render, qualify for indexing, and actually index — and where is the pipeline leaking? It separates four states and never merges them:

1. **Crawlable** — the URL is reachable and not blocked by robots.txt, auth, or a blocking redirect.
2. **Renderable** — the content Googlebot needs survives rendering (JS-rendered content is present in the rendered DOM).
3. **Indexable** — the page signals "index this": 200 status, self-referencing canonical, no noindex, no conflicting directive.
4. **Indexed** — Google actually has the page in the index (GSC URL Inspection or a site: query — observed evidence, not inference).

A page can be crawlable but not renderable, or renderable and indexable but still not indexed. Never jump from "not indexed" to a fix without naming which state failed.

## Scope boundary

- Page speed, LCP/INP/CLS, and render-blocking analysis → `cwv-performance-audit`.
- Duplicate content across similar pages and keyword cannibalization between pages targeting the same query → `keyword-cannibalization`.
- Whole-domain health triage (performance, structured data, GEO, backlinks in one pass) → `site-seo-audit`.

## Inputs

| Input | Source | If missing |
| --- | --- | --- |
| Target domain + URL sample (10-30 URLs) | user, or built from sitemap + homepage links | build the sample from fetched sitemap |
| robots.txt and sitemap(s) | fetched live (free) or pasted by user | ask user; robots evidence is mandatory |
| GSC Pages / URL Inspection export | authorized connection or user export | mark the entire "Indexed" state section N/A |
| Server or CDN access logs | authorized connection or user export | mark log-based crawl-budget section N/A |
| GA4 landing-page export (optional) | authorized connection or user export | skip; not load-bearing for this skill |

Never present "indexed" claims from anything other than GSC evidence or an observed site: query result. A page returning 200 is not proof of being indexed.

## Required flow

1. Confirm the target domain, the concern (e.g., "these 40 pages are not indexed"), and whether the site is JS-heavy.
2. Fetch robots.txt and the declared sitemaps (free fetch, no paid call). Read them before touching page checks.
3. Fix the URL sample: prioritized set of 10-30 URLs covering the concern, key templates (home, collection, product, blog), and any URL the user flagged.
4. State the plan (endpoints, URL count) before any paid call, per `references/dataforseo-contract.md` (exploratory sample: up to 30 URLs; declared scope follows the contract).
5. Run page checks, analyze patterns, deliver the report. Do not interleave report writing with more paid calls.

## Checks

### State 1 — Crawlable

| Check | Evidence source |
| --- | --- |
| robots.txt blocks the URL, its CSS/JS, or a directory in its path | fetched robots.txt |
| robots conflict: sitemap lists a URL that robots disallows | robots.txt vs sitemap |
| Non-200 status, auth wall, or redirect on entry | OnPage Instant Pages status field |
| Host variants (www / non-www, HTTP / HTTPS, trailing slash) resolving differently | fetched robots + sitemap URLs + sample checks |

### State 2 — Renderable

| Check | Evidence source |
| --- | --- |
| Primary content (title, description, price, product copy, headings) present in server response vs only after JS render | OnPage Instant Pages + OnPage Content Parsing |
| Internal links discoverable without JS | OnPage Content Parsing link targets |
| Infinite-scroll or client-side pagination hiding deeper URLs from crawlers | sitemap completeness vs crawled link set |

### State 3 — Indexable

| Check | Evidence source |
| --- | --- |
| noindex in meta robots or X-Robots-Tag | OnPage Instant Pages |
| Canonical: missing, cross-domain, pointing to a variant host, or a redirect target | OnPage Instant Pages |
| Soft 404: 200 status with "not found" / empty content | OnPage Content Parsing content read |
| Redirect chains and loops (A→B→C, A→B→A) | OnPage Instant Pages redirect field, spot-checked by hand |
| Parameter / pagination / filter variants each returning unique crawlable URLs | sample checks across the URL patterns |
| Sitemap quality: 404s, redirects, noindexed, or canonicalized URLs still listed | sitemap + page check results |

### State 4 — Indexed (user data only)

| Check | Evidence source |
| --- | --- |
| Page listed in GSC Pages report with status (Indexed / Crawled-not-indexed / Discovered-not-crawled / Excluded + reason) | GSC export |
| URL Inspection result for priority URLs | user runs GSC URL Inspection manually — see output step 5 |
| Crawl frequency and depth from logs; wasted budget on parameter URLs | log export |
| site: domain sample query as a rough sanity check | free web search |

If no GSC or log export exists: keep States 1-3, write "Indexed status: N/A — no GSC or log data provided; run the URL Inspection steps below to collect it," and do not guess.

## Output format

1. **URL sample checklist** — one row per URL: URL, template, State 1-4 verdicts, observed value for each failing state, source of evidence.
2. **Issue pattern table** — findings grouped by pattern (not by URL): pattern, affected URL count in sample, state affected, root cause, evidence snippet.
3. **Parameter governance rules** — per URL parameter: does it change indexable content? Crawl / no-crawl, index / noindex, canonical target, sitemap inclusion. Covers pagination, sort, filter, tracking parameters.
4. **P0-P3 roadmap** — P0 blocks indexing of money pages; P1 broad crawl waste or sitemap noise; P2 hygiene (host variants, trailing slash); P3 improvements. Each item: finding, fix, effort band.
5. **GSC URL Inspection manual steps** — exact list of priority URLs and the button-by-button steps for the user to run Inspection, so the Indexed state gets real evidence.

## Failure handling

- configured DataForSEO tools unavailable: work from robots/sitemap fetches and note that page-level states are unverified.
- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- No sitemap declared: report it as a finding, not an error.
- Complete the explicitly requested URL set within budget/provider limits; report every checked and unchecked URL.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=crawl-index-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
