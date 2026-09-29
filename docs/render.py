#!/usr/bin/env python3
"""Render the documentation pages to plain static HTML.

Each *.md chapter in this directory is converted to a matching *.html
file with a shared header (docs index + fingering viewer links), so the
site is served by GitHub Pages with no Jekyll build (.nojekyll sits in
this directory). Links between chapters are rewritten from .md to .html.

Usage: python3 render.py  (requires the python-markdown package)
"""
import re
import sys
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
.toc {{ display: grid; gap: 6px; margin: 1rem 0 2rem; }}
section {{ border-top: 1px solid #d8d2c2; padding-top: 1rem; }}
.pager {{ display: flex; justify-content: space-between; gap: 1rem; margin-top: 2.5rem; border-top: 1px solid #d8d2c2; padding-top: 1rem; }}
.pager span {{ flex: 1; }}
footer.dates {{ margin-top: 3rem; color: #68747d; font-size: 0.85rem; }}
footer.dates img {{ vertical-align: middle; margin-right: 10px; }}
footer.dates .irem-mark {{ vertical-align: middle; margin-right: 12px; }}
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
<footer class="dates"><img class="irem-mark" src="IREM_Logo.png" alt="IREM" height="31"><a href="https://creativecommons.org/licenses/by-nc/4.0/"><img src="cc-by-nc-88x31.png" alt="CC BY-NC 4.0" width="88" height="31"></a> Published 2026-09-27 &middot; Last updated 2026-09-27<br>Website content &copy; IREM. The 3D designs (STL files) are free to download, print, modify, and share; commercial use requires permission.</footer>
</main>
</body>
</html>
"""


def load_chapter(md_path):
    """Return (title, markdown body) with frontmatter stripped."""
    text = md_path.read_text()
    title = md_path.stem
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        fm = m.group(1)
        text = text[m.end():]
        t = re.search(r"^title:\s*(.+)$", fm, re.M)
        if t:
            title = t.group(1).strip()
    return title, text


def render_file(md_path, prev=None, nxt=None):
    title, text = load_chapter(md_path)
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    body = re.sub(r'href="([^"#]+)\.md"', r'href="\1.html"', body)
    pager = ""
    if prev or nxt:
        left = ('<a href="%s">&larr; %s</a>'
                % (prev[0].with_suffix(".html").name, prev[1])) if prev else "<span></span>"
        right = ('<a href="%s">%s &rarr;</a>'
                 % (nxt[0].with_suffix(".html").name, nxt[1])) if nxt else "<span></span>"
        pager = '<nav class="pager">%s%s</nav>' % (left, right)
    out = md_path.with_suffix(".html")
    out.write_text(TEMPLATE.format(title=title, body=body + pager))
    return out


def render_single():
    """Render every chapter into one self-contained DOCUMENTATION.html
    with internal anchors, so it works opened from anywhere, including
    a file manager's transient copy."""
    chapters = [p for p in sorted(HERE.glob("*.md"), key=page_key)
                if p.name != "1-index.md" and p.name not in LOCAL_ONLY]
    nav, sections = [], []
    ids = {p.name: "chap-%d" % (i + 1) for i, p in enumerate(chapters)}
    for i, md_path in enumerate(chapters):
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
        body = re.sub(
            r'href="([^"#]+)\.md"',
            lambda mm: 'href="#%s"' % ids.get(mm.group(1) + ".md", ""),
            body)
        nav.append('<a href="#%s">%d. %s</a>' % (ids[md_path.name], i + 1, title))
        sections.append('<section id="%s">\n%s\n</section>'
                        % (ids[md_path.name], body))
    doc = TEMPLATE.format(
        title="Documentation",
        body=('<h1>3D-Printed-One-Handed-Recorder</h1>'
              '<p>All chapters in one page; the links below stay inside '
              'this file.</p>'
              '<p>Questions, inquiries, or update requests: '
              '<a href="mailto:irem25qc@gmail.com">irem25qc@gmail.com</a></p>'
              '<nav class="toc">%s</nav>%s'
              % ("".join(nav), "\n".join(sections))))
    out = HERE / "DOCUMENTATION.html"
    out.write_text(doc)
    return out


def page_key(md_path):
    m = re.match(r"(\d+)-", md_path.name)
    return int(m.group(1)) if m else 999


# Pages kept local-only (gitignored); rendered standalone with --with-a2
# and never linked, paged, or folded into the published site.
LOCAL_ONLY = {"model-A2.md"}


def main():
    with_local = "--with-a2" in sys.argv
    pages = [p for p in sorted(HERE.glob("*.md"), key=page_key)
             if p.name not in LOCAL_ONLY]
    for i, md_path in enumerate(pages):
        prev = (pages[i - 1], load_chapter(pages[i - 1])[0]) if i > 0 else None
        nxt = (pages[i + 1], load_chapter(pages[i + 1])[0]) \
            if i + 1 < len(pages) else None
        print("rendered", render_file(md_path, prev, nxt).name)
    print("rendered", render_single().name)
    for name in sorted(LOCAL_ONLY):
        p = HERE / name
        if with_local and p.exists():
            print("rendered", render_file(p).name)
        elif not with_local and p.exists():
            # published stand-in so the URL answers instead of 404
            out = p.with_suffix(".html")
            out.write_text(TEMPLATE.format(
                title=load_chapter(p)[0],
                body="<h1>%s</h1>\n<p>Coming soon.</p>"
                     % load_chapter(p)[0]))
            print("rendered", out.name, "(placeholder)")


if __name__ == "__main__":
    main()
