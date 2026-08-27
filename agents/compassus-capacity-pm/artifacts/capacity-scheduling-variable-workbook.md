# Capacity, Scheduling & Engagement — the unabridged variable workbook

> **Mirror for reading on GitHub.** The live instrument is
> [`Capacity-Scheduling-Variable-Workbook.xlsx`](./Capacity-Scheduling-Variable-Workbook.xlsx) — edit there, then regenerate this file with `_capacity-scheduling-workbook.gen.py`.

Every variable in the 19 Aug inventory (87 of them), placed under the three arenas the
workbook itself assigns, in the plain language of the vendor one-pager, with current-state
ownership, where the information lives, and the future-state posture. **Where-it-lives entries
are first-pass hypotheses, not findings** — the confidence column says how much to trust each.


## Capacity Management — Workforce supply

### `SH-01` Clinician headcount

How many clinicians the branch actually has, counted by discipline. The base number every capacity answer starts from.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | HR / Talent — maintains the record |
| Who reads it and decides today | Branch Leadership (ED) — at staffing and budget reviews |
| Where it lives today | Workday — worker record; mirrored into HCHB |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) — owns the exception when the two systems disagree |
| Trigger / how often | Continuous — changes on hire/term |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A clean roster fact in a system of record. The only risk is Workday and HCHB disagreeing.

**Open question:** Which system wins when Workday and HCHB disagree on who is active?

### `SH-02` Discipline

What licence each person holds — RN, LPN, PT, PTA, OT, COTA, SLP, MSW, aide. Capacity is always counted inside a discipline: an RN shortage cannot be covered by a spare PT.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | HR / Talent — maintains the record |
| Who reads it and decides today | — no one reviews this today; it is simply read |
| Where it lives today | Workday — worker record; mirrored into HCHB |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | — exception only |
| Trigger / how often | Continuous — changes on hire/term |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Hard licensure fact, fully in the data.

**Open question:** Are the discipline codes identical in Workday and HCHB, or do they need mapping?

### `SH-03` Role — assessing vs assistant

Whether a clinician can open and evaluate a case (RN, PT, OT, SLP) or only carry follow-up visits (LPN, PTA, COTA). This is the lever behind offloading routine visits so assessing staff are free for admissions.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — derived from discipline, nobody maintains it separately |
| Who reads it and decides today | Clinical Manager / DCS — when deciding what can be offloaded |
| Where it lives today | Derived from discipline |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager — owns offload policy |
| Trigger / how often | Continuous — derived |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Deterministic from discipline. The sensitivity is not the data, it is the change-management of moving work to assistants.

**Open question:** Is the assessing/assistant split written down as policy anywhere, or only understood?

### `SH-04` FTE and employment type

Full-time, part-time, per-diem or contract — and the fraction of a full week each person is expected to work. Sets the ceiling of what any individual can carry.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | HR / Talent — maintains the record |
| Who reads it and decides today | Branch Leadership (ED) — at staffing reviews |
| Where it lives today | Workday — worker record |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) |
| Trigger / how often | Continuous — changes on status change |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Clean employment attribute. Flagged as a conflict risk: a vendor that models FTE differently will fight the branch.

**Open question:** Do per-diem and contract clinicians carry an FTE value at all, or are they null?

### `C-01` Headcount by discipline and employment type

The staffed supply cut both ways at once — how many RNs are full-time, how many are per-diem, and so on. The single largest driver of what a branch can deliver.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | HR / Talent — maintains the record |
| Who reads it and decides today | Branch Leadership (ED) — at staffing and referral-acceptance decisions |
| Where it lives today | Workday — worker record, rolled up |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) |
| Trigger / how often | Continuous |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A branch is only as capable as its thinnest discipline; this is the view that shows it.

**Open question:** Who owns the branch roll-up today — is anyone producing this view at all?

### `C-09` Per-diem and float pool

The flex staff a branch can call on when its core team is full. Per-diem and float clinicians deliberately have no territory — that is what makes them a targeted instrument, used either to absorb admissions or to free a territory clinician for coverage.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Aligned |
| Who does the work today | Scheduler and DCS — work the per-diem list by call, text and Teams |
| Who reads it and decides today | DCS — decides when to spend the float lever |
| Where it lives today | Stated availability lives with the scheduler — a list, a spreadsheet or memory. HCHB holds who they are, not what they will take. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | DCS — decides who to ask and when |
| Trigger / how often | On event — call-outs and admission spikes |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Yes · Y · High |

The size of the buffer is legible; whether it actually flexes is relational. The system can show who is available, never assume they will say yes.

**Open question:** Is there a maintained per-diem availability list anywhere, or is it rebuilt from memory each time?

### `C-10` Specialty competency supply

How many clinicians can perform the visits that need more than a licence — wound, IV and infusion, catheter, ventilator, paediatric. Fourteen RNs but only three wound-certified means wound capacity, not RN capacity, is the real constraint.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — partly HR (formal certs), partly nobody (informal competency) |
| Who reads it and decides today | Clinical Manager — knows who is genuinely capable |
| Where it lives today | Workday holds formal licences and certifications. Informal competency lives in the Clinical Manager's head. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Clinical Manager — confirms who is genuinely competent |
| Trigger / how often | Slow-changing — on certification or experience |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Not re-checked today |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Competency lives partly in reputation, not credentials. Surfacing it is useful; scoring it is not.

**Open question:** Is there a competency list per clinician anywhere today, and who would own keeping it current?

### `C-11` Orientation and ramp status

New hires count as headcount long before they carry a full load. Ignoring the ramp overstates supply — a week-two hire is not a full clinician.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | HR / Talent — records hire date and orientation status |
| Who reads it and decides today | Clinical Manager — judges when someone is genuinely at full load |
| Where it lives today | Workday — hire date and orientation status. The ramp curve itself is not recorded anywhere. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Clinical Manager — confirms the real ramp position |
| Trigger / how often | Weekly during onboarding |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Headcount is clear; the true ramp curve is judgment. A system can propose a curve, a manager corrects it.

**Open question:** Is there a standard ramp expectation by discipline, or is it manager-by-manager?

### `C-12` On-call and weekend rotation load

Work carried outside the standard week. A clinician coming off a weekend rotation starts Monday already partly loaded — if the schedule ignores it, the week is over-packed from day one.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Scheduler — maintains the rotation |
| Who reads it and decides today | Clinical Manager — balances the rotation across the team |
| Where it lives today | HCHB — on-call / rotation schedule |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager — owns rotation fairness |
| Trigger / how often | Weekly |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Legible load once the rotation is recorded. The fairness question is human.

**Open question:** Is the rotation kept in HCHB, or on a separate branch calendar?

### `S-12` Willingness to flex

How readily an individual clinician bends their pattern when asked — takes the extra visit, covers outside their territory, moves a day. It is the variable that decides which soft rules can actually be bent under pressure.

| | |
|---|---|
| Also touches | Scheduling, Engagement |
| Placement check | Aligned |
| Who does the work today | Scheduler and DCS — learn it by asking, over time |
| Who reads it and decides today | Scheduler — decides who to ask first |
| Where it lives today | Nobody's system. It lives in the scheduler's and DCS's working knowledge of their team. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Scheduler / DCS — decide who to approach |
| Trigger / how often | On event — coverage and surge |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | On event — coverage and surge |
| MVP · Gating · Adoption sensitivity | Maybe · N · High |

