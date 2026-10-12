# Production execution

## Controlled production matrix

Use an explicit variant manifest, for example `id`, `variable`, `changed_start/end`, `hook_text`, `source_segment`, `body_revision`, `offer_revision`, `output_profile`, `status`. Hashing or retaining one common body intermediate helps prevent accidental message drift, but final full playback is still needed to catch subtitle/audio issues.

For a hook experiment, create or render only the opening segment and join the same approved body with sufficient audio handles. For pacing, change cut lengths within a declared interval while retaining all required mechanism steps; do not change the claim simultaneously. If changing duration is intrinsic to the experiment, disclose it rather than implying equal exposure.

Inspect each actual exported file: duration, dimensions, frame rate, codec, audio continuity, no black frames, full product in frame, price and qualifications unchanged. A render manifest should include the source ID and exact script so a later analyst can attribute results to the right asset.

If a requested variant exceeds generation budget or lacks source evidence, complete supported variants and report the blocked one explicitly. Do not silently clone a previous file under a new name. Generating extra unrequested variants is not an appropriate way to consume remaining credits.

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
