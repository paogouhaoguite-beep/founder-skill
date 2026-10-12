---
name: email-dynamic-content-rules
description: "Define email content branches, customer-data requirements and safe fallbacks, then inspect each reachable variant."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email Dynamic Content Rules

Use this when a DTC merchant needs an email personalization rule set with field bindings, deterministic fallbacks and edge-case renders.

## Merchant inputs

Approved email copy; actual profile/catalog columns; data types; locale; offer eligibility; inventory; merge syntax and preview capabilities.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Map each token and conditional block to a real field, type and freshness requirement. A desired attribute absent from the export is not available personalization.

2. Define natural-language fallbacks per token, and full block fallbacks when missing data changes grammar or offer eligibility.

3. Specify predicate order and exclusive branch behavior; avoid showing mutually inconsistent discounts or product recommendations.

4. Preserve offer, consent and suppression conditions outside personalization. A name or previous purchase does not establish eligibility for a promotion.

5. Create a preview matrix for complete, missing, malformed, stale and multi-locale rows. Check rendered destination/price as well as text.

6. Deliver the field map, rule table and sample renders. Do not claim a template engine was tested unless an actual preview ran.

## Deliverable

An email personalization rule set with field bindings, deterministic fallbacks and edge-case renders.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-dynamic-content-rules&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
