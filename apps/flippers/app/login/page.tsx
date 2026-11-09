"use client";
import { Suspense, useState } from "react";
import { useSearchParams } from "next/navigation";
import Logo from "@/components/Logo";

function LoginForm() {
  const params = useSearchParams();
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError(null);
    const res = await fetch("/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    }).catch(() => null);
    if (res?.ok) {
      // Only allow redirects within this site.
      const next = params.get("next") ?? "/";
      window.location.href = next.startsWith("/") && !next.startsWith("//") ? next : "/";
      return;
    }
    setBusy(false);
    setError(res ? "Wrong password" : "Can't reach the server. Check your connection.");
  }

  return (
    <form className="login-card" onSubmit={submit}>
      <Logo size={64} />
      <h1>Flippers</h1>
      <input type="password" autoComplete="current-password" placeholder="Password" autoFocus
        value={password} onChange={(e) => setPassword(e.target.value)} />
      {error && <div className="error">{error}</div>}
      <button className="btn-primary" disabled={busy || !password}>{busy ? "Checking…" : "Unlock"}</button>
      <p className="hint">You&apos;ll stay logged in on this device.</p>
    </form>
  );
}

export default function LoginPage() {
  return (
    <main className="login-page">
      <Suspense>
        <LoginForm />
      </Suspense>
    </main>
  );
}
