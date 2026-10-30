# Recon map: Higgsfield (core create loop)

Clean-room recon. Built only from public pages (marketing site, pricing page, public blog, third-party reviews).
No source code, private APIs or anyone else's account was used. `replica/screens/` is reference only and never ships.

## 1. Scope

| question | answer |
| --- | --- |
| App | Higgsfield (higgsfield.ai): multi-model AI image and video generation suite |
| Platform | Web app (works in phone browsers) |
| Slice | Core create loop: prompt and optional reference image → pick model and preset (camera motion / effect) → generate image or video → library. Plus a cost display per generation. |
| Audience | Personal / internal tool. One user or a small team, **no billing, no plans, no public sign-up** |
| Out of slice (for now) | Marketing Studio / UGC ads, AI Influencer & Character (Soul ID), Lipsync / Speak, Cinema Studio, Genjutsu motion transfer, Supercomputer agent, Canvas, community feed, teams |

**Core loop in one line:** write a prompt, maybe drop in an image, pick a model and a camera preset, see the cost, hit Generate, watch it render, keep or retry from the library.

## 2. Sources

| # | source | URL | what it gave |
| --- | --- | --- | --- |
| 1 | Marketing home | https://higgsfield.ai/ | product areas, model list, entry points (`/ai/image?model=`, `/ai/video?model=`), preset collections |
| 2 | Pricing page | https://higgsfield.ai/pricing | per-model credit costs, concurrency limits per plan, gated features (Start & End frame, commercial use, fast-track) |
| 3 | Blog: pricing explained | https://higgsfield.ai/blog/higgsfield-pricing-explained | cost = model × duration × resolution × count; plan comparison |
| 4 | Blog: credits explained | https://higgsfield.ai/blog/ai-video-credits-explained | charged per generation whether kept or not; "test at low res, then upscale" workflow |
| 5 | Third-party review | https://creatify.ai/review/higgsfield-ai | "prompt or image → camera preset → model → generate"; 70+ camera presets; 15+ video models |
| 6 | Public tutorial videos | https://www.youtube.com/watch?v=M73BrFnVPA8 , https://www.youtube.com/watch?v=0osgyuhkaqQ | walkthroughs of the create flow (titles/descriptions only reviewed so far) |
| 7 | User's own account | — | not used. Optional: if you have an account, you can screenshot your own screens into `replica/screens/` |

Not yet read (worth a look before building UI): help center, changelog, full tutorial videos.

## 3. Screen inventory

| ID | screen | route / how you get there | purpose | key components | states to build |
| --- | --- | --- | --- | --- | --- |
| S01 | Explore / home | `/` | entry point: tool cards, preset showcase | top nav, tool cards, preset grid, hero media | filled, loading |
| S02 | Image generator | `/image?model=` | text/image → image | prompt box, reference image slots, model picker, aspect ratio, count, quality, cost badge, Generate button, results feed | empty (first use), generating, filled, error (failed job), over-concurrency |
| S03 | Video generator | `/video?model=` | text/image → video | prompt box, start frame, optional end frame, model picker, preset picker, duration, resolution, cost badge, Generate | empty, generating (progress), filled, error, model-doesn't-support-option |
| S04 | Preset picker | modal/drawer from S03 | choose a camera motion / effect | category tabs (Camera, Effects, Action…), preset cards with looping preview, search | loading, filled, none-matching |
| S05 | Model picker | popover from S02/S03 | choose model | model list with tags (speed, max res, audio), cost per unit | filled, disabled options |
| S06 | Library / history | `/library` | every generation, filter by type | grid of media cards, filters (image/video, model, date), status chips | empty, loading, filled, in-progress items, failed items |
| S07 | Asset detail | click card in S06 or result in S02/S03 | view one result | large player/viewer, prompt + settings, download, reuse settings, "animate this image", upscale, delete | image, video, failed, deleting |
| S08 | Upscale | action from S07 or `/upscale` | upscale an image or video | source preview, scale factor, cost, Generate | idle, running, done, error |
| S09 | Settings | `/settings` | provider API keys, defaults, spend cap | key fields, default model, monthly cap, usage summary | no key set, key invalid, ok |

## 4. User flows

```
F01 Text → image
    S02: type prompt → pick model (S05) → ratio/count → see cost → Generate → result card in feed → S07
    happy path: ~4 clicks after typing
    edge: empty prompt, provider error, NSFW/safety refusal, concurrency limit hit

F02 Text → video with a camera preset (the core loop)
    S03: type prompt → open S04, pick preset → pick model (S05) → duration/resolution → cost → Generate
         → progress → result → S07
    happy path: ~6 clicks after typing
    edge: model doesn't support the preset/duration/resolution (disable + explain), long render (minutes),
          job fails mid-way (no charge / mark failed), tab closed during render (job continues, shows in S06)

F03 Image → video (animate an image)
    S07 (image) → "Animate" → S03 with start frame prefilled → preset → Generate
    or S03 → upload start frame (optional end frame) → Generate
    edge: wrong file type, huge file, aspect ratio mismatch between start/end frames

F04 Iterate cheaply, then upscale
    F02 at 720p/short → S07 → "Reuse settings" (prefills S03) → tweak → Generate → keeper → S08 upscale
    edge: reuse with a model that's since been removed

F05 Browse and manage results
    S06 → filter → S07 → download / delete / reuse
    edge: empty library, hundreds of items (pagination), failed items

F06 First-run setup (clone-specific)
    S09 → paste provider API key → test → set spend cap → back to S02
    edge: invalid key, no credit on provider account
```

