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

**Next free IDs:** `C-15` · `CO-15` · `SH-14` · `S-52`
*(`SH-10`–`SH-13` and `S-51` are **reserved** for the Tier C reimbursement set — held, not adopted.
Do not reuse them.)*

> ## ✅ ID COLLISION — RESOLVED, 19 Aug 2026
>
> The `S-43` collision flagged here on 18 Aug is settled. **Handoff 1** (19 Aug) assigned the IDs and
> supersedes every earlier reservation on this page. No ID had reached the workbook, so nothing was
> renumbered. Full record:
> [`../knowledge/variable-inventory-update-2026-08-19.md`](../knowledge/variable-inventory-update-2026-08-19.md).
>
> **The two decisions the collision box asked for, both answered:**
>
> 1. **Who gets `S-43`** → **Insurance authorization.** Consent and POA were renumbered.
> 2. **Is authorization shared-spine or scheduling** → **scheduling (`S-43`), not `SH-12`.** The
>    pending-auth allowance is an *attribute* of that row, not a separate variable, which keeps
>    authorization as one concept. The shared-spine `SH-12` draft is dropped.

---

## A. In the 8.13 workbook, but unnumbered

**All three landed 19 Aug.** See *Landed* below.

## B. Proposed by us, not yet in the workbook

**Both landed 19 Aug**, renumbered and reshaped:

- *Consent / POA signature status* and *POA availability to sign at the visit* were **two rows for one
  concept plus a channel gate.** They landed as **`S-47`** (POA status and signing authority — the
  scheduling constraint) and **`CO-14`** (consent state by channel — the legal gate on contacting
  anyone at all). Consent moved to the Coordination layer because it gates a **channel**, not a visit.

## C. Confirmed as real, no row drafted yet

Named in a source and agreed as material, but not yet specified well enough to score. Each needs a
constraint, MVP flag and posture before it can be added.

| Candidate | Layer | Evidence | Why it is not a row yet |
|---|---|---|---|
| **Drive-time vs. straight-line distance** | Scheduling | 13 Aug — routing is mileage and centroid proximity today | Needs a decision on the routing data source before it can be scored |
| **Physical obstructions / crossing windows** | Scheduling | 13 Aug — the Jacksonville bridge (one zip, two non-interchangeable sides); the California interstate crossing window | Is it a territory attribute or a routing penalty? Placement decides the layer. **Partly served by `C-14`**, which measures whether a territory is still right, but not the obstruction itself |
| **Self-serve open-visit / shift finder** | Scheduling or Engagement | 13 Aug — HCHB's Shift Finder exists and is **not turned on**; NVA coding already pays differentiated rates | Straddles two layers; also an incentive-policy decision, not only a variable |
| **Clinician hand-off to own assistant** | Scheduling | 13 Aug — HCHB blocks a nurse handing a visit to her own LPN, and blocks an RN seeing her supervisee's schedule. Both HCHB design choices, not Medicare rules | **Reclassified 19 Aug: not a variable.** A capability and a product constraint — moved to the workbook Parking Lot and to the requirements backlog |
| **Assignment accept / reassign / decline + reason** | Scheduling | The Alabama lesson; DE-09 "the tool recommends, the human accepts". **Refined 18 Aug: all three are clinician selections in HCHB, taken the day before the visit. Reassign returns the visit to the scheduler *with* a recommendation; Decline returns it *without* one, and the branch places it with someone other than the original clinician.** | The *facts* are captured. What is missing is the **reason**, and the content of the reassign recommendation — which is the clinician already doing the tool's job by hand, and the best training signal in the process |
| **Plan-of-care QA / DCS clearance state** | Scheduling | 13 Aug — POC QA must clear before the first week can be assigned | **Landed 19 Aug as `S-49`** (review queue state), which carries both the POC QA queue and the physician-order approval queue |
| **Pending-auth visit visibility** | Capacity | 13 Aug — pending-auth visits are invisible and do not count toward productivity. *"If you can't see it, you can't plan"* | **Resolved 19 Aug: not a separate variable.** The permitted pending-auth count is an attribute of `S-43`; the *visibility* of those visits is a capacity-measurement defect against `C-05` |
| **Clinician weekly self-planning logic** | Scheduling | Post-session correction — in steady state the clinician plots their own week, and that logic is entirely undocumented | The largest undocumented decision process in the model |
| **Rapid reschedule (HCHB setting)** | Scheduling | 18 Aug — when the flag is on, a reschedule inside the week generates **no scheduler workflow at all**. When it is off, the same move costs the scheduler a queue item | A configuration flag rather than a clinical constraint. Decide whether branch-level config belongs in the inventory or in a separate environment profile |

## D. Watch list — changes to existing rows

