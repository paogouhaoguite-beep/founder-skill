# Worked example: Product Lifestyle Scene Generation

This is a synthetic production fixture, not a merchant result or a claim of a completed generation. No model calls were made to create this example. Named source files must be supplied or created as clearly synthetic fixtures before execution.

## Input

Synthetic merchant brief: SKU LAMP-02, an unlit sage-green cylindrical table lamp, 24 cm tall and 12 cm wide, with a single rear cable visible in product.png. Scene: dry oak sideboard in a quiet living room; no people. Requested output: landscape 4:3, left third left empty for later copy. The product image is a required merchant input; it is not included in this fixture.

## Complete generation/edit prompt

```text
Place the exact unlit sage-green table lamp from product.png on a dry oak sideboard. Preserve its cylindrical silhouette, 2:1 height-to-width ratio, visible cable exit and surface finish. Keep it unlit; do not invent controls or a glowing shade. Set the lamp in the right half, with its base centered around 70% of frame width and 76% of frame height. Use a softly blurred neutral wall and leave the left third empty. Daylight enters from upper left: match the lamp highlights to this light and create a soft contact shadow touching its base, extending to the right. Use eye-level perspective slightly above the sideboard. No added accessories, plants crossing the lamp or text.
```

## Layout and execution decisions

The sideboard top is the support plane; the base must touch it. Keep the full lamp and the visible cable segment inside the crop. Oak grain is visual context, not a ruler: the supplied lamp proportions are locked but scene dimensions are illustrative.

Bind the specified source images through the real tool's reference input, not only through their filenames in prose. Read the tool schema and translate layout intentions into supported options; do not treat the prose as API parameter names. Generate the requested image when inputs and tools exist, open the returned pixels, then apply the acceptance cases below.

## Expected output manifest

The following paths describe requested deliverables; they do not assert files already exist. Record each file's actual path or returned asset ID only after production.

- `LAMP-02/living-room-4x3.png`
- `LAMP-02/scene-card.md`

Record these task-specific fields: `identity_reference; support_plane; contact_point; light_direction; scale_basis; crop_review; actual_dimensions`.

Also record `status`, `requested_output`, `actual_output` (null before production), `source_assets`, `prompt`, `tool_used` (null if no call), `visual_review` and `unresolved_issues`. Status progresses from `not_generated` to `generated_unreviewed` and only to `verified` after actual output inspection. A failed acceptance item remains `needs_revision` or its specific failure state; incomplete companion artifacts remain pending.

## Acceptance scenarios

1. Normal case: output lamp remains unlit, base and shadow touch the sideboard, highlights and shadow agree, and the left third remains usable for text.

2. Dimensions absent: remove exact scale claims; use the observed height-to-width ratio and disclose illustrative scene scale instead of inventing centimeters.

3. Generated cable disappears or base floats: mark the image needs_revision and issue a localized correction using the original reference; do not mark the scene ready merely because the render is attractive.

4. No image tool or missing source file: return this completed production prompt and the filled reference/layout manifest, with `actual_output: null` and `status: not_generated`. Do not substitute a stock image or report an invented successful render.
