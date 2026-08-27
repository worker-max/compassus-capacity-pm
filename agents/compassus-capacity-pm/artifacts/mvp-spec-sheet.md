# MVP Spec Sheet — Capacity Management, Phase 1

> **What this is.** The day-one scope for the capacity and scheduling platform, derived from the
> scored variable inventory rather than assembled by judgment. Step 9 of
> [`playbooks/initiative-build-process.md`](../../../playbooks/initiative-build-process.md).
>
> **Status.** First pass, 22 Aug 2026. Every in-scope item traces to a variable ID; every
> out-of-scope item carries a reason and a re-entry trigger. **Two prerequisites are unmet and they
> block the whole MVP** — see §2.
>
> **Sources.** Variable Inventory (`8.13 Compassus Capacity & Scheduling Workbook.xlsx`, Drive
> `1tVEkPO2FJMFVyqLZP1TrzqbmjX0qEDgv`) · [`source-war-list-worksheet.md`](./source-war-list-worksheet.md)
> · [`business-case-register.md`](./business-case-register.md) · decisions DE-02, DE-03, DE-04, DE-09.

---

## 1. What the MVP is, in one sentence

> **The MVP does not build the schedule.**
> **It makes capacity measurable and observable — the envelope a branch can deliver against, and how
> much of it is left — for the first time.**

Three things follow from that sentence, and each is a decision already taken:

- **Capacity is Phase 1, and Phase 1 is visualisation only.** No automation in the first release
  (**DE-03**). The tool shows; people decide.
- **The capacity tool replaces the scheduling grid.** They are the same object — do not build both
  (**DE-04**).
- **The tool recommends; the human accepts** (**DE-09**). In Phase 1 it does not even recommend. It
  reports.

**Why the MVP is deliberately this small.** The previous attempt failed by putting an optimiser on
top of an unmeasured foundation. Optimisation cannot be proven without a baseline, and there is no
baseline today: **several of the initiative's primary KPIs do not exist as a live number anywhere.**
Capturing them is not preparation for the work — it *is* the first release.

---

## 2. Prerequisites — two unmet policy decisions block everything

**These are not data problems. They are policy decisions wearing data clothing**, and no amount of
integration work substitutes for someone deciding them.

| ID | Decision required | War-list ref | Owner | Status |
|---|---|---|---|---|
| **SH-07** | **The point system.** Point value per visit type × discipline. How travel is treated. | `G1` (P0) | *unassigned* | **OPEN** |
| **SH-08** | **The productivity target and ceiling.** The expected-points rule by FTE × discipline. | `G5`, `W6` (P0) | *unassigned* | **OPEN** |
| — | Productivity status thresholds (the bands a branch is judged against) | `R4` (P0) | *unassigned* | **OPEN** |

### The critical path, drawn

```
   SH-07 point values ──┐
                        ├──▶  C-05 committed load ──┬──▶ C-06 remaining capacity by day
   SH-08 target/ceiling ┘                           ├──▶ C-07 week open capacity
                                                    └──▶ C-08 assessing capacity by discipline
                                                              │
                                                              ▼
                                                     ★ THE ENTIRE MVP OUTPUT
```

> **The four derived variables `C-05`…`C-08` are the whole point of the MVP — "how much room is
> left" — and every one of them is computed from `SH-07` and `SH-08`. Until those two are decided,
> the MVP has nothing to display.**

This is the same finding as **open question #1** from Step 5, reached independently from the data
model. It has been the top open question since 17 August and still has no named owner. **That is the
single largest risk to the release**, and it is a decision, not a build.

---

## 3. How the scope was derived

Four filters over 79 scored variable rows (76 numbered + 3 unnumbered). Every count below is
computed from the inventory, not asserted.

