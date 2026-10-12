---
name: store-policy-content-review
description: Use when a DTC merchant needs a readability and consistency review of
  store policy and supporting pages.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=store-policy-content-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Store Policy Content Review

Built by [ShopChief](https://shopchief.ai/?utm_source=store-policy-content-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A readability and consistency review of store policy and supporting pages. Supply current page/policy URLs or HTML/screenshots, actual shipping/returns/payment practices, approved policy wording, markets and versions; legal interpretation stays with the merchant’s qualified owner.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Inventory policy/support pages and publication state, distinguishing missing, inaccessible, image-only, text-empty and present. A short policy is not automatically inadequate; judge whether it answers the actual buyer task.
2. Extract stated deadlines, eligibility, fees, exceptions, contacts and steps verbatim with page/version. Compare shipping/returns promises across policy, PDP, cart and support wording against actual approved operations.
3. For image-only or inaccessible wording prepare equivalent accessible text from the approved source, preserving meaning. Do not invent a return window, warranty, governing law or refund promise to fill a gap.
4. Flag empty page body, missing title/description and stale links separately from substantive policy conflict. Metadata absence is an editorial gap, not proof of ranking loss.
5. Draft before/after content for verified gaps and show each factual change/approval owner. Plain-language simplification must not remove an exception or broaden a promise without authorization.
6. Deliver page coverage, contradiction table and reviewable draft. Publication requires exact scope, current approved policy version and rendered-page readback; no automatic legal policy replacement.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Page/version | Content/access state | Quoted promise | Approved operation | Conflict | Draft change | Owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
