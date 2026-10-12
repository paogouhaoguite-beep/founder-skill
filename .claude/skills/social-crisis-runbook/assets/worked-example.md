# Worked example

All names, inputs and results below are synthetic.

Input: At 10:00 three customers report a broken lid; each supplied photo verifies batch code L7; a scheduled 11:00 durability promotion exists. Expected statement: “We are investigating reports about lids on batch L7. Please contact support with the batch code; we will update this page by 14:00.” Prepare a pause request for the 11:00 post. Without a scheduler receipt, its state is pause requested, not paused. The count of 3 does not establish the defect rate because units in use are unknown.

## Acceptance scenarios

1. Given the complaint is about a shipment delay only, route through service ownership rather than claiming a product recall.

2. Given investigation is incomplete at the promised time, publish an authorized factual progress update instead of silently missing the commitment.
