"use client";
import { useState } from "react";
import { getModel } from "@/lib/models";
import type { Generation } from "@/lib/store";


export default function MediaCard({
  g,
  onRemove,
  onReuse,
}: {
  g: Generation;
  onRemove?: (id: string) => void;
  onReuse?: (g: Generation) => void;
}) {
  const [open, setOpen] = useState<string | null>(null);
  const model = getModel(g.modelId);
  const urls = g.urls.length ? g.urls : [""];
  const isVideo = (u: string) => g.mode === "video" && !u.startsWith("data:");

  return (
    <>
      {urls.map((url, i) => (
        <div className="card" key={g.id + i}>
          <div className="media" onClick={() => url && setOpen(url)}>
            {g.status === "pending" && <div className="pending">Generating…</div>}
            {g.status === "failed" && <div className="pending error">{g.error ?? "Failed"}</div>}
            {g.status === "done" && url && (isVideo(url) ? (
              <video src={url} muted loop autoPlay playsInline />
            ) : (
              <img src={url} alt={g.prompt} className={g.mode === "video" && g.demo ? "kenburns" : ""} />
            ))}
          </div>
          <div className="meta">
            <p>{g.prompt}</p>
            <div className="row">
              <span className="grow">
                {model?.name ?? g.modelId} · {g.aspectRatio}
                {g.demo ? " · demo" : ""}
              </span>
              {onReuse && (
                <button className="icon-btn" title="Reuse settings" onClick={() => onReuse(g)}>↺</button>
              )}
              {url && g.status === "done" && (
                <a className="icon-btn" href={url} download target="_blank" rel="noreferrer" title="Download">↓</a>
              )}
              {onRemove && (
                <button className="icon-btn" title="Delete" onClick={() => onRemove(g.id)}>✕</button>
              )}
            </div>
          </div>
        </div>
      ))}
      {open && (
        <div className="lightbox" onClick={() => setOpen(null)}>
          <div onClick={(e) => e.stopPropagation()}>
            {isVideo(open) ? <video src={open} controls autoPlay /> : <img src={open} alt={g.prompt} />}
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
