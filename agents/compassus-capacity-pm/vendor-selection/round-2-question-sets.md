# Round Two — Question Architecture

Six two-hour virtual calls, one per vendor, the week of 2026-09-15. **Primary ask: walk us through the
operational design from referral through to day-to-day standard scheduling.** Time is reserved for the
vendor's own questions.

## The design

Two layers, deliberately.

**Layer one — ten questions asked identically to all six.** Comparability is the whole point: the same
question to six vendors produces a spectrum, six different questions produce six unrelated
conversations. Every one of the ten is built on something the *field as a whole* left thin, not on one
vendor's weakness.

**Layer two — a unique set per vendor**, built from that vendor's own open items, contradictions and
admitted gaps. None can be answered with a slide, because each one quotes their own return back to them.

**The third design goal, stated by the initiative lead:** give every vendor the floor to explain where
they look weaker than the others, so the field is measured across a spectrum of context rather than on
a single return read in isolation. Question 10 does this explicitly; the vendor-specific sets do it by
being answerable rather than accusatory.

## Recommended: one shared scenario

Send all six the **same** case 48 hours ahead — one patient, one branch, one week. A Medicare SOC with
PT and nursing, a mixed-discipline caseload, a rural-edge ZIP. Six walkthroughs of the same case are
comparable; six walkthroughs of each vendor's favourite case are not. **This is the single
highest-leverage change available to the round.** (Scenario not yet written.)

## Time budget

| Block | Minutes |
|---|---|
| Walkthrough, referral → steady state, with common questions 1, 2 and 6 embedded in flow | 75 |
| Common questions 3, 4, 5, 7, 8, 9 plus the vendor-specific set | 35 |
| Common question 10, and the vendor's own questions | 10 |

That is the full two hours with no slack. **Send questions 3, 7, 8 and 9 in advance and ask for numbers
ready**, or the back half gets lost. Vendor-specific sets run 7–8 questions; for MedArrive, CareStitch
and Axle the first question decides the rest of the call and should be asked in the opening fifteen
minutes, not saved for the end.

---

# Layer one — the common ten

### 1. The referral decision
> *"It's 10am, a referral lands. Show us what your product tells the person deciding whether to accept
> it — and what happens next if we say yes."*

Field-wide gap. Only Axle and Arya gave a real referral-against-capacity answer. HCHB does not forecast
referrals or discharges; CareStitch does not address inflow against the envelope; VitalisCare's branch
rollup is planned; MedArrive's referral check is Q4 roadmap; Unity's C1 never answers it at all. Also
the front door of the walkthrough being asked for.

### 2. The episode, not the visit
> *"Show us how ordered frequency, the recert window and the LUPA threshold shape the week your product
> builds — and what it does when an episode starts falling behind."*

The fluency test with teeth. LUPA, PDGM, OASIS and recert are absent from almost every return. Axle used
the vocabulary unprompted; MedArrive earned it in a different business; Zeeva has it with no customers.
Asked of all six, this separates home health from home care immediately.

### 3. HCHB freshness, with a number
> *"HCHB is our system of record and stays that way. What do you read, what do you write, by what
> mechanism, and how stale can the data be at worst? We've been given three different answers on HCHB's
> own refresh lag — give us yours, with a number."*

**There is a live factual conflict in the returns.** Arya claims sub-5-minute via screen automation;
Axle turned their integration off over a 30-minute lag; HCHB says no latency because it is native;
CareConnect's plan assumes ~20 minutes on a read replica. Someone is wrong. Asking all six triangulates
it — and the answer matters beyond vendor selection.

### 4. The line between advise and decide
> *"Where does your product decide on its own today, and where does a person confirm? Name a customer
> who moved that line — which direction, and what happened."*

Sophistication marks span 2 to 4. Arya writes back to HCHB with no approval step; Axle can run
autonomously but every real customer kept a human in the loop; HCHB stops short deliberately; Zeeva's
default sits above the Assist boundary. The same question to six vendors tells Compassus where its own
boundary should actually sit.

### 5. The clinician says no
> *"A clinician rejects an assignment. Walk us through the next sixty seconds, and the next sixty days —
> what happens on the schedule, and what changes in the model."*

**Weakest section in the entire field** — clinician fit ran 0.25 to 0.75, nobody higher. Several returns
describe a feedback loop and never describe the moment. Aligns with the knowledge base's finding that
change management, not technology, is the real risk.

### 6. A Tuesday that goes wrong
> *"Two call-outs at 7am, a patient reschedules, one visit is at the edge of its compliance window. Show
> the day re-form: how fast, who gets contacted, and what happens when nobody takes the visit."*

