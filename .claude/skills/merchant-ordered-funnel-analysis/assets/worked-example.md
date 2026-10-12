# Synthetic worked example

Input: UTC, person entry cohort Oct 1, 24-hour window, data through Oct 3; stages view/cart/checkout/purchase, strictly later timestamps. P1 has cart 08:00, view 09:00, cart 10:00, checkout 11:00, purchase 12:00. P2 view 09:00/cart 10:00 only. P3 view 09:00 only. P4 view 09:00/cart 10:00/checkout 11:00 only. P5 purchase 08:00/view 09:00 only.

Output: viewed 5; carted 3 (60% of viewers); checkout 2 (66.7% of carted); purchased 1 (50% of checkout, 20% of viewers). P1's 08:00 cart is ignored in favor of the first cart after entry; P5's earlier purchase never counts. Largest observed loss is view→cart: 2 people. This tiny cohort does not prove a broken page or mobile effect. Inspect the two paths and tracking completeness before proposing a test.

Boundary 1: data cutoff Oct 1 at noon → every still-open 24-hour window is censored, not a nonconverter.
Boundary 2: only daily totals are supplied → report unordered totals; do not present this sequence-qualified funnel.
