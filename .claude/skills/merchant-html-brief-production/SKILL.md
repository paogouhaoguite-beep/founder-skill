---
name: merchant-html-brief-production
description: "Convert approved merchant Markdown into a complete HTML reading brief or presentation deck with content-preservation and privacy checks."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Merchant HTML Brief Production

Use this when a DTC merchant needs a complete standalone HTML reading brief or presentation deck with source-to-section mapping, privacy/dependency notes and a concrete rendering/print QA checklist.

## Merchant inputs

Approved Markdown report or deck, intended audience and sharing boundary, document versus presentation mode, explicit slide boundaries if relevant, brand styles, image rights, and whether speaker notes may be distributed.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Choose a continuous document for reading and a deck for a presentation sequence; preserve explicit slide boundaries and ask about ambiguous horizontal rules. Remove the upstream minimum-line and onboarding gates. Short merchant briefs can still merit HTML when navigation or projection helps.

2. Parse headings, paragraphs, links, tables and code while retaining source order and every material fact. Escape literal text and filter dangerous URL schemes. Unsupported Markdown constructs must be converted deliberately or flagged, not silently omitted.

3. For document mode provide a clear H1, unique anchored section IDs, usable navigation and responsive readable width. Search/copy-code controls are optional, not mandatory dependencies. Include a print stylesheet that retains all content and source references.

4. For deck mode create one semantic section per slide, visible progress/sequence and previous/next links or keyboard controls with focus handling. Provide a no-script readable fallback and print one slide per page. Honor reduced motion; dense content should be split by idea instead of arbitrary source-line limits.

5. Speaker notes embedded in HTML are visible to anyone receiving the file, even if hidden in the UI. Remove confidential notes or export a separate authorized presenter copy. Prefer self-contained CSS and local assets; external fonts/scripts make the deliverable dependent and must be disclosed.

6. Compare output to the source using a section/slide count and critical facts table; inspect desktop/mobile, keyboard navigation and print when tools are available. Report tests not executed. Deliver complete files plus dependency and content-preservation notes, not just a code-generation plan.

7. Capture explicit brand colors, heading/body typography, logo rights and navigation preference into named CSS variables with documented merchant overrides. Derive background/text/link/border roles without treating color derivation as accessibility certification. Check actual foreground/background contrast and states with a trusted checker; record untested combinations. A local self-contained file needs no global configuration wizard.

## Deliverable

A complete standalone HTML reading brief or presentation deck with source-to-section mapping, privacy/dependency notes and a concrete rendering/print QA checklist.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=merchant-html-brief-production&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
