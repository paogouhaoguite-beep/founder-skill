"use client";
// Submitting generations and polling them in the background. Polling isn't
// tied to the page that started it: pending jobs resume after a reload.

import { useEffect } from "react";
import { getModel, type ModelDef, type Values } from "./catalog";
import { useStore, type Generation } from "./store";
import { demoAudio, demoImage } from "./demo";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
const active = new Set<string>();
const MAX_AGE_MS = 30 * 60 * 1000; // video upscales and long clips can be slow

type Patch = (id: string, p: Partial<Generation>) => void;
type Add = (g: Generation) => void;

export function newId() {
  // crypto.randomUUID only exists in secure contexts (https or localhost).
  return typeof crypto !== "undefined" && "randomUUID" in crypto
    ? crypto.randomUUID()
    : `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 10)}`;
}

export async function pollJob(g: Generation, patch: Patch) {
  if (!g.job || active.has(g.id)) return;
  active.add(g.id);
  try {
    while (Date.now() - g.createdAt < MAX_AGE_MS) {
      await sleep(2500);
      const res = await fetch("/api/status", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(g.job),
      });
      const s = await res.json().catch(() => ({ status: "FAILED", error: `HTTP ${res.status}` }));
      if (s.status === "COMPLETED") {
        if (!s.urls?.length) throw new Error("The model returned no output");
        patch(g.id, { status: "done", urls: s.urls, job: undefined });
        return;
      }
      if (s.status === "FAILED") throw new Error(s.error ?? "Generation failed");
    }
    throw new Error("Timed out waiting for the model");
  } catch (e) {
    patch(g.id, { status: "failed", error: (e as Error).message, job: undefined });
  } finally {
    active.delete(g.id);
  }
}

/** Resume pending jobs; mark ones that can never finish as failed. */
export function useResumeJobs() {
  const { items, patch } = useStore();
  useEffect(() => {
    for (const g of items) {
      if (g.status !== "pending") continue;
      if (g.job) pollJob(g, patch);
      else if (Date.now() - g.createdAt > 60_000) {
        patch(g.id, { status: "failed", error: "Interrupted before it was submitted" });
      }
    }
  }, [items, patch]);
}

const displayText = (model: ModelDef, v: Values) =>
  (typeof v.prompt === "string" && v.prompt.trim()) || model.name;

/**
 * Validate on the server and submit. Resolves with the new generation's id
 * once it is queued (or finished, in demo mode); throws a readable error.
 */
export async function submitGeneration(modelId: string, values: Values, add: Add, patch: Patch): Promise<string> {
  const model = getModel(modelId);
  if (!model) throw new Error("Unknown model");
  const res = await fetch("/api/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ modelId, values }),
  });
  const data = await res.json().catch(() => ({ error: `HTTP ${res.status}` }));
  if (!res.ok) throw new Error(data.error ?? "Request failed");

  const g: Generation = {
    id: newId(), tool: model.tool, modelId, output: model.output,
    prompt: displayText(model, values), values,
    createdAt: Date.now(), status: "pending", urls: [],
  };
  add(g);

  if (data.demo) {
    await sleep(900);
    const n = Number(values.count) || 1;
    const aspect = typeof values.aspect === "string" && values.aspect !== "auto" ? values.aspect : "1:1";
    const urls = model.output === "audio"
      ? [demoAudio(g.prompt)]
      : Array.from({ length: model.output === "image" ? n : 1 }, (_, i) => demoImage(g.prompt, aspect, i));
    patch(g.id, { status: "done", urls, demo: true });
    return g.id;
  }

  const job = { endpoint: data.endpoint as string, requestId: data.requestId as string };
  patch(g.id, { job });
  pollJob({ ...g, job }, patch);
  return g.id;
}

/** Wait for a generation to finish (used by storyboard batch runs). */
export async function waitFor(id: string, read: () => Generation | undefined, timeoutMs = MAX_AGE_MS) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    const g = read();
    if (g && g.status !== "pending") return g;
    await sleep(1000);
  }
  return read();
}
