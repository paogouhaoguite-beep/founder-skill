# Worked example

All names, inputs and results below are synthetic.

Input: A members-only drop has 50 units and 100 eligible members. Expected copy: “Members may purchase while stock lasts”, not “Your item is reserved.” A logged-out member returns to the same product after login. If all 50 units sell, entitlement remains true but purchasability is false; the UI shows sold out instead of another signup prompt.

## Acceptance scenarios

1. Given a legal age requirement exists, do not optimize conversion by bypassing the required verification.

2. Given the gate only hides a standard retail price without a justified purpose, flag the friction and propose an ungated test for review.
