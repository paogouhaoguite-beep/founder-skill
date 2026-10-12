---
name: merchant-caption-timing
description: "Create and validate time-aligned captions for merchant video while preserving spoken meaning and readable segmentation."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Caption Timing

## Inputs
Collect actual audio/video, transcript if available, language, delivery format and target player. Caption tools are optional; without audio access, deliver untimed caption text and mark timing not verified. A script is not proof of what was spoken.

## Caption construction
Transcribe or verify against actual audio first, including relevant non-speech information and speaker changes where appropriate. Preserve claims, numbers and negation. Split cues at semantic boundaries rather than arbitrary character counts, using the target format’s requirements and actual reading context.

Set cue start/end from audible speech, with no negative durations or accidental overlap unless intentionally supported. Check frame/timebase rounding and cue order. Avoid covering essential product details or existing text; placement and safe areas depend on the actual player.

Play through the final asset with captions enabled. Check word accuracy, sync, reading time, punctuation, line wrapping, speaker identification and sound descriptions. Inspect at intended mobile size and verify the exported SRT/VTT parses. Keep a source transcript and revision log.

## Deliver
Return caption file if generated, transcript, uncertainty list and playback QA status. Do not claim captions are accurate from script matching alone or overwrite live captions without scope.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-caption-timing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
