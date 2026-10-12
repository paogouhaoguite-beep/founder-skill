---
name: marketing-roas-analyzer
description: Diagnose marketing performance, build evidence-backed search acquisition
  deliverables, and run a dated operating review using connected account data plus
  relevant DataForSEO evidence.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=marketing-roas-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Marketing performance, acquisition plan and review

> From [ShopChief](https://shopchief.ai/?utm_source=marketing-roas-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Use this skill for spend/ROAS diagnosis, a search acquisition plan, or a weekly operating review. Distinguish a new store with no conversions from an established campaign; no-data is not zero performance.

## Read and reconcile
Use current authorized Google Ads, GA4, Shopify/order and workspace data first. Other channels require an actually connected tool or supplied export; never imply Meta/TikTok access from a platform name. Align period, timezone, currency, conversion definitions, attribution window/lag, new vs returning customers and refunds. Keep platform attribution, GA4 attribution and order revenue separate. Do not assume a fixed 20–30% overlap or sum channel-attributed revenue into store revenue.

## Metrics
Platform ROAS = platform-attributed revenue / that platform's spend.
MER = actual store net revenue / the explicitly defined total marketing spend.
Break-even revenue ROAS = 1 / pre-ad contribution margin rate, only when the rate is positive and revenue/cost populations match.
Post-ad contribution = pre-ad contribution − ad spend. Do not deduct CAC again. Read available profit-margin-analyzer guidance when detailed unit economics are needed; if unavailable apply these definitions and state cost gaps.

## DataForSEO acquisition evidence
Read [query contract](references/dataforseo-contract.md) when demand, search terms or competitors could change an action. Reuse keyword overview/history, intent and current SERP for candidate terms; domain/keyword gaps for relevant competitors. These are external estimates, not the account's realized CPC/ROAS. Map selected terms to ad groups, negative-intent themes and actual landing products/pages. Use margin and measured conversion rate (or labeled scenarios) to assess affordable CPC. Do not query every family for a simple scorecard.

## Decide by business stage
- No/low data: check tracking and landing readiness; deliver a bounded validation plan with candidate groups, finished copy via available copywriting, landing asset requirements, a user-supplied budget cap, observation window and stop conditions. Do not infer failure from three days with few conversions.
- Existing campaigns: diagnose measurement, demand, query mix, creative, inventory and landing performance before reallocating. Recommend a specific change and its rationale, accounting for conversion lag/sample uncertainty; no universal ±20%/three-day rule.
- Weekly review: explain material movements in net revenue, spend, pre/post-ad contribution and funnel metrics. Prioritize a small actionable set with object, baseline, owner/available execution path and next check.

## Complete the work
Produce finished campaign/content inputs or a concrete change preview when requested, not only analysis. Use the current connected tool schema to execute only authorized writes; missing integrations still permit complete import-ready deliverables. Record successful writes and readback; report partial completion without duplicating writes. Save the dated evidence and decision for reuse. Create recurring monitoring only when requested, with schedule, metric/threshold and notification intent; never promise a future check without a saved automation.

Incrementality requires a valid comparison design and baseline adjustment; observational ROAS alone cannot establish causal lift. Do not direct experiments or budget changes without the authorized scope.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=marketing-roas-analyzer&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
