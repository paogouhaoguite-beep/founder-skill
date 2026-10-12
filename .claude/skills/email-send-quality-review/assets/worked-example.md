# Worked example

All names, inputs and results below are synthetic.

Input: Campaign “20% off until Friday” links to a page with 10% off; audience has 5,000 rows, including 30 suppressed recipients. Expected review blocks the mismatched offer and excludes the 30, leaving at most 4,970 before dedup/other eligibility. Passed mobile HTML preview does not offset either blocker. After fixes the campaign is ready for approval, not sent.

## Acceptance scenarios

1. Given suppression data predates a recent unsubscribe import, recipient eligibility remains unresolved until refreshed.

2. Given a seed test used HTML v1 but production uses v2, apply the test only to unchanged portions and retest affected rendering.
