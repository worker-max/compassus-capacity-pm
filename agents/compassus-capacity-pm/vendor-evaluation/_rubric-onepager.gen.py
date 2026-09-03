#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renders `Vendor-Scorecard-Rubric.pdf` — the companion page to the fast scorecard.

One portrait page: what we score, how we mark it, what raises a flag instead, and what the
number means. Deliberately short — the page is allowed to end early.

    python3 _rubric-onepager.gen.py
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
W, H = 1360, 1760                       # US Letter proportion
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

INK, MUTED, RULE, PAPER = "#1B211E", "#5A6560", "#C9CCC5", "#FBFBF8"
CAP, SCH, ENG = "#1F6F78", "#2E599D", "#4E8A5B"
GOLD, MAROON, PURPLE = "#C6A01F", "#792E2E", "#795CA7"

MARKS = [
    ("A1", "Home Care Home Base integration", "20", GOLD),
    ("Section B", "Capacity", "12", CAP),
    ("Section B", "Scheduling", "12", SCH),
    ("Section B", "Engagement", "12", ENG),
    ("Section C", "Sophistication", "20", PURPLE),
    ("D1&ndash;D3", "Clinician fit", "12", INK),
    ("E1&ndash;E4", "Partnership", "12", INK),
]

SCALES = [
    ("Home Care Home Base &nbsp;<em>A1</em>", GOLD, [
        ("20", "Live, established customer base"),
        ("16", "Live, small customer base"),
        ("12", "Live through a partner"),
        ("6", "In development, with a date"),
        ("2", "On the roadmap, no date"),
        ("0", "None, and no path")]),
    ("Scope &nbsp;<em>Section B</em>", CAP, [
        ("5", "Most of it"),
        ("4", "More than half"),
        ("3", "About half"),
        ("2", "Less than half"),
        ("1", "A corner of it"),
        ("0", "Nothing here")]),
    ("Sophistication &nbsp;<em>Section C</em>", PURPLE, [
        ("4", "Runs it &mdash; decides across the whole picture"),
        ("3", "Recommends it &mdash; proposes; a person confirms"),
        ("2", "Checks it &mdash; applies rules, flags problems"),
        ("1", "Shows it &mdash; surfaces the information only"),
        ("0", "Not addressed")]),
    ("Clinician fit &nbsp;<em>D1&ndash;D3</em>", INK, [
        ("4", "Strong fit"),
        ("3", "Good fit"),
        ("2", "Workable"),
        ("1", "Poor fit"),
        ("0", "Not answered")]),
    ("Partnership &nbsp;<em>E1&ndash;E4</em>", INK, [
        ("4", "Open to equity or a stake, and set up to build it with us"),
        ("3", "Ready to build to our needs; ownership not addressed"),
        ("2", "Will take our input; they own the roadmap"),
        ("1", "A standard customer relationship"),
        ("0", "Not answered")]),
]

FLAGS = [("A2", "Customers, scale and references"),
         ("A3", "Measured impact"),
         ("C6", "What happens when their product is down")]

BANDS = [("80&ndash;100", "Advance"), ("65&ndash;79", "Consider"),
         ("50&ndash;64", "Hold"), ("Under 50", "Decline")]


