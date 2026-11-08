# Frameforge

An AI image and video studio: one prompt box in front of several generation
models, with camera/motion presets, reference images, a credit balance and a
library of past generations.

It is an original app: the name, design, copy and presets are its own.
Its feature set was scoped by looking at how AI creative suites such as
higgsfield.ai structure their product (see "Research notes" below).

## Run it

```bash
cd apps/frameforge
npm install
cp .env.example .env.local   # add FAL_KEY for real generations
npm run dev                  # http://localhost:3000
```

Without `FAL_KEY` the app runs in **demo mode**: every flow works, but
outputs are generated placeholders and no provider is called.

## Features

| Area | What it does |
|---|---|
| Explore (`/`) | Tool, model and preset directory with deep links into the studios |
| Image studio (`/image`) | Prompt, model picker, aspect ratio, 1–4 images, reference upload (required for Kontext Edit), credit cost shown before generating |
| Video studio (`/video`) | Prompt, optional start frame (image-to-video), 14 camera/mood/effect presets, model, aspect ratio, resolution, duration |
| Library (`/library`) | All generations, filter by image/video, search prompts, download, delete |
| Pricing (`/pricing`) | Credit packs (top-ups are local only until payments are wired up) |

Deep links: `/image?model=kontext-edit`, `/video?preset=orbit&prompt=...`.

## How it works

- `lib/models.ts`: the model catalog. Each model maps the studio's controls
  onto one fal.ai endpoint (`falId`, `toInput`) and defines its credit cost.
  Add or swap models here.
- `lib/presets.ts`: motion presets, which append a camera instruction to
  the prompt, so they work on any video model.
- `app/api/generate`: validates the request and submits it to the fal.ai
  queue. `app/api/status` polls the job and returns output URLs. The
  status route only fetches `https://queue.fal.run` URLs.
- `lib/store.ts`: library and credit balance, kept in the browser's
  localStorage.

## Not built yet

- User accounts, server-side credit ledger and Stripe payments (credits are client-side and can be edited by the user).
- Persistent media storage: output URLs are the provider's, which may expire.
- Community feed, contests, canvas/moodboard, lipsync, upscaling, character consistency.
- fal.ai endpoint IDs were not exercised against the live API in this build;
  verify them at https://fal.ai/models once a key is set.

## Research notes (REA)

Gathered with REA (`rea analyze-web-bundle`) plus a headless-browser read of
the public pages on 2026-11-08. These are observations about structure, not
copied content.

- The REA route inventory (22 scripts analyzed) found mostly community
  showcase routes (`/@creator/projects/<slug>`). Its limitation: the routes
  are static candidates only, so the full route set is unverified.
- Navigation exposes these product areas: image generation, video
  generation, audio, MCP/CLI and API access, preset-driven studios (shorts,
  ads, marketing, influencer), canvas, editing/inpaint, upscaling, lipsync,
  community/contests, library, pricing.
- Core generator pattern: a left control column (references, prompt,
  model, duration, aspect ratio, quality) with a credit-priced Generate
  button; the right pane holds history and output. Models are chosen with
  a `?model=` query parameter.
- Video creation is preset-centric: start image, then a camera/VFX preset,
  then a clip.

Frameforge implements the core of that: image and video generation, presets,
references, credits and a library.
