#!/usr/bin/env python3
"""Build the downloadable short CV from cv.html and _data/projects.yml.

Usage: python _scripts/build_cv_pdf.py --date 2026-09-27
Requires reportlab and PyYAML. Uses DejaVu Sans/Serif TrueType fonts; set
CV_FONT_DIR if they are installed outside /usr/share/fonts/truetype/dejavu.
Matplotlib's bundled DejaVu fonts are also detected when available.
The generated PDF is a dated snapshot, not a second manually maintained CV.
"""

from __future__ import annotations

import argparse
from datetime import date
from html import escape, unescape
import importlib.util
import os
from pathlib import Path
import re

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets/documents/johannes-bjerva-cv.pdf"
INK = colors.HexColor("#17212b")
MUTED = colors.HexColor("#4d5b67")
ACCENT = colors.HexColor("#ad4e32")
RULE = colors.HexColor("#d8d5ce")
WIDTH, HEIGHT = A4
MARGIN = 46
CONTENT_WIDTH = WIDTH - 2 * MARGIN


def normalise(value: str) -> str:
    """Use ordinary hyphens while retaining supported mathematical glyphs."""
    return unescape(value).translate(str.maketrans({
        "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-",
        "\u2014": "-", "\u2212": "-", "\u2018": "'", "\u2019": "'",
    }))


def plain(value: str) -> str:
    return re.sub(r"\s+", " ", normalise(re.sub(r"<[^>]+>", "", value))).strip()


def rich(value: str) -> str:
    """Retain the small, supported inline vocabulary used by the CV page."""
    value = normalise(value)
    value = re.sub(r"<br\s*/?>", "\n", value)
    value = value.replace("<strong>", "\x01").replace("</strong>", "\x02")
    value = value.replace("<em>", "\x03").replace("</em>", "\x04")
    value = re.sub(r"<[^>]+>", "", value)
    value = escape(value)
    return (value.replace("\x01", "<b>").replace("\x02", "</b>")
            .replace("\x03", "<i>").replace("\x04", "</i>")
            .replace("\n", "<br/>"))


def source_sections(source: str) -> dict[str, list[tuple[str, str]]]:
    result = {}
    for section in re.findall(r"<section\b[^>]*>(.*?)</section>", source, re.S):
        heading = re.search(r"<h2>(.*?)</h2>", section, re.S)
        if not heading:
            continue
        rows = re.findall(r"<time>(.*?)</time>\s*<p>(.*?)</p>", section, re.S)
        result[plain(heading.group(1))] = [
            (plain(when), rich(body)) for when, body in rows
        ]
    return result


def register_fonts() -> None:
    font_dirs = [Path(os.environ.get("CV_FONT_DIR", "/usr/share/fonts/truetype/dejavu"))]
    matplotlib = importlib.util.find_spec("matplotlib")
    if matplotlib and matplotlib.origin:
        font_dirs.append(Path(matplotlib.origin).parent / "mpl-data/fonts/ttf")
    for name, filename in [
        ("CVSans", "DejaVuSans.ttf"),
        ("CVSans-Bold", "DejaVuSans-Bold.ttf"),
        ("CVSans-Italic", "DejaVuSans-Oblique.ttf"),
        ("CVSans-BoldItalic", "DejaVuSans-BoldOblique.ttf"),
        ("CVSerif", "DejaVuSerif.ttf"),
    ]:
        font_path = next((directory / filename for directory in font_dirs
                          if (directory / filename).is_file()), None)
        if font_path is None:
            raise FileNotFoundError(f"Install DejaVu fonts or set CV_FONT_DIR: missing {filename}")
        pdfmetrics.registerFont(TTFont(name, str(font_path)))
    pdfmetrics.registerFontFamily(
        "CVSans", normal="CVSans", bold="CVSans-Bold",
        italic="CVSans-Italic", boldItalic="CVSans-BoldItalic",
    )