A purely relational variable: the act of automating it changes what it measures. Surface who has said yes before; never auto-assign on it.

**Open question:** Would clinicians accept this being visible at all? This is a trust question before it is a data question.

### `S-13` Willingness to take extra visits or overtime

Whether a clinician will go beyond target, and on what terms. Strongly tied to pay model — a per-visit clinician has a reason to say yes that a salaried one does not.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Aligned |
| Who does the work today | Scheduler — asks, one clinician at a time |
| Who reads it and decides today | Scheduler / DCS — decide who to approach for coverage |
| Where it lives today | Nobody's system. Pay model is in Workday; willingness is not recorded anywhere. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Scheduler / DCS |
| Trigger / how often | On event — coverage and surge |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | On event — coverage and surge |
| MVP · Gating · Adoption sensitivity | Maybe · N · High |

Relational and pay-linked. This is the row that connects to the incentives idea in the one-pager: today there is no mechanism, only a phone call.

**Open question:** If we attach an incentive to hard-to-fill visits, who sets it and who approves the spend?


## Capacity Management — Availability & reach

### `SH-05` Approved time off and working availability

The days each clinician is not available, and the pattern they normally work. The cleanest shared fact in the whole model: it removes capacity and removes a schedulable slot at the same moment.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Clinician requests it; HR / manager approves it |
| Who reads it and decides today | Scheduler — works around it when building the week |
| Where it lives today | Workday — time-off record. NOTE: the Workday-to-HCHB integration is currently OFF, so availability is re-entered by hand in HCHB. |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Scheduler — owns the exception when it is late or missing |
| Trigger / how often | Continuous — as requests are approved |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A firm blackout once it is in the field. The integration being off is the single highest-value plumbing fix on this sheet — it makes every capacity number stale.

**Open question:** What would it take to turn the Workday-to-HCHB availability integration back on?

### `SH-06` Territory and service area

Where the branch is responsible for covering, and which of that area each clinician works. Capacity in the wrong place is stranded capacity — it exists but cannot reach the patient.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Branch Leadership and DCS — set the lines |
| Who reads it and decides today | Branch Leadership (ED) — reviews alignment when capacity tightens |
| Where it lives today | HCHB holds branch coverage; clinician zip assignment is part HCHB, part local knowledge. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Branch Leadership (ED) — approves any territory change |
| Trigger / how often | Quarterly, or when capacity tightens |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Territory lines look fixed but encode local knowledge and standing agreements. A tool should propose changes, never redraw them.

**Open question:** Is the current zip-to-clinician assignment complete in HCHB, or does the scheduler hold part of it?

### `C-02` Branch coverage territory

The counties the branch has committed to serve. Sets the outer boundary — a gap here is a coverage hole no amount of scheduling can fill.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Branch Leadership — sets it |
| Who reads it and decides today | Branch Leadership (ED) — at growth and referral decisions |
| Where it lives today | HCHB — branch configuration |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) |
| Trigger / how often | Config — set once, revisited rarely |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Fixed boundary, cleanly held in configuration.

**Open question:** Does the recorded coverage area match what the branch actually accepts in practice?

### `C-03` Clinician territory assignment

Which zip codes each clinician covers. Territories were originally drawn on thin data and have stayed largely static, with no live relationship to where referrals are actually coming from — so capacity drifts away from demand quietly.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | DCS and Scheduler — assign and adjust |
| Who reads it and decides today | Branch Leadership (ED) with DCS — at the joint review when capacity tightens |
| Where it lives today | HCHB holds the assignment where it has been entered; the working version is often the scheduler's own reference. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Branch Leadership (ED) with DCS |
| Trigger / how often | Quarterly, or on demand shift |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · High |

Called out in the inventory as the initial variable in the whole equation. Pairing it with a live census heat-map is the highest-leverage capacity change identified.

**Open question:** How current is the zip assignment in HCHB right now — and when was it last reviewed against referral patterns?

### `C-04` Census-tract precision

Whether to model coverage at a finer grain than zip. One large zip can span an urban core and a rural edge with completely different drive times, so the zip average misleads in both directions.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — not done today |
| Who reads it and decides today | Initiative team — a modelling decision, not an operational one |
| Where it lives today | Not in any system. Census data is public; the decision is ours. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Initiative team — decide once, deliberately |
| Trigger / how often | One-time decision |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A modelling choice, not a live control. It reshapes both the capacity map and the routing at once, so it should be decided on purpose rather than inherited from a vendor default.

**Open question:** Do we want to make this call before vendor selection, or let the shortlist show us what is practical?

### `C-14` Territory currency

Whether the territories are still right. C-03 records what each territory is; this records whether it still matches where the patients actually are, and how far the two have drifted. The drift is invisible until capacity is stranded in one zip while the area next to it turns work away.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — not done today |
| Who reads it and decides today | Branch Leadership (ED) with DCS — at the joint review when capacity tightens |
| Where it lives today | Not captured. It would come from comparing the territory assignment in HCHB against actual caseload and referral distribution. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Branch Leadership (ED) — redrawing a boundary is a leadership act |
| Trigger / how often | Quarterly |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Added 19 Aug. The workbook's own example is the whole argument: one territory carrying about thirty patients across two full-time clinicians while the adjacent area declines starts. The tool proposes the misalignment; a person moves the boundary.

**Open question:** What cadence do we want for territory review, and who convenes it?

### `S-46` Achievable first-visit time

The earliest visit a clinician can actually secure, as distinct from the time they would like to start. Nothing records the gap between the two — and that gap is the clearest measure of a day lost to the caseload rather than to any decision anyone made.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — not measured today |
| Who reads it and decides today | — no one today |
| Where it lives today | Not captured. It has to be asked, not inferred. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Clinical Manager — owns the gap as a problem to work |
| Trigger / how often | Weekly |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Maybe · N · High |

Added 19 Aug, and deliberately read-only. Inferring the preference from observed start times would record defeat as choice and then optimise to preserve it. Ask, record the answer, report the gap.

**Open question:** Who asks, and how often? This only works if the answer is collected rather than derived.


## Capacity Management — The capacity math

### `C-05` Committed load — points already booked

How much work is already on each clinician's calendar, in points. Capacity means nothing until you net this off: open room is the ceiling minus what is already committed.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — the system holds it; nobody maintains it |
| Who reads it and decides today | Scheduler — reads it while assigning; Clinical Manager — at productivity reviews |
| Where it lives today | HCHB — derived from booked visits; read through the scheduling and productivity views. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager — acts on the imbalance |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Low |

Derived and safe to compute. The catch is pending-auth visits, which are on no calendar and count toward nothing — so this number is already understated today.

**Open question:** Confirm which HCHB view the branch actually uses for committed points, and whether pending-auth visits appear anywhere in it.

### `C-06` Open room by day

How many bookable points are left in each day once assigned work is subtracted. The operational read of capacity — green means space, red means the day is full.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — not produced as a view today |
| Who reads it and decides today | — no one systematically; the scheduler infers it while assigning |
| Where it lives today | Not produced today. It would be derived from committed load against the daily ceiling. |
| Confidence in that | **Low** |
| Future state | **Automate** |
| Future state — who decides | Scheduler — acts on it daily; Clinical Manager — on the pattern |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Pure derivation, but only as good as the point definitions underneath it. This is one of the clearest 'nobody can see this today' rows.

