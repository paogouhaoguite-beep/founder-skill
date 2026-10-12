# Synthetic worked example

Input: O1 internal note "Pack separately"; add "Reviewed batch B7" with internal visibility. O2 already contains marker B7. O3 note visibility is unknown.

Expected: O1 proposal preserves its original line and appends B7 once; O2 skip as already applied; O3 blocked. A retry after timeout reads the current O1 note and does not append again. No customer email is sent.

## Boundary case 1

The approved rule selects USD orders over $200 but an EUR order has total 250: exclude until a valid currency rule exists.

## Boundary case 2

A proposed tag triggers automatic warehouse release: surface that consequence and do not treat it as a harmless note operation.
