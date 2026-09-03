#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renders `Vendor-Scoring-Options.pdf` — one portrait page, two sections.

Top: option one, the full scorecard. Bottom: option two, the simple scorecard.
Written for a leader with five minutes, not for the person doing the scoring.

    python3 _options-onepager.gen.py
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
W, H = 1360, 1760          # portrait, ~US Letter proportion
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

INK, MUTED, RULE, PAPER = "#1B211E", "#5A6560", "#C9CCC5", "#FBFBF8"
CAP, SCH, ENG = "#1F6F78", "#2E599D", "#4E8A5B"
GOLD, MAROON = "#C6A01F", "#792E2E"

PARTS = [
    ("25", "Home Care Home Base integration", GOLD,
     "Do they already connect to the system our plans of care, orders and visits live in? "
     "Ticked from a list of six, not judged."),
    ("30", "Scope coverage", INK,
     "How much of the scope we published they actually cover — reported separately for "
     "capacity, scheduling and engagement."),
    ("20", "Sophistication", INK,
     "How much of the work the product does: shows it, checks it, recommends it, or runs it."),
    ("10", "Clinician fit", INK,
     "What the clinician still controls, and whether adoption is proven rather than promised."),
    ("15", "Partnership", INK,
     "Whether they will trade on the investment we are making."),
]

STEPS = [
    ("Home Care Home Base", "Picked from the same list of six."),
    ("Eleven areas", "The ones each vendor already rated themselves on in the questionnaire."),
    ("Two marks each", "What they have, and how much of the work it does, out of a hundred."),
    ("It adds up", "A coverage percentage and a rating for capacity, scheduling and engagement."),
]