```
  ALL SCORED VARIABLES ....................................... 79
    │
    ├─ Filter 1 · LAYER  ── the envelope, not the coordination
    │    Shared + Capacity ................................... 22
    │    ( Scheduling + Coordination = 57 → out, see §7 )
    │
    ├─ Filter 2 · MVP REQUIRED = Yes
    │    .................................................... 19
    │    ( C-10 ramp, C-11 competency supply = Maybe → v1.1 )
    │    ( C-13 referral volume = No, scoped out )
    │
    ├─ Filter 3 · SOURCEABLE
    │    exists today or reachable at go-live ................ 13
    │    blocked on a P0 policy decision ...................... 4
    │    partial / needs build ................................ 2
    │
    └─ Filter 4 · PHASE-1 POSTURE OVERRIDE
         every variable delivered at READ, regardless of its
         scored posture ......................................  19 in scope
```

### The posture override — the most important line in this spec

Of the 19 in-scope variables, **15 are scored `Control`** — meaning the system *could* decide and
act on them. **In Phase 1, none of them do.** All 19 ship at `Read`: the system surfaces the
information and a person decides.

| | Scored posture (target-state ceiling) | Phase 1 delivery |
|---|---:|---|
| Control | 15 | **Read** |
| Assist | 4 | **Read** |

**This is a deliberate, documented downgrade, and it is the discipline that prevents repeating the
previous failure.** The scored posture is the *ceiling the target state may eventually reach* — not
a v1 commitment. A vendor or build team that reads the inventory as a v1 automation spec has
misread it.

---

## 4. In scope — the 19 variables

**Layer: Shared (the spine both functions depend on)**

| ID | Variable | Constraint | Gating | Source today | Exists? |
|---|---|---|---|---|---|
| `SH-01` | Clinician headcount | Structural | **★** | HCHB / Workday `W1`,`W2` | Yes |
| `SH-02` | Discipline | Structural | **★** | HCHB / Workday `W3` | Yes |
| `SH-03` | Role — assessing vs. assistant | Structural | **★** | HCHB / Workday | Yes |
| `SH-04` | FTE / employment type | Structural | **★** | Workday `W4` | Yes |
| `SH-05` | Approved time off / availability | Hard | **★** | Workday — **HCHB integration exists and is OFF** | Partial |
| `SH-06` | Territory / service area | Structural | **★** | HCHB / config | Yes |
| `SH-07` | **Productivity points per visit type** | Config | — | **`G1` — P0 policy decision** | **No** |
| `SH-08` | **Productivity target & ceiling** | Config | — | **`G5`,`W6` — P0 policy decision** | **No** |
| `SH-09` | Referral inflow / discharge outflow | Event | — | Commure (in) + HCHB (out) | Partial |

**Layer: Capacity (the envelope itself)**

| ID | Variable | Constraint | Gating | Source today | Exists? |
|---|---|---|---|---|---|
| `C-01` | Headcount by discipline & employment type | Structural | **★** | Rolls up `SH-01`…`SH-04` | Yes |
| `C-02` | Branch coverage territory (county) | Structural | **★** | Org hierarchy — **`G2`: no region field on the record today** | Partial |
| `C-03` | Clinician territory assignment (zip) | Structural | **★** | HCHB zip assignment | Yes |
| `C-04` | Census-tract granularity | Config | — | Under evaluation | No |
| `C-05` | Committed load / points scheduled | Derived | — | **Derived — blocked on `SH-07`** | Blocked |
| `C-06` | Remaining capacity by day | Derived | — | **Derived — blocked on `SH-07`,`SH-08`** | Blocked |
| `C-07` | Week open capacity | Derived | — | **Derived — blocked on `SH-07`,`SH-08`** | Blocked |
| `C-08` | **Assessing capacity by discipline** | Derived | — | **Derived — blocked on `SH-07`,`SH-08`** | Blocked |
| `C-09` | Per-diem / flex capacity | Structural | **★** | Per-diem roster — largely manual | Partial |
| `C-12` | On-call / weekend rotation load | Structural | **★** | Manual today | Partial |

