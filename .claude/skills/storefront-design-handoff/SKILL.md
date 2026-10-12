---
name: storefront-design-handoff
description: "Create an implementation-ready storefront design handoff with shopper flows, responsive states, tokens and observable acceptance criteria."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Storefront Design Handoff

## Merchant contract
Collect the specific shopper task, approved wireframes/design, actual store capabilities, product/policy facts, locales, device contexts and developer destination. A text specification with annotated screenshots is sufficient. Do not select a new technology stack or invent checkout features from a visual reference.

## Flow and state design
Map entry point, shopper goal, decisions, system responses and recovery paths. Include loading, empty, error, disabled, out-of-stock and success states. Distinguish assumptions about backend behavior from confirmed contracts. Use realistic content and product variants in wireframes; mark placeholders clearly.

Define each interaction through trigger, rule, feedback and interruption/recovery behavior. For adding to cart, include pending state, duplicate clicks, stock conflict and confirmed cart update rather than only a button animation. Motion should communicate state and respect accessibility preferences, not become a required spectacle.

Specify layout by content and context: fixed/fluid dimensions, min/max behavior, wrapping, ordering, sticky elements and breakpoint rationale. Mobile adaptation may change task priority or interaction affordance, but must not silently remove essential information. Add locale expansion, RTL and keyboard/assistive-tech expectations.

List reusable color/type/spacing roles, component variants and measured values where supplied. Annotate redlines with component/state/measurement and source version; do not invent pixel precision from a scaled screenshot. Distinguish invariant identity from responsive changes.

## Acceptance and delivery
Return flow map, component/state inventory, responsive rules, tokens, copy/assets, dependencies and acceptance scenarios. Each criterion must be observable: “after a stock-conflict response, selected quantity remains and an actionable message appears,” not “feels premium.” Mark unresolved requirements and obtain actual implementation/browser evidence before calling the design implemented. No live edits are implied.

## Cross-channel continuity and resume states
For flows spanning email, storefront and support, map each handoff with the state to preserve, permitted identity context, destination and failure fallback. Specify interruption, save/resume, expiry, re-entry summary and restart behavior. Do not promise cross-device persistence without an implemented identity/state contract. For each stage, connect design rationale to observed shopper evidence or explicitly label the assumption; include task completion and error definitions for acceptance.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=storefront-design-handoff&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
