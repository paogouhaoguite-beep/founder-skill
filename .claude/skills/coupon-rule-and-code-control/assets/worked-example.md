# Synthetic worked example

Input: cart subtotal $100, promo A 10% then B 20%, sequential stacking allowed; shipping $8 excluded. Expected discount: $10 + $18 = $28; merchandise due $72, plus shipping $8 = $80. Additive stacking would be $70 merchandise and is a different policy. For a minimum subtotal $100, carts $99.99/$100/$100.01 produce ineligible/eligible/eligible.

Bulk batch request: 3 codes; existing SAVE-A. Proposed SAVE-A, SAVE-B, SAVE-C has one collision and only 2 valid new codes; do not report 3 created.

## Boundary case 1

An expired code has a future contractual redemption extension: flag conflict and obtain campaign-owner policy, do not delete.

## Boundary case 2

The code-creation request timed out after two of three successes: read back the three intended codes and retry only the proven missing one.
