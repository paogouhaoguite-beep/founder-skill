# HD Upscale

## Routing Header

- **Load when**: user asks to upscale, sharpen, enhance clarity, restore resolution, or make an existing image clearer without content changes.
- **Do not load when**: user asks only to increase file size, convert format, resize dimensions, crop, or change visual content.
- **Merge notes**: do not treat upscale as a separate paid AI step when the user mainly wants native delivery sizing. If content edits are needed, perform content edits first and upscale only when quality is still insufficient or the user explicitly requested it.
- **Hard stop**: this scene must not remove watermarks, change backgrounds, fix layout, edit text, or alter any image content.

## Scene Description

Enhance the resolution and sharpness of an existing image without modifying its content, composition, colors, or elements.

> **Hard constraint**: This scene only enhances clarity. It does not remove watermarks, change backgrounds, adjust elements, or alter image content in any way.

## Apply Method

Use the available enhancement/editing tool with the exact source through its supported reference mechanism and a concise preservation prompt:

```text
Enhance clarity and detail only. Preserve content, composition, colors, text, layout, and identity exactly. Do not add, remove, or redesign anything.
```

Select the requested output size from the current tool's documented capabilities. Do not
assume a fixed maximum tier, a `size` argument or an `auto` value. `hd_upscale` is a planning
label, not a tool name or argument.

## Content-Type Pre-Check

Before applying the upscale plan, the Agent should assess the image content type:

| Content Type | Recommendation |
|-------------|----------------|
| Product photos, natural scenes, portraits | Proceed normally with `hd_upscale` |
| **Text-heavy images** (posters, UI screenshots, infographics, documents) | **Warn the user**: "HD upscale may cause text distortion or garbled characters on text-heavy images. Consider obtaining a higher-resolution source file or using a non-AI upscaling tool instead." |
| **File size requests** ("I need it to be 2MB", "output is too small") | **This is NOT an AI task**. Route to resize tool or quality-parameter adjustment. Increasing file size ≠ increasing visual clarity. |

## Output Size Routing

| User Request | Action |
|--------------|--------|
| "Make clearer / sharpen / restore" | Use the available enhancement/editing tool with the exact supported source reference and preservation prompt above. |
| "Generate at 1K/2K" | Map the requested dimensions to the selected tool's supported parameter values. |
| "Generate at 4K" | Use native 4K output if supported. Otherwise disclose the route's actual limit and use an available authorized upscaler when suitable; label upscaled output. |

## Notes

- **No content modification**: this scene must not change composition, colors, elements, or background — only resolution and sharpness
- **4K support depends on the runtime**: use native high-resolution generation when available; otherwise use highest supported generation followed by upscale.
