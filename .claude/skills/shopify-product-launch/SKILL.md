---
name: shopify-product-launch
description: Prepare, create and verify Shopify product drafts from merchant facts
  and keyword evidence; preserve store conventions and publish only within explicit
  authorization.
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-product-launch&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Shopify product launch

> From [ShopChief](https://shopchief.ai/?utm_source=shopify-product-launch&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Turn current workspace product facts and assets into a verified Shopify draft, and complete publication only if requested and authorized. Reuse the current store brief and selected products. Never require sourcing when the merchant already has a product; procurement URLs are optional provenance.

## Prepare the launch sheet
1. Read current catalog/preferences and identify create vs update, product ID, store, market/language, currency, factual specs, variants, images, price and inventory/location. Ask once for blocking omissions; omit optional unsupported details. Supplier stock is not merchant inventory.
2. For search-led titles/SEO, reuse DataForSEO keyword evidence or read [query contract](references/dataforseo-contract.md) and query the relevant product/attribute terms when it changes wording. Prefer buyer intent and factual material over volume. No new research for a simple exact-field upload.
3. Deliver title, finished HTML description, SEO fields, handle, variant/SKU/price/image/inventory matrix and proposed tags/collections. Read [field rules](references/field-limits.md), [category playbooks](references/category-playbooks.md) and [SKU rules](references/option-axes-and-codes.md) only as applicable. Use the store's existing conventions; do not force a fixed story/FAQ or new SKU scheme.
4. Tags and collections follow the merchant's preferences and existing taxonomy. Respect explicit no-tags/no-collections requests. Otherwise propose relevant assignments for review; preserve existing values on updates and never clear them silently.
5. Use confirmed prices. Cost multiples and artificial compare-at prices are not defaults. Retain an existing handle unless a URL change is specifically requested; include a redirect plan for published URLs. Short readable handles and SEO character targets are editorial preferences, not fabricated platform limits.
6. Preview exact fields and scope, including inventory and channel changes. Preparation and workspace drafts need no additional brief approval. Follow the product's external-write confirmation rules; do not request approval twice for the same already approved payload.

## Execute and verify
Read [Shopify execution mapping](references/shopify-tool-mapping.md) and consult the available shopify-admin-api catalog/current schema. Use connected store tools, never chat credentials or ad-hoc token exchange.

Create in DRAFT. For updates use targeted operations; full-list synchronization requires a complete current list because omitted entries may be removed. Do not replace existing products with a partial variant/media list. Respect supported batch sizes; wait for async completion and media readiness. Inspect both errors and userErrors, then paginate readback across every affected variant/media item. Verify values, associations, counts and location-specific inventory against the approved launch sheet.

A timeout/partial result is not permission to recreate the product: read current state, record successful IDs and resume only missing operations within authorization. Do not publish an unverified draft.

## Publish and save
If publication is requested and authorized, set the appropriate product status and publish to the selected publication/channel using its actual ID. ACTIVE alone does not prove channel publication. Verify channel availability, URL/handle and storefront state, stating password/market restrictions if observed.

Save the verified launch sheet locally. Only inside ShopChief, optionally use an available authorized product-library tool after verification: inspect their actual schema; link the returned Shopify ID, preserve sourcing URL and captured provenance in supported fields. Do not assume nonexistent description/selling_points fields. Read back the workspace record when this optional sync runs. Without that integration, the local launch sheet is sufficient. If sync fails, keep the Shopify draft and report that distinct failure; do not recreate the listing. Save the launch sheet, evidence references and next check. Return product ID/URL, draft/published status, verified fields and any unfinished action.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=shopify-product-launch&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
