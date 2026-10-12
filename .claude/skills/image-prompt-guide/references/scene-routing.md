## Scene Router

### Priority 1 — Platform Product Image (Composite)

| Trigger | Reference | Action |
|---------|-----------|--------|
| User mentions a specific e-commerce platform (Amazon, eBay, Walmart, Shopify, Etsy, AliExpress, TikTok Shop, Shopee, Lazada, Alibaba.com, 1688) AND requests main image / image set / listing images | `platform-product-guidelines.md` | Must load platform specs, then load each selected output scene reference. Plan by requested output image and merge compatible edits per Step 4. |

Platform Product Image is a composite workflow — it consults platform requirements first, then delegates to White Background, Scene Image, Model Showcase, etc. as sub-tasks.

**Sub-task execution rules:**
- When the user uploaded product images, ALL sub-tasks MUST use those exact images through the available editing tool's documented reference mechanism; never fall back to text-to-image.
- Only **Selling Point Image** and **Logo Design** sub-tasks may trigger user clarification (for selling-point confirmation or brand context). All other sub-tasks execute directly unless safety or missing required inputs block execution.

**Platform image set planner**:
When the user requests multiple listing images (e.g. "3/5/6/11 main images", "main images + detail page images", "Alibaba.com product image set"), create an execution plan before generation:

1. Hero/main image — full product, clean white or light background, no promotional text unless the platform allows it
2. Scene image — B2B or use-context background while preserving the product
3. Detail image — visible material/structure close-up only
4. Selling-point image — only user-provided or visible/verifiable claims
5. Scale/usage image — only if supported by the image or user request
6. Packaging/accessory image — only if visible or user-provided

Rules:
- Generate or edit one final image per planned output. Do not split a single planned output into multiple AI calls unless Step 4 requires `true_sequential`.
- If the tool can only produce one image per call, explicitly run multiple calls or state the limitation.
- Output count must match the requested count when feasible; otherwise explain which planned images were produced and which remain.
- For uploaded product images, every planned image must preserve product identity and pass the exact sources through the selected tool's documented reference mechanism.

### Priority 2 — Single-Purpose Scenes

These use dedicated `planning mode` values that perform only one function. They are valid only for exact single-operation requests:

| Scene | Trigger Keywords | Reference | planning mode |
|-------|-----------------|-----------|-----------|
| **White Background** | white background, pure white bg, remove background to white | `white-background.md` | `white_background` |
| **Watermark / Element Removal** | remove authorized watermark, remove URL/contact/QR overlay, remove accidental overlay, remove non-product object/clutter | `remove-watermark.md` | `watermark_removal` |
| **HD Upscale** | upscale, enhance resolution, make clearer, sharpen, higher quality | `hd-upscale.md` | `hd_upscale` |

**Single-Purpose Use Rule**:
Use these planning modes only when the user's request exactly matches the single operation and does not require layout, composition, lighting, platform compliance, text editing, ratio change, or multiple visual changes.

Watermark removal is only allowed when the user owns the image or has rights to edit it. Do not help remove third-party copyright marks, platform watermarks, photographer signatures, or ownership identifiers to bypass licensing. Allowed cases include removing the user's own watermark, accidental overlays, stains, dust, scanner marks, or non-ownership visual clutter.

Do not treat every "delete text/logo" request as Watermark Removal. If the target is product/package text, a product brand mark, or user-specified local text, route to Text Editing's local text removal flow. If the target looks like an ownership or licensing mark and rights are unclear, ask for confirmation before editing.

**Single-Purpose Fallback**:
Switch to a merged `focused_edit`, merged `structured_composition`, or `true_sequential` plan when:
- The request contains 2 or more intents
- The user asks for platform-ready or listing-ready output
- The user uses broad outcome language such as "professional", "optimized", "cleaner", "main image", or "selling image"
- The user specifies a non-1:1 aspect ratio
- The user requests follow-up edits after the initial single-purpose operation

### Priority 3 — Specialized Editing Scenes

