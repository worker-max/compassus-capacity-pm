# Overflow & Coverage Pilot — Charter (Pay-Per-Visit Lighthouse Branch)

> **What this is.** The Phase-B pilot charter (per the [initiative playbook](../initiative-playbook.md), Gate
> B→C) for the overflow/coverage flex-pool wedge: prove that letting **per-diem** and **FT-seeking-extra**
> clinicians *see and claim* open visits — with pay attached — covers overflow faster and cheaper than the
> manual phone-tree, **without harming quality or clinicians.** A reversible experiment, not a launch.
>
> **Why this wedge, why now.** It is opt-in, earnings-led, and runs on already-schedulable visits — so it dodges
> the Alabama Smart Scheduling failure mode (top-down assignment clinicians rejected; DS §3) and doesn't wait on
> the readiness gauntlet. See [`hchb-web-scheduling-overflow-coverage-fit.md`](./hchb-web-scheduling-overflow-coverage-fit.md)
> and the [prototype spec](./overflow-coverage-prototype-spec.md).

---

## 1. Hypothesis (pre-registered)

> *In a pay-per-visit branch, publishing overflow and coverage-needed visits to an eligible flex pool as
> claimable, paid work will **reduce median time-to-cover** and **uncovered/missed-visit rate**, and **offset
> agency/OT spend**, with **neutral-to-positive clinician experience** and **zero scope/compliance violations**.*

If the board doesn't beat the phone tree on time-to-cover **and** hold quality/experience flat, it fails the gate.

## 2. Why a pay-per-visit branch (site selection)

Straight from the discovery + playbook Phase-C guidance:
- **Earnings story lands.** Per-visit clinicians are *motivated* to pick up more; the board's core message
  ("more visits = more pay") is real money to them (DS §4).
- **No entrenched habits to fight.** Favor a **new-integration or brand-new go-live** branch; avoid tenured-
  clinician offices where change resistance sank Alabama (playbook Phase C).
- **Named candidates:** Providence, Ohio Health, BSMH (pay-per-visit offices cited in discovery). Rank by
  opportunity size × readiness × flex-pool depth.

**Selection criteria (score the shortlist):** pay-per-visit model ✚ meaningful overflow/decline/miss volume ✚
a real per-diem + FT-extra pool to draw on ✚ a willing coordinator + branch leader champion ✚ clean-ish HCHB
data ✚ Smart Scheduling enabled (so the Exceptions queue exists).

## 3. Scope

**In:** one branch; the two overflow demand sources (**Status Alerts** + **Smart Scheduling Exceptions**
queues); the flex pool (per-diem + opted-in FT-extra); the one-screen claim board + coordinator Overflow Desk
(prototype spec v1); near-term window (rolling ~8 days, matching the product).

**Out:** other branches; forecasting/economics/staffing-model/territory; readiness-gauntlet work; patient-facing
surfaces; any *involuntary* reassignment (the pilot is opt-in only).

## 4. Baseline first (Gate A discipline — measure before you change anything)

Capture ≥ 4 weeks of the current manual state so the pilot has an honest comparator:
- **Median + tail time-to-cover** for declined/missed/overflow visits.
- **Uncovered / missed-visit rate**; visits that fell to agency or went unfilled.
- **Agency / OT spend** attributable to coverage gaps.
- **Per-diem utilization** and how many distinct flex clinicians actually got used (concentration).
- **Coordinator effort** — rough phone-calls/hours per gap (interview + spot log; DS §1).

Definitions locked and signed **before** launch (playbook: agreed metric definitions, documented provenance).

## 5. Primary metric & success thresholds (pre-committed)

| Metric | Type | Threshold to pass gate (illustrative — set with branch on real baseline) |
|---|---|---|
| **Median time-to-cover** | Primary | ↓ ≥ 30% vs. baseline, sustained 4–6 wks |
| **Uncovered / missed-visit rate** | Primary guardrail | No worse than baseline; ideally ↓ |
| **Agency / OT coverage spend** | Secondary | Measurable offset |
| **Offer → claim conversion** | Adoption | ≥ a set floor; board fills a majority of published work |
| **Clinician experience** | Guardrail | Neutral-to-positive (pulse survey + decline-reason read) |
| **Scope / SOC / compliance violations** | Hard guardrail | **Zero.** Any violation = stop-and-fix, not a data point |
| **Fairness spread** | Guardrail | No small group carrying it; concentration flag stays green |

*Thresholds are placeholders until the branch's real baseline is in — the playbook requires them fixed in
advance, not tuned after seeing results.*

## 6. Kill / stop criteria (committed in advance)

