# -*- coding: utf-8 -*-
"""Product sophistication one-pager: where each vendor sits on six components of sophistication.
Positions are our read of the demo calls plus each vendor's RFP return, for team discussion; the
decision row mirrors the formal scorecard's sophistication mark. Vendors alphabetical; no ranking.
    python3 _sophistication-one-pager.gen.py  -> vendor-sophistication-one-pager.html
"""
import html, pathlib
OUT = pathlib.Path(__file__).with_name("vendor-sophistication-one-pager.html")
V = [("Arya", "AR", "#2a78d6", "#fff"), ("Axle Health", "AX", "#eb6834", "#fff"),
     ("CareStitch", "CS", "#1baf7a", "#0b2a1f"), ("VitalisCare", "VC", "#eda100", "#2a1d00")]
# (name, what it measures, 5 level labels, positions {abbr: level}, boundary_after)
ROWS = [
 ("Decision-making", "Who makes the call",
  ["Shows data", "Filters who is eligible", "Recommends", "Acts, with approval", "Acts on its own"],
  {"AR": 4, "AX": 3, "CS": 2, "VC": 3}, 4),
 ("Automation", "Who does the work",
  ["Person does it, better tools", "System prepares, person does", "System does, person approves each", "System does routine; people get exceptions", "End to end, exceptions too"],
  {"AR": 4, "AX": 3, "CS": 2, "VC": 3}, 4),
 ("Engagement", "Patients and clinicians",
  ["None", "Person-led, with tools", "One-way automated notices", "Two-way automated text", "Two-way text and voice agent"],
  {"AR": 4, "AX": 3, "CS": 2, "VC": 1}, None),
 ("Data visuals", "What leaders and schedulers see",
  ["Lists", "Calendars and maps", "Capacity by clinician and day", "Forecasts and leader dashboards", "Predictive, with reasons"],
  {"AR": 2, "AX": 4, "CS": 3, "VC": 4}, None),
 ("Learning", "How it gets better",
  ["Fixed rules", "Logs feedback for people", "Override reasons retune ranking", "Learns rules from feedback", "Learns, and shows what it learned"],
  {"AR": 4, "AX": 1, "CS": 2, "VC": 3}, None),
 ("Fit: enterprise and branch", "How it is shaped to Compassus",
  ["One setup for all", "Enterprise settings", "Enterprise plus branch settings", "Branch rules, weights and autonomy", "Branch and group, self-serve, governed"],
  {"AR": 4, "AX": 3, "CS": 4, "VC": 3}, None),
]
EVID = {  # per row, per vendor: short evidence with source (demo / RFP)
 "Decision-making": {
  "AR": "Scorecard: Runs it. Ranks with a time, writes back; co-pilot approval to start (demo); full-time assignment can skip it.",
  "AX": "Scorecard: Recommends it. Clinician, day and time with every factor (demo). Can run alone; every customer keeps a person (RFP).",
  "CS": "Scorecard: Checks it. Filters and shows; the scheduler decides (demo). Recommendation engine, then agentic AI, on roadmap.",
  "VC": "Scorecard: Recommends it. Top four per discipline, better-day flags; scheduler approves (demo, RFP)."},
 "Automation": {
  "AR": "Texts patients and clinicians, re-staffs call-outs, writes to HCHB; office sees exceptions (demo).",
  "AX": "Bulk-plots the episode, call-out flow in seconds; person approves (demo). Write-back switched off.",
  "CS": "Staffing requests go out to priority groups automatically; each assignment is manual (demo, RFP).",
  "VC": "RPA writes approved assignments to HCHB (demo). Call-Off Center triage in development (RFP)."},
 "Engagement": {
  "AR": "Two-way text live: discharge check, preferences, arrival time (demo). Voice and Spanish claimed.",
  "AX": "Arrival-window text; replies go to the clinician (demo). RFP: voice, text, email, person in loop advised.",
  "CS": "Click-to-call with a call log (demo). Text confirmation on roadmap (RFP).",
  "VC": "No patient messaging, no date (demo, RFP). Clinician app for routing."},
 "Data visuals": {
  "AR": "Worklist, route map, agent-health insights (demo). Rich maps and calendars deprioritized by design (RFP).",
  "AX": "Capacity forecast by zip, utilization and productivity analytics (demo).",
  "CS": "Points grid by clinician and day, territory polygons, maps (demo). No branch total.",
  "VC": "Live map, route-adherence review, predictive benchmark (demo)."},
 "Learning": {
  "AR": "A typed rejection becomes a rule or weighting; rejection reports (demo). Rule view being built.",
  "AX": "Logic set from a survey of our rules (demo). Learning from overrides not described.",
  "CS": "Replies and reads are logged as data (demo). No model learns from them.",
  "VC": "Call: override reason trains the model. RFP: clinician disagreement does not retrain it."},
 "Fit: enterprise and branch": {
  "AR": "Org rules inherited and overridden per branch; we set hard vs soft rules; autonomy by branch, visit type (demo, RFP).",
  "AX": "Our logic captured by survey; permissions and accept/decline rules by role (demo, RFP).",
  "CS": "Self-service properties, priority groups, territories, sub-organizations (demo). Governance is on us.",
  "VC": "Rules per branch and discipline, then per person (demo)."},
}
e = html.escape
W = 980; LW = 190; X0 = LW + 10; CW = (W - X0 - 10) / 5; RH = 50; TOP = 4
H = TOP + RH * len(ROWS) + 4
s = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Sophistication spectrum: six rows, five levels each, four vendors placed on each row" xmlns="http://www.w3.org/2000/svg">']
for r, (name, sub, levels, pos, bnd) in enumerate(ROWS):
    y = TOP + r * RH
    if r % 2 == 0:
        s.append(f'<rect x="0" y="{y}" width="{W}" height="{RH}" fill="#F4F5F7"/>')
    s.append(f'<text x="6" y="{y+20}" font-size="12" font-weight="700" fill="#1F3864">{e(name)}</text>')
    s.append(f'<text x="6" y="{y+35}" font-size="10" fill="#444">{e(sub)}</text>')
    for i, lv in enumerate(levels):
        x = X0 + i * CW
        s.append(f'<line x1="{x}" y1="{y+4}" x2="{x}" y2="{y+RH-4}" stroke="#D0D3D9" stroke-width="1"/>')
        words, l1, l2 = lv.split(), "", ""
        for w_ in words:
            if not l2 and len(l1 + " " + w_) <= 26: l1 = (l1 + " " + w_).strip()
            else: l2 = (l2 + " " + w_).strip()
        s.append(f'<text x="{x+4}" y="{y+12}" font-size="8.4" fill="#555">{i+1} · {e(l1)}</text>')
        if l2: s.append(f'<text x="{x+13}" y="{y+22}" font-size="8.4" fill="#555">{e(l2)}</text>')
    s.append(f'<line x1="{X0+5*CW}" y1="{y+4}" x2="{X0+5*CW}" y2="{y+RH-4}" stroke="#D0D3D9" stroke-width="1"/>')
    if bnd:
        bx = X0 + bnd * CW
        s.append(f'<line x1="{bx}" y1="{y+2}" x2="{bx}" y2="{y+RH-2}" stroke="#A3321E" stroke-width="1.6" stroke-dasharray="4 3"/>')
    # markers
    by_level = {}
    for ab, lv in pos.items(): by_level.setdefault(lv, []).append(ab)
    for lv, abs_ in by_level.items():
        for k, ab in enumerate(sorted(abs_)):
            _, _, fill, tc = next(v for v in V if v[1] == ab)
            mx = X0 + (lv - 1) * CW + 8 + k * 40
            s.append(f'<rect x="{mx}" y="{y+26}" width="36" height="20" rx="4" fill="{fill}" stroke="#fff" stroke-width="2"/>')
            s.append(f'<text x="{mx+18}" y="{y+40}" font-size="10.5" font-weight="700" text-anchor="middle" fill="{tc}">{ab}</text>')