**Open question:** Does any current HCHB view show open points by day, or is this genuinely net-new?

### `C-07` Open capacity for the rest of the week

The 'how much more can we take this week' number — the one a branch leader actually acts on when deciding whether to accept a referral.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — not produced as a view today |
| Who reads it and decides today | Branch Leadership (ED) — would own the decision it feeds |
| Where it lives today | Not produced today. |
| Confidence in that | **Low** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) — referral acceptance |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Low |

The headline capacity number. Everything else on this sheet exists to make it trustworthy.

**Open question:** What is the decision this number should drive, and who makes it — ED, DCS, or intake?

### `C-08` Admission capacity by discipline

Open capacity limited to the clinicians who can actually open a case. New patients can only be absorbed by assessing staff, so this — not total capacity — is what gates growth.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | — not produced as a view today |
| Who reads it and decides today | Branch Leadership (ED) and DCS — at referral acceptance |
| Where it lives today | Not produced today. |
| Confidence in that | **Low** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) / DCS |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

The growth-gating number. Distinct from total open room and more binding.

**Open question:** How does the branch decide today whether it can take another admission — what is the current proxy?

### `SH-07` Visit weighting — the point value of each visit type

The shared currency. A start of care is worth more than a routine visit, so the same headcount delivers different capacity depending on the mix of work. Everything in capacity and productivity is denominated in these points.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Corporate / Operations — sets the values |
| Who reads it and decides today | Clinical Manager and Branch Leadership — read productivity against them |
| Where it lives today | HCHB holds point values per visit type; the surrounding policy sits in branch and corporate configuration. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Corporate / Operations — owns the definition |
| Trigger / how often | Config — set once, revisited by policy |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Medium |

The values exist. What is undefined is how travel, documentation time and acuity are treated — and until that is settled, every derived capacity number inherits the ambiguity.

**Open question:** Open question #1: do points account for travel, documentation and acuity, or only visit type?

### `SH-08` Targets and ceilings

The weekly load a clinician is expected to carry and the daily maximum they should not exceed. The target is what we plan toward; the ceiling is what capacity cannot cross.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Corporate / Operations — sets it |
| Who reads it and decides today | Clinical Manager — manages individuals against it |
| Where it lives today | HCHB productivity settings plus branch policy. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Config |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Medium |

A policy constant and a simple lookup. Conflict risk: a vendor with its own opinion about targets will fight branch policy.

**Open question:** Are targets uniform across branches and disciplines, or do they vary?

### `SH-09` Referrals coming in, discharges going out

The two events that move the envelope. A referral consumes capacity when it is assigned; a discharge hands it back. Reading them together is how you see capacity as a shape over the next few weeks rather than a number today.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Intake — receives referrals; Clinician — performs the discharge |
| Who reads it and decides today | Branch Leadership (ED) — reads the balance |
| Where it lives today | Referrals arrive in Commure and land in HCHB; discharges are in HCHB. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Branch Leadership (ED) |
| Trigger / how often | Continuous — as events occur |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Low |

Detecting the events is straightforward. What to do about the trend is the judgment, and it sits with the branch.

**Open question:** Is discharge date reliable enough in HCHB to forecast returning capacity?

### `C-13` Referral volume (held out of scope)

The rate of incoming referrals. Recorded here for completeness and deliberately not treated as a lever in this initiative — it belongs to intake and growth, not to capacity and scheduling.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Intake — receives them |
| Who reads it and decides today | Growth / Branch Leadership — outside this initiative |
| Where it lives today | Commure and HCHB. |
| Confidence in that | **Medium** |
| Future state | **Stays manual** |
| Future state — who decides | — outside this initiative |
| Trigger / how often | Continuous |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | No · N · Low |

Out of scope by choice, documented so the capacity math is transparent about what it holds constant.

**Open question:** Confirm this stays out of scope as the initiative moves into future-state design.


## Capacity Management — Matching

### `S-04` Preferred working days

The days each clinician normally works, including rotations like four long days or a standing Friday off. Baseline availability that scheduling has to respect.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — states it; Scheduler — holds it |
| Who reads it and decides today | Scheduler |
| Where it lives today | Partly HCHB, partly the scheduler's own knowledge. Rotations and swaps are handled informally. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Slow-changing, with informal exceptions |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

A set pattern with informal exceptions — the exceptions are the part no system holds.

**Open question:** Are working patterns recorded in HCHB per clinician, or reconstructed by the scheduler each week?

### `S-05` Preferred start time

When a clinician likes to begin. It anchors the front of the route, and the first visit of the day is the single largest lever on an individual's capacity — an 8am start and a 10am start are very different days.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — states it |
| Who reads it and decides today | Scheduler — decides how far to accommodate |
| Where it lives today | Nobody's system — the scheduler's working knowledge. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Daily, in practice |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Maybe · N · High |

Preferred and possible are two different things. Many clinicians want an early first visit and struggle to make it happen; it takes planning and patient motivation, not just a preference field.

**Open question:** Do we want to set a branch expectation on first-visit time, or keep it individual?

### `S-06` Start-time flexibility

Whether that start time can move day to day. It separates a clinician who will shift to fit a patient window from one who cannot — which is a real scheduling lever, but only if they have told you.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — decides in the moment |
| Who reads it and decides today | Scheduler — asks |
| Where it lives today | Nobody's system. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Scheduler |
| Trigger / how often | Daily |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Maybe · N · High |

Depends on a person's willingness. Assuming it is available damages the trust the whole thing runs on — surface only.

**Open question:** None — this row is intentionally read-only.

### `S-07` Lunch and documentation pattern

Whether a clinician holds time mid-day for a break or for charting. It removes a slot and splits the route into two halves.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — their own habit |
| Who reads it and decides today | Scheduler — builds around it |
| Where it lives today | Nobody's system. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Daily |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

A capturable personal habit. Worth knowing, not worth enforcing.

**Open question:** Would clinicians be willing to record this, or does it feel like surveillance?

### `S-08` Mid-day documentation block

Time reserved specifically for charting, usually mid-afternoon. It consumes schedulable time and shapes the day into segments.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — their own habit |
| Who reads it and decides today | Scheduler — builds around it |
| Where it lives today | Nobody's system. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Daily |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Same shape as the lunch pattern. Note that documentation time is real capacity consumed, and today it is invisible in the point math.

**Open question:** Should documentation time be represented in the point system? Ties to open question #1.

### `S-09` Split shift or mid-day personal break

A gap in the middle of the day — school pickup, an errand — with visits either side. It creates a two-cluster day rather than a continuous one.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — their own routine |
| Who reads it and decides today | Scheduler — builds around it when told |
| Where it lives today | Nobody's system. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Scheduler |
| Trigger / how often | Daily, and it varies |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Maybe · N · High |

A personal daily rhythm that varies. Hard to predict reliably and easily disrupted by a system that assumes it knows — read only.

**Open question:** None — intentionally read-only.

### `S-10` Hard stop — when the day has to end

The time a clinician must be finished by, usually for childcare or a second commitment. Once you know it, it behaves exactly like a hard rule; the difficulty is that knowing it depends on them telling you.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — states it |
| Who reads it and decides today | Scheduler — honours it |
| Where it lives today | Nobody's system. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Daily |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Yes · N · Medium |

