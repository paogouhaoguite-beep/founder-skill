# Synthetic worked example

Input: V1 SKU "0010", options Color=Grey/Size=M; V2 SKU "0010 ", options Color=Gray/Size=M; V3 SKU "0011", Color=Gray/Size=L. Approved dictionary Grey→Gray.

Expected: V1/V2 share comparison SKU 0010 and would both become (Gray,M); both are BLOCKED for identity review. V3 is not a duplicate. For two colors × two sizes there are four theoretical combinations; if Black/L is prohibited, the permitted matrix has three, not four.

## Boundary case 1

Identifiers "0010" and "10" remain distinct absent an authoritative rule; spreadsheet numeric coercion must not erase the difference.

## Boundary case 2

A bundle may intentionally reference a component fulfillment SKU. Record the linkage and obtain the intended identity model; do not merge its storefront variant with the component.
