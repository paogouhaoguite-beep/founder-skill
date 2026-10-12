---
name: email-list-hygiene
description: "Review email-list provenance, suppression, engagement and reactivation options without treating opens as reliable individual intent."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Email List Hygiene

Use this when a DTC merchant needs an email list health and segment audit with reliable engagement cohorts, suppression reconciliation and reversible remediation.

## Merchant inputs

ESP export; bounce/complaint/unsubscribe events; delivery history; reliable click/purchase recency; permission provenance; suppression snapshots.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Profile available dates, permission states and engagement signals. Treat privacy-protected opens as unreliable evidence of individual interest.

2. Define engagement cohorts using merchant purchase cycles and observed clicks/orders; do not automatically use fixed 30/90/180-day cutoffs.

3. Reconcile hard bounces, complaints and opt-outs to the suppression state, checking identity consistency and duplicate profiles.

4. Compare delivery quality by source cohort and time with explicit denominators. A sudden change in acquisition source may explain deterioration better than whole-list averages.

5. Propose reversible hold or suppression actions and a separately authorized repermission plan where appropriate. Do not mass-delete contacts or assume permission from a purchase.

6. Return cohort definitions, count reconciliation, suppression discrepancies and a review schedule, preserving an audit trail without exporting personal details.

## Deliverable

An email list health and segment audit with reliable engagement cohorts, suppression reconciliation and reversible remediation.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=email-list-hygiene&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
