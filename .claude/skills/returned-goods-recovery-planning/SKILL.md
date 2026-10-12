---
name: returned-goods-recovery-planning
description: Use when a DTC merchant needs a disposition and recovery plan for inspected
  returned goods.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=returned-goods-recovery-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Returned Goods Recovery Planning

Built by [ShopChief](https://shopchief.ai/?utm_source=returned-goods-recovery-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A disposition and recovery plan for inspected returned goods. Supply item/lot/serial identity, observed condition/test results, legal/brand/channel restrictions, recovery quotes, processing/freight/fees, time-to-cash and supplier warranty/RTV terms.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Verify receipt, identity and condition against category-specific approved inspection criteria. Customer allegation or serial mismatch is evidence for review, not proof of fraud. Safety/recalled goods follow responsible quality authority before economics.
2. Enumerate permitted restock/open-box/refurbish/liquidate/recycle/vendor-return paths. Clearly disclose used/repaired state; never relabel used as new or assume opened goods are resalable.
3. For each path calculate net recovery = evidenced proceeds/credit − incremental inspection/repack/repair/freight/channel costs. Keep uncertain yield, timing and collectability as scenarios; tax deduction is not equivalent cash recovery.
4. Check warranty eligibility and vendor authorization/claim window from actual terms. Track RMA, shipment, accepted credit and accounting receipt separately. No fixed claim-size or percentage threshold selects a path.
5. Compare recovery and time/capacity, assign owner, and state inventory disposition and customer resolution separately. Customer refund rights are not delayed solely to optimize merchant resale.
6. Deliver lot-level route plan and evidence checklist; physical destruction, resale listing, vendor claim and customer communication require authorized action.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Item/lot | Inspected condition | Permitted path | Proceeds | Incremental costs | Net recovery | Time/uncertainty | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
