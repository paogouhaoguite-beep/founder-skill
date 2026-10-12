# Worked example: fold-flat phone stand

Synthetic fixture only. The filenames and facts below are review inputs, not bundled footage or verified commercial claims.

## Raw input

- `stand-guide.pdf`: lift the back support, seat it in one of three visible notches, place the phone on the lower ledge; fold only after removing the phone.
- `open.mp4`: eight seconds of a real hand opening the stand; useful interval 00:01–00:05.
- `place.mp4`: seven seconds placing a phone; useful interval 00:02–00:06.
- `fold.mp4`: six seconds; phone already removed, useful interval 00:01–00:05.
- `stand-front.png`: graphite stand. No evidence of a charging function or load rating.
- Request: one 16-second 9:16 English demo using existing footage; optional generated room background, no new mechanism generation. One final export; no publication.
- Fixture tools: editor and generator unavailable. No render has been performed.

## Complete script and timeline

| Timeline | Source / production | Spoken and on-screen copy | Cut condition |
|---|---|---|---|
| 00:00–00:02 | Static front image, small crop-safe push | Voice: “Set up your phone stand.” On-screen: “Fold-flat phone stand” | Product stays graphite, no charging icon |
| 00:02–00:06 | `open.mp4` 00:01–00:05 | Voice: “Lift the support and seat it in a notch.” On-screen: “1. Set the support” | Keep notch contact visible |
| 00:06–00:10 | `place.mp4` 00:02–00:06 | Voice: “Rest your phone on the lower ledge.” On-screen: “2. Place your phone” | Show phone reaching its supported position |
| 00:10–00:14 | `fold.mp4` 00:01–00:05 | Voice: “Remove your phone before folding the stand flat.” On-screen: “3. Remove phone, then fold” | Do not imply folding with phone inside |
| 00:14–00:16 | Static front image | Voice: “See the stand details.” On-screen: “Explore the stand” | No unsupported offer or rating |

Full voice script: “Set up your phone stand. Lift the support and seat it in a notch. Rest your phone on the lower ledge. Remove your phone before folding the stand flat. See the stand details.” Record and measure before finalizing timing. If spoken copy does not fit naturally, shorten to “Lift the support into a notch. Place your phone on the ledge. Remove it before folding. Explore the stand.” Never accelerate the mechanism clips to force a longer narration into the cut.

Optional generation prompt, only for the opening/ending background:

> An empty warm-gray desk in soft window daylight, locked portrait framing, clear central area for a separately composited phone stand. No phone, stand, charger, hands, logo, text or moving objects. Keep perspective and light stable. This is a decorative background only.

The main action shots remain real footage. If a clean composite cannot preserve edges and contact shadows, retain their original background.

## Deliverable state

`status: edit handoff only`; `rendered_video: none`; `generated_background: none`; `voice_recording: none`. Delivered: script, source in/out table, background request and missing-tool note. On execution, save a rendered file, source manifest and caption file; report measured duration and whether the optional background was used.

## Acceptance scenarios

1. Tools available and clips match the guide: edit, narrate, render, inspect the notch/phone contact and entire playback; report a file only after it exists.
2. Guide says “three notches” but footage shows only two: flag the discrepancy and do not narrate a count until resolved. The generic “a notch” remains safe if visually true.
3. User asks to show wireless charging with no supporting evidence: omit the charging claim and request valid product documentation; do not generate a charging indicator.
4. `fold.mp4` begins with phone still on the stand: request or locate a removal shot; do not imply a safe fold while loaded.
