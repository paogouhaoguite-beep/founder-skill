> API 参考快照：2026-07。执行前核对当前店铺连接的 API 版本和实际 schema；本文不是对你店铺的运行验证。
> 不在本文件中的 mutation 一律视为不存在——先 introspect（见 SKILL.md），禁止猜测名称。


# Input & Enum Types

#### `CreateMediaInput`
The input fields required to create a media object.
- `originalSource`: String!
- `alt`: String
- `mediaContentType`: MediaContentType!

#### `DeliveryProfileInput`
The input fields for a delivery profile.
- `name`: String
- `profileLocationGroups`: [DeliveryProfileLocationGroupInput!]
- `locationGroupsToCreate`: [DeliveryProfileLocationGroupInput!]
- `locationGroupsToUpdate`: [DeliveryProfileLocationGroupInput!]
- `locationGroupsToDelete`: [ID!]
- `variantsToAssociate`: [ID!]
- `variantsToDissociate`: [ID!]
- `zonesToDelete`: [ID!]
- `methodDefinitionsToDelete`: [ID!]
- `conditionsToDelete`: [ID!]
- `sellingPlanGroupsToAssociate`: [ID!]
- `sellingPlanGroupsToDissociate`: [ID!]
- `coversAllItems`: Boolean

#### `FileCreateInput`
The input fields that are required to create a file object.
- `filename`: String
- `contentType`: FileContentType
- `alt`: String
- `duplicateResolutionMode`: FileCreateInputDuplicateResolutionMode (default: `APPEND_UUID`)
- `originalSource`: String!

#### `FileUpdateInput`
The input fields that are required to update a file object.
- `id`: ID!
- `alt`: String
- `originalSource`: String
- `previewImageSource`: String
- `filename`: String
- `referencesToAdd`: [ID!]
- `referencesToRemove`: [ID!]

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

#### `InventoryAdjustQuantitiesInput`
The input fields required to adjust inventory quantities.
- `reason`: String!
- `name`: String!
- `referenceDocumentUri`: String
- `changes`: [InventoryChangeInput!]!

#### `InventoryBulkToggleActivationInput`
The input fields to specify whether the inventory item should be activated or not at the specified location.
- `locationId`: ID!
- `activate`: Boolean!

#### `InventoryItemInput`
The input fields for an inventory item.
- `sku`: String
- `cost`: Decimal
- `tracked`: Boolean
- `countryCodeOfOrigin`: CountryCode
- `harmonizedSystemCode`: String
- `countryHarmonizedSystemCodes`: [CountryHarmonizedSystemCodeInput!]
- `provinceCodeOfOrigin`: String
- `measurement`: InventoryItemMeasurementInput
- `requiresShipping`: Boolean

#### `InventoryMoveQuantitiesInput`
The input fields required to move inventory quantities.
- `reason`: String!
- `referenceDocumentUri`: String!
- `changes`: [InventoryMoveQuantityChange!]!

#### `InventorySetQuantitiesInput`
The input fields required to set inventory quantities.
- `reason`: String!
- `name`: String!
- `referenceDocumentUri`: String
- `quantities`: [InventoryQuantityInput!]!

#### `InventoryShipmentCreateInput`
The input fields to add a shipment.
- `movementId`: ID!
- `trackingInput`: InventoryShipmentTrackingInput
- `lineItems`: [InventoryShipmentLineItemInput!]!
- `dateCreated`: DateTime
- `barcode`: String

#### `InventoryShipmentLineItemInput`
The input fields for a line item on an inventory shipment.
- `inventoryItemId`: ID!
- `quantity`: Int!

#### `InventoryShipmentReceiveItemInput`
The input fields to receive an item on an inventory shipment.
- `shipmentLineItemId`: ID!
- `quantity`: Int!
- `reason`: InventoryShipmentReceiveLineItemReason!

#### `InventoryShipmentReceiveLineItemReason`
The reason for receiving a line item on an inventory shipment.
- `ACCEPTED`
- `REJECTED`

#### `InventoryShipmentTrackingInput`
The input fields for an inventory shipment's tracking information.
- `trackingNumber`: String
- `company`: String
- `trackingUrl`: URL
- `arrivesAt`: DateTime

#### `InventoryShipmentUpdateItemQuantitiesInput`
The input fields for a line item on an inventory shipment.
- `shipmentLineItemId`: ID!
- `quantity`: Int!

#### `InventoryTransferCreateAsReadyToShipInput`
The input fields to create an inventory transfer.
- `originLocationId`: ID
- `destinationLocationId`: ID
- `lineItems`: [InventoryTransferLineItemInput!]! (default: `[]`)
- `dateCreated`: DateTime
- `note`: String
- `tags`: [String!]
- `referenceName`: String
- `metafields`: [MetafieldInput!]

#### `InventoryTransferCreateInput`
The input fields to create an inventory transfer.
- `originLocationId`: ID
- `destinationLocationId`: ID
- `lineItems`: [InventoryTransferLineItemInput!]! (default: `[]`)
- `dateCreated`: DateTime
- `note`: String
- `tags`: [String!]
- `referenceName`: String
- `metafields`: [MetafieldInput!]