A firm edge once known. The knowing is the tacit part.

**Open question:** Is there a place a clinician could record a standing hard stop today?

### `S-11` Maximum visits in a day

The most visits an individual will carry before the day stops working, regardless of what the points allow. It bounds how densely a day can be packed.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — states it |
| Who reads it and decides today | Scheduler — respects it |
| Where it lives today | Nobody's system. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Slow-changing |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

A personal ceiling, capturable and worth confirming. Conflict risk: a vendor that packs to points alone will breach it.

**Open question:** Do we want a branch-level maximum as well as an individual one?


## Scheduling Engine — Availability & reach

### `S-14` Home base — where the day starts and ends

The point each clinician drives from and returns to. A first visit far from home wastes the front of the day, which is the most productive part of it.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Differs — the one-pager groups this under Capacity Management |
| Who does the work today | — captured informally, if at all |
| Who reads it and decides today | Scheduler and Clinician — when building the route |
| Where it lives today | Home address is in Workday. Whether it is usable for drive-time is unconfirmed; routing today works off manual knowledge. |
| Confidence in that | **Low** |
| Future state | **Automate** |
| Future state — who decides | Scheduler — confirms the anchor |
| Trigger / how often | Slow-changing |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

A legible anchor once captured. Using home addresses for routing has a privacy dimension worth settling early.

**Open question:** Can we use clinician home addresses for drive-time calculation, and has that been agreed with them?


## Scheduling Engine — Demand

### `S-01` Ordered visits and frequency

What each discipline has ordered for a patient and how often — the demand signal at the visit level. Everything scheduling does is placing these orders into slots that work.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — plots the frequency in the plan of care; DCS — approves it |
| Who reads it and decides today | DCS — approves the plan of care before anything can be scheduled |
| Where it lives today | HCHB — plan of care and generated visits |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | DCS — owns plan-of-care approval |
| Trigger / how often | Per episode, at plan of care and at each recertification |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Clear in HCHB. Note that each discipline plots to clinical need without seeing payer limits at that moment — which is where the auth collision starts.

**Open question:** Nothing outstanding — this row is solid.

### `S-02` Visit type

What kind of visit each one is — start of care, routine, recertification, resumption, discharge, supervisory. It sizes the slot and dictates who is allowed to perform it.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — set by the order |
| Who reads it and decides today | Scheduler — reads it when assigning |
| Where it lives today | HCHB — visit record |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | — exception only |
| Trigger / how often | Per visit |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Clean order attribute.

**Open question:** Nothing outstanding.

### `S-43` Insurance authorization

Whether the payer has agreed to pay for the visits, and how many. It behaves two completely different ways: at admission it is a gate — nothing schedules until it clears — and inside the episode it is a silent ceiling checked visit by visit.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Auth team — verifies eligibility and keys the pending auth; Intake — gives final approval |
| Who reads it and decides today | Auth team, then Intake — and the Scheduler holds what is stuck |
| Where it lives today | HCHB holds auth status per visit; the referral side sits in Commure. The payer's actual rules are written by the auth team into a coordination note at verification — days before anyone writes the plan of care. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Scheduler — owns what falls out; Auth team — owns the exception |
| Trigger / how often | Per episode and per add-on order |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

The largest single bottleneck in current-state scheduling, and the most tractable: the rules already exist in writing before they are needed. Surfacing the coordination note at plan-of-care creation is the highest-value, lowest-complexity win identified. Pending-auth visits sit on no calendar and count toward nothing — if you cannot see it, you cannot plan it.

**Open question:** Can the auth coordination note be surfaced into the plan-of-care screen, and who owns that change?

### `S-44` Add-on orders

Any order written after the plan of care is submitted. In steady state there is no recurring scheduler workflow at all unless an add-on changes the frequency — at which point it routes through DCS approval, then authorization, then back to the scheduler, for every affected discipline.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Clinician — requests; DCS — reviews |
| Who reads it and decides today | DCS — decides, then it returns to the auth loop |
| Where it lives today | HCHB — orders. The DCS review workflow itself is described as still being defined. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | DCS |
| Trigger / how often | On event — mid-episode |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Flagged in the inventory as a bottleneck awaiting DCS workflow. It affects how capacity looks as well as what gets scheduled.

**Open question:** What is the current DCS add-on workflow, and is it consistent across branches?

### `S-03` Ordered-frequency window

The date range each ordered visit has to land inside. A visit delivered outside its window is a compliance miss even though the care happened.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — HCHB applies the rule |
| Who reads it and decides today | Scheduler — works to it; Clinical Manager — on exceptions |
| Where it lives today | HCHB — calculated from the order |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Scheduler — owns the exception |
| Trigger / how often | Per visit |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A hard, legible clock — among the safest things to enforce automatically.

**Open question:** Nothing outstanding.

### `S-35` Start-of-care timing window

The clock that starts when a referral is accepted. Every start of care is time-sensitive — seen within 48 hours under Medicare guidelines. 'Urgent' does not mean time-sensitive; it means a clinical priority flag on top of an already-tight clock.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Scheduler — books it inside the window |
| Who reads it and decides today | Scheduler; DCS — when it is at risk |
| Where it lives today | HCHB — referral and visit dates |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Scheduler; escalates to DCS |
| Trigger / how often | Per referral |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A hard regulatory clock, fully clear — described in the inventory as the safest automation win available.

**Open question:** Nothing outstanding.

### `S-36` Recertification and face-to-face windows

The windows that bind the end of an episode — the recertification visit must fall in the last five days, and the face-to-face encounter has its own requirement. They bind only the disciplines that are actually recertifying.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — HCHB applies the rule; Clinician performs the visit |
| Who reads it and decides today | Clinician — decides whether to recertify; DCS — approves |
| Where it lives today | HCHB — episode dates and visit records |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | DCS |
| Trigger / how often | Per episode |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Regulatory window; enforce and flag. Recert visits are already on the calendar from the original plan of care.

**Open question:** Nothing outstanding.

### `S-49` How far behind the review queues are

The depth and age of the plan-of-care QA queue and the physician-order approval queue. QA is a hard stop — nothing schedules until it clears — so when the queue runs behind, an assistant waits and a week of care compresses into a few days.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | QA and Clinical Manager — work the queue |
| Who reads it and decides today | — no one downstream can see it today |
| Where it lives today | HCHB holds the queues. Their depth and age are not surfaced to the people they block. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | DCS — escalates when the queue is the constraint |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Added 19 Aug. Queue depth and age are countable, but the queue is other people's work — surface it in front of the people it blocks, do not reorder it.

**Open question:** Can queue age be reported daily, and who owns acting on it?


## Scheduling Engine — Matching

### `S-15` Discipline and role match

Putting the visit with someone licensed to perform it. The one genuine hard gate the system enforces by itself — an RN start of care cannot go to a physiotherapy assistant.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — HCHB enforces it |
| Who reads it and decides today | Scheduler — works inside it |
| Where it lives today | HCHB — derived from discipline and visit type |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | — exception only |
| Trigger / how often | Per visit |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · High |

A hard gate and fully legible. The sensitivity is the flip side: auto-assigning routine visits to assistants opens a lot of capacity but is a significant change-management conversation.

**Open question:** How far do we want to push routine visits to assistants, and who owns that decision?

### `S-16` Specialty competency match

