# OMAR OTHMAN — Portfolio 2026

Responsive portfolio website with a matching redesigned portfolio PDF.

## Included
- `index.html` — primary English website.
- `index-ar.html` — Arabic version with the same visual system.
- `live-campaigns.html` — live campaigns + daily posts page, powered by `content/live-campaigns.json`.
- `client-reviews.html` — verified client reviews page supporting image reviews and MP4/WebM video testimonials.
- `before-after.html` — before/after campaign comparison page.
- `downloads/OMAR_OTHMAN_Portfolio.pdf` — redesigned portfolio PDF using the same light blue/orange visual language.
- `downloads/OMAR_OTHMAN_ATS_CV.pdf` and `.docx` — ATS CV files retained.
- `assets/` — portfolio imagery and folders ready for new campaign/review/before-after media.

## Content folders
Add real material only:
- `assets/live-campaigns/`
- `assets/daily-posts/`
- `assets/reviews/`
- `assets/before-after/`

Update the matching JSON file in `content/` after adding media.

## Notes
- Client ratings/testimonials are not displayed in the main portfolio. The dedicated review page is intentionally empty until real client material is supplied.
- The visitor indicator is explicitly labeled **Demo visitors** and changes every five minutes; it is not real analytics.
- Screenshot/download protection is best-effort deterrence only. A website cannot technically prevent screenshots or copying with 100% certainty.
- The client note form does not store submissions; it prepares a WhatsApp message locally.

## Automatic content folders
Upload JPG/JPEG/PNG/WEBP/GIF files directly into `assets/live-campaigns/` or `assets/daily-posts/` and the Live Campaigns page will discover them automatically through the public GitHub repository API. No JSON editing is required for those two folders.
