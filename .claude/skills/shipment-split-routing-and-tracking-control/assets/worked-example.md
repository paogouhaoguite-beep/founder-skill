# Synthetic worked example

Synthetic shared eligible stock A=5 of SKU X; O1 requires 4 and O2 requires 3. Merchant priority O1 first. Allocate O1=4, O2=1 now+2 backlog: total 5 allocated, no oversell. Splitting O2 adds shipping 6 compared with waiting.

| Order | A now | Backlog | Decision |
|---|---|---|---|
| O1 |4|0|one package|
| O2 |1|2|merchant chooses split cost 6 or wait|

For O1 remaining 4, split groups 3+3 would total 6 and are rejected even though each individually≤4.

Pickup case: an online order reserves 2 units but store staff have not picked them. Status is reserved, not ready or collected. Customer arrival cannot mark collection without matching handoff evidence; an expired reservation follows the approved expiry policy before release.

## Boundary case 1

Destination has 3 physical units but all 3 reserved for another order. Eligible 0; do not route 3 there.

## Boundary case 2

Tracking update is authorized but notification is not. Prepare/update only within authorized no-notification operation; report customer message unsent.
