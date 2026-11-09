import "server-only";
import { fal } from "@fal-ai/client";

export const hasFalKey = () => Boolean(process.env.FAL_KEY);

let configured = false;
export function falServer() {
  if (!configured) {
    fal.config({ credentials: process.env.FAL_KEY });
    configured = true;
  }
  return fal;
}

/** Pull every output URL out of a fal result, whatever its shape. */
export function outputUrls(data: unknown): string[] {
  const d = (data ?? {}) as Record<string, unknown>;
  const urls: string[] = [];
  const take = (x: unknown) => {
    const u = (x as { url?: unknown } | undefined)?.url;
    if (typeof u === "string") urls.push(u);
  };
  if (Array.isArray(d.images)) d.images.forEach(take);
  take(d.image);
  take(d.video);
  take(d.audio);
  if (typeof d.audio_url === "string") urls.push(d.audio_url);
  return urls;
}