s.append('</svg>')
svg = "\n".join(s)
legend = " ".join(f'<span class="lg"><i style="background:{c}"></i><b>{ab}</b> {e(n)}</span>' for n, ab, c, _ in V)
rows_html = []
for name, *_ in ROWS:
    cells = "".join(f"<td>{e(EVID[name][ab])}</td>" for _, ab, _, _ in V)
    rows_html.append(f'<tr><td class="lab">{e(name)}</td>{cells}</tr>')
pos_rows = []
for name, _, levels, pos, _ in ROWS:
    pos_rows.append("<tr><td class='lab'>" + e(name) + "</td>" + "".join(f"<td class='c'>{pos[ab]}</td>" for _, ab, _, _ in V) + "</tr>")
doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Vendor Product Sophistication</title>
<style>
@page{{size:11in 8.5in;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:"Liberation Sans",Arial,Helvetica,sans-serif;color:#000;font-size:6.8pt;line-height:1.16}}
.page{{width:11in;height:8.5in;padding:.3in .36in .2in;overflow:hidden}}
.hdr{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #1F3864;padding-bottom:4px;margin-bottom:6px}}
.hdr h1{{font-size:14pt;color:#1F3864}}
.hdr p{{font-size:8pt}}
.hdr .r{{text-align:right;font-size:7.6pt;color:#444}}
h2{{font-size:8.6pt;color:#1F3864;margin:4px 0 2px}}
.lgd{{display:flex;flex-wrap:wrap;gap:16px;align-items:center;margin:2px 0 4px;font-size:8pt}}
.lg{{display:inline-flex;align-items:center;gap:5px}}
.lg i{{width:14px;height:10px;border-radius:2px;display:inline-block}}
.bd{{display:inline-flex;align-items:center;gap:5px;color:#A3321E}}
.bd i{{width:18px;border-top:1.6px dashed #A3321E;display:inline-block}}
table{{border-collapse:collapse;width:100%;table-layout:fixed}}
th,td{{border:1px solid #A6A6A6;padding:1.5px 3.5px;vertical-align:top;text-align:left}}
th{{background:#D9E1F2}}
td.lab{{font-weight:bold;background:#F2F2F2}}
td.c,th.c{{text-align:center}}
.note{{font-size:6.8pt;color:#333;margin-top:4px}}
.two{{display:grid;grid-template-columns:1fr 3.2in;gap:12px;margin-top:4px}}
ul{{padding-left:12px}} li{{margin-bottom:2px}}
</style></head><body><div class="page">
<div class="hdr"><div><h1>Product Sophistication: Where Each Vendor Sits</h1>
<p>Six components of sophistication, each on a five-step scale. Positions are our read of the demo calls and each vendor's RFP return. Vendors in alphabetical order.</p></div>
<div class="r">Compassus Home Health<br>Internal, for discussion</div></div>
<div class="lgd">{legend}<span class="bd"><i></i>Compassus Assist boundary for assignment and coverage (acts, with approval)</span></div>
{svg}
<div class="two">
<div>
<h2>What puts each vendor where it is</h2>
<table><colgroup><col style="width:12%"><col><col><col><col></colgroup>
<tr><th></th>{"".join(f"<th>{e(n)}</th>" for n,_,_,_ in V)}</tr>
{"".join(rows_html)}
</table>
</div>
<div>
<h2>Positions (1-5)</h2>
<table><colgroup><col style="width:40%"><col><col><col><col></colgroup>
<tr><th></th>{"".join(f"<th class='c'>{ab}</th>" for _,ab,_,_ in V)}</tr>
{"".join(pos_rows)}
</table>
<h2>How to read it</h2>
<ul>
<li><b>Further right is more capable, not automatically a better fit.</b> For assignment and coverage, Compassus has set an Assist boundary: the system acts with approval. Past it, a product must let us keep approval switched on.</li>
<li><b>The components pull in different directions.</b> Among these four, the product that automates most shows least on screen, and the two that show most leave more of the approvals to people.</li>
<li><b>Learning and fit decide how well it serves 80+ branches.</b> Branch-level rules and learning from feedback need someone at Compassus to own and review them.</li>
<li>Decision-making mirrors the formal scorecard's sophistication mark. The other five rows are our read and are not part of the formal score.</li>
</ul>
</div></div>
<p class="note">Sources: demo calls on 22, 23, 24 and 28 Sep 2026, and the vendors' RFP returns (scorecard workbook 9.11.26). "Demo" means seen on the call; "RFP" means described in the return, not demonstrated. Claims not shown on a call are placed where the vendor says they sit and flagged in the evidence. This page compares; it does not rank or recommend.</p>
</div></body></html>'''
OUT.write_text(doc)
print("wrote", OUT)
