---
name: production-capacity-and-sequencing
description: Use when a DTC merchant needs a finite production schedule for a DTC
  brand or contract manufacturer.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=production-capacity-and-sequencing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Production Capacity And Sequencing

Built by [ShopChief](https://shopchief.ai/?utm_source=production-capacity-and-sequencing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A finite production schedule for a DTC brand or contract manufacturer. Supply released jobs/BOM/routings, due dates, quantities/yield evidence, work-center calendars, setup/changeover times, material release and labor skills, maintenance and frozen commitments.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map job operations and precedence to actual constrained resources. Net calendar time subtracts documented breaks, maintenance and unavailability once; no arbitrary efficiency/OEE discount unless observed and not already embedded in run rates.
2. Calculate operation load = setup time + quantity/run rate, adjusting quantity for evidenced yield when relevant. Compare by work center and time bucket; total plant hours can conceal a bottleneck.
3. Sequence feasible released jobs using declared merchant rule (due date, customer promise or setup-family), reserving each resource interval and honoring material release/precedence. Show each start/finish and resulting lateness; a heuristic is not a globally optimal solver.
4. Check constraint throughput and downstream capacity before optimizing non-constraint utilization. Compare overtime, outsource, batch split and changed sequence only with supported cost/capability; preserve approved frozen window.
5. For a breakdown rebuild the remaining interval ledger, identify impacted promises and draft options with owner. Unknown repair or material date stays scenario/blocked. Do not release production or change supplier orders automatically.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Job/operation | Resource | Material ready | Setup/run hours | Start/finish | Due | Lateness | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
