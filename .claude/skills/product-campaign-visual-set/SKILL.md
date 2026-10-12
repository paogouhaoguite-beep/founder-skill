---
name: product-campaign-visual-set
description: "Produce a coordinated campaign asset set for storefront banners, email and social placements using a shared product identity, approved offer and exact validity period."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Campaign Visual Set

Produce a channel-ready visual set from one approved campaign, keeping product identity, offer conditions and timing consistent. Own the asset matrix and cross-format acceptance; a single ad key visual or distribution calendar does not complete the set.

## Required inputs

Campaign ID; product/SKU references; approved key visual if any; exact offer, code, eligible products and exclusions; start/end time with timezone where time-bound; exact copy per locale; placement dimensions/crop rules and brand artwork. Separate approved offer facts from proposed visual treatments.

## Execute with available tools

Read [production notes](references/production.md) for capability checks and identity handling, and adapt the complete [worked example](assets/worked-example.md). Inspect actual input images before composing the request. Discover the currently callable image tool and read its schema; verify reference-image input, editing scope, output handling and any required feature before calling it. Use the user’s authorized provider/tool when specified. Do not invent a tool name, model, parameter, supported size or paid retry budget.

When a suitable tool is available, call it and visually inspect the returned image; a prompt alone is not the requested production output. Map every result back to its exact input assets. Repair failures within the authorized scope and budget; if the same fidelity problem persists or the budget is exhausted, stop and report the failed item. With no suitable tool, deliver the final prompt, reference manifest and layout as `not_generated`, with missing capabilities identified. If pixels cannot be inspected, use `generated_unreviewed`, never `verified`.

## Production sequence

1. Build an asset matrix: placement, aspect/dimensions, locale, product, copy, offer/conditions, validity and required output. Treat an unknown discount, timezone or offer eligibility as unresolved; do not calculate a countdown from an ambiguous end date.

2. Create one identity/style anchor using supplied artwork or an available reference-aware image tool. Lock the product and shared palette/light/graphic motif. Confirm the anchor’s product fidelity before expanding into the requested placements.

3. Generate/recompose each image with the same identity references and anchor. Wide banners, email panels and vertical social images need different product/text regions; do not force every placement into a center crop that removes terms or the product.

4. Use available text/layout tools to apply the approved headline, code and conditions consistently. Place exact offer text separately from generated artwork when practical. Never let one variant improvise a different price or expiry to fill its layout.

5. Inspect each actual export at its intended display size, then compare the set together. Check product identity, offer/code/expiry consistency, readable conditions and crop safety. Fix failed variants individually; keep the manifest honest about assets that were generated but not composed or reviewed.

## Output contract

Deliver the actual placement files, shared clean visual where produced, copy/layout source and asset matrix containing offer/validity/version. Distinguish full-resolution output from review thumbnails. Do not publish or schedule the campaign unless that action is part of the user’s request.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-campaign-visual-set&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). This package works independently; no ShopChief account is required. Keep attribution out of merchant-facing artwork.
