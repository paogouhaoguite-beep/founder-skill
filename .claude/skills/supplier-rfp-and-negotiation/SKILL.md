---
name: supplier-rfp-and-negotiation
description: Use when a DTC merchant needs a comparable supplier proposal and negotiation
  pack.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=supplier-rfp-and-negotiation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Rfp And Negotiation

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-rfp-and-negotiation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A comparable supplier proposal and negotiation pack. Supply approved requirements, forecast quantity/usage bands, supplier quotes with scope/exclusions, contract horizon, implementation/exit costs, merchant evaluation weights and negotiation authority.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Write RFP response schedule with must-pass acceptance evidence, desired criteria, shared demand scenarios, delivery/quality requirements, pricing template and submission dates. Keep supplier communications draft until authorized.
2. Normalize currency, term, units, volume tiers, one-time setup and recurring costs. Required-but-unpriced is unknown, never zero. Compare implementation, internal effort, freight, packaging, testing, support, renewal escalation and exit costs on the same scope.
3. Calculate undiscounted horizon TCO and optional finance-supplied discounted case separately. Distinguish all-unit volume discounts from graduated tiers; check minimum commitments, overages and required options under low/base/high volumes.
4. Apply mandatory gates before weighted preferences; merchant weights must sum to 1 and score anchors cite evidence. Missing criterion remains unknown; do not award a high total score over a mandatory failure or claim a certification from a badge.
5. Build negotiation brief with confirmed facts, ask, rationale, concession cost, walk-away condition and best supported alternative. Do not fabricate competing bids or promise reference rights/volume without authorization.
6. Define proof-of-capability pilot, reference questions and acceptance/exit criteria before award. Return side-by-side comparison, clarification list and negotiation options; signing and supplier contact remain separate.
7. For shortlisted vendors, attach source page/section to every commercial comparison cell and show year-one, steady-state, escalators and exit cost on the same term. Prepare a negotiation brief with target, authorized ceiling, verified alternative cost/timing, conditional concession and fallback. Draft reference-check questions tied to specific risks: actual rollout delay, billed overages, incident handling, data/export or tooling handover, and termination experience; do not claim references were contacted.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Supplier | Mandatory gates | Setup | Recurring basis | Required unknowns | Exit cost | Horizon TCO | Negotiation ask |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
