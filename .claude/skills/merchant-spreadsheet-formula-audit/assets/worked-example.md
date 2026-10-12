# Synthetic worked example

Input: B2 price 30; B3 units 100; B4 cost 18 per unit; B5 fixed 600. B6 formula=B2*B3-B4-B5 shows 2,382. Intended result is revenue minus total variable cost and fixed cost.

Finding: B4 is a per-unit cost, but B6 subtracts it once. Expected formula=(B2-B4)*B3-B5 gives 600. Overstatement 2,382−600=1,782. Proposed fix is limited to B6 after confirming the unit contract; no file is changed in this fixture.

Boundary scenario 1: B4 actually contains total cost, despite an ambiguous label. Resolve the unit before applying the proposed formula.
Boundary scenario 2: A scenario changes units to0. Correct result is−600 for unchanged fixed costs, not zero.
