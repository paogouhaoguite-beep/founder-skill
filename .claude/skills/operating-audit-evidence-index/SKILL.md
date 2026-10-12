---
name: operating-audit-evidence-index
description: Use when a DTC merchant needs an evidence index and gap review for a
  named merchant operational or financial audit.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=operating-audit-evidence-index&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Operating Audit Evidence Index

Built by [ShopChief](https://shopchief.ai/?utm_source=operating-audit-evidence-index&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

An evidence index and gap review for a named merchant operational or financial audit. Supply scope/period and actual request list, control owners, policy versions, source records/change approvals, prior findings and required delivery date/access restrictions.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Bind every request to its exact scope, period and control/question. Do not invent regulatory requirements from industry names or equate a generic checklist with the auditor’s request.
2. Inventory original records with stable IDs, system, extraction date, coverage, owner and accessible location; distinguish original evidence, derived schedule and management explanation. Record hash/version for exported artifacts without altering the original.
3. Trace a sample transaction/change through request, approval, execution and independent readback or reconciliation. A log entry alone does not prove the financial amount is right; a generated report alone is not operating-effectiveness evidence.
4. Map each request to complete/partial/missing/conflicting evidence, showing exact gaps and responsible owner. Keep prior corrective-action implementation separate from later effectiveness verification.
5. Prepare a factual response and access-controlled pack with a completeness checklist. Remove unnecessary personal/credential data, preserve retention holds and do not backdate or fabricate approvals.
6. Deliver evidence index, contradiction log and deadline/owner queue. No audit certification, journal posting or external submission is implied.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Request/control | Period | Evidence ID/version | Source/coverage | Approval/execution/readback | Gap | Owner/due |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
