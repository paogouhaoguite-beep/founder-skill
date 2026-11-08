"use client";
import { useEffect, useMemo, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import { costOf, getModel, modelsFor, type Mode } from "@/lib/models";
import { PRESETS } from "@/lib/presets";
import { useStore, type Generation } from "@/lib/store";
import { demoImage } from "@/lib/demo";
import MediaCard from "./MediaCard";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

function readFile(file: File): Promise<string> {
  return new Promise((resolve, reject) => {
    const r = new FileReader();
    r.onload = () => resolve(r.result as string);
    r.onerror = reject;
    r.readAsDataURL(file);
  });
}

export default function Studio({ mode }: { mode: Mode }) {
  const params = useSearchParams();
  const models = modelsFor(mode);
  const store = useStore();

  const [modelId, setModelId] = useState(() => {
    const q = params.get("model");
    return q && getModel(q)?.mode === mode ? q : models[0].id;
  });
  const model = getModel(modelId)!;
  const [prompt, setPrompt] = useState(params.get("prompt") ?? "");
  const [aspectRatio, setAspectRatio] = useState(model.aspectRatios[0]);
  const [resolution, setResolution] = useState(model.resolutions[0]);
  const [duration, setDuration] = useState(model.durations?.[0] ?? 5);
  const [count, setCount] = useState(mode === "image" ? 2 : 1);
  const [presetId, setPresetId] = useState(params.get("preset") ?? "freeform");
  const [reference, setReference] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [demoNotice, setDemoNotice] = useState(false);
  const fileRef = useRef<HTMLInputElement>(null);

  // Keep options valid when the model changes.
  useEffect(() => {
    if (!model.aspectRatios.includes(aspectRatio)) setAspectRatio(model.aspectRatios[0]);
    if (!model.resolutions.includes(resolution)) setResolution(model.resolutions[0]);
    if (model.durations && !model.durations.includes(duration)) setDuration(model.durations[0]);
  }, [modelId]); // eslint-disable-line react-hooks/exhaustive-deps

  const cost = costOf({ mode, modelId, count, duration });
  const feed = useMemo(() => store.items.filter((g) => g.mode === mode), [store.items, mode]);

  async function generate() {
    setError(null);
    if (!prompt.trim()) return setError("Write a prompt first.");
    if (model.needsReference && !reference) return setError(`${model.name} needs a reference image.`);
    if (cost > store.credits) return setError("Not enough credits — top up on the Pricing page.");

    setBusy(true);
    const id = crypto.randomUUID();
    const g: Generation = {
      id, mode, modelId, prompt, aspectRatio, presetId,
      createdAt: Date.now(), status: "pending", urls: [],
    };
    store.add(g, cost);

    try {
      const res = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          mode, modelId, prompt, aspectRatio, resolution, duration, count, presetId,
          referenceImage: model.acceptsReference ? reference ?? undefined : undefined,
        }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error ?? "Request failed");

      if (data.demo) {
        setDemoNotice(true);
        await sleep(1200);
        const n = mode === "image" ? count : 1;
        const urls = Array.from({ length: n }, (_, i) =>
          mode === "image" || !reference ? demoImage(prompt, aspectRatio, i) : reference,
        );
        store.patch(id, { status: "done", urls, demo: true });
        return;
      }

      // Poll the provider queue until the job finishes (max ~10 minutes).
      for (let i = 0; i < 300; i++) {
        await sleep(2000);
        const s = await fetch("/api/status", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data),
        }).then((r) => r.json());
        if (s.status === "COMPLETED") {
          store.patch(id, { status: "done", urls: s.urls });
          return;
        }
        if (s.status === "FAILED") throw new Error(s.error ?? "Generation failed");
      }
      throw new Error("Timed out waiting for the model");
    } catch (e) {
      store.patch(id, { status: "failed", error: (e as Error).message });
      store.refund(cost);
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  function reuse(g: Generation) {
    setModelId(g.modelId);
    setPrompt(g.prompt);
    setAspectRatio(g.aspectRatio);
    if (g.presetId) setPresetId(g.presetId);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return (
    <div className="studio">
      <aside className="controls">
        {(model.acceptsReference || model.needsReference) && (
          <div>
            <div className="field-label">
              {mode === "video" ? "Start frame (optional)" : "Reference image"}
            </div>
            <div className="dropzone" onClick={() => fileRef.current?.click()}
              onDragOver={(e) => e.preventDefault()}
              onDrop={async (e) => {
                e.preventDefault();
                const f = e.dataTransfer.files[0];
                if (f) setReference(await readFile(f));
              }}>
              {reference ? (
                <>
                  <img src={reference} alt="Reference" />
                  <button className="btn clear" onClick={(e) => { e.stopPropagation(); setReference(null); }}>✕</button>
                </>
              ) : (
                <>Drop an image or click to upload</>
              )}
            </div>
            <input ref={fileRef} type="file" accept="image/*" hidden
              onChange={async (e) => {
                const f = e.target.files?.[0];
                if (f) setReference(await readFile(f));
                e.target.value = "";
              }} />
          </div>
        )}

        <div>
          <div className="field-label">Prompt</div>
          <textarea className="prompt" value={prompt} onChange={(e) => setPrompt(e.target.value)}
            placeholder={mode === "image"
              ? "A lighthouse on a cliff at dusk, volumetric fog, 35mm film"
              : "A fox runs through snowy pines, breath visible in the cold air"}
            onKeyDown={(e) => { if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) generate(); }} />
        </div>

        {mode === "video" && (
          <div>
            <div className="field-label">Motion preset</div>
            <div className="presets">
              {PRESETS.map((p) => (
                <button key={p.id} className={`preset ${presetId === p.id ? "on" : ""}`}
                  style={{ background: `linear-gradient(160deg, hsl(${p.hue},60%,42%), hsl(${(p.hue + 50) % 360},55%,16%))` }}
                  onClick={() => setPresetId(p.id)} title={p.prompt || "No camera instruction"}>
                  {p.name}
                </button>
              ))}
            </div>
          </div>
        )}

        <div>
          <div className="field-label">Model</div>
          <div className="model-list">
            {models.map((m) => (
              <button key={m.id} className={`model ${m.id === modelId ? "on" : ""}`} onClick={() => setModelId(m.id)}>
                <span className="cost">✦ {m.cost}{m.mode === "video" ? "/s" : ""}</span>
                {m.name}
                <small>{m.tagline}</small>
              </button>
            ))}
          </div>
        </div>

        <div>
          <div className="field-label">Aspect ratio</div>
          <div className="chips">
            {model.aspectRatios.map((a) => (
              <button key={a} className={`chip ${a === aspectRatio ? "on" : ""}`} onClick={() => setAspectRatio(a)}>{a}</button>
            ))}
          </div>
        </div>

        {model.resolutions.length > 1 && (
          <div>
            <div className="field-label">Resolution</div>
            <div className="chips">
              {model.resolutions.map((r) => (
                <button key={r} className={`chip ${r === resolution ? "on" : ""}`} onClick={() => setResolution(r)}>{r}</button>
              ))}
            </div>
          </div>
        )}

        {mode === "video" && model.durations && (
          <div>
            <div className="field-label">Duration</div>
            <div className="chips">
              {model.durations.map((d) => (
                <button key={d} className={`chip ${d === duration ? "on" : ""}`} onClick={() => setDuration(d)}>{d}s</button>
              ))}
            </div>
          </div>
        )}

        {mode === "image" && (
          <div>
            <div className="field-label">Images</div>
            <div className="stepper">
              <button onClick={() => setCount((c) => Math.max(1, c - 1))}>−</button>
              <strong>{count}</strong>
              <button onClick={() => setCount((c) => Math.min(4, c + 1))}>+</button>
            </div>
          </div>
        )}

        {error && <div className="error">{error}</div>}
        <button className="btn-primary" disabled={busy} onClick={generate}>
          {busy ? "Generating…" : "Generate"} <span>✦ {cost}</span>
        </button>
        <div className="hint">⌘/Ctrl + Enter to generate</div>
      </aside>

      <section className="feed">
        <div className="feed-head">
          <h1>{mode === "image" ? "Image studio" : "Video studio"}</h1>
          <span className="hint">{feed.length} generations</span>
        </div>
        {demoNotice && (
          <div className="banner">
            Demo mode: no <code>FAL_KEY</code> set on the server, so these are placeholders. Add a key to <code>.env.local</code> for real generations.
          </div>
        )}
        {feed.length === 0 ? (
          <div className="empty">Your generations will show up here.</div>
        ) : (
          <div className="grid">
            {feed.map((g) => <MediaCard key={g.id} g={g} onRemove={store.remove} onReuse={reuse} />)}
          </div>
        )}
      </section>
    </div>
  );
}