| Scene | Trigger Keywords | Reference | planning mode |
|-------|-----------------|-----------|-----------|
| **Scene Image** | scene shot, change/swap background, place in environment, lifestyle shot | `scene-image.md` | `focused_edit` (preferred when product preserved) |
| **SKU Color Change** | recolor product, change product color, SKU color variant | `sku-color-change.md` | `focused_edit` / `structured_composition` |
| **Logo Customization** | print logo on product, logo mockup, emboss/engrave/stamp logo | `logo-customization.md` | `focused_edit` |
| **Model Showcase** | model photo, add model, model wearing/holding product | `model-showcase.md` | `focused_edit` |
| **Image Detail** | detail shot, zoom in, close-up of texture/stitching | `image-detail.md` | `focused_edit` |
| **Selling Point Image** | selling point image, highlight features, comparison image, vs competitors | `selling-point.md` | `focused_edit` / `structured_composition` |
| **Image Translation** | translate text in image, convert image text to [language] | `image-translation.md` | `focused_edit` |
| **Text Editing** | change text in image, replace text, fix typo, update price/date | `text-editing.md` | `focused_edit` / `structured_composition` |
| **Logo Design** | design a logo, create brand mark, logo from scratch | `logo-design.md` | `structured_composition` for generation / `focused_edit` or `structured_composition` for editing |
| **Tech Pack** | tech pack, dimension drawing, manufacturing spec, assembly diagram | `tech-pack.md` | `structured_composition` |

> **Image Translation mandatory rule**: When the user requests an edited translated image, load `image-translation.md` and execute with the available editing tool after required inputs are available. If no editing tool is available, report that the requested image has not been produced; do not present text-only translation as the completed edit.

### Priority 4 — General (Fallback)

If no specialized scene matches, use semantic instructions with `focused_edit` or `structured_composition` based on complexity. Refer to `style-guide.md` for prompt enrichment vocabulary (atmosphere, composition, lighting, materials).

### Key Disambiguation Rules

These cover the most commonly confused routing decisions:

