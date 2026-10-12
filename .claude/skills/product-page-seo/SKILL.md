---
name: product-page-seo
description: 'Audit and optimize e-commerce product detail pages: metadata, unique
  descriptions, specs, images, FAQ and trust information; Product / Offer / AggregateRating
  schema consistency with visible page content; variant URLs and canonicals; and the
  full out-of-stock and delisting lifecycle (404, 410, 301, substitutes — never redirect
  everything to the homepage). Use when the user gives product URLs (an exploratory
  sample of 10 representative pages) and asks why product pages do not rank, how to
  handle variants, or what to do when a product goes out of stock or is discontinued.
  Conversion and trust optimization uses shopify-product-page-cro; deep structured-data
  design uses schema-markup-designer; collection pages use collection-page-seo — this
  skill covers the PDP template and its lifecycle only.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=product-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Product Page SEO & Stock Lifecycle

> From [ShopChief](https://shopchief.ai/?utm_source=product-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

Product pages win long-tail product and brand queries, and they lose rankings quietly when stock changes: delisted SKUs soft-404, variants duplicate, offers stale. This skill audits an exploratory sample of 10 representative product URLs (with sampled variant and stock states) and produces a template health summary, a sample table, template-level recommendations, complete JSON-LD, a lifecycle decision tree, a URL action table, and a P0-P3 fix list.

## Scope boundary

- Collection pages and faceted navigation → `collection-page-seo`.
- Whole-site technical health (crawl budget, sitemaps, Core Web Vitals across templates) → `site-seo-audit`.
- Conversion and trust elements (CTA copy, review widgets, urgency, checkout flow, A/B tests) → `shopify-product-page-cro`. This skill reads trust information only as structured-data consistency inputs, it does not optimize conversion.
- Deep structured-data design beyond the Product/Offer/AggregateRating triple → `schema-markup-designer`.

## Required inputs

| Input | Required | Notes |
| --- | --- | --- |
| Product page URLs | required | an exploratory sample of 10 representative pages; include at least one low-content page if the user knows of any |
| Platform | required | Shopify, WooCommerce, other |
| Variant / stock states to sample | recommended | which URLs are variants or currently out of stock / discontinued |
| Product feed | optional | connected catalog data or supplied file; the cross-check source for prices, availability, GTIN, images — read through authorized connections when available |
| Known traffic business context | optional | which products matter most (best sellers, margin leaders) for prioritization |

## Workflow

1. **Confirm inputs and state the plan.** List the URLs, the sample of variant/stock states, and rough call count before the first paid call (see `references/dataforseo-contract.md`).
2. **Fetch pages.** Run OnPage Instant Pages on each product URL, including the sampled variant and out-of-stock URLs. Use OnPage Content Parsing when deeper text inspection is needed. For Schema fields, extract actual JSON-LD/microdata from public HTML or rendered DOM; use a documented extraction response only if it returns the required raw evidence. Missing extraction is unverified, not absent markup. Exploratory sample: 10 URLs; complete an explicitly requested larger scope within the query contract.
3. **Cross-check against the product feed** when provided: price, availability, image URLs, GTIN/MPN, ratings — schema values must match one of these sources or the visible page.
4. **Run the page checklist** per URL.
5. **Verify schema-to-visible consistency**: every `Product`/`Offer`/`AggregateRating` value must be visible on the page or present in the feed. Flag any value that exists only in markup (Google treats hidden-vs-visible divergence as a violation).
6. **Build the lifecycle decision tree and URL action table** from the observed stock and discontinued states.
7. **Deliver the report.** One consolidated report.

## Page checklist (per URL)

| Check | What good looks like |
| --- | --- |
| Title | unique per product, follows the template formula, no boilerplate prefix repeated across all products |
| H1 | product name, one per page, may match the Title; assess clarity and hierarchy |
| Description | unique, written for this product, not a manufacturer blurb copied across SKUs |
| Specs | key attributes in a structured table or list (the raw material for rich markup) |
| Images | descriptive filenames and alt text; primary image matches the Offer `image` value |
| FAQ | genuine relevant buyer questions, with no fixed count or required FAQ block |
| Trust information | shipping, returns, warranty, and review signals present and machine-readable where ratings exist |
| Schema consistency | `Product` + `Offer` (price, priceCurrency, availability) + `AggregateRating`/`Review` only where visible |
| Variant handling | Inspect actual variant URLs/content; consolidate parameter-selected duplicates to the principal URL, use a justified strategy for substantive independent pages, and align canonical, links, sitemap and ProductGroup data. |
| Stock state markup | out-of-stock pages still return 200 with `availability: OutOfStock`, no fake prices, no removed offers |
| Thin content | assess whether content sufficiently answers actual buyer needs and conveys distinguishing facts, without a word/spec-row quota; propose the fix, do not noindex money pages automatically |
| Internal links | related products, alternative products, and the parent collection linked; breadcrumbs present |

## Lifecycle decision tree

- Temporary stock gap: ordinarily retain a useful 200 page with truthful availability and appropriate restock/alternative information; do not automatically noindex.
- Restocked: verify actual availability, price and image, then update and read back.
- Permanently discontinued: retain a useful reference/support page when warranted; otherwise return 404/410 for genuinely removed content. No fixed deindexing deadline.
- Equivalent replacement: verify a relevant destination before a direct 301. A generic category/homepage is not a default substitute.
- Seasonal products: reuse useful stable URLs when the product returns; decide based on actual retained value, not an indexing guarantee.
- Bulk retirement: evaluate each URL and destination; do not redirect all retired SKUs to categories mechanically.

## Output format

1. **Template health summary** — 3-5 sentences on the PDP template as a system, not just the sampled pages.
2. **Sample table** — one row per URL: state (live / variant / out-of-stock / discontinued), key findings, `PASS`/`WARN`/`FAIL` per check group.
3. **Template recommendations** — developer-ready: Title formula with variables, description guidelines, content modules (spec table, FAQ block, media set), CTA placement, internal-link rules (related / alternative / parent collection).
4. **Complete JSON-LD** — one full `Product` example with every unknown or per-SKU value written as a template variable (`{{product.price}}`, `{{product.availability}}`), plus the variant strategy (`ProductGroup`/`hasVariant` or per-variant canonical) and the out-of-stock offer form. No fabricated ratings, prices, or review counts.
5. **Lifecycle decision tree** — the tree above instantiated with the user's actual states.
6. **URL action table** — one row per affected URL: current state, recommended action (keep / noindex / 410 / 301 → target), and the reason.
7. **P0-P3 priority list** — P0: schema violations, misleading stock signals, mass redirects to homepage; P1: variant duplication, stale offers; P2: content depth; P3: hygiene.

## Anti-hallucination rules

- Every finding cites an observed value from a fetched page or a feed row. Unfetched pages get no findings.
- JSON-LD contains only values from the page or feed; everything else is a template variable. Never invent ratings, review counts, prices, or GTINs.
- Do not recommend a 301 target that was not verified to exist (fetch or feed evidence).
- Out-of-stock and discontinued recommendations must match the actual state observed in step 2; when the user's description and the page disagree, report both.

## Failure handling

- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- Feed missing or unparseable → proceed with page-visible values only and state that feed cross-checking was not performed.
- Rate limit or balance error → keep completed results, stop, list what remains unverified.

For multiple pages, deduplicate shared keywords and query once, reusing overview fields. Use expansion only to discover needed new terms; never pay repeatedly for the same keyword per page.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=product-page-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
