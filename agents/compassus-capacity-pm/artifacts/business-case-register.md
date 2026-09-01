# Business Case Register — Capacity and Scheduling

> **What this is.** Every financially-connected case that can be tied to the capacity and
> scheduling initiative, directly or indirectly, with the mechanism, the evidence, the sizing
> formula, and what has to be supplied before a number can be committed. Laid out to match the
> house business-case format described in
> [`../knowledge/business-case-format-2026-08.md`](../knowledge/business-case-format-2026-08.md):
> hard, countable levers go on the waterfall, probabilistic ones go in the upside panel.
>
> **Status.** Second pass, 26 Aug 2026, after an independent numbers audit. Every dollar figure
> here is ILLUSTRATIVE unless marked otherwise, and is built from national benchmarks where
> Compassus figures do not yet exist. Section 9 lists exactly what finance and operations must
> supply to convert these to committed numbers.
>
> **⚠ This is a benefits register, not a business case.** It has no priced cost side. Section 10
> draws a waterfall with six cost bars and populates none of them. It cannot go to a CFO in this
> form. The costing work is in `ccsi-business-case/cost-of-ownership.md`.
>
> **⚠ It does not supersede the authoritative case.** The finance case of record is
> [`../knowledge/business-case-and-kpis.md`](../knowledge/business-case-and-kpis.md), rendered from
> the ROI & Finance Case tab of the **8.13 workbook, which is authoritative**. That model gives
> **$7.9M a year network-wide** at the Moderate scenario across ~80 branches. This register was
> written without reference to it and reaches different numbers. **Where the two disagree, the
> workbook wins until it is corrected at source.** Known divergences: period count (80,000 vs
> 128,000), revenue protected per avoided LUPA ($1,400 vs $1,200), replacement cost per clinician
> ($40,000 vs $45,000), and branch count. Reconciling them is the first task on this document.
>
> **Corrections applied in this pass**, from the audit in `ccsi-business-case/numbers-audit.md`:
> the circular consistency check removed; the incremental-visit figure corrected from $24M to $14M
> by using marginal rather than fully-allocated cost; the growth lever corrected for the fact that
> 20 percent is an FFS-only margin, not a blended one; LUPA recovery restated from $2.2M to $1.57M
> with a band; the $260M relabeled as Medicare fee-for-service rather than episodic; and the
> scheduler bar marked as missing its ramp, attribution haircut and severance.
>
> **Reimbursement grounding** is in
> [`payer-types-and-episode-economics.md`](./payer-types-and-episode-economics.md) and the sourced
> corpus in [`reimbursement-research/`](./reimbursement-research/).

## 1. The anchors

Two come from the coding business case, which is the only place the home health revenue base has
been written down. The rest come from Compassus discovery.

| Anchor | Value | Source |
|---|---|---|
| Home health revenue | ~549M dollars | Coding business case, upside panel |
| Medicare fee-for-service revenue | ~260M dollars | Coding business case, VBP lever. **This is the HHVBP-eligible base, which is FFS Medicare — not "episodic." Medicare Advantage episodic contracts sit outside it** |
| All other payers, by difference | ~289M dollars, 53 percent of the book | Derived. Includes Medicare Advantage on both episodic and per-visit contracts, commercial and Medicaid |
| Schedulers today | ~300 | Whiteboard session, 13 Aug |
| Schedulers in target state | ~100, with the function deliberately retained | Whiteboard session, DE-10 |
| Clinicians | ~3,000 | Whiteboard session |
| Auth notifications per scheduler per day | 50 to 60, majority non-actionable | Discovery session |
| Scheduler tasks per three-discipline admission | 7 or more | Discovery session |
| Census per full-time RN and LPN pair | 40 to 50 patients | Discovery session |

**A consistency check that does not work, retained as a warning.** An earlier version of this
document divided 260M by the CY2026 base period payment to derive ~128,000 payment periods,
then multiplied by 8.4 visits and checked the implied cost against a 20 percent margin. **That
check is circular and cannot fail.** The 193 dollar cost per visit it relies on is not a
published MedPAC figure; the research corpus derives it as 245 dollars times (1 minus 0.212)
and labels it MODELED and ILLUSTRATIVE. Unwound, the revenue figure cancels out entirely and
the check returns roughly 20 percent for any revenue base. It contains no Compassus data.

