# Overflow & Coverage — One-Screen Open-Work → Claim Prototype Spec

> **What this is.** A functional spec for the **thin coverage layer** that sits on top of HCHB Web Scheduling's
> exception queues, described in [`hchb-web-scheduling-overflow-coverage-fit.md`](./hchb-web-scheduling-overflow-coverage-fit.md) §5.
> It turns "visits needing coverage" into claimable work for a **flex pool** — **per-diem clinicians** and
> **full-time clinicians looking for extra work**.
>
> **Design law.** Keep it small. HCHB is the system of record and the demand feed; this layer adds only what
> HCHB lacks — a **clinician-facing board, availability/fit matching, a claim loop, the earnings number, and
> write-back.** No forecasting, no economics, no staffing model in v1. Resist scope creep.
>
> **Corpus refs.** IDX = [`../artifacts/capacity-tool-data-index.md`](../artifacts/capacity-tool-data-index.md),
> TAC = [`../sme/capacity-tactics-library.md`](../sme/capacity-tactics-library.md),
> ECO = [`../artifacts/capacity-ecosystem-map.md`](../artifacts/capacity-ecosystem-map.md),
> DS = [`../knowledge/discovery-session.md`](../knowledge/discovery-session.md).

---

## 1. Objective & the two surfaces

**Objective:** cut time-to-cover and uncovered-visit rate for overflow, by letting eligible flex clinicians
**see and claim** open visits — with pay attached — instead of a scheduler working the phones.

Two surfaces, one shared object (the open-work item):

- **Clinician surface — "Open Visits" (the one screen).** A mobile-first list of visits *this clinician is
  eligible for*, each claimable in one tap, with pay and fit shown up front. This is the product's whole reason
  to exist; everything else serves it.
- **Coordinator surface — "Overflow Desk."** The scheduler/staffing view: the open-work feed (from HCHB's
  queues), fill status, who was offered, the fairness ledger, and a manual-assign fallback.

## 2. Personas

| Persona | Need | Corpus |
|---|---|---|
| **Per-diem / PRN clinician** | Any well-matched visits near home on days they choose; pay visible. | IDX A7, TAC L3-7 |
| **FT clinician wanting extra** | *Incremental* visits above core load, only when they have headroom; extra earnings. | DS §4, TAC C-5 |
| **Coordinator / scheduler** | Fill the gap fast, fairly, without 20 phone calls; keep the record in HCHB. | DS §1, TAC L3-8 |
| **Branch leader (DCS/ED)** | Coverage without burnout, scope violations, or agency/OT blowout. | STRAT, TAC C-5 |

## 3. Data model (v1)

### 3.1 OpenWorkItem — the demand (sourced from HCHB, not authored here)
| Field | Source | Notes |
|---|---|---|
| `visitId` | HCHB (E1) | Join key back to the system of record |
| `originQueue` | HCHB | `status_alert` (field return) or `smart_sched_exception` (overflow) |
| `exceptionReason` | HCHB | e.g. "Worker at Max Hours", "Declined", "Missed by Clinician" |
| `discipline` / `serviceCode` / `serviceCodeType` | HCHB (E2, C4) | Drives scope-match |
| `visitDate` / `timeWindow` | HCHB (E4) | "Time not set" allowed (per the guide) |
| `patientZone` / `zip` | HCHB (C2/C3) | For proximity — **zone/zip only, not address** (PHI-min) |
| `payorSource` / `authStatus` | HCHB (D6/H) | Only surface **auth-ready** work as claimable |
| `estimatedPay` | DERIVED (VCP / pay model) | The earnings number — required on every offer |
| `pointValue` (WVP) | HCHB Productivity Points | For headroom accounting on claim |
| `continuitySensitivity` | STATIC (TAC C-4) | Flag if breaking continuity matters (warm handoff) |
| `fillState` | DERIVED | `open → offered → claimed → confirmed → written_back` / `declined` / `expired` |

### 3.2 FlexClinician — the supply (the registry HCHB doesn't provide)
| Field | Source | Notes |
|---|---|---|
| `clinicianId` | HCHB/WD (A1) | |
| `employmentType` | WD (A7) | `PRN` or `FT_seeking_extra` — **the population switch** |
| `disciplines` / `licenses` / `competencies` | WD/STATIC (A3–A5) | Hard scope filter (incl. "No SOC", "No wound care") |
| `homeZone` / `willingZones` | STATIC (A13, I1) | Willingness, not just assignment (the Alabama lever) |
| `maxExtraPerDay` / `preferredDays` | STATIC (I4, I5) | Self-declared ceiling |
| `payModel` | WD (A9) | Per-visit / bonus — drives `estimatedPay` |
| `capacityPct` | HCHB | `(Scheduled+Completed)/Expected` — **headroom gate for FT** |
| `notifyChannel` | STATIC/CIR | SMS/push (Twilio channels already in tool) |

### 3.3 Offer / Claim — the loop HCHB lacks (ECO 3I, TAC C-2/C-6)
`offerId, visitId, clinicianId, offeredAt, viewedAt, response ∈ {claimed, declined, expired}, declineReason, confirmedAt`.
**Decline reason is captured every time** — it is the buy-in signal and the training data.

## 4. Eligibility & matching (the rules engine)

Applied in order; a visit only appears on a clinician's board if it passes **all hard rails**, then is ranked.