#### `InventoryTransferEditInput`
The input fields to edit an inventory transfer.
- `originId`: ID
- `destinationId`: ID
- `dateCreated`: Date
- `note`: String
- `tags`: [String!]
- `referenceName`: String
- `metafields`: [MetafieldInput!]

#### `InventoryTransferRemoveItemsInput`
The input fields to remove inventory items from a transfer.
- `id`: ID!
- `transferLineItemIds`: [ID!]

#### `InventoryTransferSetItemsInput`
The input fields to the InventoryTransferSetItems mutation.
- `id`: ID!
- `lineItems`: [InventoryTransferLineItemInput!]!

#### `OnlineStoreThemeFilesUpsertFileInput`
The input fields for the file to create or update.
- `filename`: String!
- `body`: OnlineStoreThemeFileBodyInput!

#### `PriceListProductPriceInput`
The input fields representing the price for all variants of a product.
- `productId`: ID!
- `price`: MoneyInput!
- `compareAtPrice`: MoneyInput

#### `ProductBundleCreateInput`
The input fields for creating a componentized product.
- `title`: String!
- `consolidatedOptions`: [ProductBundleConsolidatedOptionInput!]
- `components`: [ProductBundleComponentInput!]!

#### `ProductBundleUpdateInput`
The input fields for updating a componentized product.
- `productId`: ID!
- `title`: String
- `consolidatedOptions`: [ProductBundleConsolidatedOptionInput!]
- `components`: [ProductBundleComponentInput!]

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

#### `ProductDeleteInput`
The input fields for specifying the product to delete.
- `id`: ID!

#### `ProductFeedInput`
The input fields required to create a product feed.
- `language`: LanguageCode!
- `country`: CountryCode!
- `channelId`: ID

#### `ProductOptionCreateVariantStrategy`
The set of variant strategies available for use in the `productOptionsCreate` mutation.
- `LEAVE_AS_IS`
- `CREATE`

#### `ProductOptionDeleteStrategy`
The set of strategies available for use on the `productOptionDelete` mutation.
- `DEFAULT`
- `POSITION`
- `NON_DESTRUCTIVE`

#### `ProductOptionUpdateVariantStrategy`
The set of variant strategies available for use in the `productOptionUpdate` mutation.
- `LEAVE_AS_IS`
- `MANAGE`

#### `ProductResourceFeedbackInput`
The input fields used to create a product feedback.
- `productId`: ID!
- `state`: ResourceFeedbackState!
- `feedbackGeneratedAt`: DateTime!
- `productUpdatedAt`: DateTime!
- `messages`: [String!]
- `channelId`: ID

#### `ProductSetIdentifiers`
The input fields required to identify a resource.
- `id`: ID
- `handle`: String
- `customId`: UniqueMetafieldValueInput

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

#### `ProductStatus`
The possible product statuses.
- `ACTIVE`
- `ARCHIVED`
- `DRAFT`
- `UNLISTED`

#### `ProductUpdateIdentifiers`
The input fields required to identify a product for update.
- `id`: ID
- `handle`: String
- `customId`: UniqueMetafieldValueInput

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

#### `ProductVariantAppendMediaInput`
The input fields required to append media to a single variant.
- `variantId`: ID!
- `mediaIds`: [ID!]!

#### `ProductVariantDetachMediaInput`
The input fields required to detach media from a single variant.
- `variantId`: ID!
- `mediaIds`: [ID!]!

#### `ProductVariantPositionInput`
The input fields representing a product variant position.
- `id`: ID!
- `position`: Int!

#### `ProductVariantRelationshipUpdateInput`
The input fields for updating a composite product variant.
- `parentProductVariantId`: ID
- `parentProductId`: ID
- `productVariantRelationshipsToCreate`: [ProductVariantGroupRelationshipInput!] (default: `null`)
- `productVariantRelationshipsToUpdate`: [ProductVariantGroupRelationshipInput!] (default: `null`)
- `productVariantRelationshipsToRemove`: [ID!] (default: `null`)
- `removeAllProductVariantRelationships`: Boolean (default: `false`)
- `priceInput`: PriceInput (default: `null`)

#### `ProductVariantsBulkCreateStrategy`
The set of strategies available for use on the `productVariantsBulkCreate` mutation.
- `DEFAULT`
- `REMOVE_STANDALONE_VARIANT`
- `PRESERVE_STANDALONE_VARIANT`

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

#### `QuantityPricingByVariantUpdateInput`
The input fields used to update quantity pricing.
- `quantityPriceBreaksToAdd`: [QuantityPriceBreakInput!]!
- `quantityPriceBreaksToDelete`: [ID!]!
- `quantityPriceBreaksToDeleteByVariantId`: [ID!]
- `quantityRulesToAdd`: [QuantityRuleInput!]!
- `quantityRulesToDeleteByVariantId`: [ID!]!
- `pricesToAdd`: [PriceListPriceInput!]!
- `pricesToDeleteByVariantId`: [ID!]!

#### `SubscriptionContractProductChangeInput`
The input fields required to create a Subscription Contract.
- `productVariantId`: ID
- `currentPrice`: Decimal

#### `ThemeFilesCopyFileInput`
The input fields for the file copy.
- `dstFilename`: String!
- `srcFilename`: String!
