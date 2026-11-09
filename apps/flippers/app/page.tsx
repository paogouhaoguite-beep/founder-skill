import Link from "next/link";
import { MODELS, TOOLS } from "@/lib/catalog";
import { PRESETS } from "@/lib/presets";

const PROJECTS = [
  { href: "/studios", tag: "Templates", title: "Studios", body: "Ready-made setups for ads, shorts, virtual influencers and marketing." },
  { href: "/storyboard", tag: "Multi-shot", title: "Storyboard", body: "Write scenes, generate a frame for each, keep one character throughout, animate into clips." },
  { href: "/canvas", tag: "Moodboard", title: "Canvas", body: "Collect generations and notes on a free board to plan a project." },
  { href: "/library", tag: "Archive", title: "Library", body: "Everything you've made. Search, download, reuse, or send to another tool." },
];

export default function Explore() {
  return (
    <main>
      <section className="hero">
        <h1>Make it.<br /><em>Flip it.</em></h1>
        <p>
          Your own studio for images, video, voice and music: {MODELS.length} models behind one set of controls,
          with every result one click away from being animated, edited, upscaled or given a voice.
        </p>
        <div className="cta">
          <Link href="/image" className="btn-primary" style={{ width: "auto" }}>Create an image</Link>
          <Link href="/video" className="btn">Make a video</Link>
          <Link href="/studios" className="btn">Browse templates</Link>
        </div>
      </section>

      {(["Create", "Edit"] as const).map((group) => (
        <section className="section" key={group}>
          <h2>{group}</h2>
          <div className="tiles">
            {TOOLS.filter((t) => t.group === group).map((t) => (
              <Link key={t.id} href={`/${t.id}`} className="tile">
                <span className="tag">{(() => { const c = MODELS.filter((m) => m.tool === t.id).length; return `${c} model${c === 1 ? "" : "s"}`; })()}</span>
                <h3>{t.name}</h3>
                <p>{t.blurb}</p>
              </Link>
            ))}
          </div>
        </section>
      ))}

      <section className="section">
        <h2>Projects</h2>
        <div className="tiles">
          {PROJECTS.map((p) => (
            <Link key={p.href} href={p.href} className="tile">
              <span className="tag">{p.tag}</span>
              <h3>{p.title}</h3>
              <p>{p.body}</p>
            </Link>
          ))}
        </div>
      </section>

      <section className="section">
        <h2>All models</h2>
        <div className="model-table">
          {MODELS.map((m) => (
            <Link key={m.id} href={`/${m.tool}?model=${m.id}`}>
              <strong>{m.name}</strong>
              <span>{m.tagline}</span>
              <span className="tag">{TOOLS.find((t) => t.id === m.tool)!.name}</span>
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
