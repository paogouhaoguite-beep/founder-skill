# Synthetic worked example

Input: /approved/Bottle-v2.png and /downloads/Bottle-final.png have the same verified hash; /draft/Bottle-v3.png has a different hash and no approval record.

Plan: retain approved v2 as the production asset; link the identical download as a duplicate candidate; keep v3 under drafts. Do not choose v3 solely because it is newer. Proposed paths are mapped before any move; this fixture performs no file operations.

Boundary scenario 1: Two different files map to the same destination. Stop that row and generate distinct versioned names for review.
Boundary scenario 2: A move fails midway. Use the per-file log to reconcile completed and pending moves before retrying.
