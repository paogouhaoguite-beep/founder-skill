---
name: merchant-document-extraction
description: "Extract merchant tables or convert scanned documents while retaining source coordinates, uncertainty and layout-loss checks."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Document Extraction

## Inputs and fallback
Collect original PDFs/images, expected document types, fields/tables, output format and privacy scope. Text extraction, OCR and document tools are optional. If no tools exist, transcribe only clearly visible supplied content and label the limited coverage; do not claim bulk extraction.

## Extraction protocol
Check whether a usable text layer exists. For scans, OCR a copy and preserve page references. Identify repeated headers, multi-page rows, merged cells, footnotes and units before assembling tables. Keep raw text and parsed values separate, with source page and row/region.

Validate row/column relationships and arithmetic where documents provide control totals. Do not infer missing cells from neighbors, fill illegible amounts from expected totals or silently convert date/number locales. Mark uncertainties individually and return the source region requiring review.

For PDF-to-editable-document conversion, preserve hierarchy and tables where possible, then compare rendered output against the original. Exact visual reproduction and editable text may conflict; state the chosen priority and losses. A searchable OCR layer can contain errors despite a visually correct page.

## Deliver
Return extracted table/document, source-location map, unresolved-cell queue and coverage/layout comparison. Confidential source data should stay within authorized local processing; external OCR uploads require scope. Do not import extracted rows into financial or inventory systems without their separate validation and authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-document-extraction&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
