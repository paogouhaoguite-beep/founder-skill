# Synthetic worked example

Input: 1200×1200 flattened product image, target 1200×630, critical bottle occupies x400–800/y100–1100. A direct centered crop removes top/bottom of the bottle.

Decision: use proportional fit into 1200×630 with background extension/padding, or request the editable product layer for a new layout. Do not distort the bottle or crop away its cap. Output specification names protected bounds and notes no file was rendered in this fixture.

Boundary scenario 1: A strict 100 KB limit makes label text unreadable. Report the tradeoff and request an alternate composition rather than pass a visibly damaged export.
Boundary scenario 2: Two placements share dimensions but different UI overlays. Review each safe zone independently.
