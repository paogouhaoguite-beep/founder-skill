# Synthetic worked example

Synthetic depot departs 09:00. Depot→A20 min; A window 09:00–10:00, service 10 →arrive 09:20/depart 09:30. A→B25; B window 10:00–11:00, service 15 →arrive 09:55, wait 5, depart 10:15. B→depot 30 →return 10:45. Total route 105 min = travel 75+service 25+wait 5. Driver shift ends 10:30: **infeasible**, despite both customer windows being met. Merchant can review a different route/shift; do not accept the slot as available.

## Boundary case 1

A new order arrives after the supplied same-day cutoff. Keep next eligible slot or owner exception pending; no silent timezone conversion based on viewer browser.

## Boundary case 2

Two orders each fit remaining capacity 1, but both accepted together need 2. Require a single current reservation plan; do not promise the last slot twice.
