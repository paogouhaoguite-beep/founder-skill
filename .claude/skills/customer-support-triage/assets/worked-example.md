# Synthetic worked example

All records, policies, people and outcomes here are fictional review fixtures. Drafts below have not been sent, published or applied to a merchant account.

## Supplied evidence

At **13:30 UTC on 2026-10-02**, four fictional tickets are pending. The merchant's supplied policy routes product safety reports immediately to its safety lead and instructs support to advise the customer to stop using the reported product. Fulfillment accepts address-change reviews before a supplied 14:00 UTC cutoff, but changes are not guaranteed until the order status is checked. No sending, refunds or order edits are authorized.

| Ticket | Order alias | Customer report | Available order evidence |
|---|---|---|---|
| T-101 | O-301 | Parcel is late | Order reference only; tracking not checked |
| T-102 | O-301 | Follow-up on the same late parcel | Same order and issue as T-101 |
| T-103 | O-302 | Requests address change | Cutoff is known; release/carrier state unverified |
| T-104 | O-303 | Reports a burning smell during use | Customer report only; cause not established |

## Completed triage register

| Case | Source tickets | Category | Priority reason | Owner | Next action | Current state |
|---|---|---|---|---|---|---|
| C-01 | T-104 | Product safety report | Merchant safety policy requires immediate escalation | Safety lead | Review the report and approve the safety-response draft | Escalation proposed; no message sent |
| C-02 | T-103 | Address change | 30 minutes until the supplied cutoff | Fulfillment lead | Check whether O-302 can still be edited, then review exact address change | Change pending verification and authorization |
| C-03 | T-101, T-102 | Late shipment | One unresolved delivery issue with a duplicate follow-up | Support lead | Check actual shipment/carrier record and respond once | Shipment state unverified |

There are **three cases from four tickets**. The address review has **30 minutes** remaining before the supplied cutoff; that cutoff is not a delivery or edit guarantee.

## Completed customer reply drafts

**C-01 — product safety, draft only:**

“Thank you for reporting the burning smell. Please stop using the product while our safety team reviews your report. Could you share the product name and a brief description of when you noticed it? We have not yet determined the cause or the appropriate resolution. You do not need to use the product again to demonstrate the issue.”

**C-02 — address change, draft only:**

“We have your request to change the delivery address for order O-302. Our fulfillment team needs to check whether the order can still be changed before today's 14:00 UTC cutoff. The address has not been updated yet. Please provide the corrected address through the store's normal private support channel; we'll confirm the outcome after the order status is checked.”

**C-03 — late parcel, draft only:**

“We have linked your two messages about order O-301 so they can be handled together. We haven't verified the latest tracking status yet. The next step is to check the shipment record; we cannot confirm a delivery date or a refund from the information currently available.”

## Acceptance case 1 — supported inputs

Produce three cases preserving all four source ticket IDs. Show the safety escalation and the 30-minute cutoff. Supply usable replies that state unverified status without claiming to have sent, refunded or changed anything.

## Acceptance case 2 — no order context

If the late-parcel messages omit the order reference, use this draft instead:

“I'm sorry you're still waiting for your parcel. Please send your order reference through this private support conversation so we can locate the shipment. We don't yet have enough information to confirm its status or arrival date.”

Do not request payment-card details, treat an unlocated order as fraud, or make up a shipment update.
