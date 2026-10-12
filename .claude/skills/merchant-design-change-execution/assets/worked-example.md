# Synthetic worked example

Input: Approved request changes page 2 heading from “Summer bottle” to “Bottle care” and asks for a new font. Current connector supports text replacement but exposes no font-family operation.

Manifest: page 2 element T4 text old→new; supported. Font change: manual action required, specified target font supplied by merchant. Apply text, preview, save under the existing edit authorization and read back T4 before calling it complete. If no connector is available, deliver exactly this manifest with execution status not run.

Boundary scenario 1: Save request times out. Read the saved design; retry only if the prior change is proven absent.
Boundary scenario 2: Two reviewers request opposite headings. Do not choose silently; flag the conflict while completing independent approved edits.
