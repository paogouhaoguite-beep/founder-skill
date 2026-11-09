// The model catalog. Every tool page, the server-side validation and the
// fal.ai request mapping come from here. Field names and enums follow each
// endpoint's published schema (https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=...),
// checked 2026-11-09. To add a model, add an entry; nothing else needs changing.

export type ToolId =
  | "image" | "video" | "edit" | "character" | "upscale"
  | "lipsync" | "audio" | "faceswap";
export type Output = "image" | "video" | "audio";
export type Value = string | number | boolean | string[];
export type Values = Record<string, Value | undefined>;

export type Field =
  | { kind: "prompt"; key: string; label: string; placeholder?: string; required?: boolean }
  | { kind: "image"; key: string; label: string; required?: boolean; hint?: string }
  | { kind: "images"; key: string; label: string; max: number; required?: boolean; hint?: string }
  | { kind: "mask"; key: string; label: string; imageKey: string }
  | { kind: "video"; key: string; label: string; required?: boolean }
  | { kind: "audio"; key: string; label: string; required?: boolean }
  | { kind: "select"; key: string; label: string; options: string[]; default: string }
  | { kind: "count"; key: string; label: string; max: number; default: number }
  | { kind: "toggle"; key: string; label: string; default: boolean }
  | { kind: "consent"; key: string; label: string }
  | { kind: "preset"; key: string; label: string };

export interface ModelDef {
  id: string;
  tool: ToolId;
  name: string;
  tagline: string;
  output: Output;
  fields: Field[];
  /** every endpoint this model can call (used to validate status checks) */
  endpoints: string[];
  endpoint: (v: Values) => string;
  toInput: (v: Values) => Record<string, unknown>;
}

export interface ToolDef {
  id: ToolId;
  name: string;
  blurb: string;
  group: "Create" | "Edit";
}

export const TOOLS: ToolDef[] = [
  { id: "image", name: "Image", blurb: "Text-to-image across six models", group: "Create" },
  { id: "video", name: "Video", blurb: "Text or image to video, with camera presets", group: "Create" },
  { id: "audio", name: "Audio", blurb: "Voiceover, music, sound effects, and sound for silent video", group: "Create" },
  { id: "character", name: "Character", blurb: "Keep the same person or mascot across new scenes", group: "Create" },
  { id: "edit", name: "Edit", blurb: "Change an image with words, combine images, or repaint an area", group: "Edit" },
  { id: "upscale", name: "Upscale", blurb: "Sharpen and enlarge images and video", group: "Edit" },
  { id: "lipsync", name: "Lipsync", blurb: "Make a video or a photo speak any audio", group: "Edit" },
  { id: "faceswap", name: "Face Swap", blurb: "Swap a face between two photos, with consent", group: "Edit" },
];

// ---------- shared field helpers ----------

const prompt = (placeholder: string, label = "Prompt"): Field =>
  ({ kind: "prompt", key: "prompt", label, placeholder, required: true });
const aspect = (options: string[], def = options[0]): Field =>
  ({ kind: "select", key: "aspect", label: "Aspect ratio", options, default: def });
const count = (max = 4, def = 2): Field => ({ kind: "count", key: "count", label: "Images", max, default: def });
const startFrame: Field = { kind: "image", key: "image", label: "Start frame (optional)", hint: "Upload to animate an image" };
const preset: Field = { kind: "preset", key: "preset", label: "Camera & motion preset" };

const s = (v: Values, k: string) => (typeof v[k] === "string" ? (v[k] as string) : "");
const n = (v: Values, k: string, d: number) => (typeof v[k] === "number" ? (v[k] as number) : Number(v[k]) || d);
const ifSet = (key: string, value: unknown) => (value ? { [key]: value } : {});

/** Prompt plus the selected motion preset's camera instruction. */
export const withPreset = (v: Values, presetPrompt?: string) =>
  [s(v, "prompt").trim(), presetPrompt?.trim()].filter(Boolean).join(". ");

