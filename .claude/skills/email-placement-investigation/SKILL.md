---
name: email-placement-investigation
description: "Investigate inbox placement using provider-level delivery, authentication and complaint evidence, separating clients from mailbox providers."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email Placement Investigation

Use this when a DTC merchant needs a provider-specific email placement investigation separating seed observations, delivery acceptance and unverified causal explanations.

## Merchant inputs

Per-provider seed/inbox test; exact campaign version; ESP delivery/bounce logs; domain/IP reputation exports; dates; segment and sender configuration.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Bind placement evidence to the tested message, domain, time and provider. Distinguish a seed test from the whole production audience.

2. Report inbox, spam and category placement per provider, preserving missing or inconclusive cells. SMTP accepted/delivered does not prove inbox placement.

3. Compare reputation and failure patterns with prior compatible periods; identify changes in domain, volume, acquisition source or message before proposing a cause.

4. Reconcile placement with authentication and complaint evidence. A subject keyword or a seed score alone cannot establish why a provider filtered the message.

5. Prioritize evidence-backed remediation and a small retest with one changed condition where feasible. Keep provider-specific observations separate rather than hiding them in an overall average.

6. Return a diagnosis table with observed facts, causal hypotheses, proposed checks and untested providers. Do not change DNS, warm sending volume or launch a seed send without scope.

## Deliverable

A provider-specific email placement investigation separating seed observations, delivery acceptance and unverified causal explanations.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-placement-investigation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
