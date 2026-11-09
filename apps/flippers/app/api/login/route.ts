import { NextResponse } from "next/server";
import { COOKIE, MAX_AGE, safeEqual, sessionToken } from "@/lib/session";

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

export async function POST(req: Request) {
  const expected = process.env.APP_PASSWORD;
  if (!expected) return NextResponse.json({ ok: true }); // no lock configured

  let password = "";
  try {
    password = String((await req.json()).password ?? "");
  } catch {}

  if (!safeEqual(password, expected)) {
    await sleep(800); // slow down guessing
    return NextResponse.json({ error: "Wrong password" }, { status: 401 });
  }
  const res = NextResponse.json({ ok: true });
  res.cookies.set(COOKIE, await sessionToken(expected), {
    httpOnly: true,
    sameSite: "lax",
    // Secure on https; plain http is only used for local testing.
    secure: new URL(req.url).protocol === "https:" || req.headers.get("x-forwarded-proto") === "https",
    path: "/",
    maxAge: MAX_AGE,
  });
  return res;
}
