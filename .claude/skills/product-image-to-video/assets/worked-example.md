# Worked example: front-view serum bottle

This is a synthetic review fixture. The named inputs below describe hypothetical supplied files; this package contains no product photo or generated video.

## Raw input

- `bottle-front.png`: 1600 × 2000 front photograph of one opaque sage-green cylindrical bottle, white closed pump, straight black label reading “MOSS / FACE SERUM / 30 mL”. Back and bottom unseen.
- Merchant facts: the label and appearance above only. No efficacy, ingredient, leakage or pump-performance evidence.
- Request: one 5-second silent 9:16 product clip; one initial candidate and at most one revision; no store publication.
- Tool state in this fixture: no generator connected. Budget has not been used.

## Complete production request

Task: image-conditioned video. Source: `bottle-front.png`. Final target: 1080 × 1920, five seconds, silent. Keep the product front-facing for the entire shot. Do not reveal any new surface. If the selected generator cannot meet these options, report supported alternatives before changing the requested deliverable.

Prompt:

> A single sage-green serum bottle exactly matching the supplied reference stands upright on a matte warm-white surface. Preserve the white closed pump, straight silhouette, label position and all source lettering. From 0 to 5 seconds, make a very subtle straight-in camera push while the bottle remains completely stationary and front-facing. Keep the original perspective; no orbit, yaw, turntable, opening, spraying, pouring, squeezing, floating or new objects. Soft daylight stays consistent. Leave clear headroom and keep the full bottle inside frame. Add no captions, sound, people or claims. Motion is an atmospheric product presentation, not a demonstration of a product effect.

| Final time | Picture | Audio / overlay | Acceptance point |
|---|---|---|---|
| 00:00–00:01 | Front-view composition establishes full bottle | None | Label and pump match source |
| 00:01–00:04 | Small straight push; bottle stays rigid | None | No new side/back detail or warping |
| 00:04–00:05 | Movement eases to rest | None | Whole product remains visible |

If a generated label is unstable, the production fallback is a retained source-image product layer over a subtle animated background. Label this output “animated still,” not a generated orbit. Do not stretch or redraw the bottle.

## Expected delivery and current state

`status: not generated`; `task_id: none`; `saved_video: none`; `requested_candidates: 1`; `rendered_candidates: 0`. The production request and timing table above are the delivered assets. Once a tool is available, save the actual video under a fresh filename, inspect its container/duration/dimensions and compare a beginning/middle/end contact sheet plus full playback. Only then change status to `generated, accepted` or `generated, rejected`.

## Acceptance scenarios

1. Compatible tool returns a complete clip with a stable front-facing bottle: download, inspect and report the actual path and metadata; one successful generation is not evidence of ad performance.
2. User asks for a 360-degree turn from this front image: do not invent the unseen back. Request additional views or propose the defined straight push; do not silently perform an orbit.
3. Job submission times out after returning a task ID: persist the ID and resume its status. Do not submit another paid candidate while the original outcome is unknown.
4. White pump changes shape at 3 seconds: reject that candidate even if its first/last frames look correct. Reduce motion or use the source layer within remaining scope.
