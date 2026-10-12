---
name: fulfillment-network-scenario-review
description: Use when a DTC merchant needs a demand, capacity and fulfillment-network
  operating scenario decision.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=fulfillment-network-scenario-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Fulfillment Network Scenario Review

Built by [ShopChief](https://shopchief.ai/?utm_source=fulfillment-network-scenario-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A demand, capacity and fulfillment-network operating scenario decision. Supply demand by region/SKU/time, eligible beginning stock, confirmed receipts, commitments, candidate facilities and actual capacity/fixed/handling/freight costs, service constraints and cash limits.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Fix decision horizon, units, currency and baseline. Separate controllable choices (facility, order quantity, mode) from uncertain demand/lead time; use named scenarios with evidence ranges, not invented probabilities.
2. Time-phase available-to-promise: opening eligible stock + receipts available by date − prior commitments − proposed allocations. Never use next week’s receipt for today’s promise or allocate the same pool independently to multiple customers.
3. For each network option assign demand to facilities under actual SKU/time capacity and service constraints. Compute fixed+handling+inbound/outbound transport+supported incremental inventory costs once; preserve unmet demand or backlog explicitly.
4. Reconcile demand review, supply/capacity review and finance cash view in one scenario table. Identify a constraint conflict requiring a named decision owner; a recurring meeting calendar is not evidence of agreement.
5. Run one-variable sensitivities and coherent downside combinations, separating lost sales from retained backlog. Report feasible alternatives and break-even values, not optimality unless a validated solve exists; do not average scenarios without justified weights.
6. Deliver selected/proposed scenario, unresolved inputs, trigger and review date. No facility contract, PO, inventory promise or staffing commitment without scope.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Scenario/facility | Demand served/backlog | Dated stock/capacity | Fixed/variable cost | Service feasibility | Cash constraint | Decision trigger |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
