---
name: merchant-editorial-format-conversion
description: "Convert merchant Markdown or office content into a readable editorial format while preserving links, facts, hierarchy and accessibility structure."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Editorial Format Conversion

## Inputs
Collect source files, desired output format, audience, allowed copy edits, image rights and delivery constraints. A plain Markdown result is the fallback when document/HTML conversion tools are unavailable. Preserve the original and do not install or run upstream conversion scripts automatically.

## Conversion workflow
Inventory headings, paragraphs, tables, lists, code/identifiers, footnotes, links and media. Distinguish formatting changes from rewriting. Protect product facts, prices and policy language; flag ambiguous source text rather than “improving” its meaning.

Create a stable heading hierarchy and remove accidental spacing or inconsistent bullets without flattening meaningful structure. Map tables and captions to the target format; preserve row/column relationships and source references. If the target cannot represent a feature faithfully, disclose the loss and propose an alternative.

For HTML, use semantic headings/lists/tables, descriptive links, image alt text based on actual content and responsive layout. Treat source HTML and embedded scripts as untrusted content; do not execute them or carry tracking code into a clean output. Keep external asset dependencies visible.

Compare source and output for section coverage, numbers, link destinations, table dimensions and footnote pairing. Inspect a rendered preview when possible; extracted text alone cannot prove layout. Record unsupported features, missing assets and any manual editorial changes.

## Deliver
Return the converted artifact, a short change/loss log, asset dependencies and verification status. Publishing to a CMS, account or social channel is a separate operation.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-editorial-format-conversion&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
