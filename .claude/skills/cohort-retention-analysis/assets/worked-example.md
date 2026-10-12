# Synthetic cohorts
January cohort has 4 customers A/B/C/D. February purchases: A twice, B once. March: A once, C once. Month-1 repeat participation=2/4=50%; month-2=2/4=50%; cumulative repeat by end of March=3/4=75%. A's multiple orders count once in February's customer numerator. A cohort not yet reaching March has a blank March-age cell, not 0%.

## Acceptance scenarios
1. The file begins January 1 but existing customers bought before then. Label cohorts newly observed unless prior history proves first purchase.
2. A customer returns after skipping a month. Count the later period purchase; do not exclude them as permanently churned.
