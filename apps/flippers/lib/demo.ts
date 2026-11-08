// Placeholder output used when no provider key is configured.

function hash(s: string) {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0;
  return Math.abs(h);
}

const dims: Record<string, [number, number]> = {
  "1:1": [1024, 1024],
  "4:3": [1024, 768],
  "3:4": [768, 1024],
  "16:9": [1280, 720],
  "9:16": [720, 1280],
  "21:9": [1344, 576],
};

export function demoImage(prompt: string, aspect: string, seed: number) {
  const [w, h] = dims[aspect] ?? [1024, 1024];
  const base = hash(prompt + seed);
  const h1 = base % 360;
  const h2 = (h1 + 60 + (base % 90)) % 360;
  const text = prompt.slice(0, 60).replace(/[<&>"]/g, "");
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="hsl(${h1},70%,45%)"/><stop offset="1" stop-color="hsl(${h2},70%,18%)"/></linearGradient>
<radialGradient id="r" cx="${30 + (base % 40)}%" cy="${30 + (base % 30)}%" r="60%">
<stop offset="0" stop-color="hsla(${h2},90%,75%,.55)"/><stop offset="1" stop-color="hsla(${h2},90%,75%,0)"/></radialGradient></defs>
<rect width="100%" height="100%" fill="url(#g)"/><rect width="100%" height="100%" fill="url(#r)"/>
<text x="50%" y="88%" text-anchor="middle" font-family="system-ui,sans-serif" font-size="${Math.round(w / 40)}" fill="rgba(255,255,255,.85)">${text}</text>
<text x="4%" y="8%" font-family="system-ui,sans-serif" font-size="${Math.round(w / 55)}" fill="rgba(255,255,255,.6)">DEMO OUTPUT</text></svg>`;
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
}
