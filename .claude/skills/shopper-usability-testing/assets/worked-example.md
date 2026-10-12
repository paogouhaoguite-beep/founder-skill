# Synthetic worked example

Input: Mobile prototype of a bag store. Task: “You have a 14-inch laptop measuring 31 × 22 cm and need a bag for commuting. Find a suitable option and show how you would verify the fit.” The merchant has physically checked the device: variant A fits; variant B does not fit in any allowed orientation. This compatibility matrix is the test ground truth. Success: selects a verified fitting variant and locates dimensions without help; no purchase.

Synthetic observation table:
| Participant | Result | Evidence | Issue |
|---|---|---|---|
| P1 | Unassisted success | 00:42 dimensions opened | None |
| P2 | Assisted completion | 01:20 moderator points to tab | Specification label missed |
| P3 | Incorrect completion | 00:35 selects variant B despite verified incompatibility | Unverified exterior dimensions used instead of compatibility table |

Unassisted success = 1/3 valid attempts = 33.3%; assisted completion = 1/3. This small purposive sample is diagnostic, not the store’s conversion rate. Retest an explicit compatibility label using the same success criterion.

Boundary scenario 1: Prototype link fails before the task starts. Log a technical failure separately; state whether excluded under the predeclared valid-attempt rule.
Boundary scenario 2: The only available site accepts real payments. Stop before submitting an order unless a specific test transaction is authorized.