Sending visits that need a specific skill to someone who actually has it. It narrows the eligible pool well below the discipline — a hidden hard constraint that only shows up when the match fails.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Scheduler — matches by hand, from knowledge |
| Who reads it and decides today | Scheduler; Clinical Manager — when it is not obvious |
| Where it lives today | Formal certifications in Workday; the working knowledge of who can do what sits with the Clinical Manager and Scheduler. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Clinical Manager — confirms competency |
| Trigger / how often | Per visit |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Only as good as the competency data, which is incomplete today. This is human work performed on information the system does not hold.

**Open question:** Would we build a competency register, and who maintains it?

### `S-33` Matching acuity to skill level

Sending a more complex patient to a more capable clinician. This is clinical judgment, not a rule — the system can recommend, but a person has to own it.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Scheduler — with Clinical Manager input |
| Who reads it and decides today | Clinical Manager — owns the judgment |
| Where it lives today | Acuity signals sit in HCHB; the judgment itself is not recorded. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Per visit, especially at admission |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At recertification |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Clinical judgment with patient-safety consequences. Recommend, never decide. Useful for triage when coverage is short.

**Open question:** Do we have any usable acuity measure today, or is it entirely judgment?

### `S-21` Clinician restrictions

Firm limits on what an individual can be given — no wound care, north territory only, no more than a certain acuity. Set by the branch, and treated as absolute once set.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinical Manager / DCS — set them |
| Who reads it and decides today | Scheduler — works inside them |
| Where it lives today | Not consistently in a system; typically manual, held by the scheduler and Clinical Manager. |
| Confidence in that | **Low** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager — owns the restriction |
| Trigger / how often | Slow-changing |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

A documented hard gate the system should simply honour — but only once it is actually written down somewhere the system can read.

**Open question:** Where are clinician restrictions recorded today? This may be the easiest structured-data win on the sheet.

### `S-22` Continuity of care

Keeping the same clinician with a patient across the episode. It improves outcomes and satisfaction, and the relationship carries real clinical value — but that value is invisible in the data, so an optimiser will trade it away unless told not to.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Aligned |
| Who does the work today | Scheduler — protects it when assigning |
| Who reads it and decides today | Scheduler; Clinician — raises it when broken |
| Where it lives today | HCHB records who has seen the patient; the importance of keeping them is not recorded. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per visit |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Load-bearing but invisible. Protect it explicitly rather than scoring it against efficiency.

**Open question:** How much continuity are we willing to trade for routing efficiency? A policy call, not a technical one.

### `S-37` Supervisory visit dependency

Required supervision visits on a set cadence — an RN must supervise an aide's patient every fourteen days. It chains one person's schedule to another's, which is different from a single assignment.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — HCHB generates it; Clinician performs it |
| Who reads it and decides today | Scheduler — places it; Clinical Manager — on compliance |
| Where it lives today | HCHB — rule-driven visit generation |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per cadence — typically 14 days |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Rule-based and legible.

**Open question:** Nothing outstanding.

### `S-31` Clinically driven timing

Timing set by the medicine, not by preference — a fasting lab in the morning, an insulin-teaching visit aligned to the patient's dose, a wound cadence. It looks like a preference and is not.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — determines it |
| Who reads it and decides today | Clinician — owns it |
| Where it lives today | Clinical detail in HCHB; the scheduling consequence usually in the coordination note. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | Clinician |
| Trigger / how often | Per visit for affected patients |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Clinical judgment with patient-safety consequences — flag it, never decide it. Also the clearest place where a rehospitalisation-risk signal would earn its keep.

**Open question:** Could clinically driven timing be flagged distinctly from preference in the record?

### `S-34` Infection-control sequencing

The order visits are taken in when infection risk is involved — the immunocompromised patient seen before the infectious one, never after.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — sequences their own day |
| Who reads it and decides today | Clinician |
| Where it lives today | Not recorded; applied by the clinician from clinical knowledge. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Clinician |
| Trigger / how often | Daily, when applicable |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Partly rule, partly judgment. A system can propose the sequence and flag conflicts; the clinician confirms.

**Open question:** Are there written sequencing rules, or is this entirely clinician knowledge?

### `S-48` Rehospitalisation risk

How likely a patient is to end up back in hospital, used to decide which visits matter most. A scheduling input as much as a clinical one: it should decide which visit survives a call-out and which patient can tolerate a gap.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — produced by Pulse |
| Who reads it and decides today | — no one uses it for scheduling today |
| Where it lives today | Pulse. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | Clinical Manager / Clinician — decide priority |
| Trigger / how often | Per patient, continuous |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Added 19 Aug. A risk score may inform priority; it may not silently reorder a clinician's day or override clinical judgment. The natural companion to acuity matching when coverage is short.

**Open question:** Is Pulse data reachable from scheduling today, and in what form?


## Scheduling Engine — Routing & the week

### `S-17` Closeness to the rest of the day's route

Whether a candidate visit sits near the ones already booked. Clustering is the primary efficiency lever — it cuts drive time, which converts directly into more visits that fit in a day.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Clinician — groups their own visits by drive time |
| Who reads it and decides today | Clinician; Scheduler — at assignment |
| Where it lives today | HCHB suggests a route; the clinician adjusts it. Drive-time data itself is not held today. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Clinician — adjusts the proposal |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Geometry, and safely reversible. The efficiency gain here is real rather than borrowed from someone's slack.

**Open question:** What routing data does HCHB actually use today — distance, or real drive time?

### `S-18` Route mileage

The total driving in a sequenced day. It is the cost being minimised — high mileage means fewer visits fit, so mileage and capacity are the same conversation.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | — calculated by the routing function |
| Who reads it and decides today | Clinical Manager / Branch Leadership — on cost and efficiency |
| Where it lives today | HCHB routing output; mileage also has a reimbursement and payroll dimension. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Low |

Deterministic routing maths.

**Open question:** Is mileage currently reported anywhere the branch actually looks at?

### `S-19` Order of visits within the day

The sequence the day runs in. Fixed points — a caregiver window, a timed teaching visit — pin the route, and everything else fills around them.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — sets their own order |
| Who reads it and decides today | Clinician |
| Where it lives today | HCHB suggests; the clinician decides. The pinning constraints live in coordination notes. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Clinician |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

A legible skeleton pinned by tacit anchors. Propose the sequence; let the person place the anchors.

**Open question:** Nothing outstanding.

### `S-20` Appointment time windows

Committing to a band of time rather than just a day. It turns a day-level order into a time-level promise — which is what patients actually want, and what the branch is least able to give today.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Aligned |
| Who does the work today | Clinician — agrees it on the confirmation call |
| Who reads it and decides today | Clinician; Scheduler when booked centrally |
| Where it lives today | Partly HCHB, largely agreed verbally the day before. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler / Clinician |
| Trigger / how often | Day before the visit |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Yes · N · High |

Enforceable once captured; capture is the weak point. Standardising this would move patient satisfaction and team efficiency together — and it is a visible change for clinicians.

**Open question:** Do we want to move to committed time windows, and what would that cost in flexibility?

### `S-45` Clinician safety

