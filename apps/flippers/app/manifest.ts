import type { MetadataRoute } from "next";

// Makes Flippers installable on phones and computers.
export default function manifest(): MetadataRoute.Manifest {
  return {
    id: "/",
    name: "Flippers",
    short_name: "Flippers",
    description: "Your personal AI studio for images, video, voice and music.",
    start_url: "/",
    scope: "/",
    display: "standalone",
    orientation: "any",
    background_color: "#0f0e0d",
    theme_color: "#0f0e0d",
    categories: ["photo", "graphics", "productivity"],
    icons: [
      { src: "/brand/flippers-192.png", sizes: "192x192", type: "image/png" },
      { src: "/brand/flippers-512.png", sizes: "512x512", type: "image/png" },
      { src: "/brand/flippers-512-maskable.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
    // Long-press the app icon to jump straight to these.
    shortcuts: [
      { name: "New image", url: "/image", icons: [{ src: "/brand/flippers-192.png", sizes: "192x192" }] },
      { name: "New video", url: "/video", icons: [{ src: "/brand/flippers-192.png", sizes: "192x192" }] },
      { name: "Audio", url: "/audio", icons: [{ src: "/brand/flippers-192.png", sizes: "192x192" }] },
      { name: "Library", url: "/library", icons: [{ src: "/brand/flippers-192.png", sizes: "192x192" }] },
    ],
    screenshots: [
      { src: "/brand/screenshot-wide.png", sizes: "1440x900", type: "image/png", form_factor: "wide", label: "Flippers on desktop" },
      { src: "/brand/screenshot-phone.png", sizes: "780x1688", type: "image/png", form_factor: "narrow", label: "Flippers on a phone" },
    ],
  };
}
