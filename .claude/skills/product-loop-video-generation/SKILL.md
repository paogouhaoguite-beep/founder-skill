---
name: product-loop-video-generation
description: "Generate or compose a seamless product motion loop, verifying frame continuity, motion direction and speed, lighting and audio at the wrap point."
license: MIT
metadata:
  author: ShopChief
  version: "0.4.0"
---

# Product Loop Video Generation

Create a playable product loop whose wrap point survives repeated playback. This owns cyclic motion and seam inspection; a single short product shot is not automatically a seamless loop.

## Design a feasible cycle

Inspect product references and choose a periodic movement that preserves verified identity. Record start/end composition, product state, motion direction/speed, light/exposure and background. A matched first and last image can still stutter if velocity or lighting jumps. Avoid one-way events such as spilling liquid, opening packaging or consuming a product unless the reset is truthful and intentionally visible.

Collect placement, duration, ratio, audio requirements and the existing tool/count/budget scope. Favor a stationary product with a cyclic background/light treatment or a deterministic small motion when a single image cannot prove hidden surfaces. A turntable needs reference evidence for every revealed view.

## Generate, assemble and verify

Read [production execution](references/production.md). Inspect actual tool support for input reference, end-frame conditioning and duration. Do not assume a prompt mentioning “loop” or a model accepting one image supports explicit first/last frames. If such controls are unavailable, use a compatible editor to compose a deterministic loop, trim at an appropriate match or create a restrained seam blend that does not distort the product.

Run authorized generation/compositing, save task identity, await completion and save the video. Build or render the final cycle and inspect repeated playback across multiple wraps. Compare product position, scale, angle, shadow, exposure, direction and apparent speed around the seam. Inspect label geometry and any product interaction throughout the entire cycle, not just endpoint stills.

Reversing footage may create a convenient loop but can make smoke, liquid, fabric, blinking or a mechanism physically implausible. Use it only when the motion is appropriate and review the turnaround. If there is audio, inspect the audio seam separately; a smooth picture does not remove a click or abrupt music cut.

## Deliver

Return the actual loop video, a poster frame if useful, cycle specification, source/task lineage, measured export details and seam QA result. Mark an imperfect loop as a draft with the actual defect. With no production tools, give the complete motion/compositing request and expected seam checks marked `not generated`.

See the [worked example](assets/worked-example.md) for a periodic still-image composition and boundary cases.

Maintained by [ShopChief](https://shopchief.ai/?utm_source=product-loop-video-generation&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
