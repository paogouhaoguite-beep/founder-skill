---
name: privacy-data-handling-review
description: Use when a DTC merchant needs a field-level personal-data sharing, retention
  or customer-request evidence review.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=privacy-data-handling-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Privacy Data Handling Review

Built by [ShopChief](https://shopchief.ai/?utm_source=privacy-data-handling-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A field-level personal-data sharing, retention or customer-request evidence review. Supply data dictionary and system/recipient inventory, actual purposes, approved jurisdiction-specific policy/legal instructions, retention triggers, contracts, request identity verification and preservation holds.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map each field to source, purpose, recipient, granularity, access owner and downstream copy. Pseudonymous IDs and hashed emails may remain linkable; aggregation alone is not proof of anonymity.
2. Compare proposed sharing against the minimum fields needed for the stated task. Record purpose restrictions, allowed onward sharing, security, retention/deletion and contractual responsibility evidence; do not infer permission from an app connection or clean-room label.
3. Build a retention schedule from actual approved rules: category, trigger, period, legal/policy source and hold exceptions. Unknown or conflicting retention rules block deletion; never apply generic seven-year/90-day defaults.
4. For access/erasure requests verify identity and scope through the merchant’s approved process without gathering unnecessary identity documents. Inventory linked systems and distinguish export, deletion, anonymization, suppression and restricted retention; keep request and provider completion receipts separate.
5. For consent-dependent tracking document expected behavior under accept/reject/withdraw states and the actual observed requests/events. A banner or CMP installation alone does not prove scripts obey choices; no tracking activation is implied.
6. Deliver field-minimization plan, request/retention exception register and questions for the privacy owner. This is evidence preparation, not a legal compliance determination; no sharing, deletion, consumer reply or policy publication without authorized scope.
7. Before preparing an authorized redacted artifact, inventory structured fields and free-text quasi-identifiers, inspect locale-specific formats and context, and choose remove/mask/pseudonymize per downstream purpose. Use an approved secure tokenization mechanism only when joins are needed; a homegrown unsalted hash is not anonymization. Review representative normal and adversarial samples after transformation for leaks and utility; no regex or NER pass guarantees complete removal. Report original-to-redacted example and residual risk without exposing real identifiers.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Field/system | Purpose/recipient | Minimum necessary | Policy evidence | Retention trigger/hold | Requested versus actual action | Owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
