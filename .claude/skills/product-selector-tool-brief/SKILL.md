---
name: product-selector-tool-brief
description: "Specify a product selector or calculator with decision rules, product evidence, missing-input handling and a testable prototype brief."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Product Selector Tool Brief

Use this when a DTC merchant needs a product-selector or calculator specification with traceable decision rules, no-match behavior and maintenance requirements.

## Merchant inputs

Buyer decision; product attributes; sizing/compatibility constraints; formulas or selection rules; catalogue freshness; implementation resources and success measure.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Define one useful decision the tool should support, such as size, quantity or compatible accessory. It must provide value even without a purchase.

2. Map each input to a rule and source. Separate hard compatibility constraints from preference-based ranking; unknown attributes cannot pass a hard constraint.

3. Create the smallest decision table or calculation and test representative and boundary rows before specifying UI.

4. Explain results with the inputs and tradeoffs, including no-match or insufficient-data outcomes; do not always force a product recommendation.

5. Estimate build, maintenance and data-refresh costs against plausible value scenarios, explicitly labeling assumptions instead of promising traffic.

6. Deliver a tool specification, sample results, validation cases and catalogue update contract. Do not publish or collect user data without implementation scope.

## Deliverable

A product-selector or calculator specification with traceable decision rules, no-match behavior and maintenance requirements.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=product-selector-tool-brief&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
