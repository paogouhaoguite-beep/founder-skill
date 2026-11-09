import type { MetadataRoute } from "next";

// Lets you "Add to Home Screen" on a phone and get the Flippers icon.
export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "Flippers",
    short_name: "Flippers",
    description: "Your personal AI studio for images, video, voice and music.",
    start_url: "/",
    display: "standalone",
    background_color: "#0f0e0d",
    theme_color: "#0f0e0d",
    icons: [
      { src: "/brand/flippers-192.png", sizes: "192x192", type: "image/png" },
      { src: "/brand/flippers-512.png", sizes: "512x512", type: "image/png" },
      { src: "/brand/flippers-512-maskable.png", sizes: "512x512", type: "image/png", purpose: "maskable" },
    ],
  };
}
