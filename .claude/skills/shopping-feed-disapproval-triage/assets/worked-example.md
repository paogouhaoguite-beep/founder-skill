# Synthetic diagnostic issue register

All items, issue IDs, dates and observations below are fictional. D1–D3 are local issue identifiers, not official Merchant Center diagnostic codes. The supplied diagnostic wording is preserved; this example does not claim a live account was accessed.

## Evidence received

- Export dated September 28: BLUE-M has “price mismatch”; RED-S has “image cannot be crawled”; GREEN-L has “missing identifier.” All three are marked disapproved in that export.
- September 27 feed: BLUE-M base price USD 40. October 1 supplied page capture shows a USD 35 sale beginning September 29. No September 28 crawl snapshot exists.
- October 1 supplied image-fetch log: RED-S image URL returned HTTP 503 once. No retry or crawler-specific evidence is available.
- GREEN-L catalog has a brand but no GTIN/MPN; identifier applicability has not been established.

## Completed triage register

| Issue / item | Diagnosis and evidence | Cause status | Smallest proposed correction | Owner | Required check before submission | Current outcome / rollback |
|---|---|---|---|---|---|---|
| D1 / BLUE-M | September 28 price diagnostic; older feed USD 40; later capture USD 35 sale | Historical cause unresolved: the sale began after the diagnostic | Reconcile base/sale fields and effective dates with the current selected variant; retain base price if still valid | Catalog + feed owner | Obtain actual sale end/timezone and current destination evidence; inspect older crawl evidence if available | Proposed only; preserve original price/sale fields |
| D2 / RED-S | One supplied fetch returned 503 at the image URL | Temporary fetch failure observed; sustained crawler blockage unproven | Have image-host owner investigate the failing URL and restore stable access; avoid replacing the image with an unrelated product | Image hosting owner | Re-fetch from permitted tools, verify actual image and destination rules; inspect platform readback after processing | Not retested; preserve original image URL and asset |
| D3 / GREEN-L | Identifier missing in both feed and catalog | Data gap confirmed; correct exception status unknown | Obtain verified manufacturer identifiers or document the applicable exception under current rules | Catalog/supplier owner | Verify exact variant and applicable platform identifier requirements | Awaiting evidence; no invented GTIN or exemption flag |

## Handoff and readback

All three issues remain open. None has a demonstrated approved status. Do not request repeated reviews while evidence is missing. If a scoped correction is authorized, record the submitted field values and timestamp, then read back each original affected item after processing.

Use this readback shape:

| Item | Submitted change/time | Processing status/time | Approval status/time | Serving evidence | Next action |
|---|---|---|---|---|---|
| BLUE-M | Not submitted | Not observed | Last supplied export: disapproved, September 28 | Not supplied | Finish sale/destination reconciliation |
| RED-S | Not submitted | Not observed | Last supplied export: disapproved, September 28 | Not supplied | Verify image access recovery |
| GREEN-L | Not submitted | Not observed | Last supplied export: disapproved, September 28 | Not supplied | Resolve identifier evidence |

**Summary:** 0 of 3 scoped items have verified approval after remediation; this means no remediation has yet been accepted, not that every current live status has been checked. Do not replace absent current readback with the old export's status.

## Acceptance scenarios

1. Feed upload returns success but an item's readback remains pending. Report submitted/pending, not fixed, approved or serving.
2. All items are blocked by an account-level misrepresentation notice. Preserve that scope and route to account evidence rather than rewriting every item title.
