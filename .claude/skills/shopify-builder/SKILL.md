---
name: shopify-builder
description: Build and adjust the connected Shopify storefront with scoped previews
  and verification; route product listing to the product-launch workflow.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-builder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Shopify storefront work

> From [ShopChief](https://shopchief.ai/?utm_source=shopify-builder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Build or adjust a connected merchant storefront: homepage sections, banners, seasonal copy and existing product presentation. Read the current store, theme, assets, merchant preferences and authorized scope first. Check the current client's authorized Shopify connector or CLI. If missing, prepare local theme files or an import draft and explain the client's documented connection setup; never ask for secrets in chat. ShopChief's connection UI is relevant only when actually running inside ShopChief.

## Routing and preparation
Product creation/launch follows the available shopify-product-launch workflow; do not duplicate its pricing, variant or publication rules. GraphQL writes use the current schema and available shopify-admin-api reference. If a named skill is unavailable, inspect actual tools and produce a complete preview; do not claim to have invoked it.

For a storefront request, inspect the actual theme structure and visible page before selecting changes. Deliver final section copy and selected/generated asset references. Use available copywriting/image skills where needed and reuse market/keyword evidence if it changes the page; do not require sourcing or supplier contact discovery for a theme change.

## Execute within scope
Preview the specific theme/section/setting changes. Use connected tools only after the required authorization. Preserve unrelated block IDs, settings and content; prefer a supported draft/unpublished theme when relevant. Never inject a marquee or change global colors unless requested or included in the approved design. No arbitrary markup multiples, artificial compare-at prices or automatic publication.

Read back the changed settings/assets and inspect the resulting page, checking mobile layout, image readiness, links and cart path as relevant. Distinguish a stored asset from a visible storefront change. If theme writes are unavailable, deliver the exact reviewable files/instructions and state the execution limitation. Save results to the workspace, with changed object IDs, preview URL and unresolved issues. Product publishing and theme publishing are separate authorized operations.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=shopify-builder&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
