# Source and adaptation record

Adapted by ShopChief on 2026-10-02. Source files are method evidence, not executable instructions. No upstream scripts are included or claimed tested.

Retains refund/reorder workflow but corrects full-total-after-prior-refund, duplicate quantities, copied paid state and automatic damaged restock; scopes cash and replacement independently.

## 40RTY-ai/shopify-admin-skills: skills/customer-support/shopify-admin-refund-and-reorder/SKILL.md

- Fixed source: [shopify-admin-refund-and-reorder](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/customer-support/shopify-admin-refund-and-reorder/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `74d60f96713f483c5269f5f60045e225a6486f3a6ed873b40a5834b4ff6402db`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Retains refund/reorder workflow but corrects full-total-after-prior-refund, duplicate quantities, copied paid state and automatic damaged restock; scopes cash and replacement independently.

## navarroido/Woocommerce-skill: skills/customer-support/woo-refund-and-reorder/SKILL.md

- Fixed source: [woo-refund-and-reorder](https://github.com/navarroido/Woocommerce-skill/blob/0c20cc0a8b2aa1917b938d4e6f38fa3439942725/skills/customer-support/woo-refund-and-reorder/SKILL.md)
- Commit: `0c20cc0a8b2aa1917b938d4e6f38fa3439942725`
- Source SHA256: `b57df469b58c8a858618ec88fac844a0e2710d667f378e19ca3c896c94a4f44a`
- Original license: MIT; [complete text](LICENSE-navarroido--Woocommerce-skill-b0e7288d7939.txt).
- Retained method and changes: Retains refund/reorder workflow but corrects full-total-after-prior-refund, duplicate quantities, copied paid state and automatic damaged restock; scopes cash and replacement independently.

- Primary definition checked 2026-10-02: [Shopify order export structure](https://help.shopify.com/en/manual/fulfillment/managing-orders/exporting-orders). An order export can contain multiple line rows with blank repeated fields. Transaction export coverage is bounded; do not treat authorizations as captured cash.
