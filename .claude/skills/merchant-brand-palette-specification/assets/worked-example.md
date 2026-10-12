# Synthetic worked example

Input: Verified black #000000 and white #FFFFFF; accent source only a compressed orange logo thumbnail. Relative luminance black 0 and white 1 gives contrast(1+0.05)/(0+0.05)=21:1. Accent exact hex is unknown.

Specification: black text on white or white text on black passes the supplied contrast requirement if that requirement is at most 21:1. Orange remains an approximate reference pending the brand file; no exact contrast claim. Error messages use text and icon, not orange alone.

Boundary scenario 1: Text has 50% opacity. Calculate the effective rendered color against its actual background; do not use opaque black’s ratio.
Boundary scenario 2: A photo background varies under text. Review the least legible region or add a solid text panel before measuring.
