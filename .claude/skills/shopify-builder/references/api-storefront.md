# Connected store access

Use the current client's authorized Shopify connector or CLI and inspect its actual schema and permissions. For a missing or expired connection, follow that client's documented setup and continue with local theme files or import drafts. Never request secrets in chat. Only inside ShopChief, its store-scoped connection flow is an optional integration path.

Use the available shopify-admin-api skill/current introspection for Admin operations and the actual supported storefront capability for page reads. Preview authorized writes and read back results. This package does not prescribe direct curl, frozen API versions or manual token exchange.