| Row | Change | Status |
|---|---|---|
| `S-23` Gender preference | MVP `Yes` → `No` (8.13) | **Applied to the Functional Scorecard 19 Aug** — it had never propagated there. Weight 3 → 0 |
| `S-25` Time-of-day refusal | `Hard` → `Soft` (8.13) | **Applied 19 Aug** — Scorecard gating `Y` → `N`, dictionary constraint `Hard` → `Soft` |
| `S-07` | Renamed *Lunch pattern / Documentation Pattern* (8.13) | **Applied to the dictionary 19 Aug** |
| `S-15` Discipline / role match | DE-08 — default to the paraprofessional with **explicit opt-out**. Changes the behaviour, not the row | Needs a note on the row |
| All postures | DE-03 — Phase 1 is **visualization only**. Postures describe the target, not release 1 | Needs a header note on the tab |

> **Standing risk.** The `Functional Scorecard` mirrors the inventory as **literal values, not
> formulas**, so it drifts silently every time a variable changes. All six mirrored columns were
> re-derived from the inventory on 19 Aug. Re-sync on every future change.

## E. From the payer & episode economics handoff (18 Aug) — HELD

**Superseded 19 Aug by Handoff 1 Tier C.** These are recorded on the workbook's `Decisions & Parking
Lot`, **not** in the inventory, and must not influence the Scorecard, the ROI tab or any KPI until the
reimbursement research concludes. Managed Medicare behaviour across UHC, Humana and others is not
settled, and **a single financial rule cannot be applied across the book.**

| Reserved ID | Variable | Change from the 18-Aug draft |
|---|---|---|
| `SH-10` | **Payer class** (episodic / per-visit / managed care) | Was `SH-11`. Taxonomy may need to be finer than three values once managed Medicare variants are mapped |
| `SH-11` | **Hospital discharge date** | Was `SH-10`. Which payers key benefit windows here is exactly what the research must establish |
| `SH-12` | **Payment period & case-mix group** | Was `SH-13` |
| `SH-13` | **LUPA threshold** | Was `SH-14`. CMS reference data, recalibrated annually — reference data, never configuration |
| `S-51` | **Period utilisation against payment** — the over-utilisation ceiling | Code now assigned. Posture would be **Read**: show the margin consequence, never weigh it against clinical need. Also blocked on cost-per-period, which finance has not supplied |
| ~~`SH-12`~~ | ~~Authorization state & pending-auth allowance~~ | **Dropped.** Authorization is `S-43` in the Scheduling layer; the pending-auth allowance is an attribute of it |

The new Shared-layer category these would need — **Authorization & Payer** — has deliberately **not**
been created.

**Also needed, and not a variable:** a **payer rules library** with a record per payer (thirteen fields,
schema in the handoff). Three seed entries exist — UHC, Indiana Medicaid, Ohio Medicaid — **all from
conversation, none from contracts.** Verifying the full book with the auth team is the single largest
content gap in the initiative. Colin's own `S-43` annotation anticipates it: *"State-Specific and known
insurance auth rules should be added to the system knowledge base as this greatly lends to capacity
forecasting and POC mgt."*

## F. Real, but not variables

Reclassified 19 Aug and recorded on the workbook Parking Lot so they are not re-litigated. Each is a
capability, a product limit or a process defect — none is a factor in the equation.

| Item | What it actually is |
|---|---|
| Clinician reassignment authority | A capability. Removes the only recurring scheduler trigger in routine visits — requirements backlog |
| Supervisee schedule visibility | A capability. Without it a nurse manages aide frequency blind |
| Per-discipline task multiplication | A process defect to design out. The fix is care-team recommendation at referral, so later frequency submissions assign to an established member instead of generating a task |
| Clinician schedule horizon (seven days) | A product limit |
| Notification volume | A product defect — a daily regenerating authorization workflow with no available action. The remedy is to notify on state change, **not** to build a better inbox. Some current workflows should cease to exist rather than be automated |

---

## Landed

| ID | Variable | Added | Block · Module |
|---|---|---|---|
| `S-43` | Insurance Authorization | 19 Aug 2026 | `SCH-B` · Scheduling Engine |
| `S-44` | Add-On Orders | 19 Aug 2026 | `SCH-B` · Scheduling Engine |
| `S-45` | Clinician Safety | 19 Aug 2026 | `SCH-D` · Scheduling Engine |
| `C-14` | Territory currency | 19 Aug 2026 | `CAP-B` · Capacity Management |
| `S-46` | Achievable first-visit time | 19 Aug 2026 | `SCH-C` · Capacity Management |
| `S-47` | POA status and signing authority | 19 Aug 2026 | `SCH-J` · Patient Engagement |
| `S-48` | Rehospitalization risk | 19 Aug 2026 | `SCH-K` · Scheduling Engine |
| `S-49` | Review queue state | 19 Aug 2026 | `SCH-B` · Scheduling Engine |
| `S-50` | Documentation sync latency | 19 Aug 2026 | `SCH-M` · Scheduling Engine |
| `CO-13` | Patient & caregiver contact channel | 19 Aug 2026 | `CRD-A` · Patient Engagement |
| `CO-14` | Consent state by channel | 19 Aug 2026 | `CRD-A` · Patient Engagement |

**Inventory now stands at 87 numbered variables.** All eleven are **unscored against both HCHB
products** — scoring them is the next Functional Scorecard action.
