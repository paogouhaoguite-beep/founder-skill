---
name: ai-referral-measurement
description: "Measure observable AI referral traffic and landing outcomes while separating referrers, citations and incremental sales."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# AI Referral Measurement

Use this when a DTC merchant needs an AI-referral analytics report separating observed assistant sessions, downstream events and unattributable traffic.

## Merchant inputs

Session source/referrer data; date range; known assistant domains; event/order definitions; consent coverage; current channel classification.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Inventory observed referring domains and campaign tags, distinguishing assistant referrals from search, browser wrappers and unrelated same-name hosts.

2. Define a maintainable classification table with exact domain matching and dated changes; verify uncertain domains rather than broad substring matching.

3. Calculate sessions, engaged sessions and confirmed store outcomes using the same window and definitions. Keep multiple touches per order visible.

4. Explain missing referrers and private-app transitions: unclassified/direct traffic cannot be automatically assigned to AI.

5. Separate referral traffic from AI answer mentions, citations and search impressions. An assistant mention with no click is absent from session analytics.

6. Return a source-level report, classification exceptions and validation plan. Do not claim AI market share or incrementality from the observed referral subset.

## Deliverable

An AI-referral analytics report separating observed assistant sessions, downstream events and unattributable traffic.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=ai-referral-measurement&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
