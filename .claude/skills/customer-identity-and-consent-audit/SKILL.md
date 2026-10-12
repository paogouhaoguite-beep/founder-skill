---
name: customer-identity-and-consent-audit
description: Investigate duplicate customer records and reconcile consent evidence
  before merging profiles or exporting contacts. Shared email or a past order alone
  does not prove identity or permission.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=customer-identity-and-consent-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Customer Identity And Consent Audit

Built by [ShopChief](https://shopchief.ai/?utm_source=customer-identity-and-consent-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

Customer IDs, raw/normalized email and phone, verified identity signals, order references, consent status/channel/source/timestamp, store and jurisdiction context. Include existing merge policy and conflicting records.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Normalize email/phone comparison keys using explicit rules while preserving original values. Group matches as candidates, not confirmed duplicates. Shared household addresses and recycled phone numbers are weak identity evidence.
2. Build a conflict table for each group: names, verified contact ownership, account access, order linkage, store/tenant and consent events. Keep cross-store identities separate unless the merchant explicitly owns the scope and proves linkage.
3. Reconcile consent per channel and purpose using authoritative events. Do not convert historical purchase, missing status or a transactional email into marketing consent. Conflicting status is blocked pending the actual consent system/policy; do not automatically choose the most permissive record.
4. For an approved merge, document surviving ID, source IDs, field precedence, order/history transfer expectations and fields the platform cannot merge. Export an immutable pre-merge snapshot; verify current platform support before acting.
5. Deliver proposed merge/review/no-merge decisions and eligible/suppressed/unknown contact counts without exposing unnecessary personal data. After any authorized merge, confirm both identity and consent/history state.

## Deliverable

Return the duplicate review queue and consent reconciliation with masked contact details in summaries; separate a contact-export artifact only if requested.

| Candidate group | Customer IDs | Match evidence | Conflicts | Consent state by channel | Merge decision | Survivor/precedence | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
