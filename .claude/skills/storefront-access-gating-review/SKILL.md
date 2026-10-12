---
name: storefront-access-gating-review
description: "Review account or content gates for shopper value, purchase friction, accessibility and measurable alternatives."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Storefront Access Gating Review

Use this when a DTC merchant needs a storefront access-gate review with entitlement logic, customer recovery paths and inventory-versus-permission distinctions.

## Merchant inputs

What is withheld; business reason; eligible customers; authentication/age/membership criteria; user journey; accessibility; purchase and service policies.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Identify whether the gate controls legal access, wholesale pricing, member access or a limited product drop. A growth tactic is not automatically a legitimate access requirement.

2. Map exact entitlements and the minimum verification needed; preserve public product facts and terms necessary for an informed decision where appropriate.

3. Design clear pre-gate explanation, eligibility steps, failure/help path and return to the intended product after authentication.

4. Separate inventory reservation from permission to view or purchase. A verified member is not guaranteed stock unless the system reserves it.

5. Review friction and exclusion on mobile and assistive technology, with special attention to existing eligible customers whose session expires.

6. Return a gate decision matrix and event plan. Do not remove mandatory legal controls or add deceptive scarcity to force registration.

## Deliverable

A storefront access-gate review with entitlement logic, customer recovery paths and inventory-versus-permission distinctions.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=storefront-access-gating-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
