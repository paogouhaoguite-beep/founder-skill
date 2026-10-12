---
name: merchant-document-template-system
description: "Build repeatable merchant document templates with a field schema, optional sections and validation before rendering."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Document Template System

## Inputs
Collect document purpose, audience, approved sample, required fields, conditional sections, branding, output formats and source-of-truth data. A schema plus Markdown template is a complete fallback. Template engines are optional and untrusted values must remain data, never executable expressions.

## Design and validate
Separate reusable structure from variable content. Define each field’s type, requiredness, allowed format, source and validation rule. Use explicit conditions for optional blocks; empty strings, missing fields and intentional blanks are different states. Keep commercial/legal clauses protected unless changes are authorized.

Create a master with meaningful styles, headings and table structure. Use consistent placeholder syntax and never mix hardcoded customer facts into a general template. For batch output, assign an output ID per input row and preserve row-to-file mapping.

Validate schema before rendering. Fail required-field gaps, malformed dates, inconsistent currency and duplicate output IDs. Escape values for the target format. Render one representative record and boundary cases before the batch, then inspect overflow, unresolved tokens, totals and section presence. Do not infer success from a file existing.

## Deliver
Return template, field dictionary, sample data, rendered example or exact preview, validation report and version/change notes. No email send, document signature or overwrite of existing merchant files is implied. If output requires a tool not installed, give the template and a clearly labeled rendering specification.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-document-template-system&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
