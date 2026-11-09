"use client";
// File uploads. With an API key, files go straight from the browser to fal's
// storage (through our storage-only proxy, so the key stays on the server)
// and we keep the hosted URL. In demo mode we keep a local data: URL instead.

import { fal } from "@fal-ai/client";

let demo: boolean | null = null;
export async function isDemo() {
  if (demo === null) {
    demo = await fetch("/api/config").then((r) => r.json()).then((d) => Boolean(d.demo)).catch(() => true);
  }
  return demo;
}

fal.config({ proxyUrl: "/api/fal/proxy" });

const MAX_DEMO_BYTES = 8 * 1024 * 1024;

function toDataUrl(file: Blob): Promise<string> {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onload = () => resolve(r.result as string);
    r.onerror = () => reject(r.error);
    r.readAsDataURL(file);
  });
}

export async function uploadFile(file: Blob): Promise<string> {
  if (await isDemo()) {
    if (file.size > MAX_DEMO_BYTES) throw new Error("Demo mode keeps files in the browser; use one under 8 MB");
    return toDataUrl(file);
  }
  return fal.storage.upload(file);
}

/** Reuse an existing output (e.g. "Animate this") as an input file. */
export async function urlToInput(url: string): Promise<string> {
  if (!url.startsWith("data:") || (await isDemo())) return url;
  const blob = await fetch(url).then((r) => r.blob());
  return fal.storage.upload(blob);
}

// ---- handoff between tools ("Animate", "Edit", "Upscale" buttons) ----
const HANDOFF = "flippers:handoff";
export function handoff(tool: string, values: Record<string, unknown>) {
  try {
    sessionStorage.setItem(HANDOFF, JSON.stringify({ tool, values }));
  } catch {}
}
export function takeHandoff(tool: string): Record<string, unknown> | null {
  try {
    const raw = sessionStorage.getItem(HANDOFF);
    if (!raw) return null;
    const h = JSON.parse(raw);
    if (h.tool !== tool) return null;
    sessionStorage.removeItem(HANDOFF);
    return h.values;
  } catch {
    return null;
  }
}
