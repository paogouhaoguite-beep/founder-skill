## Request Processing Pipeline

Process every request through these steps in order:

### Step 0 — Image Intake

If the user provides one or more images, inspect the image before routing.

Identify:
- Main subject
- Elements that must be preserved
- Visible text, logos, labels, watermarks
- Current aspect ratio
- Quality issues such as blur, low resolution, artifacts, occlusion
- Whether the image appears to be a product photo, poster, document, logo, model photo, or scene photo

Use this intake result to build preservation clauses and choose routing.
Never infer hidden or occluded product details.

### Step 0.5 — Reference Image Preflight

Choose the generation/editing tool actually available in this host and inspect its schema
before preparing a call. The reference mechanism and limits are runtime-specific.

1. **Use the exact intended image**: map each inspected source to a stable attachment,
   asset ID, local file path or provider-readable URL supported by that tool. For prior
   generated results, select the exact artifact requested rather than the latest image.
2. **Validate reference access**: a browser display URL, `blob:` URL or expired signed URL
   may not be readable by the provider. Use the supported file/reference mechanism and
   preserve the current account/workspace boundary; do not substitute another user's asset.
3. **Validate the actual image bytes**: check accepted formats, file size, pixel dimensions
   and reference-count limits from the selected tool. Convert or downsize a copy only when
   that route requires it, retaining the original.
4. **Use local paths when supported**: do not upload solely to satisfy a historical adapter.
   If a provider requires an upload, use the authorized destination and returned reference;
   do not expose private files through a public URL just to make them reachable.
5. **Pass references explicitly for edits**: use only the intended sources through the
   documented reference field or attachment selector. Do not assume omitted fields or
   empty lists have a particular meaning. Text-to-image must not silently replace an edit.
6. **Resolve reference errors before retrying**: use the actual returned error and provider
   documentation. Repair missing access, unsupported format or size, or a stale reference
   without guessing another image. Reconcile any uncertain job before a paid retry.

Inspect image contents only when the conversation model actually received the image as vision
input. A text-only model may forward an explicit stable reference but must not claim it saw the
image.

### Step 1 — Outcome Intent First

Before choosing any `planning mode`, identify the user's desired final outcome.

Classify the request by outcome intent first:

| Intent | Meaning |
|--------|---------|
| `platform_main_image` | Platform-ready hero/main product image |
| `platform_image_set` | Multi-image set for a listing |
| `product_cleanup` | Cleaner, more professional product photo |
| `background_replacement` | Change or replace background |
| `text_removal` | Remove specified text, ownership overlays, or visual clutter with the correct safety route |
| `text_replacement` | Replace or translate text in image |
| `selling_point_image` | Marketing layout with copy/callouts |
| `logo_design` | Create a new logo from scratch |
| `logo_customization` | Apply existing logo to product/material |
| `upscale_or_restore` | Improve clarity/resolution |
| `native_delivery` | Resize, crop, compress, convert format |

The planning mode organizes the prompt; it is not a tool argument and must not replace outcome-intent analysis.

### Step 2 — Non-AI Task Interception

Before invoking any AI image tool, check whether the request is a non-AI operation. If the user's core intent is to change the image's **size, file weight, format, or orientation** without altering content, route to native (non-AI) tools instead.

| Signal | Action |
|--------|--------|
| Crop / trim / cut to dimensions (not SKU asset creation) | Use crop/resize tool |
| Compress / reduce file size / "under X MB" | Use compress tool |
| Resize to WxH / change dimensions | Use resize tool |
| Format convert (PNG/JPG/WebP) | Use format_convert tool |
| Rotate / flip | Use transform tool |

**Key indicator**: phrases like "keep everything else unchanged", "just resize", explicit pixel dimensions with no content change, or file-size constraints ("under 2MB") strongly signal non-AI tasks.

SKU-related requests such as "split into SKU images" or "make each SKU into a listing image" must go through Step 2.5 before deciding native vs AI.

**Mixed requests**:
- Content-changing AI operations usually run first.
- Final delivery operations such as resize, crop, compress, and format conversion usually run last.
- Only run crop/resize first when the user explicitly requires a fixed canvas before editing.

> If the Agent toolset lacks a dedicated resize/compress tool, inform the user that this operation is not supported by the AI image tools and suggest alternatives.

### Step 2.5 — SKU Asset Workflow

SKU requests are not always native-only. First classify the user's SKU intent before selecting tools.

| SKU Intent | User Signals | Route |
|------------|--------------|-------|
| **Extract existing SKUs** | "split/crop/separate each SKU", "do not change products", "export each visible style" | Use native crop/segmentation/background removal first. Do not redraw products. |
| **Standardize SKU listing images** | "make each SKU into a listing/main image", "white background SKU images", "Alibaba SKU images", "same style/composition for each SKU" | First isolate each visible SKU, then use the available image-generation/editing tool per SKU with strict product fidelity. Final resize/format is native. |
| **Generate SKU variants** | "generate colors/styles", "create red/blue/green variants", "make more SKU options" | Use the available image-generation/editing tool with SKU Color Change when a reference exists; use generation only when the user explicitly asks for new variants. |

