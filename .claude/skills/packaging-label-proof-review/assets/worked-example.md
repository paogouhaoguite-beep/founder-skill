# Synthetic worked example

Synthetic carton SKU SOAP-100 revB shows "Net 100 g", approved spec says 100 g, but ingredient panel copied from revA which contains fragrance while revB is unscented. Barcode master 036000291452 matches arithmetic: first 11 digits weighted sum 58 →check digit 2.

| Field | Result | Action |
|---|---|---|
|Net quantity|matches 100 g|retain|
|Ingredients|revA vs revB mismatch|hold print and request approved revB text|
|Barcode|check digit 2 matches|still needs actual print scan|

## Boundary case 1

Only a compressed screenshot is supplied. Text content can be checked, but actual font height/quiet zone cannot be certified; request scaled proof.

## Boundary case 2

Two variants share same barcode unintentionally. Hold both mappings until product master owner resolves identity; do not generate a new assigned identifier.
