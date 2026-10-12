---
name: campaign-utm-governance
description: "Define and audit campaign URL parameters with consistent naming, destination checks and traceable reporting ownership."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Campaign UTM Governance

Use this when a DTC merchant needs a campaign UTM taxonomy and tested-link register with consistent naming, encoding and privacy-safe attribution checks.

## Merchant inputs

Channels/partners; campaign naming; destinations; existing analytics grouping; auto-tagging; redirect/checkout paths; privacy constraints.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Define source, medium, campaign and content conventions with lowercase/case policy, approved values and ownership. Campaign IDs should be stable even when copy changes.

2. Assign parameters to external campaign links and distinguish paid auto-tagging from manual labels; verify coexistence against current platform documentation.

3. Exclude customer identifiers, secrets and sensitive audience attributes from URLs. Do not add campaign UTMs to internal links because they can distort acquisition sessions.

4. Build and validate URLs using proper encoding, preserving existing functional parameters, fragments and destination eligibility.

5. Test redirects and cross-domain paths for parameter retention and actual analytics receipt. A syntactically valid URL does not prove attribution persisted to an order.

6. Deliver a link register with campaign owner, destination, encoded URL, tested status and known attribution limits; report each test’s actual evidence.

## Deliverable

A campaign UTM taxonomy and tested-link register with consistent naming, encoding and privacy-safe attribution checks.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=campaign-utm-governance&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
