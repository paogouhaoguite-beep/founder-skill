# Synthetic worked example

Input: P1 is active/published with 0 images and price $30; P2 is a draft with 0 images and price $0; P3 is published with 3 images, price $40 and compare-at $35. The merchant allows draft placeholders.

Expected result:

| ID | Finding | Disposition |
|---|---|---|
| P1 | No images on live item | Verify fresh record; prioritize image remediation |
| P2 | Placeholder draft | Record exception; no live-price alarm |
| P3 | Compare-at below price | Review sale display; do not silently rewrite price |

Two published products have actionable review flags; this does not establish that unrelated catalog fields passed.

## Boundary case 1

If 800 rows represent 300 products and 800 variants, report both populations. Do not report 800 defective products from variant-level flags.

## Boundary case 2

If a source omits image count, label image coverage unavailable. An empty imported column is not proof that the live object has no image.
