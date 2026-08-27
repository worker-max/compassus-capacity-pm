# -*- coding: utf-8 -*-
"""Building Tomorrow's Day — what the clinician considers for every patient on the caseload.

Foundation sheet for the patient-scheduling engagement maps. Canvas units = points.

The unit is one clinician, one evening, one caseload. Eight questions get asked about every
patient before tomorrow exists. Seven of the answers are on a screen; one is only on the phone,
and that one is why the whole pass happens the night before.
"""
import sys
import textwrap

C = dict(pcc="#C6A01F", hchb="#795CA7", dcs="#792E2E", clin="#2E599D",
         auth="#DF751D", intake="#1F6F78", lead="#1A1A1A", pat="#4E8A5B")
INK, MUT, RULE, BAND = "#1B211E", "#5A6560", "#C9CCC5", "#E9E9E5"
PAPER, ENG, ENGD = "#FBFBF8", "#A6E22E", "#5F8A12"

W, H = 2600, 1390
CASELOAD = 16
out = []
def add(s): out.append(s)
def esc(t): return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def lbl(x, y, t, anchor="start", cls="lb"):
    add(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{esc(t)}</text>')

def block(x, y, w, h, fill, lines, small=False, tc="#fff"):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>')
    lh = 15.5 if small else 19
    cls = "bt s" if small else "bt"
    cy = y + h/2 - (len(lines)-1)*lh/2 + (5 if small else 6)
    for i, ln in enumerate(lines):
        add(f'<text x="{x+w/2}" y="{cy+i*lh}" class="{cls}" style="fill:{tc}" '
            f'text-anchor="middle">{esc(ln)}</text>')

add(f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg">')
add(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
add('<style>'
    '.chp{font-family:var(--mono),monospace;font-size:12.5px;font-weight:700;'
    'letter-spacing:.04em;fill:#fff}'
    '.xs{font-family:var(--mono),monospace;font-size:15px;font-weight:700;fill:#792E2E}'
    '.kh{font-family:var(--body),sans-serif;font-size:14.5px;font-weight:700;fill:#1B211E}'
    '.q{font-family:var(--body),sans-serif;font-size:15px;fill:#1B211E}'
    '.tier{font-family:var(--mono),monospace;font-size:15px;font-weight:700;'
    'letter-spacing:.14em;fill:#1B211E}'
    '.big{font-family:var(--display),serif;font-size:44px;font-weight:600;fill:#1B211E}'
    '.pchip{font-family:var(--mono),monospace;font-size:12px;fill:#5A6560}'
    '</style>')
add('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
    'markerHeight="7" orient="auto">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{INK}"/></marker></defs>')

# ---------------- header ----------------
lbl(50, 62, "COMPASSUS HOME HEALTH  ·  PATIENT SCHEDULING  ·  FOUNDATION SHEET", cls="eyebrow")
lbl(50, 104, "Building Tomorrow's Day", cls="title")
lbl(50, 132, "What the clinician considers for every patient on the caseload — and what happens "
             "when the answers have to fit into one day", cls="deck")
lx = 1580
for nm, col in [("HCHB", C["hchb"]), ("The order", C["dcs"]), ("Clinician", C["clin"]),
                ("Patient", C["pat"]), ("Geography", C["pcc"]), ("Branch", C["lead"])]:
    add(f'<circle cx="{lx}" cy="58" r="9" fill="{col}"/>')
    lbl(lx+16, 63, nm, cls="leg")
    lx += 8.6*len(nm) + 50
lbl(W-50, 104, "COLOUR = WHERE THE ANSWER LIVES", "end", "colh")
add(f'<line x1="50" y1="158" x2="{W-50}" y2="158" stroke="{RULE}" stroke-width="1.4"/>')

BX0, BXW = 330, 2220

# ================= the caseload =================
TY = 190
lbl(72, TY+30, "TONIGHT", cls="tier")
lbl(72, TY+52, "tomorrow does not exist yet", cls="sub")
cw2 = (BXW - 15*14) / CASELOAD
for i in range(CASELOAD):
    x = BX0 + i*(cw2+14)
    add(f'<rect x="{x}" y="{TY+16}" width="{cw2}" height="44" rx="7" fill="#FFFFFF" '
        f'stroke="{RULE}" stroke-width="1.6"/>')
    lbl(x+cw2/2, TY+43, f"patient {i+1}", "middle", "pchip")
lbl(BX0, TY+82, "one clinician · one caseload · every visit for tomorrow still to be placed",
    cls="sub")

# ================= the eight questions =================
TY = 310
TH = 340
add(f'<rect x="50" y="{TY}" width="{W-100}" height="{TH}" rx="10" fill="{BAND}"/>')
lbl(72, TY+36, "ASKED ABOUT", cls="tier")
lbl(72, TY+58, "EVERY PATIENT", cls="tier")
lbl(72, TY+82, "one at a time,", cls="sub")
lbl(72, TY+99, "before any of it", cls="sub")
lbl(72, TY+116, "can be placed", cls="sub")
lbl(W-72, TY+36, "EIGHT QUESTIONS  ·  NONE OF THEM OPTIONAL", "end", "bandhi")

Q = [
 (["Frequency"], C["dcs"], "Do I owe this patient a visit tomorrow?",
  "Ordered 2x a week — how many are already done, how many days are left.",
  "HCHB · the 485"),
 (["Regulatory", "timing"], C["hchb"], "Is a window binding on this one?",
  "SOC OASIS inside 48 hours. The recert visit in the last 5 days of the period.",
  "HCHB"),
 (["MD orders"], C["dcs"], "What does the visit have to include?",
  "Wound care every 3 days. Labs before the MD appointment. Protocol timing.",
  "The 485"),
 (["How urgent"], C["clin"], "Can this patient safely wait a day?",
  "How they looked last visit. Wound status. Whether the family sounded worried.",
  "Last visit · my memory"),
 (["Care team"], C["hchb"], "Is another discipline going this week?",
  "PT was Monday. If I go tomorrow the patient has two visits and then nothing.",
  "HCHB calendar"),
 (["Patient", "availability"], C["pat"], "When can they actually be seen?",
  "Dialysis days. Caregiver hours. Appointments. “Not first thing.”",
  "A PHONE CALL"),
 (["Geography"], C["pcc"], "Where are they, and who is near them?",
  "Drive time, not distance. Which other patients fall on the same run.",
  "HCHB address · the roads"),
 (["What it costs"], C["lead"], "What will this visit take out of my day?",
  "Points, and the honest minutes — visit, drive, and the documentation after.",
  "HCHB points · experience"),
]
n = len(Q)
gap = 24
bw = (BXW - (n-1)*gap) / n
for i, (lines, col, q, detail, src) in enumerate(Q):
    x = BX0 + i*(bw+gap)
    by = TY + 72
    add(f'<circle cx="{x+16}" cy="{by-10}" r="13" fill="#FFFFFF" stroke="{col}" stroke-width="2"/>')
    lbl(x+16, by-5, str(i+1), "middle", "bdg")
    block(x, by, bw, 52, col, lines, small=True)
    yy = by + 78
    for ln in textwrap.wrap(q, 26):
        lbl(x, yy, ln, cls="kh"); yy += 18
    yy += 8
    for ln in textwrap.wrap(detail, 30):
        lbl(x, yy, ln, cls="sub"); yy += 16
    hot = src == "A PHONE CALL"
    sy = TY + TH - 46
    add(f'<rect x="{x}" y="{sy}" width="{bw}" height="30" rx="6" '
        f'fill="{"#F4FBE6" if hot else "#FFFFFF"}" stroke="{ENGD if hot else RULE}" '
        f'stroke-width="{2.2 if hot else 1.3}"/>')
    lbl(x+bw/2, sy+20, src, "middle", "bdg" if hot else "vid")
lbl(BX0, TY+TH-56, "WHERE THE ANSWER LIVES", cls="key")

# ================= the multiplication =================
TY = 680
TH = 150
add(f'<rect x="50" y="{TY}" width="{W-100}" height="{TH}" rx="10" fill="none" '
    f'stroke="{ENGD}" stroke-width="2"/>')
lbl(100, TY+64, f"8 questions  ×  {CASELOAD} patients", cls="big")
lbl(100, TY+96, f"≈ {8*CASELOAD} judgments before tomorrow exists — every evening, "
                f"on the clinician's own time", cls="kh")
add(f'<line x1="820" y1="{TY+24}" x2="820" y2="{TY+TH-24}" stroke="{RULE}" stroke-width="1.6"/>')
lbl(870, TY+48, "Seven of the eight answers are already on a screen.", cls="kh")
lbl(870, TY+72, "The eighth is only on the phone — and that single call is why the whole pass "
                "happens the night before, after hours,", cls="sub")
lbl(870, TY+90, "one patient at a time. It is also the only point in the day where the patient "
                "has any say in when they are seen.", cls="sub")
add(f'<rect x="870" y="{TY+104}" width="640" height="28" rx="6" fill="#F4FBE6" '
    f'stroke="{ENGD}" stroke-width="2"/>')
lbl(1190, TY+123, "THIS IS WHERE THE ENGAGEMENT MAPS ATTACH", "middle", "bdg")

# ================= the collisions =================
TY = 860
KH = 320
add(f'<rect x="50" y="{TY}" width="{W-100}" height="{KH}" rx="10" fill="none" '
    f'stroke="{C["dcs"]}" stroke-width="2"/>')
lbl(72, TY+36, "THEN THE ANSWERS HAVE TO FIT INTO ONE DAY  —  six that recur every week",
    cls="pnl")
lbl(W-72, TY+36, "ONE PERSON RESOLVES ALL SIX, ALONE, THE NIGHT BEFORE", "end", "bandhi")

COL = [
 (("Patient availability", C["pat"]), ("Patient availability", C["pat"]),
  "Two patients, one 2pm",
  "Both can only be seen after lunch. One of them moves to another day."),
 (("Patient availability", C["pat"]), ("Geography", C["pcc"]),
  "The cluster breaks",
  "The 2pm patient is 40 minutes from the rest of the run. The day loses an hour."),
 (("Frequency", C["dcs"]), ("Care team", C["hchb"]),
  "PT and OT both ordered 2x",
  "Both want the same two days. The patient gets two visits, then nothing."),
 (("How urgent", C["clin"]), ("What it costs", C["lead"]),
  "The unstable patient runs long",
  "Ninety minutes, same points as forty. Everything after it slides."),
 (("MD orders", C["dcs"]), ("Patient availability", C["pat"]),
  "Wound care q3d, caregiver weekends",
  "The order and the caregiver's hours do not overlap. Agreed on the phone, recorded nowhere."),
 (("Frequency", C["dcs"]), ("Regulatory timing", C["hchb"]),
  "Recert week, 3x ordered",
  "The LUPA floor, the ordered frequency and the recert window all bind at once."),
]
cw = (W - 144 - 5*18) / 6
for i, ((a, ca), (b, cb), head, tail) in enumerate(COL):
    x = 72 + i*(cw+18)
    y = TY + 64
    add(f'<rect x="{x}" y="{y}" width="{cw}" height="26" rx="13" fill="{ca}"/>')
    lbl(x+cw/2, y+18, a, "middle", "chp")
    lbl(x+cw/2, y+50, "\u2715", "middle", "xs")
    add(f'<rect x="{x}" y="{y+58}" width="{cw}" height="26" rx="13" fill="{cb}"/>')
    lbl(x+cw/2, y+76, b, "middle", "chp")
    yy = y + 118
    for ln in textwrap.wrap(head, 24):
        lbl(x+cw/2, yy, ln, "middle", "kh"); yy += 18
    yy += 8
    for ln in textwrap.wrap(tail, 31):
        lbl(x+cw/2, yy, ln, "middle", "sub"); yy += 16
lbl(72, TY+KH-22, "None of these are visible until the clinician tries to place the last patient "
    "\u2014 by then the first seven are already committed.", cls="hi")

# ================= what comes out =================
TY = 1215
add(f'<line x1="50" y1="{TY}" x2="{W-50}" y2="{TY}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(72, TY+42, "WHAT COMES OUT", cls="trg")
block(310, TY+18, 480, 64, C["clin"], ["Tomorrow's day", "— and a list of who got moved"],
      small=True)
add(f'<line x1="812" y1="{TY+50}" x2="{"%d" % 866}" y2="{TY+50}" stroke="{INK}" '
    f'stroke-width="2" marker-end="url(#ar)"/>')
lbl(890, TY+42, "THE RESIDUE", cls="trg")
lbl(890, TY+66, "Who was called and put off · what the caregiver agreed to · why the cluster "
    "broke · which visit is now at risk of the LUPA floor.", cls="sub")
lbl(890, TY+86, "None of it is written down, so tomorrow evening the same eight questions get "
    "asked again with no memory of tonight's answers.", cls="sub")

add(f'<line x1="50" y1="{H-58}" x2="{W-50}" y2="{H-58}" stroke="{RULE}" stroke-width="1.4"/>')
lbl(50, H-30, "FOUNDATION SHEET · patient scheduling · caseload size shown as a "
    "representative 16", cls="foot")
lbl(W-50, H-30, "Building tomorrow's day", "end", "foot")
add('</svg>')

OUT = sys.argv[1] if len(sys.argv) > 1 else "day.svg"
open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("emitted", len(out), "| canvas", W, "x", H, "| ratio", round(W/H, 3))
