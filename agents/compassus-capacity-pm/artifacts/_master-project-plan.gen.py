#!/usr/bin/env python3
"""
Build `Capacity-Scheduling-Master-Project-Plan.xlsx` from the team's base workbook.

The base (`base/First-Attempt-Master-Project-Plan.xlsx`) is the version the team already
has. This script rewrites the narrative tabs, adds the vendor-selection, rubric,
governance, house-format plan and reusable-framework tabs, and leaves every inherited
tab untouched.

    python3 _master-project-plan.gen.py

House design system (inherited from the base workbook, do not drift):
    NAVY  1F3864   titles, header rows
    MID   2E5C8A   band rows
    PALE  F2F5FA   body fill
    BAND  D9E2F3   callout fill
    GREY  5A6570   subtitles
    RED   9C2B2B   Open Items
"""

import math
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

HERE = Path(__file__).resolve().parent
BASE = HERE / "base" / "First-Attempt-Master-Project-Plan.xlsx"
OUT = HERE / "Capacity-Scheduling-Master-Project-Plan.xlsx"

NAVY, MID, PALE, BAND, GREY = "1F3864", "2E5C8A", "F2F5FA", "D9E2F3", "5A6570"
RED, REDPALE, GREEN, WHITE = "9C2B2B", "FDF3F3", "1F6F5C", "FFFFFF"
EDIT, EDITBORDER = "FFF9E6", "C9A227"

THIN = Side(style="thin", color="D5DCE7")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def fill(hexcolor):
    return PatternFill("solid", start_color=hexcolor, end_color=hexcolor)


def _wrapped_lines(text, width_chars):
    total = 0
    for segment in str(text).split("\n"):
        total += max(1, math.ceil(len(segment) / max(width_chars, 1)))
    return total


def autofit_rows(ws, first, last, only_grow=True, pad=6.0, line=12.6):
    """Set each row tall enough for its longest wrapped cell. Never shrinks by default."""
    merged_starts = {m.min_row for m in ws.merged_cells.ranges if m.max_col > m.min_col}
    for row in range(first, last + 1):
        if row in merged_starts:
            continue
        needed = 0.0
        for col in range(1, ws.max_column + 1):
            cell = ws.cell(row=row, column=col)
            if cell.value is None or not isinstance(cell.value, str):
                continue
            if cell.value.startswith("="):
                continue
            width = (ws.column_dimensions[get_column_letter(col)].width or 8.43) * 1.05
            needed = max(needed, _wrapped_lines(cell.value, width) * line + pad)
        if needed:
            current = ws.row_dimensions[row].height or 0
            ws.row_dimensions[row].height = max(current, needed) if only_grow else needed


def title_block(ws, title, subtitle, span, accent=NAVY):
    """The house title + deck: row 1 big accent-coloured, row 2 grey deck, row 3 blank."""
    ws.sheet_view.showGridLines = False
    ws["A1"] = title
    ws["A1"].font = Font(name="Calibri", size=16, bold=True, color=accent)
    ws.merge_cells(f"A1:{span}1")
    ws.row_dimensions[1].height = 26.1

    ws["A2"] = subtitle
    ws["A2"].font = Font(name="Calibri", size=10, color=GREY)
    ws["A2"].alignment = Alignment(vertical="center", wrap_text=True)
    ws.merge_cells(f"A2:{span}2")
    total = sum((ws.column_dimensions[get_column_letter(c)].width or 8.43)
                for c in range(1, ws[f"{span}1"].column + 1))
    ws.row_dimensions[2].height = max(
        32.1, _wrapped_lines(subtitle, total * 1.05) * 12.6 + 8)
    ws.row_dimensions[3].height = 6.0


def header_row(ws, row, headers, accent=NAVY, height=30.0):
    for i, text in enumerate(headers, start=1):
        c = ws.cell(row=row, column=i, value=text)
        c.font = Font(name="Calibri", size=10, bold=True, color=WHITE)
        c.fill = fill(accent)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BOX
    ws.row_dimensions[row].height = height


def band(ws, row, text, span, accent=MID, height=20.1):
    ws.cell(row=row, column=1, value=text)
    for col in range(1, span + 1):
        c = ws.cell(row=row, column=col)
        c.font = Font(name="Calibri", size=11, bold=True, color=WHITE)
        c.fill = fill(accent)
        c.alignment = Alignment(vertical="center")
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=span)
    ws.row_dimensions[row].height = height


def body_row(ws, row, values, height=None, bold_cols=(), shade=PALE,
             center_cols=(), accent_col=None, accent_fill=MID):
    for i, v in enumerate(values, start=1):
        c = ws.cell(row=row, column=i, value=v)
        c.font = Font(name="Calibri", size=10, bold=(i in bold_cols))
        if shade:
            c.fill = fill(shade)
        c.alignment = Alignment(
            vertical="top",
            horizontal="center" if i in center_cols else None,
            wrap_text=True,
        )
        c.border = BOX
    if accent_col:
        c = ws.cell(row=row, column=accent_col)
        c.font = Font(name="Calibri", size=12, bold=True, color=WHITE)
        c.fill = fill(accent_fill)
        c.alignment = Alignment(horizontal="center", vertical="center")
    if height:
        ws.row_dimensions[row].height = height


def callout(ws, row, heading, lines, span, accent=MID, tint=BAND):
    """A closing panel: a coloured strip, then pale paragraphs."""
    band(ws, row, heading, span, accent=accent, height=19.5)
    r = row + 1
    for text in lines:
        ws.cell(row=r, column=1, value=text)
        for col in range(1, span + 1):
            c = ws.cell(row=r, column=col)
            c.font = Font(name="Calibri", size=10)
            c.fill = fill(tint)
            c.alignment = Alignment(vertical="center", wrap_text=True)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=span)
        ws.row_dimensions[r].height = 30.0
        r += 1
    return r


def widths(ws, spec):
    for col, w in spec.items():
        ws.column_dimensions[col].width = w


def tab_colour(ws, hexcolor):
    ws.sheet_properties.tabColor = hexcolor


def print_setup(ws, last_col):
    """Landscape, fit to one page wide, header row repeated. These tabs get printed."""
    ws.page_setup.orientation = "landscape"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_title_rows = "1:4"
    ws.print_area = f"A1:{last_col}{ws.max_row}"
    ws.page_margins.left = ws.page_margins.right = 0.3
    ws.page_margins.top = ws.page_margins.bottom = 0.4


# ══════════════════════════════════════════════════════════════════════════════
# 1. Approach — 10 Steps  (refresh the framing; the ten steps themselves stand)
# ══════════════════════════════════════════════════════════════════════════════

def refresh_approach(wb):
    ws = wb["Approach — 10 Steps"]
    # Column E ("What came out of it") shipped at 13 characters wide carrying 130–210
    # characters of text — it was clipped. Rebalance, then refit every step row.
    widths(ws, {"A": 6.0, "B": 26.0, "C": 30.0, "D": 50.0, "E": 44.0, "F": 8.0,
                "G": 15.0, "H": 42.0})
    ws["A1"] = ("HH Scheduling & Capacity Management  —  Arc One: How We Got This "
                "Initiative Off The Ground")
    ws["A2"] = (
        "Ten steps. Steps 1 and 10 are endpoints; steps 2–6 are a LOOP that ran three times; "
        "step 7 (business case) runs in PARALLEL from the first loop pass; step 8 feeds back "
        "into the loop because half of what it finds is a new variable.    "
        "▸ Arc Two — choosing a partner — is steps 11–18 on the next tab."
    )
    row = 20
    end = callout(
        ws, row,
        "WHERE THE WORK STANDS NOW",
        [
            "Arc One built the understanding: a vocabulary, a scored variable list, a "
            "current-state baseline nobody argues with, a constraint register, a business "
            "case register and an MVP scope.  It is what made a credible vendor ask possible.",
            "Arc Two is running now — the questionnaire and reference pack went out, the "
            "rubric cut the field to six, and the six are in virtual deep dives.  Three go "
            "to on-site half-days.  See ‘Vendor Selection’ and ‘Questionnaire & Rubric’.",
            "Arc Three is being seated in parallel — the Leadership Steering Committee, the "
            "primary workgroup and the SME bench.  See ‘Governance & People’.",
        ],
        8,
    )
    autofit_rows(ws, 5, 14)
    return end


# ══════════════════════════════════════════════════════════════════════════════
# 2. Vendor Selection — steps 11–18
# ══════════════════════════════════════════════════════════════════════════════

