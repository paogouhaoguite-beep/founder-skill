import { NextResponse } from "next/server";
import { getModel, type GenRequest } from "@/lib/models";
import { PRESETS } from "@/lib/presets";
import { hasFalKey, submit } from "@/lib/fal";

export async function POST(req: Request) {
  let body: GenRequest & { presetId?: string };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "Invalid request" }, { status: 400 });
  }
  const model = getModel(body.modelId);
  if (!model || model.mode !== body.mode) {
    return NextResponse.json({ error: "Unknown model" }, { status: 400 });
  }
  if (!body.prompt?.trim()) {
    return NextResponse.json({ error: "Write a prompt first" }, { status: 400 });
  }
  if (model.needsReference && !body.referenceImage) {
    return NextResponse.json({ error: `${model.name} needs a reference image` }, { status: 400 });
  }

  const preset = PRESETS.find((p) => p.id === body.presetId);
  const request: GenRequest = {
    ...body,
    count: Math.min(Math.max(body.count || 1, 1), 4),
    duration: model.durations?.includes(body.duration) ? body.duration : model.durations?.[0] ?? 5,
    presetPrompt: preset?.prompt,
  };

  if (!hasFalKey()) {
    // Demo mode: no provider key configured, so the client renders placeholders.
    return NextResponse.json({ demo: true });
  }

  try {
    const job = await submit(model.falId(request), model.toInput(request));
    return NextResponse.json({ statusUrl: job.status_url, responseUrl: job.response_url });
  } catch (e) {
    return NextResponse.json({ error: (e as Error).message }, { status: 502 });
  }
}
