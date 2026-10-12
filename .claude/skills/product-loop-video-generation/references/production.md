# Production execution

## A loop is a temporal boundary condition

Use a timeline with declared frame rate `F`, intended duration `T` and integer output frames `N = F × T` when those values are exact. For a deterministic cyclic effect, sample frames `i = 0 … N−1` at phase `2πi/N`; do not append the phase-2π duplicate frame, which can create an extra hold on each wrap. The last and first frames need to be the next adjacent phase, not identical duplicate stills.

For generator-produced motion, request cyclic movement consistent with its actual controls. Inspect whether the returned clip contains a hold or a drift rather than assuming requested endpoints were honored. Trim only with evidence of a stable matching cycle. A crossfade can hide a luminance change while creating two bottles; inspect the overlap itself. Prefer a fixed source product layer if identity cannot survive the blend.

Create a seam review by playing at least two consecutive cycles, then scrubbing several frames before and after the join. Inspect position/velocity as well as brightness. Choose acceptance tolerance according to the placement and visible motion; there is no universal pixel score that proves a good loop. If audio is included, decode and listen over the wrap and adjust at an appropriate continuous point without removing product-relevant sound.

Probe the actual exported file after encoding; format conversion or frame-rate changes can introduce duplicate frames. Repeat the seam preview with that delivered encode, not just with the editor's timeline.

## Tool capability and execution record

These are original production instructions, not an SDK integration or a promise that a generator is installed. Inspect the tools actually available, their input schema, authentication state, output access and current provider documentation. Match the requested media operation to observed support: image conditioning, speech, lip-sync, frame controls, editing and rendering are separate capabilities. Use the user's chosen provider where it can satisfy the task; do not silently replace it.

Before a paid request, retain the existing authorized quantity and budget in the production manifest. When the user already authorized the operation, proceed within those limits. If essential pricing or a maximum cost is genuinely unknown, clarify that missing boundary rather than inventing a price. A failed or rejected candidate can still consume provider credits. Do not generate extra assets merely because the tool supports batching.

For an asynchronous generation: save the task/operation identifier as soon as it exists; record the source references, request, candidate number and creation time without credentials. Await/poll through the provider's supported status mechanism and reasonable polling cadence. A client timeout means unknown outcome unless the provider confirms otherwise. Resume the same identifier; do not blindly resubmit or spend another credit. If the creation response was lost before an ID was received, use supported request/task history or idempotency recovery where available. Otherwise report unresolved submission and stop further paid retries until the original status can be established. Keep partial outputs and explicit per-task states.

When a task succeeds, use the available authorized save/download path, record its local artifact or durable output reference and inspect the bytes. A successful API state alone does not prove a playable, correct video. Do not expose credentials or signed asset URLs in public manifests.

## Media checks when local tools are available

Use the actual editor/exporter available in the environment. For a local video, `ffprobe` can inspect container metadata without modifying the file:

```sh
ffprobe -v error -show_entries format=duration:stream=index,codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels -of json output.mp4
```

`output.mp4` is a user-created output path placeholder, not a bundled file. Confirm the program is installed before invoking it. Inspect decoded frames or use a compatible player and listen to audio. Metadata inspection is not visual QA. A composition/project file is not a video export. If no preview capability exists, report the file as rendered but visually unverified rather than claiming acceptance.

Use specific statuses such as `not generated`, `submitted`, `running`, `failed`, `generated but rejected`, `rendered but unverified` and `accepted`. Deliver the full prompt/script and source-bound specifications for blocked work so it can be resumed; mark media absent where no file was produced. Asset creation does not include publishing, ad activation or uploading unrelated private files.

## Current primary references

Capability entry points checked on 2026-10-05:

- [Google video generation documentation](https://ai.google.dev/gemini-api/docs/video): select the current supported video workflow and verify model-specific options at execution time.
- [Runway API getting started](https://docs.dev.runwayml.com/guides/using-the-api/): asynchronous creation returns task information; use the documented completion/status workflow and output retrieval.

These links guide fresh capability checks. No copied provider code, fixed model ID, pricing or undocumented endpoint contract is bundled here.
