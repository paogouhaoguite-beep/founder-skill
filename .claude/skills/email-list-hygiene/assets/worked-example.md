# Worked example

All names, inputs and results below are synthetic.

Input: 1,000 profiles; 50 globally suppressed, 20 duplicate IDs and 10 hard-bounce profiles outside suppression, with no overlap among these groups. Maximum eligible unique count = 920 before other criteria. A profile with many opens but no clicks has uncertain engagement if opens are privacy-protected. Report the 10 suppression discrepancies; do not call all 920 active buyers.

## Acceptance scenarios

1. Given a household buys annually, do not suppress it solely because no purchase occurred in 90 days.

2. Given the same complaint appears twice, deduplicate events and preserve one affected profile rather than double-counting complaint rate.
