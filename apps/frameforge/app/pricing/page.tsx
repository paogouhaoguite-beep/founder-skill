"use client";
import { useStore } from "@/lib/store";

const PACKS = [
  { name: "Starter", credits: 300, price: "$9", blurb: "About 150 Flux images or 30s of Kling video." },
  { name: "Creator", credits: 1200, price: "$29", blurb: "Best for weekly content. Every model included." },
  { name: "Studio", credits: 5000, price: "$99", blurb: "For teams and heavy video work." },
];

export default function PricingPage() {
  const { credits, topUp } = useStore();
  return (
    <div className="section">
      <h1>Credits</h1>
      <p className="hint">
        Balance: ✦ {credits}. Images cost credits per image and video costs credits per second, as shown next to each model.
        Payments aren&apos;t connected yet, so these buttons add credits locally for testing.
      </p>
      <div className="tiles" style={{ marginTop: 16 }}>
        {PACKS.map((p) => (
          <div className="tile" key={p.name}>
            <span className="tag">{p.name}</span>
            <h3>✦ {p.credits.toLocaleString()} · {p.price}</h3>
            <p>{p.blurb}</p>
            <div style={{ flex: 1 }} />
            <button className="btn-primary" onClick={() => topUp(p.credits)}>Add credits</button>
          </div>
        ))}
      </div>
    </div>
  );
}
