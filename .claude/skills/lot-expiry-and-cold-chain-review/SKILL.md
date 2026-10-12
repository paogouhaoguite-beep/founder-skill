---
name: lot-expiry-and-cold-chain-review
description: Use when a DTC merchant needs a lot-level freshness and cold-chain exception
  review for perishable DTC goods.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=lot-expiry-and-cold-chain-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Lot Expiry And Cold Chain Review

Built by [ShopChief](https://shopchief.ai/?utm_source=lot-expiry-and-cold-chain-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A lot-level freshness and cold-chain exception review for perishable DTC goods. Supply product/lot IDs, exact date-code meaning, manufacture/expiry dates, approved storage conditions and excursion procedure, sensor coverage, shipment lead time and promised remaining shelf life.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Use product-specific approved date and temperature rules; do not infer safety from generic best-before/use-by labels or universal temperature limits. Resolve ambiguous date format and timezone before allocation.
2. Compute remaining life at expected delivery, not only today. A lot qualifies only if permitted condition/state and remaining-life promise are met, then prioritize earliest eligible expiry under FEFO.
3. Reconcile lot quantities across receipt, allocation, dispatch, return and quarantine with one-step-back/forward trace IDs. Mixed lots must retain quantities separately; do not erase lot identity during repacking.
4. Review sensor interval/gaps and excursion evidence against the approved procedure. Unknown exposure or a breached limit goes to the qualified quality owner; an average temperature cannot prove no excursion.
5. Estimate quantities at risk before expiry using bounded demand and logistics scenarios. Commercial markdown/disposition is possible only for stock quality has released; recall or safety withdrawal is a separate qualified process.
6. Deliver eligible lot allocation and quarantine/evidence queue with owner. No expiration extension, safety certification, recalled-stock clearance or release of quarantined goods.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Lot | Available units | Expiry/rule | ETA remaining life | Temperature evidence | Eligible allocation | Quarantine/gap | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
