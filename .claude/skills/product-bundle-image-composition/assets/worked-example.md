# Worked example: Product Bundle Image Composition

This is a synthetic production fixture, not a merchant result or a claim of a completed generation. No model calls were made to create this example. Named source files must be supplied or created as clearly synthetic fixtures before execution.

## Input

Synthetic bundle BREAKFAST-03 includes exactly two CUP-A ivory cups (each 8 cm tall, 8 cm body diameter) and one TRAY-B rectangular oak tray (32 cm wide). Merchant supplies cup.png and tray.png. Gift box, spoons, tea bags and linen seen in inspiration photographs are excluded. Requested output: square catalog image without text.

## Complete generation/edit prompt

```text
Compose this exact three-piece breakfast set using cup.png for both included cups and tray.png for the single tray. Show exactly two separate ivory CUP-A cups and one rectangular oak TRAY-B tray. Preserve cup handles, rim thickness, color and each tray corner; do not fuse the cups. Use the confirmed size relationship: each cup body is 8 cm across and the tray is 32 cm wide. Place the tray at the rear center and the two cups in the front left and front right, with a visible gap between them; all three pieces must be individually countable. Use a quiet light-gray studio background and consistent soft contact shadows. Do not add spoons, tea, cloth, gift box, duplicate tray, labels or text.
```

## Layout and execution decisions

Square canvas: tray spans approximately 18–82% horizontally in the rear half; cup centers around 35% and 65% horizontally in the foreground. Coordinates are compositional intentions, not fixed API parameters. The product proportions from the references and dimensions override decorative symmetry.

Bind the specified source images through the real tool's reference input, not only through their filenames in prose. Read the tool schema and translate layout intentions into supported options; do not treat the prose as API parameter names. Generate the requested image when inputs and tools exist, open the returned pixels, then apply the acceptance cases below.

## Expected output manifest

The following paths describe requested deliverables; they do not assert files already exist. Record each file's actual path or returned asset ID only after production.

- `BREAKFAST-03/bundle-main.png`
- `BREAKFAST-03/contents-manifest.json`

Record these task-specific fields: `instance_id; sku; source_reference; image_region; included; count_review; relative_scale_basis`.

Also record `status`, `requested_output`, `actual_output` (null before production), `source_assets`, `prompt`, `tool_used` (null if no call), `visual_review` and `unresolved_issues`. Status progresses from `not_generated` to `generated_unreviewed` and only to `verified` after actual output inspection. A failed acceptance item remains `needs_revision` or its specific failure state; incomplete companion artifacts remain pending.

## Acceptance scenarios

1. Complete case: CUP-A-1, CUP-A-2 and TRAY-B-1 are separately identifiable, both cups match cup.png, the tray matches tray.png and no excluded object is present.

2. Cup quantity missing: do not choose two based on the visual brief. Obtain the sales quantity; until then provide the layout and prompt with quantity unresolved and mark no sales asset generated.

3. Generated image shows three cups and one tray: fail the count check even if the total visual arrangement looks balanced; regenerate only the erroneous instance region or use a more separated layout.

4. No image tool or missing source file: return this completed production prompt and the filled reference/layout manifest, with `actual_output: null` and `status: not_generated`. Do not substitute a stock image or report an invented successful render.
