#!/usr/bin/env python3
"""
Compassus vendor scorecard — the scoring engine.

One implementation of the rubric in `vendor-evaluation/scoring-guide.md`. Everything else
(the skill, the workbook, the one-pager) reads its numbers from here so they cannot drift.

    python3 score.py assess/acme.json                    # validate + print the scorecard
    python3 score.py assess/acme.json -o Acme-Scorecard.md
    python3 score.py assess/*.json --roster roster.md    # comparison table across vendors

Every part is a percentage times the points it is worth. Part 1 is the one exception:
a checkbox ladder.
"""

import argparse
import json
import os
import sys
from datetime import date
from decimal import ROUND_HALF_UP, Decimal

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_PATH = os.path.join(HERE, "spec-elements.json")

# ─── the rubric, as constants ────────────────────────────────────────────────

POINTS = {"hchb": 25, "footprint": 30, "sophistication": 20, "clinician": 10, "partnership": 15}
ARENA_POINTS = 10  # each of the three arenas, inside the footprint's 30

HCHB_RUNGS = {
    25: "Live, bi-directional, multi-customer",
    20: "Live, single customer or one-way",
    12: "Live via a partner or a brittle method",
    6: "In development, dated",
    2: "Roadmap, undated",
    0: "None, and no path",
}
HCHB_FLOOR = 12  # below this → Conditional band regardless of total

MARKS = {"covered": 1.0, "partial": 0.5, "none": 0.0}

# Sophistication is scored on how much the product actually DOES — not on how thoroughly the
# vendor narrated it. A short answer describing an optimizer still scores 4. This is the
# Read / Assist / Control language already in the primary workbook, extended to five rungs.
CAPABILITY = {
    0: "Not addressed",
    1: "Shows it",
    2: "Checks it",
    3: "Recommends it",
    4: "Runs it",
}

# Clinician fit and partnership are not capability questions — they are fit questions.
FIT = {
    0: "Not addressed",
    1: "Poor fit",
    2: "Workable",
    3: "Good fit",
    4: "Strong fit, proven elsewhere",
}

LADDER = CAPABILITY  # back-compat for anything reading the old name

SOPH_ITEMS = {
    "S1": ("Capacity", "C1"),
    "S2": ("Assignment", "C2"),
    "S3": ("The week", "C4"),
    "S4": ("Readiness", "C3"),
    "S5": ("Recovery", "C5"),
}
CLIN_ITEMS = {
    "D1": ("What the clinician decides", "D1"),
    "D2": ("Decide or advise", "D2"),
    "D3": ("Adoption evidence", "D3"),
}
PART_ITEMS = {
    "P1": ("Sharing in the value", "E2"),
    "P2": ("Deployment & change management", "E3"),
    "P3": ("What we did not ask", "E1"),
    "P4": ("What they chose not to build", "E4"),
}

BANDS = [(80, "Advance"), (65, "Consider"), (50, "Hold"), (0, "Decline")]


