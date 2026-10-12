> API 参考快照：2026-07。执行前核对当前店铺连接的 API 版本和实际 schema；本文不是对你店铺的运行验证。
> 不在本文件中的 mutation 一律视为不存在——先 introspect（见 SKILL.md），禁止猜测名称。


# Variants-inventory — 写操作目录

## inventoryActivate
Activates an inventory item at a [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location) by creating an [`InventoryLevel`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryLevel) that tracks stock quantities. This enables you to manage inventory for a [`Pro
```graphql
mutation inventoryActivate($inventoryItemId: ID!, $locationId: ID!, $available: Int, $onHand: Int, $stockAtLegacyLocation: Boolean = false) { inventoryActivate (inventoryItemId: $inventoryItemId, locationId: $locationId, available: $available, onHand: $onHand, stockAtLegacyLocation: $stockAtLegacyLocation) { userErrors { field message } } }
```
Args:
- `inventoryItemId`: ID!
- `locationId`: ID!
- `available`: Int
- `onHand`: Int
- `stockAtLegacyLocation`: Boolean = false

## inventoryAdjustQuantities
Adjusts quantities for inventory items by applying incremental changes at specific locations. Each adjustment modifies the quantity by a delta value rather than setting an absolute amount.

The mutation tracks adjustments with a reason code and optional reference URI for audit trails. Returns an [`I
```graphql
mutation inventoryAdjustQuantities($input: InventoryAdjustQuantitiesInput!) { inventoryAdjustQuantities (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryAdjustQuantitiesInput!
#### `InventoryAdjustQuantitiesInput`
The input fields required to adjust inventory quantities.
- `reason`: String!
- `name`: String!
- `referenceDocumentUri`: String
- `changes`: [InventoryChangeInput!]!

## inventoryBulkToggleActivation
Activates or deactivates an inventory item at multiple locations. When you activate an [`InventoryItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem) at a [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location), that location can stock and track q
```graphql
mutation inventoryBulkToggleActivation($inventoryItemId: ID!, $inventoryItemUpdates: [InventoryBulkToggleActivationInput!]!) { inventoryBulkToggleActivation (inventoryItemId: $inventoryItemId, inventoryItemUpdates: $inventoryItemUpdates) { userErrors { field message } } }
```
Args:
- `inventoryItemId`: ID!
- `inventoryItemUpdates`: [InventoryBulkToggleActivationInput!]!
#### `InventoryBulkToggleActivationInput`
The input fields to specify whether the inventory item should be activated or not at the specified location.
- `locationId`: ID!
- `activate`: Boolean!

## inventoryDeactivate
Removes an inventory item's quantities from a location, and turns off inventory at the location.
```graphql
mutation inventoryDeactivate($inventoryLevelId: ID!) { inventoryDeactivate (inventoryLevelId: $inventoryLevelId) { userErrors { field message } } }
```
Args:
- `inventoryLevelId`: ID!

