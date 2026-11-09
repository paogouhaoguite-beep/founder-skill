import type { Metadata, Viewport } from "next";
import Nav from "@/components/Nav";
import AppShell from "@/components/AppShell";
import "./globals.css";

export const metadata: Metadata = {
  title: "Flippers",
  applicationName: "Flippers",
  description: "Your personal AI studio for images, video, voice and music.",
  appleWebApp: { capable: true, title: "Flippers", statusBarStyle: "black-translucent" },
  formatDetection: { telephone: false },
};

export const viewport: Viewport = {
  themeColor: "#0f0e0d",
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover", // draw under the iPhone notch; CSS pads with safe-area insets
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <AppShell>
          <Nav />
          {children}
        </AppShell>
      </body>
    </html>
  );
}
