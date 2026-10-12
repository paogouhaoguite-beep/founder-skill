---
name: product-claim-evidence-review
description: Use when a DTC merchant needs a claim-by-claim substantiation review
  for product pages, packaging or ads.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=product-claim-evidence-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Product Claim Evidence Review

Built by [ShopChief](https://shopchief.ai/?utm_source=product-claim-evidence-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A claim-by-claim substantiation review for product pages, packaging or ads. Supply exact copy/image context, SKU/formulation/version, destination markets/product category, dated studies/certificates/baselines and current primary guidance or qualified review.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Extract exact express and implied claims with page/panel location. Classify performance, comparison, health, safety, environmental or certification scope; distinguish product, component, packaging and company claims.
2. Map each claim to evidence for the same tested item, population, conditions, comparator, result and date. A certificate is not proof of every implied benefit; record validity, issuing body and specific certified scope.
3. For environmental comparisons record lifecycle boundary, baseline, geography, measurement period and denominator. Separate absolute emissions, intensity reduction, offsets and avoided-emission scenarios; never call a numerical risk score proof of compliance.
4. Check how consumers could interpret qualifiers, image juxtaposition and endorsements. Preserve evidence-supported limits visibly. Changing “cures” to “may help” or adding a disclaimer does not create substantiation.
5. Use current primary guidance for exact category/jurisdiction and mark proposed rules separately from effective requirements. Without current applicable evidence return needs-qualified-review, not legally compliant/noncompliant. Do not reproduce source universal FDA/platform rules.
6. Return exact claim, support/gap, a narrower evidence-bound draft if possible and reviewer/expiry. Unsupported numerical, health or sustainability facts must not be invented to make copy sound safer. Publishing or legal approval is outside this analysis.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Claim/location | Consumer takeaway | SKU/market | Evidence ID/scope | Gap | Evidence-bound draft | Review owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
