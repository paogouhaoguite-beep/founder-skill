---
name: search-metadata-release-check
description: "Prepare and verify a metadata release using exact URLs, proposed values, duplicate checks and post-change readback."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Search Metadata Release Check

Use this when a DTC merchant needs a release-time SEO metadata comparison with valid snapshot checks, intent-aware regressions and verification steps.

## Merchant inputs

Before/after HTML snapshots or exports; URL set; deployment changes; intended metadata edits; response status; canonical/indexing policy.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Capture response status, final URL, timestamp and page variant with each snapshot. Reject login, bot-check and error pages as substitutes for the intended content.

2. Compare title, robots directives, canonical, headings, structured data and important links at the same URL and rendering stage.

3. Separate intended editorial changes from accidental deletion or conflicting indexability. Severity depends on commercial scope and crawl impact, not a fixed percentage of title text changed.

4. Validate structured-data parseability and visible-content consistency; a removed unsupported field can be an improvement rather than a regression.

5. Identify template-wide patterns versus one-page defects and propose the smallest reversible fix. Preserve before/after evidence and the release that introduced the difference.

6. Report observed regressions, deliberate changes and unverified checks. A monitoring report is not evidence that Google recrawled or changed indexing.

## Deliverable

A release-time SEO metadata comparison with valid snapshot checks, intent-aware regressions and verification steps.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=search-metadata-release-check&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
