---
name: international-seo-audit
description: 'Audit international / multi-language stores: ccTLD vs subdomain vs subdirectory
  architecture and its cost; hreflang bidirectional return links, x-default, self-referencing
  tags, and invalid codes; canonicals wrongly pointing at the primary language; auto
  IP/language redirects that block crawlers; and currency, units, address, regulatory,
  and local search-intent localization. Use when the user runs one store in several
  countries or languages and asks why the German/JP/other market page does not rank,
  how to structure markets, or whether hreflang is correct. Multi-currency checkout
  configuration requires actually connected store capabilities; single-market SEO
  uses site-seo-audit — this skill covers the cross-market layer only.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=international-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# International SEO & Hreflang Audit

> From [ShopChief](https://shopchief.ai/?utm_source=international-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

One store, many markets: the usual failure modes are hreflang clusters that do not close, canonicals that funnel every language to English, and auto-redirects that show Googlebot the wrong market. This skill samples language/regional versions page-group by page-group (an exploratory sample of 30 groups) and produces a health summary, a page-group matrix, an error table, working hreflang code or sitemap XML built from the store's real URLs, market keyword and localization gaps, architecture advice, and a monitoring checklist.

## Scope boundary

- For multi-currency payment and checkout configuration inspect actual connected tools; if unavailable provide a scoped setup preview and state the limitation. This skill checks currency display and unit localization on the page as SEO-relevant localization only.
- Single-market SEO health (one locale, no cross-market layer) → `site-seo-audit`.
- Product and collection page content depth → `collection-page-seo` / `product-page-seo`. This skill reads their output (URLs, canonicals) but does not re-audit their templates.
- This skill evaluates localization quality only where it affects ranking or crawlability: visible currency/units/address/coverage, local keyword intent, and market-specific regulation text (e.g. VAT-inclusive pricing, consumer rights). It does not translate content.

## Required inputs

| Input | Required | Notes |
| --- | --- | --- |
| Market list | required | countries and languages the store targets (e.g. US/en, DE/de, JP/ja) |
| URL architecture | required | ccTLD, subdomain, or subdirectory per market; say "unknown" and it will be detected from samples |
| Page groups to sample | required | an exploratory sample of 30 groups; a group = one theme across markets (e.g. homepage, one collection, one product, one policy page) |
| Known language-switcher behavior | recommended | auto-redirect? geo selector? cached? |
| Market keywords | optional | the queries that matter per market; otherwise derived from the store's product categories |

For unspecified scope, prioritize a representative sample. Complete a larger explicitly requested scope in internal batches within the query contract.

## Workflow

1. **Confirm inputs and state the plan.** List the page groups, the URLs per group, and rough call count before the first paid call (see `references/dataforseo-contract.md`).
2. **Fetch samples.** Run OnPage Instant Pages on one representative URL per market per group — not every URL in every group. Use a non-geo IP tool context: if the page serves different content by IP, note it explicitly rather than trusting the US view. Exploratory sample: 30 page groups; complete an explicitly requested larger scope within the query contract.
3. **Read the international signals** per fetched page: status code, `lang` attribute, canonical target, hreflang set (including `x-default` and the self-referencing tag), and whether the language switcher is a real link crawlable by Googlebot.
4. **Close the cluster.** For each hreflang set, verify every listed URL exists, returns 200, and links back. A cluster with a one-way tag is a broken cluster, not a partial success.
5. **Market keyword gaps.** For each market's priority queries, one low-cost pass with Keywords Data DataForSEO Trends subregion interests (or DataForSEO Labs data) to compare demand across markets. Localized SERP differences are reported only with evidence: name the query, the market, and what the observed result set differs in.
6. **Deliver the report.** One consolidated report.

## Checks

| Check | What good looks like |
| --- | --- |
| Architecture fit | the structure matches the business: ccTLD for strong local presence, subdirectory for shared authority with lower cost — the recommendation weighs budget, team, and current rankings |
| hreflang cluster | every URL lists all siblings + itself (`hreflang="de-de"` on the German page included) + `x-default`; all codes are valid ISO 639-1 + ISO 3166-1 |
| Return links | bidirectional: every page listed in a cluster actually points back to the set |
| Canonical | each market URL self-canonicals; no canonical pointing at the primary-language version "to consolidate" |
| Auto redirects | no IP/language auto-redirect serving Googlebot a different market; a geo banner or selector with crawlable links instead |
| Language switcher | `<a href>` links to each market version (Googlebot-readable), not a JS-only dropdown |
| Currency and units | prices shown in the market's currency, units and sizes localized, VAT/tax display matching local norms |
| Address and coverage | shipping destinations, returns, and contact details reflect the market |
| Regulation text | consumer rights, returns windows, and privacy notices match the market's norms |
| Local intent | page copy and keyword targeting match how that market actually searches (checked against step-5 evidence) |
| Sitemap | each market's URLs are in a sitemap; hreflang sitemap used when clusters are large |

## Output format

1. **Health summary** — 3-5 sentences: overall cross-market state and the 2-3 findings that matter most.
2. **Page-group matrix** — one row per URL: theme | country-language | URL | status code | `lang` | canonical target | hreflang count | return-link status | indexable. Include every checked URL; save long tables as a complete artifact.
3. **Error table** — every broken cluster, mis-canonical, or blocked-crawler finding: URL pair, what is wrong, impact, fix.
4. **Working hreflang code** — corrected `<link rel="alternate">` set or a hreflang sitemap XML block, built from the store's real URLs fetched in step 2. Never emit a URL that was not observed.
5. **Market keyword and localization gaps** — per market: demand comparison from step 5 (labeled as DataForSEO estimates with location/language) and content-localization differences, each backed by observed SERP or page evidence. No gaps without evidence.
6. **Architecture and region-selector recommendations** — keep / migrate / consolidate advice with cost and migration-risk notes, and the geo-handling design (banner + crawlable links vs selector page).
7. **Monitoring checklist** — what to re-check monthly (cluster closure, canonical drift, redirect behavior per market).

## Anti-hallucination rules

- Every matrix row cites an observed fetch. Unfetched URLs never appear in the hreflang output — placeholder comments only.
- Hreflang code uses real fetched URLs; where a sibling page was not fetched, emit a `<!-- verify: not fetched -->` comment instead of a guess.
- SERP and demand differences are reported only when the step-5 evidence names them. Do not assert "Germans search differently" without a query-level observation.
- Architecture recommendations state their assumptions (budget, team, existing rankings); they are advice, not measurements.

## Failure handling

- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- Geo-serving makes results unstable (two fetches disagree) → report geo-serving as the finding and base recommendations on the Googlebot-view fetch.
- Keywords Data DataForSEO Trends subregion interests returns no data for a market → mark demand comparison unavailable for that market; do not extrapolate from another market.
- Rate limit or balance error → keep completed results, stop, list what remains unverified.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=international-seo-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
