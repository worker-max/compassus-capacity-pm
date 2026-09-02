# -*- coding: utf-8 -*-
"""Render the review draft as a self-contained HTML page."""
import html
import pathlib

from review_content import (FRAMING, LEVERS, FUTURE, DATA, FUTURE_DATA, CLOSING)

E = html.escape

CSS = """
:root{--ink:#1a1a1a;--navy:#1F3864;--mute:#5f6672;--rule:#dfe3e8;--paper:#fff;
--wash:#f6f8fa;--tag:#e8eef7;--warm:#fff8e6;--warmline:#e0b32e;--cond:#fdf0ef;--condline:#c0524a}
*{box-sizing:border-box}
body{margin:0;background:var(--wash);color:var(--ink);
font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}
.wrap{max-width:920px;margin:0 auto;padding:0 28px 96px}
header{background:var(--navy);color:#fff;padding:44px 0 38px;margin-bottom:34px}
header .wrap{padding-bottom:0}
h1{margin:0 0 6px;font-size:34px;letter-spacing:-.4px}
.sub{font-size:18px;opacity:.85;margin:0}
.note{background:var(--warm);border-left:4px solid var(--warmline);padding:14px 18px;
border-radius:0 6px 6px 0;margin:26px 0;font-size:15px}
h2{font-size:24px;color:var(--navy);margin:52px 0 6px;padding-bottom:10px;
border-bottom:2px solid var(--rule)}
h2 .lead{font-size:15px;color:var(--mute);font-weight:400;display:block;margin-top:8px;border:0}
.card{background:var(--paper);border:1px solid var(--rule);border-radius:10px;
padding:22px 26px;margin:18px 0;box-shadow:0 1px 2px rgba(16,24,40,.04)}
.lever-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.tag{background:var(--tag);color:var(--navy);font-weight:700;font-size:12px;letter-spacing:.6px;
padding:4px 9px;border-radius:5px;white-space:nowrap}
h3{margin:0;font-size:20px;color:var(--navy)}
.def{color:#3d4450;font-style:italic;margin:12px 0 4px;padding-left:14px;
border-left:3px solid var(--tag)}
ul{margin:14px 0 0;padding-left:0;list-style:none}
li{display:flex;gap:12px;margin:0 0 11px;align-items:flex-start}
li .n{color:var(--mute);font-size:12px;font-variant-numeric:tabular-nums;min-width:38px;
padding-top:3px;font-weight:600}
li .t{flex:1}
.connect .t{font-weight:600}
.connect .n{color:var(--navy)}
.condition .t{background:var(--cond);border-left:3px solid var(--condline);padding:9px 13px;
border-radius:0 5px 5px 0}
.condition .n{color:var(--condline)}
.mini{font-size:12px;font-weight:700;letter-spacing:.8px;text-transform:uppercase;
color:var(--mute);margin:20px 0 8px}
.future{background:#fbfbfc}.future h3{color:#4a5262}
.new{background:#e6f4ea;color:#1e6b34;font-size:10px;font-weight:700;letter-spacing:.5px;
padding:3px 7px;border-radius:4px;margin-left:6px;vertical-align:2px}
footer{margin-top:56px;padding-top:22px;border-top:2px solid var(--rule);color:var(--mute);font-size:14px}
.howto{background:#eef4ff;border:1px solid #cddcfa;border-radius:10px;padding:18px 22px;margin:26px 0}
.howto strong{color:var(--navy)}
@media print{body{background:#fff}
header{background:#fff;color:var(--navy);padding:0 0 18px;border-bottom:3px solid var(--navy)}
.card{break-inside:avoid;box-shadow:none}.howto{display:none}}
"""


def bullets(items, prefix):
    out = []
    for i, item in enumerate(items, start=1):
        kind, text = item if isinstance(item, tuple) else ("", item)
        cls = f' class="{kind}"' if kind else ""
        out.append(f'<li{cls}><span class="n">{prefix}.{i}</span>'
                   f'<span class="t">{E(text)}</span></li>')
    return "\n".join(out)


