# Meridian Care Logistics — Vendor Scorecard

**84.2 / 100 · Advance**

A scheduling-and-routing optimizer built for multi-site home health, with a live bi-directional HCHB integration and a strong week-level engine. Capacity is modelled as visit points against a productivity target, which matches how Compassus already reasons. Patient engagement is thin — reminders and confirmations exist, agentic outreach does not — and the clinician-facing model is advisory by design.

| Part | Score | Budget | |
|---|---:|---:|---|
| 1 · HCHB Integration | **25** | 25 | `████████████████████` |
| 2 · Scope Footprint | **23.4** | 30 | `████████████████····` |
| 3 · Sophistication | **17.0** | 20 | `█████████████████···` |
| 4 · Clinician & Adoption | **7.5** | 10 | `███████████████·····` |
| 5 · Partnership | **11.3** | 15 | `███████████████·····` |
| **Total** | **84.2** | **100** | |

## Footprint against the Compassus spec

**Overall — 77%** (31.5 of 41 elements)

| Arena | Footprint | Covered | Partial | Not covered | Points |
|---|---:|---:|---:|---:|---:|
| Capacity Management | **82%** | 8 | 2 | 1 | 8.2 / 10 |
| Scheduling Engine | **93%** | 12 | 2 | 0 | 9.3 / 10 |
| Engagement | **59%** | 7 | 5 | 4 | 5.9 / 10 |

### Element detail


**Workforce supply**

| | Element | Evidence |
|---|---|---|
| ● | **CAP-01** Roster by discipline, role (assessing vs. assistant), FTE and employment type | B1 / C1 — *roster synced nightly by discipline, role and FTE* |
| ◐ | **CAP-02** Start-of-care capable clinicians, measured as their own distinct capacity | C1 — *assessing vs non-assessing is a role flag, not its own capacity pool* |
| ● | **CAP-03** Specialty competencies, plus orientation and ramp status | B1 — *competency matrix with ramp percentage* |
| ● | **CAP-04** Per-diem and float pool | B1 — *per-diem pool modelled as elastic supply* |
| ○ | **CAP-05** On-call and weekend rotation load | — |

**Availability & reach**

| | Element | Evidence |
|---|---|---|
| ● | **CAP-06** Approved time off and working availability | B2 — *PTO from HCHB, working patterns maintained in product* |
| ● | **CAP-07** Clinician territory assignment by zip, against branch coverage area | B2 — *zip-level territory with branch coverage overlay* |
| ● | **CAP-08** Reachability from the clinician's home base, measured by drive time | C2 — *drive-time isochrones from home base, refreshed quarterly* |

**The capacity math**

| | Element | Evidence |
|---|---|---|
| ● | **CAP-09** Visit weighting — the point value per visit type, and the productivity target and ceiling it is measured against | C1 — *visit points per type against a per-clinician weekly target* |
| ● | **CAP-10** Committed load vs. open room, by day, week, discipline and territory | C1 — *committed vs open by day, discipline and territory* |
| ◐ | **CAP-11** Referral inflow and discharge outflow against the envelope | C1 — *referral inflow modelled; discharge outflow not forecast* |

**Demand**

| | Element | Evidence |
|---|---|---|
| ● | **SCH-01** Plan-of-care orders, ordered frequency and visit types, from the EMR (Home Care Home Base) and the intake platform | A1 / B4 — *orders and frequencies read from HCHB* |
| ● | **SCH-02** Authorization status and payer rules attached to each visit | B4 — *auth status attached per visit, payer rules configurable* |
| ● | **SCH-03** Order, consent and readiness state — what is schedulable, not merely ordered | C3 — *held state — ordered but not schedulable, with a reason code* |
| ● | **SCH-04** The compliance window each visit has to fall inside | C3 — *compliance window enforced as a hard constraint* |

**Matching**

| | Element | Evidence |
|---|---|---|
| ● | **SCH-05** Discipline and role match, specialty competency, acuity to skill level | C2 — *discipline, competency and acuity weighted in the match* |
| ● | **SCH-06** Clinician working pattern, needs and restrictions | C2 — *clinician restrictions honoured as constraints* |
| ◐ | **SCH-07** Patient and caregiver needs, restrictions and availability, sourced from the patient | C7 — *patient availability captured, but by office staff not the platform* |
| ◐ | **SCH-08** Clinical timing — diagnosis-driven cadence, competing appointments, infection-control sequencing | C2 — *cadence supported; infection-control sequencing not addressed* |
| ● | **SCH-09** Continuity of care, and supervisory visit dependencies | C2 — *continuity weighted; supervisory dependencies tracked* |

**Routing & the week**

| | Element | Evidence |
|---|---|---|
| ● | **SCH-10** Home base start and end, route proximity, mileage | C2 — *route proximity and mileage optimised per day* |
| ● | **SCH-11** Appointment time windows and intra-day sequencing | B6 — *time windows and intra-day sequencing* |
| ● | **SCH-12** Front-loading, pace against the plan of care, day-by-day balancing | C4 — *front-loading and week balancing against plan-of-care pace* |

**Exceptions**

| | Element | Evidence |
|---|---|---|
| ● | **SCH-13** Missed-visit management and tracking — and reducing the occurrence | C5 — *missed visits tracked with cause coding* |
| ● | **SCH-14** Reassignment, coverage, and rebooking inside the window | C5 — *reassignment inside the compliance window, offered by rank* |

**How this should run**

| | Element | Evidence |
|---|---|---|
| ○ | **ENG-01** Outreach carried by the platform itself — agentic voice, text and email — rather than queued up for a coordinator to work | — |
| ◐ | **ENG-02** Staff able to see it, intervene, override, and take any conversation back | C7 — *staff see and control all outreach — but all of it is staff-initiated* |