**★ = gating.** Eleven of the nineteen. **A product that cannot carry a gating variable is
disqualified however well it scores elsewhere** — this is a knockout, not a weighting.

> **`C-08` is the headline output.** SOC-capable clinician availability is the binding constraint on
> branch growth (`CP-3`) and the overload cycle locks a branch at its volume indefinitely. **A number
> for `C-08`, visible daily, is the single most valuable thing this release produces.**

---

## 5. What the MVP actually shows

Four views. Nothing else in v1.

| View | Answers | Built from |
|---|---|---|
| **The envelope** | What can this branch deliver this week, by discipline and territory? | `SH-01`…`SH-06`, `C-01`…`C-03`, `C-09`, `C-12` |
| **Open room** | How much is left — by day, by week, by discipline, by territory? | `C-05`, `C-06`, `C-07` |
| **Assessing capacity** | Can we accept this referral? How many SOCs can we take? | `C-08` — *the growth question* |
| **Inflow vs. outflow** | What is arriving, what is discharging, against the envelope? | `SH-09` |

**And one thing the MVP must do that is not a view: capture the baseline.** Several primary KPIs
have no live value today. The first release's quieter job is to start the clock on
*quantified capacity and utilisation* — measured maximum deliverable visits per week versus what is
actually delivered — so that anything built later can be proven against it.

---

## 6. Which business case levers v1 proves

**Honest answer: the MVP proves the capacity case, not the scheduling case.** Roughly 60% of
full-product value is modelled to land at MVP; this is which part.

| Lever | Depends on | In v1? |
|---|---|---|
| **W5 · PTO collision avoidance** | `SH-05` | **Yes — and it is free.** The Workday↔HCHB integration exists and is switched off |
| **W3 · Premium labour offset** | `C-06`, `C-07`, `C-09` | **Yes.** Forward visibility converts reactive premium coverage into planned coverage |
| **W4 · Overtime reduction** | `C-05`, `C-06` | **Yes.** Same mechanism |
| **G1 · SOC capacity as the growth constraint** | `C-08` | **Yes — the largest upside.** Visibility only; realisation needs the acceptance decision to change |
| **U1 · Discipline & role match** | `SH-03` | **Partial.** v1 makes the assessing-vs-assistant load *visible*; acting on it is `S-15`, which is v2 |
| W1 · Scheduler capacity released | scheduling automation | No — v2 |
| W6 · Travel and drive time | `S-18` routing | No — v2 |
| R1 · Non-billable visit avoidance | authorization state | No — v2 |
| R2 · LUPA leakage recovered | period + plan-of-care data | No — v2 |
| U3 · Rebook waste | `S-38`, `CO-08` | No — v2 |

> **State this plainly at the pilot readout:** v1 cannot move `W1`, the largest single hard lever,
> because that lever lives in the scheduling layer. Promising it from a visualisation release is how
> a successful pilot gets called a failure.

---

## 7. Deliberately not in v1

**57 variables — the entire Scheduling and Coordination layers — are out.** 30 of them are scored
MVP-required and 25 are gating, which is why the exclusion must be stated deliberately rather than
left to inference: they are gating **for the full product**, not for Phase 1.

