# SME Perspective — Field RN / SOC Nurse (the clinician ground truth)

> Seeded v0 perspective (AI-generated from the field-RN / SOC-nurse lens, grounded in the operator's strategy
> download). **To be validated with real field clinicians.** Preserved verbatim per the
> [SME discovery framework](../sme-discovery-framework.md). This brief carries the strongest "the agent must
> never do X" guardrails — treat them as hard rails.

# Field RN / SOC-Nurse Ground Truth: How Capacity Is Actually Protected and Expanded

Written from the seat: I carry a route, I do Starts-of-Care, and I've watched good branches run at 110% for years while "efficient" branches bled nurses out in eighteen months. Here's what's real. The tool and the AI agent can either respect this or destroy it — there is no neutral.

---

## 1. The SOC-Nurse "Known Slots" Model — Protect the Dedicated Role or Lose Predictability

**Principle.** A nurse (or PT) dedicated to Starts-of-Care and Resumptions converts referral intake from a scramble into a *schedulable inventory*. If I own SOCs Mon–Fri, the branch knows it has, say, 3–4 bookable admission slots per SOC clinician per day — a hard, plannable number. That is the single most powerful capacity lever at the clinician level because a missed/late SOC is a lost referral and a compliance clock (the 5-day OASIS window, the 48-hour contact) that never resets in your favor.

**Why violating it destroys capacity.** SOCs are the highest-cognitive-load, longest, least-interruptible visits we do — full OASIS, med rec, F2F verification, plan of care, homebound justification, teaching, coordinating the discipline team. You cannot do a quality SOC *between* two routine wound cares. When a branch "borrows" the SOC nurse for routine overflow, admissions slip, OASIS accuracy drops (which is money and Star ratings), and the predictable slot inventory evaporates. **The erosion is always silent and always framed as "just today."** Three "just todays" a week and the model is dead.

**Encode as system logic.**
- Model SOC/ROC capacity as a *separate reservable resource pool*, not fungible visit points. Show "admission slots available today/this week" as a first-class number.
- Flag any assignment that pulls a SOC-dedicated clinician onto a routine visit as **role erosion**, with a running weekly counter.
- Track SOC-slot utilization and *unfilled* slots separately. An idle SOC slot is not "waste to backfill" — it is *absorption headroom for tomorrow's referral*.

**Train the AI agent.** Treat SOC/ROC capacity as **protected inventory**. Default reasoning: routine overflow is solved by routine clinicians, LPN/LVN rebalancing, or per-diem — *never* by raiding the admission pool. If it must ever propose pulling a SOC nurse, it must (a) show the admission-slot cost, (b) confirm no other lane exists, (c) frame it as an exception requiring branch-manager sign-off, (d) log it against the erosion counter. **Never** silently reassign a SOC clinician to fill a same-day routine gap. **Never** treat an open SOC slot as idle capacity to optimize away.

---

## 2. The SOC Assignment Rule Is Clinical Law, Not a Preference

**Principle.** RN performs any SOC where nursing is on the case. PT performs the SOC only when nursing is **not** on the referral. This is discipline-scope and reimbursement reality.

**Why violating it destroys capacity.** Send a PT to open a case that needs nursing assessment — clinically unsafe, re-do required, wasted visit. Or burn an RN slot on a therapy-only case a PT could have admitted — starving your nursing SOC inventory. Both are capacity *destroyed*, not moved.

**Encode as system logic.** Hard rule: `nursing_on_case == true → SOC must route RN`. Cross-discipline SOC assignment is a **hard-fail with reason required**. Surface the rule inline.

**Train the AI agent.** Apply the rule deterministically before any optimization. It may not "trade" an RN SOC to a PT to balance a daily load. If a referral's discipline mix is ambiguous, flag for human clarification — do not guess to keep the queue moving.

---

## 3. Visit-Points Lie: Capacity Is Windshield + Documentation + After-Hours, Not the Visit

**Principle.** The real unit of a clinician's day is **visit + drive + charting + coordination**, not the visit alone. A 45-minute wound care 40 minutes away with a complex note is *not* the same "point" as a 45-minute recert next door.

