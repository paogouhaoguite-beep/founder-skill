# Synthetic worked example

Synthetic file F1 is 60 days old with no product/page references but appears in a live email template: **retain, referenced**. F2 has no reference in audited store surfaces but external campaign embeds were not checked: **unknown external use; no deletion**. Draft D1 is 90 days old with a pending wholesale approval and reserved 5 units: **retain and ask owner**, not stale cleanup. Draft D2 has explicit owner closure and exported backup: proposed deletion of D2 only, subject to current-state recheck.

## Boundary case 1

File URLs differ only by a known resize transform but IDs match. Preserve one identity with both references; do not call the resized URL a separate orphan.

## Boundary case 2

D2 receives payment activity after preview. Block deletion and reopen review rather than applying stale approval.
