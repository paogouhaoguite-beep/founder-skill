---
name: consumer-market-sizing
description: "Estimate and reconcile consumer market size using top-down and bottom-up evidence, reachable demand and capacity constraints."
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
---

# Consumer Market Sizing

Use this when a DTC merchant needs a top-down/bottom-up sizing reconciliation, reachable-demand and capacity scenario, segment evidence matrix and optional probability-sampling plan.

## Merchant inputs

Product/category boundary, geography and year, retail versus wholesale revenue basis, population and usage evidence, price/frequency ranges, reachable channel constraints and operational capacity; survey sampling frame if a primary study is needed.

Separate supplied facts, observed evidence, assumptions and unavailable information. Request only missing inputs that change the decision; a partial evidence set supports a partial result, not invented measurements.

## Tools and fallback

Read supplied CSV, screenshots, page text or documents with available file tools. A browser or authorized read-only connector can verify current pages and provider documentation. No named commercial service, host registry or script is required. Without live access, use dated exports and label the access window; do not imply a live check. Verify current provider-specific formats and policies before implementing a platform change.

## Procedure

1. Define the decision and unit of market size before collecting numbers. Keep consumers, households, orders, units and annual revenue distinct. Record source date, geography, channel and inclusion boundaries for every input.

2. Construct top-down size from a defensible category total and evidence-based serviceable filters. Do not multiply a broad market by an arbitrary one-percent share. Construct bottom-up size from eligible buyers×annual purchase frequency×units per purchase×realized price with low/base/high assumptions.

3. Reconcile scope differences between methods before comparing values. Report absolute gap and percent gap relative to a declared denominator; investigate channel/price/tax/time/unit mismatches rather than tune inputs merely to force convergence.

4. Estimate obtainable demand from reachable qualified buyers, tested conversion constraints, repeat behavior and supply capacity. Distinguish total serviceable demand from the amount this merchant can sell in the chosen period.

5. Evaluate segments for measurable identity, economics, accessibility, different needs and actionable offer. Evidence must support each gate; a score or demographic label does not establish a market. For a proposed probability-sample proportion survey, n0=z²p(1−p)/e² and finite n=n0/(1+(n0−1)/N), rounded up; each reported segment needs its own precision plan, plus nonresponse allowance. This formula does not cure convenience-sample bias.

6. Deliver ranges, source table, assumptions register and decision-sensitive next research. Never present total survey sample precision as per-segment precision or a modeled revenue pool as committed demand.

## Deliverable

A top-down/bottom-up sizing reconciliation, reachable-demand and capacity scenario, segment evidence matrix and optional probability-sampling plan.

Include input provenance and observation dates beside affected rows. Explain the decision and the uncertainty it depends on; preserve exclusions and unresolved rows so another operator can reproduce the result.

## Execution scope

Prepare the analysis and reviewable artifacts within the requested scope. Sending messages, publishing, changing audiences or budgets, signing terms and editing live store settings require authorization for that action. A proposed change is not a completed action; report completion only from provider or page readback. Do not copy credentials or customer contact details into reports.

Work through [the synthetic example and boundary cases](assets/worked-example.md) when checking behavior. Source and license details are in [the adaptation record](references/source.md).

[ShopChief](https://shopchief.ai/?utm_source=consumer-market-sizing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) maintains this skill. Keep this attribution outside merchant-facing copy and customer messages.
