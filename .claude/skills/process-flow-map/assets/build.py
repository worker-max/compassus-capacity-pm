#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build — wrap a flowkit SVG into the house HTML, screenshot it, and render the PDF.

    python3 build.py <svg> <out.html> <out.pdf> <png> "<Title>" <W> <H>

The screenshot is the point: you MUST open the PNG and look at it before shipping.
Collisions do not announce themselves.
"""
import pathlib
import sys

SKILL = pathlib.Path(__file__).resolve().parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def main():
    svg_p, html_p, pdf_p, png_p, title, W, H = sys.argv[1:8]
    W, H = int(W), int(H)

    svg = pathlib.Path(svg_p).read_text()
    tpl = (SKILL / "wrapper.html").read_text()
    html = (tpl.replace("__SVG__", svg)
               .replace("__TITLE__", title)
               .replace("__W", str(W))
               .replace("__H", str(H)))
    pathlib.Path(html_p).write_text(html)

    # The artifact host wraps a published file in <!doctype><head><body>, so the
    # renderer must do the same or the print CSS will not apply.
    doc = ("<!doctype html><html><head><meta charset='utf-8'></head><body>"
           + html + "</body></html>")
    tmp = pathlib.Path(html_p).with_suffix(".render.html")
    tmp.write_text(doc)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + str(tmp.resolve()))
        pg.wait_for_timeout(700)
        pg.screenshot(path=png_p, full_page=True)
        pg.emulate_media(media="print", color_scheme="light")
        # Chromium rejects "pt" here — convert to inches at 72pt/in.
        pg.pdf(path=pdf_p, width=f"{W/72:.4f}in", height=f"{H/72:.4f}in",
               print_background=True, prefer_css_page_size=True)
        b.close()
    tmp.unlink()

    import pymupdf
    d = pymupdf.open(pdf_p)
    print(f"pdf pages={len(d)} box={d[0].rect}   png={png_p}")
    if len(d) != 1:
        print("!! PDF is not one page — check the @page size against the canvas")
    print("NOW LOOK AT THE PNG.")


if __name__ == "__main__":
    main()
