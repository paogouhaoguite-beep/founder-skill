# Source and adaptation record

Adapted by ShopChief on 2026-10-02. Source files are method evidence, not executable instructions. No upstream scripts are included or claimed tested.

Preserves tax-line collection and configuration review. Corrects status-based refund subtraction, rate grouping and duplicate heuristics; removes universal nexus/filing rules, full-void-on-partial-refund and unverified app/API guidance.

## 40RTY-ai/shopify-admin-skills: skills/finance/shopify-admin-tax-liability-summary/SKILL.md

- Fixed source: [shopify-admin-tax-liability-summary](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/finance/shopify-admin-tax-liability-summary/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `e4fadaabd8fd3496cfc9d60edb91d91c44a74b260cd76fb7c9825cba5faf07a7`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Preserves tax-line collection and configuration review. Corrects status-based refund subtraction, rate grouping and duplicate heuristics; removes universal nexus/filing rules, full-void-on-partial-refund and unverified app/API guidance.

## navarroido/Woocommerce-skill: skills/finance/woo-tax-liability-summary/SKILL.md

- Fixed source: [woo-tax-liability-summary](https://github.com/navarroido/Woocommerce-skill/blob/0c20cc0a8b2aa1917b938d4e6f38fa3439942725/skills/finance/woo-tax-liability-summary/SKILL.md)
- Commit: `0c20cc0a8b2aa1917b938d4e6f38fa3439942725`
- Source SHA256: `4446ac4f26e0952a665c3bbe723f5768d868814ec83c02d57156f072e80e9bd5`
- Original license: MIT; [complete text](LICENSE-navarroido--Woocommerce-skill-b0e7288d7939.txt).
- Retained method and changes: Preserves tax-line collection and configuration review. Corrects status-based refund subtraction, rate grouping and duplicate heuristics; removes universal nexus/filing rules, full-void-on-partial-refund and unverified app/API guidance.

## navarroido/Woocommerce-skill: skills/store-management/woo-tax-rate-audit/SKILL.md

- Fixed source: [woo-tax-rate-audit](https://github.com/navarroido/Woocommerce-skill/blob/0c20cc0a8b2aa1917b938d4e6f38fa3439942725/skills/store-management/woo-tax-rate-audit/SKILL.md)
- Commit: `0c20cc0a8b2aa1917b938d4e6f38fa3439942725`
- Source SHA256: `b1fbe4a356f9e26366a7ec7762cc402f324a4bfd7eab4bf79d87d8f680dd7549`
- Original license: MIT; [complete text](LICENSE-navarroido--Woocommerce-skill-b0e7288d7939.txt).
- Retained method and changes: Preserves tax-line collection and configuration review. Corrects status-based refund subtraction, rate grouping and duplicate heuristics; removes universal nexus/filing rules, full-void-on-partial-refund and unverified app/API guidance.

## finsilabs/awesome-ecommerce-skills: skills/payments-checkout/tax-calculation/SKILL.md

- Fixed source: [tax-calculation](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/skills/payments-checkout/tax-calculation/SKILL.md)
- Commit: `30a1fb674e41284e738608c059690c251699eb07`
- Source SHA256: `0f4fdf2579651750c1c9221adb6f7dbae392926e138f6e77dd9f2ba6304f8e6b`
- Original license: MIT; [complete text](LICENSE-finsilabs--awesome-ecommerce-skills-f60b7f78a85d.txt).
- Retained method and changes: Preserves tax-line collection and configuration review. Corrects status-based refund subtraction, rate grouping and duplicate heuristics; removes universal nexus/filing rules, full-void-on-partial-refund and unverified app/API guidance.

## finsilabs/awesome-ecommerce-skills: skills/payments-checkout/tax-compliance-automation/SKILL.md

- Fixed source: [tax-compliance-automation](https://github.com/finsilabs/awesome-ecommerce-skills/blob/30a1fb674e41284e738608c059690c251699eb07/skills/payments-checkout/tax-compliance-automation/SKILL.md)
- Commit: `30a1fb674e41284e738608c059690c251699eb07`
- Source SHA256: `43578c2a4cf17439bd667332ed1101e1d3a662dd86da1a53a3f285b55ed983fb`
- Original license: MIT; [complete text](LICENSE-finsilabs--awesome-ecommerce-skills-f60b7f78a85d.txt).
- Retained method and changes: Preserves tax-line collection and configuration review. Corrects status-based refund subtraction, rate grouping and duplicate heuristics; removes universal nexus/filing rules, full-void-on-partial-refund and unverified app/API guidance.

- Primary definition checked 2026-10-02: [Shopify order export structure](https://help.shopify.com/en/manual/fulfillment/managing-orders/exporting-orders). An order export can contain multiple line rows with blank repeated fields. Transaction export coverage is bounded; do not treat authorizations as captured cash.
- Primary definition checked 2026-10-02: [WooCommerce Analytics](https://woocommerce.com/document/woocommerce-analytics/). Analytics tables can be downloaded as CSV; reports have their own filters and definitions. A report export does not establish order-level event coverage.
