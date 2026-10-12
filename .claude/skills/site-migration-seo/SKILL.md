---
name: site-migration-seo
description: 'Produces the review and implementation package for a site migration
  — replatforming, redesign, domain change, CMS move, or URL restructuring — so no
  URL equity is lost. Core is a one-to-one 301 mapping table where each old URL goes
  to the new URL with the closest matching intent and content (blanket redirects to
  the homepage are refused), plus a conflict table for many-to-one, one-to-many, unmatched,
  chained, and circular cases, an old/new template equivalence check, Nginx/Apache/Cloudflare
  rule examples, pre-launch / launch-day / post-launch-1-90-day checklists, GSC Change
  of Address guidance, and rollback triggers. The skill does not execute the launch
  or DNS changes — it only produces files for human review and implementation. Shopify
  focus: URL structure differences (/collections/.../products) and Shopify-compatible
  redirect implementation via admin URL Redirects and CSV import. Use before or during
  a migration; the new site''s content health audit afterward uses site-seo-audit,
  and product URL.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=site-migration-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Site Migration SEO

> From [ShopChief](https://shopchief.ai/?utm_source=site-migration-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

Migration planning for redesigns, replatforms, domain changes, CMS moves, and URL restructuring. The deliverable is a complete review-and-implementation package whose goal is stated up front: **no URL loses its equity.** Every old URL either maps one-to-one to its best new counterpart, or is explicitly retired with a documented reason.

This skill produces documents only. It does not execute the launch, touch DNS, deploy redirect rules, or press any button on either site — every artifact is handed to the user for review and implementation.

## Scope boundary

- Content health of the new site after go-live (indexability, structured data, performance) → `site-seo-audit`.
- Decisions about retiring, consolidating, or restructuring individual product URLs for content reasons → `product-page-seo`.
- Redirect destination pages still need to rank: their on-page work is not this skill's job.

## Inputs

| Input | Source | If missing |
| --- | --- | --- |
| Old site URL (and staging/new site URL) | user | required — no plan without both |
| Migration type | user states: redesign / replatform / domain change / URL restructure / CMS move | required |
| Old URL list | user export: site crawl, GSC pages report, GA4 landing pages, or backlink export | ask user; a partial list must be labeled as partial — never presented as complete |
| New URL list | user export or sitemap of staging site | ask user |
| URL importance weights (traffic, links, revenue) | GSC/GA4/backlink exports, user-ranked | rank by user judgment, note the basis |

A crawl or export that covers only part of the old site is a partial inventory. The plan must say so and define what "complete" would require.

## Required flow

1. Confirm migration type, both site URLs, and go-live target.
2. Collect the URL lists and state their coverage honestly.
3. Build the mapping table — this is the core artifact; see rules below.
4. Resolve conflicts, check template equivalence, write the server rules.
5. Assemble the three checklists, GSC Change of Address steps, and rollback triggers.

## The mapping table

One row per old URL: `old URL | new URL | status (301 / retire / monitor) | rationale | traffic/link weight | notes`.

Mapping rules:

- **One-to-one, intent-and-content-nearest-match.** Each old URL maps to the new URL that most closely serves the same search intent and content — not merely the most similar string.
- **Never blanket-redirect to the homepage.** An old URL with no good counterpart defaults to a *retire* decision with rationale, not a homepage redirect. If the user insists on a homepage fallback, it is recorded as their explicit, risk-accepted exception.
- **Preserve template-level intent:** products → products, collection → collection, blog post → blog post, unless the user has a documented content decision.
- **Retired URLs** get a rationale and, where a related category exists, that category is the destination — chosen per URL, not by wildcard.

## Conflict table

Every case below is listed explicitly with resolution:

| Conflict | Definition | Resolution approach |
| --- | --- | --- |
| Many-to-one | Multiple old URLs map to one new URL | allowed only when the old URLs truly duplicate; otherwise split |
| One-to-many | One old URL matches several new candidates | user decides; record the choice |
| No match | No reasonable new counterpart | retire, with rationale and optional category destination |
| Chained redirects | New site already redirects the destination further | flatten to a single 301 to the final destination |
| Circular | Mapping creates A→B→A | re-map manually before launch; must be zero at launch |

## Template equivalence check

Sample pages from both sites (≤ 10 per side, via OnPage Instant Pages per the contract file) and compare per template: indexable content blocks present, heading structure, internal linking, canonical pattern, structured data. Differences that change what Google can index or how equity flows are flagged as launch blockers, not cosmetic notes.

**Shopify focus — URL structure differences:**

- Shopify forces `/products/<handle>` and `/collections/<handle>` (and `/collections/<collection>/products/<handle>` inside collection contexts). Old URLs rarely match — this drives the mapping, not a technical afterthought.
- Product handles are editable in Shopify; set them deliberately to shorten the redirect list where a clean match is possible.
- Shopify's native **URL Redirects** (admin, with CSV import/export) support exact-match redirects only — no regex, no wildcards. Bulk old inventories mean one row per URL; plan the CSV accordingly.
- Anything beyond exact matches (parameter cleanup, folder moves) needs a CDN/edge layer (e.g., Cloudflare rules) in front of Shopify — flag as infrastructure dependency.
- Canonicalization: Shopify emits its own canonicals; new URLs must match Shopify's canonical pattern or the redirects will fight the platform.

## Server rule examples

Deliver ready-to-review snippets (commented, clearly marked as examples to review, not auto-deploy):

- **Nginx:** `location`-scoped `return 301` blocks, ordered most-specific first.
- **Apache:** `.htaccess` `RewriteRule` / `RedirectMatch` block with `RewriteEngine On` guard.
- **Cloudflare:** Bulk Redirect List / redirect rule structure, noting it sits in front of origin redirects.
- **Shopify admin:** URL Redirects CSV format (`Redirect from`, `Redirect to`), import steps, and the exact-match limitation restated.

Rules are written so that no chain can form: every rule targets the final destination.

## Checklists

**Pre-launch (staging):** mapping table complete and reviewed; conflict table resolved to zero chains/cycles; template equivalence blockers closed; staging robots.txt strategy ready (block staging, unblock production); backups taken; redirect rules tested against a real sample (each test URL resolves in one hop, 200 at the end); performance spot-check of the new templates.

**Launch day:** deploy redirects before or with the DNS/content cutover, never after; verify sitemap reflects only final new URLs; check sample of 20 mappings live (single-hop 301, destination 200); GSC: submit new sitemap, run Change of Address (domain-change migrations only); watch error rates.

**Post-launch, days 1-90:** daily for week 1 then weekly — GSC coverage deltas vs baseline, 404/soft-404 spikes, crawl stats, rankings for the top weighted URLs, organic traffic vs pre-migration baseline; weeks 2-6: fix newly discovered missing mappings (404s with traffic); day ~30 and ~90: formal review vs rollback triggers; keep old-domain registrations and redirects alive for the agreed period, stated in the plan.

**Rollback triggers (defined before launch, not after):** sustained traffic drop beyond an agreed threshold at day 7/30, mass deindexing of previously indexed URLs, or GSC coverage collapse — each with the pre-agreed action (investigate / revert DNS / restore snapshot).

## Output format

1. **Migration brief** — type, both sites, go-live target, URL-list coverage statement.
2. **Mapping table** — the full one-to-one table with status and rationale per row.
3. **Conflict table** — every many-to-one / one-to-many / no-match / chain / cycle with its resolution.
4. **Template equivalence report** — sampled comparisons and launch blockers.
5. **Server rule examples** — Nginx / Apache / Cloudflare / Shopify CSV snippets, marked for review.
6. **Three checklists + rollback triggers** — pre-launch, launch day, days 1-90.
7. **GSC Change of Address steps** — applicable only for domain changes; omitted otherwise, with a note why.

## Failure handling

- URL lists missing or partial: state coverage in the brief; the mapping table is marked "partial inventory" and the plan names what is needed for completeness.
- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- configured DataForSEO tools unavailable: template equivalence falls back to user-provided exports and screenshots; mapping and checklists proceed regardless.
- For requested execution, prepare exact changes first and inspect available tools/authorization. Execute only supported approved actions, verify them, and clearly mark manual steps; never claim unsupported DNS or server access.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=site-migration-seo&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
