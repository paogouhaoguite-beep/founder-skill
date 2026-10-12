# Production execution

## Mechanism ledger and assembly

For each operating beat, record `source`, `precondition`, `action`, `visible result`, `shot`, and `claim allowed`. Unsupported results cannot become voice-over claims. Keep setup and reset frames where viewers need them to understand the operation.

Probe supplied clips before making an edit: orientation, variable frame rate, source in/out, usable handles and audio. Create an edit table in seconds at the final declared timebase. Sequence labels should have enough screen time to be read; actual readability depends on copy length and placement rather than an invented universal rate.

If creating a background, request an empty scene with matching perspective/light, then preserve the real mechanism footage in the composite. If occlusion, reflection or hand interaction cannot be composited convincingly, keep the authentic shot and simplify the background. A model's plausible mechanism animation is not a substitute for unavailable evidence.

Mix authorized narration against real clip timing; preserve important sounds where they convey operation. Render locally or through an available editor, then inspect step boundaries and the full video. Export a capture list for only the unresolved source shots instead of blocking unrelated valid editing.

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
