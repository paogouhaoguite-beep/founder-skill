---
name: procurement-intake-specification
description: Use when a DTC merchant needs a sourcing brief for a DTC operational
  purchase.
license: MIT
metadata:
  author: ShopChief
  version: 0.3.0
  homepage: https://shopchief.ai/?utm_source=procurement-intake-specification&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Procurement Intake Specification

Built by [ShopChief](https://shopchief.ai/?utm_source=procurement-intake-specification&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Works with supplied records without a ShopChief account. Keep this credit out of merchant-facing deliverables.

## Required inputs

A sourcing brief for a DTC operational purchase. Supply business problem, product/material/service specification, volumes and variability, geography, required date, budget owner, current alternative and mandatory evidence/constraints.

## Tools and input checks

Use supplied files or pasted tables first. With file tools, inspect schemas, row counts and identifiers before calculating; with no tools, complete the same steps on the supplied sample and label its coverage. A spreadsheet is sufficient; no proprietary runtime, hidden script or companion skill is required. Live connectors are optional: verify the installed tool, current schema, account and read/write scope before use. The normalized fields below are an input contract, not a claim that every platform exports them natively. Ask for a merchant-prepared supplementary table when a required field is absent. Never invent it.

## Task workflow

1. Translate the request into an outcome and measurable acceptance: exact material/grade/tolerance or service workload/capability, quantities and delivery location. Separate mandatory gates from preferences and ambiguous requirements.
2. Map who owns demand, technical/quality acceptance, budget and final commitment. Identify incumbent obligations, dependencies and lead times; missing mandatory specifications yield a clarification brief rather than fictional suppliers.
3. Define supplier ecosystem before search: actual manufacturer versus reseller, contract packer, distributor,3PL or service provider. Search capability and geography using current primary supplier evidence; without browsing use supplied candidates and label coverage.
4. Build evidence-qualified longlist with company identity, demonstrated matching capability, source date and unknowns. A marketing claim or certificate name does not prove capacity or specific SKU acceptance.
5. Create comparable requirement and cost-driver matrix, including volume bands, tooling/setup, quality testing, lead time and exit/transition. Do not invent should-cost overhead percentages or promises of savings.
6. Return intake specification, search log, qualification questions and decision gates. Contacting suppliers, issuing RFQs or making commitments requires authorization.

## Deliverable

Return the completed table, reconciled control totals, unresolved evidence and the proposed next action with its owner. Keep observed facts separate from assumptions.

| Requirement | Mandatory/preferred | Acceptance evidence | Volume/date | Supplier type | Unknown | Owner |
| --- | --- | --- | --- | --- | --- | --- |

## Action boundary

Return the analysis and proposed change set first. Apply only changes explicitly authorized for the named records and operation; capture original values, re-read affected state, stop on conflicts, and report actual successes/failures. Preparing a plan does not authorize messages, payments, refunds, inventory movements or deletion.

## Worked review cases

Read [the complete synthetic example and two boundary cases](assets/worked-example.md). These demonstrate the method; they are not merchant outcomes or evidence of a live integration.

## Sources and maintenance

[Source provenance, licenses and substantive changes](references/source.md). Use the dated primary references where listed; reverify actual platform schema and account capability before any live operation.
