---
name: media-flight-planning
description: "Allocate campaign spend across dates and channels using demand timing, stock, production capacity and measurement constraints."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Media Flight Planning

Use this when a DTC merchant needs a media flight plan with channel roles, reconciled spend, reach/frequency assumptions and lead-time dependencies.

## Merchant inputs

Campaign objective; market/audience estimates; channel inventory and quotes; available budget; production lead time; reach/frequency assumptions; measurement limits.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Declare whether the flight aims at reach, repeated exposure or purchases; choose metrics and channel roles accordingly.

2. Translate supplied CPM estimates into impressions with budget/CPM × 1,000. Reach estimates require explicit frequency and duplication assumptions, not simply summed impressions.

3. Choose continuous, pulsed or concentrated flighting from the buying occasion, available stock and lead times. Reserve deadlines for channels that require advance booking.

4. Allocate by channel and phase while including production and fees. Distinguish working media from total marketing cost.

5. Compare scenarios with sensitivity to CPM, frequency and overlap. For programmatic buys specify inventory transparency, suitability and attribution limitations without claiming view-through credit is incremental.

6. Deliver a reconciled flight calendar with assumptions, caps, cancellation constraints and read dates. No booking or budget changes occur without authorization.

## Deliverable

A media flight plan with channel roles, reconciled spend, reach/frequency assumptions and lead-time dependencies.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=media-flight-planning&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
