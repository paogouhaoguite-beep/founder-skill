# Synthetic worked example

Synthetic invoice I1 lists SKU A100 units atUSD 5=500, packing list lists 10 cartons×8=80 units, BOL shows 10 cartons. Output: **20-unit quantity inconsistency**; request whether invoice quantity or pack count is wrong before broker submission. Supplier ships from countryX but manufacturing origin record is countryY: retain originY as documented, notX. Freight 60 is separately shown; customs-value treatment remains pending destination-specific broker instructions, not automatically 560 or 500.

## Boundary case 1

Invoice covers two shipments but packing list only one. Request allocation by shipment before declaring a20-unit shortage.

## Boundary case 2

Source suggests a tariff code based on “cotton bag” but composition is unknown. Do not assign the code or rate; request material/function evidence.
