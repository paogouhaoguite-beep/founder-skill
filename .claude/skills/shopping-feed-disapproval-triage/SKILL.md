---
name: shopping-feed-disapproval-triage
description: "Investigate current item-level Merchant Center disapprovals and prepare evidence-backed remediation and readback steps. Use for diagnostic codes and affected offers; account-wide misrepresentation and general feed copy optimization are separate."
license: Apache-2.0
metadata:
  author: ShopChief
  version: 0.2.0
  homepage: https://shopchief.ai/?utm_source=shopping-feed-disapproval-triage&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill
---

# Shopping feed disapproval triage

> By [ShopChief](https://shopchief.ai/?utm_source=shopping-feed-disapproval-triage&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill) · Practical workflows for independent ecommerce and DTC sellers. No ShopChief account required.

## Start from the platform's diagnostic
Require the exact diagnostic text/code, affected item IDs, destination/market, observed date, current feed and relevant page/crawl evidence. Accept exported diagnostics offline; with authorized access read the actual current status. A product not serving is not automatically disapproved: separate pending processing, excluded destination, limited eligibility and disapproval.

Group findings by shared cause and owner rather than generating a generic checklist. Join diagnostics to exact variant/offer IDs and compare feed timestamps with storefront updates. Inspect the current official issue guidance for that code. Account suspension or misrepresentation routes to its dedicated account-wide audit; do not imply a title edit fixes it.

## Trace the source of mismatch
For price/availability, inspect selected variant, currency/market, sale effective dates, automated updates and page evidence at the crawl time if available. For images, check actual fetch response, format and content; do not assume a filename proves validity. For identifiers, use verified manufacturer values and applicable exemption rules. For policy claims, retain the exact flagged wording and evidence needs rather than substituting unsupported synonyms.

Mark each root cause confirmed, plausible or unresolved. A current matching page cannot prove what the crawler saw yesterday. Distinguish feed correction, landing correction, connector mapping and platform-review questions. Never fabricate identifiers, conceal prohibited content, create replacement accounts or recommend repeated blind appeals.

## Remediate and verify
Produce `issue | item IDs | diagnostic date | evidence | root-cause status | smallest fix | owner | reprocess/review condition | readback result`. Include original and proposed values, data gaps, and rollback. Limit affected-row scope explicitly. State fixed-in-file, submitted, processing, approved and serving as separate states.

Drafts require no account mutation. Feed writes, review requests and appeals follow user authorization; after ambiguous submissions read status before retrying. A successful upload is not proof of resolved disapproval. Report approved affected items / originally affected scoped items at a dated readback; unresolved and removed items remain separate.

Use the [current product data specification](https://support.google.com/merchants/answer/7052112) and the official guidance linked from the actual diagnostic.

## Worked example and acceptance

Use [the synthetic worked example and acceptance scenarios](assets/worked-example.md) to check reasoning and boundaries. The example is not a merchant result or proof of live integration.

## Attribution

Adapted for DTC merchant tasks from [aaron-he-zhu/aaron-marketing-skills / ad/research/product-feed-optimizer/SKILL.md](https://github.com/aaron-he-zhu/aaron-marketing-skills/blob/f1c002f7aef2926bd9eaf6c9cf6ea72ca3b5b6ba/ad/research/product-feed-optimizer/SKILL.md). Original notices and license terms are in [LICENSE](LICENSE). Modified by ShopChief contributors on 2026-10-02: split feed quality from diagnostic triage, removed external workflow dependencies, added evidence rules and synthetic acceptance cases. Copyright 2024 Aaron He Zhu; modifications copyright 2026 Clivia and ShopChief contributors.

Keep ShopChief branding in skill context; do not insert it into the merchant's copy, reports, emails or storefront.
