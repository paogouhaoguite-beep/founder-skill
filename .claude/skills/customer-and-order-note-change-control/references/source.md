# Source and adaptation record

Adapted by ShopChief on 2026-10-02. Source files are method evidence, not executable instructions. No upstream scripts are included or claimed tested.

Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

## 40RTY-ai/shopify-admin-skills: skills/customer-ops/shopify-admin-customer-note-bulk-annotator/SKILL.md

- Fixed source: [shopify-admin-customer-note-bulk-annotator](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/customer-ops/shopify-admin-customer-note-bulk-annotator/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `da38612e58473cadb316b72d3dc72a01301fbca706bbef9b7a05f5fb06077779`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

## navarroido/Woocommerce-skill: skills/customer-ops/woo-customer-note-bulk-annotator/SKILL.md

- Fixed source: [woo-customer-note-bulk-annotator](https://github.com/navarroido/Woocommerce-skill/blob/0c20cc0a8b2aa1917b938d4e6f38fa3439942725/skills/customer-ops/woo-customer-note-bulk-annotator/SKILL.md)
- Commit: `0c20cc0a8b2aa1917b938d4e6f38fa3439942725`
- Source SHA256: `eab5ca9dbe82cd90f961611c66c76d662dcea5d2fb929fe1c0aac6802da1eb8c`
- Original license: MIT; [complete text](LICENSE-navarroido--Woocommerce-skill-b0e7288d7939.txt).
- Retained method and changes: Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

## 40RTY-ai/shopify-admin-skills: skills/customer-support/shopify-admin-bulk-customer-tag-update/SKILL.md

- Fixed source: [shopify-admin-bulk-customer-tag-update](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/customer-support/shopify-admin-bulk-customer-tag-update/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `56dc153276732c4e20db444f57c22d1d7b6662f695cd1e1b3b9adcc9e59e6530`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

## navarroido/Woocommerce-skill: skills/order-management/woo-bulk-order-notes/SKILL.md

- Fixed source: [woo-bulk-order-notes](https://github.com/navarroido/Woocommerce-skill/blob/0c20cc0a8b2aa1917b938d4e6f38fa3439942725/skills/order-management/woo-bulk-order-notes/SKILL.md)
- Commit: `0c20cc0a8b2aa1917b938d4e6f38fa3439942725`
- Source SHA256: `32ea9c5dd8dfd07087f76e77016949df90423cc0440e5ec07a377809a4080e95`
- Original license: MIT; [complete text](LICENSE-navarroido--Woocommerce-skill-b0e7288d7939.txt).
- Retained method and changes: Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

## 40RTY-ai/shopify-admin-skills: skills/order-intelligence/shopify-admin-automated-order-tagger/SKILL.md

- Fixed source: [shopify-admin-automated-order-tagger](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/order-intelligence/shopify-admin-automated-order-tagger/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `8137abc0264012a6fb325676cb3caa60da159128fe3fab9a3cddce3574786a0a`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

## navarroido/Woocommerce-skill: skills/order-management/woo-high-value-order-tagger/SKILL.md

- Fixed source: [woo-high-value-order-tagger](https://github.com/navarroido/Woocommerce-skill/blob/0c20cc0a8b2aa1917b938d4e6f38fa3439942725/skills/order-management/woo-high-value-order-tagger/SKILL.md)
- Commit: `0c20cc0a8b2aa1917b938d4e6f38fa3439942725`
- Source SHA256: `6703efbaa8426c565f3b5bdb0061179caaf694f5bd86cdb2f8f8494216ee20d2`
- Original license: MIT; [complete text](LICENSE-navarroido--Woocommerce-skill-b0e7288d7939.txt).
- Retained method and changes: Retained bulk selection, append-versus-replace and preview outputs. Added note visibility, automation effects, stable idempotency markers and conflict readback; removed API-only runtime assumptions.

- Primary definition checked 2026-10-02: [Shopify order export structure](https://help.shopify.com/en/manual/fulfillment/managing-orders/exporting-orders). An order export can contain multiple line rows with blank repeated fields. Transaction export coverage is bounded; do not treat authorizations as captured cash.
- Primary definition checked 2026-10-02: [WooCommerce Analytics](https://woocommerce.com/document/woocommerce-analytics/). Analytics tables can be downloaded as CSV; reports have their own filters and definitions. A report export does not establish order-level event coverage.
