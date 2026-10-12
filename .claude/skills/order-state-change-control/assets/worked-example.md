# Synthetic worked example

Synthetic O1 is paid 40, unshipped,2 units reserved and warehouse confirms pick stopped. Proposed cancellation separates refund 40 and release 2 reservations; it does not add 2 physical units because goods never left. O2 has already shipped 1 unit: block cancel-and-restock for that unit and route to returns.

| Order | Decision | Stock action | Cash action |
|---|---|---|---|
| O1 | cancellation ready for authorized execution | release 2 reservations | separately refund 40 if authorized |
| O2 | shipment already departed | no physical increase | review return/refund policy |

## Boundary case 1

An order has address and quality holds. Address corrected: release only the address hold; quality hold remains.

## Boundary case 2

Cancellation returns a queued job. Report pending; do not claim refunded or restocked until job and financial/inventory readback establish outcomes.
