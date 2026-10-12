# Connected Shopify execution mapping

Use the current tenant/store's authorized tools and the connected API version. Consult the available shopify-admin-api skill or introspect the current schema before constructing mutations; this mapping describes operations, not a frozen payload schema.

1. Read existing product/handle/SKUs with pagination; distinguish retries and updates from creation. Check store currency, option constraints and inventory locations. Do not hardcode a shop or token.
2. For local binary media, obtain staged upload targets through supported tools and upload with the returned parameters; use the returned resource reference according to the verified media input schema. For an already reusable Shopify file, use its verified reference. Never guess stagedUploadTarget, file, options or other field names. Poll media readiness; a successful product mutation does not prove image processing completed.
3. Create DRAFT using the supported product operation. productSet may be suitable for a complete new product; current schema uses productOptions, with variant/inventory/media input types to be verified. For updates, prefer targeted mutations. productSet synchronizes supplied list fields and may delete entries omitted from those lists; read the full existing lists and require approval of deletions before using it. Large jobs may be asynchronous: retain operation ID and poll documented completion.
4. Set only authorized inventory at the selected location with current supported concurrency/compare quantities. Supplier stock is never copied into shop inventory without an explicit instruction. A stale quantity requires a fresh read, not bypassing the comparison.
5. Read back all affected fields, paginating variants/media and location inventory. Compare IDs, counts, price/currency, selected options, image readiness/association, SEO and DRAFT status. Do not declare success from the first 100 variants or first 50 images.
6. Publication is separate: after explicit authorization use the current product status mutation plus publishablePublish for the actual selected publication IDs as needed. Verify product status AND channel publication/availability, URL and visible state. Do not claim ACTIVE alone publishes a product.
7. Record the actual Shopify IDs, changed fields and verification results in the local launch sheet. Only when running inside ShopChief with an available authorized workspace tool, optionally sync the product using its current schema. Prefer update/link by existing Shopify ID over duplicate creation. An unavailable or failed workspace sync must not block delivery, undo a successful draft or trigger recreation.

At every write inspect transport/provider status, top-level errors and userErrors. If the outcome is uncertain, read current state before retrying; record successful IDs and incomplete steps. Never print credentials. Return exact object/field failures and a bounded resume plan.

References checked 2026-09-05:
- https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet
- https://shopify.dev/docs/apps/build/sales-channels/product-publishing
