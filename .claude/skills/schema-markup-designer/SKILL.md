---
name: schema-markup-designer
description: 'Two jobs in one skill: (1) audit the structured data already on sampled
  pages by reading source JSON-LD, checking type coverage, @id entity reuse, required/recommended
  properties, and consistency with visible content; (2) design complete, deployable
  JSON-LD for the missing types. Hard rule: markup may only restate what the page
  visibly shows — no invented ratings, prices, or reviews. Every template is validated
  against the official schema.org / Google Rich Results guidelines with tool and date
  recorded; unknown optional values are omitted; missing required facts block deployment.
  On Shopify the focus is Product/Offer agreeing with the visible price and stock
  state. Use when the user asks for rich results, Product/Organization schema, or
  a structured-data audit. Page-level SEO basics (titles, meta, headings) use site-seo-audit;
  product page copy structure uses product-page-seo.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=schema-markup-designer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Schema Markup Designer

> From [ShopChief](https://shopchief.ai/?utm_source=schema-markup-designer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

Structured-data audit plus deployable JSON-LD design. Two jobs:

1. **Audit** — read the JSON-LD actually present in the source of sampled pages; report type coverage, entity linking via `@id`, required and recommended properties per Google's feature requirements, and whether markup agrees with what visitors see.
2. **Design** — write complete, ready-to-deploy JSON-LD for missing or broken types, with every unknown value left as a `[TBD]` placeholder for the user to fill.

Non-negotiable rule: **markup may only restate visible page content.** A rating, price, availability, or review count that the page does not visibly show must not appear in markup. Fabricated values in structured data are a manual-action risk and are refused.

## Scope boundary

- Page basics — title, meta description, headings, canonical, indexability → `site-seo-audit`.
- Product page content structure — copy blocks, benefit ordering, A/B testing of product copy → `product-page-seo`.
- Rich-result eligibility assumes the page is indexable; if the sample shows canonical or noindex problems, flag them and hand off rather than designing markup for a page Google will not index.

## Inputs

| Input | Source | If missing |
| --- | --- | --- |
| Sample URLs, ≤ 6 (home, a collection, 1-2 products, a blog post, a policy page) | user or defaults | state a representative sample from the known store |
| Existing markup | All relevant JSON-LD blocks/microdata extracted from public HTML or rendered DOM, or a documented raw-markup extraction response | mark extraction unavailable as unverified; report no markup only after successful extraction with stated coverage |
| Visible price / stock / rating on product pages | public page or rendered DOM for the same market and variant | mark unavailable observations as unverified; compare against extracted markup |
| Business facts (brand name, logo URL, sameAs profiles, support contacts) | user | omit optional unknowns; missing required facts block deployment |

## Required flow

1. Confirm the URL sample and store type (Shopify or custom).
2. State the extraction plan per sample URL. Prefer available public HTML; render only when required. Add documented OnPage diagnostics through `dataforseo_api_request` only for missing decision-relevant evidence, per `references/dataforseo-contract.md` (exploratory sample of 6; explicit scope follows the query contract).
3. Extract all relevant JSON-LD blocks and any microdata from the actual source/DOM; parse types, `@id` graph and properties. Record URL, time, source and extraction coverage. Do not treat ordinary OnPage content or markup-presence flags as full markup; failed/partial extraction stays unverified.
4. Compare markup vs visible content on product pages (price, currency, availability, rating count).
5. Write the audit table, opportunity list, and templates. Validation of templates is a desk exercise against official guidelines — record tool and date, no extra paid calls.

## Audit checks

| Check | What to read |
| --- | --- |
| Type coverage per template: which of Organization / WebSite / BreadcrumbList / Product / Offer / AggregateRating / Review / FAQPage / Article are present | source JSON-LD |
| Entity reuse: one `@id` per entity (Organization, WebSite, each Product) referenced across the graph instead of duplicated inline objects | source JSON-LD |
| Required + recommended properties per Google Rich Results spec for each type | source JSON-LD vs spec |
| Markup vs visible content: price, currency, availability, rating value and count, review count | source JSON-LD vs rendered content |
| Syntax validity: parseable JSON-LD, correct `@context`, no conflicting duplicates (e.g., two Product objects for one product) | source JSON-LD |
| FAQPage / HowTo used only where the content is genuinely on-page | rendered content |
| Stale or orphan markup (types for content that no longer exists) | source JSON-LD vs page |

## Type coverage guide

Design markup for these types, in this priority order for a Shopify/DTC store:

1. **Organization** — name, url, logo, sameAs array. One `@id`, referenced everywhere.
2. **WebSite** — name, url, references Organization by `@id`.
3. **BreadcrumbList** — matches the visible breadcrumb trail exactly.
4. **Product + Offer** — the money pair. Product: name, description, image, sku, brand, gtin/mpn if real. Offer: price, priceCurrency, availability (from real stock state), url, itemCondition. AggregateRating and Review **only** if real ratings/reviews are visible on the page.
5. **AggregateRating / Review** — conditional; never invented. If reviews live on a third-party widget that does not expose them to the page, say so and mark N/A.
6. **FAQPage** — only where a real FAQ is visible; Google discontinued FAQ rich results in May 2026; do not claim Google rich-result eligibility or GEO benefits from this type.
7. **Article / BlogPosting** — for blog templates: headline, image, datePublished, dateModified, author.

## Output format

1. **Coverage summary** — per template: types present / missing / broken, with one-line verdicts.
2. **Consistency checklist** — per product page sampled: price, currency, availability, rating, review count — markup value vs visible value, MATCH / MISMATCH / MISSING-ON-PAGE.
3. **JSON-LD templates** — one complete block per type, with `@id` wiring, omit unknown optional properties; if a required fact is missing, label the block as a non-deployable draft. Put source explanations outside the JSON; no inline comments or placeholder literals in deployable JSON-LD.
4. **Deployment notes** — where each template goes (theme section, template file, app), Shopify-specific placement (e.g., product template for Product/Offer, not injected globally), and how to avoid double-emitting alongside theme default markup.
5. **Validation checklist** — validate every deployed block with the official validator(s) (e.g., Google Rich Results Test / Schema Markup Validator), record tool name and validation date per URL, then watch Search Console enhancement reports over the following weeks.
6. **P0-P3 roadmap** — P0: markup contradicting visible content or syntax-broken Product/Offer; P1: missing Product/Offer/Breadcrumb; P2: Organization/WebSite/Article; P3: conditional types and enrichments.

## Failure handling

- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- No existing markup found: report it as the audit finding; proceed straight to templates.
- Data unavailable for a property (e.g., no gtin): omit optional properties; block deployment when required facts are missing — never guess.
- Validation tool unavailable: label templates "syntax-reviewed, not yet validated" with the date of review.

Deployable JSON-LD must parse as JSON with no comments or placeholder values. Omit unknown optional properties; missing required facts make it a non-deployable draft. Put source notes outside the code block.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=schema-markup-designer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