def build():
    marks = "".join(
        f'''<li style="--c:{col}"><span class="q">{q}</span>
             <span class="m">{name}</span><span class="p">{pts}</span></li>'''
        for q, name, pts, col in MARKS)

    cols = ""
    for title, col, rungs in SCALES:
        rows = "".join(f'<li><span class="n">{n}</span><span class="d">{d}</span></li>'
                       for n, d in rungs)
        cols += (f'<div class="scale" style="--c:{col}">'
                 f'<p class="st">{title}</p><ul>{rows}</ul></div>')

    flags = "".join(f'<li><span class="fq">{q}</span>{name}</li>' for q, name in FLAGS)
    bands = "".join(f'<li><span class="bn">{rng}</span><span class="bl">{lbl}</span></li>'
                    for rng, lbl in BANDS)

    return f'''<style>
@page{{size:{W}pt {H}pt;margin:0}}
*{{box-sizing:border-box}}
:root{{
  --ink:{INK};--muted:{MUTED};--rule:{RULE};--paper:{PAPER};--gold:{GOLD};--maroon:{MAROON};
  --body:"Avenir Next",Avenir,"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;
  --display:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,"Cascadia Mono","Roboto Mono",Menlo,Consolas,monospace;
}}
body{{margin:0;background:#F2F3EF}}
.sheet{{width:{W}px;height:{H}px;background:var(--paper);color:var(--ink);
  font-family:var(--body);padding:70px 84px;-webkit-font-smoothing:antialiased}}

.hd{{border-bottom:1.5px solid var(--ink);padding-bottom:20px}}
.eyebrow{{font-family:var(--mono);font-size:13px;font-weight:700;letter-spacing:.18em;
  color:#7C8781;margin:0 0 11px;text-transform:uppercase}}
h1{{font-family:var(--display);font-size:52px;font-weight:400;margin:0;letter-spacing:-.013em}}
.deck{{font-size:18px;color:var(--muted);margin:15px 0 0;line-height:1.5;max-width:820px}}

h2{{font-family:var(--mono);font-size:12.5px;font-weight:700;letter-spacing:.15em;
  color:var(--muted);text-transform:uppercase;margin:44px 0 16px;padding-bottom:9px;
  border-bottom:1px solid var(--rule)}}
ul{{list-style:none;margin:0;padding:0}}

.marks li{{display:grid;grid-template-columns:132px 1fr 54px;align-items:baseline;
  column-gap:20px;padding:11px 0;border-bottom:1px solid #E6E8E2}}
.marks li:last-child{{border-bottom:0}}
.q{{font-family:var(--mono);font-size:13px;color:var(--muted)}}
.m{{font-size:20px;font-weight:600;color:var(--c)}}
.p{{font-family:var(--display);font-size:26px;text-align:right;color:var(--c)}}
.tot{{display:grid;grid-template-columns:132px 1fr 54px;column-gap:20px;
  border-top:1.5px solid var(--ink);margin-top:5px;padding-top:12px}}
.tot b{{grid-column:2;font-size:20px}}
.tot span{{grid-column:3;font-family:var(--display);font-size:29px;text-align:right}}

.scales{{display:grid;grid-template-columns:repeat(3,1fr);gap:34px 40px;
  align-items:start}}
.st{{font-size:16px;font-weight:600;color:var(--c);margin:0 0 9px;padding-bottom:7px;
  border-bottom:2px solid var(--c)}}
.st em{{font-style:normal;font-family:var(--mono);font-size:11.5px;color:var(--muted);
  letter-spacing:.04em}}
.scale li{{display:grid;grid-template-columns:24px 1fr;column-gap:11px;padding:5px 0}}
.n{{font-family:var(--display);font-size:18px;color:var(--c);text-align:right;line-height:1.25}}
.d{{font-size:14.5px;color:var(--muted);line-height:1.4}}

.bottom{{display:grid;grid-template-columns:1.35fr 1fr;gap:52px}}
.flags li{{display:grid;grid-template-columns:52px 1fr;column-gap:14px;font-size:16px;
  padding:7px 0;border-bottom:1px solid #E6E8E2}}
.flags li:last-child{{border-bottom:0}}
.fq{{font-family:var(--mono);font-size:13px;color:var(--maroon);font-weight:700}}
.fn{{margin:14px 0 0;font-size:15px;color:var(--muted);line-height:1.55}}

.bands li{{display:grid;grid-template-columns:96px 1fr;column-gap:16px;font-size:16px;
  padding:7px 0;border-bottom:1px solid #E6E8E2}}
.bands li:last-child{{border-bottom:0}}
.bn{{font-family:var(--mono);font-size:13.5px;color:var(--muted);text-align:right}}
.bl{{font-weight:600}}
</style>

<section class="sheet">

  <header class="hd">
    <p class="eyebrow">Compassus Home Health &middot; Capacity &amp; Scheduling</p>
    <h1>Vendor Scorecard</h1>
    <p class="deck">How we score each returned questionnaire. The rows are the questionnaire's own
      questions, in the order they appear on it. Seven marks a vendor.</p>
  </header>

  <h2>What we score</h2>
  <ul class="marks">{marks}</ul>
  <div class="tot"><b>Total</b><span>100</span></div>

  <h2>How we mark it</h2>
  <div class="scales">{cols}</div>

  <h2>Flags, bands</h2>
  <div class="bottom">
    <div>
      <ul class="flags">{flags}</ul>
      <p class="fn">These three raise a flag rather than moving the score. A vendor can score well
        and still carry one. We resolve it before advancing rather than trading it against points.</p>
      <p class="fn">Clinician fit is deliberately undescribed. It is our own read of what our
        clinicians will accept.</p>
    </div>
    <div><ul class="bands">{bands}</ul>
      <p class="fn">A vendor whose Home Care Home Base integration is not yet live shows as
        Conditional whatever the total.</p></div>
  </div>

</section>'''


def main():
    html = build()
    (HERE / "vendor-scorecard-rubric.html").write_text(html)
    tmp = HERE / "_render.html"
    tmp.write_text("<!doctype html><html><head><meta charset='utf-8'></head><body>"
                   + html + "</body></html>")

    from playwright.sync_api import sync_playwright
    pdf_p, png_p = str(HERE / "Vendor-Scorecard-Rubric.pdf"), str(HERE / "_rubric.png")
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + str(tmp.resolve()))
        pg.wait_for_timeout(500)
        need = pg.evaluate("""() => {
            const s = document.querySelector('.sheet');
            const prev = s.style.height; s.style.height = 'auto';
            const h = Math.ceil(s.getBoundingClientRect().height);
            s.style.height = prev; return h;
        }""")
        print(f"content {need}px of {H}px  ({H - need}px of white below)")
        pg.screenshot(path=png_p, full_page=True)
        pg.emulate_media(media="print", color_scheme="light")
        pg.pdf(path=pdf_p, width=f"{W / 72:.4f}in", height=f"{H / 72:.4f}in",
               print_background=True, prefer_css_page_size=True)
        b.close()
    tmp.unlink()

    import pymupdf
    d = pymupdf.open(pdf_p)
    print(f"pdf pages={len(d)}  {png_p}")
    if len(d) != 1:
        print("!! not one page")


if __name__ == "__main__":
    main()
