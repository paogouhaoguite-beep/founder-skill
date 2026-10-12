---
name: supplier-contract-obligations
description: Use when a DTC merchant needs an operational obligations register from
  supplier terms.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=supplier-contract-obligations&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Supplier Contract Obligations

Built by [ShopChief](https://shopchief.ai/?utm_source=supplier-contract-obligations&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An operational obligations register from supplier terms. Supply contract/SOW/amendment text with clause IDs and precedence, service scope, value/term, notice rules, actual performance evidence and merchant review priorities.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Identify signed versus draft versions, incorporated schedules and order of precedence. Extract exact source clauses for scope, price/escalation, payment, quality/SLA, remedies, change control, subcontracting, IP/data, renewal and exit.
2. Translate each obligation into actor, trigger, action/deliverable, due date, evidence and consequence. Preserve ambiguity; do not infer enforceability or missing terms from industry norms.
3. For service levels distinguish metric, clock, exclusions, measurement source, reporting and remedy/claim window. A breach is not automatically a credit: apply actual conditions and required evidence.
4. Calculate notice and delivery dates using the contract calendar convention; month-based or jurisdiction-specific deadlines require confirmation. Show budget exposure only from supported quantities/rates, never arbitrary probability-weighted legal loss.
5. Prepare clarification/negotiation positions with preferred operational outcome, fallback and specialist owner. Escalate legal/tax/privacy matters; proposed wording is a draft, not legal advice or signed agreement.
6. Return obligations calendar and evidence gaps, with renewal/termination decision owner. No notices, signatures, waivers, claims or payments are sent by producing the register.
7. For clause review quote exact text with page/section, identify the merchant side and approved playbook position, then show deviation, business impact, full proposed replacement wording, fallback and negotiation owner. Review interacting clauses and mark acceptable sections too. Without approved standard, label the proposed preference rather than invent market-standard law. For renewal compute latest notice action using actual calendar/business-day and receipt-method rules; a merchant-selected decision buffer is separate from legal notice. Unknown receipt/day-count rule means deadline provisional. Diff amended versions and missing signature pages; no reminder creation or redline submission without scope.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Clause/version | Party | Trigger | Obligation | Due/notice date | Evidence | Remedy conditions | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
