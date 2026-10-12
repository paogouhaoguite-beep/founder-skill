---
name: cwv-performance-audit
description: 'Mobile-first Core Web Vitals audit: measure LCP, INP, and CLS on representative
  templates (home, collection, product, article) with live Lighthouse runs, then trace
  each failing metric to a root cause — TTFB, images, fonts, critical CSS, third-party
  scripts, hydration cost, DOM size — and split fixes into frontend, backend, and
  design workstreams. Every metric is labeled lab or field, with tool, device, and
  test conditions recorded; missing CrUX field data is marked N/A, never estimated.
  Use when the user reports slow pages, poor PageSpeed scores, or wants a performance
  budget. Do not use for indexability, canonical, or structured-data checks (use site-seo-audit)
  or crawl and sitemap diagnostics (use crawl-index-audit).'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=cwv-performance-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Core Web Vitals Performance Audit

> From [ShopChief](https://shopchief.ai/?utm_source=cwv-performance-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

Mobile-first performance audit for LCP, INP, and CLS. The skill measures a small set of representative templates with real Lighthouse runs, attributes each failing metric to a concrete root cause, and splits the fixes by owner. Two rules govern everything:

1. **Lab and field are never mixed.** A Lighthouse run is lab data under stated conditions. CrUX-based field data (when present in the Lighthouse report or user exports) describes real-user experience. A finding must name which one it uses. No field data available → mark field view N/A; do not extrapolate lab numbers to "what users see."
2. **Every number carries its conditions.** Tool, device (mobile by default), network throttling, URL, and run date are recorded with each metric.

## Scope boundary

- Indexability, canonical, metadata, and structured-data checks → `site-seo-audit`.
- Crawl, robots, sitemap, and redirect diagnostics → `crawl-index-audit`.
- A slow page that is also not indexed: indexability first, speed second — a fast 404 helps nobody.

## Inputs

| Input | Source | If missing |
| --- | --- | --- |
| Representative pages, exploratory sample of 5 | user names them, or default to home + collection + product + one article/landing | state a representative default set and proceed within the query budget |
| Existing PageSpeed Insights / Lighthouse reports (optional) | user upload | run fresh OnPage Lighthouse instead |
| CrUX field-data export (optional) | user upload | mark field view N/A |
| Theme / app inventory (Shopify) | user lists installed apps, or visible script tags from Lighthouse report | derive the script list from the Lighthouse run |

## Required flow

1. Use the requested page set/device; otherwise state a representative mobile sample of up to 5. Complete explicit larger scope within the query contract.
2. State the plan: one OnPage Lighthouse call per page, one pass, per `references/dataforseo-contract.md`.
3. Run the measurements. Do not re-run the same page in the same pass.
4. Do root-cause analysis from the run output (blocking resources, long tasks, element-level LCP/CLS attribution).
5. Deliver the report with budget table and retest plan. Report writing does not trigger more paid calls.

## Measurements

| Metric | Read from | Notes |
| --- | --- | --- |
| LCP | Lighthouse performance section, element attribution | name the exact element and its resource |
| INP | Lighthouse (lab proxy: Total Blocking Time / long tasks) + field data if present | lab Lighthouse does not reproduce INP directly — label TBT as the lab proxy and say so |
| CLS | Lighthouse layout-shift attribution | list the shifting elements |
| TTFB | Lighthouse diagnostics + OnPage Instant Pages timing if needed | backend-owned |
| Supporting scores | Lighthouse category scores | point-in-time observation |

All runs are mobile, throttled, single-pass, unless the user explicitly asks otherwise — and then the changed conditions are recorded per run.

## Root-cause catalog

Trace each failing metric through this checklist; do not prescribe a fix before naming the cause:

- **TTFB** — origin time, caching headers, redirect before content, DNS/TLS on redirects.
- **Images** — LCP image not preloaded, oversized or unoptimized format, lazy-loading on the LCP element, missing dimensions causing CLS.
- **Fonts** — render-blocking font CSS, FOUT/FOIT contributing to CLS, no `font-display`.
- **Critical CSS / render blocking** — large stylesheets, blocking scripts in head, unused CSS volume.
- **Third-party scripts** — analytics, chat, A/B, review widgets; each blocking script is listed with what it is and what it blocks.
- **Hydration / framework cost** — long tasks and TBT after first paint; JS bundle size; main-thread work.
- **DOM size** — element count, deeply nested nodes, heavy carousels or mega-menus.
- **Layout instability** — late-loading banners, injects above content, dimensionless embeds.

On Shopify specifically: theme app scripts (reviews, upsell, chat, tracking apps injected by apps) are the most common INP/TBT culprit. List every app-injected script before proposing code changes — uninstalling or reordering an app is often cheaper than refactoring the theme.

## Output format

1. **Metric table** — one row per page: URL, template, LCP / INP-lab-proxy (TBT) / CLS values, data type (lab / field), tool, date. Missing values N/A with reason.
2. **Root-cause table** — per failing metric: metric, page(s), named cause, evidence from the run (resource name, timing, byte weight).
3. **Task split** — fixes grouped by owner: frontend (image, CSS, JS, font work), backend (TTFB, caching, redirects), design (layout stability, above-the-fold decisions). Each item: cause it addresses, expected metric impact band (qualitative: high/medium/low), effort band.
4. **Performance budget table** — per template: target LCP / TBT / CLS / total JS / image weight / third-party script count, plus which budget exists today vs target.
5. **Fixed-conditions retest plan** — same tool, same device, same throttling, same URLs, single-pass, after each fix batch; record deltas per metric and keep lab and field reported separately.

No SEO ranking claims in this report. If the user asks "will this improve rankings," answer that CWV is a confirmed but minor, query-dependent signal and stop there.

## Failure handling

- On query failure follow `references/dataforseo-contract.md`; retain successful results and mark gaps without automatic paid retries.
- No field data: field view N/A — the report says lab results only.
- configured DataForSEO tools unavailable: work from user-provided PSI/Lighthouse exports; if none, the audit cannot run and the deliverable is a measurement plan, not invented numbers.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=cwv-performance-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
