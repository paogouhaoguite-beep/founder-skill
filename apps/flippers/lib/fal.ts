// Minimal client for the fal.ai queue API (server-side only).
// Docs: https://docs.fal.ai/model-endpoints/queue

const QUEUE = "https://queue.fal.run";

export const hasFalKey = () => Boolean(process.env.FAL_KEY);

function headers() {
  return {
    Authorization: `Key ${process.env.FAL_KEY}`,
    "Content-Type": "application/json",
  };
}

export interface Submitted {
  request_id: string;
  status_url: string;
  response_url: string;
}

export async function submit(falId: string, input: Record<string, unknown>): Promise<Submitted> {
  const res = await fetch(`${QUEUE}/${falId}`, {
    method: "POST",
    headers: headers(),
    body: JSON.stringify(input),
  });
  if (!res.ok) throw new Error(`fal submit ${res.status}: ${await res.text()}`);
  return res.json();
}

// Only accept status/response URLs on fal's own queue host, so the status
// route can't be used to make the server fetch arbitrary URLs.
function assertFalUrl(u: string) {
  const url = new URL(u);
  if (url.protocol !== "https:" || url.hostname !== "queue.fal.run") {
    throw new Error("Refusing non-fal URL");
  }
  return url.toString();
}

export async function status(statusUrl: string): Promise<{ status: string }> {
  const res = await fetch(assertFalUrl(statusUrl), { headers: headers(), cache: "no-store" });
  if (!res.ok) throw new Error(`fal status ${res.status}: ${await res.text()}`);
  return res.json();
}

export async function result(responseUrl: string): Promise<string[]> {
  const res = await fetch(assertFalUrl(responseUrl), { headers: headers(), cache: "no-store" });
  if (!res.ok) throw new Error(`fal result ${res.status}: ${await res.text()}`);
  const data = await res.json();
  const urls: string[] = [];
  if (Array.isArray(data.images)) urls.push(...data.images.map((i: { url: string }) => i.url));
  if (data.image?.url) urls.push(data.image.url);
  if (data.video?.url) urls.push(data.video.url);
  return urls;
}
