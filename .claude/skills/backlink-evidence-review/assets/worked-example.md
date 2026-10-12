# Worked example

All names, inputs and results below are synthetic.

Input: 100 exported rows contain 20 duplicates, leaving 80 links. Sampled findings: 5 point to a retired product URL, 3 low-score links are genuine hobby-forum recommendations, and 2 source pages are unavailable. Expected plan investigates redirects for the 5, retains the legitimate 3 and marks the 2 unverified. It does not disavow all low-score domains.

## Acceptance scenarios

1. Given no live access, distinguish export-reported status from current link existence.

2. Given a link has rel=sponsored, do not treat it as an undisclosed editorial endorsement or promise ranking benefit.
