# Synthetic worked example

Input scan page 1 shows an invoice table: SKU A quantity 2 unit price 10 total 20; SKU B quantity unreadable unit price 5 total 15; grand total 35.

Extraction: A,2,10,20,page 1,row 1; B,UNKNOWN,5,15,page 1,row 2. Arithmetic suggests quantity 3 for B, but the deliverable keeps it unresolved until the page is checked. The row totals sum to35, which does not prove the unreadable quantity.

Boundary scenario 1: A header repeats on page 2. Do not count it as a transaction or data row.
Boundary scenario 2: “1.234,56” appears in a document with decimal-comma conventions. Parse as1234.56 only after verifying locale, preserving the raw string for review.
