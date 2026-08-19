# Variable Backlog — rows to add to the workbook

> **What this is.** A running list of variables that exist in our documents or in a source
> conversation but are **not yet numbered rows in the workbook's `Variable Inventory` tab**.
>
> **Why it matters.** The `Functional Scorecard` totals only numbered `Variable` rows. Anything on
> this page is invisible to vendor scoring — a product could score well while failing a hard stop
> nobody counted.
>
> **How to work it.** Add the row to `Variable Inventory`, assign the next free ID in its layer, then
> move the entry to the *Landed* table at the bottom with the ID and date. Append freely — this file
> is meant to grow between sessions.

**Next free IDs:** `SH-10` · `C-14` · `S-45` · `CO-13`
*(S-43 and S-44 are reserved below and not yet in the workbook — do not reuse.)*

> ## ⚠️ ID COLLISION — resolve before numbering anything
>
> The **payer and episode economics** handoff (18 Aug,
> [`../knowledge/payer-and-episode-economics.md`](../knowledge/payer-and-episode-economics.md))
> independently claims `SH-10`–`SH-14` **and `S-43`**. Neither set is in the workbook yet, so this is
> still cheap to fix — but **`S-43` is claimed twice** and IDs are never renumbered once assigned.
>
> | Code | This backlog | Payer/economics handoff |
> |---|---|---|
> | `SH-10` | *(listed as next free)* | Hospital discharge date |
> | `SH-11`–`SH-14` | — | Payer class · auth state & pending-auth allowance · payment period & case-mix group · LUPA threshold |
> | **`S-43`** | **Consent / POA signature status** | **Period utilisation against payment (the over-utilisation ceiling)** |
> | `S-44` | POA availability to sign at the visit | — |
> | `S-45` | Insurance authorization | *(overlaps `SH-12` in substance)* |
>
> **Two decisions needed.** (1) Who gets `S-43`. (2) Whether authorization is one shared-spine variable
> (`SH-12`) or a scheduling variable (`S-45`) plus a reference lookup — **right now it is drafted as
> both.** Recommended, not yet agreed: give the payer set `SH-10`–`SH-14` as written, keep `S-43`/`S-44`
> for consent/POA as first reserved, and renumber the over-utilisation ceiling after `S-45`–`S-47` land.

---

## A. In the 8.13 workbook, but unnumbered

These rows exist and are scored, but carry no ID, so they do not roll up.

| Proposed ID | Variable | Layer | Constraint | MVP | Posture | Gating | Note |
|---|---|---|---|---|---|---|---|
| `S-45` | **Insurance authorization** | Scheduling | Hard | Yes | Assist | **Y** | Hard stop upstream of the scheduler's queue. Payer rules already exist in the auth team's coordination note at verification — surface them at plan-of-care creation |
| `S-46` | **Add-on orders** | Scheduling | Hard | Yes | Assist | **Y** | Awaiting DCS workflow. Affects capacity optics and downstream scheduling |
| `S-47` | **Clinician safety — market-specific alerts** | Scheduling | Hard | Maybe | Assist | N | Time blocks and warnings per market. Washington/Providence requires a safety screening script |

## B. Proposed by us, not yet in the workbook

| Proposed ID | Variable | Layer | Constraint | MVP | Posture | Gating | Note |
|---|---|---|---|---|---|---|---|
| `S-43` | **Consent / POA signature status** | Scheduling | Config | Yes | Control | N | Rule-based flag the system can own and block on |
| `S-44` | **POA availability to sign at the visit** | Scheduling | Hard | Yes | Read | **Y** | Only binds when `S-43` is unsigned. Same shape as `S-30` — a fluctuating third-party calendar |

## C. Confirmed as real, no row drafted yet

Named in a source and agreed as material, but not yet specified well enough to score. Each needs a
constraint, MVP flag and posture before it can be added.

