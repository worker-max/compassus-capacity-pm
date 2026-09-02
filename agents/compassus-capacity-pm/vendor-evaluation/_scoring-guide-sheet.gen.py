#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renders `Vendor-Scoring-Guide.pdf` — the rubric on one landscape page.

    python3 _scoring-guide-sheet.gen.py        # writes .html, .pdf and .png beside this file

House type system per `.claude/skills/process-flow-map/reference/design-system.md`.
Canvas units are points on the output sheet — draw at sheet scale, never at A4 scale.
"""
import json
import os
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SPEC = json.load(open(HERE / ".." / ".." / ".." / ".claude" / "skills" /
                      "vendor-scorecard" / "assets" / "spec-elements.json"))
W, H = 2000, 1400   # set by the measure pass below; ratio ~1.43
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

INK, MUTED, RULE, PAPER, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#FBFBF8", "#E9E9E5"
CAP, SCH, ENG = "#1F6F78", "#2E599D", "#4E8A5B"
GOLD, MAROON = "#C6A01F", "#792E2E"

PARTS = [("1", "HCHB Integration", 25, "A1", GOLD),
         ("2", "Scope Footprint", 30, "Section B + C", INK),
         ("3", "Sophistication", 20, "Section C · A2 · A3", INK),
         ("4", "Clinician &amp; Adoption", 10, "Section D", INK),
         ("5", "Partnership", 15, "Section E", INK)]

RUNGS = [(25, "Live, bi-directional, multi-customer",
          "More than one customer, reads <em>and</em> writes, published API / HL7 / FHIR, dated."),
         (20, "Live, single customer or one-way",
          "In production &mdash; but one customer only, or it reads without writing back."),
         (12, "Live via a partner or a brittle method",
          "Third party, flat file, direct database, or screen automation."),
         (6, "In development, dated", "Building, with a committed date in the answer."),
         (2, "Roadmap, undated", "Named as intent. No date, no commitment."),
         (0, "None, and no path", "No integration and no credible route to one.")]

LADDER = [(0, "Not addressed", "Skipped, or answered without answering."),
          (1, "Asserted", "They say they do it. Nothing behind it."),
          (2, "Described", "We can picture the feature."),
          (3, "Mechanism", "We can picture <em>how it decides</em> &mdash; inputs, logic, configuration."),
          (4, "Proven", "Mechanism <strong>plus</strong> evidence: numbers, a named customer, a period, a baseline.")]

BANDS = [("Advance", "80&ndash;100", "Demo, references, deeper diligence.", "#DDEBE0"),
         ("Consider", "65&ndash;79", "Only if a differentiator justifies it.", "#F0F1EC"),
         ("Hold", "50&ndash;64", "Park unless the field thins.", "#F0F1EC"),
         ("Decline", "&lt; 50", "Close out with thanks.", "#F5E3E3")]

ITEMS = [("3", "Sophistication", 20, [
            ("S1", "Automation posture", "How much runs without a person?"),
            ("S2", "Decision depth", "Does it reason, or display?"),
            ("S3", "Readiness &amp; rules", "Ordered, but not yet schedulable."),
            ("S4", "Recovery", "Found, offered, filled &mdash; how fast?"),
            ("S5", "Enterprise trust", "Uptime, outage, commitment, scale.")]),
         ("4", "Clinician &amp; Adoption", 10, [
            ("D1", "What the clinician decides", "Change, approve, or locked."),
            ("D2", "Decide or advise", "And how far a customer can move it."),
            ("D3", "Adoption evidence", "Six months of it, or an assertion.")]),
         ("5", "Partnership", 15, [
            ("P1", "Sharing in the value", "Structure and terms, or enthusiasm."),
            ("P2", "Deployment &amp; change", "Including the resistance story."),
            ("P3", "What we did not ask", "Do they see it better than we asked?"),
            ("P4", "What they chose not to build", "Product judgement and candour.")])]


def arena_cards():
    out = []
    for arena, col in zip(SPEC["arenas"], (CAP, SCH, ENG)):
        n = sum(len(g["elements"]) for g in arena["groups"])
        groups = "".join(
            f'<li><span class="gn">{len(g["elements"])}</span>{g["name"]}</li>'
            for g in arena["groups"])
        out.append(f'''
        <article class="arena" style="--a:{col}">
          <header><p class="kick">{arena["kicker"]}</p>
            <h4>{arena["name"]}</h4>
            <p class="cnt"><b>{n}</b> elements &nbsp;·&nbsp; <b>10</b> points</p></header>
          <ul class="grp">{groups}</ul>
        </article>''')
    return "".join(out)


def build_html():
    parts = "".join(
        f'''<li style="--c:{col}"><span class="pn">{n}</span>
             <span class="pl">{name}</span>
             <span class="pbar"><i style="width:{pts / 30 * 100:.0f}%"></i></span>
             <span class="pp">{pts}</span>
             <span class="ps">{src}</span></li>''' for n, name, pts, src, col in PARTS)

    rungs = "".join(
        f'''<li{' class="top"' if p == 25 else ''}><span class="rp">{p}</span>
             <span class="rl">{lbl}</span><span class="rd">{d}</span></li>'''
        for p, lbl, d in RUNGS)

    ladder = "".join(
        f'''<li><span class="ln">{n}</span><span class="ll">{lbl}</span>
             <span class="ld">{d}</span></li>''' for n, lbl, d in LADDER)

    bands = "".join(
        f'''<li style="--b:{bg}"><span class="bl">{lbl}</span>
             <span class="br">{rng}</span><span class="bd">{d}</span></li>'''
        for lbl, rng, d, bg in BANDS)

    items = "".join(
        f'''<div class="ib"><p class="ih"><span>{n}</span>{title}
              <em>{pts} pts &nbsp;·&nbsp; ladder &times; {len(rows)}</em></p>
            <ul>{"".join(f'<li><b>{c}</b> {t} <span>{d}</span></li>' for c, t, d in rows)}</ul>
         </div>''' for n, title, pts, rows in ITEMS)

    return f'''<style>
@page{{size:{W}pt {H}pt;margin:0}}
*{{box-sizing:border-box}}
:root{{
  --ink:{INK};--muted:{MUTED};--rule:{RULE};--paper:{PAPER};--band:{BAND};
  --gold:{GOLD};--maroon:{MAROON};
  --body:"Avenir Next",Avenir,"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;
  --display:"Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,"Cascadia Mono","Roboto Mono",Menlo,Consolas,monospace;
}}
body{{margin:0;background:#F2F3EF}}
.sheet{{width:{W}px;height:{H}px;background:var(--paper);color:var(--ink);
  font-family:var(--body);padding:54px 62px 0;display:flex;flex-direction:column;
  -webkit-font-smoothing:antialiased}}

/* masthead */
.hd{{display:flex;justify-content:space-between;align-items:flex-end;
  border-bottom:1.5px solid var(--ink);padding-bottom:16px}}
.eyebrow{{font-family:var(--mono);font-size:12.5px;font-weight:700;letter-spacing:.17em;
  color:#7C8781;margin:0 0 9px;text-transform:uppercase}}
h1{{font-family:var(--display);font-size:52px;font-weight:400;margin:0;letter-spacing:-.012em}}
.deck{{font-size:16px;color:var(--muted);margin:0;max-width:660px;text-align:right;line-height:1.5}}

/* the one idea */
.idea{{display:flex;align-items:baseline;gap:22px;margin:22px 0 26px}}
.idea p{{margin:0;font-family:var(--display);font-size:27px;color:var(--ink);letter-spacing:-.008em}}
.idea p b{{color:var(--gold);font-weight:400;font-style:italic}}
.idea span{{font-family:var(--mono);font-size:12.5px;letter-spacing:.09em;color:var(--muted);
  border-left:1px solid var(--rule);padding-left:22px;line-height:1.55;max-width:520px}}

/* columns */
.cols{{display:grid;grid-template-columns:1.06fr 1fr .82fr;gap:44px;flex:1;min-height:0}}
.col{{display:flex;flex-direction:column;gap:26px;min-height:0}}
.blk{{display:flex;flex-direction:column;min-height:0}}
.grow{{flex:1}}
.grow>ul{{flex:1;display:flex;flex-direction:column;justify-content:space-around}}
.spread{{justify-content:space-between}}
.bh{{font-family:var(--mono);font-size:12.5px;font-weight:700;letter-spacing:.15em;
  color:var(--muted);margin:0 0 12px;padding-bottom:8px;border-bottom:1px solid var(--rule);
  display:flex;justify-content:space-between;align-items:baseline}}
.bh em{{font-style:normal;font-family:var(--body);font-size:13px;letter-spacing:0;
  color:#8B948E;text-transform:none}}
ul{{list-style:none;margin:0;padding:0}}

/* five parts */
.parts li{{display:grid;grid-template-columns:26px 1fr 92px 40px;
  grid-template-areas:"n l b p" ". s s s";align-items:center;
  padding:11px 0;border-bottom:1px solid #E4E6E0;column-gap:12px}}
.parts li:last-child{{border-bottom:0}}
.pn{{grid-area:n;font-family:var(--mono);font-size:13px;font-weight:700;color:var(--c)}}
.pl{{grid-area:l;font-size:17px;font-weight:600;color:var(--c)}}
.pbar{{grid-area:b;height:7px;background:#E4E6E0;display:block;border-radius:4px;overflow:hidden}}
.pbar i{{display:block;height:100%;background:var(--c);border-radius:4px}}
.pp{{grid-area:p;font-family:var(--display);font-size:25px;text-align:right;color:var(--c)}}
.ps{{grid-area:s;font-size:12.5px;color:var(--muted);padding-top:3px}}
.total{{display:flex;justify-content:space-between;align-items:baseline;
  border-top:1.5px solid var(--ink);margin-top:4px;padding-top:11px}}
.total b{{font-family:var(--mono);font-size:12.5px;letter-spacing:.15em}}
.total span{{font-family:var(--display);font-size:31px}}

/* hchb ladder */
.hchb{{background:#FBF6E4;border:1px solid #E8D9A4;border-left:4px solid var(--gold);
  padding:17px 20px 17px;margin-top:2px}}
.hchb .bh{{border-bottom-color:#E4D6A8;color:#8A7220}}
.rungs li{{display:grid;grid-template-columns:38px 1fr;grid-template-areas:"p l" ". d";
  padding:7px 0;border-bottom:1px solid #EEE6CC;column-gap:12px}}
.rungs li:last-child{{border-bottom:0}}
.rungs li.top{{background:rgba(198,160,31,.13);margin:0 -8px;padding:8px 8px 8px 8px;
  grid-template-columns:46px 1fr}}
.rp{{grid-area:p;font-family:var(--display);font-size:21px;color:#8A7220;text-align:right}}
.rl{{grid-area:l;font-size:14.5px;font-weight:600}}
.rd{{grid-area:d;font-size:12.5px;color:#7A7458;line-height:1.42;padding-top:2px}}

/* arenas */
.arena{{border-top:3px solid var(--a);padding-top:11px;margin-bottom:15px}}
.arena .kick{{font-family:var(--mono);font-size:11px;letter-spacing:.13em;
  text-transform:uppercase;color:var(--a);margin:0 0 4px;opacity:.85}}
.arena h4{{margin:0;font-size:18px;font-weight:600;color:var(--a)}}
.arena .cnt{{margin:3px 0 8px;font-size:12.5px;color:var(--muted)}}
.arena .cnt b{{color:var(--ink)}}
.grp li{{font-size:13px;color:var(--muted);padding:2.5px 0;display:flex;gap:10px}}
.gn{{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--a);
  min-width:16px;text-align:right;padding-top:1px}}

/* marks */
.marks{{display:flex;gap:10px;margin-top:2px}}
.marks div{{flex:1;border:1px solid var(--rule);padding:9px 11px;background:#fff}}
.marks b{{display:block;font-size:14px;margin-bottom:3px}}
.marks span{{font-size:11.5px;color:var(--muted);line-height:1.38;display:block}}
.marks em{{font-family:var(--display);font-size:17px;color:var(--ink);font-style:normal;
  float:right;margin-top:-2px}}

/* ladder items */
.ib{{margin-bottom:13px}}
.ih{{margin:0 0 5px;font-size:14.5px;font-weight:600;display:flex;align-items:baseline;gap:8px}}
.ih span{{font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--muted)}}
.ih em{{margin-left:auto;font-style:normal;font-family:var(--mono);font-size:11px;
  letter-spacing:.05em;color:#8B948E}}
.ib ul li{{font-size:12.5px;color:var(--muted);padding:2.5px 0 2.5px 22px;line-height:1.4}}
.ib ul li b{{font-family:var(--mono);font-size:11.5px;color:var(--ink);
  margin-left:-22px;margin-right:7px}}
.ib ul li span{{color:#8B948E}}

/* evidence ladder */
.lad li{{display:grid;grid-template-columns:30px 1fr;grid-template-areas:"n l" ". d";
  padding:7.5px 0;border-bottom:1px solid #E4E6E0;column-gap:10px}}
.lad li:last-child{{border-bottom:0}}
.ln{{grid-area:n;font-family:var(--display);font-size:22px;color:var(--muted)}}
.ll{{grid-area:l;font-size:14.5px;font-weight:600}}
.ld{{grid-area:d;font-size:12.5px;color:var(--muted);line-height:1.42;padding-top:1px}}
.lad li:last-child .ln,.lad li:last-child .ll{{color:var(--ink)}}

/* bands */
.bands li{{display:grid;grid-template-columns:1fr 74px;grid-template-areas:"l r" "d d";
  background:var(--b);padding:8px 12px;margin-bottom:5px;column-gap:8px}}
.bl{{grid-area:l;font-size:14.5px;font-weight:600}}
.br{{grid-area:r;font-family:var(--mono);font-size:12.5px;text-align:right;
  color:var(--muted);padding-top:2px}}
.bd{{grid-area:d;font-size:12px;color:var(--muted)}}
.cond{{border:1px solid var(--maroon);border-left:4px solid var(--maroon);
  padding:11px 14px;margin-top:9px;background:#FCF6F6}}
.cond b{{font-size:13.5px;color:var(--maroon);display:block;margin-bottom:3px}}
.cond span{{font-size:12.5px;color:#6E5A5A;line-height:1.45;display:block}}

/* not scored */
.ns li{{display:grid;grid-template-columns:24px 1fr;grid-template-areas:"i l" ". d";
  padding:8px 0;border-bottom:1px solid #E4E6E0;column-gap:8px}}
.ns li:last-child{{border-bottom:0}}
.ns i{{grid-area:i;font-style:normal;font-size:14px}}
.ns b{{grid-area:l;font-size:14.5px}}
.ns span{{grid-area:d;font-size:12.5px;color:var(--muted);line-height:1.42;padding-top:2px}}

/* footer */
.ft{{display:flex;justify-content:space-between;font-family:var(--mono);font-size:11.5px;
  letter-spacing:.06em;color:#8B948E;border-top:1px solid var(--rule);
  margin-top:26px;padding:13px 0 0}}
.ft em{{font-style:italic;font-family:var(--body);letter-spacing:0;font-size:12.5px}}
</style>

<section class="sheet">
  <header class="hd">
    <div><p class="eyebrow">Compassus &middot; Home Health &middot; Vendor Evaluation</p>
      <h1>The Scoring Guide</h1></div>
    <p class="deck">Sixteen returned questionnaires, one shortlist. Five parts, one hundred points,
      and three lists that carry what a number cannot.</p>
  </header>

  <div class="idea">
    <p>Every part is <b>a percentage times a budget.</b></p>
    <span>One exception, on purpose: HCHB integration is a checkbox ladder, not a judgement &mdash;
      so the priority cannot drift.</span>
  </div>

  <div class="cols">
    <div class="col">
      <div class="blk">
        <p class="bh">THE FIVE PARTS <em>100 points</em></p>
        <ul class="parts">{parts}</ul>
        <div class="total"><b>TOTAL</b><span>100</span></div>
      </div>
      <div class="blk hchb grow">
        <p class="bh">1 &nbsp;·&nbsp; THE HCHB LADDER <em>tick one, from A1</em></p>
        <ul class="rungs">{rungs}</ul>
      </div>
    </div>

    <div class="col spread">
      <div class="blk">
        <p class="bh">2 &nbsp;·&nbsp; SCOPE FOOTPRINT <em>41 elements &middot; 30 points</em></p>
        {arena_cards()}
        <div class="marks">
          <div><b>Covered <em>1.0</em></b><span>Does it today. Stated plainly, or walked through
            in Section C.</span></div>
          <div><b>Partial <em>0.5</em></b><span>Adjacent, configurable, by a partner, roadmapped
            &mdash; or claimed with no detail.</span></div>
          <div><b>&mdash; <em>0</em></b><span>Absent, out of scope, or done by a person in their
            model.</span></div>
        </div>
      </div>
      <div class="blk">
        <p class="bh">3&ndash;5 &nbsp;·&nbsp; THE TWELVE ITEMS <em>each on the ladder</em></p>
        {items}
      </div>
    </div>

    <div class="col spread">
      <div class="blk">
        <p class="bh">THE EVIDENCE LADDER <em>parts 3, 4 and 5</em></p>
        <ul class="lad">{ladder}</ul>
      </div>
      <div class="blk">
        <p class="bh">BANDS</p>
        <ul class="bands">{bands}</ul>
        <div class="cond"><b>Conditional &mdash; HCHB under 12</b>
          <span>Any band, but advancing means naming what we accept: an integration to be built,
            on their timeline, at our risk. Ties break on HCHB, then Scheduling.</span></div>
      </div>
      <div class="blk">
        <p class="bh">NOT SCORED <em>and often decisive</em></p>
        <ul class="ns">
          <li><i>&#9733;</i><b>Differentiators</b><span>Three to five lines. Against the field
            &mdash; and against our own thinking.</span></li>
          <li><i>&#9873;</i><b>Flags</b><span>Red is a stop-check. Yellow is a watch. Carried
            beside the score, never buried inside it.</span></li>
          <li><i>?</i><b>Unknowns</b><span>What they did not answer. It scores zero, and it
            becomes the demo agenda.</span></li>
        </ul>
      </div>
    </div>
  </div>

  <footer class="ft">
    <p><em>This scores a questionnaire, not a product &mdash; it decides who gets a demo, and
      nothing more.</em></p>
    <p>RUBRIC v1.0 &nbsp;·&nbsp; 41 SPEC ELEMENTS, OVERVIEW TAB &nbsp;·&nbsp;
      FORM_VERSION 2026-08-19</p>
  </footer>
</section>'''


def measure(pg):
    """Content height with the sheet un-clamped — so the canvas fits rather than guesses."""
    return pg.evaluate("""() => {
        const s = document.querySelector('.sheet');
        const prev = s.style.height; s.style.height = 'auto';
        const h = Math.ceil(s.getBoundingClientRect().height);
        s.style.height = prev; return h;
    }""")


def main():
    global H
    html = build_html()
    (HERE / "vendor-scoring-guide.html").write_text(html)
    doc = ("<!doctype html><html><head><meta charset='utf-8'></head><body>"
           + html + "</body></html>")
    tmp = HERE / "_render.html"
    tmp.write_text(doc)

    from playwright.sync_api import sync_playwright
    pdf_p = str(HERE / "Vendor-Scoring-Guide.pdf")
    png_p = str(HERE / "_scoring-guide.png")
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)
        pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        pg.goto("file://" + str(tmp.resolve()))
        pg.wait_for_timeout(500)

        # measure → re-render at the height the content actually needs
        need = measure(pg) + 54          # + the bottom padding the layout lacks
        if abs(need - H) > 6:
            H = need
            html = build_html()
            (HERE / "vendor-scoring-guide.html").write_text(html)
            tmp.write_text("<!doctype html><html><head><meta charset='utf-8'></head><body>"
                           + html + "</body></html>")
            pg.set_viewport_size({"width": W, "height": H})
            pg.goto("file://" + str(tmp.resolve()))
            pg.wait_for_timeout(500)
        print(f"canvas {W} x {H}   ratio {W / H:.2f}")

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
        print("!! not one page — check @page against the canvas")
    print("NOW LOOK AT THE PNG.")


if __name__ == "__main__":
    main()
