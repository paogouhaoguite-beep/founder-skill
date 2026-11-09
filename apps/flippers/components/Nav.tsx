"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import Logo from "./Logo";
import { useInstall } from "./AppShell";

const GROUPS = [
  [{ href: "/", label: "Explore" }],
  [{ href: "/image", label: "Image" }, { href: "/video", label: "Video" }, { href: "/audio", label: "Audio" }, { href: "/character", label: "Character" }],
  [{ href: "/edit", label: "Edit" }, { href: "/upscale", label: "Upscale" }, { href: "/lipsync", label: "Lipsync" }, { href: "/faceswap", label: "Face Swap" }],
  [{ href: "/studios", label: "Studios" }, { href: "/storyboard", label: "Storyboard" }, { href: "/canvas", label: "Canvas" }, { href: "/library", label: "Library" }],
];
const TABS = [
  { href: "/", label: "Home", icon: "⌂" },
  { href: "/image", label: "Image", icon: "◐" },
  { href: "/video", label: "Video", icon: "▶" },
  { href: "/library", label: "Library", icon: "▦" },
];
const HIDDEN = ["/login"];

async function logout() {
  await fetch("/api/logout", { method: "POST" }).catch(() => {});
  location.href = "/login";
}

export default function Nav() {
  const path = usePathname();
  const { canInstall, install } = useInstall();
  const [more, setMore] = useState(false);
  if (HIDDEN.includes(path)) return null;
  const inTabs = TABS.some((t) => t.href === path);

  return (
    <>
      <nav className="nav">
        <Link href="/" className="brand"><Logo /> Flippers</Link>
        <div className="nav-links">
          {GROUPS.map((g, i) => (
            <div key={i} className="nav-group">
              {g.map((l) => <Link key={l.href} href={l.href} className={path === l.href ? "active" : ""}>{l.label}</Link>)}
            </div>
          ))}
        </div>
        <div className="nav-actions">
          {canInstall && <button className="btn install-btn" onClick={install}>Install app</button>}
          <button className="icon-btn logout-btn" title="Log out" onClick={logout}>⎋</button>
        </div>
      </nav>

      {/* Phone-style tab bar (small screens only) */}
      <nav className="tabbar">
        {TABS.map((t) => (
          <Link key={t.href} href={t.href} className={path === t.href ? "active" : ""} onClick={() => setMore(false)}>
            <span>{t.icon}</span>{t.label}
          </Link>
        ))}
        <button className={more || !inTabs ? "active" : ""} onClick={() => setMore((m) => !m)}><span>☰</span>More</button>
      </nav>
      {more && (
        <div className="sheet-backdrop" onClick={() => setMore(false)}>
          <div className="sheet" onClick={(e) => e.stopPropagation()}>
            {GROUPS.slice(1).map((g, i) => (
              <div key={i} className="sheet-group">
                {g.map((l) => <Link key={l.href} href={l.href} className={path === l.href ? "active" : ""} onClick={() => setMore(false)}>{l.label}</Link>)}
              </div>
            ))}
            <div className="sheet-group">
              {canInstall && <button onClick={() => { setMore(false); install(); }}>Install app</button>}
              <button onClick={logout}>Log out</button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
