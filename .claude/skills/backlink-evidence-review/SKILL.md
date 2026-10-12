---
name: backlink-evidence-review
description: "Assess backlink opportunities and risks from actual referring pages, editorial relevance and link evidence."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Backlink Evidence Review

Use this when a DTC merchant needs a backlink evidence audit with sampled link context, broken/lost-link recovery and narrowly justified risk review.

## Merchant inputs

Backlink exports with dates, source/target URLs and link attributes; affected pages; known campaigns; manual-action evidence if any; competitor references.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Normalize source and target URLs, deduplicate repeated exports and distinguish live links, historical links and unavailable pages.

2. Inspect a meaningful sample for editorial context, topical relevance, link placement, destination correctness and rel attributes. A provider authority or toxicity metric is a proxy, not a search-engine verdict.

3. Identify lost valuable links, broken destinations, unlinked legitimate mentions and comparable competitor link intersections. Verify each suggested opportunity instead of mass-producing outreach targets.

4. Separate suspicious patterns from proven policy violations. Do not recommend disavow merely because a score is low; establish whether there is a relevant manual action or documented risk requiring specialist review.

5. Prioritize recovery and legitimate linkable assets by relevance and evidence. Draft a reasoned outreach opportunity only for an actual contextual fit; never buy manipulative links or fabricate citations.

6. Return an evidence table with review status, action, owner and limitations. Takedowns, outreach and disavow uploads are separate authorized actions.

## Deliverable

A backlink evidence audit with sampled link context, broken/lost-link recovery and narrowly justified risk review.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=backlink-evidence-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
