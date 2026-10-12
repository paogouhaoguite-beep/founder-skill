# Synthetic worked example

Input: SKU-A price 19.99; requested −10%, round to two decimals, floor 18.50. Raw 17.991 rounds 17.99, below the floor, so BLOCK rather than silently apply. SKU-B tags {summer,linen}; add clearance and remove summer ⇒ {linen,clearance}.

Expected manifest: A price remains 19.99 pending floor decision; B has only a tag update. The file excludes unrelated description columns. A failed retry still targets {linen,clearance}, not another additive rewrite.

## Boundary case 1

If a CSV contains a present-but-empty description cell, identify target clear behavior before proceeding; omit the column when description is outside scope.

## Boundary case 2

If the fresh record changed after backup, stop that row as conflicted. Do not overwrite a newer merchant edit with the stale proposal.
