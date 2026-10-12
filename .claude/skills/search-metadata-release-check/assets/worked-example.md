# Worked example

All names, inputs and results below are synthetic.

Input: Before page returns 200 with self-canonical and indexable robots. After deployment returns 200 but contains noindex; release notes only planned a photo change. Expected finding: unintended indexability regression. Another page’s title changes from “Blue Mug” to “Blue Ceramic Mug” as intended; do not mark it critical merely because text differs. A 403 snapshot is invalid for content comparison.

## Acceptance scenarios

1. Given the post-release response is a maintenance page, report capture failure and recheck instead of claiming content deletion.

2. Given schema removal eliminates a false rating, mark it an intentional correctness fix rather than automatically restoring it.
