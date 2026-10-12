---
name: social-crisis-runbook
description: "Prepare an evidence-based social incident response, including holding statements, escalation roles and update conditions."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Social Crisis Runbook

Use this when a DTC merchant needs a social incident response runbook with severity rationale, pause inventory, holding statements, update owners and restart checks.

## Merchant inputs

Incident facts and timestamps; channel activity; scheduled campaigns; responsible owners; relevant product/support evidence; approved response rules.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Separate verified facts, allegations and unavailable details. Identify who can investigate product safety, order impact, account compromise or legal issues.

2. Define merchant-specific severity levels using impact and uncertainty; volume is context, not an automatic severity multiplier.

3. Identify scheduled content and paid amplification that could conflict with the incident. Prepare exact pause actions for authorized owners and track their readback.

4. Draft a holding statement naming what is known, what is being checked, a contact route and the next update time. Do not speculate or promise a fix that is not approved.

5. Build an incident log with each statement version, approver, publication evidence and customer-support handoff. Treat a removal or rollback as a new action, preserving history.

6. Stand down only after incident owners clear the relevant risks and each paused surface has a deliberate restart decision. Review timing, missed signals and response accuracy against the incident timeline.

## Deliverable

A social incident response runbook with severity rationale, pause inventory, holding statements, update owners and restart checks.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=social-crisis-runbook&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
