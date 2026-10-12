# Worked example

All names, inputs and results below are synthetic.

Input: A refill brand changes from “plastic-free” to “80% less packaging mass than our old 500 g pack” with a 100 g replacement. Expected calculation: (500−100)/500 = 80%. Audit finds homepage updated, 2 paid ads still say plastic-free and 300 printed inserts use the old claim. Prioritize the ads, flag insert distribution for owner action, and record the homepage as verified. A draft fix alone does not mark an ad changed.

## Acceptance scenarios

1. Given a new slogan without a change of audience or factual promise, avoid forcing a full inventory replacement.

2. Given the comparison baseline changed from 500 g to 250 g, recompute the reduction to 60% and block reuse of the old 80% claim.
