# Worked example

All names, inputs and results below are synthetic.

Input: Product page title is “TideCup 350 ml”; OG title says “500 ml” and og:image is /old.jpg. Expected patch aligns the title to 350 ml and uses an accessible absolute image URL. Browser HTML shows the new tags, but a cached social preview still shows 500 ml; report source fixed, preview pending refresh rather than complete.

## Acceptance scenarios

1. Given the image requires login, mark it unsuitable for public preview crawlers.

2. Given a redirect changes the final page, verify metadata at the resolved destination and preserve intended canonical URL.