Market-specific rules constraining when and where a visit may be scheduled, and the alerts a clinician must see before they go. These are requirements, not preferences: one market screens for firearms in the home, other people present, and mental illness — a rule instituted after a clinician was killed in a patient's home.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — raises it; Branch Leadership — sets the rule |
| Who reads it and decides today | Branch Leadership (ED) — owns the policy |
| Where it lives today | Not held in a system today; handled market by market. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Branch Leadership (ED) |
| Trigger / how often | As raised, and by market rule |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Numbered S-45 on 19 Aug. Where it applies the slot is removed from the route rather than flagged for override. Currently invisible to any scheduling logic, and it varies by market.

**Open question:** Which markets have safety rules today, and where are they written down?

### `S-40` Front-loading the week

Concentrating visits early so a missed day later can still be recovered. The stated gold standard is around 42% of the week's work done by Tuesday night.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Clinician — builds their own week |
| Who reads it and decides today | Clinical Manager — reviews the pattern |
| Where it lives today | Derived from the schedule in HCHB. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Weekly |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

A target, not a law. Forcing it flattens the clinician's own rhythm, which costs more than it saves.

**Open question:** Is 42% by Tuesday the standard we want to hold branches to?

### `S-41` Pace against the plan

Whether a clinician is on track against their own planned week so far. It is the early signal that tells you to rebalance on Wednesday rather than discover the problem on Friday.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | — derived |
| Who reads it and decides today | Clinical Manager — acts on it; Scheduler — rebalances |
| Where it lives today | Derived from HCHB scheduled versus completed work. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Daily |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

A derived read, safe to surface. This is the archetype of the pattern you described: the system can produce it, but somebody has to look and act.

**Open question:** Who should own the daily pace read — Clinical Manager, Scheduler, or both?

### `S-42` Balancing the week day by day

Spreading work so no single day is over-packed and none is idle. It protects against both burnout days and wasted ones.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Clinician — balances their own week |
| Who reads it and decides today | Clinical Manager — on the pattern across the team |
| Where it lives today | Derived from the schedule in HCHB. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Weekly |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Optimisable, but it touches human routines — assist rather than dictate.

**Open question:** Nothing outstanding.


## Scheduling Engine — Exceptions

### `S-38` Rebooking a visit that never happened

Recovering a visit that was not worked. Spotting the miss is easy; choosing the new slot pulls in every soft constraint at once, which is why it is slow work today.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Aligned |
| Who does the work today | Scheduler — rebooks |
| Who reads it and decides today | Scheduler; DCS — when it will not resolve |
| Where it lives today | HCHB — visit status. The status the office sees can run hours behind because of the sync lag. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | On event |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Sensing the miss is legible; the recovery pulls the whole problem back in. Note the visit states run scheduled, then documentation pending, then missed — so 'missed' is a late signal.

**Open question:** Can we detect a likely miss earlier than the missed status appears?

### `S-39` Missed-visit documentation

The compliance trail behind a missed visit — the note, and the physician notified within 48 hours. This is a Medicare requirement and a hard stop in the system, and it escalates if it is late.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — documents; Scheduler — notifies the physician |
| Who reads it and decides today | Scheduler; escalates to DCS if the 48 hours lapse |
| Where it lives today | HCHB — missed-visit workflow and notification record |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Scheduler; DCS on escalation |
| Trigger / how often | On event |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · Low |

Workflow and compliance prompting — safe to automate, and already partly automated.

**Open question:** Nothing outstanding.

### `S-50` The blind window before documentation syncs

The gap between a visit happening and its documentation reaching the office. Today the office can only see that a visit was started or is incomplete — a visit performed Tuesday may not sync until Friday, and a started visit is not always one that happened.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Aligned |
| Who does the work today | Clinician — syncs; the delay is nobody's task |
| Who reads it and decides today | — no one measures it today |
| Where it lives today | HCHB, derived from the gap between visit time and sync time. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | Clinical Manager — owns the measure |
| Trigger / how often | Continuous |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Added 19 Aug, and it constrains the whole design: nothing may depend on real-time visit state read out of HCHB. The workbook's example is stark — a clinician who called an ambulance has started a visit that did not happen, and the schedule still reads as worked.

**Open question:** How long is the blind window in practice? Nobody has measured it.


## Engagement — Matching

### `S-25` Times the patient will not accept

A flat refusal of a time band — nothing before eleven, no afternoons. It removes slots outright and reshapes the whole route around it.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler or Clinician — captures it in conversation |
| Who reads it and decides today | Scheduler — schedules around it |
| Where it lives today | HCHB coordination note — free text written by a person, not a structured field. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode, revisited in conversation |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Yes · N · Medium |

Hard once captured, but a stale refusal causes a failed visit — and in practice these soften with relationship. Worth re-testing rather than treating as permanent.

**Open question:** Should refusals carry a review date so they do not calcify?

### `S-26` Preferred visit window

When the patient would like to be seen. Softer than a refusal, but it drives satisfaction and whether the visit actually happens.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler or Clinician — captures it |
| Who reads it and decides today | Scheduler — optimises toward it |
| Where it lives today | HCHB coordination note — free text. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Optimise toward it, confirm before committing.

**Open question:** Nothing outstanding.

### `S-27` Days the patient is committed elsewhere

Standing commitments that block whole days — dialysis on Monday, Wednesday and Friday, a regular clinic appointment. These are hard, and they are patient-reported.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler or Clinician — captures it |
| Who reads it and decides today | Scheduler — schedules around it |
| Where it lives today | HCHB coordination note — free text. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Weekly — when the week is built |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

A standing constraint, but patient-reported — trust and verify.

**Open question:** Could standing commitments be captured as structured dates rather than free text?

### `S-28` Caregiver has to be present

Some visits can only happen when a family member or carer is there — wound-care teaching, insulin, or simply to let the clinician in. It ties the visit to a second person's calendar.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler or Clinician — confirms before booking |
| Who reads it and decides today | Scheduler — and the Clinician on the day |
| Where it lives today | HCHB coordination note — free text. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | Scheduler — confirms with the family |
| Trigger / how often | Per visit for affected patients |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

The clearest 'surface, never decide' row on the sheet: a hard rule, a changing informal input, and a patient-safety consequence if it is wrong.

**Open question:** How often does caregiver availability change mid-episode, and does anyone update the note when it does?

### `S-29` Cognitive and dementia constraints

When a patient cannot safely admit a clinician or follow instruction alone, a caregiver becomes a hard gate and the available windows narrow sharply.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Clinician — identifies it; Scheduler — schedules to it |
| Who reads it and decides today | Clinician — owns the clinical judgment |
| Where it lives today | Clinical detail in HCHB; the scheduling consequence in the coordination note. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | Clinician / Clinical Manager |
| Trigger / how often | Per episode |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At start of care |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Cognition plus caregiver dependency plus safety. Automation must only surface.

**Open question:** Nothing outstanding — but confirm the note reliably reaches the scheduler.

### `S-30` The caregiver's own changing schedule

Scheduling around two moving calendars at once — the patient's and a carer who works rotating shifts. The hardest real case in the whole model, and almost entirely undocumented.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler and Clinician — renegotiate as it changes |
| Who reads it and decides today | Scheduler — with the family |
| Where it lives today | Not recorded anywhere in a durable form. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Scheduler |
| Trigger / how often | Weekly, sometimes more |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Two undocumented moving calendars. A system can show what it last heard; it cannot know.

**Open question:** Is there any value in capturing caregiver availability as structured data, or is it too volatile to be worth it?

