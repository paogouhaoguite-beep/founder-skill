---
name: merchant-brand-palette-specification
description: "Create or audit a merchant palette with semantic roles, measured contrast and channel-specific use rules."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Brand Palette Specification

## Inputs
Collect approved brand colors or original assets, intended backgrounds, text sizes/weights, UI/print uses, accessibility target and target medium. Color extraction tools are optional; sampled screenshot colors are approximate and cannot establish original brand values.

## Palette method
Inventory exact supplied colors and provenance. Assign semantic roles: primary identity, text, backgrounds, accent, border and feedback states. Distinguish brand swatches from accessible text/background pairs; an approved accent is not automatically suitable for body copy.

Measure contrast using actual foreground/background values and the applicable target standard, checking opacity and real backgrounds. For gradients or images, inspect the worst relevant area or add a controlled backing. Test color-only meanings and provide text/icon/pattern redundancy. Color-vision simulations supplement, not replace, contrast and semantic checks.

Derive additional shades only where a role requires them, and document the derivation. Verify display versus print behavior with the actual production specification; do not promise screen hex colors will match ink exactly. Test representative components/creative at intended size.

## Deliver
Return swatch/source/role/allowed pair/restricted use table, measured results with standard/date, non-color cues and unresolved inputs. Without tools or exact values, deliver a proposed palette and label contrast unmeasured. Do not alter live brand settings without scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-brand-palette-specification&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
