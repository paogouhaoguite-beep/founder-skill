---
name: merchant-pdf-delivery
description: "Prepare a merchant PDF with explicit page order, compression or watermark requirements and rendered delivery checks."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Pdf Delivery

## Inputs and tools
Require source documents, target audience, page selection/order, file-size target, watermark text and editable-source needs. Use trusted local PDF tools if available; otherwise return a precise production plan. Preserve originals. No upstream scripts or media are bundled.

## Produce and verify
Inventory page counts, dimensions, orientation, text/searchability, form/signature status and restrictions before changes. Map every output page to its source page for merges or splits. Resolve overlapping selections and duplicate pages intentionally.

Generate or convert with readable typography, real text where possible and semantic content structure. Compression must balance the actual delivery limit against image readability, barcode quality and legibility; do not promise a universal reduction percentage. Keep an original-quality copy. A watermark is a visible label, not redaction or access control, and must not obscure required information.

Render every final page and inspect clipping, overlap, missing glyphs, images, tables, links and order. Recheck text extraction for content coverage, but never treat it as visual proof. Verify the output opens, page count matches the manifest and any form/signature consequences are disclosed. Do not modify digitally signed files without explaining signature invalidation and obtaining scope.

## Deliver
Return PDF if actually generated, page manifest, size before/after, inspection results and known limitations. If creation or rendering did not run, say so and deliver source/specification instead. Sending or uploading the PDF remains separately authorized.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-pdf-delivery&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
