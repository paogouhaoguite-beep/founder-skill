---
name: wholesale-channel-terms-review
description: Use when a DTC merchant needs a wholesale partner commercial review for
  a DTC brand selling through multiple channels.
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=wholesale-channel-terms-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Wholesale Channel Terms Review

Built by [ShopChief](https://shopchief.ai/?utm_source=wholesale-channel-terms-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A wholesale partner commercial review for a DTC brand selling through multiple channels. Supply actual partner agreements/POs, channel pack-normalized prices and contribution, promotion calendars, service/ASN/label requirements, deductions/evidence, alternatives and negotiation authority.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Map the brand’s DTC and wholesale channels, exact packs/conditions and customer offers. Normalize unit prices but do not assume any price difference is a contractual violation. MAP, resale-price and competition-law questions need current qualified review.
2. Compare observed cross-channel volume changes with baseline and confounders. Treat cannibalization as a hypothesis unless evidence supports substitution; do not add revenue loss and margin loss for the same units as separate economic costs.
3. Extract partner-specific service/label/ASN/appointment rules and effective dates from actual agreement. Compute on-time AND in-full by the defined unit of assessment; compare alleged deduction to the exact clause and original shipment evidence, not generic retailer thresholds.
4. Prepare negotiation objective, verified facts, business alternative if no agreement, authority limits and tradable concessions. Quantify each concession’s own cost and requested reciprocal value; mark assumptions about the buyer’s alternatives as hypotheses.
5. Build best/base/downside terms scenarios including fees, returns, payment timing and required marketing/support. Separate commercial proposal, accepted agreement and implemented catalog/operational settings.
6. Deliver meeting brief, concession ledger and disputed-deduction packet. No contract acceptance, unilateral resale-price enforcement, accusation of diversion or automatic commercial concession.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Partner/term | Observed evidence | Actual clause | Contribution/cost | Negotiation alternative | Owner decision | Follow-up |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