**The period count is unresolved and it matters.** The 8.13 workbook models 1,000 Medicare
30-day periods per branch across 80 branches, which is 80,000 periods. Dividing 260M by the
base rate gives ~128,000. Those cannot both be right: 260M over 80,000 implies 3,250 dollars
per period, which needs an average case-mix weight near 1.6. Either the workbook figure is low
or the 260M covers more than traditional Medicare 30-day periods. **Resolve this before any
readout** — every episodic lever scales with it. The workbook is authoritative until it is
corrected at source.

## 2. How the cases are tiered

| Tier | Meaning | Where it goes |
|---|---|---|
| Committed | A countable unit exists today and finance can book it | Waterfall, green |
| Modeled | Mechanism is established and the arithmetic is sound, but a Compassus input is missing | Waterfall, green, flagged |
| Directional | Real, evidenced, but the size depends on behavior we have not measured | Upside panel |
| Not yet valued | Named, credible, deliberately unpriced | Upside panel, as the coding case does |
| Risk avoided | A loss that does not occur. Never a waterfall bar | Stated in the narrative |

## 3. Workforce and administrative cost — the hard core

This is where the countable money is, and it is the part of the case that does not depend on payer
class or clinical judgment.

**W1. Scheduler capacity released.** *Modeled.* The stated shape is roughly 300 schedulers today
to roughly 100 in target state, with the air-traffic-control function deliberately preserved. The
work being removed is the SOC/recert/ROC cycle, the per-discipline assignment burst, auth chasing,
and exception recovery — not routine visits, which are already clinician self-managed. At 200 roles
released and a loaded cost of 60,000 dollars, this is on the order of **12M dollars a year**
gross. The Bureau of Labor Statistics home health scheduler median is 38,090 dollars, about
54,000 fully loaded and 66,000 in year one including recruitment and turnover, so 60,000 is a
fair planning figure. The bar as drawn is still incomplete: it carries **no attribution
haircut, no year-one ramp, and no severance**, the last of which is 3 to 6M dollars and belongs
on the cost side of the waterfall. Even so it is the largest single hard lever in the
initiative. Two honesty notes: not all of it is attributable
to this platform, because part of the reduction comes from workflow automation that should arguably
not exist at all; and the release is phased across the rollout, so year one carries a fraction.

**W2. Authorization notification noise.** *Modeled, and inside W1 — do not add them.* At 55
notifications per scheduler per day across 300 schedulers, at 20 seconds each to open, read and
close, the fleet spends roughly 92 hours a day, about 11 full-time equivalents, on notifications the
majority of which are non-actionable. Named separately because it is the most-cited frustration in
the scheduler's day and the cleanest single demonstration of the problem.

**W3. Premium labor offset.** *Modeled, input missing.* Per diem and float clinicians are a
deliberate capacity instrument, not an exception path. Better forward visibility converts reactive
premium coverage into planned coverage. Sizing is contract and per-diem spend times the share that
is demonstrably reactive. Requires the spend baseline.

**W4. Overtime reduction.** *Modeled, input missing.* Same structure. Requires the overtime
baseline by discipline.

**W5. PTO collision avoidance.** *Committed, near zero cost.* The Workday to HCHB integration
exists and is switched off, so PTO is hand-keyed and five of seven nurses can be approved off the
same day. Turning it on removes manual entry and prevents a class of capacity failure outright.
This belongs in the case because it is free, immediate, and demonstrates the thesis.

**W6. Travel and drive time.** *Directional.* Travel sits on the non-labor side of the payment,
so it is never wage-index adjusted, and it is the largest unmeasured capacity leak. Routing by drive
time rather than centroid distance is the lever. Requires mileage and drive-time baselines.

**W7. Unpaid evening confirmation work.** *Directional, and it inverts by payer class.* Roughly
3,000 clinicians spend about 30 minutes a day, unpaid, in the evening, confirming tomorrow's visits.
Automating it does not reduce payroll, because it was never paid. It converts into one of two
things: retention value, or — on per-visit pay only — additional capacity the clinician can sell.
Under episodic payment an additional visit earns nothing, so this lever pays only on the
non-episodic half of the book. Naming that distinction is what keeps the case credible.

## 4. Revenue capture and leakage

