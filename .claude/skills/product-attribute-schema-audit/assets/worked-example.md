# Synthetic worked example

Input: material is list[text]; P1 supplies "linen" as scalar, P2 supplies ["cotton","linen"], P3 category attribute color needs a controlled reference but only label "Blue" is supplied.

Expected: P1 proposed ["linen"] only after confirming single-value-to-list conversion; P2 valid and unchanged; P3 BLOCKED pending authoritative category/value ID. If P2 fails at source timestamp 12:00 and the sync checkpoint advances to 12:05, keep P2 in an explicit retry ledger so it is not lost.

## Boundary case 1

Two locales label a color identically but reference different source IDs: preserve both until their equivalence is confirmed.

## Boundary case 2

A definition has no values in the filtered export but is used by a theme filter: report incomplete coverage and do not delete it.
