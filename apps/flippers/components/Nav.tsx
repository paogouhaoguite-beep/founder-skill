"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const GROUPS = [
  [{ href: "/", label: "Explore" }],
  [{ href: "/image", label: "Image" }, { href: "/video", label: "Video" }, { href: "/audio", label: "Audio" }, { href: "/character", label: "Character" }],
  [{ href: "/edit", label: "Edit" }, { href: "/upscale", label: "Upscale" }, { href: "/lipsync", label: "Lipsync" }, { href: "/faceswap", label: "Face Swap" }],
  [{ href: "/studios", label: "Studios" }, { href: "/storyboard", label: "Storyboard" }, { href: "/canvas", label: "Canvas" }, { href: "/library", label: "Library" }],
];

export default function Nav() {
  const path = usePathname();
  return (
    <nav className="nav">
      <Link href="/" className="brand">
        <span className="brand-mark" /> Flippers
      </Link>
      <div className="nav-links">
        {GROUPS.map((g, i) => (
          <div key={i} className="nav-group">
            {g.map((l) => (
              <Link key={l.href} href={l.href} className={path === l.href ? "active" : ""}>{l.label}</Link>
            ))}
          </div>
        ))}
      </div>
    </nav>
  );
}