VENDOR_STAGES = [
    (
        "11",
        "Building the questionnaire",
        "What do we actually need to know about a product, and how do we ask it so two "
        "answers can be compared?",
        "Built from our own scored variable inventory, not from a template — every question "
        "traces back to a variable ID or a catalogued constraint, and a question that traced "
        "to neither was cut. Ordered so the three pillars come FIRST and commercials come "
        "LAST: a vendor reads our operating model before they read our budget. Open response "
        "with required evidence — a screenshot, the report name, the configuration path — "
        "because a yes/no field rewards the boldest writer, not the best product.",
        "The issued questionnaire, sectioned A–J · a question-to-variable trace · a single "
        "named channel for vendor clarifications, with every answer published to all "
        "recipients so no vendor gets a private advantage",
        "Complete",
        "A set of responses answering the same questions, at the same depth, in the same "
        "order the rubric scores them.",
    ),
    (
        "12",
        "The reference pack",
        "How much context does a vendor need before their answer is worth reading?",
        "A vendor answers at the level of context they are given, so we gave them ours. "
        "Three pieces, issued WITH the questionnaire rather than on request: the one-pager "
        "(the three pillars and the primary variables under each), the full variable "
        "reference (every variable per pillar, one page each), and the current-state flow "
        "map. Publishing the map was a deliberate call — it exposes our constraints, and it "
        "is exactly what lets a vendor say ‘your step 4 is our step 7’ instead of pitching.",
        "Capacity · Scheduling · Engagement one-pager (1 page) · variable reference (3 pages) "
        "· primary current-state flow map · detailed composite flow sheet on request",
        "Complete",
        "Responses written against our process rather than against a generic home health "
        "agency — and a shared vocabulary for the deep dives that follow.",
    ),
    (
        "13",
        "Constructing the rubric",
        "How do we score this so the result is reproducible by someone who wasn’t in the "
        "room?",
        "Built BEFORE a single response was opened — a rubric written after you have read "
        "the answers is a justification, not an instrument. Its section order is IDENTICAL "
        "to the questionnaire’s, so a scorer reads a response top to bottom and scores it "
        "without hunting. Section weights were DERIVED from the scored inventory — the "
        "count and weight of the gating variables that live in each section — then left "
        "editable, because the weighting is a leadership judgement and should be arguable "
        "in public. Gating variables sit OUTSIDE the weighted score as knockouts.",
        "The scoring rubric (mirrors the questionnaire section for section) · a 0–4 evidence "
        "scale · the knockout list · an editable weight table that recomputes the whole model "
        "· scorer instructions",
        "Complete",
        "A number per vendor that can be taken apart in front of a steering committee, and a "
        "weighting anyone can challenge by changing one cell.",
    ),
    (
        "14",
        "Scoring, and the cut to six",
        "Which products can actually carry this, and where does the field genuinely break?",
        "Scored independently first, then reconciled — differences between scorers were "
        "argued to a single agreed score, and the argument was recorded, because a spread "
        "between two scorers is usually a badly-worded question rather than a disagreement "
        "about the product. Knockouts applied first, on evidence, before anything was "
        "totalled. Then ranked, and the cut taken at the natural break in the scores rather "
        "than at a pre-decided headcount — six is where the field parted, not a quota.",
        "Scored response matrix, all respondents · reconciliation notes · knockout findings "
        "· the shortlist memo naming the six and the reason for each",
        "Complete",
        "Six vendors worth spending real hours on — and a written reason for every vendor "
        "not on the list.",
    ),
    (
        "15",
        "Regrets and inclusions",
        "What do we owe the vendors who answered?",
        "Every respondent gets an answer, and every declined vendor gets a reason specific "
        "enough to be useful — not ‘we went another direction’. Sent close together so no "
        "vendor learns their outcome from someone else’s announcement. The declines are "
        "written to keep the door open: several of these products may be the right answer "
        "for a later phase, and the market is small enough that how we decline is itself a "
        "reputational act.",
        "Inclusion letters to the six, with the deep-dive expectations and the date frame · "
        "regret letters to the remainder, each carrying its reason · a re-engagement note on "
        "any vendor worth revisiting for a later phase",
        "In Process",
        "A clean field, a fair process on the record, and six vendors who know exactly what "
        "they are walking into.",
    ),
    (
        "16",
        "Virtual deep dives with the six",
        "Does the product do in a live session what the response says it does on paper?",
        "Scripted, and the SAME script for all six — an unscripted demo shows you the "
        "vendor’s best three minutes, not your hardest Tuesday. Built around our own "
        "scenarios: a call-out at 7am, a pending-authorisation admission, a LUPA-risk week, "
        "a recert window colliding with a full territory. Vendors drive their own system "
        "live; no slides for the working portion. Scored on the same instrument as the "
        "questionnaire so the two scores sit side by side and any gap between what was "
        "claimed and what was shown is visible.",
        "The deep-dive script and scenario set · a per-vendor session record · deep-dive "
        "scores against the same rubric · a claimed-versus-demonstrated gap log",
        "In Process",
        "A second, independent read on each of the six — and the evidence to cut to three.",
    ),
    (
        "17",
        "The final three — on-site half-days",
        "Can we work with these people, on our data, in our building?",
        "Half a day each, on site, with the workgroup and the people who will actually use "
        "the product in the room — not a sales audience. Built to test the things a virtual "
        "session cannot: configuration against our real branch shapes, the implementation "
        "team we would actually be assigned, integration specifics with the system of "
        "record, and how the vendor behaves when told they are wrong. Reference calls run "
        "in parallel, to agencies we choose rather than the ones offered.",
        "Finalist on-site agenda (identical for all three) · a configuration exercise on our "
        "own branch shapes · named implementation team per vendor · reference call notes · "
        "the finalist scorecard",
        "Not Started",
        "A selection recommendation the steering committee can approve on the evidence, plus "
        "a defensible second choice.",
    ),
    (
        "18",
        "Selection, then contracting",
        "What exactly are we buying, and what have we agreed it must do?",
        "The acceptance tests come out of the MVP spec and the gating variables — the "
        "contract should require the product to do the things the rubric knocked vendors out "
        "for failing. Pricing negotiated against a defined scope rather than a platform "
        "licence, exit and data-portability terms settled before signature, and the pilot "
        "written in as a reversible stage with its kill criteria already committed.",
        "Selection recommendation and steering decision · scripted acceptance demonstrations "
        "· the negotiated agreement with exit and data terms · the pilot charter",
        "Not Started",
        "A signed partner, a pilot that can be stopped, and a scope somebody can be held to.",
    ),
]


def build_vendor_tab(wb, index):
    ws = wb.create_sheet("Vendor Selection", index)
    tab_colour(ws, NAVY)
    title_block(
        ws,
        "Arc Two  —  Choosing a Partner  (Steps 11–18)",
        "Arc One made the ask credible: we could not have written a useful questionnaire "
        "before we had a scored variable list, a current-state map and a constraint register. "
        "Steps 11–13 build the instruments, 14–15 make the first cut and close the loop with "
        "every respondent, 16–17 narrow six to three on evidence, 18 turns a choice into a "
        "contract.",
        "G",
    )
    widths(ws, {"A": 6.0, "B": 26.0, "C": 30.0, "D": 62.0, "E": 44.0, "F": 14.0, "G": 40.0})
    header_row(
        ws, 4,
        ["Step", "The stage", "What it answers", "How we ran it",
         "What came out of it", "Status", "What it hands forward"],
    )
    r = 5
    for stage in VENDOR_STAGES:
        body_row(ws, r, list(stage), height=132.0, center_cols=(6,),
                 accent_col=1, accent_fill=MID)
        r += 1

    r += 1
    r = callout(
        ws, r,
        "THE FOUR RULES THAT MADE THIS COMPARABLE",
        [
            "1.  The questionnaire came out of our variable list, not a template.  A question "
            "that did not trace to a variable or a constraint was cut — which is why the "
            "responses are about our problem.",
            "2.  We sent the context with the ask.  The one-pager, the full variable reference "
            "and the current-state map went out WITH the questionnaire, so vendors answered "
            "against our process instead of a generic agency.",
            "3.  The rubric was written before any response was opened, and its sections are "
            "the questionnaire’s sections in the questionnaire’s order.",
            "4.  Every stage narrows on evidence and closes its loop.  The cut fell at the "
            "break in the scores, not at a headcount — and every vendor who answered got an "
            "answer with a reason in it.",
        ],
        7,
    )
    r += 1
    callout(
        ws, r,
        "WHERE THE SIX ARE HEADED",
        [
            "Six in virtual deep dives  →  three to on-site half-days  →  one recommendation "
            "to the steering committee, with a named second choice and the evidence behind "
            "both.  The cut from six to three is made on the deep-dive scorecard plus the "
            "claimed-versus-demonstrated gap log, not on impression.",
        ],
        7,
        accent=GREEN,
        tint="E8F1EE",
    )
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# 3. Questionnaire & Rubric
# ══════════════════════════════════════════════════════════════════════════════

