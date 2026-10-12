---
name: storefront-visual-design-review
description: "Review storefront visuals against shopper tasks and approved designs, separating observed defects from preference and untested behavior."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Storefront Visual Design Review

## Scope
Collect page/version, shopper task, reference design if any, devices, actual screenshots or browser access and merchant constraints. A screenshot review is limited to visible evidence. Conversion and accessibility behavior require additional measurement/testing.

## Review passes
First inspect whether product identity, value, options, price, conditions and next action can be understood in the given task. Assess hierarchy, grouping, alignment, spacing, density and typography at the intended viewport. Compare actual implementation with approved design and note meaningful deviations, not arbitrary pixel differences.

Evaluate states and responsive variants where evidence exists. Separate content missing from the page from content merely outside the screenshot. Identify misleading affordances, weak grouping or competing emphasis as hypotheses with a task consequence. Do not mandate a fashionable palette, font or style as a universal rule.

For each issue provide screenshot/element evidence, severity based on task impact, proposed minimal fix and verification method. A screenshot cannot prove exact contrast, font metrics, load performance or keyboard operation; flag those for proper inspection. Preserve successful parts and distinguish design-spec compliance from actual user usability.

## Deliver
Return prioritized findings, annotated locations, proposed changes and a retest checklist. Do not claim the new design increased sales or deploy fixes from a review-only request.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=storefront-visual-design-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