**Number to beat:** prompt → video with preset in ≤ 6 clicks, with cost shown before Generate.

## 5. Components

| component | variants | states | used on |
| --- | --- | --- | --- |
| PromptBox | image, video | empty, typing, too long, disabled while submitting | S02, S03 |
| ImageDropSlot | reference, start frame, end frame | empty, dragging, uploading, filled, error | S02, S03, S08 |
| ModelPicker | image models, video models | open, option disabled (unsupported), selected | S02, S03 |
| PresetCard | camera, effect | idle, hover (plays preview), selected | S04, S01 |
| PresetPicker | modal (desktop), bottom sheet (mobile) | loading, filtered, empty | S03 |
| SegmentedControl | aspect ratio, duration, resolution, count | option disabled | S02, S03, S08 |
| CostBadge | — | computing, value, over-cap warning | S02, S03, S08 |
| GenerateButton | — | ready, disabled (+reason), submitting, limit reached | S02, S03, S08 |
| JobCard / MediaCard | image, video | queued, running (progress), done, failed | S02, S03, S06 |
| MediaViewer | image, video player | loading, playing, error | S07 |
| Toast | success, error, info | — | everywhere |
| TopNav | desktop, mobile tabs | active item | everywhere |
| EmptyState | library, feed | — | S02, S03, S06 |

## 6. Inferred data model

```
Model        id, kind (image|video|upscale), provider, provider_model_id, display_name,
             supports {aspect_ratios[], durations[], resolutions[], start_frame, end_frame, presets, audio},
             cost_rule (per image | per second × resolution multiplier)
             evidence: pricing page lists per-model costs; "Start & End Frame" and resolution options per model
             confidence: high

Preset       id, name, category (camera|effect|action|...), preview_url, prompt_fragment,
             compatible_model_ids[]
             evidence: "70+ camera presets", preset collections on home page
             confidence: medium (how presets are applied internally is a guess: likely prompt
             template and/or a model-native motion parameter)

Asset        id, kind (upload|image|video), url, thumb_url, width, height, duration_s, created_at
             evidence: library, uploads as start frames
             confidence: high

Generation   id, kind, model_id, preset_id?, prompt, params (json: ratio, duration, resolution, count, seed),
             input_asset_ids[] (refs / start / end), output_asset_ids[],
             status (queued|running|succeeded|failed), error?, cost, provider_job_id,
             created_at, finished_at, parent_generation_id? (reuse/upscale lineage)
             evidence: library shows prompt+settings; credits charged per generation;
                       "reuse settings" and upscale flows
             confidence: high

Settings     provider_keys (encrypted), default_model_ids, monthly_spend_cap, concurrency_limit
             evidence: clone-specific (replaces Plan/Credits for a personal tool)
             confidence: n/a (design decision)
```

Dropped vs the original: User plans, credit wallet, subscriptions, teams/workspaces, community posts. For a personal tool, **cost = real provider spend**, tracked in `Generation.cost`.

## 7. Feature matrix

See `replica/features.csv`.

## 8. What can't be cloned

| item | why | clone instead |
| --- | --- | --- |
| Higgsfield's own models (Soul, Popcorn, Speak, Genjutsu) | proprietary | use public models via an inference API (e.g. fal.ai, Replicate, or the vendors' own APIs: Kling, Veo, Seedance, FLUX, etc.) |
| The exact 70+ preset library & preview videos | their content/IP | write your own preset set (dolly in, orbit, crane up, crash zoom, FPV, handheld…) with your own preview clips generated by the clone |
| Bundled "unlimited" deals with model vendors | partner deals | pay-as-you-go provider pricing |
| Community feed, user base | network | n/a for a personal tool |
| Branding, name, logo, UI artwork | trademark/copyright | your own name and design |

## 9. Size

- **Screens:** 9 · **Flows:** 6 · **Entities:** 5
- **Hard parts:**
  1. **Async job pipeline:** video renders take minutes; needs a queue, provider webhooks or polling, retry, and status pushed to the UI.
  2. **Model capability matrix + cost engine:** each model supports different durations/resolutions/frames and prices differently; UI must disable invalid combos and show exact cost before Generate.
  3. **Preset system:** making a preset produce consistent motion across different models (prompt templates per model, or native camera-control params where a model has them), plus generating preview clips.
- Easier parts: library, uploads/storage (S3/R2), settings.
- **Size: M** (a few weeks for one developer) for the slice above. Each extra Higgsfield area (UGC ads, characters, lipsync) is roughly another M.

## Next step

`/replica-build`: shell → F02 (text → video with preset) as the vertical slice → remaining screens with all states.
