# Render an approved HTML page to PDF, strip metadata, and check it.
# ONLY run after the owner has approved the HTML (see CLAUDE.md).
#   render_pdf.py <in.html> <out.pdf> "<PDF title>" [--embed-fonts <local.css>] [--expect-pages N]
# --embed-fonts swaps a Google Fonts <!--FONTS-->...<!--/FONTS--> block (or <link>) for a local
# @font-face file, because headless Chrome cannot reach fonts.googleapis.com through the proxy.
import sys, re, os, glob, subprocess, tempfile, argparse
from pypdf import PdfReader, PdfWriter
ap = argparse.ArgumentParser(); ap.add_argument("html"); ap.add_argument("pdf"); ap.add_argument("title")
ap.add_argument("--embed-fonts"); ap.add_argument("--expect-pages", type=int)
a = ap.parse_args()
h = open(a.html).read()
if a.embed_fonts:
    css = open(a.embed_fonts).read()
    css = css.replace("url(fonts/", "url(file://" + os.path.dirname(os.path.abspath(a.embed_fonts)) + "/fonts/")
    h = re.sub(r"<!--FONTS-->.*?<!--/FONTS-->", "<style>" + css + "</style>", h, flags=re.S)
    h = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>', "<style>" + css + "</style>", h)
tmp = os.path.join(os.path.dirname(os.path.abspath(a.html)), ".render.tmp.html")
open(tmp, "w").write(h)
chrome = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))[0]
raw = tmp + ".pdf"
subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                "--virtual-time-budget=10000", f"--print-to-pdf={raw}", "file://" + tmp],
               check=True, stderr=subprocess.DEVNULL)
w = PdfWriter(clone_from=PdfReader(raw)); w.metadata = {"/Title": a.title}; w.write(a.pdf)
os.remove(tmp); os.remove(raw)
r = PdfReader(a.pdf); data = open(a.pdf, "rb").read().lower()
leaks = [k for k in ["workforcewave", "worker@", "claude", "anthropic", "headlesschrome", "skia"] if k.encode() in data]
print("pages", len(r.pages), "| metadata", dict(r.metadata), "| leaks", leaks or "none")
if a.expect_pages and len(r.pages) != a.expect_pages: sys.exit(f"expected {a.expect_pages} pages")
if leaks: sys.exit("identifying strings found in PDF")
