# HCHB Web Scheduling as an Overflow & Coverage Layer for a Flex Pool

> **Scope of this evaluation.** A narrower, more concrete question than the full fit analysis
> ([`hchb-web-scheduling-analysis.md`](./hchb-web-scheduling-analysis.md)): *could HCHB Web Scheduling be used
> **simply** to manage **overflow and visits needing coverage** — a working space for **per-diem clinicians**
> and **full-time clinicians looking for extra work**?*
>
> **Short answer.** Web Scheduling already gives you a strong, native **demand signal and back-office triage
> surface** for overflow — the "what needs covering" half. It is **not** a flex-labor marketplace: it has no
> clinician-facing open-work board, no availability/proximity/employment-type search of supply, no offer→claim
> loop, and no earnings visibility. So the honest read is: **use Web Scheduling's exception queues as the open-
> work feed, and add a thin coverage layer on top of them.** That thin layer is also the **best low-risk wedge**
> for the whole initiative — opt-in, earnings-led, and immune to the Alabama "top-down control" failure.

---

## 1. The use case, stated precisely

Two supply populations, one demand stream:

- **Per-diem / PRN clinicians** — flex is their whole job; they want *any* well-matched visits, close to home,
  on days they choose.
- **Full-time clinicians looking for extra work** — want *incremental* visits **above their core load**,
  typically on a pay-per-visit or bonus basis (the earnings story from
  [`../knowledge/discovery-session.md`](../knowledge/discovery-session.md) §4).

The demand they cover is **overflow and coverage gaps**: visits that exceed core-team capacity, or visits a
clinician **declined / rescheduled / reassigned / missed**, or slots freed by **cancellation / discharge** that
must be backfilled before they perish (tactics [`../sme/capacity-tactics-library.md`](../sme/capacity-tactics-library.md)
L3-5, L3-7).

**Crucial distinction between the two populations — and the metric that governs it:** the FT-extra population
must only be offered work when they have **headroom**. Web Scheduling's native capacity readout —
`(Scheduled + Completed) / Expected` Productivity Points — is exactly the gate: offer extra to an FT clinician
**at or under 100%**, never to one already over. Offering overflow to a maxed FT clinician is the burnout /
turnover trap (TAC C-5). Per-diems have no "Expected," so the gate for them is willingness + fit, not headroom.

## 2. Why this is the right *wedge* (not just a feature)

Managing overflow/extra-work is a smaller, cleaner scope than the full capacity initiative, and it de-risks the
exact things that sank prior attempts:

- **Opt-in by construction.** Clinicians *choose* to pick up extra visits. That sidesteps the Alabama Smart
  Scheduling failure, which was top-down assignment (crossing zip boundaries against clinician will; DS §3).
- **Leads with the earnings story.** "More visits = more pay" is the buy-in message the discovery prescribes
  (DS §4: position as a *personal assistant that increases flexibility and earnings*, not control).
- **Works on already-schedulable visits.** Overflow is downstream of the readiness gauntlet — you don't have to
  solve DCS/POC/auth/TIC first (our Tier-1A gap). It runs on visits HCHB already shows as needing a worker.
