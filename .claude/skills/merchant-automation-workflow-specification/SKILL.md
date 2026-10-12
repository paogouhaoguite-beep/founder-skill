---
name: merchant-automation-workflow-specification
description: "Design a bounded merchant automation with trigger, state, idempotency, failure handling and approval boundaries before implementation."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Automation Workflow Specification

## Inputs
Collect the actual repetitive task, systems/events, example records, expected result, volume, latency needs, available tools and allowed actions. A workflow table is sufficient. Do not assume an integration exists from a product name or silently create a recurring job.

## Specify the state machine
Define trigger eligibility and exclusions, normalized input fields, stable event/business keys and authoritative state reads. Separate read/prepare/approve/execute/verify stages. For every external write, specify target, expected precondition and completion evidence.

Design idempotency around the business event, not just a timer. A retry must distinguish proven failure from unknown outcome and read state before repeating consequential operations. Include duplicate delivery, delayed/out-of-order events, missing fields, permission failures, partial batch success and rate limits.

Set human review conditions for exceptions and sensitive actions. Define logs with necessary IDs/statuses while minimizing personal data. Specify rollback or compensating actions only when actually supported. Decide alerting from actionable changes and ownership, not arbitrary constant notifications.

## Deliver
Return trigger/condition/action/state/result table, data contract, permission map, retry/dead-letter rules and synthetic acceptance cases. Label implementation untested until run in the real environment. Scheduling, connecting accounts or enabling live writes requires appropriate authorization.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-automation-workflow-specification&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
