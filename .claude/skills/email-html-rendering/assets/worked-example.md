# Worked example

All names, inputs and results below are synthetic.

Input: A refill announcement needs a heading, short factual copy, CTA /refills, and an unsubscribe token. No product image is required for this text-first draft. Expected output keeps the CTA and terms as live text. With images blocked, the reader still sees “Refills available” and the button. A long translated heading wraps without horizontal overflow at 320 px. All client checks in this synthetic case are planned, not executed. The supplied HTML is an illustrative artifact; no Gmail or Outlook preview has run.

## Acceptance scenarios

1. Given the merchant supplies only a screenshot containing the offer, transcribe and verify the text instead of making the whole email an image.

2. Given unsubscribe syntax is unknown, mark the footer unresolved and do not represent the HTML as send-ready.

## Concrete synthetic artifact

Additional input assumptions: the merchant supplies HTTPS destination `https://store.example/refills`, store name `Harbor Store`, footer address `10 Example Road`, and confirms its ESP resolves `{{unsubscribe_url}}`. The token is illustrative; replace it only with the merchant's actual verified syntax.

```html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Refills available</title></head>
<body style="margin:0;background:#f5f5f5;color:#202020;font-family:Arial,sans-serif">
<div style="display:none;max-height:0;overflow:hidden">Choose the refill size that fits your jar.</div>
<table role="presentation" width="100%" cellspacing="0" cellpadding="0"><tr><td align="center">
<table role="presentation" width="600" cellspacing="0" cellpadding="0" style="width:100%;max-width:600px;background:#ffffff"><tr><td style="padding:24px">
<h1 style="font-size:28px;line-height:1.25">Refills available</h1>
<p style="font-size:16px;line-height:1.5">Keep your jar in use. Check its size, then choose the matching refill. Product details and current availability are on the refill page.</p>
<p><a href="https://store.example/refills" style="display:inline-block;background:#163c2d;color:#ffffff;text-decoration:none;padding:14px 20px;font-size:16px">Choose your refill</a></p>
<p style="font-size:12px;line-height:1.5">Harbor Store · 10 Example Road<br><a href="{{unsubscribe_url}}" style="color:#202020">Unsubscribe from marketing email</a></p>
</td></tr></table></td></tr></table>
</body></html>
```

Plain-text companion:

```text
Refills available

Keep your jar in use. Check its size, then choose the matching refill.
Product details and current availability: https://store.example/refills

Harbor Store, 10 Example Road
Unsubscribe from marketing email: {{unsubscribe_url}}
```

| Check | Synthetic expectation | Actual execution status |
|---|---|---|
| Images blocked | Text and CTA remain available; no essential image-only content | Not executed |
| 320 px viewport | Container fits viewport; heading wraps | Not executed |
| Gmail web and mobile | Confirm spacing, CTA and token resolution using a real preview | Not executed |
| Outlook desktop | Inspect Word-engine table/button rendering separately from Outlook.com | Not executed |
| Dark mode | Inspect foreground/background contrast and link visibility | Not executed |
| Unsubscribe | Actual ESP must resolve token and enforce the opted-out state | Not executed |

Bundled file: [email.html](email.html). This is the same synthetic draft shown above, with no live submission or client-rendering result.
Plain-text companion: [email.txt](email.txt).