RUBRIC_SECTIONS = [
    ("A", "Company, viability & home health footprint",
     "Ownership, funding, client count IN HOME HEALTH specifically, agencies of our size and "
     "structure, churn, and who else runs this product on our system of record.",
     "Not a variable — a floor. A product that fits perfectly and is gone in three years costs "
     "more than one that fits well and survives.", 5,
     "—"),
    ("B", "Capacity management  ▲ pillar one",
     "The envelope: productive visit-hours by discipline by territory, netted against what is "
     "already committed. Points and productivity handling, PTO and availability, pending "
     "authorisation work, assessing capacity, open room by week.",
     "The heaviest section because the reframe put capacity in phase 1 — capacity is the thing "
     "no current system shows, and the gating variables cluster here.", 20,
     "Yes — several"),
    ("C", "Scheduling engine  ▲ pillar two",
     "Filling the envelope: assignment logic, continuity versus routing, clustering, "
     "territory, credential and discipline matching, recert/OASIS window protection, call-out "
     "and same-day recovery, on-call.",
     "The activity the organisation feels every day, and the one most likely to contain a "
     "vendor’s built-in way of working that contradicts ours — high weight, and the section "
     "carrying most of the conflict-risk scores.", 18,
     "Yes"),
    ("D", "Patient engagement  ▲ pillar three",
     "Confirmation, reminders, rebooking, the day-before negotiation, missed-visit handling "
     "and the human-script requirements some of our markets are committed to.",
     "Real weight but below the other two: it defends the schedule rather than setting it, and "
     "parts of it are ours to decide rather than the product’s to solve.", 10,
     "Yes — one"),
    ("E", "Data, integration & interoperability",
     "System-of-record integration depth, real-time versus batch, what is written back, HRIS "
     "and telephony, API surface, what breaks at a version upgrade.",
     "Weighted third overall and deliberately so. Of the catalogued constraints, the ones that "
     "cannot be toggled are largely here — this section decides what is buildable in v1 at all.",
     15, "Yes"),
    ("F", "Analytics, reporting & configurability",
     "Standard reporting, the ability to define our own measures, who can change a rule and "
     "how fast, sandbox and release process.",
     "Configurability is the hedge against every variable we have not discovered yet. Scored on "
     "who can change a rule — us, or a support ticket.", 8,
     "—"),
    ("G", "Compliance, security & regulatory fit",
     "HIPAA and security posture, PDGM and LUPA awareness, OASIS and cert-period timing, CoP "
     "obligations including missed-visit notification, state-specific patient contact rules.",
     "Scored as fit rather than as a checkbox: a product that cannot see a 30-day LUPA period "
     "or a 60-day cert window is not a home health product, whatever its certifications say.",
     8, "Yes"),
    ("H", "Implementation, support & change management",
     "Implementation method and duration, who is assigned, training approach, support model "
     "and escalation, what the agency is expected to supply.",
     "Sized against what we know about our own adoption history — the named failure mode here "
     "is a product that is configured to mirror the manual process and never actually piloted.",
     7, "—"),
    ("I", "Commercial model & total cost of ownership",
     "Pricing structure, what drives it, three-year total cost including implementation, "
     "integration and internal effort, exit and data-portability terms.",
     "Weighted honestly but last among the substantive sections — placed at the END of the "
     "questionnaire so the operating fit is answered before the price frames it.", 6,
     "—"),
    ("J", "Roadmap, partnership & references",
     "Published roadmap and what of ours is on it, influence over priorities, and references "
     "we choose rather than the ones offered.",
     "Light weight, heavy tiebreaker. It rarely moves a ranking and it frequently confirms one.",
     3, "—"),
]

SCORING_SCALE = [
    ("4", "Native, proven, at scale",
     "Does it today, out of the box, at a home health agency of our size — and showed us."),
    ("3", "Native and configurable",
     "Does it today; configuration required, and the configuration path was named."),
    ("2", "Partial, or a workaround",
     "Gets part of the way, or gets there through a manual step or a report."),
    ("1", "Roadmap only",
     "Committed on a roadmap with a date. Scored as intent, never as capability."),
    ("0", "Cannot do it",
     "No path. On a knockout item, this disqualifies regardless of total score."),
]


def build_rubric_tab(wb, index):
    ws = wb.create_sheet("Questionnaire & Rubric", index)
    tab_colour(ws, MID)
    title_block(
        ws,
        "The Questionnaire & The Rubric  —  how they were built and how the weighting works",
        "One instrument in two halves. The rubric’s sections ARE the questionnaire’s sections, "
        "in the questionnaire’s order, so a scorer reads a response top to bottom and scores it "
        "without hunting. Weights were derived from the scored variable inventory — where the "
        "gating variables live — and then deliberately left editable: change a weight in "
        "column E and the whole model recomputes in front of the room.",
        "G",
    )
    widths(ws, {"A": 5.0, "B": 34.0, "C": 56.0, "D": 56.0, "E": 12.0, "F": 11.0, "G": 14.0})
    header_row(
        ws, 4,
        ["§", "Section (questionnaire order)", "What the section asks about",
         "Why it weighs what it does", "Weight\n(editable)", "Weight %",
         "Knockouts\nin section"],
    )
    first = 5
    r = first
    for code, name, asks, why, weight, knock in RUBRIC_SECTIONS:
        body_row(ws, r, [code, name, asks, why, weight, None, knock],
                 height=86.0, bold_cols=(2,), center_cols=(1, 5, 6, 7),
                 accent_col=1, accent_fill=MID)
        r += 1
    last = r - 1

    for row in range(first, last + 1):
        wcell = ws.cell(row=row, column=5)
        wcell.fill = fill(EDIT)
        wcell.border = Border(left=Side(style="thin", color=EDITBORDER),
                              right=Side(style="thin", color=EDITBORDER),
                              top=Side(style="thin", color=EDITBORDER),
                              bottom=Side(style="thin", color=EDITBORDER))
        wcell.font = Font(name="Calibri", size=11, bold=True, color="7A5C00")
        wcell.alignment = Alignment(horizontal="center", vertical="center")
        pct = ws.cell(row=row, column=6)
        pct.value = f"=IF($E${last + 1}=0,0,E{row}/$E${last + 1})"
        pct.number_format = "0.0%"
        pct.font = Font(name="Calibri", size=11, bold=True, color=NAVY)

    total = last + 1
    body_row(ws, total, ["", "TOTAL", "", "", None, None, ""], height=22.0,
             bold_cols=(2, 5, 6), center_cols=(5, 6), shade=BAND)
    ws.cell(row=total, column=5).value = f"=SUM(E{first}:E{last})"
    ws.cell(row=total, column=6).value = f"=IF($E${total}=0,0,SUM(F{first}:F{last}))"
    ws.cell(row=total, column=6).number_format = "0.0%"
    for col in (5, 6):
        ws.cell(row=total, column=col).font = Font(name="Calibri", size=11, bold=True,
                                                  color=NAVY)
    ws.cell(row=total, column=2).alignment = Alignment(horizontal="right", vertical="center")

    r = total + 2
    r = callout(
        ws, r,
        "HOW THE WEIGHTS WERE SET  —  three rules, applied in order",
        [
            "1.  Derived, not asserted.  Each section’s starting weight came from the scored "
            "variable inventory: how many variables the section covers, how heavily they "
            "scored, and how many of them are GATING.  Capacity carries the most gating "
            "variables, so capacity carries the most weight.",
            "2.  Then adjusted for what the constraint register says we cannot change.  "
            "Integration was raised above its raw variable count because the constraints that "
            "cannot be toggled sit there — that section decides what is buildable at all, so "
            "it outranks sections with more variables and fewer immovable ones.",
            "3.  Then capped, so no section can carry the decision alone.  No section exceeds "
            "20, and the three pillars together sit just under half the total — enough to "
            "dominate a tie, not enough to let a strong scheduling demo carry a product that "
            "cannot see capacity.",
            "And then left editable.  The weights are a leadership judgement, not a finding.  "
            "Column E is unlocked and the yellow fill says so; the percentages, the totals and "
            "every vendor’s score recompute the moment a weight changes.  A committee that "
            "wants to argue the weighting should be able to argue it with the model open.",
        ],
        7,
    )

    r += 1
    band(ws, r, "THE SCORING SCALE  —  evidence, not impression", 7, accent=NAVY,
         height=19.5)
    r += 1
    header_row(ws, r, ["Score", "What it means", "The test", "", "", "", ""],
               accent=MID, height=20.0)
    ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
    r += 1
    for score, meaning, test in SCORING_SCALE:
        ws.cell(row=r, column=1, value=score)
        ws.cell(row=r, column=2, value=meaning)
        ws.cell(row=r, column=3, value=test)
        for col in range(1, 8):
            c = ws.cell(row=r, column=col)
            c.font = Font(name="Calibri", size=10, bold=(col in (1, 2)))
            c.fill = fill(PALE)
            c.alignment = Alignment(vertical="center",
                                    horizontal="center" if col == 1 else None,
                                    wrap_text=True)
            c.border = BOX
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=7)
        ws.row_dimensions[r].height = 22.0
        r += 1

    r += 1
    r = callout(
        ws, r,
        "THE KNOCKOUTS  —  scored outside the weighted total, applied first",
        [
            "A GATING variable is one the scored inventory marks as a hard or structural "
            "constraint that the MVP also requires.  A product that cannot do it is "
            "disqualified however well it scores elsewhere — which is the entire point of "
            "keeping knockouts out of the weighted total.  Averages hide a zero; a knockout "
            "cannot be averaged away.",
            "Knockouts are applied on EVIDENCE, before anything is totalled.  A ‘yes’ without "
            "a screenshot, a report name or a configuration path is scored as a 1 (roadmap), "
            "not a 3.",
            "Sections B, C, D, E and G carry knockouts.  Sections A, F, H, I and J do not — "
            "they can lower a ranking but they cannot end a candidacy.",
        ],
        7,
        accent=RED,
        tint=REDPALE,
    )

    r += 1
    callout(
        ws, r,
        "HOW THE CUT TO SIX WAS MADE",
        [
            "Knockouts first, on evidence.  Then independent scoring by more than one scorer, "
            "then reconciliation — where two scorers differed, the difference was argued to a "
            "single agreed score and the argument was written down, because a spread between "
            "scorers is usually a badly-worded question rather than a disagreement about the "
            "product.",
            "Then ranked, and the line drawn at the natural break in the scores.  Six is where "
            "the field parted.  Had the break fallen at five or at seven, that is where the "
            "cut would have been taken — the rubric sets the order, the break sets the count.",
            "What the rubric deliberately does NOT score: how much we liked the demo, how well "
            "we know the account team, and price as a proxy for quality.  Those belong in the "
            "on-site sessions and the negotiation, where they can be argued in the open.",
        ],
        7,
    )
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# 4. Governance & People
# ══════════════════════════════════════════════════════════════════════════════

