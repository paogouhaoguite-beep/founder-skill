---
name: paid-audience-seed-review
description: "Review customer audience seeds for provenance, consent, match suitability, exclusions and useful campaign segmentation."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Paid Audience Seed Review

Use this when a DTC merchant needs a paid-audience seed and exclusion specification with reproducible predicates, overlap counts and upload prerequisites.

## Merchant inputs

Customer/event export with lawful-use status; value and recency fields; platform audience purpose; suppression rules; minimum data-sharing scope.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Inventory available fields and distinguish a usable source field from an inferred characteristic. Exclude unnecessary personal or sensitive information.

2. Define seed membership with explicit predicates tied to supplied columns and dates, such as repeat purchasers with positive net order contribution.

3. Build exclusions for opt-outs, recent purchasers where inappropriate, returns and conflicting campaigns according to the merchant’s objective.

4. Separate a seed list definition from a platform-generated lookalike audience; the latter cannot be reconstructed from customer rows alone.

5. Evaluate each predicate on edge cases, including missing dates/value and overlapping memberships. State whether unknown values are excluded or require review.

6. Return counts, definitions, overlap and data-minimization requirements. Hashing identifiers does not by itself establish consent or permission to upload.

## Deliverable

A paid-audience seed and exclusion specification with reproducible predicates, overlap counts and upload prerequisites.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=paid-audience-seed-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
