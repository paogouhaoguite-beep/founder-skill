---
name: popup-signup-design
description: "Design a storefront signup popup with a truthful value exchange, audience rules, suppression and conversion measurement."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Popup Signup Design

Use this when a DTC merchant needs a storefront signup or popup specification with field justification, trigger/suppression rules and accessible error/success states.

## Merchant inputs

Capture purpose; traffic context; offer; current form and completion data; consent wording; field use; device constraints and dismissal behavior.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Define the exact signup outcome and promised value. A newsletter signup and customer-account creation have different required fields.

2. Audit each field against an actual use and remove unnecessary friction; separate account security requirements from marketing data collection.

3. Specify display trigger, eligible audience, dismissal persistence and suppression for existing subscribers. Use merchant context rather than a universal pop-up delay.

4. Write concise headline, benefit, field labels, CTA and consent/disclosure copy without prechecked permission or misleading close controls.

5. Check keyboard focus, visible dismissal, mobile viewport, validation errors and success/duplicate states. Do not cover essential checkout controls or trap a user.

6. Define a test measuring eligible exposure → form starts → successful signups plus conversion/complaint guardrails. A higher signup rate can still harm purchasing.

## Deliverable

A storefront signup or popup specification with field justification, trigger/suppression rules and accessible error/success states.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=popup-signup-design&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
