"use client";
import { useState } from "react";
import MediaCard from "@/components/MediaCard";
import { useStore } from "@/lib/store";
import { useResumeJobs } from "@/lib/jobs";

const FILTERS = ["all", "image", "video"] as const;

export default function LibraryPage() {
  const { items, remove } = useStore();
  useResumeJobs();
  const [filter, setFilter] = useState<(typeof FILTERS)[number]>("all");
  const [q, setQ] = useState("");
  const shown = items.filter(
    (g) => (filter === "all" || g.mode === filter) && g.prompt.toLowerCase().includes(q.toLowerCase()),
  );
  return (
    <div className="section">
      <div className="feed-head" style={{ marginBottom: 14, gap: 12, flexWrap: "wrap" }}>
        <h1 style={{ margin: 0 }}>Library</h1>
        <div className="chips">
          {FILTERS.map((f) => (
            <button key={f} className={`chip ${f === filter ? "on" : ""}`} onClick={() => setFilter(f)}>{f}</button>
          ))}
          <input className="chip" placeholder="Search prompts" value={q} onChange={(e) => setQ(e.target.value)} />
        </div>
      </div>
      {shown.length === 0 ? (
        <div className="empty">Nothing here yet. Head to the Image or Video studio.</div>
      ) : (
        <div className="grid">{shown.map((g) => <MediaCard key={g.id} g={g} onRemove={remove} />)}</div>
      )}
    </div>
  );
}
