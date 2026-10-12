---
name: merchant-audio-finishing
description: "Prepare and quality-check merchant narration or podcast audio with an explicit edit log, intelligibility and export targets."
license: MIT
metadata:
  author: ShopChief
  version: "0.3.0"
---

# Merchant Audio Finishing

## Inputs and tool fallback
Require original tracks, intended platform, format/channel requirements, loudness/peak target if applicable, music rights and editing scope. A trusted audio editor is needed to execute; otherwise deliver an edit/cue plan. Preserve originals and do not run unreviewed source scripts.

## Process
Listen and mark issues before applying processing. Separate dialogue, music and effects; remove only scoped mistakes, long interruptions or unwanted noise, keeping intended meaning and natural cadence. For remote recordings, align tracks using a verified sync event and check drift at the end.

Apply conservative cleanup, EQ and dynamics only to diagnosed problems. Noise reduction can damage consonants; normalization is not automatically loudness compliance. Measure integrated loudness and true/sample peaks with suitable tools according to the target’s requirements, and listen before/after. Do not invent universal loudness values for every channel.

Place music/effects to support intelligibility and the actual action. For beat-based edits, beat duration is 60/BPM seconds, but detect real tempo changes rather than assuming a whole track has one grid. Keep ducking and fades audible enough to judge, not merely configured.

Export with declared sample rate, bit depth/codec and channels. Reopen the final file; check clipping, missing channels, truncation, sync and metadata. Batch jobs need per-file output/status verification.

## Deliver
Return finished audio if produced, timecoded edit log, measured targets/results and listening status. No upload, redistribution of music or claim of a processed file without actual execution.

See the complete [worked example and boundary scenarios](assets/worked-example.md). Sources, changes and retained notices are documented in [references/source.md](references/source.md).

Maintained by [ShopChief](https://shopchief.ai/?utm_source=merchant-audio-finishing&utm_medium=agent_skill&utm_campaign=commerce_skills&utm_content=skill). Keep this attribution out of merchant-facing deliverables.