| Excluded group | Count | Reason | Re-entry trigger |
|---|---|---|---|
| **Scheduling — demand & compliance** (`S-01`,`S-02`,`S-03`,`S-35`,`S-36`, Insurance Authorization, Add-On Orders) | 7 | The envelope must be measurable before visits are allocated against it | v2 scope opens once `C-05`…`C-08` hold a trustworthy number for ≥ 1 quarter |
| **Scheduling — matching & constraints** (`S-15`,`S-16`,`S-21`,`S-33`, caregiver, clinical timing) | 12 | Matching is allocation. Phase 1 does not allocate | With v2 |
| **Scheduling — clinician pattern & routing** (`S-04`…`S-14`,`S-17`…`S-20`) | 15 | Requires clinician-supplied availability, which needs the adoption work first (**DE-09**) | After the clinician-facing view lands |
| **Coordination — all** (`CO-01`…`CO-12`) | 12 | Engagement is a third module; several items need legal review on automated outreach | Phase 3, gated on the consent and robocall review |
| **Distribution & exception** (`S-37`…`S-42`) | 6 | Depends on a live schedule the MVP does not produce | With v2 |
| **Capacity — deferred** (`C-10` competency supply, `C-11` ramp) | 2 | Scored `Maybe`; both are known coverage gaps but neither blocks the envelope | v1.1 — cheap additions once the roster feed is live |
| **Capacity — scoped out** (`C-13` referral volume) | 1 | Scored `No`; the demand side is Commure's | Only if the forecast work starts |

**Two exclusions worth defending explicitly, because they will be challenged:**

- **`C-11` orientation / ramp status** is a known gap — new clinicians are counted at a full capacity
  they cannot yet carry, so the envelope reads high. It is out of v1 only because it is cheap to add
  once the roster feed exists, not because it does not matter. **Flag the distortion on the view
  until it lands.**
- **Routing and drive time** (`S-18`, `C-04`) are the largest unmeasured capacity leak in the whole
  operation. They are out because reachability is a *scheduling* answer and the MVP is not
  scheduling. This is the single most likely source of "why doesn't it do X" in the pilot — script
  the answer in advance.

---

## 8. Acceptance criteria

The release is done when all of these hold:

- [ ] `SH-07`, `SH-08` and the threshold bands are **decided, documented and owned** — not inferred
- [ ] All 11 gating variables carry a live value from a named source, refreshed on a stated cadence
- [ ] `C-08` produces a defensible assessing-capacity number per branch per week
- [ ] Every displayed number traces to a war-list row with a confirmed system, report and owner
- [ ] No variable is delivered at `Control` or `Assist` posture — **all 19 ship at `Read`**
- [ ] `C-11` distortion is flagged on any view showing headcount-derived capacity
- [ ] The scheduling grid it replaces is identified per pilot branch, with retirement criteria
      (**DE-04** — do not run both indefinitely)
- [ ] Baseline captured for quantified capacity and utilisation, against a named baseline period
- [ ] Tool adoption is instrumented from day one — *if it is not used, none of the rest happens*

---

## 9. Open risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| **`SH-07` / `SH-08` remain undecided** | **The MVP has no output.** Not a delay — a null release | Assign an owner and a date this week. It is the top open question and has been since 17 Aug |
| Ramp distortion (`C-11` out of scope) | The envelope reads higher than reality on any branch that is hiring | Flag on the view; add in v1.1 |
| Pay-model split unknown | Decides whether the capacity number converts to margin at all, and it inverts by model | Highest-value single input in the business case register. Obtain before the pilot readout |
| Pilot site tension | The best sites for adoption (per-visit offices) are the worst for proving a margin case | Resolve deliberately in the pilot charter, not at readout |
| `C-02` org hierarchy incomplete | Region-level rollups fail; territory views are branch-only | `G2` — confirm the hierarchy source before build |
| "Why doesn't it schedule?" | A visualisation release will be judged against an optimiser people imagined | §1 and §6 are the script. Say it before the pilot, not after |

---

## 10. What happens next

1. **Assign `SH-07` and `SH-08`.** Nothing else on this page matters until they are owned.
2. **Turn on the Workday↔HCHB PTO integration.** Free, immediate, and it delivers `SH-05` — the
   only gating variable currently sitting at Partial for a reason we control.
3. **Run the source war-list session** to fill Confirmed Source / Report / Owner / Refresh / Exists
   for the 19 rows above. Everything returning N or Partial is the build backlog.
4. **Draw the target state** (Step 10), marking each box MVP / v2 / later, so this spec's exclusions
   are visible as phasing rather than as gaps.
