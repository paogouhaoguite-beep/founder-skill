# Synthetic worked example

Synthetic case: 2-slide PPTX; slide 2 label “CARE INSTRUCTIONS” renders as “CARE INSTRUCTI” in converter L. Source shape is fully within bounds; font verified installed. Untouched render reproduces clipping. Copy A with geometry widened still clips. Copy B with letter spacing neutralized on that one label renders complete.

Repair log: slide 2 text run → converter-specific spacing hypothesis supported by A/B renders → use B for PDF conversion only. Deliver original-spacing editable repaired.pptx and spacing-adjusted render-source.pptx distinctly; repaired.pdf has 2 pages and complete label. Visual comparison confirms other text, prices and images unchanged. These are expected fixture results, not claims of tools run in this package.

Boundary 1: only flattened PDF supplied and last characters absent → report missing source content; do not hallucinate restoration.
Boundary 2: approved brand font unavailable → request lawful font or explicit substitute choice; do not download an unlicensed lookalike or claim visual equivalence.
