"use client";
// Per-browser state kept in localStorage: the generation library, saved
// storyboards and the canvas board.

import { useCallback, useEffect, useState } from "react";
import type { Output, ToolId, Values } from "./catalog";

export interface Generation {
  id: string;
  tool: ToolId;
  modelId: string;
  output: Output;
  prompt: string;
  values?: Values; // settings to reuse (hosted file URLs only, never data: URLs)
  createdAt: number;
  status: "pending" | "done" | "failed";
  urls: string[];
  demo?: boolean;
  error?: string;
  /** provider job while it is running */
  job?: { endpoint: string; requestId: string };
}

export interface Scene { id: string; text: string; frameGenId?: string; clipGenId?: string }
export interface Storyboard { id: string; title: string; style: string; aspect: string; scenes: Scene[]; characters?: string[]; updatedAt: number }
export interface BoardItem { id: string; kind: "media" | "note"; genId?: string; url?: string; output?: Output; text?: string; x: number; y: number; w: number }

interface State {
  items: Generation[];
  boards: Storyboard[];
  canvas: BoardItem[];
}

const KEY = "flippers:v1";
const EMPTY: State = { items: [], boards: [], canvas: [] };

// Older saves used `mode` instead of `tool`/`output`.
type Legacy = Omit<Generation, "tool" | "output"> & Partial<Pick<Generation, "tool" | "output">> & { mode?: string };
function migrate(raw: { items?: Legacy[]; boards?: Storyboard[]; canvas?: BoardItem[] }): State {
  return {
    boards: raw.boards ?? [],
    canvas: raw.canvas ?? [],
    items: (raw.items ?? []).map((g): Generation => ({
      ...g,
      tool: g.tool ?? ((g.mode as ToolId) || "image"),
      output: g.output ?? ((g.mode as Output) || "image"),
    })),
  };
}

function load(): State {
  try {
    const raw = localStorage.getItem(KEY);
    if (raw) return migrate(JSON.parse(raw));
  } catch {}
  return EMPTY;
}

let saveFailed = false;
function save(s: State) {
  try {
    localStorage.setItem(KEY, JSON.stringify({ ...s, items: s.items.slice(0, 300) }));
    saveFailed = false;
  } catch {
    saveFailed = true; // storage full or blocked; state still works in memory
  }
}
export const lastSaveFailed = () => saveFailed;

const listeners = new Set<(s: State) => void>();
let state: State | null = null;

function set(update: (s: State) => State) {
  state = update(state ?? load());
  save(state);
  listeners.forEach((l) => l(state!));
}

/** Read the current snapshot outside React (e.g. inside async callbacks). */
export const snapshot = () => (state ??= load());

const strip = (v?: Values): Values | undefined => {
  if (!v) return v;
  const out: Values = {};
  for (const [k, x] of Object.entries(v)) {
    if (k.startsWith("_")) continue;
    if (typeof x === "string" && x.startsWith("data:")) continue;
    if (Array.isArray(x)) out[k] = x.filter((u) => !u.startsWith("data:"));
    else out[k] = x;
  }
  return out;
};

export function useStore() {
  const [s, setS] = useState<State>(EMPTY);
  useEffect(() => {
    state = state ?? load();
    setS(state);
    listeners.add(setS);
    return () => {
      listeners.delete(setS);
    };
  }, []);

  return {
    ...s,
    add: useCallback((g: Generation) => set((st) => ({ ...st, items: [{ ...g, values: strip(g.values) }, ...st.items] })), []),
    patch: useCallback((id: string, p: Partial<Generation>) =>
      set((st) => ({ ...st, items: st.items.map((g) => (g.id === id ? { ...g, ...p } : g)) })), []),
    remove: useCallback((id: string) => set((st) => ({ ...st, items: st.items.filter((g) => g.id !== id) })), []),
    saveBoard: useCallback((b: Storyboard) =>
      set((st) => ({ ...st, boards: [b, ...st.boards.filter((x) => x.id !== b.id)] })), []),
    deleteBoard: useCallback((id: string) => set((st) => ({ ...st, boards: st.boards.filter((b) => b.id !== id) })), []),
    setCanvas: useCallback((fn: (c: BoardItem[]) => BoardItem[]) => set((st) => ({ ...st, canvas: fn(st.canvas) })), []),
  };
}
