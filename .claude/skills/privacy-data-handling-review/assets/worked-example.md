# Synthetic worked example

Synthetic carrier-label task needs recipient name/address and order reference, but proposed export also contains marketing segment, birth date and lifetime spend. Output: omit those three unrelated fields; use reference O1, not free-text notes. Customer C1 asks deletion. CRM profile has no hold, invoice record has a finance preservation hold, email suppression record prevents re-contact. Queue: privacy owner decides CRM erasure; invoice restricted retention pending approved rule; suppression handled under approved minimization policy. No claim that deleting CRM erased all downstream copies.

Synthetic support export input: “Case C1, person alex@example.test, home address [synthetic address], item SKU7 failed.” For defect theme analysis output “Case C1, item SKU7 failed”; remove email/address rather than partially retain them. If joining repeat cases is necessary use an approved stable case/person pseudonym stored separately; no raw lookup table in the shared artifact.

## Boundary case 1

Partner calls hashed email anonymous. Record stable-linkability risk and request the actual purpose/recipient/legal review; do not mark unrestricted.

## Boundary case 2

Consent banner shows reject, but an observed analytics request still fires. Report this specific mismatch; do not certify noncompliance or claim all requests were blocked.
