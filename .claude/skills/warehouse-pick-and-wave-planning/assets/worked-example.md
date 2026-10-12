# Synthetic worked example

Synthetic cutoff 12:00; W1 starts 11:00 with 30 min picking,20packing and 5 staging →finish 11:55,5 min slack. W2 needs 45+20+5=70 min from 11:00 →12:10,10 min late. Same pack station cannot process both concurrently: assign explicit slots before promising either. Batch cart capacity 20 kg; order A12 kg+B10 kg cannot share one cart though their bins are adjacent.

## Boundary case 1

S-curve route appears shorter but crosses a locked aisle. Mark infeasible and use measured permitted path.

## Boundary case 2

Two orders each require same last unit. Allocate shared stock once; second order enters short-pick review, not another batch with duplicate unit.