### `S-32` Competing medical appointments

The patient's other appointments — dialysis, infusion, a specialist visit — that remove days or windows. Usually surfaces in conversation rather than in the record.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler or Clinician — learns it by asking |
| Who reads it and decides today | Scheduler |
| Where it lives today | HCHB coordination note when captured; otherwise not recorded. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode, and it changes |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | Day before — the confirmation round |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Capturable if reported. The failure mode is a visit booked into an appointment nobody knew about.

**Open question:** Nothing outstanding.

### `S-23` Gender preference

A patient's request for a clinician of a particular gender, often for cultural, religious or comfort reasons — and effectively hard when it applies to personal care.

| | |
|---|---|
| Also touches | — |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler — captures and matches |
| Who reads it and decides today | Scheduler |
| Where it lives today | HCHB coordination note — free text. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At start of care |
| MVP · Gating · Adoption sensitivity | No · N · Medium |

Sensitive. Surface and confirm rather than auto-matching on it.

**Open question:** Is there a policy on how this is recorded and honoured?

### `S-24` Language and cultural match

Pairing a patient with a clinician who shares their language where possible. It materially affects teaching visits, where the whole point is that the patient understands.

| | |
|---|---|
| Also touches | Engagement |
| Placement check | Differs — the one-pager groups this under Scheduling Engine |
| Who does the work today | Scheduler — matches where they can |
| Who reads it and decides today | Scheduler; Clinician — raises it when teaching fails |
| Where it lives today | Languages spoken are not reliably recorded for clinicians; patient language is in HCHB. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At start of care |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Capturable on both sides, and worth confirming specifically for teaching-critical visits.

**Open question:** Do we hold clinician language capability anywhere today?


## Engagement — Before the visit

### `CO-04` New-patient welcome call

The first call to a newly referred patient. Today it carries a real judgment as well as a greeting: is the patient actually home, or still in hospital, or putting admission off? It happens before anyone is sent out, which is precisely why nobody is sent to an empty house.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Scheduler — makes the call |
| Who reads it and decides today | Scheduler — makes the one true judgment call in the current process |
| Where it lives today | HCHB — the visit and the coordination note that follows. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per referral |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Automate the trigger and the routine parts; keep a person on the line for the judgment. This is the highest-value human call in the admission chain.

**Open question:** If outreach is automated, how do we preserve the 'is the patient really home' check?

### `CO-06` Confirming availability before booking

Checking the patient — and where needed the caregiver — can actually make a slot before it is committed. It prevents booking into a window that was always going to fail.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Scheduler — confirms |
| Who reads it and decides today | Scheduler |
| Where it lives today | Not systematically recorded; the confirmation happens in conversation. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per visit at booking |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Feeds directly off the caregiver-availability rows, which are the least reliable data on the sheet. Surface what is known; do not presume it is current.

**Open question:** Nothing outstanding — but this row depends on S-28 and S-30 being right.

### `CO-01` Day-before confirmation

The call that confirms tomorrow's visit will actually happen. It is the single biggest reducer of failed visits — and today every clinician does it by hand, for every patient, every day. The system sends nothing.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | Clinician — calls or texts each patient the evening before |
| Who reads it and decides today | Clinician — and picks the disposition straight afterwards |
| Where it lives today | The call is not recorded. Its outcome shows up as the disposition selected in HCHB. |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | Clinician — takes over when the automated round surfaces a problem |
| Trigger / how often | Daily, day before |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · N · High |

The largest single block of clinician time this initiative can hand back. The one-pager now commits to automating the round and to keeping the schedule pliable until confirmation, so changes can land before the patient is told. The care in the design is that the call also surfaces things a reminder never would.

**Open question:** How do we automate the round without losing what the conversation catches?

### `CO-02` Automated reminders

System-sent reminders ahead of a visit. A clean, low-risk automation that reduces no-shows without consuming anyone's time — and one Homecare Homebase does not do today.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — nobody; this does not happen today |
| Who reads it and decides today | — no one today; this does not happen |
| Where it lives today | Does not exist today. Would need an outbound channel. |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | — exception only |
| Trigger / how often | Per visit |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Deterministic and safe. This is the most obvious quick win in the engagement arena.

**Open question:** Nothing outstanding.

### `CO-03` On-my-way notification

Telling the patient the clinician is roughly twenty minutes out. It is fully derivable from the live route and it materially changes the experience of waiting.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | — nobody; this does not happen today |
| Who reads it and decides today | — no one today; this does not happen |
| Where it lives today | Does not exist today. Would derive from route and position. |
| Confidence in that | **High** |
| Future state | **Automate** |
| Future state — who decides | — exception only |
| Trigger / how often | Per visit |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Deterministic from position and route. Note it implies clinician location tracking, which is a conversation to have deliberately.

**Open question:** Are we comfortable with the location tracking this implies, and have clinicians been consulted?

### `CO-05` Channel and communication preferences

How each patient wants to be reached — text, call or email — and what they have consented to. It decides whether any of the automation above actually lands.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Scheduler — captures it when it comes up |
| Who reads it and decides today | Scheduler |
| Where it lives today | Phone numbers are in HCHB. Channel preference and consent are not systematically held. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Per episode |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At start of care |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Honour it, never assume it. Conflict risk: a vendor with its own communication model may not respect an existing preference store. Consent and opt-out rules also carry regulatory weight.

**Open question:** Where would channel preference and consent live, and who captures it at admission?

### `S-47` Power of attorney and who can sign

Whether someone other than the patient holds legal authority to sign admission consents and to be the contact of record. Where a power of attorney exists the patient's own agreement does not satisfy consent, and some direct that the patient not be contacted at all.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Intake and Scheduler — capture it if it surfaces |
| Who reads it and decides today | Scheduler — decides who to contact |
| Where it lives today | Partly Commure at referral, otherwise manual. Not reliably known before the visit is booked. |
| Confidence in that | **Low** |
| Future state | **Assist** |
| Future state — who decides | Scheduler — confirms who may be contacted |
| Trigger / how often | Per referral, before booking |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At referral / welcome call |
| MVP · Gating · Adoption sensitivity | Yes · Y · Medium |

Added 19 Aug. The failure it prevents is concrete: a nurse arrives for the start of care, the patient cannot sign, and the power of attorney is two states away. The visit is wasted and the clock keeps running.

**Open question:** Where would POA status be captured so the scheduler sees it before booking rather than after?

### `CO-13` A verified number for the right person

The confirmed phone number and reachable channel for the patient and, where it applies, the caregiver or power of attorney — including which of them is the right person to talk to about scheduling. Every piece of coordination depends on this, and today it is scattered.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Intake and Scheduler — capture what they are given |
| Who reads it and decides today | Scheduler — works out who to call |
| Where it lives today | Partly HCHB, partly Commure, partly neither. There is no single verified record. |
| Confidence in that | **Low** |
| Future state | **Automate** |
| Future state — who decides | Scheduler — owns the exception when nobody answers |
| Trigger / how often | Per referral, verified at admission |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | At referral / welcome call |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Added 19 Aug, and distinct from channel preference: a preference is no use without a working number for the right party. The failure it names is reminders going to a disconnected mobile while the daughter who books every visit is never contacted.

**Open question:** Who verifies the number, and at what point in admission?

### `CO-14` Consent to contact, by channel

