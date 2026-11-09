"use client";
import { useEffect, useRef, useState } from "react";
import { uploadFile } from "@/lib/upload";
import { PRESETS } from "@/lib/presets";

const ACCEPT = { image: "image/*", video: "video/*", audio: "audio/*" } as const;

function Preview({ kind, url }: { kind: keyof typeof ACCEPT; url: string }) {
  if (kind === "image") return <img src={url} alt="" />;
  if (kind === "video") return <video src={url} muted controls playsInline />;
  return <audio src={url} controls />;
}

/** Drop zone that uploads one file and reports its URL. */
export function FileField({ kind, label, hint, value, onChange }: {
  kind: keyof typeof ACCEPT; label: string; hint?: string; value?: string; onChange: (url?: string) => void;
}) {
  const input = useRef<HTMLInputElement>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function take(file?: File) {
    if (!file) return;
    if (!file.type.startsWith(kind)) return setError(`That isn't ${kind === "audio" ? "an audio" : `a ${kind}`} file`);
    setError(null);
    setBusy(true);
    try {
      onChange(await uploadFile(file));
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div>
      <div className="field-label">{label}</div>
      <div className="dropzone" onClick={() => !value && input.current?.click()}
        onDragOver={(e) => e.preventDefault()}
        onDrop={(e) => { e.preventDefault(); take(e.dataTransfer.files[0]); }}>
        {busy ? <span>Uploading…</span> : value ? (
          <>
            <Preview kind={kind} url={value} />
            <button type="button" className="btn clear" onClick={(e) => { e.stopPropagation(); onChange(undefined); }}>✕</button>
          </>
        ) : (
          <span>Drop {kind === "audio" ? "an audio file" : `a${kind === "image" ? "n" : ""} ${kind}`} or click to upload{hint ? <><br /><small>{hint}</small></> : null}</span>
        )}
      </div>
      {error && <div className="error">{error}</div>}
      <input ref={input} type="file" accept={ACCEPT[kind]} hidden
        onChange={(e) => { take(e.target.files?.[0]); e.target.value = ""; }} />
    </div>
  );
}

/** Up to `max` images, uploaded individually. */
export function ImagesField({ label, hint, max, value, onChange }: {
  label: string; hint?: string; max: number; value?: string[]; onChange: (urls: string[]) => void;
}) {
  const input = useRef<HTMLInputElement>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const urls = value ?? [];

  async function take(files: FileList | null) {
    if (!files?.length) return;
    setError(null);
    setBusy(true);
    try {
      const picked = [...files].filter((f) => f.type.startsWith("image")).slice(0, max - urls.length);
      const uploaded = await Promise.all(picked.map(uploadFile));
      onChange([...urls, ...uploaded]);
    } catch (e) {
      setError((e as Error).message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div>
      <div className="field-label">{label} ({urls.length}/{max})</div>
      <div className="thumbs">
        {urls.map((u, i) => (
          <div key={u + i} className="thumb">
            <img src={u} alt={`Reference ${i + 1}`} />
            <span className="badge">{i + 1}</span>
            <button type="button" onClick={() => onChange(urls.filter((_, j) => j !== i))}>✕</button>
          </div>
        ))}
        {urls.length < max && (
          <button type="button" className="thumb add" onClick={() => input.current?.click()}
            onDragOver={(e) => e.preventDefault()} onDrop={(e) => { e.preventDefault(); take(e.dataTransfer.files); }}>
            {busy ? "…" : "+"}
          </button>
        )}
      </div>
      {hint && <div className="hint">{hint}</div>}
      {error && <div className="error">{error}</div>}
      <input ref={input} type="file" accept="image/*" multiple hidden
        onChange={(e) => { take(e.target.files); e.target.value = ""; }} />
    </div>
  );
}

/** Paint over an image; produces a black/white PNG mask at the image's size. */
export function MaskPainter({ label, imageUrl, value, onChange }: {
  label: string; imageUrl?: string; value?: string; onChange: (url?: string) => void;
}) {
  const canvas = useRef<HTMLCanvasElement>(null);
  const drawing = useRef(false);
  const timer = useRef<ReturnType<typeof setTimeout>>(undefined);
  const [brush, setBrush] = useState(40);
  const [size, setSize] = useState<[number, number] | null>(null);
  const [status, setStatus] = useState("");

  useEffect(() => {
    setSize(null);
    onChange(undefined);
    if (!imageUrl) return;
    const img = new Image();
    img.onload = () => setSize([img.naturalWidth, img.naturalHeight]);
    img.src = imageUrl;
  }, [imageUrl]); // eslint-disable-line react-hooks/exhaustive-deps

  if (!imageUrl) return <div><div className="field-label">{label}</div><div className="hint">Upload an image first.</div></div>;

  const scale = () => {
    const c = canvas.current!;
    return c.width / c.getBoundingClientRect().width;
  };
  const point = (e: React.PointerEvent) => {
    const r = canvas.current!.getBoundingClientRect();
    const k = scale();
    return [(e.clientX - r.left) * k, (e.clientY - r.top) * k] as const;
  };
  const paint = (e: React.PointerEvent) => {
    const ctx = canvas.current!.getContext("2d")!;
    const [x, y] = point(e);
    ctx.fillStyle = "rgba(255,122,69,0.6)";
    ctx.beginPath();
    ctx.arc(x, y, (brush * scale()) / 2, 0, Math.PI * 2);
    ctx.fill();
  };

  // Turn the painted overlay into a strict black/white mask and upload it.
  function commit() {
    clearTimeout(timer.current);
    timer.current = setTimeout(async () => {
      const src = canvas.current!;
      const out = document.createElement("canvas");
      out.width = src.width;
      out.height = src.height;
      const octx = out.getContext("2d")!;
      const data = src.getContext("2d")!.getImageData(0, 0, src.width, src.height);
      let painted = 0;
      for (let i = 0; i < data.data.length; i += 4) {
        const on = data.data[i + 3] > 0;
        if (on) painted++;
        data.data[i] = data.data[i + 1] = data.data[i + 2] = on ? 255 : 0;
        data.data[i + 3] = 255;
      }
      if (!painted) return onChange(undefined);
      octx.putImageData(data, 0, 0);
      setStatus("Saving mask…");
      const blob = await new Promise<Blob>((r) => out.toBlob((b) => r(b!), "image/png"));
      try {
        onChange(await uploadFile(blob));
        setStatus("");
      } catch (e) {
        setStatus((e as Error).message);
      }
    }, 500);
  }

  function clear() {
    const c = canvas.current!;
    c.getContext("2d")!.clearRect(0, 0, c.width, c.height);
    onChange(undefined);
  }

  return (
    <div>
      <div className="field-label">{label}</div>
      <div className="mask-wrap">
        <img src={imageUrl} alt="" />
        {size && (
          <canvas ref={canvas} width={size[0]} height={size[1]}
            onPointerDown={(e) => { drawing.current = true; e.currentTarget.setPointerCapture(e.pointerId); paint(e); }}
            onPointerMove={(e) => drawing.current && paint(e)}
            onPointerUp={() => { drawing.current = false; commit(); }} />
        )}
      </div>
      <div className="row-inline">
        <span className="hint">Brush</span>
        <input type="range" min={10} max={120} value={brush} onChange={(e) => setBrush(Number(e.target.value))} />
        <button type="button" className="btn" onClick={clear}>Clear</button>
        <span className="hint">{status || (value ? "Mask ready" : "")}</span>
      </div>
    </div>
  );
}

export function PresetPicker({ label, value, onChange }: { label: string; value?: string; onChange: (id: string) => void }) {
  return (
    <div>
      <div className="field-label">{label}</div>
      <div className="presets">
        {PRESETS.map((p) => (
          <button type="button" key={p.id} className={`preset ${value === p.id ? "on" : ""}`}
            style={{ background: `linear-gradient(160deg, hsl(${p.hue},60%,42%), hsl(${(p.hue + 50) % 360},55%,16%))` }}
            onClick={() => onChange(p.id)} title={p.prompt || "No camera instruction"}>
            {p.name}
          </button>
        ))}
      </div>
    </div>
  );
}
