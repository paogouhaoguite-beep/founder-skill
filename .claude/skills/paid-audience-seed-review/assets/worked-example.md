# Worked example

All names, inputs and results below are synthetic.

Input: 100 customer rows; 60 have 2+ paid orders, 10 of those opted out and 5 further rows have fully refunded orders only. Eligible repeat-purchaser seed = 45 if these groups are distinct. A recent-purchase exclusion overlaps 12: prospecting eligible = 33. Export the definition/counts first, not customer emails. No lookalike size is claimed.

## Acceptance scenarios

1. Given value is missing for 8 rows, keep an unknown bucket rather than ranking them at zero or inventing spend.

2. Given a customer belongs to seed and suppression, suppression wins for the specified activation.
