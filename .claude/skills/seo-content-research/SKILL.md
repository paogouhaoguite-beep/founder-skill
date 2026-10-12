---
name: seo-content-research
description: Use for an already-listed or already-selling product when the user needs
  SEO content direction, topic and outline research, programmatic keyword matrices,
  UGC/category content angles, keyword-to-page mapping, briefs, or prioritization.
  Evidence is collected directly with built-in DataForSEO tools and public web research
  under this skill's data contract. Keyword metric lookups (volume, KD, CPC, intent
  for a given list) use the keyword-analysis skill. Domain health and technical audits
  use site-seo-audit. Do not produce a Go, Test, or No-go product opportunity decision.
  Blog-specific keywords and article briefs use blog-keyword-research; complete article
  writing from a keyword/brief uses blog-article-writer. This skill retains cross-page
  content strategy and non-blog planning. Pass existing evidence; if a specialist
  is unavailable complete the requested supported deliverable here.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=seo-content-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

Read [the SEO/GEO execution and delivery contract](references/seo-workflow.md) and [verified rule baseline](references/seo-rule-baseline.md); share issue IDs, evidence and review baselines.
For search research, read [the provider and evidence contract](references/dataforseo-contract.md). Use an available authorized provider client or dated merchant exports; API capability labels are research targets, not tool names.


## Query and delivery contract

Read [DataForSEO contract](references/dataforseo-contract.md) before paid calls. Plan from the user decision and store market/language, reuse workspace evidence and inspect actual tool schemas. Numeric samples below are exploratory starting points: complete an explicitly requested batch/multi-market scope within budget/provider limits without duplicate approval. Actual provider limits still apply. Prefer authorized connected data; use exports for gaps and never assume GSC is connected. References to an export below mean the equivalent dated evidence table; connected rows with the same fields also qualify. Save evidence, concrete page/field actions and verification baselines; continue requested content/repair work into finished artifacts or reviewable changes.

# SEO Content Research

> From [ShopChief](https://shopchief.ai/?utm_source=seo-content-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Use this lightweight Skill for products that already exist in the catalog or market. The outcome is a focused SEO content plan, not a product opportunity verdict.

## Required flow

1. Read `references/research-contract.md` and `references/delivery-template.md` in one parallel file-read batch. Their paths are known and independent. Do not enumerate the Skill directory.
2. Reuse the product, price, target market, channel, performance signals, and brand context already supplied. Ask only for a decision-critical omission.
3. Collect evidence directly with built-in DataForSEO tools and public web research, through the three research routes below. Choose only the routes that change the content plan; state the route plan before the first paid call.
4. Prefer existing workspace facts and current public evidence. Paid DataForSEO requests follow the caps in `references/dataforseo-contract.md` — no automatic retries or market expansion.
5. Synthesize into the delivery template. Do not reread references, enumerate directories, or repeat research unless one specific fact is missing.
6. Deliver content directions, intent clusters, page mapping, briefs, priority, evidence, assumptions, and unchecked items.

## Research routes

Pick routes by the question being answered. Route A uses available public research; access and cost depend on the connected tools; Routes B and C are DataForSEO and bounded by the contract.

### Route A — Topic and outline research (available public sources)

Public web research plus workspace context: what the audience asks, how competitors frame the product category, which formats rank for the core question, and what the existing store already covers. Output: topic candidates, angles, outline skeletons, and the intent each serves.

### Route B — Programmatic SEO keyword matrix (low cost, DataForSEO Labs)

When the plan needs a scale pattern (many pages from one template: sizes, colors, use cases, "best X for Y"):

- DataForSEO Labs Google related keywords — expansions around a seed term.
- DataForSEO Labs Google keyword suggestions — long-tail variants containing the seed.
- DataForSEO Labs Google historical keyword data — 12-month seasonality before committing a template.

Build the matrix: pattern → keyword list → per-keyword intent → page template. Start with a focused sample and complete the declared research scope within the query contract; persist the evidence and page mapping.

### Route C — Category content sentiment and UGC topics (medium cost, on demand)

When the plan needs the audience's own language and pain points as topics:

- Content Analysis search — citations and sentiment around a category keyword.
- Content Analysis phrase trends — how phrase attention moves over time (dates required).

Use on request or when Route A leaves the audience language ambiguous; state the keyword and date range before calling.

## Delegation boundary

- **Keyword metric lookups** — a given list needs volume, KD, CPC, competition, or intent values → the `keyword-analysis` skill. This skill uses those numbers only as returned context; it does not re-query them itself.
- **Domain audits** — indexability, Lighthouse, backlinks, AI visibility → `site-seo-audit`.
- **Product opportunity verdicts** — a new product or new-market entry question, Go / Test / No-go → `product-opportunity-research`. Do not invoke it and do not output a verdict unless the user separately asks.
- Research alone does not authorize publication, storefront edits, budget changes or automations. When the user already requested the next action, prepare the concrete deliverable and execute through the existing authorization flow without asking again for the same permission.

## Output

Follow `references/delivery-template.md`: recommended content direction first, then the priority plan, page mapping, briefs, and boundaries. Evidence notes must state market, observation date, and endpoint family for every DataForSEO number.

## Finished content and reuse

Map evidence to real products and existing pages; prioritize intent, product fit, attainable competition and business value. A topic-only request ends with briefs; when the user asks for an article, landing page or product copy, continue through available writing capabilities to complete the content, not only the outline. Keep claims/source discipline, save evidence, finished content and internal-link targets, and preview publication under existing authorization rules. Later reviews use the saved query/page baseline and connected data instead of repeating research.

## Specialist routing
Blog-specific keywords and article briefs use blog-keyword-research; complete article writing from a keyword/brief uses blog-article-writer. This skill retains cross-page content strategy and non-blog planning. Pass existing evidence; if a specialist is unavailable complete the requested supported deliverable here.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=seo-content-research&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
