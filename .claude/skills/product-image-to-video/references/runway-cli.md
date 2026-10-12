# Optional Runway command-line execution

Use a connected video tool if the user already has one. This optional helper needs Python 3.10+, an authorized Runway API account and `RUNWAYML_API_SECRET` set in the environment. It uses the Python standard library; no SDK installation is needed. Never paste the key into a request, chat, receipt or repository. An API account is separate from installing these skills.

The helper implements a single-reference image-to-video path. Read the selected model's current input limits and pricing first. It does not estimate charges, enforce an account spending cap or support every provider mode. It must run within the user's approved quantity, duration and budget. Prefer another available connector for multiple references, first/last frames or unsupported parameters.

## Prepare the request

Save the following as `request.json`, replacing the reference URL and prompt with approved merchant inputs. This is a configuration example, not a bundled product image. `gen4.5`, `1280:720` and `5` follow the official guide checked on 2026-10-05; verify they remain available for your account before submitting.

```json
{
  "model": "gen4.5",
  "promptImage": "https://example.com/replace-with-owned-product.jpg",
  "promptText": "The supplied closed product remains stationary with its front label unchanged. Make a subtle straight camera push-in. Preserve silhouette, material, color and cap. Do not rotate, open the product or reveal an unseen side. No added text or audio claims.",
  "ratio": "1280:720",
  "duration": 5
}
```

`promptImage` can also be an image data URI supported by the provider. The helper does not upload local paths or create public hosting. Use the current provider's private upload/data-URI options for a local image, and confirm rights before sending it.

Run these commands from this skill's installed directory, with request/output paths pointing to your working project:

```sh
python3 scripts/runway_video.py submit --request request.json
```

This only validates required fields offline. It does not check credentials, URL reachability, model availability, provider acceptance or visual fidelity.

## Execute and resume

When generation is authorized and the account has the intended budget:

```sh
python3 scripts/runway_video.py submit --request request.json --job output/shot-01.json --execute
python3 scripts/runway_video.py status --job output/shot-01.json
```

Submission creates a receipt before sending the paid request. It refuses to reuse an existing receipt. A network failure may leave `submission_unknown`; preserve that receipt and reconcile in the provider account before any resubmission. Do not delete it and rerun just because the caller timed out. There is no automatic paid retry.

The status command queries the same task once and records its state. Poll according to the provider's current guidance, with backoff for throttling. The documented recommendation is at least five seconds plus jitter between queries. `FAILED` and `CANCELED` are terminal failures, not generated assets. A temporary status error can be retried against the same ID without creating a new task.

Once status is `SUCCEEDED`:

```sh
python3 scripts/runway_video.py download --job output/shot-01.json --output output/shot-01.mp4
```

For multiple outputs use `--index 1` and another output path. Provider output URLs expire; download promptly, and keep signed URLs/receipts private. The helper sends no API credential to the output host, rejects non-HTTPS redirects, checks nonempty/declared download length and never replaces an existing final file. A failed download removes its partial file, so the download command can be retried. If the URL expired, refresh the existing task with `status`, then download again; do not regenerate.

## Inspect before delivery

Downloaded bytes do not prove a valid clip. Open the file in an available player, or inspect metadata with `ffprobe` if installed, then watch the full clip and examine product-critical frames. Check dimensions, duration, decodability, product shape/label continuity, introduced objects and unexpected audio. If playback or visual inspection is unavailable, mark it unverified; do not label it accepted.

Local validation covers offline request checks and simulated lifecycle/failure behavior only. No paid API request or generated video quality was tested for this release; see the repository validation record.

## Official references

Checked 2026-10-05. These links describe the protocol; this helper is an original implementation, with no copied SDK source.

- [Request body and API version header](https://docs.dev.runwayml.com/guides/using-the-api/)
- [Task states and polling](https://docs.dev.runwayml.com/api-details/sdks/)
- [Output retrieval and expiration](https://docs.dev.runwayml.com/assets/outputs/)
