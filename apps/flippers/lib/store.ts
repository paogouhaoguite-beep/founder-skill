"use client";
// Per-browser library of generations, kept in localStorage.

import { useCallback, useEffect, useState } from "react";
import type { Mode } from "./models";

export interface Generation {
  id: string;
  mode: Mode;
  modelId: string;
  prompt: string;
  aspectRatio: string;
  presetId?: string;
  createdAt: number;
  status: "pending" | "done" | "failed";
  urls: string[];
  demo?: boolean;
  error?: string;
  favorite?: boolean;
  /** provider queue URLs while the job is running */
  job?: { statusUrl: string; responseUrl: string };
}

const KEY = "flippers:v1";

interface State {
  items: Generation[];
}

function load(): State {
  try {
    const raw = localStorage.getItem(KEY);
    if (raw) return JSON.parse(raw);
  } catch {}
  return { items: [] };
}

function save(s: State) {
  try {
    // Data URLs from demo/reference images can be large; keep the newest 200.
    localStorage.setItem(KEY, JSON.stringify({ ...s, items: s.items.slice(0, 200) }));
  } catch {}
}

const listeners = new Set<(s: State) => void>();
let state: State | null = null;

function set(update: (s: State) => State) {
  state = update(state ?? load());
  save(state);
  listeners.forEach((l) => l(state!));
}

export function useStore() {
  const [s, setS] = useState<State>({ items: [] });
  useEffect(() => {
    state = state ?? load();
    setS(state);
    listeners.add(setS);
    return () => {
      listeners.delete(setS);
    };
  }, []);

  return {
    items: s.items,
    add: useCallback((g: Generation) => {
      set((st) => ({ ...st, items: [g, ...st.items] }));
    }, []),
    patch: useCallback((id: string, p: Partial<Generation>) => {
      set((st) => ({ ...st, items: st.items.map((g) => (g.id === id ? { ...g, ...p } : g)) }));
    }, []),
    remove: useCallback((id: string) => {
      set((st) => ({ ...st, items: st.items.filter((g) => g.id !== id) }));
    }, []),
  };
}
