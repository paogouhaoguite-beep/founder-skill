---
name: bundle-component-availability
description: Use when a DTC merchant needs a sellable bundle capacity and component-reservation
  review.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=bundle-component-availability&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Bundle Component Availability

Built by [ShopChief](https://shopchief.ai/?utm_source=bundle-component-availability&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A sellable bundle capacity and component-reservation review. Supply effective bill of materials by bundle variant, required component quantities, component stock-owning IDs, location/state, commitments, assembly constraints, and planned bundle demand.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Resolve each parent bundle variant to an effective BOM. Distinguish virtual bundles consuming components from preassembled finished stock; do not add both as independently available if they represent the same goods.
2. For a single bundle compute capacity as the minimum floor(eligible component quantity/required component quantity), where eligible excludes committed, quarantined and inaccessible stock. Missing mappings or zero/negative BOM requirements block the calculation.
3. For multiple bundles sharing components evaluate proposed quantities together: sum(bundle quantity × component requirement) must not exceed each eligible component pool. Summing standalone bundle capacities overstates shared inventory.
4. Apply location and assembly/pack capacity constraints. Stock in separate locations cannot support a single-location bundle promise unless the merchant explicitly accepts split assembly/shipment with feasible timing.
5. Identify the binding component and feasible demand priority using supplied commercial rules. Show incremental component needs and alternative allocations; do not silently substitute a component or change advertised bundle contents.
6. Prepare BOM/version, reserved quantities and shortage queue. Actual bundle creation, reservation, component adjustment or customer offer changes require scope and state readback.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Bundle/BOM version | Planned quantity | Component consumption | Eligible pool | Binding constraint | Feasible allocation | Shortage |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