Which channels we are legally allowed to use — texting, and sharing information with family — and whether the consent has actually been signed. A legal gate rather than a preference.

| | |
|---|---|
| Also touches | — |
| Placement check | Aligned |
| Who does the work today | Clinician — obtains consent at the start-of-care visit |
| Who reads it and decides today | — enforced by rule, not decided by anyone |
| Where it lives today | HCHB, once signed at admission. |
| Confidence in that | **Medium** |
| Future state | **Automate** |
| Future state — who decides | — exception only |
| Trigger / how often | Per episode, signed at the start of care |
| Stays true on its own? | **Stable** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Added 19 Aug, and it puts a hard boundary on the automation the one-pager promises: consents are signed at the start-of-care visit, so no automated texting can precede admission and the readiness call before that first visit is necessarily a voice call.

**Open question:** Does this change what we can promise vendors about pre-admission outreach?


## Engagement — When plans change

### `CO-07` Rescheduling with the patient

Negotiating a new time when the planned one stops working. A system can propose slots; the negotiation itself is a conversation between people.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Clinician — for their own visits; Scheduler — when it comes back to the office |
| Who reads it and decides today | Clinician or Scheduler, depending on who holds it |
| Where it lives today | The outcome lands in HCHB as a rescheduled visit; the negotiation is not recorded. |
| Confidence in that | **Medium** |
| Future state | **Surface** |
| Future state — who decides | Clinician / Scheduler |
| Trigger / how often | On event |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Medium |

Human negotiation around a moving constraint. Note that when rapid reschedule is switched on, a clinician moving their own visit inside the week creates no office work at all — so the volume the office sees is a branch configuration choice, not a fact.

**Open question:** Which branches have rapid reschedule enabled? It changes what the office actually sees.

### `CO-08` Following up a failed or no-show visit

Chasing the visit that did not happen — reaching the patient, rebooking, documenting. Left alone these become both a compliance problem and lost revenue.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Aligned |
| Who does the work today | Scheduler — follows up and rebooks |
| Who reads it and decides today | Scheduler; DCS — when it will not resolve |
| Where it lives today | HCHB — visit status and missed-visit workflow. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | On event |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · Low |

Detection is clean; the recovery pulls in every soft constraint again.

**Open question:** Nothing outstanding.

### `CO-09` Finding coverage when someone calls out

The scramble when a clinician is out. It is owned jointly by the DCS and the scheduler, and it runs on who will actually say yes — calls, texts and Teams messages to full-time and per-diem staff, then reassignment or moving the visit to another day.

| | |
|---|---|
| Also touches | Capacity, Scheduling |
| Placement check | Ruled 25 Aug — moved to Engagement. The 8.19 workbook still has it under Scheduling Engine; write this back to the workbook |
| Who does the work today | DCS and Scheduler — jointly |
| Who reads it and decides today | DCS and Scheduler — jointly; DCS escalates for a start of care |
| Where it lives today | No system holds this. It runs on phone, text and Teams, against the scheduler's knowledge of who might take it. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | DCS and Scheduler — jointly |
| Trigger / how often | On event |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Yes · Y · High |

Runs on the same relational willingness as the per-diem and elasticity rows. A system can assemble the candidate list and reach people directly; it cannot decide who will say yes. This is where an incentive on a hard-to-fill visit would attach.

**Open question:** Would we let the system contact clinicians directly with an open visit, or must a person always make the ask?

### `gap` Incentives and offers on hard-to-fill visits

Surfacing a difficult visit to the clinicians who could take it, with whatever incentive or differential is attached. The one-pager now asks vendors about this and the questionnaire scores it — but no variable in the inventory covers it.

| | |
|---|---|
| Also touches | Capacity |
| Placement check | Aligned |
| Who does the work today | — does not exist today |
| Who reads it and decides today | — no one today; does not exist |
| Where it lives today | Nothing today. Pay model is in Workday; there is no mechanism for a visit-level offer. |
| Confidence in that | **High** |
| Future state | **Assist** |
| Future state — who decides | Branch Leadership (ED) — would own the spend |
| Trigger / how often | On event |
| Stays true on its own? | **Drifts — needs re-contact** |
| Re-checked when | On event — coverage and surge |
| MVP · Gating · Adoption sensitivity | -- · N · High |

A genuine gap, not an oversight: this was added to the vendor ask on 21 Aug and the 19 Aug inventory predates it. Recorded here so the workbook and the questionnaire stay aligned. Next free IDs after 19 Aug are SH-10, C-15, S-51 and CO-15.

**Open question:** Do we add this to the variable inventory as a new ID? It is currently asked of vendors but not modelled by us.


## Engagement — Across the care team

### `CO-10` Coordinating visits across disciplines

Spacing the nurse, the therapist and the aide sensibly across a week rather than stacking two on one day and leaving the patient idle the next.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Ruled 25 Aug — moved to Engagement. The 8.19 workbook still has it under Scheduling Engine; write this back to the workbook |
| Who does the work today | Scheduler — spaces them; Clinician — adjusts |
| Who reads it and decides today | Scheduler |
| Where it lives today | HCHB holds the visits; the spacing judgment is manual. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Scheduler |
| Trigger / how often | Weekly per patient |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Rule-informed but bounded by what a patient will tolerate in a week. Propose, do not dictate.

**Open question:** Is there a standard on how many visits a patient should have in one day?

### `CO-11` Keeping the team and the office in step

The connective work of telling the case manager and the office when something changes. Today it is the coordination-note habit — and how well it works depends entirely on people remembering.

| | |
|---|---|
| Also touches | Scheduling |
| Placement check | Ruled 25 Aug — moved to Engagement. The 8.19 workbook still has it under Scheduling Engine; write this back to the workbook |
| Who does the work today | Scheduler and Clinician — write the notes |
| Who reads it and decides today | Case Manager / Clinical Manager — act on what they read |
| Where it lives today | HCHB coordination notes. |
| Confidence in that | **Medium** |
| Future state | **Assist** |
| Future state — who decides | Clinical Manager |
| Trigger / how often | Continuous |
| Stays true on its own? | **This is the contact** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Logging and notifying is automatable; deciding what deserves an escalation is human judgment.

**Open question:** Nothing outstanding.

### `CO-12` What coordination actually costs

The time clinicians and schedulers spend on coordination rather than care. It is capacity, and today it is invisible — roughly forty-five minutes a day per clinician by one estimate, which is a visit.

| | |
|---|---|
| Also touches | Capacity, Scheduling |
| Placement check | Ruled 25 Aug — moved to Engagement. The 8.19 workbook still has it under Scheduling Engine; write this back to the workbook |
| Who does the work today | Everyone — it is spread across every role |
| Who reads it and decides today | — no one measures it today |
| Where it lives today | Not measured anywhere. |
| Confidence in that | **Low** |
| Future state | **Surface** |
| Future state — who decides | Clinical Manager / Branch Leadership — to act on the trend |
| Trigger / how often | Continuous |
| Stays true on its own? | **Live / computed** |
| Re-checked when | — |
| MVP · Gating · Adoption sensitivity | Maybe · N · Low |

Measure and surface it; do not try to control the people doing it. This is the number that turns the business case from theory into a figure the branch recognises.

**Open question:** Is there an appetite to measure this directly, or should it be estimated from the automation we remove?

