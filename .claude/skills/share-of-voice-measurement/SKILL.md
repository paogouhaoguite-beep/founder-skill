---
name: share-of-voice-measurement
description: "Measure brand mention share within a declared source set and time window, preserving exclusions and sampling limits."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Share Of Voice Measurement

Use this when a DTC merchant needs a panel-controlled share-of-voice report with reproducible denominators, platform splits and explicit series breaks.

## Merchant inputs

Fixed competitor panel; per-brand query definitions; source/platform scope; equal observation windows; deduplicated mention counts.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Lock the brand panel, aliases, exclusions, platforms and observation windows before computing trends.

2. Count comparable relevant mentions for each brand on each platform. Preserve missing values rather than replacing them with zero.

3. Calculate brand mentions divided by all panel mentions, including the brand itself. Show numerator and denominator beside each percentage.

4. Report per-platform results first. A combined share must state its weighting and coverage; raw cross-platform addition can overweight the easiest source to collect.

5. If using sentiment-weighted share, retain unweighted share and explain coding, sample size and weights. Engagement or pageview share is a different metric, not interchangeable with mention share.

6. Mark panel, query and access changes as series breaks. Explain observed shifts without asserting market share or sales impact.

## Deliverable

A panel-controlled share-of-voice report with reproducible denominators, platform splits and explicit series breaks.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=share-of-voice-measurement&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