const sizeName: Record<string, string> = {
  "1:1": "square_hd", "4:3": "landscape_4_3", "3:4": "portrait_4_3",
  "16:9": "landscape_16_9", "9:16": "portrait_16_9",
};
const SIZE_ASPECTS = Object.keys(sizeName);

const IMG_ASPECTS = ["1:1", "4:3", "3:4", "16:9", "9:16", "21:9"];
const VOICES = ["Rachel", "Aria", "Sarah", "Laura", "Charlotte", "Alice", "Matilda", "Jessica", "Lily",
  "Roger", "Charlie", "George", "Callum", "River", "Liam", "Will", "Eric", "Chris", "Brian", "Daniel", "Bill"];

// `P` is filled in on the server with the expanded prompt (prompt + preset).
type Mapper = (v: Values, P: string) => Record<string, unknown>;
const m = (def: Omit<ModelDef, "toInput"> & { map: Mapper }): ModelDef => ({
  ...def,
  toInput: (v) => def.map(v, s(v, "_prompt") || s(v, "prompt")),
});

export const MODELS: ModelDef[] = [
  // ---------------- Image ----------------
  m({
    id: "nano-banana", tool: "image", name: "Nano Banana", tagline: "Google's fast, prompt-faithful image model", output: "image",
    fields: [prompt("A cozy reading nook in a treehouse, morning light"), aspect(["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3", "21:9"]), count()],
    endpoints: ["fal-ai/nano-banana"], endpoint: () => "fal-ai/nano-banana",
    map: (v, P) => ({ prompt: P, aspect_ratio: s(v, "aspect"), num_images: n(v, "count", 1) }),
  }),
  m({
    id: "seedream", tool: "image", name: "Seedream 4", tagline: "Detailed, high-resolution stills", output: "image",
    fields: [prompt("Macro shot of a dew-covered beetle, studio lighting"), aspect(SIZE_ASPECTS), count()],
    endpoints: ["fal-ai/bytedance/seedream/v4/text-to-image"], endpoint: () => "fal-ai/bytedance/seedream/v4/text-to-image",
    map: (v, P) => ({ prompt: P, image_size: sizeName[s(v, "aspect")], num_images: n(v, "count", 1) }),
  }),
  m({
    id: "flux-ultra", tool: "image", name: "Flux Pro Ultra", tagline: "Photoreal 2K images", output: "image",
    fields: [prompt("Portrait of an old fisherman, overcast light, 85mm"), aspect(IMG_ASPECTS), count(),
      { kind: "toggle", key: "raw", label: "Raw (more natural, less polished)", default: false }],
    endpoints: ["fal-ai/flux-pro/v1.1-ultra"], endpoint: () => "fal-ai/flux-pro/v1.1-ultra",
    map: (v, P) => ({ prompt: P, aspect_ratio: s(v, "aspect"), num_images: n(v, "count", 1), raw: Boolean(v.raw) }),
  }),
  m({
    id: "flux-dev", tool: "image", name: "Flux Dev", tagline: "Fast and versatile", output: "image",
    fields: [prompt("A lighthouse on a cliff at dusk, volumetric fog"), aspect(SIZE_ASPECTS), count()],
    endpoints: ["fal-ai/flux/dev"], endpoint: () => "fal-ai/flux/dev",
    map: (v, P) => ({ prompt: P, image_size: sizeName[s(v, "aspect")], num_images: n(v, "count", 1) }),
  }),
  m({
    id: "ideogram", tool: "image", name: "Ideogram 3", tagline: "Best at text, logos and posters", output: "image",
    fields: [prompt('A retro concert poster that says "NIGHT SWIM"'), aspect(SIZE_ASPECTS),
      { kind: "select", key: "style", label: "Style", options: ["AUTO", "GENERAL", "REALISTIC", "DESIGN"], default: "AUTO" }, count()],
    endpoints: ["fal-ai/ideogram/v3"], endpoint: () => "fal-ai/ideogram/v3",
    map: (v, P) => ({ prompt: P, image_size: sizeName[s(v, "aspect")], style: s(v, "style"), num_images: n(v, "count", 1) }),
  }),
  m({
    id: "wan-image", tool: "image", name: "Wan 2.2", tagline: "Open model with a cinematic look", output: "image",
    fields: [prompt("Neon street market in the rain, wide shot"), aspect(SIZE_ASPECTS)],
    endpoints: ["fal-ai/wan/v2.2-a14b/text-to-image"], endpoint: () => "fal-ai/wan/v2.2-a14b/text-to-image",
    map: (v, P) => ({ prompt: P, image_size: sizeName[s(v, "aspect")] }),
  }),

  // ---------------- Video ----------------
  m({
    id: "kling", tool: "video", name: "Kling 2.5 Turbo", tagline: "Smooth motion, strong prompt following", output: "video",
    fields: [startFrame, prompt("A fox runs through snowy pines, breath in the cold air"), preset,
      aspect(["16:9", "9:16", "1:1"]), { kind: "select", key: "duration", label: "Duration", options: ["5", "10"], default: "5" }],
    endpoints: ["fal-ai/kling-video/v2.5-turbo/pro/text-to-video", "fal-ai/kling-video/v2.5-turbo/pro/image-to-video"],
    endpoint: (v) => v.image ? "fal-ai/kling-video/v2.5-turbo/pro/image-to-video" : "fal-ai/kling-video/v2.5-turbo/pro/text-to-video",
    map: (v, P) => v.image
      ? { prompt: P, image_url: v.image, duration: s(v, "duration") }
      : { prompt: P, aspect_ratio: s(v, "aspect"), duration: s(v, "duration") },
  }),
  m({
    id: "veo31", tool: "video", name: "Veo 3.1", tagline: "Top quality, with generated sound and dialogue", output: "video",
    fields: [startFrame, prompt("A street musician plays violin as snow begins to fall"), preset,
      aspect(["16:9", "9:16"]), { kind: "select", key: "duration", label: "Duration", options: ["4s", "6s", "8s"], default: "8s" },
      { kind: "select", key: "resolution", label: "Resolution", options: ["720p", "1080p", "4k"], default: "1080p" },
      { kind: "toggle", key: "audio", label: "Generate sound", default: true }],
    endpoints: ["fal-ai/veo3.1", "fal-ai/veo3.1/image-to-video"],
    endpoint: (v) => v.image ? "fal-ai/veo3.1/image-to-video" : "fal-ai/veo3.1",
    map: (v, P) => ({ prompt: P, aspect_ratio: s(v, "aspect"), duration: s(v, "duration"), resolution: s(v, "resolution"),
      generate_audio: Boolean(v.audio), ...ifSet("image_url", v.image) }),
  }),
  m({
    id: "seedance", tool: "video", name: "Seedance Pro", tagline: "Cinematic shots, many aspect ratios", output: "video",
    fields: [startFrame, prompt("Slow pan across a desert canyon at sunrise"), preset,
      aspect(["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"]),
      { kind: "select", key: "duration", label: "Duration", options: ["3", "5", "8", "10", "12"], default: "5" },
      { kind: "select", key: "resolution", label: "Resolution", options: ["480p", "720p", "1080p"], default: "1080p" }],
    endpoints: ["fal-ai/bytedance/seedance/v1/pro/text-to-video", "fal-ai/bytedance/seedance/v1/pro/image-to-video"],
    endpoint: (v) => v.image ? "fal-ai/bytedance/seedance/v1/pro/image-to-video" : "fal-ai/bytedance/seedance/v1/pro/text-to-video",
    map: (v, P) => ({ prompt: P, aspect_ratio: s(v, "aspect"), duration: s(v, "duration"), resolution: s(v, "resolution"),
      ...ifSet("image_url", v.image) }),
  }),
  m({
    id: "hailuo", tool: "video", name: "Hailuo 02", tagline: "Realistic physics and people", output: "video",
    fields: [startFrame, prompt("A gymnast lands a backflip on a beach"), preset,
      { kind: "select", key: "duration", label: "Duration", options: ["6", "10"], default: "6" }],
    endpoints: ["fal-ai/minimax/hailuo-02/standard/text-to-video", "fal-ai/minimax/hailuo-02/standard/image-to-video"],
    endpoint: (v) => v.image ? "fal-ai/minimax/hailuo-02/standard/image-to-video" : "fal-ai/minimax/hailuo-02/standard/text-to-video",
    map: (v, P) => ({ prompt: P, duration: s(v, "duration"), ...ifSet("image_url", v.image) }),
  }),
  m({
    id: "wan-video", tool: "video", name: "Wan 2.2", tagline: "Open model, quick drafts", output: "video",
    fields: [startFrame, prompt("Paper boats drift down a rainy gutter"), preset,
      aspect(["16:9", "9:16", "1:1"]), { kind: "select", key: "resolution", label: "Resolution", options: ["480p", "580p", "720p"], default: "720p" }],
    endpoints: ["fal-ai/wan/v2.2-a14b/text-to-video", "fal-ai/wan/v2.2-a14b/image-to-video"],
    endpoint: (v) => v.image ? "fal-ai/wan/v2.2-a14b/image-to-video" : "fal-ai/wan/v2.2-a14b/text-to-video",
    map: (v, P) => ({ prompt: P, aspect_ratio: s(v, "aspect"), resolution: s(v, "resolution"), ...ifSet("image_url", v.image) }),
  }),

  // ---------------- Edit ----------------
  m({
    id: "kontext", tool: "edit", name: "Kontext Edit", tagline: "Describe the change, keep the rest", output: "image",
    fields: [{ kind: "image", key: "image", label: "Image to edit", required: true }, prompt("Make it nighttime with neon signs", "What should change?"),
      aspect(["1:1", "16:9", "9:16", "4:3", "3:4", "3:2", "2:3", "21:9"]), count()],
    endpoints: ["fal-ai/flux-pro/kontext"], endpoint: () => "fal-ai/flux-pro/kontext",
    map: (v, P) => ({ prompt: P, image_url: v.image, aspect_ratio: s(v, "aspect"), num_images: n(v, "count", 1) }),
  }),
  m({
    id: "nano-edit", tool: "edit", name: "Nano Banana Edit", tagline: "Combine up to 4 images in one result", output: "image",
    fields: [{ kind: "images", key: "images", label: "Images", max: 4, required: true, hint: "e.g. a person + an outfit + a place" },
      prompt("Put the person from image 1 in the jacket from image 2, standing in image 3", "Instruction"),
      aspect(["auto", "1:1", "16:9", "9:16", "4:3", "3:4"]), count()],
    endpoints: ["fal-ai/nano-banana/edit"], endpoint: () => "fal-ai/nano-banana/edit",
    map: (v, P) => ({ prompt: P, image_urls: v.images, aspect_ratio: s(v, "aspect"), num_images: n(v, "count", 1) }),
  }),
  m({
    id: "seedream-edit", tool: "edit", name: "Seedream Edit", tagline: "High-res edits from one or more images", output: "image",
    fields: [{ kind: "images", key: "images", label: "Images", max: 4, required: true },
      prompt("Turn this into a watercolor illustration", "Instruction"), count()],
    endpoints: ["fal-ai/bytedance/seedream/v4/edit"], endpoint: () => "fal-ai/bytedance/seedream/v4/edit",
    map: (v, P) => ({ prompt: P, image_urls: v.images, num_images: n(v, "count", 1) }),
  }),
  m({
    id: "inpaint", tool: "edit", name: "Inpaint", tagline: "Paint over an area and describe what goes there", output: "image",
    fields: [{ kind: "image", key: "image", label: "Image", required: true },
      { kind: "mask", key: "mask", label: "Paint the area to replace", imageKey: "image" },
      prompt("A golden retriever sitting on the bench", "What goes in the painted area?"), count()],
    endpoints: ["fal-ai/flux-pro/v1/fill"], endpoint: () => "fal-ai/flux-pro/v1/fill",
    map: (v, P) => ({ prompt: P, image_url: v.image, mask_url: v.mask, num_images: n(v, "count", 1) }),
  }),

  // ---------------- Character ----------------
  m({
    id: "character-multi", tool: "character", name: "Character (multi-reference)", tagline: "Best likeness from 1–4 reference photos", output: "image",
    fields: [{ kind: "images", key: "images", label: "Character reference photos", max: 4, required: true, hint: "Same person or mascot, different angles" },
      prompt("Same character hiking a mountain ridge at sunrise, full body", "New scene"),
      aspect(["1:1", "16:9", "9:16", "4:3", "3:4"]), count()],
    endpoints: ["fal-ai/nano-banana/edit"], endpoint: () => "fal-ai/nano-banana/edit",
    map: (v, P) => ({ prompt: `Keep the exact same character (face, hair, features) as in the reference images. ${P}`,
      image_urls: v.images, aspect_ratio: s(v, "aspect"), num_images: n(v, "count", 1) }),
  }),
  m({
    id: "instant-character", tool: "character", name: "Instant Character", tagline: "One photo, any style or scene", output: "image",
    fields: [{ kind: "image", key: "image", label: "Character photo", required: true },
      prompt("As a knight in a misty forest, oil painting", "New scene"), aspect(SIZE_ASPECTS), count()],
    endpoints: ["fal-ai/instant-character"], endpoint: () => "fal-ai/instant-character",
    map: (v, P) => ({ prompt: P, image_url: v.image, image_size: sizeName[s(v, "aspect")], num_images: n(v, "count", 1) }),
  }),

  // ---------------- Upscale ----------------
  m({
    id: "seedvr-image", tool: "upscale", name: "SeedVR Image", tagline: "Faithful upscaling up to 4K", output: "image",
    fields: [{ kind: "image", key: "image", label: "Image", required: true },
      { kind: "select", key: "target", label: "Target resolution", options: ["1080p", "1440p", "2160p"], default: "2160p" }],
    endpoints: ["fal-ai/seedvr/upscale/image"], endpoint: () => "fal-ai/seedvr/upscale/image",
    map: (v) => ({ image_url: v.image, upscale_mode: "target", target_resolution: s(v, "target") }),
  }),
  m({
    id: "clarity", tool: "upscale", name: "Clarity", tagline: "Adds fine detail while upscaling", output: "image",
    fields: [{ kind: "image", key: "image", label: "Image", required: true },
      { kind: "select", key: "factor", label: "Scale", options: ["2", "3", "4"], default: "2" }],
    endpoints: ["fal-ai/clarity-upscaler"], endpoint: () => "fal-ai/clarity-upscaler",
    map: (v) => ({ image_url: v.image, upscale_factor: n(v, "factor", 2) }),
  }),
  m({
    id: "crisp", tool: "upscale", name: "Crisp", tagline: "Quick, clean sharpening", output: "image",
    fields: [{ kind: "image", key: "image", label: "Image", required: true }],
    endpoints: ["fal-ai/recraft/upscale/crisp"], endpoint: () => "fal-ai/recraft/upscale/crisp",
    map: (v) => ({ image_url: v.image }),
  }),
  m({
    id: "seedvr-video", tool: "upscale", name: "SeedVR Video", tagline: "Upscale video up to 4K", output: "video",
    fields: [{ kind: "video", key: "video", label: "Video", required: true },
      { kind: "select", key: "target", label: "Target resolution", options: ["1080p", "1440p", "2160p"], default: "1080p" }],
    endpoints: ["fal-ai/seedvr/upscale/video"], endpoint: () => "fal-ai/seedvr/upscale/video",
    map: (v) => ({ video_url: v.video, upscale_mode: "target", target_resolution: s(v, "target") }),
  }),
  m({
    id: "topaz-video", tool: "upscale", name: "Topaz Video", tagline: "Studio-grade video enhancement", output: "video",
    fields: [{ kind: "video", key: "video", label: "Video", required: true },
      { kind: "select", key: "factor", label: "Scale", options: ["2", "4"], default: "2" }],
    endpoints: ["fal-ai/topaz/upscale/video"], endpoint: () => "fal-ai/topaz/upscale/video",
    map: (v) => ({ video_url: v.video, upscale_factor: n(v, "factor", 2) }),
  }),

  // ---------------- Lipsync ----------------
  m({
    id: "sync-lipsync", tool: "lipsync", name: "Sync Lipsync 2", tagline: "Re-time a video's mouth to new audio", output: "video",
    fields: [{ kind: "video", key: "video", label: "Video of a face", required: true }, { kind: "audio", key: "audio", label: "Speech audio", required: true },
      { kind: "select", key: "model", label: "Quality", options: ["lipsync-2", "lipsync-2-pro"], default: "lipsync-2" }],
    endpoints: ["fal-ai/sync-lipsync/v2"], endpoint: () => "fal-ai/sync-lipsync/v2",
    map: (v) => ({ video_url: v.video, audio_url: v.audio, model: s(v, "model") }),
  }),
  m({
    id: "kling-lipsync", tool: "lipsync", name: "Kling Lipsync", tagline: "Lipsync for generated video clips", output: "video",
    fields: [{ kind: "video", key: "video", label: "Video", required: true }, { kind: "audio", key: "audio", label: "Speech audio", required: true }],
    endpoints: ["fal-ai/kling-video/lipsync/audio-to-video"], endpoint: () => "fal-ai/kling-video/lipsync/audio-to-video",
    map: (v) => ({ video_url: v.video, audio_url: v.audio }),
  }),
  m({
    id: "omnihuman", tool: "lipsync", name: "Talking Photo", tagline: "Turn one photo + audio into a talking video", output: "video",
    fields: [{ kind: "image", key: "image", label: "Photo of a person", required: true }, { kind: "audio", key: "audio", label: "Speech audio", required: true }],
    endpoints: ["fal-ai/bytedance/omnihuman"], endpoint: () => "fal-ai/bytedance/omnihuman",
    map: (v) => ({ image_url: v.image, audio_url: v.audio }),
  }),

  // ---------------- Audio ----------------
  m({
    id: "tts", tool: "audio", name: "Voiceover", tagline: "Natural speech in 29 languages", output: "audio",
    fields: [{ kind: "prompt", key: "prompt", label: "Script", placeholder: "Welcome back. Today we're building something new.", required: true },
      { kind: "select", key: "voice", label: "Voice", options: VOICES, default: "Rachel" }],
    endpoints: ["fal-ai/elevenlabs/tts/multilingual-v2"], endpoint: () => "fal-ai/elevenlabs/tts/multilingual-v2",
    map: (v) => ({ text: s(v, "prompt"), voice: s(v, "voice") }),
  }),
  m({
    id: "music", tool: "audio", name: "Music", tagline: "Songs or instrumentals from a description", output: "audio",
    fields: [prompt("Upbeat lo-fi hip hop with warm keys and vinyl crackle", "Describe the track"),
      { kind: "select", key: "length", label: "Length", options: ["15s", "30s", "60s", "120s"], default: "30s" },
      { kind: "toggle", key: "instrumental", label: "Instrumental only", default: true }],
    endpoints: ["fal-ai/elevenlabs/music"], endpoint: () => "fal-ai/elevenlabs/music",
    map: (v, P) => ({ prompt: P, music_length_ms: parseInt(s(v, "length")) * 1000, force_instrumental: Boolean(v.instrumental) }),
  }),
  m({
    id: "lyria", tool: "audio", name: "Lyria 2", tagline: "Google's instrumental music model", output: "audio",
    fields: [prompt("Cinematic orchestral swell, hopeful, strings and horns", "Describe the track")],
    endpoints: ["fal-ai/lyria2"], endpoint: () => "fal-ai/lyria2",
    map: (_v, P) => ({ prompt: P }),
  }),
  m({
    id: "sfx", tool: "audio", name: "Sound Effects", tagline: "Any sound from a description", output: "audio",
    fields: [prompt("Heavy wooden door creaking open in an empty hall", "Describe the sound"),
      { kind: "select", key: "seconds", label: "Length", options: ["2", "5", "10", "20"], default: "5" }],
    endpoints: ["fal-ai/elevenlabs/sound-effects"], endpoint: () => "fal-ai/elevenlabs/sound-effects",
    map: (v, P) => ({ text: P, duration_seconds: n(v, "seconds", 5) }),
  }),
  m({
    id: "video-to-audio", tool: "audio", name: "Add Sound to Video", tagline: "Generate matching audio for a silent clip", output: "video",
    fields: [{ kind: "video", key: "video", label: "Silent video", required: true },
      prompt("Waves crashing, seagulls in the distance", "Describe the sound"),
      { kind: "select", key: "seconds", label: "Length", options: ["4", "8", "12", "20", "30"], default: "8" }],
    endpoints: ["fal-ai/mmaudio-v2"], endpoint: () => "fal-ai/mmaudio-v2",
    map: (v, P) => ({ video_url: v.video, prompt: P, duration: n(v, "seconds", 8) }),
  }),

  // ---------------- Face swap ----------------
  m({
    id: "faceswap", tool: "faceswap", name: "Face Swap", tagline: "Put the face from one photo onto another", output: "image",
    fields: [{ kind: "image", key: "base", label: "Target photo (keeps body and scene)", required: true },
      { kind: "image", key: "face", label: "Face photo", required: true },
      { kind: "consent", key: "consent", label: "I am this person, or I have their permission to use their face" }],
    endpoints: ["fal-ai/face-swap"], endpoint: () => "fal-ai/face-swap",
    map: (v) => ({ base_image_url: v.base, swap_image_url: v.face }),
  }),
];

