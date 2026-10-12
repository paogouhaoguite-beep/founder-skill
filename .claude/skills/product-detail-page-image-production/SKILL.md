---
name: product-detail-page-image-production
description: "Produce a coordinated product detail page image set with evidence-backed modules, exact copy, mobile-readable crops and an ordered asset manifest."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Detail Page Image Production

Produce the complete ordered image set for a product detail page: a hero, evidence-backed detail modules and usable mobile crops. Own module sequencing, claim-to-evidence mapping and text legibility across the set rather than a single scene treatment.

## Required inputs

SKU/variant and identity images; approved product facts and supporting close-ups; module order or buying questions; exact copy and brand artwork; desktop/mobile placement dimensions when known. Map each module to a reference and a supported claim. Identify any module needing a diagram, photograph, exact typography or source evidence not yet supplied.

## Execute with available tools

Read [production notes](references/production.md) for capability checks and identity handling, and adapt the complete [worked example](assets/worked-example.md). Inspect actual input images before composing the request. Discover the currently callable image tool and read its schema; verify reference-image input, editing scope, output handling and any required feature before calling it. Use the user’s authorized provider/tool when specified. Do not invent a tool name, model, parameter, supported size or paid retry budget.

When a suitable tool is available, call it and visually inspect the returned image; a prompt alone is not the requested production output. Map every result back to its exact input assets. Repair failures within the authorized scope and budget; if the same fidelity problem persists or the budget is exhausted, stop and report the failed item. With no suitable tool, deliver the final prompt, reference manifest and layout as `not_generated`, with missing capabilities identified. If pixels cannot be inspected, use `generated_unreviewed`, never `verified`.

## Production sequence

1. Build a module manifest before rendering: module ID, buyer question, evidence, visual type, exact copy, crop and output. Avoid making several images repeat the same claim. Do not add an unproven benefit simply to fill the gallery.

2. Define a visual system shared by all modules: product identity, background palette, product scale where comparable, light direction and typography. Keep a clean hero as the identity anchor; product detail modules still use original close-ups as evidence.

3. Call a real reference-aware image tool to produce the hero and then each supported module. Assign references to their actual role; a close-up cannot establish hidden mechanisms. Generate clean artwork separately from exact copy when the tool cannot render words reliably.

4. Use available layout tools to place approved text as editable content. Create mobile crops from each actual output, preserving the part that answers the module’s buyer question. If a crop loses the detail, recomposite that module rather than shrinking an unreadable desktop panel.

5. Inspect every output at desktop placement and a realistic phone viewing width. Compare product identity across modules, verify text against the approved copy, and check module-specific details. Repair the failed module while preserving the accepted set; list unsupported modules as pending.

## Output contract

Deliver actual ordered desktop/mobile image files, clean artwork where produced, exact-copy/layout source and module-to-evidence manifest. Record real dimensions, crop and visual/text acceptance per file. A module with missing source evidence or unresolved typography is not a completed sales asset.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-detail-page-image-production&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). This package works independently; no ShopChief account is required. Keep attribution out of merchant-facing artwork.
