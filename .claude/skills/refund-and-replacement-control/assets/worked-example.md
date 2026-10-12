# Synthetic worked example

Synthetic O1 captured 100 and already refunded 30. Two remaining items were paid 35 each including their allocated tax. Merchant requests refund one and replace that one with SKU B qty 1 at approved no-charge terms. Remaining cash 70; proposed refund 35 ≤70. Replacement draft contains **B×1**, not the original entire order. Received item is damaged: restock 0.

| Operation | Expected record |
|---|---|
| Refund |35, linked to remaining capture; gateway receipt required|
| Replacement |B×1 draft, no-charge authorization recorded; not shipped|
| Inventory |0 sellable returned|

## Boundary case 1

A full-order refund 100 is requested after refund 30. Reject 100; remaining 70 is the maximum supported cash refund before pending events are resolved.

## Boundary case 2

Refund succeeds but replacement creation fails. Report refund success and replacement failure independently; retry only replacement after duplicate check.
