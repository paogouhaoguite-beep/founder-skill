---
name: regulatory-change-action-register
description: Use when a DTC merchant needs an operational impact register for a supplied
  regulatory change.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=regulatory-change-action-register&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Regulatory Change Action Register

Built by [ShopChief](https://shopchief.ai/?utm_source=regulatory-change-action-register&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An operational impact register for a supplied regulatory change. Supply official text/link and status/date, counsel-confirmed applicability, affected SKU/market list, inventory/packaging commitments, owner lead times and cost estimates.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Separate publication, proposal/comment, enactment, effective, enforcement and transition dates. Quote only the specific requirement needed and record authority/source revision; absence of current official text blocks a definitive deadline.
2. Map applicability by product/material/market/entity with yes/no/unknown and rationale from qualified guidance. Unknown is not exempt. Map affected assets (formulation, packaging, claims, supplier certificates, listing) without guessing competitor compliance.
3. Build dependency plan from validation/qualification through artwork, purchase commitments, sell-through/transition and channel updates. Check date feasibility against actual lead times; proposed rule scenarios remain scenarios.
4. Itemize one-time and recurring costs with currency and source: obsolete materials, redesign, testing, systems, training. Count overlapping SKUs/assets once; exposed revenue is not forecast lost revenue or penalty.
5. Record alternatives and owners, evidence required for each completion and review dates. Do not invent penalties, legal requirements or universal implementation phases.
6. Deliver dated impact register and decision brief for merchant/legal owner; no filing, public comment submission, contract or policy change is authorized by analysis.
7. For a new merchant initiative as well as a rule change, map actual entity, product/category, data use, customers and operating jurisdictions to each candidate obligation. Preserve applies/not applicable/unclear with specific current authoritative citation, effective/proposal state and last-checked date. Require qualified review of applicability and a named approval gate; do not infer applicability from “EU users” alone or repeat general threshold/deadline examples as current law.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Requirement/source | Legal status | Affected SKU/asset | Applicability evidence | Dependency | Cost | Owner/date | Completion proof |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
