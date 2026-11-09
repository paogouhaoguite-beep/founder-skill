"use client";
import { useEffect, useMemo, useState } from "react";
import { useSearchParams } from "next/navigation";
import { defaultValues, getModel, getTool, modelsFor, validate, type Field, type ToolId, type Values } from "@/lib/catalog";
import { useStore, type Generation } from "@/lib/store";
import { submitGeneration, useResumeJobs } from "@/lib/jobs";
import { isDemo, takeHandoff } from "@/lib/upload";
import { FileField, ImagesField, MaskPainter, PresetPicker } from "./Fields";
import MediaCard from "./MediaCard";

export default function ToolStudio({ tool }: { tool: ToolId }) {
  const params = useSearchParams();
  const info = getTool(tool)!;
  const models = modelsFor(tool);
  const store = useStore();
  useResumeJobs();

  const [modelId, setModelId] = useState(() => {
    const q = params.get("model");
    return q && getModel(q)?.tool === tool ? q : models[0].id;
  });
  const model = getModel(modelId)!;
  const [values, setValues] = useState<Values>(() => {
    const v = defaultValues(model);
    for (const key of ["prompt", "preset", "aspect"]) {
      const q = params.get(key);
      if (q) v[key] = q;
    }
    return v;
  });
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [demo, setDemo] = useState(false);

  useEffect(() => { isDemo().then(setDemo); }, []);

  // Accept a file passed from another tool ("Animate", "Edit", "Upscale"…).
  useEffect(() => {
    const h = takeHandoff(tool);
    if (!h) return;
    if (typeof h.modelId === "string" && getModel(h.modelId)?.tool === tool) setModelId(h.modelId);
    setValues((v) => ({ ...v, ...(h.values as Values) }));
  }, [tool]);

  // When the model changes, keep shared values and fill new defaults.
  function pickModel(id: string) {
    const next = getModel(id)!;
    const d = defaultValues(next);
    const keep: Values = {};
    for (const f of next.fields) {
      const cur = values[f.key];
      if (cur === undefined) continue;
      if (f.kind === "select" && !f.options.includes(String(cur))) continue;
      if (f.kind === "count" && Number(cur) > f.max) continue;
      if (f.kind === "image" && Array.isArray(cur)) continue;
      keep[f.key] = cur;
    }
    // A single image carries over to multi-image fields and back.
    const imgs = next.fields.find((f) => f.kind === "images");
    if (imgs && !keep[imgs.key] && typeof values.image === "string") keep[imgs.key] = [values.image];
    const img = next.fields.find((f) => f.kind === "image");
    if (img && !keep[img.key] && Array.isArray(values.images) && values.images[0]) keep[img.key] = values.images[0];
    setModelId(id);
    setValues({ ...d, ...keep });
    setError(null);
  }

  const set = (key: string, v: Values[string]) => setValues((cur) => ({ ...cur, [key]: v }));
  const feed = useMemo(() => store.items.filter((g) => g.tool === tool), [store.items, tool]);

  async function generate() {
    const problem = validate(model, values);
    if (problem) return setError(problem);
    setError(null);
    setBusy(true);
    try {
      await submitGeneration(modelId, values, store.add, store.patch);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  function reuse(g: Generation) {
    if (g.modelId !== modelId) pickModel(g.modelId);
    setValues((v) => ({ ...defaultValues(getModel(g.modelId)!), ...v, ...(g.values ?? {}) }));
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  const render = (f: Field) => {
    const v = values[f.key];
    switch (f.kind) {
      case "prompt":
        return (
          <div key={f.key}>
            <div className="field-label">{f.label}</div>
            <textarea className="prompt" value={typeof v === "string" ? v : ""} placeholder={f.placeholder}
              onChange={(e) => set(f.key, e.target.value)}
              onKeyDown={(e) => { if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) generate(); }} />
          </div>
        );
      case "image": case "video": case "audio":
        return <FileField key={f.key} kind={f.kind} label={f.label} hint={"hint" in f ? f.hint : undefined}
          value={typeof v === "string" ? v : undefined} onChange={(u) => set(f.key, u)} />;
      case "images":
        return <ImagesField key={f.key} label={f.label} hint={f.hint} max={f.max}
          value={Array.isArray(v) ? v : undefined} onChange={(u) => set(f.key, u)} />;
      case "mask":
        return <MaskPainter key={f.key + String(values[f.imageKey])} label={f.label}
          imageUrl={typeof values[f.imageKey] === "string" ? (values[f.imageKey] as string) : undefined}
          value={typeof v === "string" ? v : undefined} onChange={(u) => set(f.key, u)} />;
      case "preset":
        return <PresetPicker key={f.key} label={f.label} value={typeof v === "string" ? v : "freeform"} onChange={(id) => set(f.key, id)} />;
      case "select":
        return (
          <div key={f.key}>
            <div className="field-label">{f.label}</div>
            {f.options.length > 8 ? (
              <select className="select" value={String(v)} onChange={(e) => set(f.key, e.target.value)}>
                {f.options.map((o) => <option key={o}>{o}</option>)}
              </select>
            ) : (
              <div className="chips">
                {f.options.map((o) => (
                  <button type="button" key={o} className={`chip ${String(v) === o ? "on" : ""}`} onClick={() => set(f.key, o)}>
                    {/^\d+$/.test(o) && f.key === "duration" ? `${o}s` : o}
                  </button>
                ))}
              </div>
            )}
          </div>
        );
      case "count":
        return (
          <div key={f.key}>
            <div className="field-label">{f.label}</div>
            <div className="stepper">
              <button type="button" onClick={() => set(f.key, Math.max(1, Number(v) - 1))}>−</button>
              <strong>{Number(v)}</strong>
              <button type="button" onClick={() => set(f.key, Math.min(f.max, Number(v) + 1))}>+</button>
            </div>
          </div>
        );
      case "toggle": case "consent":
        return (
          <label key={f.key} className={`toggle ${f.kind === "consent" ? "consent" : ""}`}>
            <input type="checkbox" checked={v === true} onChange={(e) => set(f.key, e.target.checked)} />
            {f.label}
          </label>
        );
    }
  };

  return (
    <div className="studio">
      <aside className="controls">
        <div>
          <div className="field-label">Model</div>
          <div className="model-list">
            {models.map((x) => (
              <button type="button" key={x.id} className={`model ${x.id === modelId ? "on" : ""}`} onClick={() => pickModel(x.id)}>
                {x.name}
                <small>{x.tagline}</small>
              </button>
            ))}
          </div>
        </div>
        {model.fields.map(render)}
        {error && <div className="error">{error}</div>}
        <button className="btn-primary" disabled={busy} onClick={generate}>
          {busy ? "Submitting…" : "Generate"}
        </button>
        <div className="hint">⌘/Ctrl + Enter to generate. You can queue several at once.</div>
      </aside>

      <section className="feed">
        <div className="feed-head">
          <div>
            <h1>{info.name}</h1>
            <div className="hint">{info.blurb}</div>
          </div>
          <span className="hint">{feed.length} results</span>
        </div>
        {demo && (
          <div className="banner">
            Demo mode: no <code>FAL_KEY</code> set on the server, so results are placeholders. Add a key to <code>.env.local</code> for real generations.
          </div>
        )}
        {feed.length === 0 ? (
          <div className="empty">Your results will show up here.</div>
        ) : (
          <div className="grid">
            {feed.map((g) => <MediaCard key={g.id} g={g} onRemove={store.remove} onReuse={reuse} />)}
          </div>
        )}
      </section>
    </div>
  );
}
