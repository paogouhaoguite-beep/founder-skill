"use client";
// Background polling for provider jobs. Polling isn't tied to the page that
// started it: if you reload or come back later, pending jobs resume here.

import { useEffect } from "react";
import { useStore, type Generation } from "./store";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
const active = new Set<string>();
const MAX_AGE_MS = 15 * 60 * 1000;

type Patch = (id: string, p: Partial<Generation>) => void;

export function newId() {
  // crypto.randomUUID only exists in secure contexts (https or localhost);
  // opening the dev server from a phone on the LAN is neither.
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