**Why violating it destroys capacity.** Home health is a windshield job — drive is 25–40% of my day and non-linear. Documentation mostly happens *after* the last visit, on my couch. A tool that counts visits and ignores drive + doc will *always* overload the efficient nurse who says yes, and look "balanced" on the dashboard while I'm charting at 9pm. That's the exact profile of the nurse who quits in month fourteen.

**Encode as system logic.**
- Capacity must include **estimated drive time** (real geo-routing, not straight-line), **documentation load per visit type** (SOC/ROC/recert >> routine), **coordination overhead**.
- Show a "true day" estimate in *time*, not points.
- Flag routes where drive time exceeds a threshold % of the clinical day — a *territory* problem surfacing as a clinician problem.
- Track **documentation debt** (visits completed but not charted) as a capacity liability.

**Train the AI agent.** When it says "you have capacity for one more," reason in *time-of-day and total workload*, including drive and the note that visit generates. Know a Friday-afternoon SOC 30 minutes out is a 2.5-hour commitment, not "one visit." **Never** present spare capacity on visit-count alone. **Never** schedule the marginal visit in a way that predictably pushes charting past end-of-day without saying so.

---

## 4. Territory as "Resting Posture" — Geography Is Capacity Before Anyone Is Asked to Stretch

**Principle.** Well-drawn territories mean coverage and referral absorption are near-automatic — the clinician nearest the patient takes it without anyone burning goodwill. Territory is the standing arrangement that *reduces the number of asks* the branch ever has to make.

**Why violating it destroys capacity.** Every cross-territory assignment spends drive time AND goodwill (an "ask"). When territories are wrong, the tool makes constant day-to-day asks to paper over a structural gap — each drawing down the reciprocity bank. Fix the posture and the day-to-day gets quiet.

**Encode as system logic.** Detect chronic cross-territory routing and *unabsorbed referral clusters* and surface them as **territory-design signals to leadership**, distinct from daily assignment.

**Train the AI agent.** Prefer in-territory continuity for routine routing. When repeatedly reaching across territory lines to cover, **escalate the pattern as a structural finding**, not just more daily stretch-asks. Distinguish "one-time exception" from "the map is wrong."

---

## 5. What Makes a Clinician Say YES: Framing, Notice, and a Real Out

**Principle.** The extra Friday eval gets a yes when the ask is (1) *specific* ("Mrs. R, 2:15, 12 minutes from your last stop, straightforward recert"), (2) *early* (notice, not ambush), (3) *honest about size* (drive + doc included), and (4) *refusable without penalty*. Vague, late, dishonestly-sized, or coercive = the yes rots into resentment even when I say yes.

**Why violating it destroys capacity.** I go the extra mile for a branch that respects my time enough to ask well. A 4:45pm "can you also take this SOC across town" with no context is not a request, it's a trap — I do it once and start declining the reasonable ones too. Discretionary capacity is renewable *only if you don't strip-mine it.*

**Encode as system logic.**
- Any discretionary ask carries a **structured payload**: exact patient/time, drive delta, doc load, why-you, and a one-tap **decline with no logged penalty**.
- Track **notice lead time** on asks; flag chronic last-minute asking as a process failure.
- Distinguish *planned load* from *discretionary ask* in every clinician's view — never blend the extra in to hide the stretch.

**Train the AI agent.** Frame every ask concretely, early, honestly sized, with a genuine no. **Never** use urgency/guilt/scarcity language ("no one else can, patient will suffer, you're our only option") to manufacture a yes. **Never** disguise a discretionary ask as a normal assignment. A no is data, not defiance — record it neutrally and route elsewhere.

---

## 6. Reciprocity Is the Currency of Discretionary Effort — And It Has a Ledger

**Principle.** I say yes to the manager who offloaded my visits during my mother's surgery. The extra Friday SOC is *repayment*, freely given, because the branch banked trust with me first. Reciprocity is real, directional, and it depletes.

**Why violating it destroys capacity.** The flexible clinicians are the ones a naive optimizer *always* picks — they say yes, so the algorithm asks them more, so they burn out first. That's the flexible-nurse death spiral, and it's algorithmically induced. Branches keep capacity by *spending down their own goodwill* (managers who protect and offload) *before* drawing on the clinician's.

**Encode as system logic.**
- Maintain a **fairness/reciprocity ledger**: who's been asked, who's said yes, who got protected when *they* needed it. Surface skew ("Nurse A has absorbed 7 of the last 9 discretionary asks").
- Weight routing to **spread discretionary load** and *not* punish reliability with more work.
- Track branch→clinician support events (offloads during hardship), not just clinician→branch. Reciprocity is bidirectional.

