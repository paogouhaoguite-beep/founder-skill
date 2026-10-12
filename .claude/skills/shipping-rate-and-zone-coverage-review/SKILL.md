---
name: shipping-rate-and-zone-coverage-review
description: Use when a DTC merchant needs a destination and basket test matrix for
  shipping rates.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=shipping-rate-and-zone-coverage-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Shipping Rate And Zone Coverage Review

Built by [ShopChief](https://shopchief.ai/?utm_source=shipping-rate-and-zone-coverage-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A destination and basket test matrix for shipping rates. Supply active zones/profiles/precedence, exact postal/country predicates, service and fulfillment locations, weight/price boundaries, package dimensions, currencies, exclusions, dated carrier divisor/rounding rules and merchant-approved delivery/import-charge wording.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Normalize zone predicates and evaluation order; overlapping country labels alone do not prove a conflict when postcodes, product profiles or precedence differ. Identify destinations and item combinations with no eligible shipping method.
2. Construct test baskets just below, exactly at and just above every price/weight threshold, including discounts, taxable basis, mixed profiles, free-shipping codes and currency conversion where actually configured. Use the platform’s observed basis, not an assumed subtotal.
3. For supplied carrier rules compute volumetric weight using matching dimension/divisor units, compare with actual weight and apply the documented rounding/minimum. Missing package dimensions or divisor leaves a quote incomplete.
4. Compare displayed methods and charges with the expected rule matrix and actual checkout evidence if available. Export-only conclusions are configuration hypotheses until a current checkout test confirms them.
5. For cross-border baskets identify who pays documented duties/taxes/fees and delivery-service exclusions from actual contract and merchant policy. Do not infer landed cost or classification from a country code, and do not promise no import charges without evidence.
6. Return coverage gaps, threshold discontinuities and a reversible change preview, with checkout retest and owner. No live shipping profile edit or test purchase/payment without authorization.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Destination/basket | Profile/rule | Basis/threshold | Expected method/charge | Observed checkout | Gap | Owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
