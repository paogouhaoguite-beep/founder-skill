# Worked example

All names, inputs and results below are synthetic.

Input: Post A has 100 engagements/1,000 reach = 10%; post B has 20/100 = 20%. Median of the two rates = 15%, while weighted total = 120/1,100 = 10.91%. Report both with labels. Post C has 150 engagements from 100 reached accounts; 150% is possible when users take multiple actions, so inspect the definition rather than reject the row.

## Acceptance scenarios

1. Given reach is absent but impressions exist, compute engagement/impressions and label it; do not silently call it reach engagement rate.

2. Given one post was boosted, keep it outside an organic-only comparison unless the mixed basis is explicitly requested.
