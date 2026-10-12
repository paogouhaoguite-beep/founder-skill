---
name: ad-placement-review
description: "Assess ad placements using comparable spend, outcomes and context, then propose scoped exclusions or controlled tests."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Ad Placement Review

Use this when a DTC merchant needs an evidence-based placement exclusion queue separating suitability violations, uncertain efficiency and observed spend loss.

## Merchant inputs

Placement/site/app report; spend and conversion lag; brand suitability policy; market; destination; merchant risk tolerance and campaign goal.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Normalize placements, network, date and spend so aliases do not split one inventory source. Preserve unavailable placement coverage.

2. Separate suitability concerns from efficiency concerns. A harmful placement may need action even with conversions; zero short-window conversions do not alone prove waste.

3. Inspect representative placements and record the actual relevance or safety evidence. Avoid blacklisting from a vague domain name or a third-party toxicity score alone.

4. Evaluate performance only after the declared attribution lag and minimum evidence needed for the decision. State the merchant-selected loss cap rather than a universal zero-conversion rule.

5. Propose exact exclusions with scope, reason, expected reach tradeoff and reversible test or review date. Do not expand one bad placement into an unsupported network-wide conclusion.

6. Return an exclusion review queue and unresolved rows; actual account edits require scoped authorization and readback.

## Deliverable

An evidence-based placement exclusion queue separating suitability violations, uncertain efficiency and observed spend loss.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=ad-placement-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
