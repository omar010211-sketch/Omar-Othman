from pathlib import Path
import json
root = Path(__file__).resolve().parents[1]
image_extensions = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.avif', '.svg'}
video_extensions = {'.mp4', '.webm', '.mov', '.m4v'}
def assets(folder, extensions):
    base = root / 'assets' / folder
    return [{'src': p.relative_to(root).as_posix(), 'title': p.stem.replace('-', ' ').replace('_', ' ').title()} for p in sorted(base.rglob('*')) if p.is_file() and p.suffix.lower() in extensions]
out = root / 'content' / 'portfolio-images.json'
out.parent.mkdir(parents=True, exist_ok=True)
data = {
    'clientLogos': assets('client-logos', image_extensions),
    'campaignDashboards': assets('campaign-dashboards', image_extensions),
    'aiCampaignVideos': assets('ai-campaign-videos', video_extensions),
}
out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
