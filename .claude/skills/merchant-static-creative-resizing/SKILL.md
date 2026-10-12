---
name: merchant-static-creative-resizing
description: "Adapt and compress a merchant image or design for specific placements while preserving product details, readable copy and source files."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Static Creative Resizing

## Inputs and tools
Obtain source dimensions/editable file, exact destination requirements, safe zones, file-size limit, critical content and image rights. Verify current platform specs when necessary; do not hardcode historical social sizes as universal rules. Image/design tools are optional; give an exact resize/crop/export specification if unavailable.

## Adaptation
Classify whether the job is a crop, proportional scale or true layout reflow. Preserve product proportions, legal qualifiers and logos; do not stretch an image to fit. Map protected content regions and decide crop anchor from the task, not automatic center-crop.

For editable designs, reposition/reflow text and imagery at the new aspect ratio. For flattened sources, explain what cannot be separated and request layers when needed. Create new outputs with placement-specific names; never replace originals by default.

Choose export format and compression based on transparency, animation, text and destination. Compare before/after at intended size for product detail, text sharpness, banding and artifacts. Record dimensions, bytes and actual QA result. Same dimensions do not guarantee identical safe zones across placements.

## Deliver
Return each actual output or production spec, source-to-target transform, size report and failed/unverified placements. Resizing is not publication; uploading assets or replacing live store media needs scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-static-creative-resizing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
