---
name: product-image-localization
description: "Localize marketing text inside product images through a region and translation ledger, preserving product pixels, regulated label facts and exact numeric claims."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Image Localization

Produce localized image variants by editing identified text regions. Own source transcription, approved replacement text, masks and outside-region preservation; translating a paragraph without editing the asset is not completion.

## Required inputs

Original image; source and target locale; intended market; editable artwork if available; approved terminology; list of editable marketing text regions. Identify immutable product labels, warnings, ingredient panels, certification marks, barcodes, units, prices and legal copy. Missing approval for regulated-label changes is not permission to translate them.

## Execute with available tools

Read [production notes](references/production.md) for capability checks and identity handling, and adapt the complete [worked example](assets/worked-example.md). Inspect actual input images before composing the request. Discover the currently callable image tool and read its schema; verify reference-image input, editing scope, output handling and any required feature before calling it. Use the user’s authorized provider/tool when specified. Do not invent a tool name, model, parameter, supported size or paid retry budget.

When a suitable tool is available, call it and visually inspect the returned image; a prompt alone is not the requested production output. Map every result back to its exact input assets. Repair failures within the authorized scope and budget; if the same fidelity problem persists or the budget is exhausted, stop and report the failed item. With no suitable tool, deliver the final prompt, reference manifest and layout as `not_generated`, with missing capabilities identified. If pixels cannot be inspected, use `generated_unreviewed`, never `verified`.

## Production sequence

1. Inspect the image and transcribe visible text region by region. Record bounding boxes as normalized coordinates plus the exact source string, role, edit permission and target string. OCR may assist; visually verify ambiguous characters and numbers before using them.

2. Translate editable marketing copy for the target locale while retaining claims and offer meaning. Do not change a unit, currency, discount, certification or legal condition through localization. Resolve unreadable facts or approved terminology before editing those regions.

3. Choose a real available image editing or layout tool. Supply the original image and supported region/mask input; request only approved text replacements and preserve the product/background outside the regions. If masks are unavailable, use localized instructions and compare the full output afterward.

4. When exact typography is important, remove only the old marketing lettering with the image tool and place approved text with a deterministic layout tool if available. Adjust line breaks and font size within the region before expanding into the product area.

5. Inspect every translated region and the unchanged image. Compare numbers, punctuation, line breaks and accents; check product/label crops and image differences where tooling permits. Reject changed labels or factual drift even when the translation reads fluently.

## Output contract

Deliver actual locale image files, region/translation ledger, unchanged-region review and any blocked strings. Mark unrendered locales as pending. The image is localized marketing artwork, not a certification that packaging complies with a market’s requirements.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-image-localization&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). This package works independently; no ShopChief account is required. Keep attribution out of merchant-facing artwork.
