---
name: order-state-change-control
description: Use when a DTC merchant needs a scoped hold, release or cancellation
  review for named orders.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=order-state-change-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Order State Change Control

Built by [ShopChief](https://shopchief.ai/?utm_source=order-state-change-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A scoped hold, release or cancellation review for named orders. Supply payment/capture/refund state, remaining fulfillment quantities, warehouse handoff, each hold reason and owner, stock reservation history, status definitions, desired transition and notification choice.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Build a state vector rather than one status: payment, fulfillment per line/location, cancellation, inventory reservation and independent holds. Confirm plugin/warehouse semantics from actual configuration.
2. For hold, identify remaining fulfillments that can still be stopped and owner who confirms the physical stop. A storefront status change alone does not stop a 3PL already picking or shipping.
3. For release, resolve the exact hold reason and ensure payment/stock/other independent holds permit release. Never clear an unrelated fraud, address or quality hold as a side effect.
4. For cancellation, separate uncaptured authorization void, captured-payment refund, reservation release and physical restock. Already dispatched items require an intercept/return workflow; cancellation is not evidence of receipt.
5. Preview every order and each side effect (cash, stock, email, automation). Re-read state before an authorized transition; keep partial successes and unknown job outcomes separate. Read actual stock/payment records afterward rather than assume platform automatic effects.
6. Deliver an action log with blocked records and specific prerequisites. Do not bulk-set completed or paid to bypass real fulfillment/payment evidence.
7. Trace duplicate, delayed and out-of-order order events using event identity and current version before proposing a transition. Payment confirmation, inventory reservation, fulfillment release and notification are separate effects; a status comparison alone is not idempotency for all side effects. Record each attempted effect and receipt, including pending/unknown outcomes.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Order | Payment | Fulfillment | Hold owner/reason | Proposed transition | Stock/cash side effects | Evidence | Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
