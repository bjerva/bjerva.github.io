"""Create a Netlify preview from a verified production build."""
from pathlib import Path
import re
import shutil
import sys

source, destination = (Path(arg).resolve() for arg in sys.argv[1:3])
if destination.exists():
    sys.exit(f"Preview destination already exists: {destination}")
shutil.copytree(source, destination)
pages = list(destination.rglob("*.html"))
for path in pages:
    text = path.read_text()
    text, count = re.subn(r'<meta name="robots" content="[^"]*">',
                          '<meta name="robots" content="noindex, nofollow">', text)
    if count != 1:
        sys.exit(f"Expected one robots tag: {path}")
    text = re.sub(r'\s*<!-- Cloudflare Web Analytics -->.*?<!-- End Cloudflare Web Analytics -->',
                  '', text, flags=re.S)
    if "cloudflareinsights.com" in text:
        sys.exit(f"Unexpected analytics script: {path}")
    path.write_text(text)
(destination / "_headers").write_text("/*\n  X-Robots-Tag: noindex, nofollow\n")
(destination / "robots.txt").write_text("User-agent: *\nDisallow: /\n")
print(f"Prepared {len(pages)} preview pages with indexing and analytics disabled.")
