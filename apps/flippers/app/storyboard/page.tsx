"use client";
import { useMemo, useState } from "react";
import { defaultValues, getModel, type Field, type Values } from "@/lib/catalog";
import { snapshot, useStore, type Scene, type Storyboard } from "@/lib/store";
import { newId, submitGeneration, useResumeJobs } from "@/lib/jobs";
import { ImagesField } from "@/components/Fields";

const FRAME_MODELS = ["nano-banana", "seedream", "flux-ultra", "flux-dev"];
const CLIP_MODELS = ["kling", "seedance", "hailuo", "veo31", "wan-video"];
const ASPECTS = ["16:9", "9:16", "1:1"];

const blank = (): Storyboard => ({
  id: newId(), title: "Untitled story", style: "cinematic, soft natural light, 35mm film look", aspect: "16:9",
  scenes: [{ id: newId(), text: "" }, { id: newId(), text: "" }, { id: newId(), text: "" }], updatedAt: Date.now(),
});

function withAspect(modelId: string, base: Values, aspect: string): Values {
  const model = getModel(modelId)!;
  const v = { ...defaultValues(model), ...base };
  const f = model.fields.find((x): x is Extract<Field, { kind: "select" }> => x.kind === "select" && x.key === "aspect");
  if (f && f.options.includes(aspect)) v.aspect = aspect;
  if ("count" in v) v.count = 1;
  return v;
}

