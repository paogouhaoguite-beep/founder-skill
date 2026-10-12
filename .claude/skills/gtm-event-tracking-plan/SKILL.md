---
name: gtm-event-tracking-plan
description: "Prepare a Google Tag Manager event implementation plan with data-layer contracts, triggers, consent states and preview checks. Use for tag deployment design; ecommerce financial definitions and attribution models are separate."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=gtm-event-tracking-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# GTM event tracking plan

> By [ShopChief](https://shopchief.ai/?utm_source=gtm-event-tracking-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Inspect ownership before adding tags
Collect container export or screenshots, platform/theme architecture, existing Google tag/pixel/app integrations, business event definitions, consent policy and environments. No GTM account is required for a plan from exports. An inaccessible container means naming and firing behavior remain proposed, not verified.

Build an inventory of tags, triggers and variables that could emit the same event. Trace who owns each business action. Prefer an explicit confirmed application data-layer event over fragile text/CSS clicks when available. Do not fire purchase on every thank-you-page view or label a form click as successful submission.

## Specify the runtime contract
For each event define the exact data-layer event name, parameter schema/type/source, readiness timing, absence behavior, consent prerequisites, trigger, variable mapping and destination. Keep environment identifiers configurable and never embed secrets or customer contact data. Specify clearing/resetting ecommerce state where necessary so prior item payloads do not leak into a later event. Do not overwrite the existing dataLayer array after the container has initialized.

Handle SPA navigation, back/forward, retries and consent transitions explicitly. Decide which duplicate path to remove only after evidence; two tags with similar names are not automatically duplicates. Use native Google tag templates for Google measurement tags rather than injecting gtag.js through custom HTML. Configure consent defaults/updates through the supported consent mechanism; do not use custom HTML to bypass consent ordering. Review actual capabilities before proposing any other custom HTML.

## Deliver the release unit
Return a tracking plan table, a synthetic data-layer example, change list against the current container, preview scenario matrix and rollback/version notes. Each scenario must state expected fires, expected non-fires and payload values. Include denied/granted consent, failed action, repeated action and reload cases relevant to the implementation.

Create a draft/workspace only within authorized scope; publication is a separate externally visible action. Validate preview network requests and downstream receipt with the merchant's intended property. A configured trigger or preview label alone does not prove reporting data is correct.

Consult [Google's data layer guide](https://developers.google.com/tag-platform/tag-manager/datalayer) for current behavior; do not assume the old configuration-tag UI matches the active container.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/analytics/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/analytics/SKILL.md); [coreyhaines31/marketingskills / skills/analytics/references/gtm-implementation.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/analytics/references/gtm-implementation.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
