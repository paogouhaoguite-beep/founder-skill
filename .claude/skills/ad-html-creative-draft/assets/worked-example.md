# Worked example

All names, inputs and results below are synthetic.

Synthetic brief: text-first1200×1200 square; white/black brand; approved facts “Cotton tote”, “$24 USD”; no photo and no performance claim. The complete HTML below is the reviewable deliverable. It has no external dependencies. Browser rendering and platform acceptance are not executed.
```html
<!doctype html>
<html lang="en"><meta charset="utf-8"><title>Cotton tote — creative A</title>
<style>*{box-sizing:border-box}body{margin:0}.creative{width:1200px;height:1200px;padding:96px;background:#fff;color:#111;font-family:Arial,sans-serif;display:flex;flex-direction:column;justify-content:space-between}h1{font-size:108px;line-height:1.05;margin:0;max-width:900px}p{font-size:56px;margin:0}.cta{font-size:42px;border:4px solid #111;padding:24px;align-self:flex-start}</style>
<main class="creative" aria-label="Cotton tote, $24 USD. Explore the tote."><h1>Cotton tote</h1><p>$24 USD</p><p class="cta">Explore the tote</p></main></html>
```
QA: dimensions declared1200×1200; price matches input; product photo not represented; no invented reviews or discount. Text fit, screenshot dimensions and placement safe areas remain pending browser/spec inspection. VariantB would change headline only after merchant supplies a second approved wording.

## Acceptance scenarios

1. Only a product-image layout is requested but no authorized image is supplied. Return a placeholder draft and missing-asset blocker, not a fake depiction.

2. The complete price qualifier does not fit. Recompose or shorten approved copy; do not crop or hide the qualifier.

Bundled file: [creative.html](creative.html). This is the same synthetic draft shown above, with no live submission or client-rendering result.
