# Synthetic worked example

Template:
“Care sheet for [[product_name]]
Capacity: [[capacity_ml]] mL
[[if care_note]]Care: [[care_note]][[end]]”

Schema: product_name required string; capacity_ml required positive number; care_note optional approved string. Synthetic row: Bottle B, 750, “Hand wash only.” Result: “Care sheet for Bottle B / Capacity: 750 mL / Care: Hand wash only.” No unresolved tokens remain.

Boundary scenario 1: capacity_ml is missing. Block rendering as final; do not output 0 mL.
Boundary scenario 2: care_note contains template syntax or HTML. Treat it as literal data and escape it; do not execute it or allow it to change the template structure.
