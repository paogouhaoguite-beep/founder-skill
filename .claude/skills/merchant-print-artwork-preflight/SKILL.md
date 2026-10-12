---
name: merchant-print-artwork-preflight
description: "Prepare print-ready merchant artwork checks from the actual printer specification, including trim, bleed, color and physical-size proofing."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Print Artwork Preflight

## Inputs
Require artwork/source, printer specification, finished dimensions, stock, print process, dieline, finishing, barcode requirements and proof deadline. A preflight checklist is the fallback without layout/PDF tools. Never invent a universal bleed, resolution or color-profile requirement.

## Preflight
Separate trim, bleed, safe area, folds, glue and cut paths. Verify orientation, page count and units. Keep text and essential product/legal details clear of finishing zones. Confirm image resolution at final physical size, not just pixel dimensions.

Use the printer’s requested color space/profile and spot-color treatment. Check black text, overprint/transparency, embedded/substituted fonts and line weights under the actual process. Preserve editable originals and licensed assets. Barcode readability needs actual printed size, quiet zone and verification appropriate to its symbology; visual appearance alone is insufficient.

Inspect separations or production preview when available and generate a scaled physical-size proof. Compare the output with the approved content and dieline. Label any missing printer parameter or unperformed proof check. Do not “fix” technical production settings by guessing.

## Deliver
Return artwork/preflight issue register, printer-question list, proof status and exact export specification or produced file. Printer submission and production approval remain separate from preparation.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-print-artwork-preflight&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