**R1. Non-billable visit avoidance.** *Modeled, input missing.* Visits delivered against pending
authorization that fall outside the payer's backdating window are written off. Backdating windows
run zero to five days at most payers, and the federal condition of participation requires the
initial assessment within 48 hours of referral — faster than many plans' authorization turnaround —
so the branch is structurally forced to work at risk. Sizing is the count of at-risk visits times
the contracted rate times the share that fell outside the window. Nobody has ever counted it. This
is the most under-instrumented dollar in the whole initiative.

**R2. LUPA leakage recovered.** *Modeled, clinically gated.* At a national LUPA rate near 7
percent, roughly 8,900 of 128,000 periods a year are LUPA periods, each losing on the order of 1,200
dollars against the full period payment — about **10.7M dollars of annual exposure**. 81.12 percent
of subsequent-period LUPAs were one visit short. If a quarter of the one-short cases turn out to be
operationally caused — a miss, a reschedule past the period boundary, an authorization hold — and
the visit was clinically indicated, recovery is on the order of **1.57M dollars a year, in a
band of 0.63M to 2.51M**. Three corrections sit behind that restatement: the loss per LUPA
period is nearer 1,500 dollars than 1,200, because a subsequent period carries no first-visit
add-on; the 81.12 percent one-visit-short figure is a **subsequent-period** statistic and was
previously applied to all LUPA periods, overstating the pool by roughly 60 percent; and the 25
percent operational-recoverability rate **appears in no source — it was assumed**, and the
headline scales linearly with it. It belongs in the assumptions block with a sensitivity band.
**The gate is absolute:** the recoverable share is only visits that were clinically indicated and
lost to an operational failure. Nothing here justifies adding a visit to clear a threshold, and a
federal audit found 21 percent of claims just above the threshold non-compliant, with contractors
committed to targeting that cluster.

**R3. Recertification capture.** *Directional.* The scheduling workflow fires only after
recertifying disciplines establish next-period frequency orders, and a new certification period is a
new authorization question. Delay at that seam risks a gap in care and a lost period. Sizing is
periods lost or shortened at recert times the period payment.

**R4. Benefit and cap management.** *Directional, non-episodic only.* Commercial and Medicaid
patients can be inside authorization and out of benefit. Care delivered past an exhausted cap is
unbillable, and the annual cap is invisible at the moment frequency is written. Sizing is unbillable
post-cap visits times the rate.

**R5. Authorization denial and rework.** *Not yet valued.* No authoritative public source exists
for home health denial rates, turnaround, or appeal overturn. Adjacent post-acute evidence shows
denials overturned on appeal at very high rates but appealed only rarely, which implies real money
is abandoned rather than lost. Requires instrumentation before any figure is credible.

## 5. Utilization and margin — episodic only

**U1. Discipline and role match.** *Modeled.* Under a fixed period payment the payment is the same
regardless of which discipline delivered the visit, so an appropriate paraprofessional substitution
converts directly to margin and simultaneously frees the higher-licensed clinician for starts, which
is where growth is blocked. DE-08 already sets the policy: default to the paraprofessional with
explicit opt-out. At a 30 dollar loaded cost differential per visit, therapy at roughly 40 percent
of 1.07M episodic visits, and a 15 percent shift, this is on the order of **1.9M dollars a year** —
before counting the freed evaluation capacity, which is worth more.

**U2. Visit distribution and timing.** *Directional, and deliberately not framed as fewer visits.*
In the flat zone a visit is pure cost, and one extra nursing visit per period cuts period operating
profit by 28 percent. Across the period base, a single avoidable visit per period is roughly
**14M dollars of cost** at a marginal cost of about 109 dollars per visit. An earlier version
of this document used the fully-allocated 193 dollars and reported 24M, which overstated it by
72 percent: fully-allocated cost carries overhead, quality assurance and systems that do not
vary with one more visit. Use marginal cost for incremental-visit questions and fully-allocated
cost only for whole-program questions. The defensible lever is timing and distribution, not volume: the front-loading
evidence found one to two visits per week outperformed higher frequencies, while a delayed first
visit carried four times the rehospitalization odds. Industry visits per period already fell from
10.2 to 8.4 between 2019 and 2024 while discharge to community got worse, so this initiative should
not propose to cut further. It should propose to place the same visits better.

