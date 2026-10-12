# Synthetic variant repair

All products, identifiers, URLs and source records below are invented. This is a completed review artifact, not an upload or a merchant outcome.

## Supplied evidence

- `catalog-demo.csv`, observed 2026-10-01: POUCH-BLUE is the blue variant of family POUCH; base price USD 30. GTIN and current stock are absent.
- `feed-before-demo.csv`, exported 2026-09-30: the same item has red copy, a red-variant URL and USD 25.
- `variant-map-demo.csv`: the blue variant uses `?variant=blue`; this map does not prove that the destination currently renders the correct price.
- Live landing-page access is unavailable. The destination, price, image and availability checks remain pending.

## Before row

```csv
id,item_group_id,title,color,link,price,gtin
POUCH-BLUE,POUCH,"Travel pouch, red",red,https://store.example.com/products/pouch?variant=red,25.00 USD,
```

## Proposed after row — held for verification

```csv
id,item_group_id,title,color,link,price,gtin
POUCH-BLUE,POUCH,"Travel pouch, blue",blue,https://store.example.com/products/pouch?variant=blue,30.00 USD,
```

This is a **partial review extract**, not a complete upload-ready feed: destination-required fields such as availability and image details have not been supplied. The item ID and family relationship are preserved. An empty GTIN is an unresolved field, not a declaration that the item is identifier-exempt.

## Completed change register

| Item | Field | Before | Proposed after | Evidence | Release condition |
|---|---|---|---|---|---|
| POUCH-BLUE | title | Travel pouch, red | Travel pouch, blue | Catalog variant is blue | Copy change ready for merchant review |
| POUCH-BLUE | color | red | blue | Catalog variant is blue | Attribute change ready for review |
| POUCH-BLUE | link | red variant | blue variant | Supplied variant map | Open the actual blue destination and verify selected variant |
| POUCH-BLUE | price | 25.00 USD | 30.00 USD | Catalog base price, October 1 | Reconcile current destination and any sale before import |
| POUCH-BLUE | gtin | empty | empty | No manufacturer identifier supplied | Obtain valid identifier evidence or applicable exception; do not invent one |
| POUCH-BLUE | availability | not provided | unresolved | No stock record | Obtain current variant availability |

**Readout:** one of one scoped rows has proposed changes; zero rows have been uploaded or approved. Review title/color now; hold feed activation until destination and required-attribute checks are complete. Retain the original export for rollback.

## Acceptance scenarios

1. Two variants share one family ID but have separate item IDs. Preserve separate rows and the valid group relationship; do not merge them into one offer.
2. The feed has a price and the page cannot be opened. Keep the comparison unverified and the upload gate pending; do not certify price consistency.
