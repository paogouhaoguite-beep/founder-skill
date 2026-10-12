# Worked example: Product Detail Page Image Production

This is a synthetic production fixture, not a merchant result or a claim of a completed generation. No model calls were made to create this example. Named source files must be supplied or created as clearly synthetic fixtures before execution.

## Input

Synthetic brief: SKU TOTE-07 is a navy canvas bag with two short handles and one interior zip pocket. Merchant supplies front.png, pocket-closeup.png and dimension-sheet.png confirming 36 cm width and 40 cm height. Approved copy: “Everyday carry”, “Interior zip pocket”, and “36 × 40 cm”. Requested modules: hero, pocket detail and size panel. Request square desktop modules and 4:5 mobile modules; actual tool-supported render sizes must be checked. No load capacity, waterproofness or sustainability claim is approved.

## Complete generation/edit prompt

```text
Produce the clean hero artwork for TOTE-07 using front.png as the product identity. Preserve the exact navy canvas texture, rectangular silhouette, two short handles and small front label. Place the whole bag centered against a warm cream background with soft upper-left studio light. Keep the top quarter quiet for separately placed approved text. Do not add text, props, water, certification badges or additional pockets. Show the full handles and bottom edge. This is the hero module of a matched product page set, not a collage.
```

## Layout and execution decisions

Module 01: place approved “Everyday carry” above the hero with an available text-layout tool. Module 02 complete edit prompt: “Use pocket-closeup.png as identity and framing reference. Show the same interior zip pocket, zipper teeth, pull and stitching in a clean close-up. Preserve the visible lining color and pocket opening. Do not invent a lining compartment or change the closure. Keep the lower fifth quiet for separately placed text; no generated letters.” Overlay “Interior zip pocket”. Module 03: retain the front silhouette and use deterministic line/text placement to show horizontal 36 cm and vertical 40 cm dimensions from dimension-sheet.png; do not infer handle-drop dimensions. For mobile, recompose each module to 4:5 without cutting the hero handles, pocket zipper or dimension arrowheads. Record actual sizes after export.

Bind the specified source images through the real tool's reference input, not only through their filenames in prose. Read the tool schema and translate layout intentions into supported options; do not treat the prose as API parameter names. Generate the requested image when inputs and tools exist, open the returned pixels, then apply the acceptance cases below.

## Expected output manifest

The following paths describe requested deliverables; they do not assert files already exist. Record each file's actual path or returned asset ID only after production.

- `TOTE-07/01-hero-desktop.png`
- `TOTE-07/01-hero-mobile.png`
- `TOTE-07/02-pocket-desktop.png`
- `TOTE-07/02-pocket-mobile.png`
- `TOTE-07/03-size-desktop.png`
- `TOTE-07/03-size-mobile.png`
- `TOTE-07/module-manifest.json`
- `TOTE-07/copy-layout.json`

Record these task-specific fields: `module_id; buyer_question; evidence_reference; exact_copy; visual_type; desktop_output; mobile_output; text_review; crop_review; actual_dimensions`.

Also record `status`, `requested_output`, `actual_output` (null before production), `source_assets`, `prompt`, `tool_used` (null if no call), `visual_review` and `unresolved_issues`. Status progresses from `not_generated` to `generated_unreviewed` and only to `verified` after actual output inspection. A failed acceptance item remains `needs_revision` or its specific failure state; incomplete companion artifacts remain pending.

## Acceptance scenarios

1. Complete evidence and tooling: six images match the same bag, the pocket detail preserves its zipper and lining, the size panel uses only 36 cm and 40 cm, and all three mobile variants remain readable.

2. Pocket close-up missing: finish the supported hero and size modules, mark pocket awaiting_reference and do not generate an imagined interior pocket.

3. Actual phone preview cuts off the 40 cm arrowhead or makes the label unreadable: fail that crop, enlarge/reposition the dimension layout and inspect the revised file; a desktop pass does not approve mobile.

4. No image tool or missing source file: return this completed production prompt and the filled reference/layout manifest, with `actual_output: null` and `status: not_generated`. Do not substitute a stock image or report an invented successful render.