**Hard rails (never optimized around — guardrail set, TAC §guardrails):**
1. **Scope & licensure match**, including the **SOC rule** (RN if nursing on case; PT only if not) and explicit
   restrictions ("No SOC", "No wound care", "No high-acuity"). This is the ECO-flagged correctness gap — enforce
   it, don't just display it.
2. **Auth-ready only** — never surface a visit blocked on authorization as claimable (H2–H4).
3. **Headroom gate for FT-extra:** offer only when `capacityPct ≤ target`. Per-diems skip this (no Expected).
4. **`patient_confirmed` is immovable** — you fill open work; you never create it by pulling an accepted visit
   (DS Process 3; TAC L3-3).

**Ranking (soft, for order on the board):** proximity (drive-time from `homeZone`), day/preference fit,
continuity where sensitive, and **fairness** (boost clinicians owed hours / under-offered — TAC L3-8, C-1).

## 5. The claim loop (states & rules)

```
open ──publish──▶ offered ──tap claim──▶ claimed ──coordinator/one-tap──▶ confirmed ──sync──▶ written_back
   │                  │                                                                            
   └── manual assign  └── declined(reason) / expired(TTL) ──▶ re-rank & re-offer to next eligible
```

- **No double-promise.** A visit `claimed` by one clinician locks immediately for others (optimistic lock;
  first-confirmed wins; late claimants told "already covered" — never two people sent).
- **Offer TTL** so stale offers expire and re-circulate; near-term visits get shorter TTL (perishable — TAC L3-5).
- **Write-back** posts the assignment to HCHB (or, until an API exists, drops a one-tap task in the coordinator's
  Overflow Desk to assign in HCHB/Citrix — the guide notes exception assignment still round-trips to Citrix).

## 6. The clinician "Open Visits" screen (v1 layout)

A single scrollable list of cards. Each card:
- **Pay** (large — the reason they opened it), **discipline + service code**, **date / time window**,
  **zone + drive estimate**, continuity flag if relevant.
- One primary action: **Claim.** One secondary: **Not interested → reason** (penalty-free; a "no" is data).
- Filters kept minimal: date, distance, my-disciplines. No firehose — the list is *already* eligibility-filtered.

**Tone rule (TAC C-2):** cards state the honest size (drive + doc), never use urgency/guilt/scarcity, and a
decline costs nothing. The screen is a *personal-assistant* surface, not a dispatch order (DS §4).

## 7. The coordinator "Overflow Desk"
- **Open-work feed** = HCHB **Status Alerts** + **Smart Scheduling Exceptions** queues, deduped, with fill state.
- **Per-visit offer trail:** who's eligible, who was offered/viewed/declined (+reason), TTL countdown.
- **Fairness ledger:** offers & fills per clinician; flags concentration ("same 3 carrying it") — TAC L3-8/C-1.
- **Manual assign fallback** for anything the board can't fill; escalation to leadership when a gap is
  structural, not transient (guardrail #9 — label structural vs one-off; don't paper a staffing hole with flex).

## 8. Notifications
Reuse the tool's existing **Twilio channels**. Push/SMS an eligible clinician when new matching work publishes;
respect quiet hours and per-clinician cadence; **never** blast the whole pool for one visit (fairness + noise).

## 9. Integration & data-trust
- **In:** HCHB queues (poll/export/API — cadence TBD, see Open Questions), worker record (capacity %, phone,
  employment type if exposed), pay model.
- **Out:** assignment write-back to HCHB, or coordinator one-tap task.
- **Staleness:** capacity % and visit state ride **PointCare manual sync** (ECO 3K) — show a data-freshness
  timestamp; treat headroom as approximate; re-check on confirm.

## 10. Instrumentation (prove it works)
Primary: **time-to-cover** and **uncovered/missed-visit rate** vs. the manual baseline. Secondary:
**offer→claim conversion**, **fill rate by board vs. manual**, **decline-reason distribution**, **fairness
spread** (Gini-ish across the pool), **FT-extra offers that respected the headroom gate** (compliance), and
**agency/OT offset**. Every one maps to a Phase-C scorecard line in the playbook.

## 11. Scope

**In (v1):** the two surfaces, the three data objects, the rules engine (hard rails + simple ranking), the claim
loop with decline-reason capture, Twilio notify, and write-back-or-task. Single branch, near-term window.

**Out (v1, explicit):** demand forecasting, LUPA/margin economics, the staffing-model & territory views, the
readiness gauntlet, patient-facing surfaces. These are the fuller capacity tool — not this wedge.

## 12. Open questions / dependencies
1. **Do the Status-Alerts & Smart-Scheduling-Exceptions queues have an API/export** (fields, cadence, reason
   codes)? Determines automated feed vs. screen-scrape. *(Blocking.)*
2. **Does HCHB expose `employmentType`/PRN and `payModel`** on the worker record, or must the registry own them?
3. **Is there a write-back path** to assign a visit via API, or is the coordinator one-tap-in-Citrix the v1
   reality?
4. **How is "Expected" set** (the headroom denominator)? Flat default vs. market/discipline-tuned changes the
   FT-extra gate (STRAT L1.4).
5. **BAA / PHI surface** for the clinician board — confirm zone/zip-not-address and minimum-necessary before any
   patient-linked field ships (IDX §6, CLAUDE.md HIPAA).

---

*Companion to the overflow/coverage fit evaluation and the pilot charter
([`overflow-coverage-pilot-charter.md`](./overflow-coverage-pilot-charter.md)). v1 = a reversible experiment,
not a launch.*
