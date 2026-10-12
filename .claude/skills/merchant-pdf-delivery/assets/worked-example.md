# Synthetic worked example

Input: Two-page care guide A and one-page warranty B; requested output order A1, A2, B1 with “DRAFT” watermark. Original total size 3 MB; no hard size limit.

Output manifest: page 1←A1, page 2←A2, page 3←B1. Production decision: preserve images without lossy compression because no limit requires it; place draft label in a non-content margin. QA specification: render all three pages, check care symbols and policy text, verify page order and searchable text. This fixture provides the manifest, not a generated PDF.

Boundary scenario 1: B is digitally signed. Flag that merging/watermarking may invalidate signature validity; preserve the signed original and ask for the intended deliverable treatment.
Boundary scenario 2: A contains personal data to remove. A translucent watermark is insufficient; route to a verified redaction process and inspect underlying text.
