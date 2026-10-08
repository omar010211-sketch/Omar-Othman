Portfolio image and video folders
==================================

Copy the package contents over the root of your existing website repository, keeping paths intact. It updates both bilingual pages and adds an automatic GitHub Actions content index.

Add files to these folders and push them to GitHub:
- assets/client-logos/: client logo images.
- assets/campaign-dashboards/: campaign dashboard images.
- assets/ai-campaign-videos/: campaign videos produced with AI (MP4 or WebM recommended; MOV/M4V are also indexed).

The workflow scans folders after each push, updates content/portfolio-images.json, and commits the generated index. The English and Arabic pages read this index to populate the client logo slider, campaign dashboard gallery, and AI campaign video section. Video titles come from filenames. The AI Content button sits beside the CV download button and links to the video section.

GitHub Actions must be enabled and allowed to write repository contents. Keep the existing site assets, content, downloads, and other pages when merging this package; it contains only the modified pages and new supporting files. Existing GitHub Pages setup should publish from the same branch and repository root.
