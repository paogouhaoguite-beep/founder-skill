// Checks every model request in lib/catalog.ts against fal.ai's live input schemas.
// Run: npm run check:schemas
import { MODELS, defaultValues, validate, type Values, type Field } from "../lib/catalog";

const URL_IMG = "https://v3.fal.media/files/test/a.png", URL_VID = "https://v3.fal.media/files/test/a.mp4", URL_AUD = "https://v3.fal.media/files/test/a.mp3";
const cache = new Map<string, any>();
async function schema(id: string) {
  if (!cache.has(id)) cache.set(id, await (await fetch("https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=" + id)).json());
  const j = cache.get(id), S = j.components.schemas;
  const ref = Object.values<any>(j.paths).find((p) => p.post).post.requestBody.content["application/json"].schema.$ref.split("/").pop();
  return { inp: S[ref], S };
}
function sample(fields: Field[], withStart: boolean): Values {
  const v: Values = {};
  for (const f of fields) {
    if (f.kind === "prompt") v[f.key] = "test prompt";
    if (f.kind === "image" && (f.required || withStart)) v[f.key] = URL_IMG;
    if (f.kind === "images") v[f.key] = [URL_IMG, URL_IMG];
    if (f.kind === "mask") v[f.key] = URL_IMG;
    if (f.kind === "video") v[f.key] = URL_VID;
    if (f.kind === "audio") v[f.key] = URL_AUD;
    if (f.kind === "consent") v[f.key] = true;
  }
  return v;
}
let problems = 0, checks = 0;
(async () => {
  for (const m of MODELS) {
    const variants: Values[] = [];
    const optionalStart = m.fields.some((f) => f.kind === "image" && !f.required);
    for (const withStart of optionalStart ? [false, true] : [false]) {
      // default values plus every option of every select, one at a time
      const base = { ...defaultValues(m), ...sample(m.fields, withStart) };
      variants.push(base);
      for (const f of m.fields) if (f.kind === "select") for (const o of f.options) variants.push({ ...base, [f.key]: o });
    }
    for (const v of variants) {
      const err = validate(m, v);
      if (err) { console.log("VALIDATE", m.id, err); problems++; continue; }
      const ep = m.endpoint(v);
      if (!m.endpoints.includes(ep)) { console.log("ENDPOINT not listed", m.id, ep); problems++; }
      const input = m.toInput(v);
      const { inp, S } = await schema(ep);
      checks++;
      for (const req of inp.required ?? []) if (input[req] === undefined) { console.log("MISSING required", m.id, ep, req); problems++; }
      for (const [k, val] of Object.entries(input)) {
        const p = inp.properties[k];
        if (!p) { console.log("UNKNOWN field", m.id, ep, k); problems++; continue; }
        const r = p.$ref || p.allOf?.[0]?.$ref; const d = r ? S[r.split("/").pop()] : p;
        const opts = d.enum ?? p.anyOf?.flatMap((a: any) => (a.$ref ? S[a.$ref.split("/").pop()].enum : a.enum) ?? []);
        const type = d.type ?? p.anyOf?.map((a: any) => a.type).filter(Boolean);
        if (opts?.length && !opts.includes(val) && !(Array.isArray(type) && type.includes(typeof val) && !d.enum)) {
          console.log("BAD VALUE", m.id, ep, k, JSON.stringify(val), "allowed:", opts.join("|")); problems++;
        }
        const t = typeof val === "object" ? (Array.isArray(val) ? "array" : "object") : typeof val;
        const types = [type].flat().filter(Boolean).map((x: string) => (x === "integer" ? "number" : x));
        if (types.length && !types.includes(t) && !(opts?.length)) { console.log("BAD TYPE", m.id, ep, k, t, "want", types.join("|")); problems++; }
        if (typeof val === "number" && (d.minimum !== undefined && val < d.minimum || d.maximum !== undefined && val > d.maximum)) {
          console.log("OUT OF RANGE", m.id, ep, k, val, d.minimum, d.maximum); problems++;
        }
      }
    }
  }
  console.log(`\n${MODELS.length} models, ${checks} request variants checked against live fal schemas, ${problems} problems`);
})();
