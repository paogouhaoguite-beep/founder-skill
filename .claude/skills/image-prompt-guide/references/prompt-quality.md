## Prompt Construction

### Generation Prompt Formula

```
[Shot type] of [Subject] in [Setting], [Action/State].
[Style], [Composition], [Lighting], [Color palette], [Quality].
```

| Element | Description | Examples |
|---------|-------------|----------|
| Subject | What to depict (be specific) | "ginger tabby cat", "ergonomic wireless headphones" |
| Setting | Environment/location | "windowsill with afternoon sunlight", "minimalist studio" |
| Style | Overall aesthetic | "cinematic", "watercolor", "flat vector" |
| Composition | Camera/framing | "close-up", "wide-angle", "rule-of-thirds" |
| Lighting | Light source and mood | "golden hour", "soft diffused", "Rembrandt lighting" |
| Color | Palette direction | "Morandi palette", "high saturation", "monochromatic" |
| Quality | Detail level | "8K", "hyperrealistic", "sharp detail" |

For text in images, use explicit quotes: `Display "LIMITED EDITION" in bold serif font`.

### Editing Prompt Formula

```
[Edit instruction targeting specific area].
[Preservation clause (concise, ≤3 lines)].
```

**Preservation clause template** (append to every edit prompt):

```
Keep the product exactly unchanged — preserve geometry, color, texture, labels, and camera angle.
Only change: [specific allowed changes].
Do not redraw, simplify, or invent any product detail.
```

Keep it concise. Long enumeration lists (20+ protected items) do not improve compliance and may reduce model execution quality. The model responds better to clear, short constraints than to exhaustive lists.

**Example — Scene change**:
```
Place the product on a modern kitchen countertop with warm morning light.
Keep the product exactly unchanged — preserve geometry, color, texture, labels, and camera angle.
Only change: background/scene.
Do not redraw, simplify, or invent any product detail.
```

---


## Result Check

After receiving a generation or editing result:

1. **Preservation audit**: Compare the result against the preservation clause. If the model altered protected elements (product shape distorted, text removed, colors shifted), retry with a stronger constraint — e.g., add "CRITICAL:" prefix, list each protected element individually, or reduce edit scope.
2. **Intent completeness**: Verify all user-requested changes are present. If a sub-task from Step 4 was missed, execute the remaining sub-tasks on the current output.
3. **Quality gate**: If the result is clearly unusable (heavy artifacts, wrong subject, garbled text), inform the user and offer to retry with adjusted parameters (e.g., switch `focused_edit` → `structured_composition`, or simplify the prompt).

Hard failure conditions:
- Product shape, structure, SKU color/pattern, packaging text, logo, handle, seam, hole, accessory, or camera angle changed when not requested
- A crop/split/resize/format task was handled by generating a new product image
- Multi-image or multi-SKU output count does not match the requested/confirmed count
- White-background output changes the product or leaves damaged/blurred edges
- Text editing/removal causes garbled text, misspellings, or modifies unspecified text
- Platform hero image includes prohibited overlays, watermarks, contact information, or unsupported claims
- User requested "do not change the product" but the result redraws or reimagines the product

### Scene Acceptance Criteria

| Scene | Acceptance Criteria |
|-------|---------------------|
| White Background | Background is pure white or near #FFFFFF; product shape unchanged; edges clean |
| HD Upscale | More detail without changing identity, color, text, or layout |
| Watermark / Element Removal | Removed target element only; no damage to product or surrounding content |
| Text Editing | Exact requested text; readable; no garbled characters |
| Product Cleanup | Product identity preserved; lighting/background improved; no invented claims |
| Selling Point Image | No fabricated claims; labels readable; text does not cover product |
| Platform Hero | Meets platform background, text, watermark, ratio, and product coverage rules |
| Logo Design | Original, legible, commercially safe, not similar to known trademarks |

> Do NOT silently retry indefinitely. After 2 failed attempts at the same task, inform the user of the limitation and suggest alternatives.

---
