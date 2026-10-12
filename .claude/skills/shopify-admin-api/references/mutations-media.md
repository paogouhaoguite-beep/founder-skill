> API 参考快照：2026-07。执行前核对当前店铺连接的 API 版本和实际 schema；本文不是对你店铺的运行验证。
> 不在本文件中的 mutation 一律视为不存在——先 introspect（见 SKILL.md），禁止猜测名称。


# Media — 写操作目录

## deliveryProfileCreate
Creates a [`DeliveryProfile`](https://shopify.dev/docs/api/admin-graphql/latest/objects/DeliveryProfile) that defines shipping rates for specific products and locations.

A delivery profile groups products with their shipping zones and rates. You can associate profiles with [`SellingPlanGroup`](http
```graphql
mutation deliveryProfileCreate($profile: DeliveryProfileInput!) { deliveryProfileCreate (profile: $profile) { userErrors { field message } } }
```
Args:
- `profile`: DeliveryProfileInput!
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

## deliveryProfileRemove
Enqueue the removal of a delivery profile.
```graphql
mutation deliveryProfileRemove($id: ID!) { deliveryProfileRemove (id: $id) { userErrors { field message } } }
```
Args:
- `id`: ID!

## deliveryProfileUpdate
Updates a [`DeliveryProfile`](https://shopify.dev/docs/api/admin-graphql/latest/objects/DeliveryProfile)'s configuration, including its shipping zones, rates, and associated products.

Modify location groups to control which fulfillment [`Location`](https://shopify.dev/docs/api/admin-graphql/latest/
```graphql
mutation deliveryProfileUpdate($id: ID!, $profile: DeliveryProfileInput!) { deliveryProfileUpdate (id: $id, profile: $profile) { userErrors { field message } } }
```
Args:
- `id`: ID!
- `profile`: DeliveryProfileInput!
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

## fileAcknowledgeUpdateFailed
Acknowledges file update failure by resetting FAILED status to READY and clearing any media errors.
```graphql
mutation fileAcknowledgeUpdateFailed($fileIds: [ID!]!) { fileAcknowledgeUpdateFailed (fileIds: $fileIds) { userErrors { field message } } }
```
Args:
- `fileIds`: [ID!]!

## fileCreate
Creates file assets for a store from external URLs or files that were previously uploaded using the
[`stagedUploadsCreate`](https://shopify.dev/docs/api/admin-graphql/latest/mutations/stageduploadscreate)
mutation.

Use the `fileCreate` mutation to add various types of media and documents to your st
```graphql
mutation fileCreate($files: [FileCreateInput!]!) { fileCreate (files: $files) { userErrors { field message } } }
```
Args:
- `files`: [FileCreateInput!]!
#### `FileCreateInput`
The input fields that are required to create a file object.
- `filename`: String
- `contentType`: FileContentType
- `alt`: String
- `duplicateResolutionMode`: FileCreateInputDuplicateResolutionMode (default: `APPEND_UUID`)
- `originalSource`: String!

## fileDelete
Deletes file assets that were previously uploaded to your store.

Use the `fileDelete` mutation to permanently remove media and file assets from your store when they are no longer needed.
This mutation handles the complete removal of files from both your store's file library and any associated refer
```graphql
mutation fileDelete($fileIds: [ID!]!) { fileDelete (fileIds: $fileIds) { userErrors { field message } } }
```
Args:
- `fileIds`: [ID!]!

## fileUpdate
Updates properties, content, and metadata associated with an existing file asset that has already been uploaded to Shopify.

Use the `fileUpdate` mutation to modify various aspects of files already stored in your store.
Files can be updated individually or in batches.

The `fileUpdate` mutation supp
```graphql
mutation fileUpdate($files: [FileUpdateInput!]!) { fileUpdate (files: $files) { userErrors { field message } } }
```
Args:
- `files`: [FileUpdateInput!]!
#### `FileUpdateInput`
The input fields that are required to update a file object.
- `id`: ID!
- `alt`: String
- `originalSource`: String
- `previewImageSource`: String
- `filename`: String
- `referencesToAdd`: [ID!]
- `referencesToRemove`: [ID!]

## themeFilesCopy
Copy theme files. Copying to existing theme files will overwrite them.
```graphql
mutation themeFilesCopy($themeId: ID!, $files: [ThemeFilesCopyFileInput!]!) { themeFilesCopy (themeId: $themeId, files: $files) { userErrors { field message } } }
```
Args:
- `themeId`: ID!
- `files`: [ThemeFilesCopyFileInput!]!
#### `ThemeFilesCopyFileInput`
The input fields for the file copy.
- `dstFilename`: String!
- `srcFilename`: String!

## themeFilesDelete
Deletes a theme's files.
```graphql
mutation themeFilesDelete($themeId: ID!, $files: [String!]!) { themeFilesDelete (themeId: $themeId, files: $files) { userErrors { field message } } }
```
Args:
- `themeId`: ID!
- `files`: [String!]!

## themeFilesUpsert
Creates or updates theme files in an online store theme. This mutation allows batch operations on multiple theme files, either creating new files or overwriting existing ones with the same filename.

> Note: You can process a maximum of 50 files in a single request.

Each file requires a filename an
```graphql
mutation themeFilesUpsert($themeId: ID!, $files: [OnlineStoreThemeFilesUpsertFileInput!]!) { themeFilesUpsert (themeId: $themeId, files: $files) { userErrors { field message } } }
```
Args:
- `themeId`: ID!
- `files`: [OnlineStoreThemeFilesUpsertFileInput!]!
#### `OnlineStoreThemeFilesUpsertFileInput`
The input fields for the file to create or update.
- `filename`: String!
- `body`: OnlineStoreThemeFileBodyInput!
