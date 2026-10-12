# Synthetic worked example

Synthetic ship date October 1, delivery ETA October 4, merchant promise at least 10 remaining calendar days. LotA expiresOctober 12:8 days at delivery, **ineligible**. LotB expiresOctober 20:16 days, eligible if released. Order needs 6 units; B has 5, so allocate at most 5 and flag shortage 1; do not fill fromA merely because it expires first. LotC has sufficient date life but a2-hour sensor gap during transport: quality review pending under supplied procedure, not declared safe.

## Boundary case 1

Date 04/10 is ambiguous. Stop eligibility calculation until date convention is confirmed.

## Boundary case 2

Temperature average matches target but one logged peak breaches the approved limit. Preserve peak/duration and quarantine decision pending quality review; no averaging away.
