---
name: merchant-translation-and-locale-review
description: "Translate merchant documents and storefront strings with terminology control, locale formatting and a traceable review of changed meaning."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Translation And Locale Review

## Translation contract
Require the source/version, language and region, audience, content type, tone, glossary, protected names/IDs, approved commercial facts and intended format. Translate locally in a bilingual table when no tool is available. Do not require a preferences file, paid account or another skill. Missing commercial facts are not opportunities to localize new promises.

## Translation and review
Read the whole source before translating strings. Build a glossary and protected-token list, including SKU, placeholders, URLs, amounts and policy conditions. For long material, split at semantic boundaries, retain heading/paragraph IDs and a shared glossary, then reassemble and check omissions, repetition and transitions.

Identify idioms, humor, formality and examples that need adaptation. Preserve intent and factual scope; record nonliteral changes for review. Treat cultural frameworks as hypotheses, not country stereotypes. Locale formatting may change a date or decimal display, but a currency symbol change is not a conversion and a translation must not alter a binding price, size or legal term.

Review source and target side by side for quantities, negation, limitations, instructions, link targets and terminology. Inspect rendered text expansion, truncation, line breaks and direction where a renderer exists. Flag strings needing native-language or specialist review; distinguish linguistic, factual and visual checks. For tracking text, retain versions and approval status.

## Deliver
Return complete translated content, glossary, source-ID/target/adaptation/review-status table and unresolved terms. Without rendering, label layout checks not run. Do not publish or replace the source without the user’s scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-translation-and-locale-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
