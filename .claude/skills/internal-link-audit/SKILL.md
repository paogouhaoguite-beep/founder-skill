---
name: internal-link-audit
description: 'Use when the user wants an internal-link audit of a store site: crawl
  internal links with OnPage Content Parsing (initial sample up to 100 pages, suited
  to Shopify stores), report click depth, broken links, redirect chains and loops,
  find orphan pages with an explicit statement of which discovery channels were used,
  grade anchor text (descriptive / vague / mismatched), and deliver a concrete new-link
  table with source, location, target, recommended anchor, and semantic reason. Declared
  limitation: this skill does not compute or fabricate PageRank-like values. Do not
  use for page indexability problems (use site-seo-audit) or for designing the internal-link
  structure of a new topic-cluster plan (use seo-content-research).'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=internal-link-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.

## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# Internal Link Audit

> From [ShopChief](https://shopchief.ai/?utm_source=internal-link-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

## Overview

This skill audits how a store's pages link to each other and returns a fix list: which pages are buried or orphaned, which links are broken or looping, where anchor text misleads, and exactly which new links to add. Internal links distribute discovery and relevance; this skill measures the observable structure — links present in parsed HTML — and states its limits.

**Declared limitation:** this skill does not compute, estimate, or fabricate PageRank-like authority values. It reports link counts, depth, and anchor quality from the crawl it actually performed.

## Scope boundary

- Page indexability, canonical, robots, sitemap problems → `site-seo-audit`.
- Designing the internal-link structure for a new content plan (which pages should exist and link conceptually) → `seo-content-research`.
- Multiple URLs competing for one query → `keyword-cannibalization`.

## Required inputs

| Input | Required | Default if missing |
| --- | --- | --- |
| Site domain | yes | ask |
| Page list to include (or crawl from the sitemap/homepage) | recommended | seed from homepage + sitemap entries, within the declared crawl scope/budget |
| Priority pages (money pages: collections, products, key landing pages) | recommended | infer from URL patterns, state the inference |

## Required flow

1. **Crawl.** Use OnPage Content Parsing to parse internal and external links per page. Exploratory sample: up to **100 pages**, with scope and spend declared before crawling. Seed order: homepage → top navigation targets → sitemap entries → money pages. Record which pages were actually parsed; anything not reached is out of evidence.
2. **Build the link graph** from the parsed pages only. Compute: inbound link count per page, click depth from the homepage (following internal links), outbound links per page.
3. **Depth report.** Flag money pages at depth ≥ 4 and pages at depth ≥ 6. Depth is computed from this crawl's reachability; if a page is unreachable in the crawl, that is a separate finding (see 4), not an infinite depth.
4. **Broken links, redirect chains, loops.** From the parse: links pointing to 404/410, links through redirect chains (note the chain only if the parse exposes status; otherwise mark as "unverified status"), and self-referential or circular link patterns among parsed pages. Live-verify the highest-severity items with OnPage Instant Pages (budget cap applies).
5. **Orphan pages.** Pages present in the sitemap or user list but receiving no internal link from any parsed page. **Always state the discovery channels used** (sitemap, homepage crawl, user list) and that orphan status is relative to the ≤ 100-page crawl, not a guarantee of the whole site.
6. **Anchor text grading.** For each audited link (or the highest-value subset): **descriptive** (accurate in its source context; natural variations per target are valid), **vague** ("click here", "learn more", bare URLs), **mismatched** (anchor promises a different topic than the target page delivers). Propose a corrected anchor per flagged link.
7. **New-link table.** Concrete additions: source page | location on the page (module/section) | target | recommended anchor text | semantic reason (why this link helps a reader or a search engine understand the relationship). Prioritize links into orphan or deep money pages. Do not propose links between pages with no semantic relationship to pad counts.

## Output format

1. **Crawl scope statement** — pages parsed, seed order, date, cap reached or not.
2. **Depth & orphan report** — per flagged page: depth, inbound link count, status.
3. **Broken / redirect / loop findings** — with verification status.
4. **Anchor text grading table** — link | current anchor | grade | suggested anchor.
5. **New-link table** — source | location | target | recommended anchor | semantic reason.

## Failure handling

- Crawl cap reached: report the coverage (X of Y known pages) and scope all findings to the crawled set.
- OnPage Content Parsing fails for a page: note the page as unparsed; do not infer its links.
- Sitemap unreachable and no user list: state that orphan detection is limited to the crawled graph.
- Never fabricate authority scores, crawl budgets, or link counts not observed in the parse.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=internal-link-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
