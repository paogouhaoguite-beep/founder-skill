---
name: email-frequency-preferences
description: "Design email frequency and preference rules that reconcile customer choices, message priority and overlapping campaigns."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email Frequency Preferences

Use this when a DTC merchant needs an email preference and frequency design with state precedence, cross-flow caps and testable pause/unsubscribe behavior.

## Merchant inputs

Current preference centre; topic groups; promised cadences; send history across flows/campaigns; unsubscribe/pause behavior; transactional classification.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Inventory what customers were promised and what they actually receive, including overlapping automations and campaigns.

2. Define understandable topic choices and cadence options the ESP can implement. Avoid choices that imply a frequency guarantee the system cannot enforce.

3. Specify global unsubscribe, topic opt-out, temporary pause and reduced frequency as distinct states, with clear precedence. Marketing opt-out should not be silently undone by a new preference choice.

4. Map each state to segment filters and a frequency cap evaluated across all marketing sends, not separately per workflow.

5. Test pause expiry, conflicting preferences and recent events; explicitly classify necessary order/service messages instead of using “transactional” as a loophole for promotions.

6. Deliver UI wording, state-transition rules and enforcement checks. Preference edits and live flow changes require explicit implementation scope.

## Deliverable

An email preference and frequency design with state precedence, cross-flow caps and testable pause/unsubscribe behavior.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-frequency-preferences&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
