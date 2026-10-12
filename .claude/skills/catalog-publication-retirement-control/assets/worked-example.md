# Synthetic worked example

Input: P1 active but unpublished on the online store; P2 active/out of stock with confirmed replenishment next week; P3 obsolete draft with no orders; P4 retired but supports an active subscription. Merchant asks to archive obsolete drafts.

Expected: archive proposal contains P3 only. P1 is a publication investigation, P2 remains unchanged, P4 is blocked pending subscription handling. Deletion and redirects are not included in the request.

Lifecycle case: outgoing A has 20 released units and successor B changes ingredients. Keep version-specific listings/evidence; draft “A is being discontinued; B has a different ingredient list. Your subscription will not switch without your choice.” Present opt-in/stop options subject to approved policy. No inherited A reviews asserted for B.

## Boundary case 1

A field name resembles a removed review app but another template still renders it: keep the field and investigate the caller.

## Boundary case 2

The store page still shows an archived item immediately after change: verify current admin state and caching before retrying the mutation.
