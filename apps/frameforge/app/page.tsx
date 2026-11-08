import Link from "next/link";
import { MODELS } from "@/lib/models";
import { PRESETS } from "@/lib/presets";

const TOOLS = [
  { href: "/image", tag: "Create", title: "Image studio", body: "Text-to-image across several models, up to four variations per run." },
  { href: "/image?model=kontext-edit", tag: "Edit", title: "Edit with words", body: "Upload a photo and describe the change: new background, outfit, lighting." },
  { href: "/video", tag: "Animate", title: "Video studio", body: "Turn a prompt or a still image into a short clip, with camera presets." },
  { href: "/video?preset=orbit", tag: "Presets", title: "Camera moves", body: "Orbit, push-in, crane, FPV and more, all in one click on any video model." },
  { href: "/library", tag: "Organize", title: "Library", body: "Every generation in one place. Search, download and reuse settings." },
  { href: "/pricing", tag: "Credits", title: "Pay per result", body: "One credit balance for every model. You only spend on what you generate." },
];

export default function Explore() {
  return (
    <main>
      <section className="hero">
        <h1>
          Every frame,<br /><em>one studio.</em>
        </h1>
        <p>
          Frameforge brings leading image and video models together behind one prompt box, with camera presets,
          reference images and a shared library.
        </p>
        <div className="cta">
          <Link href="/image" className="btn-primary" style={{ width: "auto" }}>Create an image</Link>
          <Link href="/video" className="btn">Make a video</Link>
        </div>
      </section>

      <section className="section">
        <h2>Tools</h2>
        <div className="tiles">
          {TOOLS.map((t) => (
            <Link key={t.title} href={t.href} className="tile">
              <span className="tag">{t.tag}</span>
              <h3>{t.title}</h3>
              <p>{t.body}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Models</h2>
        <div className="tiles">
          {MODELS.map((m) => (
            <Link key={m.id} href={`/${m.mode}?model=${m.id}`} className="tile">
              <span className="tag">{m.mode}</span>
              <h3>{m.name}</h3>
              <p>{m.tagline}</p>
              <p>✦ {m.cost}{m.mode === "video" ? " per second" : " per image"}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>Camera &amp; motion presets</h2>
        <div className="tiles">
          {PRESETS.filter((p) => p.id !== "freeform").map((p) => (
            <Link key={p.id} href={`/video?preset=${p.id}`} className="tile" style={{ minHeight: 0 }}>
              <div className="swatch" style={{ background: `linear-gradient(160deg, hsl(${p.hue},60%,42%), hsl(${(p.hue + 50) % 360},55%,16%))` }} />
              <span className="tag">{p.category}</span>
              <h3>{p.name}</h3>
              <p>{p.prompt}</p>
            </Link>
          ))}
        </div>
      </section>
    </main>
  );
}
