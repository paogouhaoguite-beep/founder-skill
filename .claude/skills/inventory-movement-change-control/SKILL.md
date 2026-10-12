---
name: inventory-movement-change-control
description: Use when a DTC merchant needs a stock correction or transfer change set.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=inventory-movement-change-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Inventory Movement Change Control

Built by [ShopChief](https://shopchief.ai/?utm_source=inventory-movement-change-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A stock correction or transfer change set. Supply SKU/variant/location IDs, as-of on-hand/available/committed/unavailable definitions, counted quantity and cutoff movements, reason/evidence, transfer dispatch/receipt records, desired absolute or delta mode and authorized scope.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Resolve exact inventory identity and stock-owning level; reject ambiguous SKU, untracked stock or unknown location mapping. Snapshot quantity state and timestamps. Negative available can be legitimate backorder, not proof of sync error.
2. For physical count, bridge movements since count cutoff before comparing current recorded stock. State absolute target versus incremental delta explicitly; compute preview old+delta=new and preserve commitments/unavailable states.
3. For transfer, check uncommitted eligible source units. An insufficient source blocks the proposed dispatch; never bypass this with a warning. Track dispatch as source physical decrease and in-transit increase, not immediate destination availability.
4. On evidenced receipt move in-transit into destination received/quarantine and release to available only after required inspection. Reconcile network owned units across locations and in-transit, separating loss/damage with approved evidence.
5. Before an authorized update re-read state and stop if changed; use supported compare-and-set/version safeguards when available. Absolute updates from stale exports can overwrite concurrent orders; if atomic protection is unavailable, coordinate a controlled window or keep as proposal.
6. Capture operation/reference IDs and readback for every leg. Unknown timeout status requires reconciliation before retry. Never repeat a relative delta blindly or simulate a transfer with two unrelated adjustments and claim atomic success.
7. Document each tracked item’s stock-owning level and actual reservation lifecycle: reserved, consumed, released and expired events. Check actual reservation expiry and payment/cancellation transitions; do not assume every platform holds stock at checkout or forbids negative inventory. Any last-unit concurrency acceptance requires scoped testing and actual state readback, not a schema checkbox.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Item/location | Operation | Before state | Proposed delta/target | In-transit change | Evidence | Actual readback | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
