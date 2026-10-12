# Synthetic worked example

Input: Product title can contain 60 characters; mobile content width 320 px. Specification: title may wrap naturally with no fixed height; body and care conditions retain readable size; price uses consistent numeral alignment where needed. Font must include Arabic if that locale is supported.

QA requirement: render a long actual product name, a large currency value and care text at the target widths and text enlargement. No exact font size is declared without testing the supplied face/content.

Boundary scenario 1: Brand font lacks a supported script. Choose an approved compatible fallback and verify mixed-script appearance.
Boundary scenario 2: A title fits only after shrinking below the agreed readability target. Allow wrapping or redesign the layout rather than silently reduce it.
