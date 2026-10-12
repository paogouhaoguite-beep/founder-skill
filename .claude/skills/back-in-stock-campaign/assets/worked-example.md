# Synthetic worked example

All people, products, account results and amounts below are invented fixtures, not merchant outcomes. Amounts are USD unless noted.

Synthetic usable stock 40, reserved orders 10 and merchant buffer 5 leave 25 sellable units for this plan. With an observed 20% purchase rate and one unit/order, a 100-person batch has expected demand 20 units; a 125-person batch has expected demand 25 but no uncertainty buffer. Choose and justify a smaller pilot based on risk; expectation is not a guarantee. An immediate inventory recheck finding only 8 remaining units invalidates the earlier 100-person plan.

Draft: “The navy travel pouch you asked about is available again at USD 39. Availability can change while you browse. View the navy pouch for current stock and delivery.” Do not claim a reservation.

## Acceptance scenarios

1. Given the requested navy variant remains sold out while black restocks, do not notify navy subscribers as though their requested item returned.
2. Given stock falls between batch preparation and send, pause/recalculate the unsent batch instead of relying on the stale snapshot.
