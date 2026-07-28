# HCHB Web Scheduling ↔ Our Capacity Tool — How They Support Each Other

> **Question answered.** Is there a point at which HCHB Web Scheduling can **support the visuals in our capacity
> tool**, feed it data, or serve as the place to **act on what our tool surfaces**? Short answer: **yes, at three
> concrete points** — but the relationship today is *"read-to-inform + hand-off-to-act,"* not a live closed loop,
> and it's gated by whether the queues/worker data are available as a feed and whether write-back exists.
>
> **The two artifacts.** *Our capacity tool* = `invisiblegears` — a 9-tab **Clinician Capacity Management Tool**
> with a real supply→demand **directive engine** (see [as-built spec](../artifacts/capacity-tool-mockup-data-spec.md)).
> *Web Scheduling* = HCHB's browser scheduling cockpit (see [operational spec sheet](./hchb-web-scheduling-operational-spec-sheet.md)).
> **They are complementary, not competing:** our tool is *measurement + matching + forward guidance*; Web
> Scheduling is *execution + the system of record*. The seam between them is where the value is.

---

## 1. The relationship in one picture

```
   OUR CAPACITY TOOL (invisiblegears)                       HCHB WEB SCHEDULING (+ HCHB of record)
   ─────────────────────────────────────                    ────────────────────────────────────────
   measure · match · guide · forecast                       surface exceptions · read/act · record
                                                          
   Worker Productivity grid    ◀── points/completions ──── Productivity Points · (Sched+Comp)/Expected
   Per-Diem remaining capacity ◀── worker week + NVA ────── Worker Calendar flyout
   Worker Trends (missed %/pace)◀── field-return status ─── Status Alerts queue (declined/missed/…)
   Capacity Cockpit demand feed ◀── overflow signal ─────── Smart Scheduling Exceptions ("Max Hours")
   Open-Capacity headline       ◀── validate the metric ─── the capacity % HCHB already shows
                                                          
   7 ranked directives ───────────── propose ────────────▶ scheduler ACTS: Visit List / Worker Calendar
   (referral→fit, offload, backfill,                        (view & triage in web; assign in Citrix today)
    re-engage PD, reassign, extend, park overflow)   ◀───── the trigger: an exception SEEN in Web Scheduling
```

**Read it two ways:** Web Scheduling **feeds** several of our visuals (left arrows), and our tool **proposes what
to do** about what Web Scheduling surfaces, which the scheduler then **executes** back in HCHB (right arrows).

## 2. Direction A — Web Scheduling **supports our visuals** (data in)

Mapping each of our tool's screens to the Web Scheduling data that could power or validate it:

| Our tool (tab / visual) | What it shows | Web Scheduling data that supports it | Strength |
|---|---|---|---|
| **Worker Productivity grid** (Tab 1) — `pointsByDay`, `productivityPct`, completed/in-progress/scheduled/missed bar | Per-clinician points vs. target | **Productivity Points** + visit **status** (Scheduled/Completed/Missed) — the exact inputs; and HCHB's own **capacity %** independently corroborates our `earned/expected` | **High** — same currency, direct feed |
| **Open Capacity headline / KPI** (Entity 4) — "unearned points = admit headroom" | The growth-bridge number | HCHB's `(Scheduled+Completed)/Expected` is the *same idea* live — a **validation source** so our headline matches what the branch already sees on the worker calendar | **High** — reconciliation anchor |
| **Per Diem** (Tab 3) — available vs. scheduled, remaining capacity, **disengagement flag** (≥7 days) | Flex-pool state | **Worker Calendar flyout** (visits + NVA + capacity %) gives remaining capacity; **last confirmed visit / status** informs the disengagement flag | **Medium** — needs worker-level query |
| **Worker Trends** (Tab 4) — 13-wk spark, front-load score, **missed-visit %**, pace | Per-clinician archetype | **Status Alerts** (Missed by Clinician) → missed %; visit **status by day** → front-load/pace | **Medium** — needs history warehoused (our Gap G4) |
| **Capacity Guidance — Cockpit** (Tab 6) — supply/demand matching | The brain's supply side | Worker **remaining capacity** (capacity % + NVA) is a live supply input | **Medium** |
| **Capacity Map** (Tab 7) — zip tiles by RN/PT remaining capacity | Geographic headroom | Patient **Zip/City** + worker **Home Branch**; but Web Scheduling is worker-week grain, **not zone-capacity** — partial only | **Low–Med** |
| **Roster** (Tab 2) — territory zips, PTO, **restrictions/competencies** | Clinician master | Worker card (job desc, home branch, phone); restrictions/competencies live in the **HCHB worker profile**, not this screen — must be sourced separately | **Low** (via HCHB, not the web UI) |

**The headline for "supporting the visuals":** Web Scheduling most directly powers and **validates our
productivity/capacity visuals** — the grid, the Open-Capacity KPI, and the per-diem/trends screens — because it
computes the *same metric in the same currency*. That's not a coincidence to fight; it's a gift: it lets us
**replace our demo-seeded `pointsByDay` with live points** (closing the downstream of our Gap G1) and make our
Open-Capacity number **reconcile to what the branch already trusts.**

> **One overlap to manage deliberately.** Both tools compute a capacity %. **Treat HCHB's as the source of truth
> for the *actuals*** (points scheduled/completed vs. Expected) and layer *our* value on top — weighting
> (travel/doc/acuity), forward projection, SOC-slot separation, and zone grain — rather than publishing a rival
> number the branch doesn't recognize. Same currency, our extra dimensions.

