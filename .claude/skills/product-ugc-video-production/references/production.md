# Production execution

## Presenter and product separation

Build a narrator record: real customer / hired presenter / synthetic character, allowed statements, likeness source and voice permission. If the source is genuine customer footage, preserve its exact experience and consent boundaries; do not rewrite it into a stronger endorsement.

Define synthetic character appearance without referencing a real person's identity. Check that the chosen tool accepts the required character/reference/voice combination. Native generated audio, separate text-to-speech and lip-sync are different capabilities; never assume one implies the others. Prefer off-camera narration plus genuine product inserts when reliable lip-sync or handling is unavailable.

Each scene request should include dialogue verbatim, delivery style, framing, character continuity and what the character must not claim. Keep a transcript of the resulting audio and compare it with the approved script. An output that adds an unsupported benefit must be re-recorded or replaced, not accepted because the visual is attractive.

For a generated presenter, choose useful transparency language such as “Brand demonstration • AI presenter” when appropriate to the intended use. This is a practical disclosure draft, not a statement that it satisfies every jurisdiction or platform. Review current rules only for the publication actually requested; do not impose an unrelated legal workflow on a local asset draft.

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
