import type { Metadata } from "next";
import Nav from "@/components/Nav";
import "./globals.css";

export const metadata: Metadata = {
  title: "Flippers",
  applicationName: "Flippers",
  appleWebApp: { title: "Flippers", statusBarStyle: "black-translucent" },
  description: "Generate images and video with the best AI models in one studio.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Nav />
        {children}
      </body>
    </html>
  );
}
