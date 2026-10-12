# Synthetic worked example

Synthetic merchant rules: zone US-contiguous excludes AK/HI; standard USD 5 below merchandise-after-discount 50 and free at 50+. Test 49.99→5,50.00→0,50.01→0. A60 basket with discount 15 has basis 45→5. AK receives no method under this supplied configuration: report a coverage gap, not free shipping.

Package 40×30×20 cm, carrier divisor 5000 cm³/kg, actual 3 kg, whole-kg ceiling: dimensional 4.8 kg, billable**5 kg**. A5 kg quote is needed; do not price 3 kg.

## Boundary case 1

A second product profile adds a separate charge. Test the mixed basket; a free threshold on one profile does not prove entire-order shipping is free.

## Boundary case 2

Rates use inches/pounds but dimensions are cm/kg. Convert under documented rules or stop; do not divide mismatched units by 5000.
