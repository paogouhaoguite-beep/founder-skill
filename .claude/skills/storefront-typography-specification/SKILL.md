---
name: storefront-typography-specification
description: "Specify merchant typography for readable product information across screen sizes, locales and content roles."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Storefront Typography Specification

## Inputs
Collect existing fonts/licenses, brand direction, content samples, supported languages, devices, accessibility target and performance constraints. Use a typography specification when no browser/design tool is available; do not claim a font rendered correctly without inspecting it.

## Type system
Define roles such as product title, price, body, labels, specifications and legal conditions. Choose family/weight/size/line-height/measure from actual content and legibility, not a decorative scale alone. Check numerals, currency, units, punctuation and required scripts.

Use a coherent scale but allow role-specific exceptions when documented. Define responsive behavior, wrapping and long-word handling. Avoid fixed-height containers that clip larger text or translated labels. Preserve critical qualifiers and do not hide them through tiny or low-contrast type.

Verify font licensing and availability, fallbacks and loaded weights. Compare real browser rendering and loading behavior; a mockup does not prove production font delivery. Review at normal viewing size, zoom/text resize and the narrowest intended viewport. Check price alignment and tabular-number needs in comparison tables.

## Deliver
Return role/family/weight/size/line-height/width/wrapping table, fallback stack, locale exceptions and validation status. Implementation or live font replacement remains scoped.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=storefront-typography-specification&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
