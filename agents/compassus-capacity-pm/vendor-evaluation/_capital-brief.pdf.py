#!/usr/bin/env python3
"""Print Vendor-Capital-Brief.html to Letter PDF.

Run _capital-brief.gen.py first. The print styling lives in the page's own
@media print block, not here — this script only drives the browser, so the
screen and paper versions can never drift apart.
"""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "Vendor-Capital-Brief.html"
OUT = HERE / "Vendor-Capital-Brief.pdf"

# The artifact fragment needs a document around it before a browser will print it.
SHELL = ('<!doctype html><html><head><meta charset=utf8>'
         '<meta name=viewport content="width=device-width,initial-scale=1">'
         '<style>body{margin:0}img{max-width:100%}</style></head><body>'
         + SRC.read_text() + '</body></html>')
tmp = HERE / "_print.tmp.html"
tmp.write_text(SHELL)

FOOTER = (
    '<div style="width:100%;font-family:-apple-system,sans-serif;font-size:7.5pt;'
    'color:#6E7683;padding:0 13mm;display:flex;justify-content:space-between;">'
    '<span>Compassus &middot; Vendor Capital Ledger &middot; 9 September 2026 &middot; '
    'public sources only</span>'
    '<span class="pageNumber"></span>/<span class="totalPages"></span></div>')

try:
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
        pg = b.new_page()
        # A reader's dark mode must never print as a black slab.
        pg.emulate_media(color_scheme="light", media="print")
        pg.goto(tmp.as_uri(), wait_until="networkidle")
        pg.wait_for_timeout(2500)          # let the webfonts land
        pg.pdf(path=str(OUT), format="Letter", print_background=True,
               margin={"top": "14mm", "bottom": "16mm",
                       "left": "13mm", "right": "13mm"},
               display_header_footer=True,
               header_template="<div></div>", footer_template=FOOTER)
        b.close()
finally:
    tmp.unlink(missing_ok=True)

print(f"Wrote {OUT.name}  ({OUT.stat().st_size // 1024} KB)")
