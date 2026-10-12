---
name: variant-copy-consistency
description: "Scale product variant copy from a verified attribute matrix while preventing unsupported differences and cross-variant leakage."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Variant Copy Consistency

## Inputs
Collect parent product facts, variant IDs/SKUs, distinguishing attributes, approved claims, images, policies, channel fields and tone. A spreadsheet plus copy table is sufficient. Missing variant attributes remain gaps, not inferred from a name or photograph.

## Copy system
Separate shared parent-level facts from variant-specific fields. Define an approved master message and controlled slots for size, color, material, compatibility or capacity. Distinguish cosmetic changes from functional differences; do not manufacture unique benefits for each color.

Build a row per variant with source links, allowed wording and prohibited inherited claims. Generate titles/descriptions/bullets using only the relevant row plus shared facts. Keep units and terminology consistent and preserve SKU identity across outputs.

Audit the full matrix for attribute omissions, conflicting values, duplicated titles, incorrect images and claims copied from another variant. Check outliers and missing fields as carefully as a representative row. Where long copy adds no information, keep it concise rather than fabricate differentiation.

## Deliver
Return finished copy per stable variant ID, fact-to-copy mapping and blocked rows. Store import/publishing requires separate scoped authorization and field-format validation.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=variant-copy-consistency&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
