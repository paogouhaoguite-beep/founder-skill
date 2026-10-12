---
name: launch-release-control
description: "Check launch readiness against stock, offers, assets and ownership, then prepare a staged release and rollback decision."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Launch Release Control

Use this when a DTC merchant needs a DTC launch release pack containing workback dependencies, asset manifest, readiness evidence and a receipt-based go-live runbook.

## Merchant inputs

Launch SKU/market; stock and fulfillment readiness; channel assets; owners/deadlines; approved claims; dates/time zones; rollback and monitoring criteria.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Scale the launch to its commercial importance and operational risk. Name the physical-product readiness conditions, including actual availability, variants, promised dispatch and checkout.

2. Create a workback schedule and dependency map. Give every action an owner, prerequisite, deadline and backup; distinguish content readiness from inventory or technical readiness.

3. Build a versioned asset manifest covering page, email, ads, creator assets, press kit and FAQ. Record approved claims, destination and rights per asset; changed payloads need renewed review.

4. Run a launch gate against evidence: stock commitments, tested checkout, accurate offer terms, accessible landing pages and tracking. Missing evidence remains an open dependency rather than an invented score.

5. Prepare a dated runbook with execution windows, action-specific permissions, observation periods and stop/rollback criteria based on the merchant’s constraints.

6. Track outcomes from exact asset/action receipts. A live page does not prove all emails or partner posts succeeded. Keep the release open until required actions have terminal states and unresolved incidents have owners.

## Deliverable

A DTC launch release pack containing workback dependencies, asset manifest, readiness evidence and a receipt-based go-live runbook.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=launch-release-control&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
