// Placeholder outputs used when no provider key is configured.

function hash(s: string) {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0;
  return Math.abs(h);
}

const dims: Record<string, [number, number]> = {
  "1:1": [1024, 1024], "4:3": [1024, 768], "3:4": [768, 1024], "3:2": [1152, 768], "2:3": [768, 1152],
  "16:9": [1280, 720], "9:16": [720, 1280], "21:9": [1344, 576],
};

export function demoImage(prompt: string, aspect: string, seed: number) {
  const [w, h] = dims[aspect] ?? [1024, 1024];
  const base = hash(prompt) + seed * 97;
  const h1 = base % 360;
  const h2 = (h1 + 60 + ((base >> 3) % 120)) % 360;
  const text = prompt.slice(0, 60).replace(/[<&>"]/g, "");
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="hsl(${h1},70%,45%)"/><stop offset="1" stop-color="hsl(${h2},70%,18%)"/></linearGradient>
<radialGradient id="r" cx="${20 + (base % 60)}%" cy="${20 + ((base >> 2) % 50)}%" r="60%">
<stop offset="0" stop-color="hsla(${h2},90%,75%,.55)"/><stop offset="1" stop-color="hsla(${h2},90%,75%,0)"/></radialGradient></defs>
<rect width="100%" height="100%" fill="url(#g)"/><rect width="100%" height="100%" fill="url(#r)"/>
<text x="50%" y="88%" text-anchor="middle" font-family="system-ui,sans-serif" font-size="${Math.round(w / 40)}" fill="rgba(255,255,255,.85)">${text}</text>
<text x="4%" y="8%" font-family="system-ui,sans-serif" font-size="${Math.round(w / 55)}" fill="rgba(255,255,255,.6)">DEMO OUTPUT</text></svg>`;
  return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
}

/** A short two-note chime as a tiny WAV data URL. */
export function demoAudio(prompt: string) {
  const rate = 8000, secs = 1.2, len = Math.floor(rate * secs);
  const f1 = 330 + (hash(prompt) % 200), f2 = f1 * 1.5;
  const buf = new Uint8Array(44 + len);
  const dv = new DataView(buf.buffer);
  const str = (o: number, t: string) => [...t].forEach((c, i) => dv.setUint8(o + i, c.charCodeAt(0)));
  str(0, "RIFF"); dv.setUint32(4, 36 + len, true); str(8, "WAVE"); str(12, "fmt ");
  dv.setUint32(16, 16, true); dv.setUint16(20, 1, true); dv.setUint16(22, 1, true);
  dv.setUint32(24, rate, true); dv.setUint32(28, rate, true); dv.setUint16(32, 1, true); dv.setUint16(34, 8, true);
  str(36, "data"); dv.setUint32(40, len, true);
  for (let i = 0; i < len; i++) {
    const t = i / rate, f = t < secs / 2 ? f1 : f2;
    const env = Math.min(1, t * 20) * Math.exp(-3 * (t % (secs / 2)));
    buf[44 + i] = 128 + Math.round(60 * env * Math.sin(2 * Math.PI * f * t));
  }
  let bin = "";
  buf.forEach((b) => (bin += String.fromCharCode(b)));
  return `data:audio/wav;base64,${btoa(bin)}`;
}
