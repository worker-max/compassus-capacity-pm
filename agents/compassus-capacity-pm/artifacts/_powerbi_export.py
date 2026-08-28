# -*- coding: utf-8 -*-
"""_powerbi_export — emit the Power BI star schema for every flow that has a vmap.

    python3 _powerbi_export.py

Writes powerbi/variables.csv, powerbi/blocks.csv, powerbi/block_variables.csv and one
background PNG per flow per state. Re-run after editing a vmap or re-importing the workbook.

blocks.csv carries each block's geometry as a percentage of the drawing canvas AND its posture
under all three states, so one Power BI page can slice between Dashboard, MVP and Target State
without swapping the background image.
"""
import csv
import io
import contextlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import _flow_live as L
import _flow_vis as VIS

FLOWS = {
    "soc":     ("_flow-detailed-composite.gen.py", "vmap-soc.json",            "SOC / ROC"),
    "episode": ("_flow-primary-map.gen.py",        "vmap-episode.json",        "Full Episode"),
    "dcs":     ("_flow-dcs-scheduler.gen.py",      "vmap-dcs-scheduler.json",  "DCS / Scheduler"),
    "routine": ("_flow-routine-visits.gen.py",     "vmap-routine-visits.json", "Routine Visits"),
}

V = json.loads((HERE / "variables.json").read_text())
OUT = HERE / "powerbi"
OUT.mkdir(exist_ok=True)

VCOLS = ["variable", "arena", "group", "plain", "does", "decides_now", "lives", "confidence",
         "role", "decides", "trigger", "mvp", "gating", "adoption", "why", "open"]
VHEAD = ["Id", "Variable", "Arena", "Group", "In plain terms", "Who does it today",
         "Who decides today", "Where it lives today", "Confidence", "Future role",
         "Future decider", "Trigger", "MVP", "Gating", "Adoption sensitivity",
         "Why this posture", "Open question"]

with open(OUT / "variables.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f); w.writerow(VHEAD)
    for k in sorted(V):
        w.writerow([k] + [V[k].get(c, "") for c in VCOLS])

blocks, bridge = [], []
for flow, (gen, mapfile, nice) in FLOWS.items():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        svg, rec, W, H = L.run(gen)
    seen, uniq = set(), []
    for r in rec:
        if r[:4] in seen:
            continue
        seen.add(r[:4]); uniq.append(r)
    vmap = json.loads((HERE / mapfile).read_text())
    gone = VIS.REMOVED.get(flow, {})
    for x, y, w_, h, lines, kind in uniq:
        if not lines:
            continue
        key = L.key_of(lines)
        ids = vmap.get(key)
        if ids is None:
            continue
        removed = key in gone
        full = VIS.scope(ids, V, mvp_only=False) if ids else None
        mvp = VIS.scope(ids, V, mvp_only=True) if ids else None
        blocks.append(dict(
            Flow=nice, Block=key,
            Dashboard="Removed" if removed else ("View" if ids else "Not mapped"),
            MVP="Removed" if removed else (mvp or "View"),
            Target="Removed" if removed else (full or "Not mapped"),
            Variables=len(ids),
            X=round((x + w_ / 2) / W * 100, 3), Y=round(100 - (y + h / 2) / H * 100, 3),
            BubbleSize=round(w_ * h / (W * H) * 10000, 2),
            LeftPct=round(100 * x / W, 3), TopPct=round(100 * y / H, 3),
            WidthPct=round(100 * w_ / W, 3), HeightPct=round(100 * h / H, 3),
            CanvasW=W, CanvasH=H))
        for i in ids:
            bridge.append(dict(Flow=nice, Block=key, Id=i))

for name, rows in [("blocks.csv", blocks), ("block_variables.csv", bridge)]:
    with open(OUT / name, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"{name:22} {len(rows):4} rows")
print(f"{'variables.csv':22} {len(V):4} rows")
print("flows:", ", ".join(sorted({b['Flow'] for b in blocks})))
