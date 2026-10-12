---
name: store-configuration-and-access-review
description: Use when a DTC merchant needs a redacted store-settings, account-access
  and payment-mode review.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=store-configuration-and-access-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Store Configuration And Access Review

Built by [ShopChief](https://shopchief.ai/?utm_source=store-configuration-and-access-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A redacted store-settings, account-access and payment-mode review. Supply approved baseline and current configuration snapshots, named owners/roles, actual privilege and MFA attestations, last activity if available, gateway mode evidence and intended environment.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Inventory store/environment, collection date and coverage. Exclude secret values and signed URLs; use an allowlist of reportable configuration fields. Presence/absence of a masked credential is not proof that credentials work.
2. Diff typed settings by stable group/key and distinguish intentional environment differences, defaults and unobserved fields. A redacted value cannot be compared for equality; use configured/unknown attestation without exposing it.
3. Compare staff/app privileges with the current role need and employment/vendor status. Flag excessive scope, unknown owner, stale access evidence and offboarding gaps; missing last-login data is unknown, not proof of inactivity.
4. Check admin MFA/recovery ownership and separate customer account controls. Passwordless login does not eliminate phishing or account takeover. Do not reproduce a password-hashing/authentication implementation from this operational review.
5. For payment methods record enabled state, documented live/test mode, supported market/currency and observed checkout visibility separately. A nonempty setting or first display order does not prove a live charge will succeed.
6. Deliver minimal proposed permission/configuration changes and a rollback/verification owner. No credential export, account revocation, security policy change or real payment test without authorization; preserve emergency recovery access.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Setting/account | Environment | Baseline/current | Evidence coverage | Privilege or mode issue | Owner | Proposed action |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
