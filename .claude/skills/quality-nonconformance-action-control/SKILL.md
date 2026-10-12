---
name: quality-nonconformance-action-control
description: Use when a DTC merchant needs a product nonconformance investigation
  and corrective-action register.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=quality-nonconformance-action-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Quality Nonconformance Action Control

Built by [ShopChief](https://shopchief.ai/?utm_source=quality-nonconformance-action-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A product nonconformance investigation and corrective-action register. Supply product/lot/revision, approved specification, measurement/inspection records, affected quantities/locations/orders, containment evidence, responsible quality owner and applicable approved requirements.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Record actual versus specification with unit/tolerance and instrument/calibration evidence. Identify affected lot/adjacent lots, WIP/finished stock and shipped orders; unknown traceability broadens the investigation, not certainty of defect.
2. Separate immediate containment proposal/confirmed hold from root-cause analysis. Escalate safety or regulatory questions to responsible owner; do not claim authority to release, recall or destroy.
3. Use IS/IS-NOT and cause hypotheses (material, method, equipment, measurement, environment, people). Every why-link needs evidence or a verification action; “human error” or retraining alone does not prove root cause.
4. Compare rework-to-spec, repair with approved deviation, supplier return and scrap under quality/engineering authority. Cost cannot override safety/specification gates; record disposition approvals and retest evidence.
5. Define corrective action owner/date, implementation proof and a risk-appropriate effectiveness sample/window agreed by quality owner. Installing a control is verification, not proof recurrence ended. Do not impose universal 90 day/3lot closure rules.
6. Return NCR/CAPA register with open evidence and release conditions; no automatic production release, supplier claim, public recall or customer contact.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| NCR/lot | Actual/spec | Scope/containment | Cause evidence | Disposition authority | Action | Effectiveness evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
