---
name: storefront-microcopy-state-review
description: "Write and audit shopper-facing UI text across normal, empty, loading, error and recovery states using verified product behavior."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Storefront Microcopy State Review

## Inputs
Collect journey/screens, actual behavior and state transitions, product/policy facts, tone, locale and space constraints. Screenshots plus a state table are enough for drafting; browser testing is optional but required to verify behavior. Do not infer a refund, order submission or saved change from optimistic UI text.

## State-copy workflow
Map each control or message to what the shopper is trying to do and what the system actually knows. Write labels using the shopper’s language and actions, not internal IDs or generic “Submit” where a precise verb is possible.

For each error, state what happened, what is preserved and the next feasible action. Avoid blame, unsupported certainty and instructions the interface cannot perform. Differentiate validation errors, stock changes, payment decline, pending submission and unknown network outcome. Do not invite repeated payment submission when the first outcome is unknown.

Check consistency of product/variant terms, button labels, inline help, confirmations and links. Keep critical conditions close to the action. Ensure accessible names and visible labels agree, error text is not color-only, and translated strings preserve placeholders and meaning.

## Deliver
Return screen/state/current/proposed/evidence/recovery table and complete replacement strings, plus unresolved behavior questions. Microcopy is not a substitute for fixing a broken workflow. Do not change live copy or promise new capabilities without scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=storefront-microcopy-state-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