Rules:
- Never invent SKU count, colors, materials, or variants unless the user explicitly requested them.
- For batch SKU work, first identify the expected output count. If the count is unclear or visual separation is ambiguous, ask for confirmation.
- For listing-ready SKU images, output one image per SKU. Do not satisfy a multi-SKU request with one combined image.
- Preserve each SKU's exact color, pattern, shape, material, labels, accessories, and visible details.
- Use AI only for listing standardization or requested variant generation; use native tools for pure extraction/crop/format delivery.

### Step 3 — Ambiguity Check

Evaluate whether the request contains enough information to proceed:

| Ambiguity Signal | Action |
|------------------|--------|
| No actionable verb ("edit this", "process these") | Ask what specific changes are needed |
| Safe default subjective requests ("make it cleaner / more professional / optimize") | Proceed with conservative visual cleanup; ask only if the desired outcome is unclear or risky |
| Context-only reply ("yes", "right", "go ahead") with no prior clear instruction | Ask what the user would like done |
| Folder/batch reference without per-image instructions | List files and ask what operation to apply |

| Ambiguity Type | Examples | Action |
|----------------|----------|--------|
| Blocking ambiguity | "edit this", "process these", folder with no operation | Ask user |
| Safe default ambiguity | "make it more professional", "optimize product image", "make it cleaner" | Proceed with safe visual defaults |

Safe visual defaults include cleaner background, balanced composition, soft natural lighting, sharper product presentation, corrected product centering, and preservation of product identity.

Do not add new claims, text, logos, certifications, dimensions, materials, or product features unless the user provides them.

Ask the user with specific, selectable options when the host provides a prompt UI; otherwise ask a concise plain-language question (e.g., "What would you like to do: change background, remove watermark, adjust colors, add text, or something else?").

### Step 4 — Multi-Intent Execution Planner

If the request contains **2 or more intents** (including mixed AI + non-AI), plan by output image and minimize AI calls. Decomposition is for reasoning; it does not automatically mean sequential execution.

1. **Identify** all requested intents and the expected output count.
2. **Separate native delivery intents**: resize, crop, compress, rotate, and format conversion should usually run last with native tools and should not trigger an AI call.
3. **Group AI intents by output image**: if several visual changes belong to the same final image, merge them into one prompt when the tool can satisfy them together.
4. **Load references for every matched scene** using the Reference Loading Contract.
5. **Choose execution mode**:
   - `single_purpose`: only when the request exactly matches one dedicated task and no other visual/layout/platform changes are needed.
   - `merged_simple`: one `focused_edit` call for compatible product-fidelity edits such as scene/background, white/light hero styling, centering, shadow, lighting cleanup, local cleanup, logo placement, or product color change.
   - `merged_complex`: one `structured_composition` call for dense layouts, selling-point images, comparison grids, tech packs, or multi-region visual design in a single output.
   - `true_sequential`: only when a previous output is required before the next step, when tool limitations force it, or when the user explicitly requests separate intermediate outputs.
6. **Execute the minimum number of AI calls needed** for the requested output count, then apply native delivery operations last.
7. **Aggregate** results and state any skipped or native-only operations.

**Cost guard**:
- Prefer one AI call per requested output image.
- Do not multiply calls by the number of detected intents when the intents can be expressed in one prompt.
- If a plan would require more AI calls than the requested output count, compress the plan first; ask or explain only when compression would reduce quality or violate safety/tool constraints.
- Platform image sets and SKU batches may require multiple calls because the user expects multiple output images, but each output should still use the fewest feasible calls.

**Merge examples**:

| Request | Preferred Execution |
|---------|---------------------|
| "Make an Amazon main image with white background, centered product, natural shadow" | Load Platform + White Background, then one `focused_edit` call |
| "Remove small clutter, change to white background, and improve lighting" | Load relevant references, then one `focused_edit` call unless clutter is a complex authorized watermark |
| "Change product to red and put it on a gray studio background" | Load SKU Color Change + Scene Image, then one `focused_edit` call |
| "Add my logo and make it a clean listing hero" | Load Logo Customization + Platform/White Background if relevant, then one `focused_edit` call |
| "Create 5 Alibaba listing images" | One planned call per requested output image, not one call per sub-intent inside each image |

Use `true_sequential` for cases such as isolating each SKU before standardization, removing a dense watermark before a high-fidelity edit, or generating separate tech-pack drawings requested as distinct outputs.

### Step 5 — Scene Routing

Match the request against the Scene Router below (Priority 1 → 4). Use the first matching priority level.

---
