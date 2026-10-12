---
name: competitor-ad-evidence
description: "Collect and classify competitor ad evidence without inferring profitability or sales from ad-library visibility."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Competitor Ad Evidence

Use this when a DTC merchant needs a competitor ad evidence matrix with observed creative patterns, limitations and original merchant test hypotheses.

## Merchant inputs

Competitor list; dated public ad-library observations; visible creative; landing pages; market and objective; explicit partnership evidence.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Capture each observable ad with date, market, platform, format and source. Ad presence does not reveal its spend, profitability or exact targeting.

2. Code hooks, product claims, proof, offers, visual demonstrations and CTA separately. For video, preserve timestamped observations when media is available.

3. Record destination and product/offer continuity; distinguish what the ad says from whether the underlying claim is independently supported.

4. Identify creator partnerships only from explicit dated evidence. Do not infer exclusivity, payment or partnership terms from a tagged post alone.

5. Compare patterns and gaps across an appropriately scoped sample. Long run time is an observation, not proof of winning performance.

6. Translate findings into original test hypotheses for the merchant, each tied to its own product evidence. Do not reproduce a rival’s creative or invent benchmark numbers.

## Deliverable

A competitor ad evidence matrix with observed creative patterns, limitations and original merchant test hypotheses.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=competitor-ad-evidence&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