export const getModel = (id: string) => MODELS.find((x) => x.id === id);
export const getTool = (id: string) => TOOLS.find((t) => t.id === id);
export const modelsFor = (tool: ToolId) => MODELS.filter((x) => x.tool === tool);
export const ALL_ENDPOINTS = new Set(MODELS.flatMap((x) => x.endpoints));

export function defaultValues(model: ModelDef): Values {
  const v: Values = {};
  for (const f of model.fields) {
    if (f.kind === "select") v[f.key] = f.default;
    if (f.kind === "count") v[f.key] = f.default;
    if (f.kind === "toggle") v[f.key] = f.default;
    if (f.kind === "preset") v[f.key] = "freeform";
  }
  return v;
}

const isUrl = (x: unknown) => typeof x === "string" && /^(https:|data:)/.test(x);

/** Returns an error message, or null when the values satisfy the model's fields. */
export function validate(model: ModelDef, v: Values): string | null {
  for (const f of model.fields) {
    const val = v[f.key];
    switch (f.kind) {
      case "prompt":
        if (f.required && !(typeof val === "string" && val.trim())) return `${f.label} is required`;
        if (typeof val === "string" && val.length > 5000) return `${f.label} is too long`;
        break;
      case "image": case "video": case "audio":
        if (f.required && !val) return `${f.label} is required`;
        if (val && !isUrl(val)) return `${f.label} is not a valid file`;
        break;
      case "mask":
        if (!val) return "Paint the area you want to replace";
        if (!isUrl(val)) return "Mask is not a valid file";
        break;
      case "images":
        if (f.required && !(Array.isArray(val) && val.length)) return `${f.label}: add at least one`;
        if (Array.isArray(val) && (val.length > f.max || !val.every(isUrl))) return `${f.label}: up to ${f.max} images`;
        break;
      case "select":
        if (!f.options.includes(String(val))) return `Choose a valid ${f.label.toLowerCase()}`;
        break;
      case "count":
        if (!(Number(val) >= 1 && Number(val) <= f.max)) return `${f.label} must be 1–${f.max}`;
        break;
      case "consent":
        if (val !== true) return "Please confirm you have permission to use this face";
        break;
    }
  }
  return null;
}
