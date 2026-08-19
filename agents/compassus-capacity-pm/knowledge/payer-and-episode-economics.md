# Payer and Episode Economics

> **Source:** `8.18 HAND OFF DOCUMENT FOR PAYER AND HH EPISODE ECONOMICS.docx` — Google Drive
> `1Er-XhCgtRDbaeFdrq9OBsKEjARZLrnLP`, folder `1RPI1ogTdyDeEf64OBRmaRQ0ESNWp5k5o`. Rendered faithfully.
> `CN-##` refers to [`constraint-register.md`](./constraint-register.md).
>
> **How payment works, what it constrains, and the payer rules the Scheduling Engine needs.**
>
> ⚠️ **Variable-ID warning.** This document proposes `SH-10 … SH-14` and `S-43`. **None of them are in
> the 8.13 workbook yet** (the workbook's numbered inventory ends at `SH-09` / `S-42`), and `S-43`/`S-44`
> were separately reserved for consent/POA in
> [`../artifacts/variable-backlog.md`](../artifacts/variable-backlog.md). **The `S-43` code is claimed
> twice and must be resolved before either set is written into the workbook.** See the collision note
> at the end of this file.

## Why this document exists

Three reasons, in order.

1. **The inventory had no payer dimension.** Authorization is the largest single bottleneck in
   current-state scheduling, and until the recent additions nothing in the 76 numbered variables
   represented payer class, authorization state, or the pending-auth allowance that caps how far ahead a
   scheduler can work. The proposed variables **are pointers to reference data that does not yet exist in
   structured form.** This document is that reference data's specification and its first content.
2. **Most authorization pain is self-inflicted, which makes it unusually tractable.** Plans of care are
   written without regard to payer limits, and the frustration arrives at week three. The payer
   information is already captured — the auth team writes it into a coordination note at verification —
   but **nobody reads it at the moment it would change a decision.**
3. **The fastest available win depends on this.** Surfacing payer rules to the clinician at
   plan-of-care creation is high value and low complexity **precisely because the data is already being
   collected. It needs structuring, not gathering.**

## Payer classes — and the direction of risk is opposite between them

Proposed as `SH-11`.

| Class | How revenue works | Direction of risk |
|---|---|---|
| **Episodic** | Medicare under PDGM. A fixed case-mix adjusted amount per **30-day period**, regardless of how many visits are delivered inside it above the LUPA threshold. Revenue does not follow the visit. | **Two directions.** Too few visits triggers LUPA; too many erodes margin. |
| **Per-visit** | Revenue follows the delivered visit. A missed visit is lost revenue. | One-directional and intuitive. |
| **Managed care** | Revenue follows the delivered visit, but **authorization caps what may be delivered** and gates further authorization behind completion and documentation. An unauthorized visit is non-billable. | One-directional, but the constraint is **upstream and administrative**. |

**The design consequence.** The same missed visit means opposite things across these classes. Under
episodic payment it is a LUPA-exposure and outcome-achievement problem, **not lost revenue** — unless it
drops the period below threshold, at which point it is a **cliff rather than a slope**. Any module that
reports financial risk has to compute it **per class**, not by one rule.

**Compassus is majority non-traditional-Medicare today.** The system was built when the business was
roughly 90% traditional Medicare, and the workflow was never rebuilt for a managed-care book — **which is
the root cause of most authorization friction rather than anyone's negligence.**

## Episodic — Medicare under PDGM

### The unit of payment

**A 30-day period.** Not the visit, and not the certification period.

The 60-day certification period is unchanged, so **two 30-day payment periods sit inside one
certification period**, each independently assigned a case-mix group and therefore its own LUPA threshold
and its own payment amount. A sequence of 30-day periods continues until there is a gap of at least 60
days, at which point the next period is classified as *early* again.

Proposed as `SH-13`, and **the single most consequential fact in this document.** Episode shape and
margin must be computed against the **payment** period. *A system that models only the certification
period cannot see the payment cliff it is walking toward.*

### The case-mix groups

**432 groups**, formed by five variables:

| Variable | Values |
|---|---|
| Admission source | community or institutional (2) |
| Timing | early (first 30-day period in a sequence) or late (all subsequent) (2) |
| Clinical grouping | twelve categories based on the primary reason for care (12) |
| Functional impairment level | three levels (3) |
| Comorbidity adjustment | three subgroups (3) |

2 × 2 × 12 × 3 × 3 = 432. The group determines **both the payment amount and the LUPA threshold**, which
is why it has to be known **per period** rather than per episode.

### LUPA — the floor

If a 30-day period's total visit count falls below its group's threshold, the period is paid **national
per-visit amounts by discipline** instead of the case-mix adjusted period rate. **A cliff, not a
gradient.**

Thresholds are group-specific, ranging from **two to six visits**, set at the tenth percentile of visits
observed for that group with a floor of two. They are **recalibrated annually by CMS** — eighteen groups
moved by one visit for CY 2026.

Three implications:

1. **The threshold is reference data, not configuration.** A hard-coded number will be wrong within a
   year. Proposed as `SH-14`.
2. **Exposure is forward-looking.** A Tuesday miss in a period sitting one visit below threshold with
   three days remaining is recoverable. **The alert has to carry the remaining days and the visits still
   needed, not arrive as a next-day report.**
3. **The guard should sit above the floor, not at it.** Planning to exactly the threshold means any
   single miss triggers LUPA.

### The ceiling — over-utilisation

Once a period is at or above its threshold, **every further visit is cost with no matching revenue**.
There is no gradient here either: the period pays what it pays.

Proposed as `S-43`, and **the half of episode economics the earlier design work did not carry.** The
existing distribution variables — front-loading (`S-40`), pace (`S-41`), day-by-day balancing (`S-42`) —
describe the *shape* of delivery but not its *cost against payment*.

> The correct target is therefore neither "as many visits as authorized" nor "as few as possible."
> **It is the clinically right number, above the LUPA threshold and no higher than the period payment
> supports.**

`S-43` carries **Read** posture deliberately. Margin consequence may be *shown*; it may **never** enter an
objective function or weigh against clinical need. The clinician originates frequency (**CN-06**). The
engine's only job is to make the consequence visible **at the moment the decision is made**.

### CY 2026 rate context

Margin pressure is tightening, which raises the value of the ceiling work:

- A **permanent prospective adjustment of −1.023%**, accounting for the difference between assumed and
  actual behaviour change since PDGM began.
- A **one-year temporary reduction of 3.0%**.
- Case-mix weights and LUPA thresholds **recalibrated on CY 2024 claims data**.

### What this means for scheduling

- **Discipline-role match becomes a margin lever, not only a cost-per-visit one** — the period pays the
  same regardless of which discipline delivered the visit.
- **A no-show that is rebooked consumes two slots to deliver one visit.** Under a fixed period payment
  that waste lands directly on margin — a cleaner argument for coordination investment than the
  lost-revenue framing.
- **Utilisation management and scheduling stop being separate concerns. The plan of care is where margin
  is set.**

## Per-visit and managed care

### Authorization as the constraint

For any payer other than traditional Medicare, a referral routes to the authorization team for
eligibility verification and pending-auth keying **before scheduling sees it at all**, then back to intake
for final approval. **This upstream wait is invisible on the current process map and is a bottleneck in
its own right** — *"we know we have the referral, but it's just not in my workflow to schedule yet."*

### Pending authorization

Payers permit a number of visits to be scheduled against pending authorization — **some one, some three,
some five, some ten**. This number caps how far ahead the scheduler can work. Proposed as `SH-12`.

It is keyed by a person today from payer rules that are already knowable, which makes it a **strong
automation candidate: the allowance should be derived from the payer rather than entered.**

Pending authorization means: **see the patient, submit the documentation, and the actual authorization
follows.** It is **not universally payable.** Some payers will not retroactively pay against a pending
auth, and where they do not, a leader decides whether to see the patient as a non-billable visit
(**CN-17**). *That decision should route to the right approver rather than sitting with the scheduler.*

### The gates

Additional authorization beyond the initial allowance is gated three ways depending on payer:

1. **Completion gates.** A proportion of authorized visits must be completed before more are granted.
2. **Documentation gates.** Completion is not sufficient; the documentation must support continued need.
3. **Benefit windows.** A calendar limit that may be keyed to the **hospital discharge date** rather than
   our admit date (proposed `SH-10`), so days elapsed before the start of care consume benefit we never
   used.

A fourth constraint is **structural rather than a gate**: **shared pools**, where several disciplines draw
from one allowance.

### The false constraint worth correcting

Schedulers widely believe additional authorization cannot be requested until the day before or day of the
visit. **That is not a rule** — it reflects a misunderstanding of the system. **Correcting it is training,
not engineering, and it is free.**

## The payer rules library

### Schema

Each payer needs a record carrying, at minimum:

| Field | Note |
|---|---|
| Payer name and plan | And whether rules vary by product line within the payer |
| Payer class | episodic · per-visit · managed care (`SH-11`) |
| Pending-auth allowance | Count of visits schedulable before further authorization (`SH-12`) |
| Pending-auth payability | Whether the payer retroactively pays against pending auth |
| Initial allowance by discipline | How many visits granted at the outset |
| Shared pool | Which disciplines draw from a combined allowance, and its size |
| Completion gate | Visits that must be completed before more are granted |
| Documentation gate | What must be documented to support continuation |
| Benefit window | Duration, **and the date it starts from** (admit or discharge) |
| Discipline substitution rules | Where the payer mandates a specific discipline |
| Authorization turnaround | Observed time from submission to response |
| Urgent-request behaviour | Whether the payer honours an expedited path |
| Source and last verified | Because these change on contract renegotiation |

### Seeded entries

> **These three are sourced from conversation, not from contract documents, and must be verified before
> they are used to drive a scheduling decision.**

**UnitedHealthcare** — managed care.
Initial nursing allowance **5 visits** · completion gate **4 of the 5 completed** · documentation gate:
documentation must support the need for visit 6.
*Practical consequence:* writing a plan of care at twice-weekly for four weeks against a five-visit
allowance **guarantees a week-three problem**.

**Indiana Medicaid** — managed care.
Benefit window **30 days, starting from the hospital discharge date, not our admit date** · nursing
effectively unlimited within the window · therapy **8 visits total shared across PT, OT and ST combined**.
*Practical consequence:* three ordered therapy disciplines split eight visits — roughly four each if two
are involved. **Discharge planning starts on day one**, and a five-day gap between discharge and start of
care consumes a sixth of the benefit.

**Ohio Medicaid** — managed care.
Benefit window **30 days, with the discharge date knowable in advance**.
*Practical consequence:* cited as the case where **capacity can be projected forward**, because the
discharge date is predictable rather than discovered.

**General patterns noted but not attributed to a specific payer**

- Some payers grant **one authorization at a time**, capping the week regardless of ordered frequency.
- Some payers **will not pay for a skilled nursing visit and require an LPN visit instead** (**CN-16**).
- Pending-auth allowances observed at **1, 3, 5 and 10**.

### What we do not have

The library is a **schema with three unverified entries**. Missing:

- Verified rules for every payer in the book, **sourced from contracts rather than recollection**
- **Authorization turnaround times per payer** — nobody in the session knew what the queue time actually is
- The authoritative list of which payers permit pending auth to be used
- Whether rules vary by product line inside a payer
- Ohio Medicaid's therapy and nursing specifics

## Where this data lives today

**In a coordination note.** At verification, the authorization team records the insurance type and what
authorization will look like for that payer. Since an initiative launched early the prior year, they have
also been asked to add a **template snippet of what the clinician needs to know** about that payer.

**And that is the whole mechanism.** The clinician is supposed to reference the note when creating the
plan of care. In practice it is one note among hundreds, arriving **before the moment it matters**, in
free text, **with no prompt at the point of decision**.

> So the problem is not collection. It is that structured knowledge is being stored as prose in a place
> that does not surface at the moment of use. **That is a good problem to have, because it means the fix
> is a schema and a surfacing point rather than a data-gathering programme.**

## Making it structured

Five proposed variables carry this, and each needs a home:

| Proposed ID | Variable | Where it comes from |
|---|---|---|
| `SH-11` | Payer class | From the referral, via **Commure** |
| `SH-12` | Authorization state and pending-auth allowance | **Derived from payer** rather than keyed |
| `SH-13` | Payment period and case-mix group | **Computed** |
| `SH-14` | LUPA threshold | **Looked up from CMS reference data** by group |
| `SH-10` | Hospital discharge date | From the referral, via **Commure** |
| `S-43` | Period utilisation against payment | **Derived**; requires cost data to be precise |

**The surfacing point that matters most is plan-of-care creation.** That is where frequency is written,
where the payer constraint is currently invisible, and where a prompt **changes** the outcome rather than
explaining it afterwards.

## Reference data maintenance

Three separate cadences, and **each needs an owner**:

1. **LUPA thresholds and case-mix weights** — recalibrated annually by CMS, effective with the calendar
   year. **432 rows.** Should live as its own reference file, refreshed each rule cycle, **not embedded
   in a workbook tab**.
2. **Payment rates and adjustments** — annually, with the final rule.
3. **Payer contract terms** — on renegotiation, **which is irregular and easy to miss. A payer rule that
   silently goes stale produces confident wrong scheduling advice, which is worse than no advice.**

The **Capacity Steward** charter is the natural home for the first two. The third belongs with whoever
owns payer contracting, and needs an **explicit handoff** into this library.

## What to find out, and from whom

| Question | Owner |
|---|---|
| **Verified payer rules for the full book** — *the single largest content gap in the initiative* | The authorization team |
| **Authorization turnaround by payer** — measurable from existing data; nobody has measured it | Analytics |
| Which payers permit pending auth to be used, and whether that list is maintained anywhere authoritative | Auth team |
| Whether **Commure** can key pending auth end to end without a human touch, given the allowance is derivable from the payer | Commure / intake |
| **Cost per payment period by case-mix group** — a prerequisite for `S-43` to carry a credible number rather than a directional one | Finance |
| Whether **consent capture can move earlier** than the SOC visit, into the hospital or the Commure intake flow — a patient-engagement blocker rather than a payer question, but it sits in the same upstream conversation | Legal / intake |

**Note on scoping.** The earlier work deliberately treated authorization as intake or revenue-cycle
territory rather than scheduling, in the same way referral volume was scoped out. That was defensible
when the map began at the scheduler's queue. **It is no longer defensible now that the upstream
authorization wait is understood to be a scheduling bottleneck.** The scope should extend to **where
authorization interfaces with scheduling** — not to the authorization team's internal workflow (DE-06).

## Two honest limits

1. **The payer library is a schema with three unverified entries.** UHC, Indiana Medicaid and Ohio
   Medicaid came from conversation, not contracts. They are plausible and they illustrate the pattern
   well, but **they should not drive a scheduling decision until the authorization team confirms them.**
2. **`S-43` stays directional until finance supplies cost per period by case-mix group.** The mechanism
   is right and the direction is right, but *"you're three visits above what this period supports"* needs
   a real cost number behind it before a clinician will believe it.

## References

- CMS, *Calendar Year 2026 Home Health PPS Final Rule* (CMS-1828-F) fact sheet
- CMS, *Home Health Patient-Driven Groupings Model*
- Palmetto GBA, *LUPA Threshold Lookup*
- Applied Policy, *CY 2026 Home Health Rule* summary
- SimiTree, *Resource Utilization Under PDGM*

---

## ⚠️ Variable-ID collision — unresolved

Two independent workstreams have claimed overlapping codes. **Neither set is in the workbook yet**, so
the collision is still cheap to fix — but it must be fixed before either lands, because
`Variable Inventory` IDs are the join key and are never renumbered.

| Code | Claim A — this document (18 Aug) | Claim B — [`variable-backlog.md`](../artifacts/variable-backlog.md) |
|---|---|---|
| `SH-10` | Hospital discharge date | *(free — backlog lists `SH-10` as the next free shared ID)* |
| `SH-11` … `SH-14` | Payer class · auth state & pending-auth allowance · payment period & case-mix group · LUPA threshold | *(unclaimed)* |
| **`S-43`** | **Period utilisation against payment (over-utilisation ceiling)** | **Consent / POA signature status** |
| `S-44` | — | POA availability to sign at the visit |
| `S-45` – `S-47` | — | Insurance authorization · Add-on orders · Clinician safety *(the three unnumbered workbook rows)* |

**Also overlapping in substance, not just code:** backlog `S-45` *Insurance authorization* and this
document's `SH-12` *authorization state and pending-auth allowance* describe the same object from two
sides. **Decide whether authorization is one shared-spine variable or a scheduling variable plus a
reference lookup before numbering either.**

**Recommended resolution** (not yet agreed): give the payer/economics set the shared-spine block
`SH-10 … SH-14` as written, keep the backlog's `S-43`/`S-44` for consent/POA as first reserved, and
renumber this document's over-utilisation ceiling to the next free scheduling ID after the three
unnumbered workbook rows land.
