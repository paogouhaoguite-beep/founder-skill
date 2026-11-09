import { NextResponse, type NextRequest } from "next/server";

// Optional lock for a personal deployment: set APP_PASSWORD and the browser
// asks for it (any username) before showing any page or calling the API.
export function middleware(req: NextRequest) {
  const password = process.env.APP_PASSWORD;
  if (!password) return NextResponse.next();

  const header = req.headers.get("authorization") ?? "";
  if (header.startsWith("Basic ")) {
    try {
      const decoded = atob(header.slice(6));
      if (safeEqual(decoded.slice(decoded.indexOf(":") + 1), password)) return NextResponse.next();
    } catch {
      // malformed header: fall through to the 401
    }
  }
  return new NextResponse("Password required", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="Flippers"' },
  });
}

// Compare without returning early, so timing doesn't reveal how much matched.
function safeEqual(a: string, b: string) {
  let diff = a.length ^ b.length;
  for (let i = 0; i < Math.max(a.length, b.length); i++) diff |= (a.charCodeAt(i) || 0) ^ (b.charCodeAt(i) || 0);
  return diff === 0;
}

// Icons and the app manifest stay public: phones fetch them without the password.
export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico|icon.svg|apple-icon.png|manifest.webmanifest|brand/).*)"],
};
