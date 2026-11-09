import { NextResponse } from "next/server";
import { getModel, validate, withPreset, type Values } from "@/lib/catalog";
import { PRESETS } from "@/lib/presets";
import { falServer, hasFalKey } from "@/lib/fal-server";

export async function POST(req: Request) {
  let body: { modelId?: string; values?: Values };
  try {
    body = await req.json();
  } catch {
    return NextResponse.json({ error: "Invalid request" }, { status: 400 });
  }
  const model = getModel(body.modelId ?? "");
  if (!model) return NextResponse.json({ error: "Unknown model" }, { status: 400 });
  const values: Values = { ...(body.values ?? {}) };

  const problem = validate(model, values);
  if (problem) return NextResponse.json({ error: problem }, { status: 400 });

  if (!hasFalKey()) return NextResponse.json({ demo: true });

  // Uploads made in demo mode are data: URLs; real runs need hosted files.
  const files = Object.values(values).flat().filter((x) => typeof x === "string" && x.startsWith("data:"));
  if (files.length) {
    return NextResponse.json({ error: "Re-upload your files (they were added before the API key was set)" }, { status: 400 });
  }

  const preset = PRESETS.find((p) => p.id === values.preset);
  values._prompt = withPreset(values, preset?.prompt);

  try {
    const endpoint = model.endpoint(values);
    const { request_id } = await falServer().queue.submit(endpoint, { input: model.toInput(values) });
    return NextResponse.json({ endpoint, requestId: request_id });
  } catch (e) {
    return NextResponse.json({ error: describe(e) }, { status: 502 });
  }
}

function describe(e: unknown) {
  const err = e as { message?: string; body?: { detail?: unknown } };
  const detail = err.body?.detail;
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail)) return detail.map((d) => (d as { msg?: string }).msg ?? JSON.stringify(d)).join("; ");
  return err.message ?? "Request failed";
}
