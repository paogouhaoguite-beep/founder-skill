---
name: search-portfolio-performance
description: "Reconcile search performance across page and query groups before prioritizing changes or explaining a visibility shift."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Search Portfolio Performance

Use this when a DTC merchant needs a multi-store search performance report with non-overlapping property totals, query/page changes and evidence-qualified investigation priorities.

## Merchant inputs

Search Console exports/property list; verified store domains; equal time periods; query/page/device/country dimensions; brand query dictionary; access coverage.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Confirm property scope and overlapping domain/URL-prefix properties before totals. A domain and its prefix property can contain the same clicks.

2. Use comparable complete periods and dimensions, recording data freshness, extraction limits and missing permissions. Query-row totals can differ from site totals.

3. Calculate clicks, impressions, CTR and position changes with correct weighting; a simple average of query CTRs is not portfolio CTR.

4. Separate brand/non-brand and page types before prioritizing changes. “No row returned” may reflect privacy, filtering or truncation rather than no ranking.

5. For material declines compare impressions, CTR, query mix and observed result-page changes. Check site availability and ownership before blaming content; position correlations are hypotheses, not proof of cause.

6. Return per-store findings and a prioritized check queue with source windows. Do not claim a title fix or ranking recovery occurred from an analysis alone.

## Deliverable

A multi-store search performance report with non-overlapping property totals, query/page changes and evidence-qualified investigation priorities.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=search-portfolio-performance&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
