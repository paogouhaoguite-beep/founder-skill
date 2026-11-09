import { NextResponse } from "next/server";
import { ALL_ENDPOINTS } from "@/lib/catalog";
import { falServer, outputUrls } from "@/lib/fal-server";

export async function POST(req: Request) {
  let body: { endpoint?: string; requestId?: string };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ status: "FAILED", error: "Invalid request" }, { status: 400 });
  }
  const { endpoint, requestId } = body;
  // Only check on jobs for endpoints in our own catalog.
  if (!endpoint || !ALL_ENDPOINTS.has(endpoint) || !requestId || !/^[\w-]+$/.test(requestId)) {
    return NextResponse.json({ status: "FAILED", error: "Unknown job" }, { status: 400 });
  }
  try {
    const fal = falServer();
    const s = await fal.queue.status(endpoint, { requestId });
    if (s.status !== "COMPLETED") return NextResponse.json({ status: s.status });
    const { data } = await fal.queue.result(endpoint, { requestId });
    return NextResponse.json({ status: "COMPLETED", urls: outputUrls(data) });
  } catch (e) {
    const err = e as { message?: string; body?: { detail?: unknown } };
    const detail = err.body?.detail;
    const msg = typeof detail === "string" ? detail : Array.isArray(detail)
      ? detail.map((d) => (d as { msg?: string }).msg ?? "").join("; ") : err.message;
    return NextResponse.json({ status: "FAILED", error: msg ?? "Generation failed" });
  }
}
