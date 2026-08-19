# Business Case, KPIs and Vendor Fit

> **Source:** the `ROI & Finance Case`, `KPIs & Baseline`, `Functional Scorecard` and `Footprint & Fit`
> tabs of the **8.13 Compassus Capacity & Scheduling Workbook** — Google Drive
> `1tVEkPO2FJMFVyqLZP1TrzqbmjX0qEDgv`. **The workbook is authoritative;** this file is a read-only
> rendering so the numbers can be reasoned about offline. If a figure changes there, change it here —
> not the reverse. A dated CSV snapshot of every tab is in
> [`source/workbook-2026-08-13/`](./source/workbook-2026-08-13/).

---

## 1. The finance case

**Headline: `$7.9M / yr`** — modelled annual impact across ~80 branches, **Moderate** scenario, full
product.

| Scenario | Capacity/efficiency gain | Annual network impact |
|---|---:|---:|
| Conservative | 2% | **$4.0M** |
| **Moderate** *(the defensible planning number)* | 4% | **$7.9M** |
| Hopeful | 7% | **$14.3M** |

### Assumptions and drivers — every figure is computed from these

| Driver | Value |
|---|---:|
| Admissions per branch per year | 600 |
| Contribution margin per recovered admission | $1,200 |
| Premium (contract / PRN / overtime) labor pool per branch per year | $120,000 |
| Medicare 30-day payment periods per branch per year | 1,000 |
| Revenue protected per avoided LUPA | $1,400 |
| Clinician departures per branch per year | 5 |
| Replacement cost per clinician | $40,000 |
| Branch count (network) | 80 |
| MVP capture (share of full-product impact realised at MVP) | 0.60 |

| Scenario driver | Conservative | Moderate | Hopeful |
|---|---:|---:|---:|
| Capacity / efficiency gain | 2% | 4% | 7% |
| Premium-labor recovery | 15% | 30% | 50% |
| LUPA rate reduction (share of periods) | 0.5% | 1.0% | 2.0% |
| Clinician turnover reduction | 5% | 10% | 20% |

### Where the return comes from

| Source | Conservative | Moderate | Hopeful |
|---|---:|---:|---:|
| Recovered admissions (freed capacity) | $14,400 | $28,800 | $50,400 |
| Reduced premium / contract labor | $18,000 | $36,000 | $60,000 |
| Reduced LUPAs | $7,000 | $14,000 | $28,000 |
| Reduced clinician turnover | $10,000 | $20,000 | $40,000 |
| **Per branch, full product** | **$49,400** | **$98,800** | **$178,400** |
| **Per branch, MVP** | **$29,640** | **$59,280** | **$107,040** |
| **Network (~80 branches), full product** | **$3,952,000** | **$7,904,000** | **$14,272,000** |
| **Network (~80 branches), MVP** | **$2,371,200** | **$4,742,400** | **$8,563,200** |

> Figures are modelled from labelled, editable assumptions — **not guaranteed outcomes.**

### The argument, in the workbook's own frame

- **The schedule is the entire business, in one place.** Every referral dollar follows the same path:
  *referral (potential) → **capacity decision (the hinge)** → schedule (the plan) → visit (the only event
  that earns) → period revenue.* Everything upstream of the capacity decision is only potential.
- **Why the schedule fights back every hour.** A home visit is not one constraint but a dozen that must
  all be true at once — discipline and licensure match (SN, PT, OT, ST, MSW, HHA, none of which
  substitute for one another), authorization, LUPA thresholds, drive time, caregiver availability,
  continuity, acuity. **These constraints conflict.** Continuity fights geography; productivity fights
  acuity. And it is dynamic.
- **The spreadsheet-and-AI counter-proposal, taken seriously then retired.** The instinct that AI belongs
  in this problem is correct and the product uses it; the disagreement is about the *daily fresh sheet*:

  | The daily-sheet approach assumes… | …and here is why it breaks |
  |---|---|
  | A fresh sheet each morning is fine | **It has amnesia.** With no history it cannot trend, forecast, or prove ROI |
  | The AI can just optimise it | The real constraints — licensure, authorizations, LUPA thresholds, drive time, caregiver availability — are not in the sheet |
  | It produces the schedule, which is the goal | **The value is not the schedule, it is the measurement.** A capacity system answers *can we take this referral* |
  | An LLM reshuffling the day is low-risk | Scheduling clinical visits is a **high-harm** process — no constraint enforcement, no audit trail |
  | One clever person in Excel can run it | Does not scale nationally, does not survive turnover, creates no shared source of truth |

- **What we are deliberately not trying to solve.** *"The MVP does not build the schedule."* It gives
  schedulers and leaders visibility they have never had. **The first job of this product is not to
  optimise anything. It is to make capacity measurable and observable.** (Consistent with **DE-03**:
  Phase 1 is visualisation only.)
