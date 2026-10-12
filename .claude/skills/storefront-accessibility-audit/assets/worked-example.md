# Synthetic worked example

Input: Staging cart drawer can open by keyboard, but Tab cycles behind it and Escape does nothing. Screenshot shows a close icon; accessible name and color values are unavailable.

Finding: keyboard focus management fails the intended modal interaction; reproduce by opening drawer and pressing Tab. Proposed fix: implement correct modal semantics/focus containment and a keyboard-operable close mechanism, restoring focus afterward. Accessible-name and contrast checks remain unknown until DOM/style inspection. Do not label the whole store compliant/noncompliant from this one test.

Boundary scenario 1: Scanner reports zero issues. Continue manual keyboard, form and assistive-technology checks.
Boundary scenario 2: Only a screenshot is provided. Report visual risks; do not claim keyboard or screen-reader behavior was tested.
