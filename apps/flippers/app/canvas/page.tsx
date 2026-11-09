"use client";
import { useRef, useState } from "react";
import { useStore, type BoardItem } from "@/lib/store";
import { newId } from "@/lib/jobs";

const WIDTHS = [160, 240, 360];
// Cascade new items so they don't land exactly on top of each other.
const spot = (n: number) => ({ x: 40 + (n % 10) * 48 + Math.floor(n / 10) * 260, y: 40 + (n % 10) * 36 });

export default function CanvasPage() {
  const { canvas, setCanvas, items } = useStore();
  const [picker, setPicker] = useState(false);
  const drag = useRef<{ id: string; dx: number; dy: number } | null>(null);
  const area = useRef<HTMLDivElement>(null);
  const recent = items.filter((g) => g.status === "done" && g.output !== "audio").slice(0, 40);

  const move = (id: string, p: Partial<BoardItem>) => setCanvas((c) => c.map((x) => (x.id === id ? { ...x, ...p } : x)));
  const remove = (id: string) => setCanvas((c) => c.filter((x) => x.id !== id));
  const toTop = (id: string) => setCanvas((c) => { const it = c.find((x) => x.id === id); return it ? [...c.filter((x) => x.id !== id), it] : c; });

  function onDown(e: React.PointerEvent, it: BoardItem) {
    if ((e.target as HTMLElement).closest("button, textarea")) return;
    const r = area.current!.getBoundingClientRect();
    drag.current = { id: it.id, dx: e.clientX - r.left + area.current!.scrollLeft - it.x, dy: e.clientY - r.top + area.current!.scrollTop - it.y };
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
    toTop(it.id);
  }
  function onMove(e: React.PointerEvent) {
    const d = drag.current;
    if (!d) return;
    const r = area.current!.getBoundingClientRect();
    move(d.id, {
      x: Math.max(0, e.clientX - r.left + area.current!.scrollLeft - d.dx),
      y: Math.max(0, e.clientY - r.top + area.current!.scrollTop - d.dy),
    });
  }

  const addNote = () => setCanvas((c) => [...c, { id: newId(), kind: "note", text: "", ...spot(c.length), w: 200 }]);
  const addMedia = (url: string, genId: string, output: BoardItem["output"]) =>
    setCanvas((c) => [...c, { id: newId(), kind: "media", url, genId, output, ...spot(c.length), w: 240 }]);

  return (
    <div className="canvas-page">
      <div className="canvas-bar">
        <h1>Canvas</h1>
        <span className="hint">Moodboard: drag things around, add notes, collect references.</span>
        <span className="grow" />
        <button className="btn" onClick={() => setPicker((p) => !p)}>{picker ? "Close library" : "Add from library"}</button>
        <button className="btn" onClick={addNote}>Add note</button>
        <button className="btn" onClick={() => canvas.length && confirm("Clear the whole canvas?") && setCanvas(() => [])}>Clear</button>
      </div>
      {picker && (
        <div className="picker">
          {recent.length === 0 ? <span className="hint">Generate something first.</span> : recent.flatMap((g) => g.urls.slice(0, 1).map((u) => (
            <button key={g.id} className="thumb" onClick={() => addMedia(u, g.id, g.output)} title={g.prompt}>
              {g.output === "video" && !u.startsWith("data:image") ? <video src={u} muted /> : <img src={u} alt="" />}
            </button>
          )))}
        </div>
      )}
      <div className="canvas-area" ref={area} onPointerMove={onMove} onPointerUp={() => (drag.current = null)}>
        {canvas.length === 0 && <div className="canvas-empty">Empty board. Add images from your library or a note.</div>}
        {canvas.map((it) => (
          <div key={it.id} className={`board-item ${it.kind}`} style={{ left: it.x, top: it.y, width: it.w }} onPointerDown={(e) => onDown(e, it)}>
            <div className="board-tools">
              {WIDTHS.map((w, i) => <button key={w} className={it.w === w ? "on" : ""} onClick={() => move(it.id, { w })}>{"SML"[i]}</button>)}
              <button onClick={() => remove(it.id)}>✕</button>
            </div>
            {it.kind === "note" ? (
              <>
              <div className="note-handle" title="Drag to move" />
              <textarea value={it.text} placeholder="Note…" onChange={(e) => move(it.id, { text: e.target.value })} />
              </>
            ) : it.output === "video" && !it.url?.startsWith("data:image") ? (
              <video src={it.url} muted loop autoPlay playsInline />
            ) : (
              <img src={it.url} alt="" draggable={false} />
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
