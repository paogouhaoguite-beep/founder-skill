# Production execution

## Single-image execution detail

Create a manifest with source filename/hash, visible-view description, locked identity features, allowed motion, one final-use ratio and requested final duration. Keep the full original; prepare a crop only after checking product margins. An image input may be a URL, uploaded asset or another provider-specific object; never treat a local path as a provider-accessible URL.

A tool-neutral request contains: source reference, task `image-conditioned video`, approved motion prompt, desired duration/ratio, candidate limit, audio policy and identity checks. Translate it into the *observed* tool schema, not an assumed JSON endpoint. If a provider has no supported duration matching the requested final cut, choose a supported duration within budget and trim only after preserving the intended motion; report that difference.

For tiny labels, avoid promising exact generated lettering. Keep the product rigid using an actual still layer where an editor can preserve it, reduce motion, or reject the generated candidate. Frame sampling alone does not prove absence of flicker: play the complete short clip before acceptance.

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
