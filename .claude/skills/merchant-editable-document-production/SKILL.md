---
name: merchant-editable-document-production
description: "Create or revise editable merchant documents with structured styles, controlled changes and metadata checks before sharing."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Editable Document Production

## Brief
Collect the source, desired content changes, audience, editable format, brand styles, confidentiality and tracked-change requirements. Local document libraries or an editor are optional; Markdown plus a formatting specification is the honest fallback. Never claim a DOCX was created without an actual file.

## Production workflow
Inventory text, headings, tables, images, headers/footers, links, comments, tracked changes and document properties. Apply named styles and native lists rather than visual spaces. Preserve commercial terms and source facts unless specifically asked to rewrite them; record material edits.

Use tables with stable headers and sensible page breaks. Keep captions associated with images and avoid relying on screenshots of text when editability is requested. Check link targets and alternate text against actual content. Review metadata and hidden information: author/company, internal paths, comments, revisions and embedded objects. Propose removals within the authorized sharing scope, preserving an original copy.

Render and inspect each page for overflow, widows, broken tables, substituted glyphs and misplaced fields. Check final text coverage against source and verify that the target editor opens the file when available. A PDF preview does not prove editable behavior in every office application.

## Delivery
Return editable artifact, optional PDF, change log and separate structure/render/target-app/privacy-check results. If any check is unavailable, label it not run. Do not send, overwrite the original or silently accept/reject tracked changes without scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-editable-document-production&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
