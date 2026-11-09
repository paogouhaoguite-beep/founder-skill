import { NextResponse } from "next/server";
import { hasFalKey } from "@/lib/fal-server";

export const dynamic = "force-dynamic";
export function GET() {
  return NextResponse.json({ demo: !hasFalKey() });
}
