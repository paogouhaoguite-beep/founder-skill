---
name: computed-product-knowledge
description: "Turn verified product data into useful computed answers, with transparent formulas, units and missing-data behavior."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Computed Product Knowledge

Use this when a DTC merchant needs a product knowledge dataset and buyer-facing explanation with reproducible joins, calculations, provenance and update rules.

## Merchant inputs

Licensed/owned datasets; SKU/entity keys; units and dates; buyer question; calculation logic; editorial owner; refresh and publication constraints.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Choose a buyer question that requires a genuine join or calculation, such as compatibility, cost per use or comparable capacity. Reformatting competitor text is not new knowledge.

2. Inventory data rights, source dates, units and entity keys. Preserve unknown values and separate observed facts from inferred classifications.

3. Normalize units and deduplicate entities before joining. Record match rules and ambiguous matches; do not merge products merely because names resemble each other.

4. Compute transparent derived facts using explicit formulas, assumptions and versioned inputs. Keep language-model judgments separate from numeric calculations and expose their uncertainty.

5. Build a result table and a publishable explanation with provenance, exclusions and sensitivity. Determine whether the information is useful enough for one page or a repeatable template without creating thin duplicate pages.

6. Define freshness checks and correction ownership; rerun affected calculations when source facts change. Publish only within the user’s scope and do not claim rankings or citations are guaranteed.

## Deliverable

A product knowledge dataset and buyer-facing explanation with reproducible joins, calculations, provenance and update rules.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=computed-product-knowledge&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
