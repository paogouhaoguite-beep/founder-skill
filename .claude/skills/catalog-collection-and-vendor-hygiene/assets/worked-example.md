# Synthetic worked example

Input: P1 vendor "Acme Ltd", P2 "ACME", P3 "Acme Studio". Merchant confirms only P1/P2 are one entity. Collection C requires vendor="ACME" AND tag="linen". P1 and P2 both have linen.

Expected: rename P1 to ACME adds P1 to C; P2 unchanged; P3 is unresolved and untouched. C gains one member after the proposed mapping, which must be shown in the preview.

## Boundary case 1

A collection uses ANY rather than ALL: evaluate the actual boolean rule; do not copy an AND assumption.

## Boundary case 2

Two vendors share a word but different supplier accounts: retain separate entities unless the merchant verifies a merger.
