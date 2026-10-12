---
name: dark-social-measurement
description: "Investigate unattributed sharing with tagged links, declared-source responses and bounded evidence rather than invented channel credit."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Dark Social Measurement

Use this when a DTC merchant needs a dark-social evidence brief combining direct-traffic segments, self-reports and share-link hygiene without fabricating attribution.

## Merchant inputs

Session source/landing page exports; branded-search series; social activity dates; optional self-reported acquisition answers; share-link scheme.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Inventory measurable share links and private sharing paths. Direct traffic includes typed URLs, missing referrers and other causes; it is not synonymous with dark social.

2. Specify a stable UTM taxonomy for owned share buttons and campaign links. Do not add campaign UTMs to internal navigation or assume copied address-bar URLs retain attribution.

3. Design an optional, low-friction “how did you hear about us” question and keep free text plus normalized categories; discuss form friction instead of mandating an extra field.

4. Segment direct sessions by deep landing URLs, device and time, comparing like windows. Label plausible private-sharing exposure as a hypothesis rather than assigning every session to social.

5. Compare self-reports and branded search around activity dates. Describe association, sampling bias and alternate drivers; never add self-reports to orders already counted.

6. Deliver ranges or evidence tiers where attribution is incomplete. Recommend a controlled test when a causal budget decision is needed.

## Deliverable

A dark-social evidence brief combining direct-traffic segments, self-reports and share-link hygiene without fabricating attribution.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=dark-social-measurement&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