## inventoryItemUpdate
Updates an [`InventoryItem`](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryItem)'s properties including whether inventory is tracked, cost, SKU, and whether shipping is required. Inventory items represent the goods available to be shipped to customers.
```graphql
mutation inventoryItemUpdate($id: ID!, $input: InventoryItemInput!) { inventoryItemUpdate (id: $id, input: $input) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `input`: InventoryItemInput!
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

## inventoryMoveQuantities
Moves inventory quantities for a single inventory item between different states at a single location. Use this mutation to reallocate inventory across quantity states without moving it between locations.

Each change specifies the quantity to move, the source state and location, and the destination
```graphql
mutation inventoryMoveQuantities($input: InventoryMoveQuantitiesInput!) { inventoryMoveQuantities (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryMoveQuantitiesInput!
#### `InventoryMoveQuantitiesInput`
The input fields required to move inventory quantities.
- `reason`: String!
- `referenceDocumentUri`: String!
- `changes`: [InventoryMoveQuantityChange!]!

## inventorySetQuantities
Set quantities of specified name using absolute values. This mutation supports compare-and-set functionality to handle
concurrent requests properly. If `ignoreCompareQuantity` is not set to true,
the mutation will only update the quantity if the persisted quantity matches the `compareQuantity` value
```graphql
mutation inventorySetQuantities($input: InventorySetQuantitiesInput!) { inventorySetQuantities (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventorySetQuantitiesInput!
#### `InventorySetQuantitiesInput`
The input fields required to set inventory quantities.
- `reason`: String!
- `name`: String!
- `referenceDocumentUri`: String
- `quantities`: [InventoryQuantityInput!]!

## inventoryShipmentAddItems
Adds items to an inventory shipment.

> Caution:
> As of 2026-01, this mutation supports an optional idempotency key using the `@idempotent` directive.
> As of 2026-04, the idempotency key is required and must be provided using the `@idempotent` directive.
> For more information, see the [idempotenc
```graphql
mutation inventoryShipmentAddItems($id: ID!, $lineItems: [InventoryShipmentLineItemInput!]!) { inventoryShipmentAddItems (id: $id, lineItems: $lineItems) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `lineItems`: [InventoryShipmentLineItemInput!]!
#### `InventoryShipmentLineItemInput`
The input fields for a line item on an inventory shipment.
- `inventoryItemId`: ID!
- `quantity`: Int!

## inventoryShipmentCreate
Adds a draft shipment to an inventory transfer.

> Caution:
> As of 2026-01, this mutation supports an optional idempotency key using the `@idempotent` directive.
> As of 2026-04, the idempotency key is required and must be provided using the `@idempotent` directive.
> For more information, see the
```graphql
mutation inventoryShipmentCreate($input: InventoryShipmentCreateInput!) { inventoryShipmentCreate (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryShipmentCreateInput!
#### `InventoryShipmentCreateInput`
The input fields to add a shipment.
- `movementId`: ID!
- `trackingInput`: InventoryShipmentTrackingInput
- `lineItems`: [InventoryShipmentLineItemInput!]!
- `dateCreated`: DateTime
- `barcode`: String

## inventoryShipmentCreateInTransit
Adds an in-transit shipment to an inventory transfer.

> Caution:
> As of 2026-01, this mutation supports an optional idempotency key using the `@idempotent` directive.
> As of 2026-04, the idempotency key is required and must be provided using the `@idempotent` directive.
> For more information, se
```graphql
mutation inventoryShipmentCreateInTransit($input: InventoryShipmentCreateInput!) { inventoryShipmentCreateInTransit (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryShipmentCreateInput!
#### `InventoryShipmentCreateInput`
The input fields to add a shipment.
- `movementId`: ID!
- `trackingInput`: InventoryShipmentTrackingInput
- `lineItems`: [InventoryShipmentLineItemInput!]!
- `dateCreated`: DateTime
- `barcode`: String

## inventoryShipmentDelete
Deletes an inventory shipment. Only draft shipments can be deleted.
```graphql
mutation inventoryShipmentDelete($id: ID!) { inventoryShipmentDelete (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## inventoryShipmentMarkInTransit
Marks a draft inventory shipment as in transit.
```graphql
mutation inventoryShipmentMarkInTransit($id: ID!, $dateShipped: DateTime) { inventoryShipmentMarkInTransit (id: $id, dateShipped: $dateShipped) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `dateShipped`: DateTime

## inventoryShipmentReceive
Receive an inventory shipment.

> Caution:
> As of 2026-01, this mutation supports an optional idempotency key using the `@idempotent` directive.
> As of 2026-04, the idempotency key is required and must be provided using the `@idempotent` directive.
> For more information, see the [idempotency docu
```graphql
mutation inventoryShipmentReceive($id: ID!, $lineItems: [InventoryShipmentReceiveItemInput!], $dateReceived: DateTime, $bulkReceiveAction: InventoryShipmentReceiveLineItemReason) { inventoryShipmentReceive (id: $id, lineItems: $lineItems, dateReceived: $dateReceived, bulkReceiveAction: $bulkReceiveAction) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `lineItems`: [InventoryShipmentReceiveItemInput!]
- `dateReceived`: DateTime
- `bulkReceiveAction`: InventoryShipmentReceiveLineItemReason
#### `InventoryShipmentReceiveItemInput`
The input fields to receive an item on an inventory shipment.
- `shipmentLineItemId`: ID!
- `quantity`: Int!
- `reason`: InventoryShipmentReceiveLineItemReason!

## inventoryShipmentRemoveItems
Remove items from an inventory shipment.
```graphql
mutation inventoryShipmentRemoveItems($id: ID!, $lineItems: [ID!]!) { inventoryShipmentRemoveItems (id: $id, lineItems: $lineItems) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `lineItems`: [ID!]!

## inventoryShipmentSetBarcode
Sets the barcode on an inventory shipment.
```graphql
mutation inventoryShipmentSetBarcode($id: ID!, $barcode: String!) { inventoryShipmentSetBarcode (id: $id, barcode: $barcode) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `barcode`: String!

## inventoryShipmentSetTracking
Edits the tracking info on an inventory shipment.
```graphql
mutation inventoryShipmentSetTracking($id: ID!, $tracking: InventoryShipmentTrackingInput!) { inventoryShipmentSetTracking (id: $id, tracking: $tracking) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `tracking`: InventoryShipmentTrackingInput!
#### `InventoryShipmentTrackingInput`
The input fields for an inventory shipment's tracking information.
- `trackingNumber`: String
- `company`: String
- `trackingUrl`: URL
- `arrivesAt`: DateTime

## inventoryShipmentUpdateItemQuantities
Updates items on an inventory shipment.
```graphql
mutation inventoryShipmentUpdateItemQuantities($id: ID!, $items: [InventoryShipmentUpdateItemQuantitiesInput!] = []) { inventoryShipmentUpdateItemQuantities (id: $id, items: $items) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `items`: [InventoryShipmentUpdateItemQuantitiesInput!] = []
#### `InventoryShipmentUpdateItemQuantitiesInput`
The input fields for a line item on an inventory shipment.
- `shipmentLineItemId`: ID!
- `quantity`: Int!

## inventoryTransferCancel
Cancels an inventory transfer.
```graphql
mutation inventoryTransferCancel($id: ID!) { inventoryTransferCancel (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## inventoryTransferCreate
Creates a draft inventory transfer to move inventory items between [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Location) objects in your store. The transfer tracks which items to move, their quantities, and the origin and destination locations.

Use [`inventoryTransferMark
```graphql
mutation inventoryTransferCreate($input: InventoryTransferCreateInput!) { inventoryTransferCreate (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryTransferCreateInput!
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

## inventoryTransferCreateAsReadyToShip
Creates an inventory transfer in ready to ship.

> Caution:
> As of 2026-01, this mutation supports an optional idempotency key using the `@idempotent` directive.
> As of 2026-04, the idempotency key is required and must be provided using the `@idempotent` directive.
> For more information, see the
```graphql
mutation inventoryTransferCreateAsReadyToShip($input: InventoryTransferCreateAsReadyToShipInput!) { inventoryTransferCreateAsReadyToShip (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryTransferCreateAsReadyToShipInput!
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

## inventoryTransferDelete
Deletes an inventory transfer.
```graphql
mutation inventoryTransferDelete($id: ID!) { inventoryTransferDelete (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## inventoryTransferDuplicate
This mutation allows duplicating an existing inventory transfer. The duplicated transfer will have the same
line items and quantities as the original transfer, but will be in a draft state with no shipments.

> Caution:
> As of 2026-01, this mutation supports an optional idempotency key using the `@
```graphql
mutation inventoryTransferDuplicate($id: ID!) { inventoryTransferDuplicate (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## inventoryTransferEdit
Edits an inventory transfer.
```graphql
mutation inventoryTransferEdit($id: ID!, $input: InventoryTransferEditInput!) { inventoryTransferEdit (id: $id, input: $input) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `input`: InventoryTransferEditInput!
#### `InventoryTransferEditInput`
The input fields to edit an inventory transfer.
- `originId`: ID
- `destinationId`: ID
- `dateCreated`: Date
- `note`: String
- `tags`: [String!]
- `referenceName`: String
- `metafields`: [MetafieldInput!]

## inventoryTransferMarkAsReadyToShip
Sets an inventory transfer to ready to ship.
```graphql
mutation inventoryTransferMarkAsReadyToShip($id: ID!) { inventoryTransferMarkAsReadyToShip (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## inventoryTransferRemoveItems
This mutation removes [`InventoryTransferLineItem`s](https://shopify.dev/docs/api/admin-graphql/latest/objects/InventoryTransferLineItem),
or portions of them, from a `DRAFT` or `READY_TO_SHIP` Transfer.

For each referenced line item, if its entire quantity is still unallocated to a
shipment, the l
```graphql
mutation inventoryTransferRemoveItems($input: InventoryTransferRemoveItemsInput!) { inventoryTransferRemoveItems (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryTransferRemoveItemsInput!
#### `InventoryTransferRemoveItemsInput`
The input fields to remove inventory items from a transfer.
- `id`: ID!
- `transferLineItemIds`: [ID!]

## inventoryTransferSetItems
This mutation sets the quantity for one or more line items on a Transfer.

Only the items you include in the `lineItems` field are updated. Items already on
the transfer but not referenced in your update will stay unchanged. Each inventory
item may appear at most once in `lineItems`; duplicate `inve
```graphql
mutation inventoryTransferSetItems($input: InventoryTransferSetItemsInput!) { inventoryTransferSetItems (input: $input) { userErrors { field message } } }
```
Args:
- `input`: InventoryTransferSetItemsInput!
#### `InventoryTransferSetItemsInput`
The input fields to the InventoryTransferSetItems mutation.
- `id`: ID!
- `lineItems`: [InventoryTransferLineItemInput!]!

## orderEditAddVariant
Adds a [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) as a line item to an [`Order`](https://shopify.dev/docs/api/admin-graphql/latest/objects/Order) that's being edited. The mutation respects the variant's contextual pricing.

You can specify a [`Locati
```graphql
mutation orderEditAddVariant($id: ID!, $variantId: ID!, $locationId: ID, $quantity: Int!, $allowDuplicates: Boolean = false) { orderEditAddVariant (id: $id, variantId: $variantId, locationId: $locationId, quantity: $quantity, allowDuplicates: $allowDuplicates) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `variantId`: ID!
- `locationId`: ID
- `quantity`: Int!
- `allowDuplicates`: Boolean = false

## quantityPricingByVariantUpdate
Updates quantity pricing on a [`PriceList`](https://shopify.dev/docs/api/admin-graphql/latest/objects/PriceList) for specific [`ProductVariant`](https://shopify.dev/docs/api/admin-graphql/latest/objects/ProductVariant) objects. You can set fixed prices (see [`PriceListPrice`](https://shopify.dev/doc
```graphql
mutation quantityPricingByVariantUpdate($priceListId: ID!, $input: QuantityPricingByVariantUpdateInput!) { quantityPricingByVariantUpdate (priceListId: $priceListId, input: $input) { userErrors { field message } } }
```
Args:
- `priceListId`: ID!
- `input`: QuantityPricingByVariantUpdateInput!
#### `QuantityPricingByVariantUpdateInput`
The input fields used to update quantity pricing.
- `quantityPriceBreaksToAdd`: [QuantityPriceBreakInput!]!
- `quantityPriceBreaksToDelete`: [ID!]!
- `quantityPriceBreaksToDeleteByVariantId`: [ID!]
- `quantityRulesToAdd`: [QuantityRuleInput!]!
- `quantityRulesToDeleteByVariantId`: [ID!]!
- `pricesToAdd`: [PriceListPriceInput!]!
- `pricesToDeleteByVariantId`: [ID!]!
