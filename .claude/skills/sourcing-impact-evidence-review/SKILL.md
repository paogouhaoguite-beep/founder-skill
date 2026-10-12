---
name: sourcing-impact-evidence-review
description: Use when a DTC merchant needs a supplier environmental/social evidence
  and bounded activity-emissions comparison.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=sourcing-impact-evidence-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Sourcing Impact Evidence Review

Built by [ShopChief](https://shopchief.ai/?utm_source=sourcing-impact-evidence-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A supplier environmental/social evidence and bounded activity-emissions comparison. Supply the sourcing decision, facility/product boundaries, activity quantities/units, dated emission-factor source/method/geography, supplier attestations/audits/certificate scope and merchant criteria.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Define decision scope and functional unit before comparing suppliers: same delivered product function/quantity, period, facilities and included lifecycle stages. A transport-only estimate is not a product or company footprint.
2. Build an evidence register distinguishing supplier assertion, certificate with scope/expiry, audit observation and corrective-action proof. A certification does not prove every product/facility or labor practice is compliant; unresolved coverage stays visible.
3. Calculate each supported emissions line as activity × factor with compatible units. Document factor date, geography, technology and boundary, missing categories and uncertainty; do not mix spend-based and activity-based estimates for the same activity.
4. Compare absolute emissions and intensity only on like boundaries. Changes in volume/mix may explain absolute changes; purchased offsets or avoided-emission scenarios must not silently cancel inventory emissions.
5. Evaluate sourcing options against merchant requirements and actual cost/availability/quality constraints. Separate disqualifying missing mandatory evidence from preferred improvements; do not invent ESG scores or legal clearance.
6. Deliver evidence gaps, bounded calculations and supplier questions. No public green claim, certification statement or supplier commitment without the relevant authorized evidence review.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Supplier/activity | Boundary/unit | Quantity | Factor/source/date | Calculated estimate | Evidence gap | Decision question |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
