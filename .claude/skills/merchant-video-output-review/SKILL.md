---
name: merchant-video-output-review
description: "Review merchant video or animation exports for product truth, readability, motion, accessibility and placement fit."
license: Apache-2.0
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Video Output Review

## Inputs and tools
Require actual video/animation, product references, approved copy, target placement specs and intended audio/captions. Playback/frame inspection is needed for execution; without media access produce an explicit review checklist marked not run. Do not infer full-video quality from a thumbnail.

## Review passes
Watch the complete asset at normal speed, then inspect critical frames and transitions. Check product geometry/labels, visual continuity, claims, hand/object anomalies and text accuracy. Log timestamped evidence and distinguish severe product misrepresentation from cosmetic issues.

Inspect text dwell and motion at intended size. Animate for hierarchy and comprehension rather than movement alone; avoid excessive flashing and honor applicable reduced-motion requirements in interactive contexts. Verify contrast against real frames and check banding, clipping and encode artifacts.

For aspect-ratio adaptation, choose crop, re-layout or padding based on protected content. Track subjects only when it preserves the actual product/action. Verify safe areas using current destination requirements. For looping GIF/animations, inspect loop seams, palette changes, frame timing, file size and readability; compression is not allowed to obscure facts.

Check audio intelligibility, clipping, sync and captions, plus first/last frame and actual player behavior. A successful encoder exit is not sufficient acceptance.

## Deliver
Return pass/fail/unknown by criterion, timestamp/frame issue register, proposed repair and export manifest. Do not publish a failed asset or claim conversion impact from visual review.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-video-output-review&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