**Before the visit**

| | Element | Evidence |
|---|---|---|
| ○ | **ENG-03** New-patient welcome call | — |
| ◐ | **ENG-04** Patient availability captured before the visit is booked | C7 — *captured in product, entered by a coordinator* |
| ● | **ENG-05** Automated reminders and en-route notification | B8 — *SMS reminders and en-route ping from the clinician app* |
| ◐ | **ENG-06** The day-before confirmation round automated for every patient, every day | B8 — *confirmation round exists, run by staff from a worklist* |
| ○ | **ENG-07** The schedule staying pliable until that confirmation, so clinician and capacity changes can land before the patient is told | — |
| ● | **ENG-08** Channel and communication-preference management | B8 — *channel preference per patient* |

**When plans change**

| | Element | Evidence |
|---|---|---|
| ◐ | **ENG-09** Reschedule coordination with the patient | C5 — *reschedule is a staff task with a suggested slot* |
| ● | **ENG-10** Coverage coordination — matching potential clinicians to an open need, and reaching them directly | C5 — *open need broadcast to eligible clinicians in the app* |
| ● | **ENG-11** Call-out coverage, and the urgent or prioritized needs that surface during the day | C5 — *call-out triggers a ranked coverage offer within minutes* |
| ◐ | **ENG-13** Failed-visit and no-show follow-up and rebooking | C5 — *no-show logged and requeued; follow-up is manual* |

**Incentives & offers**

| | Element | Evidence |
|---|---|---|
| ○ | **ENG-12** Incentives or differentials attached to hard-to-fill visits, and offered to the clinicians who can take them | — |

**Across the care team**

| | Element | Evidence |
|---|---|---|
| ● | **ENG-14** Multi-discipline visit coordination | B11 — *multi-discipline coordination on the shared week view* |
| ● | **ENG-15** Care-team and office coordination updates | B11 — *office and care-team updates in-product* |
| ● | **ENG-16** A clinician view of their own schedule and their own results — the case for the change, made to the person it lands on | D3 — *clinician sees own schedule, points and mileage* |

## Sophistication — 17.0 / 20

| | Item | Ladder | Source | Reading |
|---|---|---|---|---|
| 3 | **Automation posture** | Mechanism | B / C7 | Scheduling is automated with a person approving; all patient outreach is staff-initiated. |
| 4 | **Decision depth** | Proven | C1, C2 | Constraint solver with named weights. Answers the referral question directly: shows the envelope impact before accepting. |
| 3 | **Readiness & rules** | Mechanism | C3 | Held state with reason codes and auto-release on auth. Mechanism clear, no evidence offered. |
| 4 | **Recovery** | Proven | C5 | Ranked offer within 4 minutes median, escalation to per-diem, then to the DCS worklist. Figures over 12 months, named customer. |
| 3 | **Enterprise trust** | Mechanism | C6, A2, A3 | 99.95% over 12 months, read-only failover, 99.9% contractual. Impact claimed with a baseline but a single site. |

## Clinician & Adoption — 7.5 / 10

| | Item | Ladder | Source | Reading |
|---|---|---|---|---|
| 3 | **What the clinician decides** | Mechanism | D1 | Clinician can decline and reorder their own day; cannot change assignment. Declines feed a preference weight. |
| 4 | **Decide or advise** | Proven | D2 | Designed to advise; decide mode is a per-branch configuration with a documented migration path. |
| 2 | **Adoption evidence** | Described | D3 | Adoption defined as weekly active use. No six-month curve supplied. |

## Partnership — 11.3 / 15

| | Item | Ladder | Source | Reading |
|---|---|---|---|---|
| 2 | **Sharing in the value** | Described | E2 | Open to design-partner pricing and a joint roadmap. No structure or terms proposed. |
| 4 | **Deployment & change management** | Proven | E3 | Three named deployments, a resistance story, and a change they made because of it — moved from decide to advise. |
| 3 | **What we did not ask** | Mechanism | E1 | Raised payer-mix-aware sequencing, which is not on our one-pager. |
| 3 | **What they chose not to build** | Mechanism | E4 | Chose not to build patient-facing voice; says the EMR should own the record of contact. |

## ⭐ Differentiators

- Only answer that gives a branch leader the envelope impact of accepting a referral **before** they accept it (C1).
- Coverage offer with a measured median time-to-fill — 4 minutes — rather than a described workflow (C5).
- Decide-vs-advise is a per-branch switch with a migration path, not a product-wide posture (D2).
- Raised payer-mix-aware sequencing, which is not on our one-pager and probably should be (E1).

## 🚩 Flags

- 🔴 Measured impact (A3) comes from one site. References offered but not yet named.
- 🟡 All patient outreach is staff-initiated — the coordinator labour we are trying to remove stays.
- 🟡 Hospice and private duty are 40% of their business; home health is not the whole company.

## ❓ Unknowns — the demo agenda

- On-call and weekend rotation load (CAP-05) — not addressed anywhere in the return.
- Whether discharge outflow can be forecast, or only observed (CAP-11).
- What the day-before confirmation round actually costs in staff hours at our scale.
- E2 — what a value-share would concretely look like. Needs a direct conversation.

---

*Scored 2026-09-02 · by Worked example — Meridian Care Logistics is fictional. Nothing here is a real vendor. · questionnaire completed by K. Alvarez, VP Solutions — 28 Aug 2026 · rubric v1.0 · 41 spec elements, form_version 2026-08-19.*
