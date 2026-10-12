---
name: merchant-bulk-creative-production
description: "Generate a traceable batch of product creatives from a verified template schema and merchant data rows."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Bulk Creative Production

## Inputs
Require authorized template, its field schema, source data with stable row IDs, image rights/assets, required output formats and allowed generation scope. A compatible design connector can render; local CSV plus mapping and a preview specification is the fallback. Do not claim bulk assets exist when only a plan exists.

## Batch control
Inspect schema before mapping data. Separate text, image and numeric fields, required values and limits. Map columns explicitly, retaining identifiers and locale/currency formatting. Validate duplicates, missing fields, broken images, claim support and incompatible variants before jobs start.

Resolve images to approved asset identifiers or accessible rights-cleared files. A URL alone is not proof of licensing or successful upload. Preview one representative row, a long-text row and a missing/edge row. Check template fit, price/qualifier visibility and correct product-image pairing.

Create one tracked job per intended row with row ID, template version, inputs and output ID/status. Respect actual rate limits and partial failures. Retry failed or unknown rows only after checking existing outputs to avoid duplicates. Never let one successful job imply the whole batch completed.

## Deliver
Provide output manifest, actual links/files, mapping, validation failures and unresolved rows. Keep original data and template unchanged. Posting creatives or spending on ads remains outside batch creation.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-bulk-creative-production&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
