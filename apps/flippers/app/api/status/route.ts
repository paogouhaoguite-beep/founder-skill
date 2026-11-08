import { NextResponse } from "next/server";
import { result, status } from "@/lib/fal";

export async function POST(req: Request) {
  const { statusUrl, responseUrl } = (await req.json()) as {
    statusUrl: string;
    responseUrl: string;
  };
  try {
    const s = await status(statusUrl);
    if (s.status !== "COMPLETED") return NextResponse.json({ status: s.status });
    const urls = await result(responseUrl);
    return NextResponse.json({ status: "COMPLETED", urls });
  } catch (e) {
    return NextResponse.json({ status: "FAILED", error: (e as Error).message }, { status: 502 });
  }
}
