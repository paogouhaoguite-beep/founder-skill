---
name: conversion-value-design
description: "Define conversion values from merchant economics and event evidence before changing bidding or measurement settings."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.3.0
---

# Conversion Value Design

Use this when a DTC merchant needs a conversion-value specification linking order economics, bidding payloads, micro-conversion proxies and refund adjustments.

## Merchant inputs

Order-level revenue, discounts, refunds, COGS, shipping/fulfillment/payment costs; conversion actions; current value payloads; currency; downstream event outcomes.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Inventory primary and secondary conversion actions and identify which represent actual purchases versus micro-events. Avoid optimizing toward every funnel event as equal value.

2. Declare one value basis: gross revenue, net revenue or contribution. State treatment of tax, discounts, refunds and variable costs; do not relabel revenue as profit.

3. Map dynamic order values to the bidding event and preserve currency and transaction identity. A constant fallback is explicit and cannot silently override actual values.

4. For non-purchase actions, estimate expected value only from compatible downstream conversion evidence and the declared value basis; avoid adding multiple proxy values for the same eventual order.

5. Define adjustment or restatement handling for returns/cancellations and data latency. Retain a reconciliation table from order truth to exported bidding value.

6. Produce a value specification and test cases; changing primary goals or uploading values is a separate authorized implementation.

## Deliverable

A conversion-value specification linking order economics, bidding payloads, micro-conversion proxies and refund adjustments.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=conversion-value-design&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
