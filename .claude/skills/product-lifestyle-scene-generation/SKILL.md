---
name: product-lifestyle-scene-generation
description: "Generate reference-faithful product lifestyle images with a coherent support plane, physical scale, lighting and contact shadows, plus scene-level visual acceptance."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Lifestyle Scene Generation

Produce a finished scene in which a real product sits plausibly in its surroundings. Own the support geometry, scale evidence and lighting match; do not invent product performance to justify a scene.

## Required inputs

Product reference images and SKU; permitted use setting; product dimensions if scale matters; approved scene or style reference; intended crop and copy space. Give references explicit roles: product identity, scene geometry or lighting style. Identify the surface supporting each product and which objects are background props.

## Execute with available tools

Read [production notes](references/production.md) for capability checks and identity handling, and adapt the complete [worked example](assets/worked-example.md). Inspect actual input images before composing the request. Discover the currently callable image tool and read its schema; verify reference-image input, editing scope, output handling and any required feature before calling it. Use the user’s authorized provider/tool when specified. Do not invent a tool name, model, parameter, supported size or paid retry budget.

When a suitable tool is available, call it and visually inspect the returned image; a prompt alone is not the requested production output. Map every result back to its exact input assets. Repair failures within the authorized scope and budget; if the same fidelity problem persists or the budget is exhausted, stop and report the failed item. With no suitable tool, deliver the final prompt, reference manifest and layout as `not_generated`, with missing capabilities identified. If pixels cannot be inspected, use `generated_unreviewed`, never `verified`.

## Production sequence

1. Inspect the product and reference scene. Define the support plane, camera height, light direction and relative scale before generation. If scale is unverified, choose a composition without familiar size anchors or mark scale as illustrative.

2. Specify the product placement as a bounding region and contact point. Reserve the requested copy space. Exclude props that imply unverified accessories, ingredients, water resistance or heat tolerance.

3. Call a real reference-aware image tool with the product reference and the scene reference only if one exists. Ask for one coherent scene: product geometry locked, plausible environmental reflections, and a contact shadow attached to the support point.

4. Inspect the output at full frame and the product/surface intersection. Check that shadow direction agrees with highlights, the object rests on the surface, perspective converges consistently and local occlusion is plausible.

5. Repair local defects with the original identity reference plus the accepted scene. Preserve correct regions; do not restart the whole style to fix a floating base. Export requested crops only after confirming the crop retains the contact point and entire required product.

## Output contract

Deliver actual scene files, a scene card describing support plane/light/scale basis, source-to-output manifest and crop checks. Record product drift and any illustrative scale. Keep generated lifestyle imagery distinct from documentation of real field use.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-lifestyle-scene-generation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). This package works independently; no ShopChief account is required. Keep attribution out of merchant-facing artwork.
