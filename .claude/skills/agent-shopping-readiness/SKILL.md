---
name: agent-shopping-readiness
description: "Audit whether product facts and shopping steps are understandable to agents, with authoritative data and purchase authorization boundaries."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Agent Shopping Readiness

Use this when a DTC merchant needs a store agent-readiness review separating discoverable catalogue truth, deterministic variant/cart behavior and purchase authorization.

## Merchant inputs

Public product/variant pages; machine-readable catalogue; current price/stock/shipping facts; crawler policy; cart/checkout flows; authorization boundaries.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Define the intended agent task: discover products, compare variants or assist a shopper through an authorized purchase. Do not assume machine-readable product data grants checkout authority.

2. Compare visible product/variant facts with feeds and structured data, including price, currency, stock, shipping and return conditions; identify stale or conflicting representations.

3. Inspect access and rendering for relevant documented crawlers/agents, distinguishing search inclusion from training and from authenticated commerce operations.

4. Check whether variant selection, cart quantities and destination costs can be understood deterministically. Mark unsupported protocols or inaccessible steps as unavailable rather than claiming universal agent compatibility.

5. Specify buyer confirmation points for final product, total price, address/payment handling and order placement, using an existing supported integration if available.

6. Return an evidence matrix and improvement backlog. Do not create a purchase, expose credentials or publish a new checkout API as part of the audit.

## Deliverable

A store agent-readiness review separating discoverable catalogue truth, deterministic variant/cart behavior and purchase authorization.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=agent-shopping-readiness&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