export default function StoryboardPage() {
  const store = useStore();
  useResumeJobs();
  const [board, setBoard] = useState<Storyboard | null>(null);
  const [frameModel, setFrameModel] = useState(FRAME_MODELS[0]);
  const [clipModel, setClipModel] = useState(CLIP_MODELS[0]);
  const [error, setError] = useState<string | null>(null);
  const byId = useMemo(() => new Map(store.items.map((g) => [g.id, g])), [store.items]);
  const characters = board?.characters ?? [];
  // A frame/clip needs (re)doing if it was never made, failed, or was deleted from the library.
  const needs = (id?: string) => { const g = id ? byId.get(id) : undefined; return !g || g.status === "failed"; };

  const update = (b: Storyboard) => {
    const next = { ...b, updatedAt: Date.now() };
    setBoard(next);
    store.saveBoard(next);
  };
  // Async runs read the latest saved board so parallel updates don't clobber each other.
  const patchScene = (boardId: string, sceneId: string, p: Partial<Scene>) => {
    const latest = snapshot().boards.find((b) => b.id === boardId);
    if (!latest) return;
    update({ ...latest, scenes: latest.scenes.map((s) => (s.id === sceneId ? { ...s, ...p } : s)) });
  };

  async function makeFrame(b: Storyboard, scene: Scene) {
    if (!scene.text.trim()) return;
    const prompt = `${scene.text.trim()}. Style: ${b.style}`;
    const chars = (snapshot().boards.find((x) => x.id === b.id) ?? b).characters ?? [];
    const id = chars.length
      ? await submitGeneration("character-multi", withAspect("character-multi", { prompt, images: chars }, b.aspect), store.add, store.patch)
      : await submitGeneration(frameModel, withAspect(frameModel, { prompt }, b.aspect), store.add, store.patch);
    patchScene(b.id, scene.id, { frameGenId: id, clipGenId: undefined });
  }

  async function makeClip(b: Storyboard, scene: Scene) {
    const frame = scene.frameGenId && byId.get(scene.frameGenId);
    if (!frame || frame.status !== "done") return;
    const id = await submitGeneration(clipModel, withAspect(clipModel, { prompt: scene.text, image: frame.urls[0] }, b.aspect), store.add, store.patch);
    patchScene(b.id, scene.id, { clipGenId: id });
  }

  async function run(fn: () => Promise<unknown>) {
    setError(null);
    try {
      await fn();
    } catch (e) {
      setError((e as Error).message);
    }
  }

  if (!board) {
    return (
      <div className="section">
        <div className="feed-head" style={{ marginBottom: 14 }}>
          <div><h1 style={{ margin: 0 }}>Storyboard</h1><div className="hint">Write scenes, generate a frame for each, then animate them into clips.</div></div>
          <button className="btn-primary" style={{ width: "auto" }} onClick={() => update(blank())}>New storyboard</button>
        </div>
        {store.boards.length === 0 ? <div className="empty">No storyboards yet.</div> : (
          <div className="tiles">
            {store.boards.map((b) => {
              const first = b.scenes.map((s) => s.frameGenId && byId.get(s.frameGenId)).find((g) => g && g.status === "done");
              return (
                <div key={b.id} className="tile" onClick={() => setBoard(b)} style={{ cursor: "pointer" }}>
                  {first ? <img className="swatch" style={{ objectFit: "cover", width: "100%" }} src={first.urls[0]} alt="" /> : <div className="swatch" style={{ background: "var(--panel-2)" }} />}
                  <h3>{b.title}</h3>
                  <p>{b.scenes.length} scenes · {b.aspect}</p>
                  <button className="icon-btn" style={{ alignSelf: "flex-end" }} onClick={(e) => { e.stopPropagation(); store.deleteBoard(b.id); }}>Delete</button>
                </div>
              );
            })}
          </div>
        )}
      </div>
    );
  }

  const b = board;
  return (
    <div className="section">
      <div className="row-inline" style={{ marginBottom: 12 }}>
        <button className="btn" onClick={() => setBoard(null)}>← All storyboards</button>
        <input className="title-input" value={b.title} onChange={(e) => update({ ...b, title: e.target.value })} />
      </div>
      <div className="board-settings">
        <div><div className="field-label">Visual style (added to every frame)</div>
          <input className="select" value={b.style} onChange={(e) => update({ ...b, style: e.target.value })} /></div>
        <div><div className="field-label">Aspect ratio</div>
          <div className="chips">{ASPECTS.map((a) => <button key={a} className={`chip ${a === b.aspect ? "on" : ""}`} onClick={() => update({ ...b, aspect: a })}>{a}</button>)}</div></div>
        <div><div className="field-label">Frame model</div>
          <select className="select" value={frameModel} onChange={(e) => setFrameModel(e.target.value)} disabled={characters.length > 0}>
            {FRAME_MODELS.map((id) => <option key={id} value={id}>{getModel(id)!.name}</option>)}
          </select></div>
        <div><div className="field-label">Clip model</div>
          <select className="select" value={clipModel} onChange={(e) => setClipModel(e.target.value)}>
            {CLIP_MODELS.map((id) => <option key={id} value={id}>{getModel(id)!.name}</option>)}
          </select></div>
        <div style={{ gridColumn: "1 / -1" }}>
          <ImagesField label="Recurring character (optional): keeps the same face in every frame" max={4} value={characters} onChange={(c) => update({ ...b, characters: c })} />
        </div>
      </div>
      <div className="row-inline" style={{ margin: "14px 0" }}>
        <button className="btn" onClick={() => run(() => Promise.all(b.scenes.filter((s) => needs(s.frameGenId)).map((s) => makeFrame(b, s))))}>Generate missing frames</button>
        <button className="btn" onClick={() => run(() => Promise.all(b.scenes.filter((s) => needs(s.clipGenId)).map((s) => makeClip(b, s))))}>Animate all frames</button>
        {error && <span className="error">{error}</span>}
      </div>
      <div className="scenes">
        {b.scenes.map((scene, i) => {
          const frame = scene.frameGenId ? byId.get(scene.frameGenId) : undefined;
          const clip = scene.clipGenId ? byId.get(scene.clipGenId) : undefined;
          return (
            <div key={scene.id} className="scene">
              <div className="scene-head">
                <strong>Scene {i + 1}</strong>
                <span className="grow" />
                <button className="icon-btn" disabled={i === 0} onClick={() => { const s = [...b.scenes]; [s[i - 1], s[i]] = [s[i], s[i - 1]]; update({ ...b, scenes: s }); }}>↑</button>
                <button className="icon-btn" disabled={i === b.scenes.length - 1} onClick={() => { const s = [...b.scenes]; [s[i + 1], s[i]] = [s[i], s[i + 1]]; update({ ...b, scenes: s }); }}>↓</button>
                <button className="icon-btn" onClick={() => update({ ...b, scenes: b.scenes.filter((x) => x.id !== scene.id) })}>✕</button>
              </div>
              <textarea className="prompt" style={{ minHeight: 70 }} placeholder="What happens in this shot?" value={scene.text}
                onChange={(e) => update({ ...b, scenes: b.scenes.map((s) => (s.id === scene.id ? { ...s, text: e.target.value } : s)) })} />
              <div className="scene-media">
                <div className="slot">
                  {!frame ? <span className="hint">No frame yet</span> : frame.status === "pending" ? <div className="pending">Frame…</div>
                    : frame.status === "failed" ? <span className="error">{frame.error}</span> : <img src={frame.urls[0]} alt="" />}
                </div>
                <div className="slot">
                  {!clip ? <span className="hint">No clip yet</span> : clip.status === "pending" ? <div className="pending">Clip…</div>
                    : clip.status === "failed" ? <span className="error">{clip.error}</span>
                    : clip.urls[0].startsWith("data:image") ? <img className="kenburns" src={clip.urls[0]} alt="" /> : <video src={clip.urls[0]} muted loop autoPlay playsInline controls />}
                </div>
              </div>
              <div className="row-inline">
                <button className="btn" disabled={!scene.text.trim()} onClick={() => run(() => makeFrame(b, scene))}>{frame ? "Redo frame" : "Make frame"}</button>
                <button className="btn" disabled={frame?.status !== "done"} onClick={() => run(() => makeClip(b, scene))}>{clip ? "Redo clip" : "Animate"}</button>
              </div>
            </div>
          );
        })}
        <button className="scene add-scene" onClick={() => update({ ...b, scenes: [...b.scenes, { id: newId(), text: "" }] })}>+ Add scene</button>
      </div>
    </div>
  );
}