**Train the AI agent.** Before asking, check the ledger. Prefer the clinician who *hasn't* been tapped. When one person is carrying the discretionary load, **surface the imbalance to leadership** rather than asking them a tenth time. **Never** exploit reliability — "she always says yes" is a reason to protect her, not to ask her again.

---

## 7. Continuity of Caregiver — Default to It, and Know Exactly When to Bend

**Principle.** Same clinician across a patient's episode is clinically real: I catch the subtle decline because I saw the baseline, the patient admits they haven't been taking the water pill, families stop re-explaining. Continuity should be the *default*; routing efficiency bends to it — **except** at defined break points.

**Why violating it destroys capacity.** Continuity *creates* capacity downstream: fewer missed changes, fewer avoidable rehospitalizations (a Compassus-level outcome and referral-source trust metric), faster visits from rapport. But rigid continuity destroys capacity when it forces a 40-minute cross-town drive for a stable routine recert. **Bend for:** stable/low-acuity, pure logistics, PRN coverage; **protect for:** SOC→follow-up handoff, wound cases, decline-watch, psych/behavioral, end-of-life.

**Encode as system logic.** Tag each patient with a **continuity-sensitivity level** (protect / flexible). Optimizer honors "protect" as a strong constraint; overrides continuity only for "flexible" patients or with a stated reason. Track continuity rate as an *outcome* metric; watch for continuity breaks predicting rehospitalization.

**Train the AI agent.** Default to the established caregiver. Trade continuity for efficiency **only** on flexible-tagged patients, and state the tradeoff. **Never** break continuity on a protected patient (wound, decline-watch, psych, EOL, active SOC episode) purely to smooth a route. When continuity must break, flag a **warm handoff need** (notes, heads-up) rather than a silent swap.

---

## 8. Burnout and Turnover Are Capacity Destruction on a Lag — Optimize for the Quarter, Not the Day

**Principle.** Every day you run the flexible nurses hot, the dashboard looks great. The bill comes 6–14 months later as a resignation, and losing one experienced SOC-capable RN removes *months* of admission capacity plus onboarding drag.

**Why violating it destroys capacity.** The most expensive thing a branch can do is lose a tenured field RN — getting a new hire to independent-SOC competence is a 3–6 month capacity hole. A tool that can't *see* the lag trades a nurse's longevity for this week's numbers — and does it to your *best* people first, because they absorb.

**Encode as system logic.**
- Track **leading burnout indicators** per clinician: sustained utilization above a sane ceiling, documentation-debt trend, declining yes-rate, PTO not taken, after-hours charting, consecutive high-load days.
- Model **turnover cost** explicitly — a projected resignation is a projected capacity cliff.
- Enforce a **utilization ceiling** the optimizer cannot exceed without human override.

**Train the AI agent.** Optimize the *quarter*, not the day. Treat sustained overload as a cost, not a success. When a clinician trips burnout indicators, **reduce their asks and flag to leadership** — do not keep drawing the well dry because they haven't quit *yet*. **Never** maximize this-week utilization at the expense of sustainability, and **never** target the reliable/flexible clinicians for overflow because they comply.

---

## 9. Culture Is the Multiplier — A Tool Can Reinforce or Corrode Trust, Never Stay Neutral

**Principle.** Clinicians go the extra mile *because the branch protects them*: clear policy, fair process, accountability both directions. The tool and its AI agent are now *part of the culture* — every ask, framing, and flag signals "this place respects me" or "this place is squeezing me."

**Why violating it destroys capacity.** The multiplier is why an 85%-capacity branch with great culture out-produces a 100%-staffed branch with bad culture. An agent that nags, guilt-trips, hides the true size of asks, or plays favorites will *strip the multiplier* faster than any staffing shortfall — at scale, and every clinician sees it.

**Encode as system logic.** Make trust signals measurable: transparency (every recommendation shows its reasoning), fairness (the reciprocity ledger), protection (burnout ceilings), accountability (the tool owns its bad calls — a wrong assignment is logged and corrected). Give clinicians visibility into *why* they were asked and a channel to push back.