- **Clean pilot population.** Pay-per-visit offices and new/integration branches (DS §4, Next Steps #2) are the
  ideal first cohort — no entrenched habits to fight.

## 3. What Web Scheduling gives you **today** (the demand signal + triage)

| Capability in the product | What it does for overflow/coverage | Reference (guide) |
|---|---|---|
| **Scheduling Status Alerts queue** | The native "visits needing coverage" list — **Rescheduled, Reassigned, Declined, Missed by Clinician** = field returns that must be re-placed. | p.3 |
| **Smart Scheduling Exceptions queue** ("Worker at Max Hours") | The native **overflow** list — visits the optimizer couldn't place because core workers are full. | p.4 |
| **Worker Search → Worker Calendar flyout** | Pull up a candidate's **7-day week + NVA** and their **capacity %** — is this per-diem/FT open this week? | p.10–11 |
| **Worker capacity = (Scheduled + Completed) / Expected** | The **headroom gate** for FT-extra; identifies who can absorb more. | p.11 |
| **Worker card: Primary Phone, Job Description, Home Branch, Status** | Enough to make the ask by phone; discipline + branch to match the visit. | p.10 |
| **Visit Details: service code, payor, auth, date, patient zip/city** | The context needed to judge fit (discipline, geography, auth-ready). | p.5–6, p.11 |
| **PRN visits filter (show/hide)** | The product already carries a PRN concept at the visit level. | p.7 |

**The manual "overflow desk" you could run tomorrow, with the product as-is:**
1. Watch the **Alerts** queue (field returns) and **SS Exceptions** queue (over-capacity overflow) for coverage
   needs.
2. Open **Visit Details** for the uncovered visit — service code, payor/auth, date, patient zip.
3. **Worker Search** a known flex clinician → **Worker Calendar** → read capacity % and open days → get
   **Primary Phone**.
4. Call, offer, confirm → assign. *(Caveat: today the SS-exception assignment step still round-trips to the
   Citrix app — see §4.)*

This is a real, working, **scheduler-driven** overflow triage flow for someone who already knows their flex
pool. It is genuinely useful and requires nothing new.

## 4. What it **cannot** do — the flex-marketplace gaps

These are the pieces a per-diem / FT-extra "space" needs that Web Scheduling does not provide. Each maps to a
capability our corpus already specifies.

| Gap in Web Scheduling | Why it matters for a flex pool | Our corpus answer |
|---|---|---|
| **No clinician-facing open-work board.** It is a back-office scheduler tool only — no surface where a per-diem/FT clinician *sees* and *claims* open visits. | The whole point of the "space" is self-serve pickup. Scheduler-pull doesn't scale and buries the earnings story. | Per-diem-facing "open slots" view; publish the need 5–7 days out (TAC **L3-7**). |
| **Supply search is by name only** (min 3 chars). No filter by **employment type** (PRN vs FT), **availability**, **capacity headroom**, or **proximity**. | For overflow you must query *"who is open, near this zip, this discipline, this day"* — you can't if you must already know the name. | Availability/zone/headroom matching (IDX A7, A13; TAC L3-4, L2-1). |
| **No offer → accept / decline loop, and no reason capture.** (SS-Prevented is a one-way veto flag.) | Accept/decline + reason is the buy-in mechanism *and* the training signal; without it you repeat Alabama. | Accept/decline governance (ECO **3I**); "the ask that gets a yes" (TAC **C-2**); override sacred (**C-6**). |
| **No earnings / pay visibility.** | The core motivator for *both* populations is pay; a coverage offer with no $ attached is weak. | VCP comp layer; pay-model + willingness fields (IDX A9, I3). |
| **Fill action for exceptions returns to Citrix.** | The loop isn't closed in the browser yet — friction on the actual assignment. | Write-back integration once HCHB exposes it. |
| **No gap forecast.** Present-tense, rolling 8 days, on manual PointCare sync. | You want to publish predictable open work ahead, not just react. | Nightly gap forecast → publishable slots (TAC **L3-7**); staleness-aware design (ECO 3K). |
| **No fairness / reciprocity ledger.** | Overflow offered to "whoever answers first" concentrates work and burns the reliable few. | Per-diem fairness ledger (TAC **L3-8**); reciprocity / don't-exploit-the-yes (**C-1**, guardrails). |

## 5. The thin layer to add on top (the actual "space")

Keep it deliberately small. The product is: **an open-work board fed by HCHB's own exception queues, matched to
a flex pool, with a claim loop and the earnings story.** Concretely:

1. **Open-work feed = the two HCHB queues.** Ingest **Scheduling Status Alerts** + **Smart Scheduling
   Exceptions** as the source of truth for "visits needing coverage." No new demand model required.
2. **A flex-pool registry** with the fields HCHB lacks: employment type (PRN / FT-seeking-extra), disciplines &
   competencies, home zone, willingness (zones, SOC, max extra/day), pay model, and preferred days
   (IDX A5–A9, A13, I1–I5).
3. **Availability + fit match**, not name lookup: rank open visits to eligible clinicians by discipline/scope,
   **proximity**, and **headroom** (FT-extra gated on capacity % ≤ target; per-diem gated on willingness).
   **Hard-enforce scope and restrictions** ("No SOC," "No wound care") — the correctness gap flagged in ECO.
4. **A claim / offer loop with reason capture** — the buy-in and training signal HCHB doesn't have.
5. **Attach the earnings number** to every offer (pay-per-visit / bonus). This is what makes an FT clinician
   open the notification at all.
6. **Write the accepted assignment back** to HCHB (or hand the scheduler a one-tap confirm) so the record of
   truth stays in the system of record.

Everything else — forecasting, economics, staffing model — stays out of *this* wedge. It can grow into the
fuller capacity tool later; for the overflow "space," resist scope creep.

## 6. Guardrails carried from the corpus (non-negotiable, even in a "simple" tool)

- **Protect the reliable clinician; keep it fair.** Spread overflow across the eligible pool; never route by
  who-answers-fastest; run the fairness ledger (TAC C-1, L3-8, guardrail #6). *Don't exploit the yes.*
- **The ask is honest and refusable.** Specific, early, true size (drive + doc), penalty-free decline; **never**
  guilt/urgency/patient-welfare leverage; a "no" is data (TAC C-2, guardrail #7).
- **Scope + the SOC rule are hard rails**, not optimization variables. LPN can't assess; PT does SOC only when
  nursing is off the case. Overflow never routes around scope (guardrail #2, TAC L1-3).
- **`patient_confirmed` visits are immovable** without explicit human release — you can *fill* open work, you
  can't *pull* an accepted visit to create it (DS Process 3; TAC L3-3, guardrail #8).
- **FT-extra is capped by headroom.** Offer only at/under Expected; enforce a utilization ceiling; sustained
  overload is a cost, not a win (TAC C-5).
- **Continuity where it counts.** Coverage fills are one-offs, but flag when a break matters (wound/decline/
  EOL/active SOC) for a warm handoff (TAC C-4).
- **PHI minimum-necessary.** The offer needs discipline, zone, date, and pay — not patient identifiers beyond
  what fit requires (CLAUDE.md HIPAA rules; IDX §6).

## 7. Recommendation

- **Yes — use Web Scheduling for this, as the demand/triage layer, immediately.** Its two exception queues are a
  ready-made, native "visits needing coverage" feed, and the Worker Calendar capacity % is the exact headroom
  gate for FT-extra. A scheduler-driven overflow desk works today with zero build.
- **But the "space" itself is the thin coverage-marketplace layer on top** (§5) — that's where the per-diem and
  FT-extra populations actually live, because the product has no clinician-facing board, no availability search,
  no claim loop, and no earnings story.
- **Treat this as the pilot wedge for the whole initiative.** It's opt-in, earnings-led, runs on already-
  schedulable visits, and dodges the Alabama failure mode — the cleanest possible first win, ideally in a
  pay-per-visit or new-integration office.

**Immediate next moves**
1. Confirm what the **Smart Scheduling Exceptions** and **Status Alerts** queues expose via API/export (fields,
   cadence, reason codes) — that determines whether the open-work feed can be automated or is screen-scraped.
2. Confirm whether HCHB exposes **employment type / PRN status** and **pay model** on the worker record, or
   whether the flex-pool registry must hold them.
3. Stand up the flex-pool registry (§5.2) and a one-screen open-work→claim prototype over a single pilot
   branch's two queues; measure fill rate and time-to-cover against today's manual baseline.
4. Validate the **"Expected" target** definition (the headroom denominator) so FT-extra offers gate correctly.

---

*Prepared for the Compassus Capacity & Scheduling initiative. Companion to the full HCHB Web Scheduling fit
analysis. Product capabilities cited from the Web Scheduling User Guide (KB0025451 v10.0); flex-pool design
patterns and guardrails drawn from the initiative's discovery, tactics library, data index, and ecosystem map.*
