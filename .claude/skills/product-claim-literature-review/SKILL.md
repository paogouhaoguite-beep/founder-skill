---
name: product-claim-literature-review
description: "Review research relevant to a proposed product claim, separating study quality, applicability, uncertainty and commercial wording."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Product Claim Literature Review

Use this when a DTC merchant needs a source-linked literature evidence map with study extraction rows, exact claim applicability, conflicting findings, search log and a bounded internal recommendation.

## Merchant inputs

Specific product claim/question, ingredient/material/design and use conditions, target population, outcomes and safety relevance, date window, supplied papers or accessible research sources, and desired internal decision.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Translate the proposed claim into population, intervention/exposure, comparator, outcome and conditions. Separate efficacy, mechanism, durability and safety questions; do not imply evidence for an ingredient automatically validates the finished product.

2. Build a query ledger using synonyms and subquestions; search relevant primary literature and reviews, including conflicting and null findings. Use supplied full texts offline; distinguish abstract-only evidence and inaccessible papers. Record search date, database and inclusion criteria.

3. Deduplicate by DOI or title/authors/year, link preprints to later versions and label corrections/retractions when verified. Citation count and journal prestige are discovery aids, not automatic quality weights.

4. Extract study design, sample, comparator, dose/material specification, use conditions, endpoint/timepoint, effect size and uncertainty, funding and limitations. Preserve denominators and distinguish statistical evidence from practical importance; do not pool incompatible endpoints.

5. Compare evidence by applicability to the exact commercial product and customer. Mechanistic, animal, laboratory and human outcomes must remain separate. Explain contradictions by methods/population before calling them a consensus.

6. Return a claim-to-evidence matrix, reading order, search coverage and unresolved gaps. Draft only a bounded internal conclusion; regulated claims need applicable current authoritative requirements and qualified review before use. Do not fabricate citations or declare a systematic review unless the actual protocol and coverage support it.

## Deliverable

A source-linked literature evidence map with study extraction rows, exact claim applicability, conflicting findings, search log and a bounded internal recommendation.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=product-claim-literature-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
