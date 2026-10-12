---
name: marketing-attribution-audit
description: "Reconcile store orders with advertising and analytics credit rules to explain conflicting channel reports. Use for model/window/identity differences; event implementation and automatic budget reallocation are outside this audit."
license: MIT
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=marketing-attribution-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Marketing attribution audit

> By [ShopChief](https://shopchief.ai/?utm_source=marketing-attribution-audit&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Establish what is being counted
Read order/refund ledger, platform and analytics reports, timezone/currency, conversion definitions, attribution windows, click/view rules, model, export date and reporting lag. Without row-level journey data, compare aggregate definitions and evidence gaps; do not manufacture a joined customer journey. Use redacted exports or authorized read-only connectors.

Choose a defined financial/order anchor, including treatment of cancellations, test orders, refunds, tax and shipping. Different tools may count conversion event time or interaction time; align dates before interpreting differences. Preserve platform-modeled versus observed conversions where available.

## Reconcile without pretending certainty
Build a bridge of known differences: duplicate transaction IDs, order-state exclusions, currency, refunds, lag, consent/missing identifiers, cross-device and view-through scope. Do not subtract an unexplained residual and label it fraud or overclaiming. Never sum platform-attributed conversions into total store sales.

If complete eligible touch histories exist, calculate clearly named models on that same population and lookback window. First-touch and last-touch redistribute recorded credit; neither proves causation. Unknown/direct should remain distinguishable from known direct navigation. A high direct or branded-search share does not prove upstream campaigns worked.

Triangulate with post-purchase survey evidence, acknowledging recall and respondent bias. A prospective holdout can investigate incrementality if feasible; do not present existing observational ROAS as lift. Avoid prescribing an MMM from arbitrary minimum data or asserting one model is universally correct.

## Output
Deliver `source | conversion/revenue definition | date basis | model/window | identity/consent limits | reported total`, a reconciliation bridge with confirmed versus unresolved causes, and a scoped measurement improvement plan. For CAC, state which acquisition spend and newly acquired customer cohort form numerator/denominator; for ROAS, state attributed revenue and matching spend/window. No missing spend or customer identity becomes zero.

Do not change budgets, attribution settings, tags or upload customer identifiers without the user's actual scope. Explain what remains unknowable from available exports rather than forcing an exact channel allocation.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [coreyhaines31/marketingskills / skills/attribution/SKILL.md](https://github.com/coreyhaines31/marketingskills/blob/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/skills/attribution/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE).

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
