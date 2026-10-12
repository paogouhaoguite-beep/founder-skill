---
name: merchant-pdf-form-completion
description: "Fill a merchant-supplied PDF form from verified data with field mapping, required-value checks and signature boundaries."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Pdf Form Completion

## Inputs and tools
Require the original form, allowed fields, authoritative values, output path and whether the form is interactive or flattened. A PDF form editor is needed to produce a filled file; otherwise deliver a field/value/source mapping. Keep originals and do not upload private data to an external service without scope.

## Fill and verify
Inspect field names/types, required fields, option values, checkboxes and date/number format. Match by actual labels and semantics, not field order alone. Identify repeating or duplicated field names that could change multiple pages together. Missing values remain blocked rather than invented.

Fill only authorized fields, preserve unrelated pages and record transformations such as date formatting. Do not sign, certify, accept contractual terms or insert someone’s signature from a generic completion request. Existing digital signatures may be invalidated by edits; flag before producing a modified version.

Render all affected pages and compare displayed values to the mapping. Check clipping, missing glyphs, checkbox states, calculated fields and whether values remain when reopened. Flatten only if requested and after validation because it reduces editability and may change accessibility.

## Deliver
Return the filled file if actually created, field/source register, unresolved required fields and verification status. Submitting the form is a separate action.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-pdf-form-completion&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
