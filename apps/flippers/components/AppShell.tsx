"use client";
// App behaviour: registers the service worker and offers "Install app".
// Chrome/Edge/Android get a one-tap install; iPhone/iPad get instructions,
// because Safari only installs through Share → Add to Home Screen.

import { createContext, useContext, useEffect, useState } from "react";

interface InstallPrompt extends Event { prompt: () => Promise<void>; userChoice: Promise<{ outcome: string }> }
interface Install { canInstall: boolean; installed: boolean; install: () => void }

const Ctx = createContext<Install>({ canInstall: false, installed: false, install: () => {} });
export const useInstall = () => useContext(Ctx);

export default function AppShell({ children }: { children: React.ReactNode }) {
  const [prompt, setPrompt] = useState<InstallPrompt | null>(null);
  const [installed, setInstalled] = useState(false);
  const [ios, setIos] = useState(false);
  const [showIosHelp, setShowIosHelp] = useState(false);

  useEffect(() => {
    if ("serviceWorker" in navigator && process.env.NODE_ENV === "production") {
      navigator.serviceWorker.register("/sw.js").catch(() => {});
    }
    const standalone = matchMedia("(display-mode: standalone)").matches ||
      (navigator as Navigator & { standalone?: boolean }).standalone === true;
    setInstalled(standalone);
    setIos(/iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1));

    const onPrompt = (e: Event) => { e.preventDefault(); setPrompt(e as InstallPrompt); };
    const onInstalled = () => { setInstalled(true); setPrompt(null); };
    addEventListener("beforeinstallprompt", onPrompt);
    addEventListener("appinstalled", onInstalled);
    return () => { removeEventListener("beforeinstallprompt", onPrompt); removeEventListener("appinstalled", onInstalled); };
  }, []);

  const value: Install = {
    installed,
    canInstall: !installed && (Boolean(prompt) || ios),
    install: () => {
      if (prompt) {
        prompt.prompt();
        prompt.userChoice.finally(() => setPrompt(null));
      } else if (ios) setShowIosHelp(true);
    },
  };

  return (
    <Ctx.Provider value={value}>
      {children}
      {showIosHelp && (
        <div className="lightbox" onClick={() => setShowIosHelp(false)}>
          <div className="login-card" onClick={(e) => e.stopPropagation()}>
            <h1>Install Flippers</h1>
            <ol className="ios-steps">
              <li>Tap the <strong>Share</strong> button <span aria-hidden>(□↑)</span> in Safari&apos;s toolbar.</li>
              <li>Scroll down and tap <strong>Add to Home Screen</strong>.</li>
              <li>Tap <strong>Add</strong>. Flippers opens full-screen from your home screen.</li>
            </ol>
            <button className="btn-primary" onClick={() => setShowIosHelp(false)}>Got it</button>
          </div>
        </div>
      )}
    </Ctx.Provider>
  );
}