| Candidate | Layer | Evidence | Why it is not a row yet |
|---|---|---|---|
| **Drive-time vs. straight-line distance** | Scheduling | 13 Aug — routing is mileage and centroid proximity today | Needs a decision on the routing data source before it can be scored |
| **Physical obstructions / crossing windows** | Scheduling | 13 Aug — the Jacksonville bridge (one zip, two non-interchangeable sides); the California interstate crossing window | Is it a territory attribute or a routing penalty? Placement decides the layer |
| **Self-serve open-visit / shift finder** | Scheduling or Engagement | 13 Aug — HCHB's Shift Finder exists and is **not turned on**; NVA coding already pays differentiated rates | Straddles two layers; also an incentive-policy decision, not only a variable |
| **Clinician hand-off to own assistant** | Scheduling | 13 Aug — HCHB blocks a nurse handing a visit to her own LPN, and blocks an RN seeing her supervisee's schedule. Both HCHB design choices, not Medicare rules | Needs pairing with the accept/decline loop below |
| **Assignment accept / reassign / decline + reason** | Scheduling | The Alabama lesson; DE-09 "the tool recommends, the human accepts". **Refined 18 Aug: all three are clinician selections in HCHB, taken the day before the visit. Reassign returns the visit to the scheduler *with* a recommendation; Decline returns it *without* one, and the branch places it with someone other than the original clinician.** | The *facts* are captured. What is missing is the **reason**, and the content of the reassign recommendation — which is the clinician already doing the tool's job by hand, and the best training signal in the process |
| **Plan-of-care QA / DCS clearance state** | Scheduling | 13 Aug — POC QA must clear before the first week can be assigned | Sibling of `S-45`; may fold into a single readiness state |
| **Pending-auth visit visibility** | Capacity | 13 Aug — pending-auth visits are invisible and do not count toward productivity. *"If you can't see it, you can't plan"* | Arguably a capacity-measurement defect rather than a new variable — decide which |
| **Clinician weekly self-planning logic** | Scheduling | Post-session correction — in steady state the clinician plots their own week, and that logic is entirely undocumented | The largest undocumented decision process in the model |
| **Rapid reschedule (HCHB setting)** | Scheduling | 18 Aug — when the flag is on, a reschedule inside the week generates **no scheduler workflow at all**. When it is off, the same move costs the scheduler a queue item | A configuration flag rather than a clinical constraint. Decide whether branch-level config belongs in the inventory or in a separate environment profile |

## D. Watch list — changes to existing rows

| Row | Change | Status |
|---|---|---|
| `S-23` Gender preference | MVP `Yes` → `No` (8.13) | Applied to our documents |
| `S-25` Time-of-day refusal | `Hard` → `Soft` (8.13) | Applied to our documents |
| `S-07` | Renamed *Lunch / documentation pattern* (8.13) | Applied to our documents |
| `S-15` Discipline / role match | DE-08 — default to the paraprofessional with **explicit opt-out**. Changes the behaviour, not the row | Needs a note on the row |
| All postures | DE-03 — Phase 1 is **visualization only**. Postures describe the target, not release 1 | Needs a header note on the tab |

## E. From the payer & episode economics handoff (18 Aug)

Proposed as a shared-spine block, because both capacity and scheduling consume them. **All six are
pointers to reference data that does not exist in structured form yet** — adding the row is the small
half of the job. See the collision box above before assigning codes.

| Proposed ID | Variable | Layer | Constraint | MVP | Posture | Gating | Where the value comes from |
|---|---|---|---|---|---|---|---|
| `SH-10` | **Hospital discharge date** | Shared | Hard | Yes | Read | **Y** | The referral, via Commure. Some benefit windows start here, not at admit (CN-14) |
| `SH-11` | **Payer class** (episodic / per-visit / managed care) | Shared | Structural | Yes | Control | **Y** | The referral, via Commure. Financial risk runs in *opposite directions* by class |
| `SH-12` | **Authorization state & pending-auth allowance** | Shared | Hard | Yes | Assist | **Y** | Should be **derived from the payer**, not keyed (CN-12). Overlaps `S-45` — reconcile |
| `SH-13` | **Payment period & case-mix group** | Shared | Derived | Yes | Control | N | Computed. Two 30-day payment periods per 60-day cert period, each with its own group |
| `SH-14` | **LUPA threshold** | Shared | Config | Yes | Control | N | CMS reference data by group; **432 rows, recalibrated annually.** Never hard-code |
| *(code TBD)* | **Period utilisation against payment** — the over-utilisation ceiling | Scheduling | Derived | Yes | **Read** | N | Derived; **stays directional until finance supplies cost per period by case-mix group.** Read posture is deliberate: show the margin consequence, never weigh it against clinical need (CN-06) |

**Also needed, and not a variable:** a **payer rules library** with a record per payer (thirteen fields,
schema in the handoff). Three seed entries exist — UHC, Indiana Medicaid, Ohio Medicaid — **all from
conversation, none from contracts.** Verifying the full book with the auth team is the single largest
content gap in the initiative.

---

## Landed

Move rows here once they are numbered in the workbook.

| ID | Variable | Added |
|---|---|---|
| — | *(none yet)* | — |
