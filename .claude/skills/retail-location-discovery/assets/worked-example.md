# Worked example

All names, inputs and results below are synthetic.

Synthetic store: Oak Tote Studio,18 Cedar Lane, weekday pickup12:00–18:00 by appointment; no weekend pickup. Current directory says09:00–21:00 daily. Website says weekday pickup but omits appointment requirement.
Location copy: “Collect your order at Oak Tote Studio,18 Cedar Lane. Weekday pickup is available from12:00 to18:00 by appointment. Contact the store to arrange collection.”
Queue: directory hours→replace with verified schedule after authorized owner update; site pickup details→add appointment condition. Both are drafts, not live changes. No map pin coordinates or sales lift invented.

## Acceptance scenarios

1. A seller ships nationwide from a private home and has no customer-facing location. Do not generate city profiles or publish the home address; return eligibility and customer-discovery constraints.

2. A temporary event has different dates/hours from the permanent store. Maintain a dated event record; do not overwrite the permanent schedule with a recurring claim.
