---
name: supplier-finder
description: Find supplier candidates, compare evidenced procurement conditions and
  prepare sample checks using authorized Sorftime or public sources.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=supplier-finder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Supplier feasibility and sample preparation

> From [ShopChief](https://shopchief.ai/?utm_source=supplier-finder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Compare supply for the selected product and requested quantity. Use an authorized Sorftime ali1688_similar_product capability if actually available; otherwise use public web search/fetch for procurement directions and verifiable supplier candidates. State which route is available before research. A connector is not a guarantee of supplier reliability.

For Sorftime responses:
- A zero price is not free. Select a valid wholesale_price_range tier for the requested quantity; if absent, mark price unknown.
- Interpret MOQ from wholesale_price_range purchase_quantity ranges. Do not trust the nearly constant min_order_quantity=1 without support. Ambiguous ranges require supplier confirmation.
- Exclude entries with no valid price/tier and missing store/inventory information. Do not infer a fixed failure percentage from earlier samples.
- shipping_time has returned city names; do not present those as lead times. List-level material, dimensions and compliance documents are unavailable unless separately verified.
- offer_identities/seller_identities are supplier badges, not product certification. Repurchase rate and service scores are risk proxies, not logistics or quality guarantees.
- Inspect truncation and pagination; request relevant fields and pages rather than treating a truncated list as complete.

Return actual product links, quotes/currency/quantity tiers, supported MOQ, available supplier indicators, missing conditions and a sample-inspection checklist. Check links using available tools; mark unchecked or failed links and do not prioritize failed ones. Public candidates alone do not establish orderability, sample availability, lead time or compliance. Never invent suppliers or fill missing conditions. Do not contact suppliers, order samples or make payments without explicit authorization.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=supplier-finder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