Stop or roll back if any of: a **scope/SOC/compliance violation** the guardrails didn't catch; **missed-visit or
quality signal worsens**; **clinician experience turns negative** (coercion complaints, fairness grievances,
burnout signal); **coordinator load goes up** instead of down; or the board **can't beat the phone tree** on
time-to-cover by mid-pilot with no path to. A kill is a successful experiment — it bought a cheap "no."

## 7. Roles (RACI, condensed)

| Role | In the pilot |
|---|---|
| **Branch ED** | Accountable for branch outcomes; protects the "opt-in, not control" framing; owns go/no-go locally |
| **DCS / clinical manager** | Owns scope/SOC/compliance rails; validates that offered work is clinically appropriate |
| **Coordinator / scheduler** | Runs the Overflow Desk; the human in the loop on confirm & fallback; primary friction sensor |
| **Flex-clinician champion(s)** | 1–2 respected per-diem/FT voices who model the earnings story and surface UX pain |
| **Product / data** | Wires the queue feed + registry, ships the board, instruments the scorecard |
| **PM (this initiative)** | Charter, scorecard, decision log, phase-gate readout; guards against metric-gaming |

## 8. Change management (the Alabama antidote)

- **Position as a personal assistant, not a control mechanism** — "does the legwork, you keep your flexibility,
  pick up more if you want the earnings" (DS §4). Every clinician touchpoint honors this.
- **Opt-in only.** No involuntary reassignment in the pilot. A "no" is free and never held against anyone.
- **Champions before broadcast.** Seed with the 1–2 flex champions; let early wins pull others in.
- **Fairness visible.** Show the pool the work is spread — the fastest way to lose a per-diem is unfair
  distribution or a cancelled promise (TAC L3-8).
- **Don't over-promise.** Under-scope the board; a small tool that reliably fills 10 visits beats a grand one
  that flakes.

## 9. Cadence (from the playbook)
- **Daily 15-min capacity huddle:** open visits, no-fills, over/under-loaded clinicians, any scope near-miss.
- **Weekly pilot standup:** scorecard vs. baseline + decision log.
- **Bi-weekly adoption/friction review:** decline reasons, coordinator load, clinician pulse.
- **Mid-pilot course-correction** and an end-of-pilot **Gate C→D readout** with evidence + recommendation.

## 10. Risk register (top items)

| Risk | Mitigation |
|---|---|
| **Queue feed has no API** → manual/screen-scrape drag | Confirm early (spec Open Q#1); accept a semi-manual v1 if fill-rate signal still provable |
| **Flex pool too thin** to fill overflow | Score pool depth in site selection; recruit/onboard registry before launch |
| **Stale PointCare sync** → wrong headroom, double-book | Freshness timestamp; optimistic lock on claim; re-check on confirm (spec §5, §9) |
| **Scope/SOC violation** via mis-match | Hard rails enforced in the rules engine, not displayed; DCS spot-audit weekly |
| **Fairness / burnout** — same few carry it, FT-extra over-offered | Fairness ledger + headroom gate; utilization ceiling; PM watches concentration |
| **Coercion drift** — "asks" become expectations | Penalty-free decline, honest-size cards, no urgency/guilt language (TAC C-2) |
| **Metric gaming** — visits padded to look covered | Missed-visit + quality guardrails; never count a padded visit as a win |

## 11. Compliance & data posture
- **PHI minimum-necessary:** clinician board shows discipline, zone/zip (not address), date, pay — not patient
  identifiers beyond what fit requires. Confirm BAA-covered surface before any patient-linked field ships.
- **Scope, SOC rule, compliance windows** are hard rails throughout (recert/30-day/14-day/48h are the DCS's, not
  the board's, but the board must never surface an obligated or scope-mismatched slot as claimable).
- **`patient_confirmed` visits immovable** — pilot fills open work only.

## 12. What advancing the gate optimizes — and trades against

*(The one question the playbook demands at every gate.)* Advancing scales a **fast, opt-in, earnings-positive**
way to cover overflow. It **trades against**: a possible lean on flex labor that masks a **structural staffing
gap** (watch PRN-dependency — a >15% chronic reliance is a Layer-1 hire signal, not a coverage win, TAC L1-8),
and the risk that a coverage-marketplace becomes a comfortable substitute for fixing the readiness gauntlet and
the staffing model that *actually* set capacity. The pilot proves the wedge; it must not let the wedge become
the whole answer.

---

*Companion to the overflow/coverage fit evaluation and the prototype spec. Gate-B artifact — thresholds and site
to be finalized with the branch's real baseline before Gate B→C sign-off.*
