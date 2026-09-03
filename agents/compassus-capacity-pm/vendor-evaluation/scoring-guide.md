# Vendor Scoring Guide

**Compassus Home Health · Capacity & Scheduling Platform**
Scoring the returned vendor questionnaires (form_version 2026-08-19) · 16 vendors → a shortlist.

---

## The one idea

**Every part of the score is a percentage times the points it is worth.**

That is the whole system. Score the items, take the percentage, multiply by the points that
part is worth. Nothing is hidden, nothing needs a formula anyone has to trust blindly, and two
people scoring the same questionnaire should land within a few points of each other.

There is exactly one exception, and it is deliberate: **HCHB integration is a checkbox ladder,
not a judgment.** You pick the rung. That is how the leadership priority gets protected from
scoring drift.

---

## The five parts

| # | Part | Points | Answered from |
|---|---|---:|---|
| 1 | **HCHB Integration** | **25** | A1 |
| 2 | **Scope Footprint** | **30** | Section B + Section C |
| 3 | **Sophistication** | **20** | Section C, plus A2/A3 |
| 4 | **Clinician & Adoption** | **10** | Section D |
| 5 | **Partnership** | **15** | Section E |
| | **Total** | **100** | |

Alongside the number, every scorecard carries three things that are *not* scored but decide
almost as much: **Differentiators**, **Flags**, and **Unknowns**. See [§6](#6-what-is-not-scored).

---

## 1 · HCHB Integration — 25 points

The single biggest weight on the sheet, and the only part that is a checkbox. Tick **one** rung
from A1. If the answer is ambiguous, tick the lower rung and raise a flag — do not average.

| Pts | Rung | What A1 has to show |
|---:|---|---|
| **25** | **Live, bi-directional, multi-customer** | In production with more than one customer today, reads *and* writes HCHB, over a published API / HL7 / FHIR. Names a go-live date. |
| **20** | **Live, single customer or one-way** | In production, but with one customer only, or it reads from HCHB without writing back. |
| **12** | **Live via a partner or a brittle method** | Delivered through a third party, or implemented by flat file, direct database access, or screen automation. Works today; carries maintenance and risk. |
| **6** | **In development, dated** | Not live, but building, with a committed target date in the answer. |
| **2** | **Roadmap, undated** | Named as intent. No date, no commitment. |
| **0** | **None, and no path** | No integration and no credible route to one. |

**Why it is worth a quarter of the score.** HCHB is where the plan of care, the orders, the
authorization state and the visit record already live. A platform that cannot read and write it
either duplicates that data or asks schedulers to work two systems — which is the cost this
initiative exists to remove.

> **Scoring note — sync latency.** A1 asks how the vendor handles data changing on both sides.
> An answer that ignores it does not change the rung — but raise a flag. Two systems that both
> believe they own the schedule is the failure mode that hurts most.

---

## 2 · Scope Footprint — 30 points

This is the part that reads their free text back against **our** one-pager. The Overview tab
specifies **41 elements** across the three arenas. Mark each one from what they actually said.

| Mark | Value | Means |
|---|---:|---|
| **Covered** | 1.0 | The product does this today. Stated plainly, or evidenced in a Section C walkthrough. |
| **Partial** | 0.5 | Adjacent, configurable-with-work, delivered by a partner, roadmapped with a date, or claimed without any supporting detail. |
| **Not covered** | 0 | Absent, explicitly out of scope, or done by a person in their model. |

Then, per arena:

```
footprint %  =  marks ÷ elements
points       =  footprint % × 10
```

| Arena | Elements | Points |
|---|---:|---:|
| Capacity Management | 11 | 10 |
| Scheduling Engine | 14 | 10 |
| Engagement | 16 | 10 |
| **Overall footprint** | **41** | **30** |

Equal pointss, unequal element counts — on purpose. A vendor that covers all three arenas
shallowly and one that owns scheduling completely and ignores engagement should not be able to
tie by accident. The three percentages get reported separately on every scorecard, because
*which* arena a vendor covers is more useful to us than the total.

**Rules that keep this honest:**

1. **A vendor's own Section B answer is enough to mark Covered.** They were given a dropdown and
   a small notes box, not room for an essay. Do not demote a plain claim for lacking
   elaboration — that penalises the form, not the product. Note the follow-up question instead.
2. **Section C overrides Section B only where the two contradict.** If C describes something
   narrower than B claimed, believe C and say why.
3. **"Configurable" is not "covered."** Neither is an open API, a dated roadmap item, or an area
   marked in-scope that they did not claim to have. Those are Partial because the answer itself
   says so.
4. **A partner delivering it is Partial**, and gets a flag naming the partner.
5. **ENG-01 and ENG-02** (agentic outreach; staff able to take the conversation back) have no
   Section B area of their own. Score them from **C7** and **D1**.

---

## 3 · Sophistication — 20 points

**How much of the work the product actually does.** Part 2 counts *what* a vendor has;
this measures *how advanced it is*.

This is the category leadership asked for by name, and it is the one that separates two vendors
who both tick the same boxes — one that shows a scheduler a number, and one that works out the
answer and acts on it.

### The capability scale (0–4)

The same **Read / Assist / Control** language already in the primary workbook's Functional
Scorecard, on five rungs.

| | | |
|---:|---|---|
| **0** | Not addressed | They do not do this, or did not say. |
| **1** | **Shows it** | Surfaces the information. A person does all the work. *(Read)* |
| **2** | **Checks it** | Applies rules and flags problems. A person still works it. |
| **3** | **Recommends it** | Works out the answer and proposes it. A person confirms. *(Assist)* |
| **4** | **Runs it** | Decides across the whole picture, and re-decides when things change. *(Control)* |

> **Score the product, not the write-up.** A three-sentence answer saying the engine optimises
> across drive time, continuity and capacity together is a **4**. We deliberately do not reward
> a vendor for explaining their internals at length, or punish one for brevity: the questionnaire
> did not give room for it, and *"how does that work?"* is a demo question, not a scoring penalty.
> If a claim seems thin, mark what they claimed and put the follow-up on the unknowns list.

### The five questions

| # | Item | From | Asks |
|---|---|---|---|
| S1 | **Capacity** | C1 | How much does it do to work out what a branch can take on? |
| S2 | **Assignment** | C2 | How much does it do to decide which clinician takes a visit? |
| S3 | **The week** | C4 | How much does it do across a week or an episode, not just a day? |
| S4 | **Readiness** | C3 | How much does it do with a visit ordered but not yet schedulable? |
| S5 | **Recovery** | C5 | How much does it do when the plan breaks? |

```
points = (S1+S2+S3+S4+S5) ÷ 20 × 20
```

> **A 4 is not automatically what we want.** Where we set an *Assist* boundary, a product that
> decides on its own is a risk to note — the same overreach idea the Functional Scorecard already
> uses. Score the capability honestly; raise the overreach as a flag.

### Three questions that deliberately do not reach the score

**A2** (customers and scale), **A3** (measured impact) and **C6** (what happens when they are
down) raise **flags** instead of losing points. A vendor with no continuity commitment should be
stopped and asked, not quietly docked four points — and a vendor whose impact numbers have no
baseline needs a conversation, not an arithmetic penalty.

## 4 · Clinician & Adoption — 10 points

The questionnaire says it outright: adoption, more than algorithm quality, decides whether this
succeeds. Three items, on the **fit scale** — clinician and partnership are not capability
questions.

| | | |
|---:|---|---|
| **0** | Not addressed | Skipped, or answered without answering. |
| **1** | Poor fit | What they described works against how we need to operate. |
| **2** | Workable | We could live with it. |
| **3** | Good fit | Matches how we want to work. |
| **4** | Strong fit, proven elsewhere | Matches, and they have done it with a customer already. |

| # | Item | From |
|---|---|---|
| D1 | **What the clinician decides** — what they can change, what needs approval, what is locked, and whether disagreement changes anything | D1 |
| D2 | **Decide or advise** — where it was designed to sit, and how much a customer can move it | D2 |
| D3 | **Adoption evidence** — how they measure it, what healthy looks like, six-month data, and what a clinician sees about their own results | D3 |

```
points = (D1+D2+D3) ÷ 12 × 10
```

A product that decides everything and lets a clinician change nothing scores low here **and**
takes a red flag — regardless of how elegant the algorithm is.

---

## 5 · Partnership — 15 points

Compassus is bringing a dedicated optimization team, SME time, design partnership, an enterprise
deployment and co-marketing. This part measures whether the vendor is set up to trade on that.

Same fit scale.

| # | Item | From |
|---|---|---|
| P1 | **Sharing in the value** — a concrete proposal, not enthusiasm | E2 |
| P2 | **Deployment & change management** — approach, what they learned, and the resistance story with what they changed | E3 |
| P3 | **What we did not ask** — do they understand our problem better than our questions did? | E1 |
| P4 | **What they chose not to build** — product judgment and candour | E4 |

```
points = (P1+P2+P3+P4) ÷ 16 × 15
```

> **E2 is the one to read closely.** A vendor offering design-partner pricing, a co-development
> lane, equity or revenue share, or roadmap governance is proposing a partnership. A vendor
> offering a discount is proposing a discount. Both are legitimate; only one is what we asked
> for. An offer with structure and terms is a 3–4; "we're open to
> discussing" is a 1.

---

## 6 · What is not scored

The three columns that will decide more conversations than the totals do.

### ⭐ Differentiators
A concise list — **three to five bullets, one line each** — of what this vendor does that the
others do not. Two kinds count:

- **Against the field** — capability, mechanism, evidence, model, or reach nobody else showed.
- **Against our thinking** — something they raised that is not on our one-pager and probably
  should be. E1 and E4 are the richest source. These are the answers worth reading twice.

Anything that appears on five vendors' lists is not a differentiator. Cut it.

### 🚩 Flags
Facts that change a decision, carried next to the score rather than buried in it.

| | Stop-check — resolve before advancing |
|---|---|
| 🔴 | No HCHB integration and no credible path |
| 🔴 | No uptime figure, no outage story, or no contractual commitment (C6) |
| 🔴 | The system decides and the clinician cannot override (D1) |
| 🔴 | One customer, or no willingness to provide references (A2) |
| 🔴 | Core scope delivered by an unnamed third party |

| | Watch — note it, keep going |
|---|---|
| 🟡 | Home health is a minority of their business (A2) |
| 🟡 | Impact claimed with no baseline or period (A3) |
| 🟡 | Section C answered in marketing language rather than mechanism |
| 🟡 | Integration by flat file, database access or screen automation |
| 🟡 | No answer on sync latency, or two systems both owning the schedule |

### ❓ Unknowns
What we could not score because they did not answer. Explicit, and it becomes the demo agenda.
An unanswered question is a **0**, and it goes on this list — never a charitable guess.

---

## 7 · Bands and the shortlist rule

| Band | Score | What happens |
|---|---:|---|
| **Advance** | 80–100 | Demo, references, deeper diligence |
| **Consider** | 65–79 | Advance only if a differentiator or a low-cost gap-closer justifies it |
| **Hold** | 50–64 | Park unless the field thins |
| **Decline** | < 50 | Close out with thanks |

**The HCHB floor.** Any vendor scoring **under 12 on Part 1** lands in a **Conditional** band
regardless of total. They can still advance — but only on an explicit decision that names what
we are accepting: an integration to be built, on their timeline, at our risk. This is how the
leadership priority stays a priority without becoming a hard gate that eliminates a genuinely
better product.

**Ties break on Part 1, then Part 2 Scheduling.**

---

## 8 · Running it

**Ten minutes a vendor, once you have the rhythm.**

1. Read the whole questionnaire once, without scoring. Note what surprises you.
2. **Part 1** — tick the rung. One decision.
3. **Part 2** — walk the 41 elements. B for the claim, C for the evidence.
4. **Parts 3–5** — twelve items on the 0–4 ladder.
5. Write the three unscored lists: differentiators, flags, unknowns.
6. Enter the row in `Vendor-Scorecard.xlsx`. It does the arithmetic.

**Two people, independently, on the first three vendors.** Compare, argue, and write down what
you decided. Those decisions become house rules and the rest of the field goes faster and
straighter for them.

**Or run the skill.** `/vendor-scorecard` takes the returned file and produces the deep dive,
the summary, the footprints and a scorecard row in this exact rubric. Use it to do the first
pass and to check your own — not to replace the read. The skill is instructed to cite every
mark, so its scoring is auditable line by line.

---

## 9 · The honest limits

- **This scores a questionnaire, not a product.** It measures how well a vendor described
  themselves against our spec. Nothing here survives contact with a demo, a reference call or a
  sandbox — it is designed to pick *who gets those*, and nothing more.
- **It still rewards a clear answer over a vague one.** We have removed the places where length
  was rewarded — sophistication scores the product, and a plain Section B claim is enough for
  scope — but a vendor who answers a question ambiguously will score lower than one who answers
  it plainly. That is why the unknowns list sits next to the number: it names what to go and ask.
- **It cannot see price.** Deliberately. Commercials enter after the shortlist, so they do not
  colour the capability read.
- **41 elements is our spec, not the market's.** A vendor scoring low on footprint may simply
  have built a different, defensible product. The differentiator list is where that gets said.

---

*Rubric v1.0 · scored against questionnaire form_version 2026-08-19 · 41 spec elements from the
Overview tab.*
