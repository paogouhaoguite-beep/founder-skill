# Synthetic worked example

Input Markdown: title “Bottle Care”, a two-item care list, a table with “Capacity | 750 mL”, and link [Care policy](https://example.com/care). Output target: semantic HTML.

Finished fragment:
```html
<article><h1>Bottle Care</h1><ul><li>Hand wash only.</li><li>Do not tumble dry.</li></ul><table><caption>Product specification</caption><tbody><tr><th scope="row">Capacity</th><td>750 mL</td></tr></tbody></table><p><a href="https://example.com/care">Care policy</a></p></article>
```

Coverage check: title, two restrictions, capacity and link preserved. No new sales claim added; browser layout not tested in this text fixture.

Boundary scenario 1: A Word table uses merged cells. Explain the target mapping and verify row associations; do not silently flatten them into misleading pairs.
Boundary scenario 2: Source HTML contains a script. Preserve needed visible content after inspection, but do not execute or distribute the script as editorial content.
