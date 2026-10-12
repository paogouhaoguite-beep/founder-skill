---
name: paid-campaign-architecture
description: "Map paid campaigns to distinct goals, products, markets and economic controls, then prepare a reversible account change plan."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Paid Campaign Architecture

Use this when a DTC merchant needs a paid-media account architecture and migration plan aligning campaign roles, signal ownership, exclusions and platform-specific checks.

## Merchant inputs

Campaign goals; product/feed structure; market; account exports; budgets; conversion signal quality; creative; channel constraints and existing overlap.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Map campaigns to distinct objectives, markets, products and economic constraints. Consolidate only when those settings are compatible; smaller campaign count is not inherently better.

2. Separate acquisition, retention, brand demand and testing roles where control or economics require it. Avoid blanket claims that broad and exact keywords automatically bid against themselves.

3. Choose search, shopping/feed, social or automated formats according to intent, signal and asset readiness; show the tradeoff between control and automation.

4. Create an account map of campaign/group, goal, audience/feed, exclusions, conversion/value basis and budget owner. Diagnose overlap from actual eligibility/auction evidence, not names alone.

5. For platform-specific adaptations inspect native data: Microsoft imported settings/UET, TikTok creative permissions and event matching, Google feed and search settings. Verify current provider requirements before implementation.

6. Deliver a reversible migration plan with baseline, staged changes and duplicate-conversion safeguards. Do not move spend, delete campaigns or assume learning is complete from a fixed day count.

## Deliverable

A paid-media account architecture and migration plan aligning campaign roles, signal ownership, exclusions and platform-specific checks.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=paid-campaign-architecture&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