def build():
    parts = "".join(
        f'''<li style="--c:{col}"><span class="pt">{pts}</span>
              <span class="pl">{name}</span><span class="pd">{desc}</span></li>'''
        for pts, name, col, desc in PARTS)
    steps = "".join(
        f'''<li><span class="sl">{name}</span><span class="sd">{desc}</span></li>'''
        for name, desc in STEPS)

    return f'''<style>
@page{{size:{W}pt {H}pt;margin:0}}
*{{box-sizing:border-box}}
:root{{
  --ink:{INK};--muted:{MUTED};--rule:{RULE};--paper:{PAPER};--gold:{GOLD};
  --body:"Avenir Next",Avenir,"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;
  --display:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,"Cascadia Mono","Roboto Mono",Menlo,Consolas,monospace;
}}
body{{margin:0;background:#F2F3EF}}
.sheet{{width:{W}px;height:{H}px;background:var(--paper);color:var(--ink);
  font-family:var(--body);padding:62px 84px;display:flex;flex-direction:column;
  -webkit-font-smoothing:antialiased}}

.hd{{border-bottom:1.5px solid var(--ink);padding-bottom:20px}}
.eyebrow{{font-family:var(--mono);font-size:13px;font-weight:700;letter-spacing:.18em;
  color:#7C8781;margin:0 0 11px;text-transform:uppercase}}
h1{{font-family:var(--display);font-size:52px;font-weight:400;margin:0;letter-spacing:-.014em}}
.deck{{font-size:18px;color:var(--muted);margin:14px 0 0;line-height:1.5;max-width:900px}}

.opt{{display:flex;gap:38px;padding:26px 0 0}}
.opt + .opt{{border-top:1px solid var(--rule);margin-top:24px}}
.num{{font-family:var(--display);font-size:88px;line-height:.78;color:var(--rule);
  min-width:96px;letter-spacing:-.03em}}
.body{{flex:1;min-width:0}}
.oh{{display:flex;align-items:baseline;justify-content:space-between;gap:24px;
  border-bottom:1px solid var(--rule);padding-bottom:13px}}
.oh h2{{font-family:var(--display);font-size:36px;font-weight:400;margin:0;letter-spacing:-.01em}}
.time{{font-family:var(--mono);font-size:14px;letter-spacing:.07em;color:var(--muted);
  white-space:nowrap}}
.lead{{font-size:19px;line-height:1.55;margin:14px 0 0;max-width:920px}}

ul{{list-style:none;margin:20px 0 0;padding:0}}
.parts li{{display:grid;grid-template-columns:64px 1fr;grid-template-areas:"t l" ". d";
  column-gap:22px;padding:9px 0;border-bottom:1px solid #E6E8E2}}
.parts li:last-child{{border-bottom:0}}
.pt{{grid-area:t;font-family:var(--display);font-size:32px;color:var(--c);text-align:right;
  line-height:1}}
.pl{{grid-area:l;font-size:20px;font-weight:600;color:var(--c);line-height:1.2}}
.pd{{grid-area:d;font-size:16px;color:var(--muted);line-height:1.5;padding-top:6px}}

.steps li{{display:grid;grid-template-columns:210px 1fr;column-gap:22px;
  padding:10px 0;border-bottom:1px solid #E6E8E2}}
.steps li:last-child{{border-bottom:0}}
.sl{{font-size:18px;font-weight:600}}
.sd{{font-size:16px;color:var(--muted);line-height:1.5}}

.why{{margin:18px 0 0;padding:16px 24px;border-left:3px solid var(--gold);background:#FBF7E9}}
.why p{{margin:0;font-size:16.5px;line-height:1.52;color:#453F2E}}
.why p + p{{margin-top:10px}}
.why b{{font-weight:600;color:var(--ink)}}
</style>

<section class="sheet">

  <header class="hd">
    <p class="eyebrow">Compassus Home Health &middot; Capacity &amp; Scheduling</p>
    <h1>Scoring the vendor questionnaires</h1>
    <p class="deck">Sixteen vendors have returned the questionnaire. Two ways to get from those
      to a shortlist &mdash; the same judgement, at two levels of depth.</p>
  </header>

  <div class="opt">
    <div class="num">1</div>
    <div class="body">
      <div class="oh"><h2>The full scorecard</h2>
        <span class="time">ABOUT 10 MINUTES A VENDOR</span></div>
      <p class="lead">Each questionnaire is scored out of a hundred across the five things we
        said mattered. The team picks from menus; the sheet does the arithmetic.</p>
      <ul class="parts">{parts}</ul>
      <div class="why">
        <p>Home Care Home Base is a quarter of the score and a <b>tick box rather than a
          judgement</b>, so the priority cannot get watered down as we work through sixteen
          vendors. Scope is measured against the one-pager we published, so each vendor is
          compared to <b>what we asked for</b> rather than to one another's marketing.</p>
        <p>Sophistication uses the <b>read, assist, control</b> language already in our workbook.
          It separates a product that shows a scheduler a number from one that works out the
          answer and acts on it. We score what the product does, not how much the vendor wrote
          about it &mdash; how something works is a question for the demo.</p>
        <p>Out of it comes a number we can defend line by line, and three short lists for each
          vendor: what makes them different, what worries us, and what to go and ask.</p>
      </div>
    </div>
  </div>

  <div class="opt">
    <div class="num">2</div>
    <div class="body">
      <div class="oh"><h2>The simple scorecard</h2>
        <span class="time">ABOUT 3 MINUTES A VENDOR</span></div>
      <p class="lead">The same judgement at a coarser grain &mdash; twelve rows a vendor
        instead of fifty.</p>
      <ul class="steps">{steps}</ul>
      <div class="why">
        <p>It follows the functional scorecard already in our workbook, so it <b>reads like
          something the team has seen before</b>. Most of it is transcription rather than
          judgement: what a vendor has comes straight from their own answer.</p>
        <p>Sophistication is still here &mdash; it is the rating out of a hundred, on the same
          read, assist, control idea, just given once per area instead of five times.</p>
        <p>This is the fast read across the field. What it cannot do is separate two vendors
          who both cover an area but do it very differently, and it carries no partnership or
          clinician score at all &mdash; so <b>where the shortlist is close, option one is the
          one that holds up.</b></p>
      </div>
    </div>
  </div>

</section>'''


def main():
    global H
    html = build()
    (HERE / "vendor-scoring-options.html").write_text(html)
    tmp = HERE / "_render.html"
    doc = "<!doctype html><html><head><meta charset='utf-8'></head><body>{}</body></html>"
    tmp.write_text(doc.format(html))

    from playwright.sync_api import sync_playwright
    pdf_p, png_p = str(HERE / "Vendor-Scoring-Options.pdf"), str(HERE / "_options.png")
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
        print(f"content needs {need}px in a {H}px page  ({need - H:+d})")
        pg.screenshot(path=png_p, full_page=True)
        pg.emulate_media(media="print", color_scheme="light")
        pg.pdf(path=pdf_p, width=f"{W / 72:.4f}in", height=f"{H / 72:.4f}in",
               print_background=True, prefer_css_page_size=True)
        b.close()
    tmp.unlink()

    import pymupdf
    d = pymupdf.open(pdf_p)
    print(f"pdf pages={len(d)} box={d[0].rect}  png={png_p}")
    if len(d) != 1:
        print("!! not one page")


if __name__ == "__main__":
    main()