STEERING_SEATS = [
    ("Executive Sponsor", "Owns the initiative’s existence, its funding and its air cover.",
     "Go / no-go at every phase gate. Kills it or backs it."),
    ("Home Health Operations Executive",
     "Owns the operating model this changes, and the regions that have to live with it.",
     "Operating-model changes; which markets pilot; what the field is asked to absorb."),
    ("Clinical / Quality Executive",
     "Guards patient safety, CoP obligations and the quality measures a capacity push could "
     "quietly damage.",
     "Veto on anything that trades quality for throughput. Owns the clinical guardrails."),
    ("Finance",
     "Owns the business case, the capital and whether the benefit converts to margin.",
     "Approves the case and the spend; rules on how benefit is counted."),
    ("Technology / IT",
     "Owns the system-of-record relationship, integration capacity and the architecture it "
     "lands in.",
     "Integration feasibility; security and architecture approval; sequencing against other "
     "IT work."),
    ("People / HR / Workforce",
     "Owns the clinician experience, pay models and the retention risk this plan must not "
     "create.",
     "Anything that touches pay, productivity expectation or the employment relationship."),
    ("Revenue Cycle & Payer Operations",
     "Owns authorisation, the payer rules and the economics of an episode.",
     "Rules on authorisation handling and anything with a reimbursement consequence."),
    ("Compliance / Legal",
     "Owns regulatory exposure, contracting and the state-specific patient contact rules.",
     "Legal sign-off on vendor terms and on any automated patient contact."),
    ("Field voice — Regional or Branch Executive Director",
     "The seat that has to make it work on a Tuesday. Without it the committee is theory.",
     "Reality-tests every decision; carries the field’s objection into the room before "
     "rollout, not after."),
    ("OpEx / PMO Lead",
     "Runs the initiative, holds the evidence, brings the gate pack.",
     "Does not decide — presents, and says plainly when a gate cannot be evidenced."),
]

WORKGROUP_ROLES = [
    ("Initiative Lead (PM)", "Runs the week. Owns the plan, the register and the readout.",
     "Every week"),
    ("Capacity & scheduling process owner",
     "Owns the process design end to end — the person who can say what the target state IS.",
     "Every week"),
    ("Clinical operations lead",
     "Translates every design decision into what it does to a clinical day.", "Every week"),
    ("Scheduler representative  ×2",
     "The people who do the job today. Two, so one absence does not silence the seat.",
     "Every week"),
    ("DCS / Clinical Manager representative",
     "Owns the upstream work — orders, QA, care-team assignment — that the schedule depends on.",
     "Every week"),
    ("Data & analytics",
     "Owns the baseline, the scorecard and the source war-list. Nothing is displayed without a "
     "named source.", "Every week"),
    ("IT / integration",
     "Owns the feasibility answer and the system-of-record relationship.", "Every week"),
    ("Finance analyst",
     "Keeps the business case honest as scope moves. Owns the anti-double-counting rules.",
     "Bi-weekly"),
    ("Change & communications lead",
     "Owns what the field hears, when, and from whom.", "Every week"),
    ("Training lead",
     "Owns the curriculum and the ambassador model. Joins in force at pre-pilot.", "From pilot"),
    ("Vendor evaluation coordinator",
     "Single channel to every vendor. Owns the questionnaire, the scores and the session "
     "logistics.", "Through selection"),
]

SME_BENCH = [
    ("Field RN / SOC nurse", "Admission reality, the 485 moment, what a full day actually holds."),
    ("PT / OT / ST discipline leads",
     "Discipline-specific visit patterns, front-loading, and the PT/PTA economics."),
    ("Home health aide & paraprofessional lead",
     "The shortage, the scheduling pattern, and the part of capacity most often left out of "
     "the model."),
    ("Authorisation & payer operations",
     "Auth as gate and as ceiling; the notification volume; what actually holds an admission."),
    ("Revenue cycle / PDGM coding",
     "Period boundaries, LUPA thresholds, and what a missed visit costs in payment terms."),
    ("OASIS & clinical documentation",
     "Assessment windows, recert timing, and the documentation load that eats capacity."),
    ("System-of-record administrator (HCHB / MatrixCare)",
     "What the system can and cannot do, what is switched off, and what a change costs."),
    ("Commure / point-solution owners",
     "Overlap, sequencing, and where a new tool would collide with one already arriving."),
    ("Workday / HRIS",
     "Roster, PTO and availability truth — and which integrations are currently OFF."),
    ("Legal & state regulatory (WA, CA named)",
     "Automated patient contact rules and the human-script commitments already made."),
    ("Telephony & patient communications",
     "What the confirmation and reminder path can physically do today."),
    ("Labour relations",
     "Any agreement that constrains scheduling, productivity expectation or notice."),
    ("Branch Executive Director — per pilot market",
     "Local truth for the market being piloted. A different person per wave, by design."),
    ("Recruiting & onboarding",
     "Orientation drag, time-to-productive, and how fast capacity can actually be added."),
    ("Data warehouse / BI",
     "Where a number really comes from, how often it refreshes, and who owns the report."),
]


def build_governance_tab(wb, index):
    ws = wb.create_sheet("Governance & People", index)
    tab_colour(ws, "7A5C00")
    title_block(
        ws,
        "Governance & People  —  who decides, who builds, who we call",
        "Three bodies, deliberately separate. The steering committee DECIDES and unblocks; the "
        "workgroup BUILDS and meets weekly; the SME bench is CONSULTED and is never "
        "accountable for delivery. Most initiatives stall by confusing the three — an SME asked "
        "to decide, or a steering committee asked to design. Seats are listed by ROLE. Names "
        "are open: write them in.",
        "E",
    )
    widths(ws, {"A": 5.0, "B": 44.0, "C": 60.0, "D": 52.0, "E": 24.0})

    r = 4
    band(ws, r, "1 — LEADERSHIP STEERING COMMITTEE     ·     monthly, plus a session at every "
                "phase gate     ·     decides, funds, unblocks", 5, accent=NAVY, height=22.0)
    r += 1
    header_row(ws, r, ["#", "Seat", "Why this seat is at the table",
                       "What this seat decides", "Name  (write in)"],
               accent=MID, height=26.0)
    r += 1
    for i, (seat, why, decides) in enumerate(STEERING_SEATS, start=1):
        body_row(ws, r, [i, seat, why, decides, None], height=44.0,
                 bold_cols=(2,), center_cols=(1,))
        c = ws.cell(row=r, column=5)
        c.fill = fill(EDIT)
        c.border = Border(left=Side(style="thin", color=EDITBORDER),
                          right=Side(style="thin", color=EDITBORDER),
                          top=Side(style="thin", color=EDITBORDER),
                          bottom=Side(style="thin", color=EDITBORDER))
        r += 1

    r += 1
    band(ws, r, "2 — PRIMARY WORKGROUP     ·     weekly     ·     builds the thing, brings the "
                "evidence, owns the artifacts", 5, accent=NAVY, height=22.0)
    r += 1
    header_row(ws, r, ["#", "Role on the workgroup", "What this role owns", "Cadence",
                       "Name  (write in)"], accent=MID, height=26.0)
    r += 1
    for i, (role, owns, cadence) in enumerate(WORKGROUP_ROLES, start=1):
        body_row(ws, r, [i, role, owns, cadence, None], height=38.0,
                 bold_cols=(2,), center_cols=(1,))
        ws.cell(row=r, column=4).alignment = Alignment(horizontal="center", vertical="center")
        c = ws.cell(row=r, column=5)
        c.fill = fill(EDIT)
        c.border = Border(left=Side(style="thin", color=EDITBORDER),
                          right=Side(style="thin", color=EDITBORDER),
                          top=Side(style="thin", color=EDITBORDER),
                          bottom=Side(style="thin", color=EDITBORDER))
        r += 1

    r += 1
    band(ws, r, "3 — SUBJECT MATTER EXPERT BENCH     ·     as needed, by invitation     ·     "
                "consulted, never accountable", 5, accent=NAVY, height=22.0)
    r += 1
    header_row(ws, r, ["#", "Domain", "What we would call them for",
                       "Likely source / team  (write in)", "Name  (write in)"],
               accent=MID, height=26.0)
    r += 1
    for i, (domain, why) in enumerate(SME_BENCH, start=1):
        body_row(ws, r, [i, domain, why, None, None], height=36.0,
                 bold_cols=(2,), center_cols=(1,))
        for col in (4, 5):
            c = ws.cell(row=r, column=col)
            c.fill = fill(EDIT)
            c.border = Border(left=Side(style="thin", color=EDITBORDER),
                              right=Side(style="thin", color=EDITBORDER),
                              top=Side(style="thin", color=EDITBORDER),
                              bottom=Side(style="thin", color=EDITBORDER))
        r += 1

    r += 1
    callout(
        ws, r,
        "HOW TO KEEP THE THREE FROM COLLAPSING INTO EACH OTHER",
        [
            "A steering committee that designs has stopped governing.  Bring it decisions with "
            "a recommendation and the evidence, not open questions.",
            "A workgroup with no decision rights becomes a status meeting.  It should be able "
            "to settle anything that does not change scope, spend, the operating model or the "
            "clinical guardrails — and escalate only what genuinely does.",
            "An SME asked to be accountable will start hedging.  Call them for a specific "
            "question, take their answer as evidence, and leave the delivery accountability "
            "with the workgroup.",
            "Every seat is filled by a NAMED person with a named alternate.  A seat that is "
            "‘the finance team’ is an empty seat, and it will be empty at the gate that "
            "matters.",
        ],
        5,
    )
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# 5. Overall Project — extend the team's existing house-format plan
#
#    The base workbook's 'Overall Project' tab is already the format the team
#    works in: Item# · Category · Phase · Task Description · OpEx Owner ·
#    Due Date · Status · Date Complete · Notes/Decision, banded by STEP, with
#    steps 1–10 filled to row 67. We continue it — same bands, same styling
#    (cloned cell-for-cell from rows 8 and 9), same numbering. Owners and dates
#    on the new rows are left blank to be written in.
# ══════════════════════════════════════════════════════════════════════════════

