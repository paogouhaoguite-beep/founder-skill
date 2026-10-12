---
name: order-risk-review-queue
description: Use when a DTC merchant needs a human review queue for flagged orders
  or unusual refund/return patterns.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=order-risk-review-queue&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Order Risk Review Queue

Built by [ShopChief](https://shopchief.ai/?utm_source=order-risk-review-queue&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A human review queue for flagged orders or unusual refund/return patterns. Supply provider risk assessment and actual reasons, rule versions, order/payment/fulfillment events, linked past dispute outcomes, refund and return events, review decisions and merchant response policy.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Keep provider risk label, triggered rule, observable evidence and reviewer conclusion separate. A high score, address mismatch, VPN, refund request or dispute is not proof of fraud. Never invent feature contributions for an opaque model.
2. Join events by order/customer/payment IDs, distinguishing identity certainty and shared-household ambiguity. Consolidate multiple partial refunds on one order before counting affected orders; separate authorized goodwill, defects and service failures from unexplained patterns.
3. Calculate count, value and rate with explicit denominator, observation window and minimum maturity. Compare like-for-like cohorts and show small samples; do not create universal suspect thresholds or probability scores from arbitrary weights.
4. For each flagged order show payment authorization/capture status, fulfillment state, exact trigger, supporting and contradicting evidence, next evidence request and the supplied review deadline. Sort using merchant priority and exposure, not nationality or inferred personal characteristics.
5. Prepare neutral tags/hold recommendations with expiry and owner. A prior dispute that was won or a resolved service complaint must not become a permanent automatic customer blacklist. A hold must address each relevant fulfillment and cannot undo a dispatched parcel.
6. Check outcomes of reviewed, declined and allowed cohorts separately. Observed chargebacks do not prove every declined order was fraud; lost good demand needs independent outcomes or a bounded study. No capture, cancellation, refund, rejection or tag write without scope and readback.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Order | Source risk/rule | Observed facts | Alternative explanation | Payment/fulfillment | Evidence gap | Proposed review | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
