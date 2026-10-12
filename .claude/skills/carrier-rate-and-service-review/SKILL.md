---
name: carrier-rate-and-service-review
description: Use when a DTC merchant needs a lane-level carrier rate, invoice and
  service review for inbound stock or outbound parcels.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=carrier-rate-and-service-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Carrier Rate And Service Review

Built by [ShopChief](https://shopchief.ai/?utm_source=carrier-rate-and-service-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A lane-level carrier rate, invoice and service review for inbound stock or outbound parcels. Supply dated contracts/quotes, fuel tables and indices, minimums, accessorial predicates, actual shipment/invoice rows, promised and actual service events, tender outcomes, lane/currency and merchant service requirements.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Normalize the shipment basket by lane, equipment/service, billable weight/cube, distance, dates and mandatory handling. Separate contracted, spot and quoted-not-booked evidence; a network average does not prove performance on the required lane.
2. Reprice each observed shipment using its effective linehaul, explicit minimum rule, fuel basis/index/lag and applicable accessorials. Apply the contractual order of minimums and surcharges; do not assume percentage fuel includes every charge. Reconcile expected total with billed rows and retain unsupported charges.
3. Compare bids on identical shipment and fuel scenarios, including quotes that omit an essential accessorial as unknown. Calculate billed-weight and residential/remote/appointment cost drivers before proposing a mode or consolidation change.
4. Calculate on-time pickup/delivery on eligible completed events, tender acceptance on valid tenders, invoice accuracy on reviewed invoices, and claim frequency versus severity separately. Open shipments stay in an aging queue, not assumed on time; no universal acceptable threshold.
5. Identify concentration and actual fallback capacity by lane. Review market evidence dates, current authority/insurance requirements with the responsible transport owner, and trial capacity commitments. Do not repeat generic insurance minima or infer misconduct from billing errors.
6. Deliver disputed charge evidence, negotiation items and a conditional routing-guide recommendation with merchant-selected service gates. No carrier booking, contract acceptance or allocation change without scope and confirmed capacity.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Lane/carrier | Comparable shipments | Expected all-in | Billed/quoted | Variance | Service denominator | Fallback evidence | Action |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
