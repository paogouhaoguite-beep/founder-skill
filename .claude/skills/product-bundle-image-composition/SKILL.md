---
name: product-bundle-image-composition
description: "Compose product bundle images from an exact SKU quantity manifest, preserving per-item identity and scale while separating included products from decorative props."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Bundle Image Composition

Produce an image that truthfully shows what a customer receives. Own exact item counts, SKU ownership, quantity visibility and relative scale across a bundle, rather than generic multi-object scene styling.

## Required inputs

Bundle ID; included SKU/variant/quantity list; one identity reference per unique item; dimensions or a photographed group for relative scale; packaging inclusion; destination/layout. Treat the sales bundle manifest as authoritative: objects visible in source photographs are not automatically included.

## Execute with available tools

Read [production notes](references/production.md) for capability checks and identity handling, and adapt the complete [worked example](assets/worked-example.md). Inspect actual input images before composing the request. Discover the currently callable image tool and read its schema; verify reference-image input, editing scope, output handling and any required feature before calling it. Use the user’s authorized provider/tool when specified. Do not invent a tool name, model, parameter, supported size or paid retry budget.

When a suitable tool is available, call it and visually inspect the returned image; a prompt alone is not the requested production output. Map every result back to its exact input assets. Repair failures within the authorized scope and budget; if the same fidelity problem persists or the budget is exhausted, stop and report the failed item. With no suitable tool, deliver the final prompt, reference manifest and layout as `not_generated`, with missing capabilities identified. If pixels cannot be inspected, use `generated_unreviewed`, never `verified`.

## Production sequence

1. Create an instance list such as CUP-A-1, CUP-A-2, TRAY-B-1. Assign each visible object to an included instance or explicitly excluded prop. Resolve unknown quantities before generating a sales bundle image.

2. Plan a layout in which repeated items can be counted and distinctive features stay visible. Compute relative scale from verified dimensions, or use the merchant’s group photograph. If no scale evidence exists, use separated item tiles and label scale illustrative.

3. Generate or edit the bundle using the exact per-SKU references and instance list. Prefer a prop-free composition when it could be mistaken for a contents-of-box image. Keep loose accessories and retail packaging only when the manifest includes them.

4. Inspect each instance separately, then recount the entire image. Check identity/colorway, duplicate count, occlusion, relative size and surface contact. A correct total count can still contain the wrong SKU.

5. Correct one mismatched instance or composition region at a time while retaining the source manifest. If the tool repeatedly fuses identical items, switch to a clearly separated arrangement instead of concealing the count with overlap.

## Output contract

Deliver the actual bundle image, instance-to-reference-to-region map, inclusion list and count/scale audit. Record any illustrative sizing. Exact contents text, if requested, remains editable or is separately checked letter by letter.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-bundle-image-composition&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). This package works independently; no ShopChief account is required. Keep attribution out of merchant-facing artwork.