def r1(x):
    """Round half-up to one decimal — what the spreadsheet displays, not banker's rounding."""
    return float(Decimal(str(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


# ─── spec ────────────────────────────────────────────────────────────────────

def load_spec(path=SPEC_PATH):
    with open(path) as fh:
        return json.load(fh)


def spec_index(spec):
    """{element_id: (arena_id, arena_name, group_name, text)} in sheet order."""
    idx = {}
    for arena in spec["arenas"]:
        for group in arena["groups"]:
            for el in group["elements"]:
                idx[el["id"]] = (arena["id"], arena["name"], group["name"], el["text"])
    return idx


# ─── scoring ─────────────────────────────────────────────────────────────────

def _ladder_part(block, items, worth, label, scale=CAPABILITY):
    """(sum ÷ max) × the points this part is worth. Missing item = 0, and it is reported."""
    rows, total, missing = [], 0, []
    for key, (name, source) in items.items():
        entry = block.get(key) or {}
        raw = entry.get("score")
        if raw is None:
            raw, missing = 0, missing + [key]
        raw = int(raw)
        if not 0 <= raw <= 4:
            raise ValueError(f"{label} {key}: score {raw} is outside the 0–4 ladder")
        total += raw
        rows.append({
            "key": key, "name": name, "source": source, "score": raw,
            "rung": scale[raw], "cite": entry.get("cite", ""), "note": entry.get("note", ""),
        })
    ceiling = len(items) * 4
    exact = total / ceiling * worth
    return {
        "rows": rows, "raw": total, "ceiling": ceiling,
        "pct": total / ceiling, "points": r1(exact), "points_exact": exact,
        "budget": worth, "missing": missing,
    }


def score_footprint(assessment, spec):
    idx = spec_index(spec)
    marks = assessment.get("footprint", {})
    unknown = [k for k in marks if k not in idx]
    if unknown:
        raise ValueError(f"footprint has unknown element ids: {', '.join(sorted(unknown))}")

    arenas, elements = {}, []
    for arena in spec["arenas"]:
        arenas[arena["id"]] = {
            "id": arena["id"], "name": arena["name"], "kicker": arena["kicker"],
            "value": 0.0, "count": 0, "covered": 0, "partial": 0, "none": 0,
        }
    for eid, (aid, aname, gname, text) in idx.items():
        entry = marks.get(eid) or {}
        mark = (entry.get("mark") or "none").lower()
        if mark not in MARKS:
            raise ValueError(f"{eid}: mark '{mark}' is not covered / partial / none")
        cite = (entry.get("cite") or "").strip()
        # A vendor's own Section B answer is enough to mark Covered. We do not demote a claim
        # for lacking elaboration — the questionnaire did not give room for it, and "how does
        # that work?" is a demo question, not a scoring penalty. Section C only ever overrides
        # when it contradicts Section B, and that is a judgement the scorer makes directly.
        demoted = False
        a = arenas[aid]
        a["value"] += MARKS[mark]
        a["count"] += 1
        a[mark if mark != "none" else "none"] += 1
        elements.append({
            "id": eid, "arena": aid, "group": gname, "text": text, "mark": mark,
            "cite": cite, "quote": entry.get("quote", ""), "demoted": demoted,
        })

    for a in arenas.values():
        a["pct"] = a["value"] / a["count"] if a["count"] else 0.0
        a["points_exact"] = a["pct"] * ARENA_POINTS
        a["points"] = r1(a["points_exact"])

    total_value = sum(a["value"] for a in arenas.values())
    total_count = sum(a["count"] for a in arenas.values())
    return {
        "arenas": list(arenas.values()), "elements": elements,
        "value": total_value, "count": total_count,
        "pct": total_value / total_count if total_count else 0.0,
        "points": r1(sum(a["points_exact"] for a in arenas.values())),
        "points_exact": sum(a["points_exact"] for a in arenas.values()),
        "budget": POINTS["footprint"],
    }


def score(assessment, spec=None):
    spec = spec or load_spec()

    hchb = assessment.get("hchb") or {}
    rung = hchb.get("rung")
    if rung is None:
        raise ValueError("hchb.rung is required — tick a rung from the A1 ladder")
    rung = int(rung)
    if rung not in HCHB_RUNGS:
        raise ValueError(f"hchb.rung {rung} is not a rung: {sorted(HCHB_RUNGS)}")

    fp = score_footprint(assessment, spec)
    soph = _ladder_part(assessment.get("sophistication", {}), SOPH_ITEMS,
                        POINTS["sophistication"], "sophistication")
    clin = _ladder_part(assessment.get("clinician", {}), CLIN_ITEMS,
                        POINTS["clinician"], "clinician", FIT)
    part = _ladder_part(assessment.get("partnership", {}), PART_ITEMS,
                        POINTS["partnership"], "partnership", FIT)

    # Sum unrounded, round once — so the engine and the workbook cannot disagree.
    total = r1(rung + fp["points_exact"] + soph["points_exact"]
               + clin["points_exact"] + part["points_exact"])
    band = next(name for floor, name in BANDS if total >= floor)
    conditional = rung < HCHB_FLOOR

    return {
        "vendor": assessment.get("vendor", "Unnamed vendor"),
        "scored_on": assessment.get("scored_on") or date.today().isoformat(),
        "scored_by": assessment.get("scored_by", ""),
        "completed_by": assessment.get("completed_by", ""),
        "summary": assessment.get("summary", ""),
        "hchb": {
            "points": rung, "budget": POINTS["hchb"], "rung": HCHB_RUNGS[rung],
            "cite": hchb.get("cite", "A1"), "note": hchb.get("note", ""),
        },
        "footprint": fp, "sophistication": soph, "clinician": clin, "partnership": part,
        "total": total, "band": band, "conditional": conditional,
        "band_label": f"Conditional — {band}" if conditional else band,
        "differentiators": assessment.get("differentiators", []),
        "flags": assessment.get("flags", []),
        "unknowns": assessment.get("unknowns", []),
    }


# ─── rendering ───────────────────────────────────────────────────────────────

def _pct(x):
    return f"{round(x * 100)}%"


def _bar(pct, width=20):
    filled = round(pct * width)
    return "█" * filled + "·" * (width - filled)


def render(s):
    L = []
    add = L.append
    add(f"# {s['vendor']} — Vendor Scorecard")
    add("")
    add(f"**{s['total']} / 100 · {s['band_label']}**")
    if s["conditional"]:
        add("")
        add("> **Conditional.** HCHB integration scored below the floor of "
            f"{HCHB_FLOOR}/25. Advancing means explicitly accepting an integration to be "
            "built, on their timeline, at our risk.")
    add("")
    if s["summary"]:
        add(s["summary"])
        add("")

    add("| Part | Score | Out of | |")
    add("|---|---:|---:|---|")
    for key, label in [("hchb", "1 · HCHB Integration"), ("footprint", "2 · Scope Footprint"),
                       ("sophistication", "3 · Sophistication"), ("clinician", "4 · Clinician & Adoption"),
                       ("partnership", "5 · Partnership")]:
        p, b = s[key]["points"], s[key]["budget"]
        add(f"| {label} | **{p}** | {b} | `{_bar(p / b if b else 0)}` |")
    add(f"| **Total** | **{s['total']}** | **100** | |")
    add("")

    add("## Footprint against the Compassus spec")
    add("")
    add(f"**Overall — {_pct(s['footprint']['pct'])}** "
        f"({s['footprint']['value']:g} of {s['footprint']['count']} elements)")
    add("")
    add("| Arena | Footprint | Covered | Partial | Not covered | Points |")
    add("|---|---:|---:|---:|---:|---:|")
    for a in s["footprint"]["arenas"]:
        add(f"| {a['name']} | **{_pct(a['pct'])}** | {a['covered']} | {a['partial']} | "
            f"{a['none']} | {a['points']} / {ARENA_POINTS} |")
    add("")

    add("### Element detail")
    add("")
    sym = {"covered": "●", "partial": "◐", "none": "○"}
    current = None
    for el in s["footprint"]["elements"]:
        if el["group"] != current:
            current = el["group"]
            add("")
            add(f"**{current}**")
            add("")
            add("| | Element | Evidence |")
            add("|---|---|---|")
        note = el["cite"]
        if el["quote"]:
            note = f"{note} — *{el['quote']}*" if note else f"*{el['quote']}*"
        add(f"| {sym[el['mark']]} | **{el['id']}** {el['text']} | {note or '—'} |")
    add("")

    for key, title, scale in [("sophistication", "Sophistication", "Does"),
                              ("clinician", "Clinician & Adoption", "Fit"),
                              ("partnership", "Partnership", "Fit")]:
        blk = s[key]
        add(f"## {title} — {blk['points']} / {blk['budget']}")
        add("")
        add(f"| | Item | {scale} | Source | Reading |")
        add("|---|---|---|---|---|")
        for r in blk["rows"]:
            add(f"| {r['score']} | **{r['name']}** | {r['rung']} | {r['cite'] or r['source']} | "
                f"{r['note'] or '—'} |")
        add("")

    add("## ⭐ Differentiators")
    add("")
    add("\n".join(f"- {d}" for d in s["differentiators"]) or "*None identified.*")
    add("")
    add("## 🚩 Flags")
    add("")
    if s["flags"]:
        for f in s["flags"]:
            level = (f.get("level") if isinstance(f, dict) else "yellow") or "yellow"
            text = f.get("text") if isinstance(f, dict) else str(f)
            add(f"- {'🔴' if level.startswith('r') else '🟡'} {text}")
    else:
        add("*None raised.*")
    add("")
    add("## ❓ Unknowns — the demo agenda")
    add("")
    add("\n".join(f"- {u}" for u in s["unknowns"]) or "*Nothing left unanswered.*")
    add("")
    add("---")
    add("")
    meta = [f"Scored {s['scored_on']}"]
    if s["scored_by"]:
        meta.append(f"by {s['scored_by']}")
    if s["completed_by"]:
        meta.append(f"questionnaire completed by {s['completed_by']}")
    add(f"*{' · '.join(meta)} · rubric v1.0 · 41 spec elements, form_version 2026-08-19.*")
    return "\n".join(L)


def render_roster(scored):
    ranked = sorted(scored, key=lambda s: (-s["total"], -s["hchb"]["points"]))
    L = ["# Vendor comparison", "",
         "| # | Vendor | Total | Band | HCHB | Footprint | Cap | Sch | Eng | Soph | Clin | Ptnr | 🔴 |",
         "|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for i, s in enumerate(ranked, 1):
        a = {x["id"]: x for x in s["footprint"]["arenas"]}
        reds = sum(1 for f in s["flags"]
                   if isinstance(f, dict) and str(f.get("level", "")).startswith("r"))
        L.append(
            f"| {i} | **{s['vendor']}** | **{s['total']}** | {s['band_label']} | "
            f"{s['hchb']['points']} | {_pct(s['footprint']['pct'])} | "
            f"{_pct(a['CAP']['pct'])} | {_pct(a['SCH']['pct'])} | {_pct(a['ENG']['pct'])} | "
            f"{s['sophistication']['points']} | {s['clinician']['points']} | "
            f"{s['partnership']['points']} | {reds or '—'} |")
    L += ["", "*Ranked on total, ties broken on HCHB. Rubric v1.0.*"]
    return "\n".join(L)


# ─── cli ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Score a Compassus vendor questionnaire assessment.")
    ap.add_argument("assessment", nargs="+", help="assessment JSON file(s)")
    ap.add_argument("-o", "--out", help="write the scorecard markdown here (single input only)")
    ap.add_argument("--roster", help="write a comparison table across all inputs here")
    ap.add_argument("--json", action="store_true", help="emit computed scores as JSON")
    args = ap.parse_args()

    spec = load_spec()
    scored = []
    for path in args.assessment:
        with open(path) as fh:
            try:
                scored.append(score(json.load(fh), spec))
            except ValueError as exc:
                sys.exit(f"{path}: {exc}")

    if args.json:
        print(json.dumps(scored if len(scored) > 1 else scored[0], indent=2))
    elif len(scored) == 1:
        md = render(scored[0])
        if args.out:
            with open(args.out, "w") as fh:
                fh.write(md + "\n")
            print(f"wrote {args.out}  —  {scored[0]['vendor']}: "
                  f"{scored[0]['total']}/100 ({scored[0]['band_label']})")
        else:
            print(md)
    else:
        for s in scored:
            print(f"{s['vendor']:<28} {s['total']:>5} / 100   {s['band_label']}")

    if args.roster:
        with open(args.roster, "w") as fh:
            fh.write(render_roster(scored) + "\n")
        print(f"wrote {args.roster}  —  {len(scored)} vendors")


if __name__ == "__main__":
    main()