## 3. Direction B — our tool tells the scheduler **what to do about what they see** (action out)

This is the "responding to things seen within that tool" half — and it's the **strongest fit.** Every one of
our seven directives is triggered by an event Web Scheduling now surfaces natively:

| What the scheduler **sees in Web Scheduling** | Our tool's **directive** (Tab 6) | Where they **act** |
|---|---|---|
| **Smart Scheduling Exception** — "Worker at Max Hours" (overflow) | *Park overflow with a front-loader who has headroom*; *reassign before it goes missed*; *extend a per-diem into the maxed zip* | Web Scheduling to view; **Citrix to assign** (today) |
| **Status Alert — Declined / Reassigned** | *Referral/visit → best-fit clinician* (capacity + proximity, per-diem favored) | Visit List / Worker Calendar → assign |
| **Status Alert — Missed by Clinician** | *Reassign behind-pace backlog before it goes missed*; feeds **Worker Trends** missed-% | Reschedule per frequency |
| **Worker Calendar shows a clinician near/over 100%** | *Offload routine RN→LPN / PT→PTA to free assessment capacity* | Reassign routine visits |
| **A discharge / freed slot** (via HCHB) | *Discharge → backfill nearest referral* (perishable slot) | Assign the backfill |
| **A disengaging per-diem** (idle on the Worker Calendar) | *Re-engage the disengaging per-diem* | Our Twilio outreach → then assign |

**The closed loop we're really describing:** *Web Scheduling makes the exception visible → our capacity tool
turns it into a ranked, guardrailed recommendation (who, why, at what cost) → the scheduler executes it back in
HCHB.* Web Scheduling is both the **trigger** (the queues) and the **execution surface** (visit list / worker
calendar), and our tool is the **decision layer** between them that Web Scheduling doesn't have.

## 4. Is there a point? — the honest verdict

**Yes — three concrete points of genuine mutual support:**

1. **A live data source + validation for our capacity visuals.** Web Scheduling computes our core metric in our
   core currency (Productivity Points; `(Sched+Comp)/Expected`). It can feed our Worker Productivity grid,
   Open-Capacity KPI, per-diem, and trends screens, and make our numbers **reconcile to what the branch already
   sees** — retiring the demo-seeded data behind those visuals.
2. **A live demand/trigger feed for our directive brain.** The two exception queues are exactly the events our
   Tab-6 directives are built to answer — especially the **Smart-Scheduling overflow** queue, which maps
   one-to-one to our "park overflow / reassign / extend per-diem" directives, and **Status Alerts**, which drive
   our backfill/reassign directives and Worker-Trends missed-%.
3. **The execution surface for our recommendations.** What our tool proposes, the scheduler acts on in Web
   Scheduling's visit list / worker calendar — the response loop for "things seen within that tool."

**What gates it (be honest about today):**
- **No confirmed API/feed** for the queues or worker capacity — if it's screen-only, Direction A is manual until
  HCHB exposes data (our integration-questions item **A**). *Blocking for automation.*
- **Write-back round-trips to Citrix** — the *act* step isn't yet inside Web Scheduling for exceptions (item **B**).
- **Sync latency + worker-week grain** — Web Scheduling is present-tense and worker-week; our tool wants
  day/zone grain and forward view, so its data **informs but doesn't replace** our supply model.
- **Shared blind spots** — neither tool sees the **readiness gauntlet** or **economics**; Web Scheduling can't
  fill those holes in our tool, and vice-versa. Those stay net-new for both.

**Net:** the two are **complementary and connectable**, not redundant. Web Scheduling is the **eyes and hands**
(surface the exception, hold the record, execute the assignment); our capacity tool is the **brain** (weight the
capacity, forecast the demand, rank the response, guard the guardrails). Wired together — once the queue/worker
**feed** and **write-back** are confirmed — they form the "see → decide → act" loop the discovery asked for.
**Un-wired, they still cooperate manually:** a scheduler reads the exception in Web Scheduling, consults our
tool for the recommended move, and executes it in HCHB.

## 5. What to do about it
1. **Confirm the feed (integration-questions §A/§C).** Whether the exception queues and worker capacity % are
   API-available decides if Direction A is live or manual. *Highest priority.*
2. **Reconcile the metric.** Pull HCHB's Productivity-Point values + "Expected" and align our WVP/target so our
   Open-Capacity number equals what the worker calendar shows (validation, not a rival figure).
3. **Wire the exception queues into the Tab-6 cockpit** as a live demand input — the single highest-value
   connection (overflow → our directives).
4. **Design for hand-off, not just automation.** Until write-back exists, our tool should output a directive the
   scheduler can execute in one or two clicks in HCHB/Citrix — the loop works manually now, automates later.
5. **Keep the guardrails ours.** Web Scheduling won't enforce scope/SOC, weighting, fairness, or the readiness
   gate — our tool must, before any directive it hands to a Web Scheduling action.

---

*Companion to the operational spec sheet and executive overview. Our-tool references read from `invisiblegears`
`main` @ `6dba163` via [`../artifacts/capacity-tool-mockup-data-spec.md`](../artifacts/capacity-tool-mockup-data-spec.md);
Web Scheduling capabilities from the User Guide (KB0025451 v10.0). The Direction-A data links are contingent on
the HCHB feed questions being answered Y.*
