# Synthetic worked example

Synthetic co-pack batch has 100 accepted unitsX and 45 boxes, each finished kit needs 2X+1box. Component capacity=min(100/2,45)=45 kits before quality losses. Actual 42 released,2 rejected and 1 WIP consume 90 X/45boxes if each was assembled; remaining 10 X must reconcile separately. Cross-dock inbound arrives 13:00; unload 30 min+inspection 30+sort 30 gives ready 14:30. Carrier cutoff 14:00 is missed by 30 min: propose rebook/hold, never label it feasible direct transfer.

## Boundary case 1

Supplier says 100 shipped but receiving counted 95. Use 95 physical receipt pending discrepancy resolution; do not build the plan on ASN100.

## Boundary case 2

Packaging artwork version is unapproved. Hold the affected packing release even when labor and parts are available.
