"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { getModel } from "@/lib/catalog";
import { useStore, type Generation } from "@/lib/store";
import { handoff, urlToInput } from "@/lib/upload";
import { newId } from "@/lib/jobs";

function Media({ g, url, big }: { g: Generation; url: string; big?: boolean }) {
  // Demo video/audio output is a placeholder still or chime.
  if (g.output === "audio") return <div className="audio-tile"><span>♪</span><audio src={url} controls /></div>;
  if (g.output === "video" && !url.startsWith("data:image")) {
    return <video src={url} muted={!big} loop autoPlay playsInline controls={big} />;
  }
  return <img src={url} alt={g.prompt} className={g.output === "video" ? "kenburns" : ""} />;
}

export default function MediaCard({ g, onRemove, onReuse }: {
  g: Generation; onRemove?: (id: string) => void; onReuse?: (g: Generation) => void;
}) {
  const router = useRouter();
  const { setCanvas } = useStore();
  const [open, setOpen] = useState<string | null>(null);
  const [menu, setMenu] = useState(false);
  const model = getModel(g.modelId);
  const urls = g.urls.length ? g.urls : [""];
  const isImage = g.output === "image";
  const isVideo = g.output === "video";

  async function send(tool: string, modelId: string | undefined, key: string, url: string) {
    const file = await urlToInput(url);
    const values: Record<string, unknown> = { [key]: file };
    if (key === "image") values.images = [file];
    handoff(tool, { modelId, values });
    router.push(`/${tool}`);
  }

  function toCanvas(url: string) {
    setCanvas((c) => [...c, { id: newId(), kind: "media", genId: g.id, url, output: g.output,
      x: 40 + (c.length % 10) * 48 + Math.floor(c.length / 10) * 260, y: 40 + (c.length % 10) * 36, w: 240 }]);
    setMenu(false);
  }

  return (
    <>
      {urls.map((url, i) => (
        <div className="card" key={g.id + i}>
          <div className={`media ${g.output === "audio" ? "is-audio" : ""}`} onClick={() => url && g.output !== "audio" && setOpen(url)}>
            {g.status === "pending" && <div className="pending">Generating…</div>}
            {g.status === "failed" && <div className="pending error">{g.error ?? "Failed"}</div>}
            {g.status === "done" && url && <Media g={g} url={url} />}
          </div>
          <div className="meta">
            <p>{g.prompt}</p>
            <div className="row">
              <span className="grow">{model?.name ?? g.modelId}{g.demo ? " · demo" : ""}</span>
              {onReuse && <button className="icon-btn" title="Reuse settings" onClick={() => onReuse(g)}>↺</button>}
              {url && g.status === "done" && (
                <>
                  <a className="icon-btn" href={url} download target="_blank" rel="noreferrer" title="Download">↓</a>
                  <button className="icon-btn" title="More actions" onClick={() => setMenu((m) => !m)}>⋯</button>
                </>
              )}
              {onRemove && <button className="icon-btn" title="Delete" onClick={() => onRemove(g.id)}>✕</button>}
            </div>
            {menu && url && (
              <div className="actions">
                {isImage && <button onClick={() => send("video", undefined, "image", url)}>Animate</button>}
                {isImage && <button onClick={() => send("edit", undefined, "image", url)}>Edit</button>}
                {isImage && <button onClick={() => send("upscale", "seedvr-image", "image", url)}>Upscale</button>}
                {isImage && <button onClick={() => send("character", undefined, "image", url)}>Use as character</button>}
                {isImage && <button onClick={() => send("lipsync", "omnihuman", "image", url)}>Make it talk</button>}
                {isVideo && <button onClick={() => send("upscale", "seedvr-video", "video", url)}>Upscale</button>}
                {isVideo && <button onClick={() => send("audio", "video-to-audio", "video", url)}>Add sound</button>}
                {isVideo && <button onClick={() => send("lipsync", undefined, "video", url)}>Lipsync</button>}
                {g.output === "audio" && <button onClick={() => send("lipsync", undefined, "audio", url)}>Use for lipsync</button>}
                {g.output !== "audio" && <button onClick={() => toCanvas(url)}>Add to canvas</button>}
              </div>
            )}
          </div>
        </div>
      ))}
      {open && (
        <div className="lightbox" onClick={() => setOpen(null)}>
          <div onClick={(e) => e.stopPropagation()}>
            <Media g={g} url={open} big />
            <div className="bar">
              <a className="btn" href={open} download target="_blank" rel="noreferrer">Download</a>
              <button className="btn" onClick={() => setOpen(null)}>Close</button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
