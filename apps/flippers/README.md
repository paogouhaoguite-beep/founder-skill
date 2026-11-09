# Flippers

A personal AI studio for images, video, voice and music: 31 models behind one
set of controls, plus storyboards, a moodboard canvas and ready-made
templates. No accounts, credits or payments.

## Run it

```bash
cd apps/flippers
npm install
cp .env.example .env.local   # add FAL_KEY for real generations
npm run dev                  # http://localhost:3000
```

Without `FAL_KEY` the app runs in **demo mode**: every tool works, but results
are placeholders (gradient images, a chime for audio) and nothing is sent to
a provider. With a key, fal.ai bills your account for each generation.

If you deploy it anywhere public, set `APP_PASSWORD`. Otherwise anyone who
finds the URL can generate on your fal.ai key. With it set, Flippers shows a
login page, and each device stays logged in for a year. Changing the password
logs every device out.

## Install it as an app

Flippers is an installable web app (PWA). Once it's deployed on https:

- **iPhone / iPad (Safari):** tap **Install app** (or Share → **Add to Home Screen**).
- **Android (Chrome):** tap **Install app**, or ⋮ → **Install app**.
- **Mac / Windows (Chrome or Edge):** click **Install app** in the top bar, or the
  install icon in the address bar.

It then opens full-screen from its own icon, with a phone-style tab bar on
small screens. Long-press the icon for shortcuts (New image, New video, Audio,
Library). Without a connection it shows an offline screen instead of a
browser error. It never caches generations or API calls.

## What's in it

| Page | Models / what it does |
|---|---|
| Image | Nano Banana, Seedream 4, Flux Pro Ultra, Flux Dev, Ideogram 3 (text in images), Wan 2.2 |
| Video | Kling 2.5 Turbo, Veo 3.1 (with sound), Seedance Pro, Hailuo 02, Wan 2.2. Text or start image, 14 camera/mood/effect presets |
| Audio | Voiceover (ElevenLabs, 21 voices), Music (ElevenLabs), Lyria 2, Sound effects, Add sound to a silent video (MMAudio) |
| Character | Multi-reference likeness (1–4 photos), Instant Character (1 photo) |
| Edit | Kontext (edit with words), Nano Banana Edit and Seedream Edit (combine up to 4 images), Inpaint (paint a mask) |
| Upscale | SeedVR / Clarity / Crisp for images; SeedVR / Topaz for video |
| Lipsync | Sync Lipsync 2, Kling Lipsync, Talking Photo (photo + audio → video) |
| Face Swap | Requires confirming you have the person's permission |
| Studios | 15 templates for ads, shorts, virtual influencers and marketing; each opens a tool pre-filled |
| Storyboard | Write scenes, generate a frame per scene (optionally with one recurring character), animate every frame into a clip |
| Canvas | Moodboard: drag generations and notes around a free board |
| Library | Everything you've made, filterable by image/video/audio |

Every result has a ⋯ menu to send it on: Animate, Edit, Upscale, Use as
character, Make it talk, Add sound, Lipsync, Add to canvas.

## How it works

- `lib/catalog.ts`: the single source of truth. Each model lists its input
  fields, its fal.ai endpoint(s) and how fields map onto the request. Pages,
  forms and server validation are all generated from it. To add a model, add
  an entry.
- `app/api/generate`: validates input against the catalog, then submits to
  the fal queue. `app/api/status` polls and returns output URLs, only for
  endpoints listed in the catalog.
- `app/api/fal/proxy`: lets the browser upload files straight to fal storage
  without seeing the key. It is restricted to the storage endpoints.
- `lib/jobs.ts`: background polling. Jobs keep going if you switch pages
  and resume after a reload.
- `lib/store.ts`: library, storyboards and canvas, kept in your browser's
  localStorage (per browser, per device).
- `middleware.ts` + `lib/session.ts`: optional `APP_PASSWORD` login (signed,
  HttpOnly session cookie) over every page and API route.
- `public/sw.js`, `app/manifest.ts`, `components/AppShell.tsx`: the installable-app
  parts (service worker, manifest, install button).

## Notes

- Every model's request shape was checked against fal's published schemas on
  2026-11-09 (all 215 option combinations), but no paid generation has been run.
  Run one generation per tool once your key is in.
- Output URLs are fal's and may expire. Download anything you want to keep.
- Higgsfield's in-house models (Soul, Genjutsu, Mangaka, etc.) only run on
  their service, so they aren't here. Name, design, copy, presets and
  templates are original.
