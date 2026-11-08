# Flippers

A personal AI image and video studio: one prompt box in front of several
generation models, with camera/motion presets, reference images and a library
of everything you've made. No accounts, credits or payments.

## Run it

```bash
cd apps/flippers
npm install
cp .env.example .env.local   # add FAL_KEY for real generations
npm run dev                  # http://localhost:3000
```

Without `FAL_KEY` the app runs in **demo mode**: every flow works, but
outputs are generated placeholders and no provider is called. With a key,
fal.ai bills your account directly for each generation.

If you deploy it anywhere public, set `APP_PASSWORD`. Otherwise anyone who
finds the URL can generate on your fal.ai key.

## Features

| Area | What it does |
|---|---|
| Explore (`/`) | Tool, model and preset directory with deep links into the studios |
| Image studio (`/image`) | Prompt, model picker, aspect ratio, 1–4 images, reference upload (required for Kontext Edit) |
| Video studio (`/video`) | Prompt, optional start frame (image-to-video), 14 camera/mood/effect presets, model, aspect ratio, resolution, duration |
| Library (`/library`) | All generations, filter by image/video, search prompts, download, delete |

Deep links: `/image?model=kontext-edit`, `/video?preset=orbit&prompt=...`.

## How it works

- `lib/models.ts`: the model catalog. Each model maps the studio's controls
  onto one fal.ai endpoint (`falId`, `toInput`). Add or swap models here.
- `lib/presets.ts`: motion presets, which append a camera instruction to
  the prompt, so they work on any video model.
- `app/api/generate`: validates the request and submits it to the fal.ai
  queue. `app/api/status` polls the job and returns output URLs. The
  status route only fetches `https://queue.fal.run` URLs.
- `lib/store.ts`: the library, kept in your browser's localStorage, so it
  is per browser and per device.
- `middleware.ts`: optional `APP_PASSWORD` lock.

## Notes

- fal.ai endpoint IDs were not exercised against the live API in this build;
  verify them at https://fal.ai/models once a key is set.
- Output URLs are fal.ai's and may expire. Download anything you want to keep.

## Research notes (REA)

The feature scope came from an REA (`rea analyze-web-bundle`) pass and a
headless-browser read of public AI creative-suite pages on 2026-11-08.
Name, design, copy and presets are original.
