---
name: indexnow-change-notification
description: "Prepare and verify an IndexNow URL-change notification, including host ownership, payload scope and acceptance status."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# IndexNow Change Notification

Use this when a DTC merchant needs an IndexNow change-notification preparation and verification plan with host validation, exact URL set and honest acceptance states.

## Merchant inputs

Owned site host; changed/added/deleted URL list; response status; canonical/indexability intent; supported search-engine endpoint; key ownership evidence.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Identify which URLs actually changed and whether they are intended for discovery, correction or removal. Do not submit staging/private URLs or treat submission as a workaround for noindex.

2. Validate host ownership and the required verification-key location against current IndexNow documentation. Keep secrets out of public reports; distinguish this mechanism from Google’s separate restricted indexing API.

3. Normalize and deduplicate URLs while preserving meaningful query semantics. Reject URLs outside the verified host or with invalid responses caused by transient outages.

4. Prepare the current documented request shape and batch limits, and retain the exact URL set and submission intent for review.

5. After an authorized request, record response status and any provider errors. An accepted notification is not proof of crawling, indexing or ranking.

6. Recheck the affected pages and later available search evidence independently; avoid repeated blind submissions when errors need correction.

7. Official IndexNow documentation reviewed on 2026-10-02 permits up to 10,000 URLs per POST. HTTP200 means received and202 means key validation pending; neither proves indexing. A key hosted in a subdirectory limits the eligible URL prefix. Recheck current requirements at https://www.indexnow.org/documentation and https://www.bing.com/indexnow/getstarted before a live request.

## Deliverable

An IndexNow change-notification preparation and verification plan with host validation, exact URL set and honest acceptance states.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=indexnow-change-notification&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
