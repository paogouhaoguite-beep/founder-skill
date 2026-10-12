# Worked example: Product Campaign Visual Set

This is a synthetic production fixture, not a merchant result or a claim of a completed generation. No model calls were made to create this example. Named source files must be supplied or created as clearly synthetic fixtures before execution.

## Input

Synthetic campaign FALL-TOTE includes only navy TOTE-08 shown in tote.png. Approved offer: “15% off the navy tote”; code NAVY15; exclusion: “Cannot be combined with other offers.” Validity: 2026-10-10 00:00 to 2026-10-13 00:00 America/New_York, end exclusive. Display end copy: “Ends Oct 12 at 11:59 pm ET”. Requested placements: a 3:1 storefront banner, 4:3 email image and 9:16 social image. These are the example merchant’s requested layouts, not current platform specifications.

## Complete generation/edit prompt

```text
Create the clean campaign anchor for FALL-TOTE using the exact navy tote from tote.png. Preserve its handle count, silhouette, canvas texture and label. Use a warm cream background with a restrained soft amber arc behind the product and consistent soft light from upper left. Keep the whole tote visible, with no extra products or seasonal props implying items included. Leave generous quiet space beside the product for text that will be placed separately. Do not generate lettering, prices, codes or badges. The approved navy product must remain the same across every placement.
```

## Layout and execution decisions

Storefront 3:1: product in right third, offer/code at left, terms below the offer. Email 4:3: product right, offer left, terms in a dedicated lower band. Social 9:16: product in middle, offer above, code/end-copy/terms below, with inset padding adapted to the actual placement. Exact copy for all: “15% off the navy tote”, “Code: NAVY15”, “Ends Oct 12 at 11:59 pm ET”, “Cannot be combined with other offers.” Recomposition prompt for the vertical base: “Adapt the approved FALL-TOTE clean anchor into a vertical composition, using tote.png to lock the identical bag. Keep the whole bag centered in the middle, cream space above and below for separate text, and the same amber arc and upper-left soft light. Do not add text, change the bag or crop its handles.” Use actual supported render options and verify the exported aspects.

Bind the specified source images through the real tool's reference input, not only through their filenames in prose. Read the tool schema and translate layout intentions into supported options; do not treat the prose as API parameter names. Generate the requested image when inputs and tools exist, open the returned pixels, then apply the acceptance cases below.

## Expected output manifest

The following paths describe requested deliverables; they do not assert files already exist. Record each file's actual path or returned asset ID only after production.

- `FALL-TOTE/storefront-3x1.png`
- `FALL-TOTE/email-4x3.png`
- `FALL-TOTE/social-9x16.png`
- `FALL-TOTE/campaign-assets.json`
- `FALL-TOTE/copy-layout.json`

Record these task-specific fields: `placement; locale; product_reference; offer; code; exclusions; start_at; end_at; timezone; copy_version; actual_output; composition_status; crop_review`.

Also record `status`, `requested_output`, `actual_output` (null before production), `source_assets`, `prompt`, `tool_used` (null if no call), `visual_review` and `unresolved_issues`. Status progresses from `not_generated` to `generated_unreviewed` and only to `verified` after actual output inspection. A failed acceptance item remains `needs_revision` or its specific failure state; incomplete companion artifacts remain pending.

## Acceptance scenarios

1. Complete inputs and tools: three actual exports use the same navy bag, 15% offer, NAVY15 code, end copy and exclusion; all required terms remain readable at their target display size.

2. Campaign end is supplied only as “Sunday night”: produce authorized clean artwork, mark expiry unresolved and do not generate a countdown or publish a guessed end time.

3. Email variant says 20% or drops the exclusion: fail that asset even if the banner is correct; restore the exact approved copy and inspect the re-export before marking the set verified.

4. No image tool or missing source file: return this completed production prompt and the filled reference/layout manifest, with `actual_output: null` and `status: not_generated`. Do not substitute a stock image or report an invented successful render.
