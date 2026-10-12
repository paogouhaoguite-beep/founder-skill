---
name: arabic-rtl-artifact-review
description: "Prepare and verify Arabic or bilingual merchant artifacts using logical Unicode, native RTL structure and target-application checks."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Arabic Rtl Artifact Review

## Inputs and tools
Identify locale, Arabic-first or bilingual intent, editable source, requested output, target application and available Arabic-capable fonts. A text-only correction can be done locally; visual and application checks require a renderer or app. Missing tools mean those checks are not run, not passed.

## Preserve semantic structure
Keep Arabic in logical Unicode order. Do not reverse characters, pre-shape presentation forms or insert invisible direction controls as a general fix. Inspect unexpected controls and preserve linguistically meaningful ZWJ/ZWNJ unless a specific error is verified. Never normalize identifiers, signatures or code blindly.

Set paragraph/container direction separately from alignment and language metadata. Keep long Latin passages, URLs, codes and formulas in appropriate LTR containers; use direction isolation for unknown inline content where the format supports it. Use native lists and table semantics, not spaces to fake indentation. Mirror semantic reading order only where appropriate, not logos, charts or universally meaningful symbols by default.

Check Arabic glyph coverage and actual font substitution; installed fonts do not prove embedded portability. Prefer editable Arabic text over generated lettering in images, and verify any raster lettering letter by letter.

Render the entire final artifact. Inspect joins, punctuation, digits, mixed acronyms, parentheses, bullets, wrapping, tables and overflow. Open it in the named application when available. For a repair, write a new file and confirm unrelated content survives; do not silently overwrite originals.

## Delivery record
Return corrected artifact or precise repair specification and separate results for content, Unicode/RTL structure, visual layout, target application and font portability. A PDF companion may preserve appearance but does not replace requested editability.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=arabic-rtl-artifact-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
