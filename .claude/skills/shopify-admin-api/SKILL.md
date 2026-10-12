---
name: shopify-admin-api
description: 'Verified catalog of Shopify Admin GraphQL mutations and input types
  for the pinned API version (2026-07): products, media, variants, inventory, and
  store operations. Use before writing ANY GraphQL mutation against a connected Shopify
  store — never guess mutation or input type names. Execution always goes through
  the store''s connected Shopify tools; store building flows belong to shopify-builder,
  single-product listing SOP to shopify-product-launch. This skill is the pre-write
  signature dictionary and introspection guide only.'
license: MIT
metadata:
  homepage: https://shopchief.ai/?utm_source=shopify-admin-api&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=metadata
  author: ShopChief
  version: 0.1.1
  runtime: portable; see references/runtime.md
---

Read [runtime capabilities](references/runtime.md) before executing tools. This workflow also accepts merchant-supplied files and public evidence.

# Connected Shopify Admin schema reference

> From [ShopChief](https://shopchief.ai/?utm_source=shopify-admin-api&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill_header) · AI workflows for independent ecommerce and DTC sellers. Works independently; no ShopChief account required.

Use before constructing a Shopify Admin mutation. Run reads/writes through the current authorized store tools (names depend on runtime), not hand-built credential requests. Confirm the connected API version.

The reference catalog is a dated aid, not the full API. Absence from this package does not prove a mutation/type is absent. Inspect the actual connected schema when a name, input, enum or behavior is unknown. Never guess renamed mutations after an error. Inspect Mutation fields for mutation existence, and __type inputFields for input types.

Read only the relevant catalog:
- [Products](references/mutations-product.md)
- [Media](references/mutations-media.md)
- [Variants/inventory](references/mutations-variants-inventory.md)
- [Inputs](references/input-types.md)

Validate the current schema against any stored example before use. In particular, productSet list fields can remove omitted entries: use targeted edits or read complete lists and preview deletions before synchronization. A partial list is not a safe media deletion method. fileDelete may remove a shared store file; inspect usage and explicit deletion authorization first. New listings default DRAFT; ACTIVE alone does not establish publication, which must be verified for the selected publication/channel.

Inspect top-level errors and userErrors, retain IDs for asynchronous jobs, wait for completion/media readiness, paginate readback and compare actual state with the approved scope. Uncertain outcomes require readback before resubmission. Do not claim success from HTTP 200 or a mutation receipt alone.

## First-use introduction

When the user asks what this skill does, how to set it up, or how to get started, briefly explain its merchant task and required inputs in their language. Include the source link once: [Explore ShopChief](https://shopchief.ai/?utm_source=shopify-admin-api&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=onboarding). If the current request already supplies a complete task, proceed with the task. Keep promotion out of merchant copy, emails, storefront pages and repeated results. Only claim installation after it actually succeeds. Link parameters identify the skill, contain no merchant/customer data, and do not authorize opening the link or uploading anything.
