---
name: product-prior-art-evidence-map
description: "Map product features to patent and technical documents for qualified review, preserving family, claim, date and status distinctions."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Product Prior Art Evidence Map

Use this when a DTC merchant needs a patent-family and feature-to-claim evidence map with identifiers, dates, jurisdictions, source passages, status verification and questions for qualified counsel.

## Merchant inputs

Technical product features/drawings, invention or sourcing question, jurisdictions and date of interest, known patent/publication identifiers, and any existing qualified legal advice.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Break the physical product into technical features and mechanisms. Define the search purpose: landscape/prior-art discovery versus collecting documents for freedom-to-operate counsel. Do not convert a search result into a legal clearance verdict.

2. Build keyword/synonym and classification queries using verified CPC/IPC entries. Search relevant patent registers and non-patent technical literature, recording query, date and database; supplied documents support an offline partial map.

3. Resolve publication numbers, applicants/inventors and patent families. Keep priority, filing, publication and grant dates distinct; deduplicate family variants while preserving jurisdiction-specific claim sets and legal status evidence.

4. Read the relevant claims and supporting description/drawings. Map each product feature to exact claim passage or no identified match. Independent claims are not always limited to claim1, and a dependent claim adds limitations rather than automatically proving an inventive step.

5. Record jurisdiction, verified status and status-as-of date from authoritative records when available. Application, granted, expired or abandoned labels may differ within a family; unknown status stays unknown. Do not infer enforceability or a date-specific novelty conclusion from title similarity.

6. Deliver a ranked document/feature evidence map and search gaps for qualified review. Explain priority by technical relevance and evidence completeness, not an invented infringement probability. The output supports investigation; it does not establish novelty, validity, patentability or freedom to operate.

## Deliverable

A patent-family and feature-to-claim evidence map with identifiers, dates, jurisdictions, source passages, status verification and questions for qualified counsel.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=product-prior-art-evidence-map&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
