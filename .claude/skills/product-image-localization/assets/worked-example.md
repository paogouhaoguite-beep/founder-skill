# Worked example: Product Image Localization

This is a synthetic production fixture, not a merchant result or a claim of a completed generation. No model calls were made to create this example. Named source files must be supplied or created as clearly synthetic fixtures before execution.

## Input

Synthetic brief: a square SHAMPOO-06 image contains a bottle on the right, immutable bottle label “250 mL”, and editable English marketing text “Daily wash” at top left and “For normal hair” below it. Approved French replacements are “Lavage quotidien” and “Pour cheveux normaux”. Merchant requests French marketing artwork; the bottle label and all product pixels must stay unchanged. Input file shampoo-ad-en.png is a fixture specification, not included.

## Complete generation/edit prompt

```text
Edit shampoo-ad-en.png only in the two approved left-side marketing text regions. Replace “Daily wash” with exactly “Lavage quotidien” in the upper-left heading region. Replace “For normal hair” with exactly “Pour cheveux normaux” in the subheading region below it. Preserve the original hierarchy and dark text color, using line breaks within each region if necessary. Keep the bottle, its shape, cap, colors, every bottle-label pixel including “250 mL”, background, shadow and all unlisted regions unchanged. Do not translate the bottle label, convert units, add a benefit claim or redraw the product. Return one French marketing image.
```

## Layout and execution decisions

Ledger: heading x=0.07,y=0.12,w=0.38,h=0.18; subheading x=0.07,y=0.33,w=0.38,h=0.14. Coordinates are normalized against the inspected source canvas; verify them on the actual input before constructing tool-specific masks. Bottle region remains protected. If generated text is inaccurate, create a cleaned text plate and overlay the exact approved strings using available text-layout tools.

Bind the specified source images through the real tool's reference input, not only through their filenames in prose. Read the tool schema and translate layout intentions into supported options; do not treat the prose as API parameter names. Generate the requested image when inputs and tools exist, open the returned pixels, then apply the acceptance cases below.

## Expected output manifest

The following paths describe requested deliverables; they do not assert files already exist. Record each file's actual path or returned asset ID only after production.

- `SHAMPOO-06/shampoo-ad-fr.png`
- `SHAMPOO-06/translation-ledger.json`

Record these task-specific fields: `source_asset; target_locale; region_bbox; source_text; approved_target_text; editable; text_proof; outside_region_review`.

Also record `status`, `requested_output`, `actual_output` (null before production), `source_assets`, `prompt`, `tool_used` (null if no call), `visual_review` and `unresolved_issues`. Status progresses from `not_generated` to `generated_unreviewed` and only to `verified` after actual output inspection. A failed acceptance item remains `needs_revision` or its specific failure state; incomplete companion artifacts remain pending.

## Acceptance scenarios

1. Normal case: two French strings match exactly, bottle label still reads “250 mL”, product details remain unchanged and no extra claim is introduced.

2. Source reads “2?0 mL” and the user asks to translate the bottle: do not infer the digit or overwrite the label. Request a clear source/approved label, while proceeding on independent authorized marketing regions.

3. Tool redraws the bottle while correctly translating the headings: fail the unchanged-region check and return to a local text edit or deterministic overlay; fluent French is not a pass.

4. No image tool or missing source file: return this completed production prompt and the filled reference/layout manifest, with `actual_output: null` and `status: not_generated`. Do not substitute a stock image or report an invented successful render.