Where the products genuinely differ. "What if nobody takes it" went unanswered by several vendors.
Make them do it live, not on a slide.

### 7. What you don't do
> *"Name the three things in our scope your product does not do today. For each: a date, a workaround,
> or never. We'll hold this against your Section B answers."*

Multiple returns claim Section B coverage that Section C does not support — the rubric already says
believe Section C. Rewards the candor the rubric scores, and cheaply resolves the contradictions.

### 8. What breaks at our size
> *"Here is our scale. What's your largest deployment, what broke when you got there, and what would you
> do differently starting with us?"*

Durability came back Neutral or unaddressed for five of the six advancing — no company size, no funding,
no statement of how central home health is. Gets at it without asking a question they will deflect.

### 9. The one number you'd stake it on
> *"One measured result, one named customer: what it was before, what it is now, over what period, how
> the baseline was set. One is enough if it's real."*

A3 was marked Watch for nearly the whole field — impact claimed without baseline or period. Only Arya
and HCHB cleared it. Asking for one verifiable number beats asking for more claims.

### 10. Where you'll look worse
> *"We're running six of these. Where do you expect to compare unfavourably, and what context would we be
> missing if we scored you on that alone?"*

The spectrum-of-context mechanism, made explicit. The answer is itself a candor read — vendors who name
their real gap tend to be the ones telling the truth elsewhere.

---

# Layer two — vendor-specific sets

## Arya — 84, Advance
*Strongest return in the field. These ask whether the strength is where Compassus needs it.*

1. How many of your ~60 production orgs are on HCHB, how many bi-directionally in production, and since
   when? **Your return never gives an HCHB-specific count.**
2. Your integration is Citrix screen automation. What happens when HCHB changes a screen — who notices,
   who fixes it, how fast, and has it broken in production yet?
3. You're the only vendor scored at "Runs it" — writes back to HCHB with no approval step. Which
   actions, at which customer? Can every one of them be configured to require approval **permanently**,
   not as a phase-one setting we're expected to graduate out of?
4. "No more apps for clinicians, ever." Walk us through a clinician's actual week under that model. What
   happens to the clinician who won't engage with an agent by voice or text?
5. Before-the-visit automation is live at one customer and you recommend staging it late. What's the
   realistic sequence and date for us?
6. Aveanna — +11% authorized hours delivered. Was that private duty or home health? Different scheduling
   problems; we need to know which one the number came from.
7. Your customer mix is described as "an even split." Give us the actual percentages. And nothing in the
   return covers company size, funding stage, or how central home health is versus other post-acute
   settings.

## HCHB — 75, Consider
*The incumbent. Two of these are uncomfortable and both need asking.*

1. **Stop-check, open:** your twelve-month uptime figure and the contractual commitment with remedies.
   The return has neither. This was supposed to be resolved before you advanced.
2. Partnership scored 1 of 4 — lowest in the field. Co-marketing is not a partnership. Is there any
   structure available — design partner terms, roadmap seat, shared economics, ownership — or is this a
   standard license?
3. Your automations depend on accurate and timely documentation in HCHB. Late and incomplete
   documentation is our daily reality. **What does the product do with bad data, rather than assume good
   data?**
4. "Agency configuration" carries a lot of weight in your answers. Who configures it, how long, what does
   it cost, and what does a misconfiguration look like in production?
5. You don't forecast future referrals or discharges. We're being asked to run capacity against future
   demand — what fills that gap, and is it on the roadmap with a date?
6. Visit Finder is new and you weren't sure who's using it. Name a live customer, or tell us it's
   pre-release.
7. Show us the clinician's actual interface — what they can see, change and request about their own week.
   Your return didn't describe it.
8. You're our EHR. If we invest a dedicated team in building this with you, what stops it shipping to
   every competitor next quarter? Is there any lead time or exclusivity on the table?

## VitalisCare — 67, Consider
*Live HCHB integration and real numbers. The question is whether any of it is home health.*

1. Six production customers since 2023 — how many are home health versus hospice, and what's the largest
   home health census? **Demo a home health branch, not a hospice one.**
2. Your return mentions RN and HHA, never PT, OT or SLP. Does the product schedule therapy disciplines at
   all — eval-driven frequency, therapy sequencing, discipline-specific productivity?
3. Walk us through a 60-day Medicare episode: SOC window, recert window, LUPA risk. **PDGM, LUPA, OASIS,
   SOC and recert appear nowhere in your return.**
