// Camera and motion presets. Each preset appends a motion instruction to the
// prompt, so they work with any video model.

export interface Preset {
  id: string;
  name: string;
  category: "Camera" | "Mood" | "Effect";
  prompt: string;
  hue: number; // tile colour for the preset card
}

export const PRESETS: Preset[] = [
  { id: "freeform", name: "Freeform", category: "Camera", prompt: "", hue: 220 },
  { id: "push-in", name: "Slow Push-In", category: "Camera", prompt: "the camera slowly pushes in toward the subject", hue: 12 },
  { id: "orbit", name: "Orbit", category: "Camera", prompt: "the camera orbits 180 degrees around the subject", hue: 32 },
  { id: "crane-up", name: "Crane Up", category: "Camera", prompt: "the camera rises vertically, revealing the surroundings", hue: 200 },
  { id: "whip-pan", name: "Whip Pan", category: "Camera", prompt: "a fast whip pan with motion blur", hue: 280 },
  { id: "handheld", name: "Handheld", category: "Camera", prompt: "handheld camera with subtle natural shake", hue: 150 },
  { id: "crash-zoom", name: "Crash Zoom", category: "Camera", prompt: "a sudden dramatic zoom onto the subject's face", hue: 350 },
  { id: "fpv", name: "FPV Dive", category: "Camera", prompt: "an FPV drone dives fast through the scene", hue: 180 },
  { id: "golden", name: "Golden Hour", category: "Mood", prompt: "warm golden-hour light, long soft shadows", hue: 40 },
  { id: "noir", name: "Neo-Noir", category: "Mood", prompt: "high-contrast neon-lit noir atmosphere, rain", hue: 260 },
  { id: "dream", name: "Dreamlike", category: "Mood", prompt: "soft focus, floating particles, dreamy haze", hue: 310 },
  { id: "slowmo", name: "Slow Motion", category: "Effect", prompt: "shot in extreme slow motion", hue: 100 },
  { id: "explode", name: "Shatter", category: "Effect", prompt: "the subject shatters into glowing fragments", hue: 0 },
  { id: "melt", name: "Liquify", category: "Effect", prompt: "the scene melts and flows like liquid", hue: 190 },
];