PT = "Project Team/OpEx"
GOV = "Governance"
MEAS = "Measurement - Analytics & Feedback"
COMMS = "Communications"
SHARED = "Shared Services (IT, Contracting, Marketing, Legal)"
WORK = "Workforce"
TMX = "Team Member Experience Plan + Recognition"
TRAIN = "Training, Materials & Ambassadors"
BC = "Business Continuity"
FIN = "Finish the Job Priorities"

DISC, PRE, PILOT, ONGOING = ("Discovery", "Pre-Pilot Development", "Active Pilot",
                             "Ongoing Management")

# (category, phase, task, status, note)  ·  a bare string is a STEP band
HOUSE_PLAN = [
    "STEP 11  ·  BUILDING THE VENDOR QUESTIONNAIRE",
    (PT, DISC, "Build the questionnaire from the scored variable inventory, not from a "
     "template", "Complete",
     "Every question traces to a variable ID or a catalogued constraint. Questions that "
     "traced to neither were cut, however standard they looked."),
    (PT, DISC, "Order the sections so the three pillars are answered before the commercials",
     "Complete",
     "A vendor reads our operating model before they read our budget. Pricing is section I "
     "of J, deliberately."),
    (MEAS, DISC, "Require evidence with every claim — screenshot, report name, configuration "
     "path", "Complete",
     "Yes/no rewards the boldest writer, not the best product. An unevidenced 'yes' scores "
     "as roadmap."),
    (COMMS, DISC, "Run every vendor clarification through one named channel, published to all "
     "recipients", "Complete",
     "No vendor holds private information. The clarification log is part of the record."),

    "STEP 12  ·  THE REFERENCE PACK  —  GIVING VENDORS OUR CONTEXT",
    (COMMS, DISC, "Issue the one-pager — the three pillars and the primary variables under "
     "each", "Complete",
     "One landscape page. Orientation for whoever at the vendor actually writes the "
     "response."),
    (COMMS, DISC, "Issue the full variable reference — every variable, one page per pillar",
     "Complete", "The depth behind the one-pager, for the detailed sections."),
    (COMMS, DISC, "Issue the current-state flow map WITH the questionnaire, not on request",
     "Complete",
     "A deliberate exposure of our constraints. It is what lets a good vendor say 'your step "
     "4 is our step 7' instead of pitching."),
    (GOV, DISC, "Decide what may be shared with a vendor, and on what terms", "In Process",
     "Settled for the reference pack. Still open for the on-sites, which go to real branch "
     "shapes and volumes — see OI-18."),

    "STEP 13  ·  CONSTRUCTING THE RUBRIC",
    (GOV, DISC, "Build the rubric BEFORE opening a single response", "Complete",
     "A rubric written after reading the answers is a justification, not an instrument."),
    (GOV, DISC, "Mirror the questionnaire's section order exactly", "Complete",
     "A scorer reads a response top to bottom and scores it without hunting."),
    (MEAS, DISC, "Derive the section weights from the scored inventory, then adjust for the "
     "immovable constraints", "Complete",
     "Capacity carries the most gating variables so it carries the most weight; integration "
     "was raised above its raw count because the nine untoggleable constraints sit there."),
    (GOV, DISC, "Cap any single section so none can carry the decision alone", "Complete",
     "No section above 20. The three pillars together sit just under half the total."),
    (GOV, DISC, "Leave the weighting editable, and say so on the sheet", "Complete",
     "Weighting is a leadership judgement, not a finding. Change one cell and every score "
     "recomputes in front of the room."),
    (MEAS, DISC, "Hold the gating variables outside the weighted total, as knockouts",
     "Complete", "An average can hide a zero. A knockout cannot be averaged away."),
    (GOV, DISC, "Reconcile the as-run weights against the issued questionnaire before the "
     "steering review", "Not Started",
     "OI-15. Where the as-run set differs from the set on the rubric tab, the as-run set "
     "governs and the difference is noted."),

    "STEP 14  ·  SCORING, AND THE CUT TO SIX",
    (PT, DISC, "Apply the knockouts first, on evidence, before anything is totalled",
     "Complete", "Disqualification is a finding about capability, not a low score."),
    (PT, DISC, "Score independently, then reconcile to one agreed score per section",
     "Complete",
     "A spread between two scorers usually indicts the question rather than the product. "
     "The argument was written down either way."),
    (GOV, DISC, "Take the cut at the natural break in the scores, not at a pre-decided "
     "headcount", "Complete",
     "Six is where the field parted. Had the break fallen at five, five is where the cut "
     "would have been taken."),
    (GOV, DISC, "Publish the shortlist memo with a written reason for every vendor on and off "
     "the list", "Complete", "The record that makes the cut defensible from outside the room."),

    "STEP 15  ·  REGRETS AND INCLUSIONS",
    (COMMS, DISC, "Send inclusion letters to the six with the deep-dive expectations and the "
     "date frame", "In Process", "Six vendors who know exactly what they are walking into."),
    (COMMS, DISC, "Send regret letters, each carrying a reason specific enough to be useful",
     "In Process",
     "'We went another direction' is not a reason. The market is small and how we decline is "
     "itself a reputational act."),
    (COMMS, DISC, "Send them close together so no vendor learns their outcome from someone "
     "else", "In Process", "Sequencing is part of the courtesy."),
    (PT, DISC, "Note the vendors worth re-engaging for a later phase", "In Process",
     "Several of these products may be the right answer for a later pillar."),

    "STEP 16  ·  VIRTUAL DEEP DIVES WITH THE SIX",
    (PT, PRE, "Build ONE deep-dive script and use it unchanged for all six", "In Process",
     "OI-16. Lock it before further sessions run, or the last vendors were evaluated on a "
     "different instrument and the scorecard cannot carry the cut."),
    (PT, PRE, "Build the session on our own scenarios, not on the vendor's demo", "In Process",
     "The 7am call-out, the pending-authorisation admission, the LUPA-risk week, the recert "
     "window colliding with a full territory."),
    (PT, PRE, "Have the vendor drive their own system live; no slides for the working portion",
     "In Process",
     "An unscripted demo shows you their best three minutes, not our hardest Tuesday."),
    (MEAS, PRE, "Score the deep dives on the same instrument as the questionnaire",
     "In Process", "The two reads then sit side by side, and the gap between them is visible."),
    (MEAS, PRE, "Keep the claimed-versus-demonstrated gap log", "In Process",
     "The primary input to the cut from six to three."),

    "STEP 17  ·  THE FINAL THREE  —  ON-SITE HALF-DAY SESSIONS",
    (GOV, PRE, "Agree the decision rule for the cut from six to three before the last deep "
     "dive", "Not Started",
     "OI-17. Deep-dive score, gap log, knockouts surfaced live — and in what order. Decided "
     "afterwards, it is a justification."),
    (PT, PRE, "Run an identical half-day on site with each of the three finalists",
     "Not Started",
     "Workgroup and the people who will actually use the product in the room. Not a sales "
     "audience."),
    (PT, PRE, "Configure against our real branch shapes during the session", "Not Started",
     "Tests the thing a virtual session cannot: whether it bends to our territory, "
     "discipline and pay reality."),
    (SHARED, PRE, "Meet the implementation team we would actually be assigned", "Not Started",
     "Not the pre-sales team. Named people, named availability, named method."),
    (SHARED, PRE, "Work the integration specifics with the system-of-record owner present",
     "Not Started", "Real-time versus batch, what is written back, what breaks at upgrade."),
    (PT, PRE, "Run reference calls to agencies we choose, not the ones offered", "Not Started",
     "Run in parallel with the on-sites so the answers can be put to the vendor."),
    (GOV, PRE, "Bring the selection recommendation and a named second choice to steering",
     "Not Started", "With the evidence behind both, not a preference."),

    "STEP 18  ·  SELECTION AND CONTRACTING",
    (SHARED, PRE, "Write the acceptance tests from the MVP spec and the gating variables",
     "Not Started",
     "The contract should require the product to do the things the rubric disqualified other "
     "vendors for failing."),
    (SHARED, PRE, "Negotiate against a defined scope rather than a platform licence",
     "Not Started", "Price the residual, not the brochure."),
    (SHARED, PRE, "Settle exit and data-portability terms before signature", "Not Started",
     "Our data, our format, on our notice. It is never cheaper to ask later."),
    (GOV, PRE, "Write the pilot charter with the kill criteria pre-committed", "Not Started",
     "Written before the pilot starts, by the people who would have to honour it."),

    "GOVERNANCE  ·  SEATING THE PEOPLE WHO RUN THIS",
    (GOV, DISC, "Identify and seat the Leadership Steering Committee", "In Process",
     "OI-12. Ten seats defined by role and decision right on 'Governance & People'. Names "
     "open for write-in."),
    (GOV, DISC, "Publish the steering charter — decision rights, cadence, escalation path",
     "Not Started", "Monthly, plus a session at every phase gate."),
    (PT, DISC, "Confirm the primary workgroup and its decision rights", "In Process",
     "OI-13. Eleven roles, including two scheduler seats so one absence does not silence the "
     "frontline."),
    (PT, DISC, "Finalise the subject matter expert bench", "In Process",
     "OI-14. Fifteen domains, each with what we would call them for. Consulted, never "
     "accountable."),
    (GOV, DISC, "Name an alternate for every steering seat", "Not Started",
     "A seat that is 'the finance team' is an empty seat, and it will be empty at the gate "
     "that matters."),
    (GOV, PRE, "Set the phase-gate criteria and the go/no-go convention", "Not Started",
     "A gate that cannot be evidenced has not been passed, and someone has to say so."),

    "WHAT THE NEXT ARC NEEDS  ·  PILOT READINESS",
    (PT, PRE, "Select the lighthouse pilot branch", "Not Started",
     "Favour a new-integration or brand-new go-live. Resolve the pay-model trade deliberately "
     "in the charter, not at readout."),
    (MEAS, PRE, "Pull the 13-week trailing baseline and agree the metric definitions in "
     "writing", "Not Started", "Definitions differ silently branch to branch."),
    (MEAS, PRE, "Pre-register the primary pilot metric, its threshold and its duration",
     "Not Started", "Registered before the pilot, with the stop rule attached."),
    (TRAIN, PRE, "Build the ambassador model and name candidates per pilot branch",
     "Not Started", "Ambassadors trained first, and trained deeper."),
    (TMX, PRE, "Define what changes for a scheduler, a DCS and a field clinician",
     "Not Started",
     "Three separate answers — they are three different jobs. Frame to clinicians as a "
     "personal assistant, not a control mechanism."),
    (WORK, PRE, "Design the staffing-to-census ratios and the trigger bands", "Not Started",
     "By discipline and acuity, including the PRN and agency call thresholds."),
    (BC, PRE, "Keep the manual process alive until the pilot clears its gate", "Not Started",
     "The pilot is a reversible experiment. Reversible has to mean something."),
    (FIN, ONGOING, "Publish the reusable initiative framework", "Complete",
     "See the 'Initiative Framework' tab — our own method with the subject matter removed, "
     "for the next initiative."),
]


