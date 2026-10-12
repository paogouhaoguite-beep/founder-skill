# Synthetic worked example

Input: A bilingual care card contains Arabic instruction and product code B-750. The merchant requests editable DOCX plus PDF, but only text editing is available.

Content: “يُغسل يدويًا فقط.” Product code remains “B-750”. Specification: Arabic paragraph with native RTL and Arabic language metadata; separate LTR line for B-750. Do not reverse the Arabic string or add manual spacing to force placement.

QA report: content reviewed as a draft; structural implementation not run; rendered layout not run; Word acceptance not run; font portability unknown. Deliver a correction specification, not a claim that DOCX/PDF files were produced.

Boundary scenario 1: The Arabic looks correct in one preview but a URL appears reversed. Put the URL in an LTR container and retest the target application.
Boundary scenario 2: ZWNJ appears in supplied text. Do not globally strip it; examine whether it is linguistically meaningful before a scoped correction.
