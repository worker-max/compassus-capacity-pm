# Compassus brand — the reference for anything we hand to the business

Read this before building any document, deck, workbook or page that leaves the team.

**Where this came from.** The logo and its two colours were extracted from the Compassus logo
asset embedded in `Home_Health_101_1.pptx`, supplied by the PM on 2026-09-07, and the colours were
sampled from the logo's own pixels. **Those two colours are the only facts here.** Everything below
them is the supporting palette that deck already used, recorded so our documents stay consistent
with it — not an official Compassus brand standard. **If Compassus marketing publishes a real brand
guide, it wins and this file gets replaced.**

---

## The mark

| File | Use it for |
|---|---|
| `compassus-logo.png` | 609 × 234, **transparent background**, trimmed. The default. Print, PDF, decks, anything on a light ground |
| `compassus-logo-320.png` | 320 × 123, transparent. Screen, and anywhere the full-size file is wasteful |
| `compassus-logo.datauri.txt` | The 320px file as a `data:` URI, one line. **Artifacts and published HTML pages need this** — the artifact sandbox blocks external images, so the mark has to be inlined |

**Rules.** Never recolour it, never stretch it, never put it on a mid-tone or busy ground, never set
it below about 120px wide (the ® stops resolving). Leave clear space around it of at least the
height of the *C*. The heart sits to the upper right of the wordmark and is part of the mark — do
not use it alone, and do not use the wordmark alone.

## The two brand colours

Sampled from the logo. These are the ones to be exact about.

| Name | Hex | What it is |
|---|---|---|
| **Compassus Navy** | `#182752` | The wordmark. Primary. Headings, rules, the dark ground |
| **Compassus Gold** | `#F0A91B` | The heart. **An accent, never a background and never body text** — it is the one warm mark on a cool page |

Navy on white is 13.6:1 — passes AA and AAA at any size. **Gold on white is 2.0:1 and fails
everything**: use it for a rule, a dot, a keyline or a fill behind navy text, never for text on a
light ground.

## The supporting palette

What `Home_Health_101_1.pptx` actually used, by frequency. Consistent with the mark, and the set to
draw from so our documents look like each other.

| Role | Hex | Notes |
|---|---|---|
| Navy, working | `#253356` | The deck's text navy — a touch lighter than the logo. Fine for body headings |
| Ink | `#1F2430` | Body text |
| Muted | `#6E7683` | Secondary text, captions, keys |
| Rule | `#DCE0E6` | Hairlines and table borders |
| Rule, stronger | `#C7CCD4` | Section rules |
| Paper | `#F4F6F8` | Page ground |
| Band | `#EDEFF2` | Table band and header fills |
| Blue | `#3D5FB4` | **Scheduling** |
| Teal | `#0E8F80` | **Capacity** |
| Gold | `#F2A900` | The deck's working gold. Prefer the logo's `#F0A91B` where the mark is present |
| Amber | `#D97706` | Warning, a step down from maroon |
| Maroon | `#B23B3B` | **A gap, a flag, a stop-check** |

## Type

The deck is set entirely in **Calibri**, which is the Office default rather than a brand choice —
it is what the template gave, not what anyone picked. **Do not treat Calibri as the brand face.**

Use the house stack, which is a deliberate choice and reads better:

- **Serif, for display:** Iowan Old Style → Source Serif 4 → Georgia
- **Sans, for text and UI:** Avenir Next → Mulish → system sans
- **Mono, for keys, labels and data:** SF Mono → IBM Plex Mono

In a `.pptx` or `.docx` that a Compassus colleague will open and edit on a Windows machine, set
Calibri — a font they do not have will substitute badly and that is worse than a plain face.

## How this relates to the house design system

`.claude/skills/process-flow-map/reference/design-system.md` defines the house palette we build
internal artefacts in: ink `#1B211E`, muted `#5A6560`, rule `#C9CCC5`, paper `#FBFBF8`, teal
`#1F6F78`, blue `#2E599D`, green `#4E8A5B`, maroon `#792E2E`, gold `#9A7B15`.

The two are siblings, not rivals. The house system is warm-grey and quiet; the Compassus palette is
cool-navy and corporate. The arena colours line up one-to-one — teal is capacity, blue is
scheduling, maroon is a flag — so a document can be moved from one to the other by swapping the
tokens and nothing else.

**Which to use.** House palette for working artefacts the team lives in: flow maps, scorecards,
research matrices, internal drafts. **Compassus palette, with the mark, for anything that goes to a
Compassus audience outside the team** — the leader's read-out, an executive brief, a business case,
a vendor-facing document. When in doubt, ask which room it will be read in.

## The one thing to get right

The mark is the only piece of this file that is unambiguously Compassus's. Use it accurately and
sparingly — once, at a known size, in a known place — and the rest of the page can be ours.
