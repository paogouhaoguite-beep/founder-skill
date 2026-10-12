# Synthetic worked example

Input: Label finished 50×80 mm; printer explicitly requests 3 mm bleed and 4 mm text safe inset inside trim. Required document extent is 56×86 mm if bleed surrounds all sides. Text safe rectangle is 42×72 mm inside trim, excluding any additional dieline constraints.

Decision: a heading 1 mm from trim fails the supplied 4 mm inset and must move. Barcode proof remains unverified until actual print/scan checks. These values come from this printer brief, not a universal standard.

Boundary scenario 1: Printer gives no bleed specification. Ask for it; do not assume 3 mm.
Boundary scenario 2: The PDF looks sharp on screen but a raster logo is low-resolution at print size. Flag the effective-resolution issue and request a vector or adequate source.