| Ambiguous Request | Correct Route | Why |
|-------------------|---------------|-----|
| "Change background to white" | **White Background** | Pure white (#FFFFFF) → single-purpose task |
| "Change background to kitchen / blue / gray" | **Scene Image** | Any non-pure-white background = scene swap |
| "Recolor the product body" | **SKU Color Change** | Product color, not background |
| "[Platform name] + white background main image" | **Platform** → White Background | Platform keyword → Priority 1 first |
| "Zoom in on zipper detail" vs "Highlight waterproof feature" | **Image Detail** vs **Selling Point** | Pure zoom (no text) → Detail; zoom + marketing copy → Selling Point |
| "Lifestyle selling point image" / "Detail with callouts" | **Selling Point Image** | Marketing expressions + any other scene keyword → Selling Point wins |
| "Make image clearer" vs "Generate a 2K image" | **HD Upscale** vs Resolution Routing | No resolution specified → upscale; explicit resolution → see below |
| "Design a logo" vs "Print logo on product" | **Logo Design** vs **Logo Customization** | From scratch → Design; apply existing → Customization |
| "Translate text in image" vs "Change price from 50% to 70%" | **Image Translation** vs **Text Editing** | Cross-language → Translation; same-language replacement → Text Editing |
| "Delete specified product text" vs "Remove authorized watermark/overlay" vs "Add marketing copy" | **Text Editing** vs **Watermark Removal** vs **Selling Point** | Product/package text removal → Text Editing local removal; authorized watermark/contact/QR/non-product overlay removal → `watermark_removal`; add new text + layout → Selling Point |
| "Tech pack / dimension drawing" vs "Mark dimensions as selling point" | **Tech Pack** vs **Selling Point ③** | Production/OEM specs → Tech Pack; marketing display → Selling Point |

### Strict Product Fidelity Mode

Enable this mode whenever the user asks to keep the product unchanged, produce platform/listing images from a reference, remove/replace text while preserving the product, make a white-background hero, or change only the surrounding scene/background.

Append this constraint to all relevant image-generation/editing prompts:

```
Keep the product exactly unchanged — preserve geometry, color, texture, labels, and camera angle.
Only change: [describe allowed changes here].
Do not redraw, simplify, or invent any product detail.
```

Keep the constraint concise (≤3 lines). Verbose constraint lists (enumerating 20+ protected items) do not improve model compliance and can reduce prompt execution quality.

When product fidelity conflicts with a more creative instruction, product fidelity wins unless the user explicitly asks to redesign the product.

**Planning rule**: When Strict Product Fidelity Mode is active, prefer `focused_edit` over `structured_composition` unless the loaded reference requires dense layout or annotations. In many runtimes, structured prompt strategies are more likely to affect the whole image, increasing product drift risk.

**Selling Point Image priority rule**: When a request combines marketing expressions (selling point, copy, layout, callout, comparison) with other scene keywords (detail, scene, model), route to **Selling Point Image**. Only Selling Point Image can output copy + layout + visual anchors together.

### Output Size Routing

| Request | Action |
|---------|--------|
| "Make it clearer / sharpen" | Use the available enhancement/editing tool with the exact supported source reference and a concise preservation-first prompt. |
| "Generate at 1K / 2K" | Check the current tool's supported dimensions and parameter names, then request the matching output size. |
| "4K" or higher | Use native output at the requested size if the selected route supports it. Otherwise state its actual limit and use an available authorized upscale step when suitable; label upscaled output. |

### Planning Mode Safety Rules

A planning mode organizes the prompt; it is not a tool argument or the user's intent.

Before selecting a planning mode:
1. Identify the user's desired final outcome.
2. List all required visual changes.
3. Check whether a single-purpose planning mode can satisfy all required changes.
4. If not, use a merged `focused_edit`, merged `structured_composition`, or `true_sequential` plan only when required by Step 4.

Use single-purpose planning modes only when the user requests exactly one operation:
- `white_background`: only pure white background replacement
- `hd_upscale`: only clarity/resolution improvement
- `watermark_removal`: authorized removal of watermarks, URLs, contact info, QR codes, accidental overlays, stains, dust, scanner marks, or non-product visual clutter. Product/package text and product brand marks are not this route.

Do not use single-purpose planning modes for:
- Platform-ready product images
- General image optimization
- "Make it professional"
- Mixed requests
- Follow-up refinements
- Layout, text, selling-point, or composition changes
- Requests involving product coverage, shadows, centering, lighting, or platform compliance

### Planning Misrouting Guard

| User Request | Avoid | Prefer |
|-------------|-------|--------|
| "Make this an Amazon main image" | `white_background` only | Platform workflow + prompted edit |
| "Make it cleaner/professional" | `hd_upscale` only | Product cleanup with safe defaults |
| "Remove text and make white background" | `watermark_removal` only | Load Text Editing or Watermark Removal + White Background; prefer one merged `focused_edit` unless true sequential is required |
| "Optimize this product photo" | Single-purpose planning mode | Product cleanup / platform intent |
| "Change background and improve lighting" | `white_background` | Load Scene Image; use one merged `focused_edit` |
| "Delete logo from product" | `watermark_removal` blindly | Clarify ownership/intent if needed |
| "Turn this into a listing image" | Any single-purpose planning mode | Platform or product image workflow |

### Focused vs Structured Planning

| Criteria | `focused_edit` | `structured_composition` |
|----------|-------------------------------|----------------------------------|
| Edit scope | Single region, localized | Multi-region or full-image overhaul |
| Product preserved? | Yes — this is the safe choice | Higher redraw risk |
| Elements modified | ≤2 | ≥3 or major composition change |
| Typical use | Background swap, scene change, single recolor, logo stamp, product-on-white | Poster with selling points, comparison grid, infographic, tech pack |

**When in doubt, use `focused_edit`**. The downside of `focused_edit` on a complex task is lower layout quality; the downside of `structured_composition` on a fidelity task is product destruction.

### Structured Composition Risk Guard

`structured_composition` is higher-risk for product-fidelity tasks because many image-to-image runtimes treat complex edits as broader redraws rather than localized edits. Use it only when the requested output genuinely needs dense layout, annotations, comparison grids, or full-image design composition.

**Default to `focused_edit`** unless the task genuinely requires complex layout:

| Scenario | Correct planning mode |
|----------|------------------|
| Background swap / scene change (product preserved) | `focused_edit` |
| Single-region edit (recolor, remove object, add logo) | `focused_edit` |
| White/light hero image from product photo | `focused_edit` |
| Platform main image (product preserved) | `focused_edit` |
| Model showcase with product | `focused_edit` |
| Localized product/package text removal | `focused_edit` via Text Editing local removal |
| Authorized watermark/contact/QR/non-product overlay removal | `watermark_removal` |
| Dense annotations / selling-point layout / comparison grid | `structured_composition` |
| Multi-region independent edits in one image | `structured_composition` |
| Full creative poster / heavy compositional redesign | `structured_composition` |
| Tech pack with dimension callouts | `structured_composition` |

**Rule of thumb**: If the product must stay unchanged, use `focused_edit`. The "complex" in the user's request description does not mean you should use `structured_composition` — a visually rich background or detailed scene is still a `focused_edit` task when the product is preserved.

If using `structured_composition` with a product reference, always enable Strict Product Fidelity Mode.

---
