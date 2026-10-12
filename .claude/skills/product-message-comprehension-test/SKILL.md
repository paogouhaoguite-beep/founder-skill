---
name: product-message-comprehension-test
description: "Design a shopper comprehension or recall test with fixed stimuli, neutral prompts and precommitted interpretation rules."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Product Message Comprehension Test

Use this when a DTC merchant needs a message-test protocol with exact stimulus, recruit criteria, neutral questions, scoring rubric, observation fields and a precommitted revise/continue rule.

## Merchant inputs

Exact approved message variants and version, product facts, target shopper cohort, decision to inform, recruitment constraints, chosen comprehension/recall/relevance outcome and merchant-defined decision criterion.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Freeze the candidate text and stimulus format before designing the test; record version/hash or exact immutable copy. Unsupported claims in a stimulus require correction or an explicit block before showing them to participants.

2. Choose unaided comprehension for meaning, timed first impression for recall, or a relevance/differentiation panel for perceived fit. A preference response is not a purchase conversion; select the protocol that answers the decision.

3. Specify recruitment by real shopping situation, eligibility/exclusions, sample rationale, assignment and presentation order. If multiple variants are shown to the same person, counterbalance order and retain paired observations; do not use an independent-groups test on paired choices.

4. Write neutral prompts: “What do you think this product does?”, “Who is it for?”, “What, if anything, was unclear?” Define a correct restatement rubric from actual product facts before seeing results. Keep moderator hints out of unaided scores.

5. Precommit outcome denominator, missing/invalid response handling, evaluation rule and revise/stop action. Merchant chosen thresholds are decision rules, not universal benchmarks or proof of market fit. Changed text, cohort or protocol starts a new test version.

6. Deliver field-ready protocol, stimulus pack, coding rubric and result table. When counts are later supplied, report n/N and uncertainty with the appropriate design; small purposive panels reveal confusion but do not establish market prevalence. Recruiting or running a panel requires separate scope.

## Deliverable

A message-test protocol with exact stimulus, recruit criteria, neutral questions, scoring rubric, observation fields and a precommitted revise/continue rule.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=product-message-comprehension-test&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
