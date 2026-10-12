# Synthetic worked example

Input records: C1 Maya Li, maya@example.test, phone blank, marketing opt-out; C2 Maya Li, same email, phone +15550100, marketing opt-in without proof; C3 Noah Li, same household email, different phone. Owner confirms C1/C2 are Maya, not C3.

Review result: proposed cluster {C1,C2}, survivor C1; name/email retained from C1; phone proposed from C2 with provenance; consent conflict remains unresolved and does not authorize marketing. C3 stays separate. Pair checks involving C3 fail identity confirmation despite shared email. Proposed count after approved merge: 3→2; actual CRM count remains 3 because nothing ran.
Field ledger: C1.phone ← C2.phone (fill blank, review approved); C1.marketing ← no change (conflict); C2 order associations → proposed native merge review, never delete/reimport. Deliver merge-plan.csv and conflicts.csv as unapplied drafts.

Boundary 1: two exact names only → review candidate, no merge decision.
Boundary 2: A/B share email and B/C share phone but A/C incompatible → split/hold full cluster; never transitive auto-merge.
