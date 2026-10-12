> API 参考快照：2026-07。执行前核对当前店铺连接的 API 版本和实际 schema；本文不是对你店铺的运行验证。
> 不在本文件中的 mutation 一律视为不存在——先 introspect（见 SKILL.md），禁止猜测名称。


# Product — 写操作目录

## bulkProductResourceFeedbackCreate
Creates product feedback for multiple products.
```graphql
mutation bulkProductResourceFeedbackCreate($feedbackInput: [ProductResourceFeedbackInput!]!) { bulkProductResourceFeedbackCreate (feedbackInput: $feedbackInput) { userErrors { field message } } }
```
Args:
- `feedbackInput`: [ProductResourceFeedbackInput!]!
#### `ProductResourceFeedbackInput`
The input fields used to create a product feedback.
- `productId`: ID!
- `state`: ResourceFeedbackState!
- `feedbackGeneratedAt`: DateTime!
- `productUpdatedAt`: DateTime!
- `messages`: [String!]
- `channelId`: ID

## collectionReorderProducts
Asynchronously reorders products within a specified collection. Instead of returning an updated collection, this mutation returns a job, which should be [polled](https://shopify.dev/api/admin-graphql/latest/queries/job). The [`Collection.sortOrder`](https://shopify.dev/api/admin-graphql/latest/objec
```graphql
mutation collectionReorderProducts($id: ID!, $moves: [MoveInput!]!) { collectionReorderProducts (id: $id, moves: $moves) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `moves`: [MoveInput!]!

## giftCardProductSet
Creates or updates a
[`gift card`](https://shopify.dev/docs/api/admin-graphql/latest/objects/GiftCard)
product. This mutation is specifically designed for gift card products and automatically sets
the `giftCard` field to `true`, applies gift card variant defaults (non-taxable, no shipping
required,
```graphql
mutation giftCardProductSet($input: GiftCardProductSetInput!, $synchronous: Boolean = true, $identifier: ProductSetIdentifiers) { giftCardProductSet (input: $input, synchronous: $synchronous, identifier: $identifier) { userErrors { field message } } }
```
Args:
- `input`: GiftCardProductSetInput!
- `synchronous`: Boolean = true
- `identifier`: ProductSetIdentifiers
#### `GiftCardProductSetInput`
The input fields for creating or updating a gift card product with the
[`giftCardProductSet`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/giftCardProductSet)
mutation.

For list fields
- `descriptionHtml`: String
- `handle`: String
- `seo`: SEOInput
- `productType`: String
- `tags`: [String!]
- `templateSuffix`: String
- `giftCardTemplateSuffix`: String
- `title`: String
- `vendor`: String
- `redirectNewHandle`: Boolean
- `status`: ProductStatus
- `collections`: [ID!]
- `metafields`: [MetafieldInput!]
- `files`: [FileSetInput!]
- `productOptions`: [OptionSetInput!]
- `issuanceCurrency`: CurrencyCode
- `crossCurrencyRedeemable`: Boolean
- `variants`: [GiftCardProductVariantSetInput!]

## priceListFixedPricesByProductUpdate
Sets or removes fixed prices for all variants of a [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) on a [`PriceList`](https://shopify.dev/docs/api/admin-graphql/latest/objects/PriceList). Simplifies pricing management when all variants of a product should have the same
```graphql
mutation priceListFixedPricesByProductUpdate($pricesToAdd: [PriceListProductPriceInput!], $pricesToDeleteByProductIds: [ID!], $priceListId: ID!) { priceListFixedPricesByProductUpdate (pricesToAdd: $pricesToAdd, pricesToDeleteByProductIds: $pricesToDeleteByProductIds, priceListId: $priceListId) { userErrors { field message } } }
```
Args:
- `pricesToAdd`: [PriceListProductPriceInput!]
- `pricesToDeleteByProductIds`: [ID!]
- `priceListId`: ID!
#### `PriceListProductPriceInput`
The input fields representing the price for all variants of a product.
- `productId`: ID!
- `price`: MoneyInput!
- `compareAtPrice`: MoneyInput

## productBundleCreate
Creates a product bundle that groups multiple [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) objects together as components. The bundle appears as a single product in the store, with its price determined by the parent product and inventory calculated from the componen
```graphql
mutation productBundleCreate($input: ProductBundleCreateInput!) { productBundleCreate (input: $input) { userErrors { field message } } }
```
Args:
- `input`: ProductBundleCreateInput!
#### `ProductBundleCreateInput`
The input fields for creating a componentized product.
- `title`: String!
- `consolidatedOptions`: [ProductBundleConsolidatedOptionInput!]
- `components`: [ProductBundleComponentInput!]!

## productBundleUpdate
Updates a product bundle or componentized product.
```graphql
mutation productBundleUpdate($input: ProductBundleUpdateInput!) { productBundleUpdate (input: $input) { userErrors { field message } } }
```
Args:
- `input`: ProductBundleUpdateInput!
#### `ProductBundleUpdateInput`
The input fields for updating a componentized product.
- `productId`: ID!
- `title`: String
- `consolidatedOptions`: [ProductBundleConsolidatedOptionInput!]
- `components`: [ProductBundleComponentInput!]

## productCreate
Creates a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
with attributes such as title, description, vendor, and media.

The `productCreate` mutation helps you create many products at once, avoiding the tedious or time-consuming
process of adding them one by one in the
```graphql
mutation productCreate($product: ProductCreateInput, $media: [CreateMediaInput!]) { productCreate (product: $product, media: $media) { userErrors { field message } } }
```
Args:
- `product`: ProductCreateInput
- `media`: [CreateMediaInput!]
#### `ProductCreateInput`
The input fields required to create a product.
- `descriptionHtml`: String
- `handle`: String
- `seo`: SEOInput
- `productType`: String
- `tags`: [String!]
- `templateSuffix`: String
- `giftCardTemplateSuffix`: String
- `title`: String
- `vendor`: String
- `category`: ID
- `giftCard`: Boolean
- `collectionsToJoin`: [ID!]
- `combinedListingRole`: CombinedListingsRole
- `metafields`: [MetafieldInput!]
- `productOptions`: [OptionCreateInput!]
- `status`: ProductStatus
- `requiresSellingPlan`: Boolean
- `claimOwnership`: ProductClaimOwnershipInput

## productDelete
Permanently deletes a product and all its associated data, including variants, media, publications, and inventory items.

Use the `productDelete` mutation to programmatically remove products from your store when they need to be
permanently deleted from your catalog, such as when removing discontinue
```graphql
mutation productDelete($input: ProductDeleteInput!, $synchronous: Boolean = true) { productDelete (input: $input, synchronous: $synchronous) { userErrors { field message } } }
```
Args:
- `input`: ProductDeleteInput!
- `synchronous`: Boolean = true
#### `ProductDeleteInput`
The input fields for specifying the product to delete.
- `id`: ID!

## productDuplicate
Duplicates a product.

If you need to duplicate a large product, such as one that has many
[variants](https://shopify.dev/api/admin-graphql/latest/input-objects/ProductVariantInput)
that are active at several
[locations](https://shopify.dev/api/admin-graphql/latest/input-objects/InventoryLevelInput)
```graphql
mutation productDuplicate($productId: ID!, $newTitle: String!, $newStatus: ProductStatus, $includeImages: Boolean = false, $includeTranslations: Boolean = false, $synchronous: Boolean = true) { productDuplicate (productId: $productId, newTitle: $newTitle, newStatus: $newStatus, includeImages: $includeImages, includeTranslations: $includeTranslations, synchronous: $synchronous) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `newTitle`: String!
- `newStatus`: ProductStatus
- `includeImages`: Boolean = false
- `includeTranslations`: Boolean = false
- `synchronous`: Boolean = true
#### `ProductStatus`
The possible product statuses.
- `ACTIVE`
- `ARCHIVED`
- `DRAFT`
- `UNLISTED`

## productFeedCreate
Creates a product feed for a specific publication.
```graphql
mutation productFeedCreate($input: ProductFeedInput) { productFeedCreate (input: $input) { userErrors { field message } } }
```
Args:
- `input`: ProductFeedInput
#### `ProductFeedInput`
The input fields required to create a product feed.
- `language`: LanguageCode!
- `country`: CountryCode!
- `channelId`: ID

## productFeedDelete
Deletes a product feed for a specific publication.
```graphql
mutation productFeedDelete($id: ID!) { productFeedDelete (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## productFullSync
Runs the full product sync for a given shop.
```graphql
mutation productFullSync($beforeUpdatedAt: DateTime, $id: ID!, $updatedAtSince: DateTime) { productFullSync (beforeUpdatedAt: $beforeUpdatedAt, id: $id, updatedAtSince: $updatedAtSince) { userErrors { field message } } }
```
Args:
- `beforeUpdatedAt`: DateTime
- `id`: ID!
- `updatedAtSince`: DateTime

## productJoinSellingPlanGroups
Adds multiple selling plan groups to a product.
```graphql
mutation productJoinSellingPlanGroups($id: ID!, $sellingPlanGroupIds: [ID!]!) { productJoinSellingPlanGroups (id: $id, sellingPlanGroupIds: $sellingPlanGroupIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `sellingPlanGroupIds`: [ID!]!

## productLeaveSellingPlanGroups
Removes multiple groups from a product.
```graphql
mutation productLeaveSellingPlanGroups($id: ID!, $sellingPlanGroupIds: [ID!]!) { productLeaveSellingPlanGroups (id: $id, sellingPlanGroupIds: $sellingPlanGroupIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `sellingPlanGroupIds`: [ID!]!

## productOptionUpdate
Updates an [option](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption)
on a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product),
such as size, color, or material. Each option includes a name, position, and a list of values. The combination
of a product
```graphql
mutation productOptionUpdate($option: OptionUpdateInput!, $productId: ID!, $optionValuesToAdd: [OptionValueCreateInput!], $optionValuesToUpdate: [OptionValueUpdateInput!], $optionValuesToDelete: [ID!], $variantStrategy: ProductOptionUpdateVariantStrategy) { productOptionUpdate (option: $option, productId: $productId, optionValuesToAdd: $optionValuesToAdd, optionValuesToUpdate: $optionValuesToUpdate, optionValuesToDelete: $optionValuesToDelete, variantStrategy: $variantStrategy) { userErrors { field message } } }
```
Args:
- `option`: OptionUpdateInput!
- `productId`: ID!
- `optionValuesToAdd`: [OptionValueCreateInput!]
- `optionValuesToUpdate`: [OptionValueUpdateInput!]
- `optionValuesToDelete`: [ID!]
- `variantStrategy`: ProductOptionUpdateVariantStrategy
#### `ProductOptionUpdateVariantStrategy`
The set of variant strategies available for use in the `productOptionUpdate` mutation.
- `LEAVE_AS_IS`
- `MANAGE`

## productOptionsCreate
Creates one or more [options](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption)
on a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product),
such as size, color, or material. Each option includes a name, position, and a list of values. The combination
of
```graphql
mutation productOptionsCreate($productId: ID!, $options: [OptionCreateInput!]!, $variantStrategy: ProductOptionCreateVariantStrategy = LEAVE_AS_IS) { productOptionsCreate (productId: $productId, options: $options, variantStrategy: $variantStrategy) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `options`: [OptionCreateInput!]!
- `variantStrategy`: ProductOptionCreateVariantStrategy = LEAVE_AS_IS
#### `ProductOptionCreateVariantStrategy`
The set of variant strategies available for use in the `productOptionsCreate` mutation.
- `LEAVE_AS_IS`
- `CREATE`

## productOptionsDelete
Deletes one or more [options](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption)
from a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product). Product options
define the choices available for a product, such as size, color, or material.

> Caution:
> Remo
```graphql
mutation productOptionsDelete($productId: ID!, $options: [ID!]!, $strategy: ProductOptionDeleteStrategy = DEFAULT) { productOptionsDelete (productId: $productId, options: $options, strategy: $strategy) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `options`: [ID!]!
- `strategy`: ProductOptionDeleteStrategy = DEFAULT
#### `ProductOptionDeleteStrategy`
The set of strategies available for use on the `productOptionDelete` mutation.
- `DEFAULT`
- `POSITION`
- `NON_DESTRUCTIVE`

## productOptionsReorder
Reorders the [options](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOption) and
[option values](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductOptionValue) on a
[product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product),
updating the order in w
```graphql
mutation productOptionsReorder($productId: ID!, $options: [OptionReorderInput!]!) { productOptionsReorder (productId: $productId, options: $options) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `options`: [OptionReorderInput!]!

## productReorderMedia
Reorders [media](https://shopify.dev/docs/api/admin-graphql/latest/interfaces/Media) attached to a product, changing their sequence in product displays. The operation processes asynchronously to handle [products](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) with large media col
```graphql
mutation productReorderMedia($id: ID!, $moves: [MoveInput!]!) { productReorderMedia (id: $id, moves: $moves) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `moves`: [MoveInput!]!

## productSet
Performs multiple operations to create or update products in a single request.

Use the `productSet` mutation to sync information from an external data source into Shopify, manage large
product catalogs, and perform batch updates. The mutation is helpful for bulk product management, including price

```graphql
mutation productSet($input: ProductSetInput!, $synchronous: Boolean = true, $identifier: ProductSetIdentifiers) { productSet (input: $input, synchronous: $synchronous, identifier: $identifier) { userErrors { field message } } }
```
Args:
- `input`: ProductSetInput!
- `synchronous`: Boolean = true
- `identifier`: ProductSetIdentifiers
#### `ProductSetInput`
The input fields required to create or update a product via ProductSet mutation.
- `descriptionHtml`: String
- `handle`: String
- `seo`: SEOInput
- `productType`: String
- `tags`: [String!]
- `templateSuffix`: String
- `giftCardTemplateSuffix`: String
- `title`: String
- `vendor`: String
- `category`: ID
- `giftCard`: Boolean
- `redirectNewHandle`: Boolean
- `status`: ProductStatus
- `collections`: [ID!]
- `metafields`: [MetafieldInput!]
- `files`: [FileSetInput!]
- `productOptions`: [OptionSetInput!]
- `variants`: [ProductVariantSetInput!]
- `requiresSellingPlan`: Boolean
- `claimOwnership`: ProductClaimOwnershipInput
- `combinedListingRole`: CombinedListingsRole

## productUpdate
Updates a [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product)
with attributes such as title, description, vendor, and media.

The `productUpdate` mutation helps you modify many products at once, avoiding the tedious or time-consuming
process of updating them one by one in th
```graphql
mutation productUpdate($product: ProductUpdateInput, $media: [CreateMediaInput!], $identifier: ProductUpdateIdentifiers) { productUpdate (product: $product, media: $media, identifier: $identifier) { userErrors { field message } } }
```
Args:
- `product`: ProductUpdateInput
- `media`: [CreateMediaInput!]
- `identifier`: ProductUpdateIdentifiers
#### `ProductUpdateInput`
The input fields for updating a product.
- `descriptionHtml`: String
- `handle`: String
- `seo`: SEOInput
- `productType`: String
- `tags`: [String!]
- `templateSuffix`: String
- `giftCardTemplateSuffix`: String
- `title`: String
- `vendor`: String
- `category`: ID
- `redirectNewHandle`: Boolean
- `id`: ID
- `collectionsToJoin`: [ID!]
- `collectionsToLeave`: [ID!]
- `deleteConflictingConstrainedMetafields`: Boolean (default: `false`)
- `metafields`: [MetafieldInput!]
- `status`: ProductStatus
- `requiresSellingPlan`: Boolean

## productVariantAppendMedia
Appends existing media from a product to specific variants of that product, creating associations between media files and particular product options. This allows different variants to showcase relevant images or videos.

For example, a t-shirt product might have color variants where each color varia
```graphql
mutation productVariantAppendMedia($productId: ID!, $variantMedia: [ProductVariantAppendMediaInput!]!) { productVariantAppendMedia (productId: $productId, variantMedia: $variantMedia) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `variantMedia`: [ProductVariantAppendMediaInput!]!
#### `ProductVariantAppendMediaInput`
The input fields required to append media to a single variant.
- `variantId`: ID!
- `mediaIds`: [ID!]!

## productVariantDetachMedia
Detaches media from product variants.
```graphql
mutation productVariantDetachMedia($productId: ID!, $variantMedia: [ProductVariantDetachMediaInput!]!) { productVariantDetachMedia (productId: $productId, variantMedia: $variantMedia) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `variantMedia`: [ProductVariantDetachMediaInput!]!
#### `ProductVariantDetachMediaInput`
The input fields required to detach media from a single variant.
- `variantId`: ID!
- `mediaIds`: [ID!]!

## productVariantJoinSellingPlanGroups
Adds multiple selling plan groups to a product variant.
```graphql
mutation productVariantJoinSellingPlanGroups($id: ID!, $sellingPlanGroupIds: [ID!]!) { productVariantJoinSellingPlanGroups (id: $id, sellingPlanGroupIds: $sellingPlanGroupIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `sellingPlanGroupIds`: [ID!]!

## productVariantLeaveSellingPlanGroups
Remove multiple groups from a product variant.
```graphql
mutation productVariantLeaveSellingPlanGroups($id: ID!, $sellingPlanGroupIds: [ID!]!) { productVariantLeaveSellingPlanGroups (id: $id, sellingPlanGroupIds: $sellingPlanGroupIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `sellingPlanGroupIds`: [ID!]!

## productVariantRelationshipBulkUpdate
Creates new bundles, updates component quantities in existing bundles, and removes bundle components for one or multiple [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) objects.

Each bundle variant can contain up to 30 component variants with specified q
```graphql
mutation productVariantRelationshipBulkUpdate($input: [ProductVariantRelationshipUpdateInput!]!) { productVariantRelationshipBulkUpdate (input: $input) { userErrors { field message } } }
```
Args:
- `input`: [ProductVariantRelationshipUpdateInput!]!
#### `ProductVariantRelationshipUpdateInput`
The input fields for updating a composite product variant.
- `parentProductVariantId`: ID
- `parentProductId`: ID
- `productVariantRelationshipsToCreate`: [ProductVariantGroupRelationshipInput!] (default: `null`)
- `productVariantRelationshipsToUpdate`: [ProductVariantGroupRelationshipInput!] (default: `null`)
- `productVariantRelationshipsToRemove`: [ID!] (default: `null`)
- `removeAllProductVariantRelationships`: Boolean (default: `false`)
- `priceInput`: PriceInput (default: `null`)

## productVariantsBulkCreate
Creates multiple [product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant)
for a single [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) in one operation.
You can run this mutation directly or as part of a [bulk operation](https://shopif
```graphql
mutation productVariantsBulkCreate($variants: [ProductVariantsBulkInput!]!, $productId: ID!, $media: [CreateMediaInput!], $strategy: ProductVariantsBulkCreateStrategy = DEFAULT) { productVariantsBulkCreate (variants: $variants, productId: $productId, media: $media, strategy: $strategy) { userErrors { field message } } }
```
Args:
- `variants`: [ProductVariantsBulkInput!]!
- `productId`: ID!
- `media`: [CreateMediaInput!]
- `strategy`: ProductVariantsBulkCreateStrategy = DEFAULT
#### `ProductVariantsBulkInput`
The input fields for specifying a product variant to create as part of a variant bulk mutation.
- `barcode`: String
- `compareAtPrice`: Money
- `id`: ID
- `mediaSrc`: [String!]
- `inventoryPolicy`: ProductVariantInventoryPolicy
- `inventoryQuantities`: [InventoryLevelInput!]
- `quantityAdjustments`: [InventoryAdjustmentInput!]
- `inventoryItem`: InventoryItemInput
- `mediaId`: ID
- `metafields`: [MetafieldInput!]
- `optionValues`: [VariantOptionValueInput!]
- `price`: Money
- `taxable`: Boolean
- `taxCode`: String
- `unitPriceMeasurement`: UnitPriceMeasurementInput
- `showUnitPrice`: Boolean
- `requiresComponents`: Boolean
- `published`: Boolean

## productVariantsBulkDelete
Deletes multiple variants in a single [`Product`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product). Specify the product ID and an array of variant IDs to remove variants in bulk. You can call this mutation directly or through the [`bulkOperationRunMutation`](https://shopify.dev/doc
```graphql
mutation productVariantsBulkDelete($variantsIds: [ID!]!, $productId: ID!) { productVariantsBulkDelete (variantsIds: $variantsIds, productId: $productId) { userErrors { field message } } }
```
Args:
- `variantsIds`: [ID!]!
- `productId`: ID!

## productVariantsBulkReorder
Reorders multiple variants in a single product. This mutation can be called directly or via the bulkOperation.
```graphql
mutation productVariantsBulkReorder($productId: ID!, $positions: [ProductVariantPositionInput!]!) { productVariantsBulkReorder (productId: $productId, positions: $positions) { userErrors { field message } } }
```
Args:
- `productId`: ID!
- `positions`: [ProductVariantPositionInput!]!
#### `ProductVariantPositionInput`
The input fields representing a product variant position.
- `id`: ID!
- `position`: Int!

## productVariantsBulkUpdate
Updates multiple [product variants](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant)
for a single [product](https://shopify.dev/docs/api/admin-graphql/latest/objects/Product) in one operation.
You can run this mutation directly or as part of a [bulk operation](https://shopif
```graphql
mutation productVariantsBulkUpdate($variants: [ProductVariantsBulkInput!]!, $productId: ID!, $media: [CreateMediaInput!], $allowPartialUpdates: Boolean = false) { productVariantsBulkUpdate (variants: $variants, productId: $productId, media: $media, allowPartialUpdates: $allowPartialUpdates) { userErrors { field message } } }
```
Args:
- `variants`: [ProductVariantsBulkInput!]!
- `productId`: ID!
- `media`: [CreateMediaInput!]
- `allowPartialUpdates`: Boolean = false
#### `ProductVariantsBulkInput`
The input fields for specifying a product variant to create as part of a variant bulk mutation.
- `barcode`: String
- `compareAtPrice`: Money
- `id`: ID
- `mediaSrc`: [String!]
- `inventoryPolicy`: ProductVariantInventoryPolicy
- `inventoryQuantities`: [InventoryLevelInput!]
- `quantityAdjustments`: [InventoryAdjustmentInput!]
- `inventoryItem`: InventoryItemInput
- `mediaId`: ID
- `metafields`: [MetafieldInput!]
- `optionValues`: [VariantOptionValueInput!]
- `price`: Money
- `taxable`: Boolean
- `taxCode`: String
- `unitPriceMeasurement`: UnitPriceMeasurementInput
- `showUnitPrice`: Boolean
- `requiresComponents`: Boolean
- `published`: Boolean

## sellingPlanGroupAddProductVariants
Adds multiple product variants to a selling plan group.
```graphql
mutation sellingPlanGroupAddProductVariants($id: ID!, $productVariantIds: [ID!]!) { sellingPlanGroupAddProductVariants (id: $id, productVariantIds: $productVariantIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `productVariantIds`: [ID!]!

## sellingPlanGroupAddProducts
Adds multiple products to a selling plan group.
```graphql
mutation sellingPlanGroupAddProducts($id: ID!, $productIds: [ID!]!) { sellingPlanGroupAddProducts (id: $id, productIds: $productIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `productIds`: [ID!]!

## sellingPlanGroupRemoveProductVariants
Removes multiple product variants from a selling plan group.
```graphql
mutation sellingPlanGroupRemoveProductVariants($id: ID!, $productVariantIds: [ID!]!) { sellingPlanGroupRemoveProductVariants (id: $id, productVariantIds: $productVariantIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `productVariantIds`: [ID!]!

## sellingPlanGroupRemoveProducts
Removes multiple products from a selling plan group.
```graphql
mutation sellingPlanGroupRemoveProducts($id: ID!, $productIds: [ID!]!) { sellingPlanGroupRemoveProducts (id: $id, productIds: $productIds) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `productIds`: [ID!]!

## subscriptionContractProductChange
Allows for the easy change of a Product in a Contract or a Product price change.
```graphql
mutation subscriptionContractProductChange($actor: SubscriptionActor, $subscriptionContractId: ID!, $lineId: ID!, $input: SubscriptionContractProductChangeInput!) { subscriptionContractProductChange (actor: $actor, subscriptionContractId: $subscriptionContractId, lineId: $lineId, input: $input) { userErrors { field message } } }
```
Args:
- `actor`: SubscriptionActor
- `subscriptionContractId`: ID!
- `lineId`: ID!
- `input`: SubscriptionContractProductChangeInput!
#### `SubscriptionContractProductChangeInput`
The input fields required to create a Subscription Contract.
- `productVariantId`: ID
- `currentPrice`: Decimal
