"""Check the generated site, including internal links and fragment targets."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import sys
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.canonicals = [], [], []
        self.h1_count = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        self.h1_count += tag == "h1"
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])


root = Path(sys.argv[1]).resolve()
expected = ("index.html", "research/index.html", "publications/index.html",
            "collaborate/index.html", "group/index.html", "teaching/index.html",
            "service/index.html", "cv/index.html", "404.html")
errors, pages = [], {}
for name in expected:
    path = root / name
    if not path.is_file():
        errors.append(f"Missing page: {name}")
for path in root.rglob("*.html"):
    text = path.read_text()
    page = pages[path] = Page(text)
    name = path.relative_to(root).as_posix()
    if "{{" in text or "{%" in text:
        errors.append(f"Unrendered Liquid: {name}")
    if page.h1_count != 1:
        errors.append(f"Expected one h1: {name}")
    if len(page.canonicals) != 1 or not page.canonicals[0].startswith("https://bjerva.github.io/"):
        errors.append(f"Invalid canonical: {name}")
    for ident, count in Counter(page.ids).items():
        if count > 1:
            errors.append(f"Duplicate id: {name}#{ident}")
for path, page in pages.items():
    source_url = "/" + path.relative_to(root).as_posix()
    for link in page.links:
        parsed = urlsplit(urljoin(source_url, link))
        if parsed.scheme or parsed.netloc:
            continue
        target = root / unquote(parsed.path).lstrip("/")
        if target.is_dir():
            target /= "index.html"
        if not target.is_file():
            errors.append(f"Broken link in {source_url}: {link}")
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f"Missing fragment in {source_url}: {link}")
sitemap = ET.parse(root / "sitemap.xml")
urls = [node.text for node in sitemap.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
if "https://bjerva.github.io/collaborate/" not in urls:
    errors.append("Collaboration page missing from sitemap")
if errors:
    sys.exit("\n".join(errors))
print(json.dumps({"html_pages_checked": len(pages), "sitemap_urls": len(urls), "errors": 0}))
