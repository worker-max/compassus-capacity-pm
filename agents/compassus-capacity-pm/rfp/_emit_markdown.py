# -*- coding: utf-8 -*-
"""Emit the vendor-facing questionnaire markdown from _content.py — single source of truth."""
import _content as c

L = []
L.append("# Capacity & Scheduling Platform — Vendor Questionnaire")
L.append("")
L.append("**Compassus Home Health**")
L.append("")
L.append("---")
L.append("")

def block(sections, part_b_after="A"):
    for key, title, framing, qs in sections:
        L.append(f"## Part {key} — {title}")
        L.append("")
        if framing:
            L.append(framing)
            L.append("")
        for qid, label, text in qs:
            L.append(f"**{qid}. {label}.**")
            L.append(text)
            L.append("")
        if key == part_b_after:
            L.append("---")
            L.append("")
            L.append("## Part B — Coverage self-assessment")
            L.append("")
            L.append("Mark where you stand on each area. Options: **Production** · "
                     "**In development** · **Roadmap** · **Not offered**.")
            L.append("")
            L.append("| # | Area | | Status | Notes |")
            L.append("|---|---|---|---|---|")
            n = 0
            for mod, rows in c.COVERAGE_STANDARD:
                L.append(f"| | **{mod}** | | | |")
                for name, desc in rows:
                    n += 1
                    L.append(f"| {n} | {name} | {desc} | | |")
            L.append("")
        L.append("---")
        L.append("")

block(c.SECTIONS)
while L and L[-1] in ("", "---"):
    L.pop()
L.append("")
open("vendor-questionnaire.md", "w", encoding="utf-8").write("\n".join(L))
print("wrote vendor-questionnaire.md")
