#!/usr/bin/env python3
"""Render the documentation pages to plain static HTML.

Each *.md chapter in this directory is converted to a matching *.html
file with a shared header (docs index + fingering viewer links), so the
site is served by GitHub Pages with no Jekyll build (.nojekyll sits in
this directory). Links between chapters are rewritten from .md to .html.

Usage: python3 render.py  (requires the python-markdown package)
"""
import re
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | 3D-Printed-One-Handed-Recorder</title>
<style>
:root {{ color-scheme: light; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; color: #1b2227; background: #fdfcf8; line-height: 1.6; }}
header {{ background: #16302b; color: #f2f6f4; padding: 14px 20px; }}
header nav {{ display: flex; gap: 18px; flex-wrap: wrap; max-width: 50rem; margin: 0 auto; align-items: baseline; }}
header .site {{ font-weight: 700; margin-right: auto; }}
header a {{ color: #bfe3d9; text-decoration: none; }}
header a:hover {{ color: #ffffff; }}
main {{ max-width: 50rem; margin: 0 auto; padding: 28px 20px 48px; }}
h1, h2, h3 {{ line-height: 1.25; }}
a {{ color: #0e6f66; }}
table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
th, td {{ border: 1px solid #d8d2c2; padding: 7px 10px; text-align: left; }}
th {{ background: #efece3; }}
blockquote {{ border-left: 4px solid #0e6f66; margin: 1rem 0; padding: 2px 14px; background: #f0f5f2; }}
code {{ background: #efece3; padding: 1px 5px; border-radius: 4px; }}
img {{ max-width: 100%; }}
</style>
</head>
<body>
<header><nav>
<span class="site">3D-Printed-One-Handed-Recorder</span>
<a href="1-index.html">Docs</a>
<a href="fingering_viewer.html">Fingering viewer</a>
</nav></header>
<main>
{body}
</main>
</body>
</html>
"""


def render_file(md_path):
    text = md_path.read_text()
    title = md_path.stem
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        fm = m.group(1)
        text = text[m.end():]
        t = re.search(r"^title:\s*(.+)$", fm, re.M)
        if t:
            title = t.group(1).strip()
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    body = re.sub(r'href="([^"#]+)\.md"', r'href="\1.html"', body)
    out = md_path.with_suffix(".html")
    out.write_text(TEMPLATE.format(title=title, body=body))
    return out


def main():
    for md_path in sorted(HERE.glob("*.md")):
        print("rendered", render_file(md_path).name)


if __name__ == "__main__":
    main()
