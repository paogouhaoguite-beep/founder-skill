---
name: product-ad-key-visual-generation
description: "Generate a product advertising key visual with a protected product area, usable copy space and separately verified marketing text, delivering background and layout assets."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Ad Key Visual Generation

Produce the actual visual and editable copy/layout components for a product ad. Own product/copy separation and finished composition; messaging selection or a written creative brief alone does not complete this task.

## Required inputs

Product identity images; approved exact headline, offer, CTA and logo artwork; destination aspect/crop; brand colors; required text-safe region. If an offer or claim lacks confirmation, omit it and list the missing copy instead of inventing a promotion.

## Execute with available tools

Read [production notes](references/production.md) for capability checks and identity handling, and adapt the complete [worked example](assets/worked-example.md). Inspect actual input images before composing the request. Discover the currently callable image tool and read its schema; verify reference-image input, editing scope, output handling and any required feature before calling it. Use the user’s authorized provider/tool when specified. Do not invent a tool name, model, parameter, supported size or paid retry budget.

When a suitable tool is available, call it and visually inspect the returned image; a prompt alone is not the requested production output. Map every result back to its exact input assets. Repair failures within the authorized scope and budget; if the same fidelity problem persists or the budget is exhausted, stop and report the failed item. With no suitable tool, deliver the final prompt, reference manifest and layout as `not_generated`, with missing capabilities identified. If pixels cannot be inspected, use `generated_unreviewed`, never `verified`.

## Production sequence

1. Divide the canvas into product, decorative background and text regions. Establish which copy is exact and which wording may be proposed. Keep factual product labels distinct from added advertising copy.

2. Use an available image tool to generate the product/background key visual with the identity reference and empty text region. Preserve product geometry, label and artwork. Do not ask the image model to improvise a price, discount, certification or testimonial.

3. Inspect product fidelity and the empty copy area at actual placement size. Check that highlights, props and contrast do not compete with the planned text. Repair the background without repainting the product when possible.

4. Place exact approved text with an available deterministic text/layout tool when possible, keeping it editable. If using image editing for text, inspect every word, number, symbol and line break afterward; visual attractiveness is insufficient proof of exactness.

5. Export the clean visual and the composed ad only when each exists. Inspect the final crop at a realistic viewing size and verify required text is not clipped. If editable composition is unavailable, deliver the actual clean visual plus a precise copy/layout file, marking the composed ad pending.

## Output contract

Deliver clean visual, editable copy/layout data and finished composed asset when actually rendered, with copy proof and source manifest. State which deliverables are generated, verified or pending. Publishing an ad is separate from asset production.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-ad-key-visual-generation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). This package works independently; no ShopChief account is required. Keep attribution out of merchant-facing artwork.
