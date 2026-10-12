---
name: social-preview-metadata
description: "Inspect and draft social link-preview metadata, images and fallback behavior for exact storefront URLs."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Social Preview Metadata

Use this when a DTC merchant needs a social share-preview metadata fix plan with resolved tags, image accessibility and cache-aware verification.

## Merchant inputs

Share URL; rendered HTML; approved title/description; brand-safe image; canonical URL; target sharing platforms and actual preview tools.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Inspect the resolved URL and initial HTML for Open Graph and relevant card metadata; note redirects and authentication barriers.

2. Map title, description, canonical share URL, image and image alt text to the actual page and offer. Do not let previews promise a price absent from the destination.

3. Check absolute HTTPS image URLs, access, dimensions and safe cropping against current platform documentation rather than a universal crop assumption.

4. Handle duplicate tags and framework overrides explicitly; document the final resolved values instead of editing a tag that is later replaced.

5. Use actual platform preview/debugger evidence where available. Distinguish source markup from cached preview output and plan cache refresh/recheck.

6. Deliver exact metadata changes and per-platform observed results. Do not claim a corrected image appeared everywhere before cache/readback verification.

## Deliverable

A social share-preview metadata fix plan with resolved tags, image accessibility and cache-aware verification.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=social-preview-metadata&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
