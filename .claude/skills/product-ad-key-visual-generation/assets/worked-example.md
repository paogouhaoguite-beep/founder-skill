# Worked example: Product Ad Key Visual Generation

This is a synthetic production fixture, not a merchant result or a claim of a completed generation. No model calls were made to create this example. Named source files must be supplied or created as clearly synthetic fixtures before execution.

## Input

Synthetic brief: BAG-05 is a navy rectangular canvas tote in bag.png with two short handles and a small cream label. Approved headline: “Carry less. Do more.” Approved CTA: “Explore the tote”. No price or offer. Square output; cream background; text in the left 42% and product in the right half. The brief describes fixture inputs; no source photo or generated ad is bundled.

## Complete generation/edit prompt

```text
Create a square advertising base using the exact navy canvas tote in bag.png. Preserve its rectangular proportions, two short handles, cream label and canvas texture. Place the full bag in the right half on a warm cream studio surface, with the handles entirely inside the frame. Use broad soft light from upper left and a gentle contact shadow. Keep the left 42% visually quiet, mostly uniform cream and completely free of objects or generated lettering. Do not add products, decorative badges, numbers, price, logo or marketing text. This is the clean visual layer; the supplied headline and CTA will be placed separately.
```

## Layout and execution decisions

Copy layout, normalized to the square canvas: headline box x=0.08,y=0.22,w=0.32,h=0.24; CTA box x=0.08,y=0.56,w=0.30,h=0.10. Headline text exactly “Carry less. Do more.”; CTA exactly “Explore the tote”. Use merchant-approved typography if supplied; otherwise use an available legible sans font and record its actual name. These are example layout choices, not ad-platform safe-area rules.

Bind the specified source images through the real tool's reference input, not only through their filenames in prose. Read the tool schema and translate layout intentions into supported options; do not treat the prose as API parameter names. Generate the requested image when inputs and tools exist, open the returned pixels, then apply the acceptance cases below.

## Expected output manifest

The following paths describe requested deliverables; they do not assert files already exist. Record each file's actual path or returned asset ID only after production.

- `BAG-05/key-visual-clean.png`
- `BAG-05/copy-layout.json`
- `BAG-05/ad-square.png`

Record these task-specific fields: `product_reference; clean_visual_path; exact_copy; text_regions; font_used; composition_status; copy_proof; actual_dimensions`.

Also record `status`, `requested_output`, `actual_output` (null before production), `source_assets`, `prompt`, `tool_used` (null if no call), `visual_review` and `unresolved_issues`. Status progresses from `not_generated` to `generated_unreviewed` and only to `verified` after actual output inspection. A failed acceptance item remains `needs_revision` or its specific failure state; incomplete companion artifacts remain pending.

## Acceptance scenarios

1. Full tooling: clean visual has no generated lettering; rendered ad contains the exact headline and CTA, handles are not cropped, and editable layout data is delivered.

2. No text composition capability: produce the clean image if possible, deliver the exact layout JSON and mark ad-square pending_composition. Do not count the layout as a finished ad.

3. An unconfirmed “50% OFF” appears in a generation: reject or remove that text, retain only approved wording and record that no offer was supplied.

4. No image tool or missing source file: return this completed production prompt and the filled reference/layout manifest, with `actual_output: null` and `status: not_generated`. Do not substitute a stock image or report an invented successful render.