NEW = {"L1", "L2", "L4", "L7", "L8", "D1", "D2", "D4", "D7", "D8"}


def card(item, cls=""):
    tag = item["id"]
    flag = '<span class="new">UPDATED</span>' if tag in NEW else ""
    return f"""<div class="card {cls}">
  <div class="lever-head"><span class="tag">{tag}</span><h3>{E(item['name'])}{flag}</h3></div>
  <p class="def">{E(item['def'])}</p>
  <ul>
{bullets(item['points'], tag)}
  </ul>
</div>"""


def data_card(d, cls=""):
    flag = '<span class="new">UPDATED</span>' if d["id"] in NEW else ""
    b = bullets(d["baseline"], d["id"])
    n = len(d["baseline"])
    o = "\n".join(
        f'<li><span class="n">{d["id"]}.{n+i}</span><span class="t">{E(t)}</span></li>'
        for i, t in enumerate(d["ongoing"], start=1))
    return f"""<div class="card {cls}">
  <div class="lever-head"><span class="tag">{d['id']}</span><h3>{E(d['name'])}{flag}</h3></div>
  <p class="mini">Baseline</p>
  <ul>
{b}
  </ul>
  <p class="mini">Ongoing measurement</p>
  <ul>
{o}
  </ul>
</div>"""


parts = [f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Capacity and Scheduling — Review Draft</title><style>{CSS}</style></head><body>
<header><div class="wrap"><h1>Capacity and Scheduling</h1>
<p class="sub">Value levers and measurement requirements &middot; review draft, second pass</p>
</div></header><div class="wrap">
<div class="howto"><strong>Review draft, second pass.</strong> Items marked
<span class="new">UPDATED</span> changed since your last read. Every item is numbered, so mark up
precisely and the Word version will be rebuilt to match. Note the levers renumbered when
Assessment Capacity Release was added as L2.</div>
<div class="note">A discussion document. It contains no figures by design. The first section sets
out how this program creates financial value. The second sets out what we would need to request in
order to size each item and to track it once underway.</div>
<h2>Why scheduling is a financial system<span class="lead">Five characteristics of this business
determine how the levers behave. Worth establishing before the list, because several items below
read as counterintuitive without them.</span></h2>
<div class="card"><ul>
{bullets(FRAMING, "F")}
</ul></div>
<h2>Section one &nbsp;&middot;&nbsp; Value levers</h2>"""]

parts += [card(l) for l in LEVERS]
parts.append('<h2>Identified but not yet quantified<span class="lead">Each is credible and '
             'deliberately carries no figure, because the data required to value it does not '
             'exist today.</span></h2>')
parts += [card(f, "future") for f in FUTURE]
parts.append('<h2>Section two &nbsp;&middot;&nbsp; Measurement requirements<span class="lead">'
             'Baseline data is required once, to establish current performance and size the '
             'opportunity. Ongoing data is what we would monitor thereafter to confirm the result. '
             'These are different requests: the first is a one-time extract, the second is a '
             'reporting commitment that needs an owner.</span></h2>')
parts += [data_card(d) for d in DATA]
parts += [data_card(d, "future") for d in FUTURE_DATA]
parts.append(f'<h2>On the scale of this request</h2><div class="card"><ul>\n'
             f'{bullets(CLOSING, "S")}\n</ul></div>')
parts.append('<footer>Review draft, second pass. No figures included by design. Mark up by item '
             'number and the Word version will be rebuilt to match.</footer></div></body></html>')

out = pathlib.Path(r"C:\Users\chigh\Downloads\Capacity-Scheduling-Review.html")
out.write_text("\n".join(parts), encoding="utf-8")
print("written", out, len(out.read_text(encoding='utf-8')), "chars")
