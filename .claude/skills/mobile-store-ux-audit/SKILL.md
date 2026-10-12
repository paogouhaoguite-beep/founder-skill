---
name: mobile-store-ux-audit
description: "Inspect mobile shopping interactions across navigation, search, variants, cart and overlays. Use for touch, viewport and accessibility friction; lab performance metrics and product-page persuasion are separate audits."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=mobile-store-ux-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Mobile store UX audit

> By [ShopChief](https://shopchief.ai/?utm_source=mobile-store-ux-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Use an observable device context
Gather the store URL or supplied recording, target device/viewport, browser, input method, locale and representative shopping task. A browser with viewport controls supports direct inspection; screenshots support layout observations only. Record whether the evidence comes from real device, emulation or static capture.

Choose paths from buyer tasks rather than visiting every page: find a category, narrow a collection, select an available variant, add to cart and inspect delivery information. Do not place an order or submit personal data. Track viewport dimensions, zoom, scroll position, overlay state and evidence for each failure.

## Inspect interaction states
Check menu open/close/focus return, search keyboard and results, filter apply/reset, swipe galleries versus page scrolling, size/variant availability, quantity edits and cart feedback. Look for sticky bars hiding controls, consent/chat overlaps, background scroll while modal is open, clipped content at text zoom, focus loss, missing visible labels and keyboard traps. Use current accessibility guidance when assigning conformance failures; heuristics alone are not a full accessibility certification.

Separate reproducible interaction defects from aesthetic preferences and latency observations. Do not label a page failing Core Web Vitals from a slow recording; performance measurement is another scope. When a state cannot be exercised, retain it in the unverified list.

Return `task | device/state | steps | expected behavior | observed evidence | impact | fix | retest`, plus annotated captures if available. Prioritize inability to complete a task, then avoidable errors and comprehension friction. If task completion is measured, provide successful attempts / observed attempts with participant/task definitions; a single expert walkthrough is not a conversion-rate study.

Local component changes may follow authorized implementation scope. Live theme publication or external account changes are not granted by requesting an audit.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/cro/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/cro/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
