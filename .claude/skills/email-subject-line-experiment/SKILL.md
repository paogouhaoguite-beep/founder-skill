---
name: email-subject-line-experiment
description: "Design a subject-line experiment with controlled content, eligible recipients, prespecified outcomes and valid stopping rules."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email Subject Line Experiment

Use this when a DTC merchant needs a subject/preheader test plan with truthful variants, fixed experimental conditions and uncertainty-aware readout.

## Merchant inputs

Approved email content; candidate subject/preheader pairs; segment; observed baseline; expected volume; primary metric; privacy limitations; sample/duration constraints.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Generate subjects from the actual content and offer, preserving conditions. Count characters as an observable property; screen for misleading urgency and fake reply prefixes.

2. Pair each subject with a preheader that adds useful context rather than repeating it. Treat possible truncation as a render check, not a universal character cutoff.

3. Define one changed variable, randomization unit, audience eligibility and allocation. Keep content, sender and timing comparable unless timing is the variable being tested.

4. Predeclare the primary outcome, observation window and decision rule. Opens may be distorted by privacy features; prefer meaningful click/order outcomes when the goal and sample support them.

5. Record creative versions and actual delivered counts per cell. Check allocation imbalance, suppression changes, bot clicks and overlapping sends before interpreting results.

6. Report absolute and relative differences with uncertainty; do not choose a statistical winner from a tiny early sample or automatically mail the rest of the list.

## Deliverable

A subject/preheader test plan with truthful variants, fixed experimental conditions and uncertainty-aware readout.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-subject-line-experiment&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