def build(snapshot: date) -> None:
    register_fonts()
    source = (ROOT / "cv.html").read_text(encoding="utf-8")
    sections = source_sections(source)
    projects = yaml.safe_load((ROOT / "_data/projects.yml").read_text(encoding="utf-8"))
    name = plain(re.search(r"<h1>(.*?)</h1>", source, re.S).group(1))
    role = plain(re.search(r'<p class="page-lead">(.*?)</p>', source, re.S).group(1))
    email = re.search(r'href="mailto:([^"]+)"', source).group(1)
    profile = re.search(r'href="(https://vbn\.aau\.dk/en/persons/[^\"]+)"', source).group(1)

    styles = {
        "name": ParagraphStyle("name", fontName="CVSerif", fontSize=27,
                               leading=32, textColor=INK, spaceAfter=7),
        "role": ParagraphStyle("role", fontName="CVSans", fontSize=10,
                               leading=15, textColor=MUTED),
        "meta": ParagraphStyle("meta", fontName="CVSans", fontSize=8,
                               leading=12, textColor=MUTED),
        "section": ParagraphStyle("section", fontName="CVSans-Bold", fontSize=11,
                                  leading=15, textColor=ACCENT, spaceBefore=14,
                                  spaceAfter=5, keepWithNext=True),
        "date": ParagraphStyle("date", fontName="CVSans-Bold", fontSize=8.1,
                               leading=12.5, textColor=ACCENT),
        "body": ParagraphStyle("body", fontName="CVSans", fontSize=9.1,
                               leading=12.5, textColor=INK, alignment=TA_LEFT),
    }
    story = [
        Paragraph("SHORT ACADEMIC CV", styles["meta"]), Spacer(1, 8),
        Paragraph(escape(name), styles["name"]),
        Paragraph(escape(role), styles["role"]), Spacer(1, 4),
        Paragraph(f'<link href="mailto:{escape(email)}">{escape(email)}</link>'
                  f' &nbsp; | &nbsp; <link href="{escape(profile)}">AAU Research Portal</link>'
                  ' &nbsp; | &nbsp; <link href="https://bjerva.github.io/cv/">Online CV</link>',
                  styles["meta"]),
        Spacer(1, 12), HRFlowable(width="100%", thickness=0.7, color=RULE),
    ]

    def add_section(title: str, rows: list[tuple[str, str]]) -> None:
        if not rows:
            raise ValueError(f"No CV entries found for {title}")
        story.append(Paragraph(escape(title), styles["section"]))
        for when, body in rows:
            date_label = re.sub(r"([A-Z][a-z]{2} \d{4})-([A-Z][a-z]{2} \d{4})",
                                r"\1 -<br/>\2", escape(when))
            table = Table([[Paragraph(date_label, styles["date"]),
                            Paragraph(body, styles["body"])]],
                          colWidths=[90, CONTENT_WIDTH - 90], hAlign="LEFT")
            table.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, -1), 12),
                ("RIGHTPADDING", (1, 0), (1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]))
            story.append(KeepTogether([table]))

    for title in ["Appointments", "Education", "Selected leadership"]:
        add_section(title, sections[title])

    story.extend([PageBreak(), Paragraph("FUNDING, SERVICE AND RECOGNITION", styles["meta"])])
    awards = list(projects)
    awards.extend(project["related_award"] for project in projects if project.get("related_award"))
    rows = []
    for award in sorted(awards, key=lambda a: a["award_year"], reverse=True):
        title = escape(normalise(award["title"]))
        if award.get("url"):
            title = f'<link href="{escape(award["url"])}">{title}</link>'
        details = f'{award["funder"]} · ' if award.get("funder") else ""
        details += award["amount"]
        if "co-led" in award.get("funding_share", ""):
            details += f' (total award; {award["funding_share"]})'
        rows.append((str(award["award_year"]), f"<b>{title}</b><br/>{escape(normalise(details))}"))
    add_section("Selected research funding", rows)
    add_section("Selected academic service", sections["Selected academic service"])
    add_section("Memberships, policy & recognition", sections["Memberships, policy & recognition"])
    story.extend([
        Spacer(1, 18), HRFlowable(width="100%", thickness=0.7, color=RULE), Spacer(1, 10),
        Paragraph('The <link href="' + escape(profile) + '">AAU Research Portal</link> provides '
                  'a fuller institutional record of projects, outputs, activities, supervision, '
                  'and media appearances.', styles["meta"]),
    ])

    stamp = f"{snapshot.day} {snapshot.strftime('%B')} {snapshot.year}"

    def footer(canvas, doc) -> None:
        canvas.saveState()
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(MARGIN, 41, WIDTH - MARGIN, 41)
        canvas.setFont("CVSans", 7)
        canvas.setFillColor(MUTED)
        canvas.drawString(MARGIN, 28, f"{name}  |  Source snapshot: {stamp}")
        canvas.drawRightString(WIDTH - MARGIN, 28, str(doc.page))
        canvas.restoreState()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=MARGIN,
                            rightMargin=MARGIN, topMargin=36, bottomMargin=55,
                            title=f"{name} - Short academic CV",
                            author=name, subject=f"Academic CV; source snapshot {stamp}",
                            pageCompression=1)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="2026-09-27", help="Source snapshot date (YYYY-MM-DD)")
    build(date.fromisoformat(parser.parse_args().date))
