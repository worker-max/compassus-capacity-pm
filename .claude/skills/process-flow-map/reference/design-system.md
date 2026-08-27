# The design system

## Colour = actor, and the person beats the system

| Actor | Hex | Notes |
|---|---|---|
| Intake | `#1F6F78` | Distinct from the auth team — they are different actors |
| Insurance & Auth | `#DF751D` | Also the colour for pending-auth / invisibility blocks |
| PCC / Scheduler | `#C6A01F` | |
| ED / DCS | `#792E2E` | |
| Clinician | `#2E599D` | |
| HCHB | `#795CA7` | **Only where the system acts by itself** |
| Per Diem / Float | `#795933` | |
| Patient | `#4E8A5B` | |
| Branch Leadership | `#1A1A1A` | White text |

Neutrals: ink `#1B211E` · muted `#5A6560` · rule `#C9CCC5` · band fill `#E9E9E5` ·
grey feeder tag `#E8EAED` · paper `#FBFBF8` · spine lane `#DBDBD6` at 55%.

**The rule that matters most:** a workflow item that lives in HCHB but is *worked by a person*
carries the person's colour. Purple is reserved for what HCHB does on its own — generating tasks,
applying rules, checking auth, suggesting a route. Colouring every in-system step purple hides human
labour, which is exactly the labour a capacity tool would relieve.

Corollaries that have already come up:
- The scheduler reads a coordination note someone wrote — that is a **scheduler** step, not a system step.
- HCHB does not send appointment reminders. Confirmation coordination is the **clinician's** work.
- Outcomes (revenue realized, capacity returned) are **white with an ink outline**, not an actor colour.
- A step two actors genuinely share is drawn **half and half** (`split_block`).

## Shape vocabulary

| Shape | Means |
|---|---|
| Rounded rect, actor-filled | A step someone performs |
| **Large** block | Happens every time |
| **Small** block (`small=True`) | Conditional |
| Pill / chip | A watch condition, trigger or state — *not* a step |
| Diamond, white + ink | A decision, whoever owns it |
| Oval | A terminus or outcome |
| Grey tag | An input or reference — data, not action |
| Badge above a block | A qualifier: `× N disciplines`, `ALL AT ONCE`, `GATE` |

**Size = weight.** If a rare condition is drawn as large as an every-time step, the page argues that
they matter equally. LUPA risk became a pill for exactly this reason.

## Type scale

All in the wrapper CSS; do not invent new classes without adding them there.

`.title` 34px display · `.deck` 16px · `.eyebrow` 13px mono tracked ·
`.bt` 16px block text (`.bt.s` 13.5px) · `.dt`/`.ct` 15px ·
`.band` 14px mono tracked (band headings) · `.bandhi` 14px blue (band right-side claim) ·
`.note` 14px · `.sub` 13.5px (the plain-language lists) · `.hi` 15px gold (the line that matters) ·
`.pnl` 13.5px maroon (panel headings) · `.colh`/`.colhb`/`.colhA` 12.5px (panel column heads) ·
`.trg` 12.5px (TRIGGER / BOUNDARIES side labels) · `.foot` 12.5px.

## The canvas rule — the one that breaks sheets

**Canvas units are points on the output sheet.** A 16-unit label prints at 16pt. Draw at sheet scale
— 2000–2900 units wide — and never at A4 scale intending to scale up: an A4-scale canvas prints its
block text at about 4.5pt, which is unreadable. Always landscape. Width follows content.

Typical: banded flow ≈ 2200 × 1550 · wide banded ≈ 2600 × 1780 · four-phase map ≈ 2450 × 1970.
Aim for a ratio between 1.25 and 1.5.

## Layout grammar

Two sheet shapes have proven out. Pick one, don't blend.

**Banded spine** (flows 1, 2, 3, 5 and the primary map) — horizontal bands, one per phase, each with
a mono heading on the left and a claim on the right (`NO SCHEDULER WORKFLOW`, `CHECKED PER VISIT, NOT
PER EPISODE`). Steps run left to right inside the band with plain-language sublists beneath. Below
the bands: a dashed reference panel, a `BOUNDARIES` chip strip, and a `WHERE IT BREAKS` row.

**Five-column swimlane** (the detailed composite) — outlined functional columns, a grey clean-path
lane running horizontally through the middle, feeders above it, recovery below it, centred title and
circle legend. This is the shape the team already knows how to read.

**Band widths follow their own content.** Ending every band at a common right edge makes the short
ones read half-empty. `band(..., slots=N, pad=P)` sizes each one to its last block.

## Sheet furniture

- **Masthead:** eyebrow (`COMPASSUS HOME HEALTH · FLOW N`), display title, deck line, hairline rule.
- **Legend:** filled circles + names, top right. Wrap to two rows past ~5 actors (`per_row=4`).
- **`TRIGGER`** side label + chip on the left of the first band.
- **Plain-language sublists** under steps — 2–4 items naming what the person is actually working
  around ("drive time, not distance"), never variable IDs. IDs go stale on a renumber; descriptions
  don't. `SHOW_VCHIPS` stays off until the inventory is settled.
- **One gold `.hi` line per band, at most** — the sentence you want remembered.
- **Footer:** *current state · nothing on this sheet is a proposal* on the left, sheet identity right.

## The one sheet that is a proposal

`Flow-Target-State` (22 Aug 2026) is the first and only sheet in the set that breaks
non-negotiables 1 and 2, deliberately and visibly:

- The eyebrow reads `TARGET STATE`, not `CURRENT STATE`.
- The footer is **inverted**: *this sheet IS a proposal — the only sheet in the set that is · every
  other sheet is current state.* A reader who has seen any other sheet must not have to guess.
- Every block carries **two markers in its badge**: the release that delivers it (`MVP` / `V2` /
  `V3`) and how far the system may go (`READ` / `ASSIST` / `CONTROL`). An unmarked block on a
  target-state sheet is an unbounded promise.
- It carries an **OPEN · NOT DRAWN** panel naming the design questions the operator still has to
  close. Boxes that would have been guesses are absent and *listed as absent* — the skill's rule
  about not filling a gap with a plausible box matters more here than anywhere, because a target
  state has no reality to be corrected against.

Everything else — palette, actor rule, size semantics, type scale, band grammar — is unchanged, so
current and target lay side by side and the delta is the only thing that reads as different.

**Do not treat this as licence for a second proposal sheet.** If another is ever drawn, it inherits
all four rules above.

## Non-negotiables

1. Every sheet is **current state**, including what is wasteful or manual, and says so in the footer
   — *except* `Flow-Target-State`, which says the opposite in its footer.
2. Nothing on a sheet is a proposal, with that one labelled exception.
3. One unbroken spine per sheet; exceptions hang off it, they don't interrupt it.
4. Solid connectors are the main path; dashed are exceptions, loops and feedback.
5. Same type scale across every sheet in the set, so they read as one system.