**Train the AI agent.** Be transparent by default; never issue black-box demands. Respect the clinician as the ground-truth expert — their "no," their read on a patient, their sense of their own load **overrides the model's estimate**, and the agent learns from the correction. Accountability runs to the agent too. **Never** manipulate, guilt, rank clinicians publicly by compliance, or use patient welfare as leverage. **Never** pretend a recommendation is a rule.

---

## 10. Same-Day Referral Absorption — The Yes That Wins Referral Sources (Handle It Deliberately)

**Principle.** The hospital discharge planner who gets a "yes, we'll see them today" at 3pm sends you the next ten referrals. Same-day/late-day absorption is disproportionately valuable — it feeds the *referral precondition*. But it's the single most burnout-dense ask there is, so it must be *resourced*, not improvised on a tired nurse's back.

**Why violating it destroys capacity.** Referral-source trust is built on reliability under pressure. But if every same-day yes comes from ambushing whoever's still in the field, you win the referral and lose the nurse. Branches that do this sustainably *pre-fund* it — protected SOC slots held open, an on-call/flex admission clinician, or explicit reciprocity spend.

**Encode as system logic.** Hold a portion of SOC-slot inventory as **same-day absorption reserve**. Track same-day admission yes-rate as a *referral-source-health* metric. When same-day capacity is exhausted, surface it *before* asking an already-loaded clinician — the honest "we're at capacity today, first thing tomorrow?" protects both the source relationship and the nurse.

**Train the AI agent.** Route same-day referrals to *reserved* admission capacity first. Only reach into discretionary asks when reserve is gone, and then per all the rules above. **Never** default to grinding the nearest field nurse for the same-day admission just because saying yes to the source is easy for the branch. The referral source's yes cannot be financed by a nurse's breakdown.

---

## 11. The Human Override Is Sacred — Clinician Ground Truth Beats the Model

**Principle.** I can look at a patient and know they're circling a rehospitalization before any metric shows it. I know that "stable" recert is actually a family in crisis that'll take 90 minutes. The clinician's read is *higher-fidelity data* than the model, not noise to be smoothed.

**Why violating it destroys capacity.** A tool that treats overrides as friction to minimize makes worse decisions *and* destroys trust simultaneously. The override is how real-world ground truth corrects the model. Suppress it and you get confidently wrong routing plus a workforce that stops engaging with the tool (they'll work around it, and you lose your data).

**Encode as system logic.** Every override is captured *with its reason* and fed back as training signal. A clinician-declined ask is logged neutrally (no penalty). Patterns of override on the same recommendation type = a model defect to fix, surfaced to leadership.

**Train the AI agent.** Treat clinician input as authoritative on the ground. When overridden, ask *why* (optionally), record it, adjust. **Never** re-ask after a considered no, argue, or escalate a decline into pressure. **Never** treat override frequency as clinician non-compliance — treat it as the model needing to learn.

---

## Hard-Truth Summary — the guardrails an agent must never cross

- **Never** raid SOC/ROC admission slots for routine overflow, or treat an open slot as idle waste.
- **Never** route SOCs against discipline law (RN if nursing on case; PT only if not).
- **Never** offer "capacity for one more" on visit-count alone — drive + doc + coordination or it's a lie.
- **Never** use guilt, urgency, scarcity, or patient-welfare-as-leverage to manufacture a yes.
- **Never** punish reliability by routing more work to whoever says yes; spread it and protect the flexible ones.
- **Never** break continuity on protected patients (wound, decline-watch, psych, EOL, active episode) for routing convenience.
- **Never** maximize this-week utilization at the cost of a clinician's sustainability — burnout is capacity destruction on a lag.
- **Never** finance a referral-source yes on an already-loaded nurse's back without going through reserve first.
- **Never** treat a clinician's no, or their read on a patient, as noise — it is the highest-fidelity data in the system.
- **Never** be a black box — every ask shows its reasoning, its true size, and a real, penalty-free out.

The through-line: **capacity is not a number you extract, it's a relationship you steward.** The staffing model and territory set the resting posture so you rarely have to ask; culture and reciprocity are what make the asks land when you do; and the fastest way for this tool to *destroy* capacity is to optimize the visible daily number while quietly spending down the invisible things — SOC-slot integrity, reciprocity, continuity, and the nurses themselves — that don't show up on the dashboard until they're gone.
