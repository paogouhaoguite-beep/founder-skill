---
name: bid-strategy-change-plan
description: "Plan a bidding change using conversion signal quality, economics, constraints and an explicit evaluation window."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Bid Strategy Change Plan

Use this when a DTC merchant needs a bidding-strategy change proposal grounded in mature economics with target rationale, observation window and rollback conditions.

## Merchant inputs

Current strategy/settings; mature conversion/value history; target economics; campaign role; lag; planned events; budget/volume constraints.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Validate conversion counts and values before treating the bidding baseline as meaningful. Distinguish revenue and contribution objectives.

2. Choose strategy candidates from the business objective, available signal and control needs, using current platform eligibility requirements rather than a universal conversion threshold.

3. Calculate achieved mature CPA or ROAS on compatible windows and derive a feasible starting target with the merchant’s risk tolerance. Do not promise an aspirational target the account has never supported.

4. Separate campaigns with different economics or goals before portfolio decisions; do not mix acquisition and existing-customer value assumptions silently.

5. Define a bounded change, observation window allowing conversion lag, guardrails and rollback evidence. Avoid simultaneous creative/audience changes that defeat diagnosis.

6. Return exact proposed settings, assumptions and a readout plan. Strategy changes and spend adjustments are externally consequential and need authorization.

## Deliverable

A bidding-strategy change proposal grounded in mature economics with target rationale, observation window and rollback conditions.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=bid-strategy-change-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
