// Model catalog. Each entry maps the studio's generic controls onto one fal.ai
// endpoint. Endpoint IDs change over time — check https://fal.ai/models and
// edit `falId` / `toInput` here if a model is renamed or retired.

export type Mode = "image" | "video";

export interface GenRequest {
  mode: Mode;
  modelId: string;
  prompt: string;
  aspectRatio: string;
  count: number; // images per run (image mode)
  duration: number; // seconds (video mode)
  resolution: string;
  referenceImage?: string; // data: URL or https URL
  presetPrompt?: string; // camera/motion instruction appended to prompt
}

export interface ModelDef {
  id: string;
  mode: Mode;
  name: string;
  tagline: string;
  /** credits per image, or per second of video */
  cost: number;
  aspectRatios: string[];
  resolutions: string[];
  durations?: number[];
  needsReference?: boolean;
  acceptsReference?: boolean;
  falId: (req: GenRequest) => string;
  toInput: (req: GenRequest) => Record<string, unknown>;
}

const fullPrompt = (r: GenRequest) =>
  [r.prompt.trim(), r.presetPrompt?.trim()].filter(Boolean).join(". ");

const fluxSize: Record<string, string> = {
  "1:1": "square_hd",
  "4:3": "landscape_4_3",
  "3:4": "portrait_4_3",
  "16:9": "landscape_16_9",
  "9:16": "portrait_16_9",
};

export const MODELS: ModelDef[] = [
  {
    id: "flux-dev",
    mode: "image",
    name: "Flux Dev",
    tagline: "Fast, versatile text-to-image",
    cost: 2,
    aspectRatios: ["1:1", "4:3", "3:4", "16:9", "9:16"],
    resolutions: ["Standard"],
    falId: () => "fal-ai/flux/dev",
    toInput: (r) => ({
      prompt: fullPrompt(r),
      image_size: fluxSize[r.aspectRatio] ?? "square_hd",
      num_images: r.count,
    }),
  },
  {
    id: "flux-pro-ultra",
    mode: "image",
    name: "Flux Pro Ultra",
    tagline: "High-resolution photoreal stills",
    cost: 6,
    aspectRatios: ["1:1", "4:3", "3:4", "16:9", "9:16", "21:9"],
    resolutions: ["2K"],
    falId: () => "fal-ai/flux-pro/v1.1-ultra",
    toInput: (r) => ({
      prompt: fullPrompt(r),
      aspect_ratio: r.aspectRatio,
      num_images: r.count,
    }),
  },
  {
    id: "kontext-edit",
    mode: "image",
    name: "Kontext Edit",
    tagline: "Edit a reference image with words",
    cost: 4,
    aspectRatios: ["1:1", "4:3", "3:4", "16:9", "9:16"],
    resolutions: ["Standard"],
    needsReference: true,
    acceptsReference: true,
    falId: () => "fal-ai/flux-pro/kontext",
    toInput: (r) => ({
      prompt: fullPrompt(r),
      image_url: r.referenceImage,
      aspect_ratio: r.aspectRatio,
      num_images: r.count,
    }),
  },
  {
    id: "kling",
    mode: "video",
    name: "Kling",
    tagline: "Smooth motion, strong prompt following",
    cost: 10,
    aspectRatios: ["16:9", "9:16", "1:1"],
    resolutions: ["720p"],
    durations: [5, 10],
    acceptsReference: true,
    falId: (r) =>
      r.referenceImage
        ? "fal-ai/kling-video/v2.1/standard/image-to-video"
        : "fal-ai/kling-video/v2.1/standard/text-to-video",
    toInput: (r) => ({
      prompt: fullPrompt(r),
      duration: String(r.duration),
      aspect_ratio: r.aspectRatio,
      ...(r.referenceImage ? { image_url: r.referenceImage } : {}),
    }),
  },
  {
    id: "seedance",
    mode: "video",
    name: "Seedance Pro",
    tagline: "Cinematic multi-shot video",
    cost: 14,
    aspectRatios: ["16:9", "9:16", "1:1", "4:3", "21:9"],
    resolutions: ["480p", "1080p"],
    durations: [5, 10],
    acceptsReference: true,
    falId: (r) =>
      r.referenceImage
        ? "fal-ai/bytedance/seedance/v1/pro/image-to-video"
        : "fal-ai/bytedance/seedance/v1/pro/text-to-video",
    toInput: (r) => ({
      prompt: fullPrompt(r),
      duration: String(r.duration),
      aspect_ratio: r.aspectRatio,
      resolution: r.resolution,
      ...(r.referenceImage ? { image_url: r.referenceImage } : {}),
    }),
  },
  {
    id: "veo",
    mode: "video",
    name: "Veo 3",
    tagline: "Video with generated sound",
    cost: 40,
    aspectRatios: ["16:9", "9:16"],
    resolutions: ["720p", "1080p"],
    durations: [8],
    falId: () => "fal-ai/veo3",
    toInput: (r) => ({
      prompt: fullPrompt(r),
      aspect_ratio: r.aspectRatio,
      resolution: r.resolution,
      duration: `${r.duration}s`,
    }),
  },
];

export const modelsFor = (mode: Mode) => MODELS.filter((m) => m.mode === mode);
export const getModel = (id: string) => MODELS.find((m) => m.id === id);

export function costOf(req: Pick<GenRequest, "modelId" | "count" | "duration" | "mode">) {
  const m = getModel(req.modelId);
  if (!m) return 0;
  return m.mode === "image" ? m.cost * req.count : m.cost * req.duration;
}
