---
name: collection-page-seo
description: 'Audit and optimize e-commerce collection (category) pages: metadata,
  H1 and intro copy, FAQ, product cards, pagination and infinite-scroll discoverability,
  Product + ItemList + BreadcrumbList schema, and faceted navigation rules. Use when
  the user gives collection URLs (an exploratory sample of 10) and asks why category
  pages do not rank, how to handle filter parameters, or wants per-page Title/Description/H1/copy/link
  recommendations. Product detail pages use product-page-seo; whole-site technical
  health uses site-seo-audit; conversion and trust optimization of product pages uses
  shopify-product-page-cro — this skill covers only the collection-page layer.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=collection-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Collection Page SEO

> From [ShopChief](https://shopchief.ai/?utm_source=collection-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

Collection pages are the ranking engine of a store: they target the head and mid-tail category keywords that product pages cannot. This skill audits an exploratory sample of 10 collection URLs (plus the filter/facet system behind them) and produces a health summary, a page-level checklist, a faceted-navigation decision matrix, per-page content recommendations, template-level development requirements, and a P0-P3 fix list.

## Scope boundary

- Product detail pages (single-URL templates, variants, PDP schema) → `product-page-seo`.
- Whole-site technical health (crawl budget, sitemaps at scale, Core Web Vitals across templates) → `site-seo-audit`.
- Conversion and trust elements of product pages (CTA, reviews widgets, checkout flow) → `shopify-product-page-cro`.
- This skill touches the technical plane only where it serves collection-page indexability: canonical tags, robots directives, pagination, and facet crawlability. It does not redesign site architecture beyond the collection layer.

## Required inputs

| Input | Required | Notes |
| --- | --- | --- |
| Collection page URLs | required | start with an exploratory sample of 10 for exploratory work; complete explicitly requested scope within the query contract |
| Platform | required | Shopify, WooCommerce, other |
| Core products and attributes | required | product families, the attribute dimensions used for filters (size, color, material, price, brand...) |
| Target keywords | recommended | one primary keyword per collection where the user has one |
| Product feed | optional | connected catalog data or supplied file; used to cross-check product cards, read through authorized connections when available |

Audit the supplied URLs; state how far their findings can generalize to a template without asking to expand the scope.

## Workflow

1. **Confirm inputs and state the plan.** List the URLs to fetch, the keyword-evidence queries, and the rough number of paid calls before the first call (see `references/dataforseo-contract.md`).
2. **Fetch pages.** Run OnPage Instant Pages on each collection URL (inspect public HTML first; enable JavaScript rendering only if required content is absent because it hydrates client-side, not merely because it is a Shopify 2.0 theme). Add OnPage Content Parsing for documented heading/content/link fields when deeper inspection is needed. Extract Schema from actual HTML/DOM markup or a verified extraction response; ordinary content parsing does not establish complete Schema fields. Exploratory sample: 10 URLs; complete an explicitly requested larger scope within the query contract.
3. **Gather keyword evidence.** For each collection's primary keyword, one pass of DataForSEO Labs Google keyword ideas (low cost) to confirm search value before recommending indexable facets or new subcategory pages. Do not recommend an indexable facet without search evidence.
4. **Run the page checklist** (below) per URL.
5. **Build the faceted-navigation decision matrix** (below) from the attributes in the inputs plus the facet links observed in the parsed pages.
6. **Deliver the report.** One consolidated report; do not interleave report writing with further paid calls.

## Page checklist (per URL)

| Check | What good looks like |
| --- | --- |
| Title | unique, primary keyword front-loaded, concise, accurate; length is an editorial preview consideration, brand suffix optional |
| H1 | one H1, matches the collection's primary keyword, may match the Title; assess clarity and hierarchy |
| Intro copy | 1-3 sentence top intro visible above the grid; no keyword stuffing |
| FAQ | FAQ section answering real pre-purchase questions; FAQPage schema optional and only if content is on-page |
| Breadcrumbs | visible breadcrumb trail + `BreadcrumbList` schema, path reflects site hierarchy |
| Schema | `ItemList` listing the products on the page; `Product` schema only if the page genuinely represents one product family |
| Product cards | image, name, price (and compare-at price when discounted), rating when present; no sold-out card without an availability signal |
| Pagination | crawlable `<a href>` links to page 2+ (or numbered links); `rel="prev/next"` is ignored by Google and is not a fix; infinite scroll has a paginated fallback |
| Empty results | filtered combinations that return zero products either return an appropriate real 404 or remain useful and explicitly excluded from indexing; never intentionally produce a soft 404 or are excluded from indexing |
| Seasonal / out-of-stock | seasonal collections have evergreen URLs with rotating content, not new URLs each season |
| Brand × category pages | only built when the pair has search evidence; otherwise noindex thin combos |
| Internal links | links to child collections, buying guides, and sibling collections; no orphan collections |

## Faceted-navigation decision matrix

For every filter parameter observed (and every parameter the user plans), fill one row:

| Parameter | Search value (evidence) | Crawlable | Indexable | Canonical | Internal links | Sitemap |
| --- | --- | --- | --- | --- | --- | --- |

Decision rules:
- Evidence of distinct search intent AND useful unique inventory/content can justify an indexable self-canonical landing page; volume alone cannot.
- For near-duplicate variants, use canonical consolidation consistently. For intentional search exclusion, use crawlable noindex and remove from sitemap; do not use noindex to select a canonical.
- For excessive crawling of unwanted facet combinations, consider preventing crawl through URL/link design or robots.txt. Blocked URLs cannot expose noindex/canonical reliably, and robots.txt does not guarantee removal from search.
- Preserve useful pagination with distinct self-canonical URLs. Verify user access and actual rendering separately.

## Output format

1. **Health summary** — 3-5 sentences: overall state of the collection layer, the 2-3 findings that matter most.
2. **Page checklist table** — one row per URL × check, `PASS` / `WARN` / `FAIL` with observed values.
3. **Facet decision matrix** — the filled table above, with evidence source per row.
4. **Per-page recommendations** — for each URL: recommended Title, meta Description, H1, top intro copy (1-3 sentences, ready to paste), complete supporting copy when requested, relevant buyer questions with complete factual answers when useful, internal-link targets. Write recommendations from the fetched page's actual products and category; do not invent product attributes.
5. **Template-level development requirements** — changes that apply to the collection template (schema additions, pagination fallback, facet handling), each as a developer-ready requirement.
6. **P0-P3 priority list** — P0 blocks indexing or misleads users; P1 costs rankings on proven keywords; P2 content depth; P3 hygiene.

## Anti-hallucination rules

- Every check result cites an observed value from a fetched page. If a page could not be fetched, mark all its checks unverified.
- Schema recommendations quote only fields visible on the page or present in the product feed. Unknown values become template variables, not guesses.
- Search volumes are DataForSEO estimates: label them as such, with location and language. Never present a number without its evidence query.
- Do not recommend indexable facets or brand × category pages without search evidence from step 3.

## Failure handling

- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- DataForSEO Labs Google keyword ideas returns no data for a keyword → report "no search evidence found"; that is a finding, not an error.
- Rate limit or balance error → keep completed results, stop, list what remains unverified.

For multiple pages, deduplicate shared keywords and query once, reusing overview fields. Use expansion only to discover needed new terms; never pay repeatedly for the same keyword per page.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=collection-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
