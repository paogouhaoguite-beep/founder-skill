"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useStore } from "@/lib/store";

const LINKS = [
  { href: "/", label: "Explore" },
  { href: "/image", label: "Image" },
  { href: "/video", label: "Video" },
  { href: "/library", label: "Library" },
  { href: "/pricing", label: "Pricing" },
];

export default function Nav() {
  const path = usePathname();
  const { credits } = useStore();
  return (
    <nav className="nav">
      <Link href="/" className="brand">
        <span className="brand-mark" /> Frameforge
      </Link>
      <div className="nav-links">
        {LINKS.map((l) => (
          <Link key={l.href} href={l.href} className={path === l.href ? "active" : ""}>
            {l.label}
          </Link>
        ))}
      </div>
      <div className="nav-spacer" />
      <div className="credits" title="Credits">
        ✦ {credits}
        <Link href="/pricing">
          <button type="button">Top up</button>
        </Link>
      </div>
    </nav>
  );
}
