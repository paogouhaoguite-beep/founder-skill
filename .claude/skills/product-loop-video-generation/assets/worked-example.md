# Worked example: a six-second product-page loop

Synthetic fixture. The input image, editor project and exported video do not exist in this package.

## Raw input

`bottle-front.png`: merchant-owned front view of a closed opaque bottle on a transparent background. Visible front label and silhouette are approved; no back or underside reference. Request: six-second silent 1080 × 1350 loop for a product page, fixed bottle, softly moving background, one deliverable, no publication. Available fixture tools: none.

## Complete composition specification

Use the source bottle unchanged as the foreground layer. Center it with stable scale, rotation and contact shadow. Do not animate the label or bottle. Background: plain warm gray with a broad soft light gradient whose center moves on a closed horizontal path. There are no hands, liquid, particles, text or product actions.

Final timebase for this worked example: 30 frames/second, six seconds, 180 frames. At frame `i` from 0 through 179, background light center is:

```text
phase = 2 * pi * i / 180
x = 540 + 60 * sin(phase)
y = 675
light_opacity = 0.12
product_position, product_scale, product_rotation = constant
```

This is a chosen composition specification, not an API parameter set or a universal video requirement. The 180th phase endpoint is deliberately omitted: after frame 179, frame 0 is the next cyclic sample.

| Time | Background light | Product / audio |
|---|---|---|
| 00:00 | Center, moving right | Original foreground fixed; silent |
| 00:01.5 | Rightmost point, smooth direction change | Foreground fixed |
| 00:03 | Center, moving left | Foreground fixed |
| 00:04.5 | Leftmost point, smooth direction change | Foreground fixed |
| 00:06 boundary | Returns to center moving right | Wrap to first frame without extra held endpoint |

If using generation for only the background, complete prompt:

> Empty warm-gray studio background in a locked portrait composition, no objects and no text. A broad soft patch of light moves gently left and right in a closed periodic cycle while brightness and color stay constant. No camera movement, perspective change, flicker, new shadow, cut or fade to black. This background will be composited behind a stationary product. Use only the currently supported duration and reference controls; do not invent a last-frame parameter.

The deterministic editor composition is preferred here because it keeps the product entirely unchanged and the period explicit. If no editor is available, this request remains a handoff rather than an output video.

## Delivery state and seam verification

Current state: `not generated`; `not rendered`; `actual output files: none`. Intended deliverable: `bottle-loop-6s.mp4`, plus a frame-count/metadata record and seam notes. After rendering, inspect actual 180-frame delivery if the requested timebase is retained. Play the delivered encode for at least two wraps, inspect frames surrounding the wrap, confirm constant foreground and no luminance jump, and verify it contains no audio stream if silent delivery was requested.

## Acceptance scenarios

1. Editor available: execute the composition, render and inspect the delivered encode; only then report a complete seamless loop.
2. User asks for a full bottle rotation from this single front image: request additional views or retain the stated background-only motion; do not invent the back label.
3. Generator lacks end-frame input: use supported cyclic prompting and inspect its output, or the deterministic composition; never send a made-up end-frame parameter.
4. Last frame is identical to first but movement changes direction abruptly: reject the seam. Match the motion trajectory or recompose; identical endpoint pixels alone do not pass.
5. A crossfade produces two bottle edges: keep the source bottle fixed and blend only the background, then recheck the actual export.
