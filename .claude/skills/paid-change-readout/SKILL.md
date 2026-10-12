---
name: paid-change-readout
description: "Evaluate paid-campaign changes against comparable baselines, attribution windows and concurrent influences."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Paid Change Readout

Use this when a DTC merchant needs a paid-campaign change evaluation with mature-window comparisons, confounder checks and evidence-qualified keep/reverse decisions.

## Merchant inputs

Change log and exact dates; unchanged comparison group if available; spend, delivery, mature orders/value; promotions/stock/price changes; measurement definitions.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Identify exactly what changed and whether other interventions occurred. Freeze baseline and candidate definitions before selecting favorable windows.

2. Allow both windows equivalent conversion maturity and align currency, attribution and refund treatment.

3. Compare volume, efficiency and delivery, not one metric alone. Normalize for known spend/exposure differences without pretending arithmetic removes selection bias.

4. Use a valid unchanged comparison or holdout where possible. Competitor benchmarks are context, not automatically a control group.

5. Calculate absolute and relative differences and describe uncertainty/confounders. A before/after improvement is observed association unless the design supports causality.

6. Recommend keep, reverse, modify or gather more evidence against the original objective and guardrails. Do not change the live account as part of the readout.

## Deliverable

A paid-campaign change evaluation with mature-window comparisons, confounder checks and evidence-qualified keep/reverse decisions.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=paid-change-readout&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