- **The same instrument extends to hospice.** Home health and home-based hospice solve one problem —
  the right clinician, the right patient, the right day. **Four hospice mechanics need rules added, not
  new products**, starting with interdisciplinary group (IDG) scheduling.
- **Why it compounds.** Every cycle it runs, it captures data the company has never systematically held.
  This is not a one-time optimiser, and there is a cost to waiting.

---

## 2. KPIs and baseline

Split into **Primary** (the scoreboard finance judges results by) and **Secondary** (leading indicators
that move first and explain the primaries). *One copy of the sheet is filled per branch, against a named
baseline period.*

### Primary — the scoreboard

| KPI | Unit | Lever | Lead/Lag | Source | Available today? |
|---|---|---|---|---|---|
| **Quantified capacity & utilisation** — measured maximum deliverable visits per week versus what is actually delivered. *The initiative's core metric* | % (and visits/wk) | Foundational | Leading | Scheduling + HR/staffing + visit-time standards (product-computed) | **No** |
| **Referral turn-down rate (no capacity)** — clinically appropriate referrals declined for lack of capacity | % (and admits / ADC) | Revenue | Lagging | Referral / intake system; turn-down log | **No** |
| **Premium / contract / overtime labor** — share of clinical labor delivered at a premium because capacity was not visible | % of labor cost (and $) | Cost | Lagging | Payroll / staffing | Partial |
| **LUPA rate & revenue leakage** — share of PDGM 30-day periods below threshold that forfeit full-period payment | % of periods (and $) | Revenue / Compliance | Lagging | EMR / billing (PDGM) | Partial |
| **Clinician turnover** — annualised attrition and replacement cost | % annualised (and $) | Cost | Lagging (slow) | HR | Yes |

### Secondary — the leading indicators

| KPI | Unit | Lever | Lead/Lag | Available today? |
|---|---|---|---|---|
| Time to start of care (SOC), against the 48-hour standard | hours (median) | Revenue / Quality | Leading | Partial |
| Missed / rescheduled visit rate | % of scheduled visits | Cost / Risk | Lagging | Partial |
| Continuity of care — share of a patient's visits by their primary clinician (feeds CAHPS / VBP) | % | Quality / Risk | Lagging | **No** |
| Schedule volatility / churn — how much of the set schedule changes before it is worked | % of plan changed | Workforce | Leading | **No** |
| Caseload balance (acuity + travel weighted) | index / variance | Workforce | Leading | **No** |
| Productivity vs. potential / drive-time | % (and visits/day) | Cost | Leading | **No** |
| Coordination / hand-off latency across the intake-to-care pipeline | hours | Flow | Leading | **No** |
| **Tool adoption (scheduler usage)** — *MVP-critical: if it is not used, none of the rest happens* | % of decisions via tool | Adoption | Leading | **No** |

> **The point the tab makes explicitly:** several **primary** metrics do not exist as a live number
> today. **Capturing the baseline is itself part of the work** — and it is the same observation the
> finance tab makes: *almost none of these exist today as a live, trustworthy, decision-ready number.*

---

## 3. Vendor fit — what the incumbent already covers

The `Functional Scorecard` scores each candidate product against every numbered variable; `Footprint &
Fit` rolls those into weighted category coverage (0 = untouched). Two products are scored today, **both
of them HCHB**:

| | HCHB Web Scheduling | HCHB Smart Scheduling | Combined |
|---|---:|---:|---:|
| Overall weighted rating | **62.1** | **71.2** | — |
| **Posture overreach** (variables where the product drives what we said it may only assist or read) | **0** | **16** | — |
| Footprint — average category coverage | 32.6 | 54.8 | **57.4** |
| Categories still a GAP | — | — | **6** |
| Categories covered | — | — | **26** |

**The six gap categories in the selected combination:**

| Layer | Category | Why it matters |
|---|---|---|
| Capacity | **Ramp** | Orientation / ramp status (`C-11`) — new clinicians counted at full capacity they cannot yet carry |
| Capacity | **Context** | Referral volume (`C-13`, scoped out today) — the demand side of the envelope |
| Scheduling | **Compliance** | The SOC / recert / face-to-face windows (`S-35`, `S-36`) |
| Scheduling | **Preference** | Patient preference variables |
| Scheduling | **Caregiver** | Caregiver-present requirement and fluctuating caregiver availability (`S-28`, `S-30`) |
| Coordination | **Coordination Cost** | Coordination time load (`CO-12`) — the work of making the schedule survive contact |

> **Read the overreach column alongside the rating.** Smart Scheduling scores highest **and** overreaches
> our stated posture on 16 variables. That is the Alabama failure mode expressed as a number: a product
> that wants to decide where we said the human decides (**DE-09**, **CN-43**). A higher score is not
> automatically a better fit.
