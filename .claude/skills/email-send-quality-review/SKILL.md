---
name: email-send-quality-review
description: "Check an exact email send against audience, suppression, offer, links, personalization and deployment settings."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email Send Quality Review

Use this when a DTC merchant needs an email pre-send acceptance report binding copy, segment, suppression, rendering and destination evidence to one campaign version.

## Merchant inputs

Final copy/HTML; segment definition and suppression snapshot; approved offer; destination; schedule/time zone; authentication/placement evidence; sender identity.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Bind the check to one creative version, audience definition, time and destination. A change in offer or segment invalidates only the affected completed checks.

2. Verify subject/preheader/body consistency, accurate price/stock/conditions and a working CTA. Remove misleading reply prefixes or fabricated urgency.

3. Reconcile recipient eligibility, suppression and topic/frequency permissions from evidence. A segment count alone is not proof of permission.

4. Check personalization fallbacks, accessible copy, unsubscribe route, plain text and available render tests. Keep predicted rendering separate from observed inbox tests.

5. Review authentication and recent delivery/complaint evidence for the sending domain without treating keyword scans or a composite score as deliverability guarantees.

6. Return ready-for-approval, revisions-needed or unresolved with concrete blockers. A ready artifact is not a sent campaign; use actual provider receipts for execution status.

## Deliverable

An email pre-send acceptance report binding copy, segment, suppression, rendering and destination evidence to one campaign version.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-send-quality-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
