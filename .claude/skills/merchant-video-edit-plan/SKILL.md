---
name: merchant-video-edit-plan
description: "Turn merchant footage and an approved script into a timecoded edit plan with deterministic asset, audio and export checks."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Video Edit Plan

## Inputs and execution modes
Require approved message, source footage/assets and rights, product facts, target duration/aspect ratio, frame rate, audio, captions and output requirements. A local editor/render tool can execute; an edit decision list is the fallback. No upstream render scripts are bundled or assumed installed.

## Timeline construction
Inventory assets with duration, frame rate, dimensions, audio and role. Keep an immutable source manifest. Build the narrative edit before visual polish: orient the shopper, demonstrate the verified product action, show supporting detail and finish with the authorized next step. Use only approved claims.

Create a timecoded scene table with source in/out, timeline start/end, crop, overlays, audio and transition. Establish timebase and distinguish seconds from frame indices; include handles for transitions without silently shortening essential actions. If rendering programmatically, use deterministic seeds/assets, explicit frame counts and locally available fonts; avoid network-dependent content during final render.

Keep product geometry, labels and sequence truthful. Sync voice and visuals against actual audio, not estimated script length. Verify every referenced file and license before render. Record partial render failures and unresolved dependencies; do not claim a video exists from a composition file alone.

## Delivery checks
Preview beginning/end, every edit boundary, key product action and full audio/captions. Inspect total duration, frame dimensions, codec/container and target-player playback. Return actual render if produced, EDL, asset manifest and verification status. Publishing or ad spend is separate.

## Script and repeatable composition mode
When the input is a factual brief rather than an approved script, first draft the full spoken/on-screen copy: hook promise, context, demonstration beats, qualified proof, offer terms and one next action. A long tutorial uses beat-level question/delivery/bridge and a final payoff matching the title; choose pacing from read-aloud timing and actual footage, never fixed retention-cliff or attention-reset claims. Mark B-roll, graphics and narration separately. Have the factual/rights owner resolve unapproved claims before treating the script as approved.

For a promotion, preserve exact dates/timezone, market, price, eligibility and address when relevant; put essential terms on screen legibly and in accompanying caption. Preview each requested aspect ratio and poster frame rather than blindly cropping. If a compatible HTML/video composition tool is available, produce the actual composition with asset paths, scenes, seek-safe animation and caption timing, then lint/preview/render before claiming outputs. Otherwise deliver script and EDL as the explicit fallback. Save reusable brand/closing-scene specifications separately from per-offer facts; old prices and dates must be revalidated for each repeat. Tool-specific runtimes and generated speech remain optional and require rights/availability checks.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-video-edit-plan&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
