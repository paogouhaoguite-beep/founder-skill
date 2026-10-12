---
name: merchant-plain-language-edit
description: "Rewrite confusing merchant copy into clear customer language while preserving facts, qualifications and the intended brand voice."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Merchant Plain Language Edit

Use this when a DTC merchant needs a complete plain-language revision plus original phrase / problem / replacement / evidence or unresolved question table.

## Merchant inputs

Original draft, intended shopper and reading context, facts/terms that must survive, approved voice samples, and requested audit or rewrite mode.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Protect the source before editing

Identify exact protected regions and tokens before rewriting: verbatim quotations, attributed text, code blocks, tables, URLs, file paths, product IDs, quantities with units, dates, required disclaimers and brand spelling. Separate them from editable prose. Preserve them exactly unless the requested change specifically authorizes a correction. A suspected false claim remains a flagged issue; preserving its text does not approve it for publication.

Use owned voice samples to distinguish intentional rough edges from accidental confusion. Rewrite only the spans that need work; an informal register does not need to become corporate prose.

## Procedure

1. Identify the one decision or fact the reader needs and outline the supporting points before editing sentences. A draft without a coherent claim needs restructuring, not cosmetic synonyms.

2. Remove notes addressed to the commissioning merchant, internal production commentary and headings that only announce a finding. Keep legally or commercially necessary qualifications; do not impose a target percentage cut.

3. For every sentence identify actor, action and object. Expand noun stacks and undefined abbreviations; translate internal status into the shopper consequence and next action. Do not infer a deadline from a technical state.

4. Audit every quantified or comparative claim against supplied evidence, preserving units, dates, denominators and limitations. Flag unsupported experience or testimonials rather than manufacturing a personal anecdote.

5. Check cross-paragraph contradictions, pronoun references and misleading certainty; read aloud and preserve meaningful brand voice. Readability and stylistic preferences are not reliable AI-authorship tests.

6. Compare the before/after protected regions and token inventory. Check for removed qualifications, shifted attribution or meaning changes even when the same tokens remain. Record exact changed spans and reasons. Repair only the affected span, then recheck; an unresolved preservation mismatch blocks calling that passage complete. Do not invoke a missing verifier skill or claim a detector ran.

7. Use source-specific voice samples to identify generic rhythm and vague attribution; preserve supported personality while removing false authority. Do not imitate lived experience or use stylistic tells to declare AI authorship. Return the full clean revision, changed-span summary and preservation status, with unanswered factual questions outside publishable copy.

## Deliverable

A complete plain-language revision plus an original span / replacement / reason / evidence table and a protected-token and meaning-preservation audit. State unresolved mismatches explicitly.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=merchant-plain-language-edit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
