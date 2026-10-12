---
name: deferred-revenue-evidence-schedule
description: Use when a DTC merchant needs a working schedule for prepaid goods or
  bundled service obligations under a finance-approved recognition policy.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=deferred-revenue-evidence-schedule&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Deferred Revenue Evidence Schedule

Built by [ShopChief](https://shopchief.ai/?utm_source=deferred-revenue-evidence-schedule&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A working schedule for prepaid goods or bundled service obligations under a finance-approved recognition policy. Supply contract/line IDs, consideration excluding collected tax as defined by finance, approved distinct obligations and allocation basis, event evidence, opening balances and journal references.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Obtain the finance owner’s actual obligation definitions, recognition triggers and accounting policy. Do not decide that every physical product recognizes at carrier delivery or every subscription is recognized daily.
2. Allocate contract consideration using the approved standalone-price method or other explicitly supplied basis. Reconcile all allocations to transaction price including residual rounding; missing obligation or allocation evidence blocks a finalized schedule.
3. Trace each approved trigger to dated shipment/delivery/service evidence. A charge or platform paid status alone is not the recognition trigger. Separate scheduled future recognition from supported period recognition.
4. Roll forward each obligation: opening deferred balance + allocated additions − recognized amounts − approved credits/reclassifications = closing. This is not necessarily all store cash receipts minus all revenue because scope/tax/timing differ.
5. Keep returns, warranty and variable-consideration estimates as finance-approved inputs with effective date. Do not generate universal return reserves, breakage or automatic adjusting entries.
6. Deliver reconciled evidence schedule and unresolved policy questions for finance review; no journal posting, accounting certification or customer transaction.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Contract/obligation | Approved basis/trigger | Opening | Additions | Supported recognition | Credits | Closing | Evidence gap |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