4. No patient-facing communication of any kind exists today and no date was given. What's the plan, what
   does it cost, and when — or do we keep doing that work manually?
5. You admitted authorization and readiness aren't tracked states. How do not-ready visits stay off the
   schedule today?
6. Point-weighting and the branch rollup are both "planned." Dates, and who funds that build.
7. Company size, funding, headcount. Would we be your largest customer by a multiple?
8. Name the actual product set — Sync, Sync360, the mobile app. What requires which, and what does a
   clinician have to install?

## Axle Health — 63, Conditional — Hold
*Best product answers in the field attached to a zero on integration. This call is mostly one question.*

1. You built HCHB write-back and turned it off over a 30-minute refresh lag. What specifically lags,
   what's your threshold, and what has to change for it to be viable? **Is the Databricks/Snowflake
   migration a commitment HCHB has made to you with a date, or your read of where they're going?**
2. Would you turn it back on for Compassus — read-only first, full write-back later, or not at all? A
   date, and what you need from us.
3. Your C6 answer says the integration is "always bi-directional." It's off. Reconcile those two
   statements.
4. Which EHRs do your 25 customers actually run — including the 11k ADC deployment? What would be
   different about us?
5. E1 and E2 read rushed — referral credits and general openness, no structure. Given what we're putting
   in, what's the real partnership proposal?
6. Incentives are a manual waitlist; dynamic pricing is in development. Date, and what do we do in the
   interim?
7. No name on your return. Who's on this call, and who would actually run our deployment?
8. Nothing on company size or funding anywhere in the return.

## CareStitch — 56, Conditional — Hold
*Highest home health concentration in the field, 69%. And the thinnest integration story.*

1. Your HCHB beta is read-only screen automation that has never run in production, with no go-live date.
   Give us a date for read, a date for write-back, and the engineering plan behind both. **This is the
   entire reason you're Conditional.**
2. The manual-upload path where the agency uploads HCHB reports — is that what your HCHB customers
   actually do today? How many HCHB customers do you have?
3. You ingest no orders and no authorization from HCHB, and don't enforce compliance windows. That's the
   spine of home health scheduling. Plan and date.
4. You scored lowest of the six on sophistication — you filter and display, the scheduler makes every
   call. Is "advise and orchestrate" a principle you'll hold, or a stage you'll move past? What would it
   take to get to recommend?
5. References were "expected," not committed. We need three named home health references in writing
   before the next round.
6. Front-loading is scheduler-driven, not paced by the product. Under PDGM, pacing is where the money is.
   Will the product ever pace the episode itself?
7. 69% home health across 79 orgs and 144 branches is the strongest HH concentration here — show us that.
   Which orgs, which EHRs, what size?
8. Nothing says how central home health is to CareStitch's business as a whole, or anything about company
   size and funding.

## MedArrive — 48, Conditional — Decline, two open stop-checks
*This call is about whether they belong in the round. Be straight with them and with ourselves.*

1. **Stop-check, open:** zero home health, hospice or private duty customers. Is there a signed or
   in-flight home health customer? Would we be the first?
2. **Stop-check, open:** your ROI study is hospital-at-home. Which of those results should transfer to a
   home health branch, and which shouldn't? You get to make the case.
3. LUPA pacing, the recert window, the readiness check, the referral-capacity check — you describe all
   four in real detail and all four are roadmap. Which exist in code today? Show them running. What's the
   build plan and who pays for it?
4. Your narrative describes a working ranked coverage-suggestion feature; your status line calls it
   roadmap. Which is true?
5. Clinician fit scored lowest in the field. Your six-month adoption numbers are real but come from gig
   field clinicians. W-2 home health clinicians with established caseloads and strong feelings about
   their own week behave nothing like that. What transfers?
6. You've pivoted once already — from running a 700-clinician field operation to selling software — and
   are now aimed at a market you've never served. Funding, runway, headcount, and what happens if home
   health doesn't land.
7. You've chosen not to build agentic voice. Most of the coverage problem is outreach. What fills that?
8. What would make us wrong to rule you out?

---

## Where this goes in the workbook

The Questions tab of `VendorScorecard Rubric 9.11.26 Copy.xlsx` is the intended home: columns D–I are
the six advancing vendors, with three slots under each of A, B, C, D, E and Intangibles. **It is still
an empty scaffold.** Two structural changes should land with the content — a stop-check resolution row
above Section A, and a verdict column so the demo can move the mark. See
[`rubric-review-and-process-findings.md`](./rubric-review-and-process-findings.md), findings 1 and 4.
