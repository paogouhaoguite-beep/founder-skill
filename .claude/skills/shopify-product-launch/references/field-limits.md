# Platform validation and merchant preferences

Inspect the connected API version/schema and actual store capability before writes. Verified reference: https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet (checked 2026-09-05) describes a default maximum of 2,048 variants. Provider input-array, mutation batch and async limits are separate from total variants; split/paginate accordingly. A connector-specific smaller limit must be reported as a connector limitation, not Shopify's universal limit.

| Field | Rule |
|---|---|
| Product title | Clear, factual, aligned with merchant conventions; validate actual API limits |
| Handle | Readable and unique, preserve existing published URL; no universal 25-character/3-word rule |
| SEO title/description | Roughly 60/155–160 characters are preview targets, not guaranteed SERP display or universal API limits; follow store language and actual API constraints |
| Variants/options | Check connected limits (Shopify default 2,048 variants, up to 3 option axes); batch writes and paginate readback |
| Description | Use useful facts, benefits and care/specs; story/FAQ only when relevant and supported |
| Media | Preserve product identity and map to the correct variants; verify ready state |
| SKU | Preserve merchant scheme, check duplicates and distinguish update from a new product |
| Tags/collections | Store preference and approved scope; preserve on update unless explicitly changed |
| Price/compare-at | Confirmed prices and substantiated reference price only |

Merchant-specific tighter limits apply only to that merchant. Report validation failures for the affected field and fix before writing, not by silently truncating or deleting business data.
