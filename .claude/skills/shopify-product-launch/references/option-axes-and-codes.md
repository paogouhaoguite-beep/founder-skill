# Option Axes & Abbreviation Codes

## Optional SKU example

Preserve the merchant's existing SKU scheme and all existing variant SKUs by default. The following abbreviation approach is only an example for new SKUs when the merchant has no scheme and approves this convention. Do not regenerate existing identifiers. Axis values must still come from verified product facts.

### Example rules

1. Any axis name is valid (Color, Size, Material, Style…). Axis names and
   values come from the product fact sheet, never invented here.
2. Abbreviations are uppercase, 2–4 characters, **unique within one axis**.
3. SKU = `model_no` + axis abbreviations in axis order; axes without an
   abbreviation are skipped.
4. Unknown values: propose an abbreviation, show it in the variant table,
   and get user confirmation at the Launch Sheet.
5. Abbreviation collision within an axis → extend letters (e.g. CAR vs CHR)
   until unique.

## Color codes (seed table, extend as needed)

| Value | Code | | Value | Code |
|---|---|---|---|---|
| Black | BLK | | Camel | CAR |
| Charcoal | CHA | | Beige | BEI |
| White | WHT | | Ivory | IVY |
| Brown | BRN | | Tan | TAN |
| Navy | NVY | | Olive | OLV |
| Grey/Grey melange | GRY | | Burgundy | BGD |
| Green | GRN | | Mustard | MUS |
| Red | RED | | Pink | PNK |
| Blue | BLU | | Cream | CRM |

## Size codes

| Value | Code | | Value | Code |
|---|---|---|---|---|
| S / M / L / XL / XXL | S / M / L / XL / 2XL | | Numeric (36–46) | as-is |
| One size | OS | | Custom | confirmed at Launch Sheet |

## Material / Style codes

No seed table — propose from the value name (first consonant cluster),
confirm at the Launch Sheet, and record confirmed pairs in the merchant's working launch sheet for reuse, not in the installed skill package.
