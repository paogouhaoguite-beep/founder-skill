---
name: merchant-design-export-repair
description: "Diagnose and repair a broken merchant deck or PDF export by comparing controlled renders while preserving the editable original."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Design Export Repair

Use when an exported deck, catalog or PDF clips text, substitutes fonts or loses content. Inputs: editable source when available, broken export, expected reference, destination viewer/converter and required editability. Preserve untouched originals and record tool/version. Use available trusted document/rendering tools; no third-party repair script or fonts are shipped. Without rendering capability, deliver a suspected-defect report and mark repair acceptance pending.

Reproduce the defect by rendering the untouched source through the named conversion path. Inspect output, page/slide count and affected text. Classify package-structure defects, off-canvas geometry, font substitution and renderer-specific text shaping separately. A valid XML box does not prove a correct visual render.

For an editable OOXML package, inspect content-type declarations and relationships against actual parts without deleting unfamiliar content. Resaving via another application may remove unsupported features, so compare them explicitly. For geometry, check full text extents and table grids; intentional bleed is not automatically wrong. For fonts, verify installed/embedded family and permitted use; request licensed font files or approve a disclosed substitution.

Make one isolated change on a copy and render again. If letter spacing is the verified cause of clipping in a specific converter, use a separate render-only copy and retain original spacing in the editable deliverable. Do not globally shrink text or remove clipping from every element to mask symptoms.

Compare repaired and original pages for wording, digits, line breaks, alignment, links, images and hidden/master content. Reopen the editable file in the target app where available. A bare PDF may permit limited PDF-native correction, but cannot guarantee restoration of missing content or original editability; request source when needed.

Deliver repaired artifacts only when actually generated, plus slide/page defect→evidence→isolated change→validation and unresolved limitations. Do not overwrite originals, install fonts or publish files without authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-design-export-repair&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
