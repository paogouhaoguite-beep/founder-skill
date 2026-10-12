---
name: product-image-to-video
description: "Generate and verify a short product video from an approved product image, preserving visible identity and limiting motion to supported views."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Image to Video

Turn a product still into an actual short motion asset when a compatible generator is available. This owns single-image execution and output inspection, rather than a multi-shot motion brief.

## Inputs and shot boundary

Read the source image before writing a prompt. Collect the intended placement, duration, aspect ratio, permitted motion, product facts and existing generation budget/count. Record which product surfaces the image actually proves. A front view does not establish the back, underside, interior or opening mechanism. Prefer a locked product with background/light movement or a small crop-safe camera move when those views are missing.

Preserve packaging, label wording, silhouette, material, color, closures and count. Do not animate liquid, heat, waterproofing, durability or mechanical operation without supporting evidence. A camera move must not reveal undocumented geometry. Establish one action, one camera behavior and a stable background; leave graphics for deterministic editing if exact typography matters.

## Produce the asset

Read [production execution](references/production.md) when selecting or calling tools. Inspect the available tool schema and current provider documentation for image conditioning, accepted duration/ratio and upload rules. Use an already authorized tool and count/budget without reconfirming routine execution. Submit a bounded candidate, save its task identity and await completion; resume the same task after an uncertain timeout.

For an authorized Runway account without an installed connector, the bundled [command-line helper](scripts/runway_video.py) provides `submit`, `status` and `download`. Read [setup and exact commands](references/runway-cli.md). Submission is an offline dry run unless `--execute` is supplied; pass the user's generation scope through to execution. The helper uses Python 3.10+ and an environment API key, never keys in prompts or files. An existing receipt blocks repeated submission; an unknown result must be reconciled before retrying.

Download/save completed output through the available authorized mechanism. Inspect the complete clip, including beginning, midpoint, end and the frames where movement exposes new detail. Compare directly with the source: labels, edges, count, shadows, reflections and product-to-background scale. Reject distorted logos, added seams, shape changes or invented surfaces. Revise the specific motion defect within the remaining budget; do not solve it by accepting an inaccurate SKU.

A conventional image pan/zoom is a useful alternative if it meets the user's request, but label it as an animated still. Never present it as generated 3D rotation. Without a compatible generator, deliver the complete source-bound prompt and request specification, explicitly `not generated`.

## Deliver

Return the saved video and poster frame if produced, source/prompt manifest, requested versus actual dimensions/duration, task/output status and visual acceptance notes. Separate a playable file from a rejected candidate or a prompt-only handoff. Publication is outside a request to create an asset.

Use the [worked example](assets/worked-example.md) for a single-view prompt, shot timing and failure decisions.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-image-to-video&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