def extend_house_plan(wb):
    """Continue the team's existing 'Overall Project' sheet in its own styling."""
    from copy import copy as _copy

    ws = wb["Overall Project"]

    band_style = _copy(ws["A8"]._style)          # the STEP band
    row_styles = {col: _copy(ws.cell(row=9, column=col)._style) for col in range(1, 10)}

    # continue the item numbering and start below the last filled row
    last, item = 7, 0
    for row in range(8, ws.max_row + 1):
        if any(ws.cell(row=row, column=c).value is not None for c in range(1, 10)):
            last = row
        v = ws.cell(row=row, column=1).value
        if isinstance(v, (int, float)):
            item = max(item, int(v))

    r = last + 2
    for entry in HOUSE_PLAN:
        if isinstance(entry, str):
            ws.cell(row=r, column=1, value=entry)
            for col in range(1, 10):
                ws.cell(row=r, column=col)._style = _copy(band_style)
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=9)
            ws.row_dimensions[r].height = 21.95
        else:
            category, phase, task, status, note = entry
            item += 1
            values = {1: item, 2: category, 3: phase, 4: task, 5: None, 6: None,
                      7: status, 8: None, 9: note}
            for col in range(1, 10):
                c = ws.cell(row=r, column=col, value=values[col])
                c._style = _copy(row_styles[col])
            ws.row_dimensions[r].height = 32.1
        r += 1

    ws.auto_filter.ref = f"A7:I{r - 1}"
    ws["D1"] = ("Key Milestones  ·  six vendors in deep dive  ·  final three on site  ·  "
                "selection to steering  ·  pilot charter")

    # the dropdowns the team already uses, re-pointed at the inherited List tab
    phase_dv = DataValidation(type="list", formula1="=List!$A$2:$A$8", allow_blank=True)
    status_dv = DataValidation(type="list", formula1="=List!$A$15:$A$23", allow_blank=True)
    for dv in (phase_dv, status_dv):
        ws.add_data_validation(dv)
    phase_dv.add(f"C8:C{r - 1}")
    status_dv.add(f"G8:G{r - 1}")
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# 6. Initiative Framework — the reusable, topic-neutral roadmap
# ══════════════════════════════════════════════════════════════════════════════

