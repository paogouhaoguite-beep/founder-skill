---
name: support-macro-library-design
description: "Create a maintainable library of shopper support drafts with scenario eligibility, verified data tokens and policy ownership."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Support Macro Library Design

## Inputs and tools
Collect a dated ticket sample, reason taxonomy, policies, brand tone, channels and helpdesk import constraints. A Markdown or CSV library is the local fallback. Do not assume a universal sample window, word limit or number of buckets.

## Build and verify
Group recurring scenarios by the action an agent must take, distinguishing policy branches such as eligible return, missing order identity and carrier investigation. Include low-frequency but important scenarios when they merit controlled wording. For each macro define when to use it, when not to use it, required evidence and escalation conditions.

Write acknowledgment → verified answer or action → next step. Use consistent tokens such as [[order_id]] and maintain a token dictionary with authoritative source and required/optional status. Optional branches must have complete alternative sentences; do not leave broken grammar when values are missing. A token is a data requirement, not permission to guess.

Render examples with realistic synthetic data and test missing fields, changed policy and unauthorized remedies. Block use when a required fact or policy version is unavailable. Never include “refunded” unless transaction status proves it. Avoid universal promises, legal conclusions and variable values embedded in boilerplate.

## Deliver and maintain
Provide taxonomy, macro ID/title/version, usage conditions, text, token dictionary, owner and review triggers. Usage and satisfaction can identify review candidates but do not establish that a macro caused satisfaction changes; preserve sample sizes and case mix. Policy changes trigger review regardless of usage. Produce an import preview only; publishing macros or sending messages requires scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=support-macro-library-design&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
