# Synthetic worked example

All quantities, amounts, policies and company circumstances below are invented for arithmetic or decision review. They are not benchmarks.

Synthetic PO: 120 units × USD 8 = 960; freight 140; total 1,100. Quote requires a 30% deposit on goods only: deposit 288; remaining goods 672 plus freight 140 = 812. Applying 30% to the total would incorrectly request 330, a USD 42 overpayment against those terms.

## Acceptance case 1 — supported inputs

Calculate deposit 288 and balance-plus-freight 812, and flag the 330 draft as a term mismatch.

## Acceptance case 2 — boundary or missing evidence

If a supplier sends an amended quantity under the same PO number after partial receipt, preserve received quantities and produce a revision diff; do not create a second PO.

These cases specify expected behavior. Reading them or validating package syntax does not demonstrate live merchant acceptance.
