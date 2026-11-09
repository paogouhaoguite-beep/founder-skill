// Password sessions. After you log in once, a signed cookie remembers you, so
// the app works as a home-screen app (iPhone standalone apps don't handle the
// browser's built-in password popup well). Runs in middleware (edge) and in
// route handlers, so it only uses Web Crypto.

export const COOKIE = "flippers_session";
export const MAX_AGE = 60 * 60 * 24 * 365; // one year

const enc = new TextEncoder();

/** The session token is an HMAC of a fixed label keyed by the password, so
 *  changing APP_PASSWORD logs every device out. */
export async function sessionToken(password: string) {
  const key = await crypto.subtle.importKey("raw", enc.encode(password), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = await crypto.subtle.sign("HMAC", key, enc.encode("flippers-session-v1"));
  return [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

/** Constant-time string comparison, so timing doesn't reveal how much matched. */
export function safeEqual(a: string, b: string) {
  let diff = a.length ^ b.length;
  for (let i = 0; i < Math.max(a.length, b.length); i++) diff |= (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0);
  return diff === 0;
}