FRAMEWORK = [
    ("ARC ONE  —  UNDERSTAND     ·     you are not allowed to design yet", None, None, None, None),
    ("1", "Test the problem you were handed",
     "Is the problem as presented the real one?",
     "Refuse the framing until it survives one round of evidence. The presented problem is "
     "usually a symptom with a department attached to it.",
     "A restated problem, in writing, with what changed and why. If nothing changed, say that "
     "too — but say it after testing, not instead of testing.",
     "You build an excellent solution to the wrong problem, and nobody finds out until "
     "rollout."),
    ("2", "Run four kinds of meeting, and never mix them",
     "What actually happens, and where does it get stuck?",
     "Discovery (blank page), SME download (one expert, uninterrupted), validation (a DRAFT "
     "brought to be corrected) and decision (someone who can decide, in the room). A "
     "validation meeting without a draft becomes a discovery meeting and you lose the week.",
     "A verbatim, line-numbered record so every later citation still resolves. Decisions "
     "numbered on the day and never renumbered.",
     "Six weeks later nobody can reconstruct why anything was decided, and the same debate "
     "runs twice."),
    ("3", "Build the variable list BEFORE the map",
     "For this thing to happen, what must all be true at once?",
     "Build it first, deliberately. A map drawn first contains only what the mapper already "
     "thinks about. Group into ID families and fill each one to exhaustion; the IDs become "
     "the join key to every document downstream, forever.",
     "An ID’d inventory, grouped, with nothing in it that cannot be explained to a new person "
     "in a sentence.",
     "Your map is a portrait of your own assumptions, and every gap in it is invisible."),
    ("4", "Map the current state AGAINST that list",
     "How does the work actually run today?",
     "Fix the design system before drawing. Generate from source so a correction costs a "
     "minute, not an afternoon. Split into several flows rather than one monster. Draw it "
     "specific enough to be WRONG in public — vague diagrams never get corrected because "
     "there is nothing to point at.",
     "A current-state baseline, plus the correction history: every change, who raised it, what "
     "it changed.",
     "You get consensus on a picture nobody believes, which is not the same as agreement."),
    ("5", "Separate the pain from the constraint",
     "Where is the energy, and separately, where is the money?",
     "They are not the same and must be kept apart. A pain point is what people complain "
     "about; a constraint is what limits throughput. Then classify every constraint by "
     "CHANGEABILITY, not severity — severity tells you what hurts, changeability tells you "
     "what to do about it.",
     "A constraint register and a ranked set of dossiers. The constraints that CANNOT be "
     "changed are your entire case for building anything.",
     "You spend the budget on the loudest complaint, which is often your own policy and needed "
     "no system at all."),
    ("6", "Re-cut the list, then score it",
     "Which of these actually matter, and what do we still not know?",
     "Close the loop back to step 3 — by now the list is three documents old. Re-cut against "
     "the map’s corrections and the constraint weightings, then SCORE, so priority is "
     "reproducible from columns rather than remembered from a meeting.",
     "A scored inventory carrying weight, a gating flag and a conflict-risk flag; and the open "
     "questions published in DEPENDENCY order, so answering one unblocks the next.",
     "Priority becomes whoever argued hardest most recently."),
    ("ARC TWO  —  GROUND IT     ·     make it real, costed and sourced", None, None, None, None),
    ("7", "Open the business case early, and in parallel",
     "If this works, what changes, in what unit, that someone could count?",
     "Open it at the first pass, not at the end. Built late, a case gets reverse-engineered "
     "from a number somebody wants to hear. Built early, it tells you which variables are "
     "worth building for.",
     "A register with sized cases, evidence tiers, anti-double-counting rules, the missing "
     "inputs named, and an explicit ‘must never claim’ list.",
     "You defend a number you cannot source, in front of the one person who can check it."),
    ("8", "Prove the data you are designing against exists",
     "Does any of this actually exist, today, somewhere, refreshed?",
     "Three separate instruments, not one: the landscape (what touches this, and is it "
     "real-time), the source war-list (per element: exact report, owner, refresh cadence, "
     "exists-today Y/Partial/N) and the coverage scan (what the design assumes that does not "
     "exist).",
     "A row per data element with a named source, a named owner and a stated refresh. "
     "Everything marked N or Partial IS the build backlog.",
     "You ship a design that requires data nobody produces, and discover it during "
     "configuration."),
    ("9", "Specify the MVP as a projection, not an invention",
     "What exactly are we building first, and what will it deliberately NOT do?",
     "The MVP is the variable list pushed through filters — layer, required, sourceable, "
     "phase posture. If it requires invention, an earlier step is incomplete; go back rather "
     "than forward.",
     "An in-scope list where every EXCLUSION carries a reason and a re-entry trigger. An "
     "exclusion with no re-entry trigger is a decision you will silently forget.",
     "Scope grows by accretion and nobody can say what v1 was supposed to be."),
    ("10", "Draw the target state only once the current state stops moving",
     "Where are we going, and what is still genuinely undecided?",
     "Defer it deliberately. A target state drawn early encodes your assumptions instead of "
     "the organisation’s reality. Draw it in the SAME visual language as the current state so "
     "the two lie side by side.",
     "A target sheet with every element marked for release and posture, plus an explicit panel "
     "naming what was deliberately NOT drawn.",
     "You get a future state that is a wish list, and an argument about scope disguised as an "
     "argument about the diagram."),
    ("ARC THREE  —  CHOOSE     ·     run this arc only if the answer might be bought",
     None, None, None, None),
    ("11", "Write the questionnaire from your own variable list",
     "What do we need to know, and how do we ask it so two answers are comparable?",
     "Every question traces to a variable or a constraint; a question that traces to neither "
     "gets cut, however standard it looks. Order the sections so your operating model is "
     "answered before your budget is. Require evidence — a screenshot, a report name, a "
     "configuration path — because yes/no rewards the boldest writer.",
     "A sectioned questionnaire, a question-to-variable trace, and ONE named channel for "
     "clarifications with every answer published to all recipients.",
     "You collect brochures, and the scoring becomes a debate about who writes best."),
    ("12", "Send your context with the ask",
     "How much do they need to know before their answer is worth reading?",
     "A vendor answers at the level of context you give them. Send the summary, the full "
     "variable reference and the current-state map WITH the questionnaire. Yes, it exposes "
     "your constraints — that is what lets a good vendor say ‘your step 4 is our step 7’ "
     "instead of pitching.",
     "A reference pack issued with the ask: one page for orientation, the full list for depth, "
     "the map for the process.",
     "Every answer is generic, and you cannot tell a good fit from a good writer."),
    ("13", "Build the rubric before you open a single response",
     "How do we score this so someone who wasn’t in the room gets the same answer?",
     "Same section order as the questionnaire, so a scorer never hunts. Weights DERIVED from "
     "the scored list, then left EDITABLE, because weighting is a leadership judgement and "
     "should be arguable with the model open. Keep the knockouts OUTSIDE the weighted total — "
     "an average can hide a zero.",
     "A scoring instrument, an evidence scale, a knockout list, and a weight table where "
     "changing one cell visibly recomputes every score.",
     "The rubric becomes a justification written after the fact, and everyone can feel it."),
    ("14", "Narrow in stages, and close every loop",
     "Who is actually worth our hours, and what do we owe the rest?",
     "Knockouts first, on evidence. Score independently, then reconcile — and write the "
     "argument down, because a spread between two scorers is usually a badly-worded question. "
     "Take the cut at the natural break in the scores, not at a pre-decided headcount. Then "
     "answer every respondent, with a reason.",
     "A documented long list → shortlist → deep dives → finalists → on-site, each stage with "
     "its own evidence; and a written reason behind every decline.",
     "The shortlist looks arbitrary from the outside, and the market remembers how you "
     "declined them."),
    ("ARC FOUR  —  GOVERN & PROVE     ·     the part most initiatives skip",
     None, None, None, None),
    ("15", "Seat three bodies, and keep them separate",
     "Who decides, who builds, and who do we merely call?",
     "Steering DECIDES and unblocks. The workgroup BUILDS and meets weekly. SMEs are "
     "CONSULTED and are never accountable for delivery. Confusing the three is the most common "
     "way an initiative stalls without anyone being able to say why.",
     "Named seats — a role with no name attached is an empty seat — decision rights in "
     "writing, a cadence, and a named alternate for every seat.",
     "Decisions wait for a meeting that has no authority to make them."),
    ("16", "Pre-commit the kill criteria",
     "What would make us stop, and have we agreed it in advance?",
     "Written before the pilot starts, by the people who would have to honour it. A stop rule "
     "agreed afterwards is a negotiation, not a control.",
     "A charter with a pre-registered primary metric, a threshold, a duration, and a stop rule "
     "someone has signed.",
     "Nothing is ever killed; it is quietly rescoped until it cannot fail, and cannot "
     "succeed."),
    ("17", "Pilot as a reversible experiment, not a soft launch",
     "Does this actually work, in one place, without breaking something else?",
     "One unit. The binding constraint. A metric registered in advance. Keep the old way alive "
     "until the gate is cleared, and watch for the local win that hides a system loss.",
     "A repeatable playbook — the MECHANISM, not a heroic manager — and a result that held for "
     "long enough to believe.",
     "You scale one exceptional person, and it does not replicate."),
    ("18", "Scale no faster than support, then hand it over",
     "Can this survive without the people who built it?",
     "Waves sequenced by readiness, not by calendar. Central standards with local judgement — "
     "over-centralising amputates the judgement the system still needs. A gate that cannot be "
     "evidenced has not been passed, and someone has to be willing to say so out loud.",
     "Drift detection, a refresh cadence, a runbook, and a NAMED standing owner who is not the "
     "project team.",
     "It backslides the quarter after attention moves on, and the next initiative inherits the "
     "cynicism."),
]


def build_framework_tab(wb, index):
    ws = wb.create_sheet("Initiative Framework", index)
    tab_colour(ws, GREEN)
    title_block(
        ws,
        "Initiative Framework  —  a reusable roadmap for getting an initiative off the table",
        "Topic-neutral by design: this is the SHAPE of the work, not the content of ours. It is "
        "the capacity & scheduling method with the subject matter removed — four arcs, eighteen "
        "steps. Arc Three runs only when the answer might be purchased; everything else applies "
        "to any initiative large enough to need a steering committee.",
        "F",
        accent=GREEN,
    )
    widths(ws, {"A": 6.0, "B": 34.0, "C": 40.0, "D": 58.0, "E": 54.0, "F": 46.0})
    header_row(
        ws, 4,
        ["Step", "The step", "The question it answers", "The rule that makes it work",
         "What must exist when it is done", "Skip it, and this is what happens"],
        accent=GREEN,
    )
    r = 5
    for entry in FRAMEWORK:
        if entry[1] is None:
            band(ws, r, entry[0], 6, accent=GREEN, height=22.0)
        else:
            body_row(ws, r, list(entry), height=108.0, bold_cols=(2,),
                     accent_col=1, accent_fill="2E7D68", shade="F2F7F5")
        r += 1

    r += 1
    callout(
        ws, r,
        "THE RULES THAT HOLD WHATEVER THE INITIATIVE IS",
        [
            "1.  Build the list before the picture.  Anything drawn first is a portrait of the "
            "drawer’s assumptions.",
            "2.  Classify by changeability, not severity.  Severity tells you what hurts; "
            "changeability tells you what to do.",
            "3.  Derive priority from columns, not from memory.  If it cannot be recomputed, it "
            "will be re-argued.",
            "4.  Publish a draft specific enough to be wrong.  Vagueness is not humility — it "
            "is what stops people correcting you.",
            "5.  If a step produced no document, it did not happen.  The register is the test, "
            "not the meeting calendar.",
            "6.  Weightings, scopes and stop rules are set BEFORE the evidence arrives, and "
            "left editable afterwards.  Decided-in-advance and arguable-in-public are not in "
            "tension; together they are the whole discipline.",
        ],
        6,
        accent=GREEN,
        tint="E8F1EE",
    )
    return ws


# ══════════════════════════════════════════════════════════════════════════════
# 7. Document Register — extend with everything arcs two and three produced
# ══════════════════════════════════════════════════════════════════════════════

