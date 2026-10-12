# Synthetic worked example

Input template fields: product_name required text, price_text required text, product_image required image. Rows: R1 Bottle B, “USD 30”, approved image I1; R2 Bag C, price missing, image I2.

Mapping: name→product_name, price_display→price_text, asset_id→product_image. R1 passes; R2 blocked for missing price. Manifest: R1 ready to render, R2 blocked. With no connector, no output link is invented. If R1 is rendered successfully, completed count 1/2 intended rows, not “batch complete”.

Boundary scenario 1: Long product name overflows the preview. Revise layout or approved copy before the rest of the batch.
Boundary scenario 2: A job timeout returns no design ID. Search/read job state by row/job reference before issuing another creation.