**U3. Rebook waste.** *Modeled, input missing.* A rebooked visit consumes two slots to deliver
one. Under a fixed period payment that waste lands directly on margin rather than showing up as lost
revenue, which makes it a cleaner argument for coordination investment than the lost-revenue
framing. Sizing is the rebook count times the marginal cost of a slot. Requires the missed and
rebooked visit rate, which no public source has and Compassus has not measured.

## 6. Growth and throughput — the largest upside

**G1. Start-of-care capacity as the growth constraint.** *Directional, top of the upside panel.*
SOC-capable clinician availability is the binding constraint on branch growth, and the overload
cycle locks a branch at its volume indefinitely. Every point of admission growth is revenue against
a largely fixed cost base, so incremental contribution margin is well above the average margin. A 2
percent lift on 549M dollars is **11M dollars of revenue**, and the margin on it is higher than the
20 percent rate because the branch infrastructure is already paid for. **But that 20 percent is
MedPAC's FFS-Medicare-only margin, not a blended one.** The all-payer figure is 5.0 percent,
which implies the non-FFS book runs near negative 11 percent. If that holds here, growth on the
non-FFS half is margin-dilutive rather than accretive, and the defensible growth lever is about
**5.2M dollars on the FFS base**, not 11M on total revenue. Compassus's real margin by payer
segment is knowable internally and must replace the national benchmark before this lever is
quoted. Note also that cost-report margins and EBITDA margins are not comparable.

**G2. The enrollment moratorium makes throughput the only growth.** *Context, not a lever.* CMS
imposed a national six-month moratorium on new home health and hospice Medicare enrollment in May
2026, including certain ownership changes. While it holds, growth cannot be bought with new
locations. That converts this initiative from an efficiency program into the growth strategy, and
it is the single strongest framing available for the steering committee.

**G3. Referral source trust and time to initial care.** *Directional.* Referral sources route to
agencies that accept and start reliably. Time to initial care is measurable today and is a
defensible proxy. Declining referrals you cannot staff protects quality but trains sources to route
elsewhere, so the lever is disciplined acceptance rather than either extreme.

**G4. Integration and acquisition onboarding.** *Not yet valued.* With new enrollment restricted,
growth by integration matters more, and the cleanest pilot site is a new-integration or brand-new
branch. A repeatable capacity model shortens the ramp of every future integration.

## 7. Quality-linked revenue

**Q1. Value-based purchasing.** *Directional, use the house convention.* The established modeling
convention here is a 0.5 percent swing on in-scope episodic revenue, which is **1.3M dollars**. The
theoretical maximum adjustment is plus or minus 5 percent, which would be about 13M dollars on the
same base. Two things to carry: the measure set changed, so acute-care hospitalization and emergency
department use were retired after the CY2025 performance year and the claims measures are now
potentially preventable hospitalization, discharge to community, and Medicare spending per
beneficiary; and OASIS functional measures are 40 percent of the total performance score and are
dose-responsive, which ties them directly to visit timing.

**Q2. The quality lever and the utilization lever are the same size.** *Framing.* On our own
arithmetic the VBP band and one visit per period are comparable in magnitude, which means quality
belongs in the case as a peer of margin rather than as a footnote.

**Q3. Star ratings.** *Not a lever.* Two published studies put the consumer-choice effect at
roughly 0.8 percentage points and a statistically insignificant 0.25 percentage points. Do not build
ROI on referral lift from star ratings.

**Q4. Payer contracting leverage.** *Directional.* Per-visit Medicare Advantage stays carry 12
percent higher odds of mid-stay inpatient transfer than episodic ones, with the implied mechanism
being loss of agency discretion over visit mix and timing. A branch that can evidence better
transfer performance inside per-visit constraints is intervening exactly where the payer's own harm
is documented. Against roughly 289M dollars of non-episodic revenue, a 1 percent rate or mix
improvement is **2.9M dollars**.

## 8. Risk avoided, and option value

Neither belongs on the waterfall. Both belong in the narrative.

**Risk avoided.** Threshold-adjacent billing scrutiny, now an active contractor target. The 48-hour
physician notification on missed visits, which is both a Medicare requirement and a system hard
stop. Missed 30-day reassessment and recertification windows. Points-system wage exposure — one
documented case resolved a 44.16 dollar headline point rate to 30.06 dollars an hour actual, a 32
percent gap that is simultaneously a wage-and-hour exposure and a turnover driver. Review Choice
Demonstration states carry additional documentation risk.

