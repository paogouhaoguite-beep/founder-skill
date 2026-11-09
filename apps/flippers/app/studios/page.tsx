"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { defaultValues, getModel, type Values } from "@/lib/catalog";
import { handoff } from "@/lib/upload";

// Ready-made starting points. Each opens a tool with the model, prompt and
// settings filled in; replace the [bracketed] parts with your own details.
interface Template { name: string; studio: Studio; blurb: string; tool: string; modelId: string; values: Values; needs?: string }
type Studio = "Ads" | "Shorts" | "Influencer" | "Marketing";

const T: Template[] = [
  { studio: "Ads", name: "Product hero shot", tool: "edit", modelId: "nano-edit", needs: "Upload your product photo",
    blurb: "Your product on a premium set with studio lighting.",
    values: { prompt: "Place the product from image 1 on a [polished marble pedestal] with soft studio lighting and gentle reflections, premium advertising photo, no text", aspect: "1:1" } },
  { studio: "Ads", name: "Product turntable", tool: "video", modelId: "kling", needs: "Upload a product photo as the start frame",
    blurb: "A slow orbit around your product with light sweeping across it.",
    values: { prompt: "The [product] rotates slowly on a dark set as a soft light sweeps across its surface, premium commercial", preset: "orbit" } },
  { studio: "Ads", name: "Selfie-style testimonial", tool: "video", modelId: "veo31",
    blurb: "A handheld vertical clip of someone recommending a product, with spoken audio.",
    values: { prompt: "A [friendly woman in her 30s] in her kitchen holds [a green coffee tin] to the phone camera and says: \"[I stopped buying coffee out. This is better.]\" Handheld selfie video, natural light", aspect: "9:16", preset: "handheld", audio: true } },
  { studio: "Ads", name: "Before / after", tool: "edit", modelId: "kontext", needs: "Upload the 'before' photo",
    blurb: "Show the transformation your product makes.",
    values: { prompt: "Show the same scene after [a professional deep clean]: spotless, bright, organized, same camera angle" } },

  { studio: "Shorts", name: "Scroll-stopping hook", tool: "video", modelId: "seedance",
    blurb: "A punchy vertical opener with a crash zoom.",
    values: { prompt: "[A chef slams a knife into a cutting board], dramatic lighting, high energy", aspect: "9:16", preset: "crash-zoom", duration: "3" } },
  { studio: "Shorts", name: "Faceless explainer frame", tool: "image", modelId: "nano-banana",
    blurb: "Clean vertical illustration for a voiceover video.",
    values: { prompt: "Minimal flat illustration explaining [how compound interest grows money over time], bold shapes, limited palette, lots of empty space at the top for captions", aspect: "9:16", count: 2 } },
  { studio: "Shorts", name: "Narration", tool: "audio", modelId: "tts",
    blurb: "Voiceover for your short.",
    values: { prompt: "[Most people never notice this.] But once you see it, you can't unsee it. Here's why." } },
  { studio: "Shorts", name: "Background track", tool: "audio", modelId: "music",
    blurb: "A short instrumental bed under your voiceover.",
    values: { prompt: "[Driving minimal electronic beat], curious and upbeat, builds slightly, no vocals", length: "30s", instrumental: true } },

  { studio: "Influencer", name: "Design your persona", tool: "image", modelId: "flux-ultra",
    blurb: "A photoreal portrait of an original virtual creator.",
    values: { prompt: "Candid portrait of [a 26-year-old surfer with sun-bleached curly hair and freckles], natural light, shot on 50mm, realistic skin texture", aspect: "3:4", count: 4 } },
  { studio: "Influencer", name: "Same persona, new place", tool: "character", modelId: "character-multi", needs: "Upload 1–4 photos of your persona",
    blurb: "Put your persona in a new scene with the same face.",
    values: { prompt: "Same character [drinking coffee at a busy Lisbon cafe terrace], candid lifestyle photo, golden hour", aspect: "4:3" } },
  { studio: "Influencer", name: "Talking persona", tool: "lipsync", modelId: "omnihuman", needs: "Upload a portrait and a voice clip",
    blurb: "Make a portrait speak your script.", values: {} },

  { studio: "Marketing", name: "Launch poster", tool: "image", modelId: "ideogram",
    blurb: "A poster with a crisp, readable headline.",
    values: { prompt: "Bold launch poster for [a running shoe called 'DRIFT'], headline text \"[DRIFT. RUN LIGHTER.]\", dynamic composition, modern sports branding", aspect: "3:4", style: "DESIGN" } },
  { studio: "Marketing", name: "Social banner", tool: "image", modelId: "ideogram",
    blurb: "A wide header image for a profile or newsletter.",
    values: { prompt: "Wide banner for [a plant shop called 'Fern & Co'], text \"[Fern & Co]\", lush greenery, airy and calm", aspect: "16:9", style: "DESIGN" } },
  { studio: "Marketing", name: "Lifestyle photo", tool: "image", modelId: "seedream",
    blurb: "Your product in real life.",
    values: { prompt: "Lifestyle photo of [a ceramic pour-over coffee set] on a sunlit wooden table, morning, steam rising, editorial look", aspect: "4:3", count: 2 } },
  { studio: "Marketing", name: "Sound logo", tool: "audio", modelId: "sfx",
    blurb: "A short audio signature for videos and ads.",
    values: { prompt: "[Bright, playful three-note chime with a soft whoosh], modern tech brand sound logo", seconds: "2" } },
];

const STUDIOS: Studio[] = ["Ads", "Shorts", "Influencer", "Marketing"];

export default function StudiosPage() {
  const router = useRouter();
  const [studio, setStudio] = useState<Studio | "All">("All");
  const shown = T.filter((t) => studio === "All" || t.studio === studio);

  function open(t: Template) {
    const model = getModel(t.modelId)!;
    handoff(t.tool, { modelId: t.modelId, values: { ...defaultValues(model), ...t.values } });
    router.push(`/${t.tool}`);
  }

  return (
    <div className="section">
      <div className="feed-head" style={{ marginBottom: 14, flexWrap: "wrap", gap: 12 }}>
        <div><h1 style={{ margin: 0 }}>Studios</h1><div className="hint">Templates for common jobs. Open one, swap the [bracketed] parts, generate.</div></div>
        <div className="chips">
          {(["All", ...STUDIOS] as const).map((s) => <button key={s} className={`chip ${s === studio ? "on" : ""}`} onClick={() => setStudio(s)}>{s}</button>)}
        </div>
      </div>
      <div className="tiles">
        {shown.map((t) => (
          <button key={t.name} className="tile" style={{ textAlign: "left" }} onClick={() => open(t)}>
            <span className="tag">{t.studio} · {getModel(t.modelId)!.name}</span>
            <h3>{t.name}</h3>
            <p>{t.blurb}</p>
            {t.needs && <p className="hint">↳ {t.needs}</p>}
          </button>
        ))}
      </div>
    </div>
  );
}
