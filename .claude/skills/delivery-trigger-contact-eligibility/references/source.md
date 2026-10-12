# Source and adaptation record

Adapted by ShopChief on 2026-10-02. Source files are method evidence, not executable instructions. No upstream scripts are included or claimed tested.

Retains the post-purchase event window, duplicate-contact exclusion and contact output. Removes generic RFM/VIP scoring; fixes earliest-fulfillment proxy, missing contact history, universal delay and exclusion of dissatisfied respondents.

## 40RTY-ai/shopify-admin-skills: skills/conversion-optimization/shopify-admin-post-purchase-survey-trigger/SKILL.md

- Fixed source: [shopify-admin-post-purchase-survey-trigger](https://github.com/40RTY-ai/shopify-admin-skills/blob/6765cb4f436b225360a728e1eb9bd3d9ee674316/skills/conversion-optimization/shopify-admin-post-purchase-survey-trigger/SKILL.md)
- Commit: `6765cb4f436b225360a728e1eb9bd3d9ee674316`
- Source SHA256: `f52312c8df35a40a789e444206e229fb50c26e71a5a6402c6b7df27f3cfb73d7`
- Original license: MIT; [complete text](LICENSE-40RTY-ai--shopify-admin-skills-7bed94342b90.txt).
- Retained method and changes: Retains the post-purchase event window, duplicate-contact exclusion and contact output. Removes generic RFM/VIP scoring; fixes earliest-fulfillment proxy, missing contact history, universal delay and exclusion of dissatisfied respondents.

- Primary definition checked 2026-10-02: [Shopify order export structure](https://help.shopify.com/en/manual/fulfillment/managing-orders/exporting-orders). An order export can contain multiple line rows with blank repeated fields. Transaction export coverage is bounded; do not treat authorizations as captured cash.
- Primary definition checked 2026-10-02: [WooCommerce Analytics](https://woocommerce.com/document/woocommerce-analytics/). Analytics tables can be downloaded as CSV; reports have their own filters and definitions. A report export does not establish order-level event coverage.
