#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_win — Windows render shim for the process-flow-map skill.

Same contract as the skill's build.py, but drives installed Chrome via its CLI
instead of playwright's bundled Chromium (which is not present on this machine).

    python build_win.py <svg> <out.html> <out.pdf> <png> "<Title>" <W> <H>
"""
import pathlib
import subprocess
import sys
import tempfile

SKILL = pathlib.Path(r"C:\Users\chigh\compassus-capacity-pm\.claude\skills\process-flow-map\assets")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def main():
    svg_p, html_p, pdf_p, png_p, title, W, H = sys.argv[1:8]
    W, H = int(W), int(H)

    svg = pathlib.Path(svg_p).read_text(encoding="utf-8")
    tpl = (SKILL / "wrapper.html").read_text(encoding="utf-8")
    html = (tpl.replace("__SVG__", svg)
               .replace("__TITLE__", title)
               .replace("__W", str(W))
               .replace("__H", str(H)))
    pathlib.Path(html_p).write_text(html, encoding="utf-8")

    doc = ("<!doctype html><html><head><meta charset='utf-8'></head><body>"
           + html + "</body></html>")
    tmp = pathlib.Path(html_p).with_suffix(".render.html")
    tmp.write_text(doc, encoding="utf-8")
    url = tmp.resolve().as_uri()

    profile = tempfile.mkdtemp(prefix="flowchrome-")
    base = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
            f"--user-data-dir={profile}", "--virtual-time-budget=4000"]

    subprocess.run(base + [f"--screenshot={pathlib.Path(png_p).resolve()}", f"--window-size={W},{H}", url],
                   check=True, capture_output=True)
    subprocess.run(base + [f"--print-to-pdf={pathlib.Path(pdf_p).resolve()}", "--no-pdf-header-footer", url],
                   check=True, capture_output=True)
    print(f"png {png_p}\npdf {pdf_p}\nhtml {html_p}")


if __name__ == "__main__":
    main()
