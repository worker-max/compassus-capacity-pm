# SME Perspective — Branch Executive Director

> Seeded v0 perspective (AI-generated from the Branch ED lens, grounded in the operator's strategy download).
> **To be validated with a real Branch ED.** Preserved verbatim as a discovery input per the
> [SME discovery framework](../sme-discovery-framework.md).

# Home Health Capacity Tactics — Branch ED Lens

Below are the tactics that actually moved capacity in a branch I grew from a bottom-quartile performer to top-of-region. These are field-tested, not framework theory. I've written each so a developer can build the rule and a trainer can teach the agent. I'll flag where a tactic depends on the staffing model being right first — because nothing downstream works if the model is wrong.

---

## 1. Discipline-Balance Guardrail (RN:LPN and PT:PTA ratios)

**Tactic.** The great branch staffs LPNs and PTAs deliberately so RNs and PTs are spent on the visits only they can do — SOCs, ROCs, resumptions, recerts, complex assessments — and routine follow-up visits flow to the assistant level. When the assistant tier is understaffed, RNs and PTs silently absorb routine visits and the branch loses SOC capacity it never sees on a report.

**Trigger / context.** Continuous, but especially when a branch is "busy but not growing" — clinicians are maxed, yet SOC acceptance is flat or declining.

**Why it works.** Capacity for *new* patients is created almost entirely at the skilled-clinician SOC slot. Every routine LPN-appropriate visit a RN does is a SOC that RN can't do that day. The imbalance is invisible on a raw productivity report (the RN looks "full") — it only shows up when you decompose the RN's day by visit type.

**Encode as system logic.**
- Track per-discipline visit mix: for each RN, `% of weekly visits that are routine/follow-up (LPN-eligible)`. Flag when RN routine-visit share exceeds a market-set threshold (I ran ~20-25%).
- Compute live ratios `RN:LPN` and `PT:PTA` against a **market-target band** (not a national default). Flag out-of-band.
- Derived metric: **"Skilled-hours leakage"** = RN/PT hours spent on assistant-eligible visits × loaded rate. Surface as a dollar figure and as "SOCs foregone this week."

**Train the AI agent.** Watch for RNs whose calendars are full of routine visits while SOC referrals are being declined/deferred. Recommend shifting routine visits to LPN/PTA to free skilled slots, or flag an assistant-tier hire. Do NOT recommend "hire more RNs" as the first lever when the real problem is an LPN/PTA gap — that's the expensive wrong answer and it's the most common mistake. Always express the fix as "SOCs unlocked," not just "hours rebalanced."

---

## 2. Market-Unique Model Sizing (no copy-paste ratios)

**Tactic.** Each branch's staffing model is sized to *its* market's referral potential, payer mix, geography, and acuity — never cloned from another branch. A dense metro branch with high LPN-eligible chronic census runs a very different ratio than a rural branch with long drive times and RN-heavy acuity.

**Trigger / context.** New branch build, annual model reset, a market shift (new referral source, MA plan change, competitor exit), or any time actuals drift from the plan two quarters running.

**Why it works.** The staffing model is the PRIMARY effector of capacity. A model tuned to potential means new referrals get absorbed almost automatically; a mistuned model either strands capacity (overstaffed, margin bleeds) or chokes growth (understaffed, SOCs bounce). Potential is a function of the market, so the model must be too.

**Encode as system logic.**
- Model each discipline's target FTE as a function of inputs: projected weekly referrals × payer/acuity mix × avg visits-per-episode by discipline × geography factor (drive time / density) ÷ target productivity.
- Store a **per-market target band** for every ratio and productivity number; national numbers are seed defaults only, explicitly labeled "unvalidated for this market."
- Run a monthly **plan-vs-actual variance** on referral volume, mix, and per-discipline utilization; auto-flag when the model's assumptions no longer hold.

**Train the AI agent.** Reason from *this market's* numbers, never a global constant. When asked "are we staffed right?", pull the market's referral trend and mix first, then compare to the model. Recommend model re-sizing when variance persists. Do NOT normalize one branch against another's ratios as if they're comparable — surface the market differences that justify the gap.

---

## 3. SOC-Dedicated Nurse (and SOC PT) — Manufacturing Known Slots

**Tactic.** Create one or more nurses who do *only* SOCs, ROCs, and resumptions — no ongoing caseload. Their week is a grid of bookable start-of-care slots. In markets with PT-driven ortho volume, do the same with a SOC-dedicated PT.

**Trigger / context.** Once referral flow is steady and predictable enough to keep a dedicated role busy — typically a mid-to-large branch, or a smaller one with a reliable high-SOC referral source (joint-replacement program, MA chronic-care contract).

**Why it works.** It converts capacity from a *guess* into *inventory*. Normally a scheduler has to interrupt a RN's day and hope; with a SOC nurse, capacity is a set of known slots you can book against and even promise to a referral source ("we can start tomorrow AM"). It removes the daily productivity/SOC tug-of-war, protects episode start-timeliness, and makes acceptance decisions instant. Known slots also let the branch say "yes" faster than competitors — which grows referrals.

**Encode as system logic.**
- Model the SOC nurse/PT as a **slot inventory** object: N bookable SOC slots per day, with geography tags. The capacity cockpit's referral/discharge matching engine books referrals directly into slots.
- Surface **SOC slot fill rate** and **slots remaining today/this week** as a headline cockpit number.
- Apply the **SOC assignment rule** at booking: RN performs any SOC where nursing is on the case; PT performs the SOC only when nursing is NOT on the referral. The engine routes to the correct dedicated role automatically.
- Trigger a "create/expand SOC role" recommendation when SOC volume × interruption cost to skilled staff exceeds the cost of a dedicated FTE, or when SOC-timeliness starts slipping.

**Train the AI agent.** Treat SOC slots as the branch's true growth capacity — protect and fill them. When a referral arrives, check nursing-on-case to route RN-SOC vs PT-SOC correctly, then book the nearest open slot by geography. Watch for slot under-fill (role too big / referral dip) and over-subscription (role too small / need a second SOC nurse). Do NOT let a SOC nurse get quietly loaded with ongoing caseload "just this once" — that's how the known-slot capacity evaporates; flag any recurring visit assigned to a SOC role.

---

## 4. SOC-on-Referral Match Directive (turn capacity into an answer in minutes)

**Tactic.** Every inbound referral is matched to a concrete start plan — discipline, clinician/slot, day, geography fit — before the intake conversation ends, so acceptance is a real commitment, not "we'll call you back."

**Trigger / context.** Every referral, all day. Highest value during peaks and when competing against another agency for the same discharge.

**Why it works.** Referral sources reward speed and certainty. A branch that answers "yes, [PT] starts Thursday AM, she's already in that ZIP" wins the next referral too. It also forces the capacity question to be answered honestly at intake instead of discovered as a missed SOC three days later.

**Encode as system logic.**
- The directive engine takes referral attributes (disciplines ordered, nursing-on-case y/n, ZIP, acuity, requested SOC window) and returns a ranked match: SOC slot or clinician with resting-posture headroom in that territory.
- Enforce the RN-SOC / PT-SOC rule at match time.
- Log **time-to-match** and **accept vs decline with reason**; decline reasons feed the model-variance and hiring signals.

**Train the AI agent.** On each referral, produce the best 1-3 start plans with named slot/clinician + day + drive fit, and the nursing-on-case routing. Recommend accept when a compliant slot exists; if not, surface exactly what's missing (no LPN coverage in that ZIP, SOC nurse full Thu) so it becomes a staffing signal, not a silent decline. Do NOT accept a SOC the model can't actually staff on time — a late or bounced SOC costs more than a clean decline.

---

## 5. Resting-Posture Territory Design

**Tactic.** Assign clinicians to geographic territories with a deliberate "resting posture" — a home base and a caseload target set below their ceiling — so a clinician's default state already covers active clients *and* leaves absorption headroom for the next referral in their area. Coverage becomes nearly automatic.

**Trigger / context.** Caseload assignment, territory redraw after a hire/departure, or when drive time (non-productive miles) starts climbing.

**Why it works.** If everyone runs at 100%, every new referral is a scramble and a negotiation. If territories carry planned slack tied to referral density, the new SOC in that ZIP has an obvious home and the daily scheduling load drops. It ties caseload distribution to data and logic instead of "who complained least."

**Encode as system logic.**
- Give each clinician a **territory** (ZIP/geo cluster) and a **target caseload band** with intentional headroom keyed to that territory's referral rate.
- Roster/cockpit shows **headroom by territory** (green = absorb-ready, amber = tight, red = over). Matching engine prefers the in-territory clinician with headroom to minimize drive time.
- Flag **territory imbalance**: one clinician red while an adjacent one is green → rebalance suggestion. Track **non-productive drive miles** as a territory-health metric.

**Train the AI agent.** Route referrals to the in-territory clinician/slot with real headroom, protecting resting-posture slack rather than filling every clinician to the top. Recommend caseload rebalancing when adjacent territories diverge. Watch drive-mile creep as an early sign a territory is mis-drawn. Do NOT optimize purely for "fill the emptiest calendar" if it means cross-town assignments that burn windshield time and torch productivity.

---

## 6. Per-Diem / PRN Visibility & Pre-Positioning

**Tactic.** The branch keeps a live, ready per-diem bench and makes the *need* visible days ahead — so PRN coverage is arranged before a gap becomes a missed visit, not after. Per-diem coordination is genuinely hard; the tool's job is to make the gap show up early.

**Trigger / context.** Known upcoming crunch — PTO, census spike, a territory temporarily short, seasonal surge, a clinician out sick.

**Why it works.** Per-diem is the shock absorber for day-to-day variance. The failure mode is always *late visibility* — you find the hole the morning of. Surfacing projected uncovered visits 3-7 days out turns a scramble into a phone call.

**Encode as system logic.**
- Maintain a **per-diem roster** with disciplines, geographies, availability windows, credential/comp status.
- **Coverage-gap projection**: for the next 7-14 days, compute visits at risk of no assigned clinician given PTO/known absences and territory headroom; rank by SOC-criticality and recert deadlines.
- Match projected gaps to eligible per-diems by discipline + geo + availability; flag **credential/expiry** blocks before assignment.

**Train the AI agent.** Look ahead, not just at today — surface projected uncovered visits early and propose specific per-diem matches. Prioritize SOCs and recert-deadline visits when triaging which gaps to fill first. Do NOT assign a per-diem whose credentials/onboarding aren't current, and do NOT wait until the day-of to raise a foreseeable gap.

---

## 7. Reciprocity Offload Ledger (bank the "yes")

**Tactic.** When a clinician is having a hard week — personal crisis, burnout, a brutal SOC run — the manager proactively offloads visits and *protects* them. That deposit gets repaid later as discretionary effort: the Friday-afternoon eval, the SOC accepted near-full, the extra weekend ROC.

**Trigger / context.** Detected clinician overload, back-to-back heavy weeks, a known personal hardship, or a manager-initiated protective move.

**Why it works.** Culture is the multiplier on capacity. Clinicians go the extra mile for a branch that has demonstrably gone the extra mile for them. Reciprocity is real and it's earned in advance. A protected clinician is a retained clinician, and retention is capacity.

**Encode as system logic.**
- Track a per-clinician **load-strain signal**: rolling visit count vs band, consecutive heavy weeks, weekend/after-hours count, SOC density, recent PTO.
- Log **offload events** and **stretch events** as a lightweight ledger — not for surveillance/scoring, but so the branch can see reciprocity balance and prevent burnout.
- Alert when a clinician crosses into sustained overload → prompt a protective offload *before* a resignation-risk threshold.

**Train the AI agent.** Watch for sustained overload and recommend proactively offloading before burnout, especially for clinicians carrying stretch load. Frame stretch asks as favors to be balanced, not entitlements. Do NOT repeatedly route the extra visit to the same willing clinician — that "reliable yes" is exactly who burns out; distribute the ask and flag when one person is carrying the branch. Never present the ledger as a performance-ranking or use it to pressure a clinician.

---

## 8. Clear-Policy Protection (make "yes" safe)

**Tactic.** The branch has explicit, written policy/process for the hard moments — after-hours SOC expectations, weekend rotation, what "full" means, when it's OK to decline — so clinicians can stretch without fear of being blamed later. Protection is structural, not just a nice manager.

**Trigger / context.** Any recurring friction point where clinicians hesitate to say yes because the rules are ambiguous.

**Why it works.** Discretionary effort only shows up when the extra mile won't be punished. Ambiguity kills volunteering. Clear policy converts "I'm not sure I'm allowed" into a confident yes, which is directly capacity.

**Encode as system logic.**
- Encode **branch policy thresholds** as tool config: after-hours SOC window, weekend expectations, definition of "at capacity," decline-allowed conditions. The directive engine references these so asks are always policy-compliant.
- When the engine asks a clinician to stretch, attach the **policy basis** ("within weekend rotation policy; comp per PRN rate").

**Train the AI agent.** Only make stretch asks that fall inside encoded branch policy, and always cite the policy basis. If a needed ask falls outside policy, escalate to the manager rather than pressuring the clinician. Do NOT invent expectations the branch hasn't set.

---

## 9. SOC-Timeliness & Start-of-Care Protection

**Tactic.** The branch treats SOC-timeliness (referral-to-start interval) as a top-line capacity KPI, not a compliance afterthought. Fast, reliable starts are what referral sources actually buy.

**Trigger / context.** Continuous; alarms when the referral-to-SOC interval drifts up or a referral source's volume dips.

**Why it works.** A missed or slow SOC is lost capacity *and* a lost referral relationship. Protecting start timeliness keeps the referral precondition healthy. It's the clearest external signal the staffing model is right-sized.

**Encode as system logic.**
- Track **referral-to-SOC interval** per referral, segmented by source, discipline, geography. Alert on drift above a market-set target (e.g., >48h standard, tighter for hospital discharges).
- Correlate rising SOC intervals with SOC-slot fill and discipline balance to point at the *cause*.
- Track **decline-rate by referral source** as early warning.

**Train the AI agent.** Treat SOC timeliness as a growth metric. When it drifts, diagnose upstream — SOC slots full? LPN/PTA gap? territory mis-draw? — and recommend the specific staffing fix. Do NOT treat a slow SOC as merely a compliance flag.

---

## 10. Recert / Episode-End Discharge Forecasting (recycle capacity)

**Tactic.** The branch forecasts discharges and recert decisions weeks out, so freed-up caseload slots are matched to incoming referrals deliberately — capacity is *recycled* on a plan.

**Why it works.** Every discharge reopens a bookable slot in a territory. Seeing discharges coming lets the matching engine pre-commit that slot to a new referral in the same geography — near-zero friction, no idle capacity between patients.

**Encode as system logic.** Project upcoming **discharges and recert decisions** from episode data; expose as freeing slots by territory/discipline; feed into the referral-matching engine. Metric: **slot-recycle time**.

**Train the AI agent.** Anticipate discharges and pre-match incoming referrals to opening slots in the same territory. Do NOT hold a patient past clinical need to "keep the slot warm."

---

## 11. Financial-Health Capacity Lens (margin per skilled hour)

**Tactic.** The ED sizes and defends the model in dollars: cost-per-visit by discipline, margin per skilled hour, and the real cost of RN/PT time spent on assistant-level work.

**Why it works.** The cheapest capacity gain is usually *not* another RN — it's an LPN/PTA that frees existing RN/PT SOC slots. Seeing capacity in margin terms keeps the branch from over-hiring the expensive tier.

**Encode as system logic.** Attach **loaded cost + reimbursement** per visit type/discipline/payer; compute **margin per skilled hour** and **skilled-hours-leakage dollars**. On any hire recommendation, output a **tier comparison**: cost and SOC-capacity gained by LPN/PTA vs RN/PT for the same dollars.

**Train the AI agent.** Always compare tiers on cost and SOCs-unlocked; default to the lowest-cost tier that actually frees skilled slots. Do NOT recommend adding skilled FTEs when an assistant-tier hire unlocks the same SOC capacity for less.

---

## 12. Referral-Source Concentration & Pipeline Guard

**Tactic.** The branch monitors where referrals come from and defends against over-reliance on any single source — the staffing model is only as stable as the referral flow feeding it.

**Why it works.** Referrals are the precondition for everything. A concentrated pipeline means one relationship change can strand a whole staffing model overnight.

**Encode as system logic.** Track **referral volume and trend by source**; compute a **concentration index**; alert on over-concentration and on a major source's volume declining. Tie source trends to model-variance and decline-rate.

**Train the AI agent.** Watch referral-source concentration as a leading indicator of capacity risk. When a top source dips, check it against decline-rate and SOC-timeliness — if we're declining that source's referrals, it's a self-inflicted staffing problem. Do NOT treat referral volume as exogenous.

---

### How these stack (for the tool's mental model)

1. **Referrals** must exist and stay diversified (Tactics 12, 9) — the precondition.
2. **Staffing model** is the primary effector: discipline balance (1), market-unique sizing (2), SOC-dedicated roles (3), sized in dollars (11).
3. **Territory management** gives near-automatic coverage: resting posture (5), matching engine (4, 10).
4. **Day-to-day management** absorbs variance: per-diem visibility (6), SOC-timeliness protection (9).
5. **Culture/leadership** multiplies it all: reciprocity (7), clear-policy protection (8).

The single highest-leverage thing the tool can teach the AI agent: **capacity is created at the SOC slot, and it is most often lost because the assistant tier is understaffed — never diagnose a "we're full" problem without first decomposing skilled clinicians' days by visit type.**
