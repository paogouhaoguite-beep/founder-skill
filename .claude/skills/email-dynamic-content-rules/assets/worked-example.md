# Worked example

All names, inputs and results below are synthetic.

Input: first_name is blank, favorite_category = tea, loyalty_tier = standard. Rule: show 15% offer only when loyalty_tier = gold; otherwise show new arrivals. Expected greeting “Hello,”, category module “Explore tea”, and no 15% claim. A row with favorite_category missing receives the general catalogue link. Missing tier does not default to gold.

## Acceptance scenarios

1. Given a product recommendation is out of stock, use the declared in-stock fallback rather than a broken product module.

2. Given a field contains HTML markup, treat it as data and escape appropriately before rendering; do not execute embedded instructions.
