# Worked example

All names, inputs and results below are synthetic.

Synthetic Markdown has two sections: “Launch decision” stating inventory80units; “Open issue” stating carrier collection unconfirmed. Mode=deck, no private notes. Expected: two slides preserving both facts; no “ready to ship” inference. Complete offline HTML:
```html
<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Launch review</title><style>body{margin:0;color:#111;background:#fff;font:1.3rem/1.5 Arial,sans-serif}section{min-height:100vh;padding:8vh 8vw;box-sizing:border-box}nav a{margin-right:2rem}a:focus{outline:3px solid #111}small{display:block}@media print{section{min-height:0;break-after:page}section:last-child{break-after:auto}nav{display:none}}</style><main><section id="slide-1" aria-labelledby="s1"><small>1 of 2</small><h1 id="s1">Launch decision</h1><p>Inventory: 80 units.</p><nav aria-label="Slides"><a href="#slide-2">Next: Open issue</a></nav></section><section id="slide-2" aria-labelledby="s2"><small>2 of 2</small><h1 id="s2">Open issue</h1><p>Carrier collection is unconfirmed.</p><nav aria-label="Slides"><a href="#slide-1">Previous: Launch decision</a></nav></section></main></html>
```
Source mapping: section1→slide-1; section2→slide-2. No network dependencies or hidden notes. Navigation is native keyboard-accessible links; no claimed arrow-key/presenter-mode implementation. Structural HTML inspection completed by reading this synthetic artifact; browser and print rendering remain untested. For reading mode, remove full-viewport/print slide breaks and use a TOC linking the same IDs; content remains unchanged.

## Acceptance scenarios

1. A deck contains confidential margin notes. Do not merely hide them with CSS; exclude them from the distributed file and report separate presenter-only output if authorized.

2. An unsupported nested table or footnote would disappear during conversion. Preserve it with a documented alternative or stop that conversion, not silently discard it.

Bundled file: [brief.html](brief.html). This is the same synthetic draft shown above, with no live submission or client-rendering result.
