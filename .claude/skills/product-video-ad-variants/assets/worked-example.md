# Worked example: two hooks, one fixed pouch demonstration

Synthetic review fixture; no advertisement has run and no video file has been rendered.

## Raw input

Product: Pouch One with one main compartment and a detachable wrist strap. No price promotion. CTA destination supplied by merchant as the product-detail page; this fixture contains no live tracking URL.

Approved assets: `hero.png`; `open.mp4` useful span 00:01–00:05; `strap.mp4` useful span 00:02–00:06; `pack.mp4` useful span 00:01–00:04. Brand owns these hypothetical clips. Request: two 15-second silent 9:16 exports, compare hook wording only, no ad publishing. Existing editing tools unavailable in fixture.

## Test definition and full scripts

Hypothesis: task-led versus feature-led opening wording may affect initial attention. Outcome unknown. Primary variable: on-screen wording during first three seconds. Picture, timing, typography, music policy, body copy and CTA fixed.

| ID | 00:00–00:03 hook | Fixed offer | Status |
|---|---|---|---|
| A-task | “Keep the small things together.” | No promotional offer | Not rendered |
| B-feature | “One pouch. A detachable strap.” | No promotional offer | Not rendered |

| Final time | Picture / source | On-screen script |
|---|---|---|
| 00:00–00:03 | `hero.png`, identical gentle crop-safe push in A and B | Hook A or Hook B only |
| 00:03–00:07 | `open.mp4` 00:01–00:05 | “One main compartment” |
| 00:07–00:11 | `strap.mp4` 00:02–00:06 | “Detachable wrist strap” |
| 00:11–00:14 | `pack.mp4` 00:01–00:04 | “For your small essentials” |
| 00:14–00:15 | Same final product frame | “Explore Pouch One” |

No voice-over, music or generated model performance required. Complete rendering request: preserve these five timeline intervals, use one consistent product-safe text layout, identical 1080 × 1920 final frame and the editor's verified compatible MP4 export profile. Save `pouch-hook-A-task.mp4` and `pouch-hook-B-feature.mp4` separately. If one second is too short for the final CTA in the chosen placement, adjust both versions identically and record the common timeline revision before rendering.

## Output record

Current deliverables: the two complete on-screen scripts, common edit table and variant manifest. `rendered_count: 0`; `published_count: 0`; `test_results: none`. On execution, render both, confirm the body matches from 00:03 onward and check complete playback. Report actual file paths and metadata. Do not mark one “winning”.

## Acceptance scenarios

1. Editor available and assets verified: render both variants and inspect equal duration, fixed body and only the intended opening-copy change.
2. Variant B accidentally gains “Waterproof” text: reject; waterproofing is neither supplied fact nor the chosen variable.
3. User requests ten variants but authorizes only two new generated scenes: build reusable edits within scope or state the exact blocked remainder; do not launch ten paid generations.
4. An output file exists but has a frozen black body section: mark that variant rejected, repair and re-export before claiming the pair complete.