REGISTER_ADDITIONS = [
    ("STEPS 11–18 — VENDOR SELECTION", None, None, None, None),
    ("Vendor questionnaire  ★", "11",
     "The scored variable inventory + the constraint register. Sections A–J, pillars first and "
     "commercials last; every question traced to a variable ID or a constraint, and untraceable "
     "questions cut",
     "Vendor selection folder", "Complete"),
    ("Question-to-variable trace", "11",
     "The map from each question back to the variable or constraint that justifies it — the "
     "instrument that kept the questionnaire from becoming a template",
     "Vendor selection folder", "Complete"),
    ("Vendor clarification log", "11",
     "Every question a vendor asked and the answer, published to all recipients so no vendor "
     "held private information", "Vendor selection folder", "Complete"),
    ("Reference pack — one-pager", "12",
     "The three pillars and the primary variables under each, on one landscape page. Issued "
     "WITH the questionnaire", "artifacts/ (PDF)", "Complete"),
    ("Reference pack — variable reference", "12",
     "Three pages, one per pillar, carrying every variable. The depth behind the one-pager",
     "artifacts/ (PDF)", "Complete"),
    ("Reference pack — current-state flow map", "12",
     "The primary map, with the detailed composite available on request. Published "
     "deliberately: it is what lets a vendor map their process onto ours",
     "artifacts/ (PDF)", "Complete"),
    ("Scoring rubric  ★", "13",
     "Section order identical to the questionnaire. Weights derived from the scored inventory, "
     "adjusted for immovable constraints, capped, and left editable. Knockouts held outside the "
     "weighted total", "Workbook tab ‘Questionnaire & Rubric’", "Complete"),
    ("Scorer instructions & evidence scale", "13",
     "The 0–4 scale, what counts as evidence, and the rule that an unevidenced ‘yes’ scores as "
     "roadmap", "Vendor selection folder", "Complete"),
    ("Scored response matrix", "14",
     "Every respondent, every section, both scorers, the reconciled score and the knockout "
     "findings", "Vendor selection folder", "Complete"),
    ("Reconciliation notes", "14",
     "Where scorers differed and how it was resolved — kept because a spread usually indicts "
     "the question, not the product", "Vendor selection folder", "Complete"),
    ("Shortlist memo — the six", "14",
     "The ranked field, where the natural break fell, and a written reason for every vendor on "
     "and off the list", "Vendor selection folder", "Complete"),
    ("Regret & inclusion letters", "15",
     "One per respondent. Inclusions carry the deep-dive expectations and the date frame; "
     "regrets carry a specific reason and, where warranted, a re-engagement note",
     "Vendor selection folder", "In Process"),
    ("Deep-dive script & scenario set", "16",
     "The same script for all six, built on our own scenarios — the 7am call-out, the "
     "pending-auth admission, the LUPA-risk week, the recert collision",
     "Vendor selection folder", "In Process"),
    ("Deep-dive session records & scores", "16",
     "Per vendor, scored on the same instrument as the questionnaire so the two reads sit side "
     "by side", "Vendor selection folder", "In Process"),
    ("Claimed-versus-demonstrated gap log", "16",
     "Every place a live session did not match the written response. The primary input to the "
     "cut from six to three", "Vendor selection folder", "In Process"),
    ("Finalist on-site agenda", "17",
     "Identical half-day for all three: configuration on our own branch shapes, the named "
     "implementation team, integration specifics, and how the vendor behaves when told they "
     "are wrong", "Vendor selection folder", "Not Started"),
    ("Reference call notes", "17",
     "Agencies we choose, not the ones offered", "Vendor selection folder", "Not Started"),
    ("Selection recommendation", "18",
     "The finalist scorecard, the recommendation, the named second choice and the evidence "
     "behind both", "Vendor selection folder", "Not Started"),
    ("Scripted acceptance demonstrations", "18",
     "Drawn from the MVP spec and the gating variables — the contract should require what the "
     "rubric disqualified vendors for failing", "Vendor selection folder", "Not Started"),
    ("GOVERNANCE, PLAN & FRAMEWORK", None, None, None, None),
    ("Governance roster  ★", "gov",
     "Three bodies defined by role: steering (decides), workgroup (builds), SME bench "
     "(consulted). Names left open for write-in",
     "Workbook tab ‘Governance & People’", "In Process — names open"),
    ("Overall project plan — house format", "gov",
     "The overarching plan in the layout the team already uses: Item# · Category · Phase · Task "
     "· OpEx Owner · Due Date · Status · Date Complete · Notes. Owners and dates left blank",
     "Workbook tab ‘Overall Project Plan’", "In Process"),
    ("Initiative framework  ★", "all",
     "Our own method with the subject matter removed — four arcs, eighteen steps, each with its "
     "rule, its deliverable and the cost of skipping it. Built to be handed to a different "
     "initiative", "Workbook tab ‘Initiative Framework’", "Complete"),
]


def extend_register(wb):
    ws = wb["Document Register"]
    r = ws.max_row + 2
    # continue the numbering already running in column A
    n = 0
    for row in range(5, ws.max_row + 1):
        v = ws.cell(row=row, column=1).value
        if isinstance(v, (int, float)):
            n = max(n, int(v))
    for entry in REGISTER_ADDITIONS:
        if entry[1] is None:
            band(ws, r, entry[0], 6, accent=MID, height=20.1)
        else:
            n += 1
            doc, step, inputs, where, status = entry
            body_row(ws, r, [n, doc, step, inputs, where, status], height=45.95,
                     bold_cols=(2,), center_cols=(1, 3, 6), shade=None)
        r += 1
    return r


# ══════════════════════════════════════════════════════════════════════════════
# 8. Open Items — what the new arcs added
# ══════════════════════════════════════════════════════════════════════════════

OPEN_ADDITIONS = [
    ("OI-12", "GATE", "gov", "Seat the Leadership Steering Committee by name",
     "Ten seats are defined by role and decision right; none is filled. A vendor "
     "recommendation, a pilot charter and a set of pre-committed kill criteria all require a "
     "body that can approve them. Until the seats carry names with named alternates, there is "
     "nothing for the selection to be presented TO.", "TBD", "In Process"),
    ("OI-13", "GATE", "gov", "Confirm primary workgroup membership and its decision rights",
     "Eleven roles defined, including two scheduler seats so one absence does not silence the "
     "frontline. Without written decision rights the workgroup escalates everything and becomes "
     "a status meeting — the failure mode the governance design exists to prevent.",
     "TBD", "In Process"),
    ("OI-14", "GATE", "gov", "Finalise the subject matter expert bench",
     "Fifteen domains listed with what each would be called for. Several gate work already in "
     "flight: the system-of-record admin for integration feasibility, revenue cycle for the "
     "LUPA and period questions, and state legal for the automated-contact question behind "
     "OI-07.", "TBD", "In Process"),
    ("OI-15", "DECISION", "13",
     "Confirm the as-run rubric section weights against the issued questionnaire",
     "The weight set on ‘Questionnaire & Rubric’ is the derived set, reconstructed for the "
     "record. Before it is shown to a steering committee it should be reconciled against the "
     "weights actually used to make the cut to six — and if they differ, the as-run set is the "
     "one that governs, with the difference noted.", "TBD", "Not Started"),
    ("OI-16", "BLOCKER", "16",
     "Lock the deep-dive script before any further sessions run",
     "The comparison only holds if all six vendors are asked the same things in the same order "
     "against the same scenarios. A script that evolves between session two and session five "
     "means the last three vendors were evaluated on a different instrument, and the scorecard "
     "cannot carry the cut to three.", "TBD", "In Process"),
    ("OI-17", "DECISION", "17",
     "Set the decision rule for the cut from six to three, and the on-site agenda",
     "Agree in advance what decides it — deep-dive score, the claimed-versus-demonstrated gap "
     "log, knockouts surfaced live — and in what order. Decided afterwards, it is a "
     "justification. The half-day agenda must then be identical for all three, or the finalist "
     "comparison has the same defect.", "TBD", "Not Started"),
    ("OI-18", "GATE", "12",
     "Confirm what may be shared with a vendor before the on-site sessions",
     "The reference pack deliberately exposed our process. The on-sites go further — real "
     "branch shapes, real volumes, real constraint detail. Agree now what is shareable under "
     "NDA and what is not, rather than in the room.", "TBD", "Not Started"),
]


def extend_open_items(wb):
    ws = wb["Open Items"]
    r = ws.max_row + 1
    for item in OPEN_ADDITIONS:
        body_row(ws, r, list(item), height=62.1, bold_cols=(1, 2),
                 center_cols=(1, 2, 3, 6, 7), shade=REDPALE)
        for col in (1, 2):
            ws.cell(row=r, column=col).font = Font(name="Calibri", size=10, bold=True,
                                                   color=RED)
        r += 1
    ws["A2"] = ("BLOCKERS are decisions or defects that make a deliverable wrong or "
                "unbuildable. GATES are validations never performed. OI-01…OI-11 are findings "
                "from the five-specialist QA review of 22 Aug 2026; OI-12…OI-18 come from arcs "
                "two and three — vendor selection and governance.")
    total = sum((ws.column_dimensions[get_column_letter(c)].width or 8.43)
                for c in range(1, 8))
    ws.row_dimensions[2].height = max(
        18.0, _wrapped_lines(ws["A2"].value, total * 1.05) * 12.6 + 8)
    return r


# ══════════════════════════════════════════════════════════════════════════════
# main
# ══════════════════════════════════════════════════════════════════════════════

ORDER = [
    "Approach — 10 Steps",
    "Vendor Selection",
    "Questionnaire & Rubric",
    "Governance & People",
    "Overall Project",
    "Initiative Framework",
    "Document Register",
    "Open Items",
]


def main():
    wb = load_workbook(BASE)

    refresh_approach(wb)
    build_vendor_tab(wb, 1)
    build_rubric_tab(wb, 2)
    build_governance_tab(wb, 3)
    extend_house_plan(wb)
    build_framework_tab(wb, 4)
    extend_register(wb)
    extend_open_items(wb)

    for name in ("Vendor Selection", "Questionnaire & Rubric", "Governance & People",
                 "Initiative Framework", "Document Register", "Open Items"):
        autofit_rows(wb[name], 5, wb[name].max_row)

    for name, last_col in (("Vendor Selection", "G"), ("Questionnaire & Rubric", "G"),
                           ("Governance & People", "E"), ("Initiative Framework", "F"),
                           ("Document Register", "F"), ("Open Items", "G"),
                           ("Approach — 10 Steps", "H")):
        print_setup(wb[name], last_col)

    # Final tab order: the eight narrative tabs, then every inherited tab as it was.
    front = [wb[name] for name in ORDER]
    rest = [ws for ws in wb.worksheets if ws not in front]
    wb._sheets = front + rest
    wb.active = 0

    wb.save(OUT)
    print(f"wrote {OUT}")
    for i, ws in enumerate(wb.worksheets):
        print(f"  {i:2d}  {ws.title}")


if __name__ == "__main__":
    main()