**Option value.** The payer rules library is contract-level data that nobody publishes — not CMS,
not the plans — so it must be captured per contract, per branch, at implementation. That is an
onboarding cost and a durable moat. An instrumented platform would hold the first real dataset on
home health authorization turnaround and denial behavior, which federal oversight has formally
asked CMS to start collecting and which does not exist anywhere today. And the electronic prior
authorization requirement effective 1 January 2027 lands inside this initiative's scale phase, so
designing authorization state as a measured input rather than a hard-coded assumption means the
forecast improves on its own when it arrives.

## 9. What finance and operations must supply

Nothing below can be sourced externally. Each one converts a modeled number into a committed one.

| Input | Unlocks |
|---|---|
| Loaded cost of a scheduler role | W1, W2 |
| Contract, per diem and overtime spend baselines | W3, W4 |
| Mileage and drive-time baseline | W6 |
| Count and value of visits written off for authorization | R1 |
| Actual LUPA rate and periods-one-visit-short count | R2 |
| Missed, rescheduled and rebooked visit rates | U3, R2 |
| Cost per payment period by case-mix group | U1, U2 — the ceiling stays directional without it |
| Loaded cost per visit by discipline, including PTA and LPN differentials | U1 |
| Clinician turnover rate and replacement cost | Turnover lever |
| Pay-model split across the branch estate: per visit, hourly, salaried, points | Every margin lever, because the sign changes |
| Actual episodic period count and average period payment | Replaces the derived 128,000 |

**The pay-model split is the highest-value single input.** For a per-visit clinician, cost is linear
and scheduling optimization cannot create margin — only rate negotiation can. For a salaried
clinician the marginal visit is near-free to the ceiling, so unused capacity is a realized loss. The
named pilot candidates are the per-visit offices, which are the best sites for adoption and the
worst sites for proving a margin case. That tension should be resolved deliberately, in advance,
rather than discovered in the pilot readout.

## 10. Proposed waterfall for this initiative

Matching the house layout, with two named workstreams and their own subtotals.

| Bar | Type | Workstream |
|---|---|---|
| Scheduler capacity released | value | Capacity |
| Premium labor offset | value | Capacity |
| Overtime reduction | value | Capacity |
| Platform license | cost | Capacity |
| Implementation and integration | cost | Capacity |
| Capacity steward and analyst roles | cost | Capacity |
| **Capacity Net** | subtotal | |
| Non-billable visits avoided | value | Scheduling |
| LUPA leakage recovered, clinically gated | value | Scheduling |
| Discipline and role match | value | Scheduling |
| Rebook waste removed | value | Scheduling |
| Payer rules library build and upkeep | cost | Scheduling |
| Change management and training | cost | Scheduling |
| **Scheduling Net** | subtotal | |
| **Total net benefit** | net | |

Upside panel, in order of size: start-of-care throughput and growth; value-based performance at the
house 0.5 percent convention; payer contracting leverage on the non-episodic half; clinician
retention; and one deliberately unvalued lever, as the coding case does.

## 11. Anti-double-counting rules

- W2 sits inside W1. Never add them.
- U1 appears once. The freed evaluation capacity it creates is G1, and G1 is upside, not waterfall.
- R2 and U3 overlap where a rebooked visit is also the visit that would have cleared the floor.
  Count it once, in R2.
- W7 pays only on non-episodic patients. Do not apply it to the whole clinician base.
- G1 revenue must be converted at contribution margin, not at the blended 20 percent, and must not
  be added to any lever that already assumes the same freed capacity.

## 12. What this case must never claim

- That visits will be added to clear a payment floor.
- That margin will enter a scheduling objective function or weigh against clinical need.
- That fewer visits per period is itself the goal. Industry utilization has already fallen 18
  percent while discharge to community deteriorated.
- That telehealth can substitute for a floor visit. It counts toward nothing.
- That star ratings will deliver referral growth.
- Any saving that depends on a specific manager working weekends. If it is not encoded as standard
  work, it is not a business case.

## 13. Next step

Build the assumptions model — one sheet of named, editable inputs feeding the waterfall and the
upside panel, so the case can be argued at the assumption level rather than the conclusion level,
and generate the house-format output from it. The inputs in section 9 are the model's input block;
everything else in this register is a formula.
