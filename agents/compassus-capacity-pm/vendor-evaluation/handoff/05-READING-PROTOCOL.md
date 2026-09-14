# 05 · The reading protocol

The procedure for one returned questionnaire, then how sixteen are handled. Follow it in order.
The output is the brief in `06-BRIEF-TEMPLATE.md`.

---

## Step 0 · Intake

Returns arrive as the questionnaire xlsx, in every state of repair: merged cells, answers on the
wrong row, a Word document attached instead of the form filled in.

The unit you read is a **transcript**, not the xlsx: one flat text file, one block per question id in
form order, headed by the vendor name, who completed it, the form version, and a short fingerprint of
the file. At the end, an appendix of every non-empty cell that did not map to a question, so nothing
is silently lost.

- **Preferred:** the PM runs `extract_return.py` on each file and gives you the transcript.
- **Fallback:** you are given the xlsx. Produce the transcript yourself as your first output, show
  it, and only then read. Extraction mistakes must become visible before they become highlights.

Confirm three things before reading: the vendor name, the form version (must be `2026-08-19`), and
that the pack's version stamp matches the workbook.

## Step 1 · Cold read

Read the whole transcript once without tagging anything. Write three lines only:

1. What they lead with. The first answer tells you what they think they are.
2. Where the register changes. Which sections read like a mechanism, which like a brochure.
3. What they raised that we did not ask.

## Step 2 · Per-question pass

For every item in form order, apply the five tags from the template: **FACT**, **CLAIM**, **RED
FLAG**, **GOLD**, **ASK**. Every tag line carries a verbatim quote of at most twenty-five words with
the question id. Nothing untagged is reported; nothing tagged is unquoted.

Use `04-QUESTION-GUIDE.md` for what to look for. Run both catalogues against every answer and cite the
id (`RF-07`, `G-03`), so a flag is a pattern match and not an opinion. Where a pattern is new, say so
and propose it for the catalogue; do not invent an id.

For each Section B row, list the spec elements the return actually evidences (a B claim plus C
support) and the ones absent. Count the areas claimed in scope and the areas Section C supports.

## Step 3 · The seven cross-checks

The part a human skims past at vendor twelve. Each produces a FACT, a RED FLAG, or *consistent*.

1. **A1 against Section C.** Does the integration story hold? Bi-directional claimed; file drop,
   one-way read, screen automation or an unnamed partner described? Is a conflict rule for two systems
   owning the schedule stated anywhere?
2. **Section B against Section C.** Areas marked in scope, against areas C describes a mechanism for.
   Report both numbers. A wide gap is the Wayfinder pattern in `09-CALIBRATION.md`.
3. **A2 against A3.** Impact claimed from how many customers, with a baseline and a period, or not.
4. **D1 and D2 against C2 and C4.** Does the clinician's stated control match the engine's described
   behaviour? Is there a *runs it* where we set an assist boundary?
5. **E2 against E4 and E1.** Partnership language, against candour, against whether they understood
   our problem.
6. **C6.** Uptime figure, outage story, contractual commitment: present, partial or absent. Does it
   mention HCHB?
7. **Scale coherence.** A1 customer count, A2 customer count, A3 site count, D3 six-month data, E3
   named deployments. These five must reconcile.

Close with one line on who wrote this, with the evidence: named constraints, numbers, and whether
*we don't do that* appears anywhere.

## Step 4 · The brief

Write the brief per `06-BRIEF-TEMPLATE.md`. First screen for the leader, the rest for the PM. Then
the paste blocks, in the workbook's own shapes.

Mark every GOLD item *(provisional)*. Gold that turns out to be on five briefs is not gold, and only
the field pass can tell.

Stop. Do not begin another vendor in this conversation.

---

## Sixteen vendors

**One conversation per vendor.** Vendor nine is not read through vendor eight.

**Then one field conversation** that reads the sixteen briefs, not the transcripts, and produces
`FIELD-COMPARISON.md`:

- A vendor-by-column matrix: A1 rung evidence, B claimed versus C supported, stop-checks, gold count,
  one-line differentiator, who-wrote-this read, extraction quality.
- The **commonplace list**: anything on five or more briefs. It is struck from every GOLD list; the
  rubric's own rule is that anything on five vendors' lists is not a differentiator.
- The **singular list**: things only one vendor said.
- Field-wide asks: the demo script.
- Pairs worth reading head to head.

The field pass emits a per-vendor delta (*strike G-01 from Arbor; it appeared on nine briefs*) rather
than regenerating sixteen briefs.

## Handing off to the PM

The PM pastes; the PM picks the dropdowns. Every brief ends with:

- **Eight section note cells**, in the workbook's `ID: note` line style: Section A, Capacity,
  Scheduling, Engagement, Section C, Section D, Section E, Intangibles.
- **The three closing rows**: what stands out, what worries me, what to go and ask.
- **The Questions tab**: six sections, three slots each. Overflow listed beneath and marked as such.

## What you never produce

A total. A band. A rank. A mark on Clinician fit or an intangible. A quote without an id. A sentence
about the vendor that is not anchored in the transcript.
