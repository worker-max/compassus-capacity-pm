# Home Health Authorization Operations

**Scope:** the administrative machinery between a referral and a schedulable visit, for non-traditional-Medicare home health payers (Medicare Advantage, Medicaid managed care, Medicaid fee-for-service, commercial).

**Research date:** all sources accessed 2026-08-18 unless otherwise noted. Publication dates are given inline.

**A note on evidence quality.** Home health authorization is a poorly documented field. Payers publish their *rules* unevenly and their *performance* almost not at all. Where a number below is general-medical rather than home-health-specific, it is labeled as such. Where no authoritative public source exists, this document says so rather than substituting a plausible figure. Several widely repeated field claims — auth staffing ratios, home-health-specific denial rates, home-health-specific turnaround — have **no authoritative public source**, and that absence is itself a finding.

---

## 1. The end-to-end workflow, with precise definitions

The field uses several of these terms loosely. The definitions below are how payers use them in published policy.

### 1.1 Eligibility verification

Confirmation that the patient is enrolled with the payer on the date of service and that the plan is the correct one. Transacted as the X12 270 (inquiry) / 271 (response). This is the cheapest and most automated transaction in healthcare — 84% fully electronic on the plan side, at $0.04 per transaction for plans and $2.00 for providers when electronic, versus $8.57 provider cost when manual ([2024 CAQH Index Report](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf), published Jan 2025, cost table p. 60).

Critically, **eligibility verification is not a benefit check.** A 271 confirms coverage exists. It does not reliably tell you how many home health visits remain, whether the benefit is per-discipline or pooled, or whether the plan delegates home health authorization to a vendor. Vendors sell this distinction as one product; operationally they are two.

### 1.2 Benefit check

Determination of what the plan actually covers for home health: visit or day limits, per-discipline versus pooled limits, cost share, benefit-period anchoring, and whether the plan delegates. In practice this is done by a human reading the plan document or calling the payer, not by transaction. Option Care Health's authorization guide for its Ohio network makes the separation explicit — agencies request a "benefit check" as a discrete portal action separate from the authorization request ([Option Care Health / CSI Authorization Guide, Ohio, rev. 8/2024](https://optioncarehealth.com/wp-content/uploads/Authorization-Guide.-Ohio-rev8.2024.pdf), p. 1).

**The delegation question is the operationally load-bearing one and it is not in any transaction.** A UnitedHealthcare Medicare Advantage member may be managed by Optum, by Home & Community (formerly naviHealth), or by neither, and the rules differ completely by which. An Anthem Medicare Advantage member in Ohio is managed by Carelon only if the member ID carries one of six specific alpha prefixes — JRI, JRG, VOC, VOD, ZVR, AFH — and by Anthem directly otherwise (Option Care guide, p. 7). Routing is keyed to a substring of the member ID.

### 1.3 Initial authorization request

The first request to the payer for approval of home health services. Published requirements vary along four axes: what documentation is required, when the request must be submitted relative to start of care, how many visits may be requested, and whether the payer will honor a request submitted after care has begun.

The Option Care guide's baseline initial-authorization packet is: home health orders, discharge summary if the patient is coming from a facility, and updated clinical documentation / H&P. Notably, "ST, MSW, and HHA are not considered for initial authorizations; please request these services with ongoing authorization after initial home health evaluation is completed" (p. 2). **Speech therapy, social work, and aide are structurally excluded from the initial ask by several payers** — they can only be added at the first reauthorization. That is a scheduling constraint, not a billing one.

### 1.4 Pending / provisional authorization

See §2. Briefly: a payer-sanctioned window in which the agency may deliver a bounded number of visits or days before an authorization number exists, on the expectation that the eventual authorization will cover them. The term is used loosely in the field to mean three different things — a request awaiting decision, a payer's affirmative allowance to start care, and an agency's own risk decision to start uncovered. Only the second is contractually meaningful.

### 1.5 Concurrent review

Payer review of clinical documentation *while the patient is on service*, to decide whether to continue, modify, or terminate the authorization. The distinguishing feature versus reauthorization is that concurrent review can *reduce* an already-issued authorization; reauthorization only decides the next one. In home health, concurrent review is most often documentation-triggered at a fixed cadence rather than continuous. The Health Affairs Scholar study of MA home health UM found practice ranging from "very light concurrent review after" an initial approval, through reauthorization "around day 30," to the pathological cases of authorization "week by week" or "by visit" ([Thomas KS et al., *Health Affairs Scholar*, Vol 3 Issue 3, March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917)).

### 1.6 Reauthorization

A request for a *new* authorization covering a subsequent period, typically requiring a clinical justification of continued need. Distinct from an **amendment**, which adds visits to an existing authorization under the same authorization number. Montana Medicaid draws this line explicitly: additional visits within the initial period are an "amendment to the initial request" processed "using the same authorization number," whereas extended services past the annual limit generate "a new prior authorization number" ([Montana DPHHS Home Health Policy 410, issued April 1, 2019](https://dphhs.mt.gov/assets/sltc/HomeHealth/Section400/HH410PrAuth.pdf), pp. 2–4).

This distinction matters for a scheduling system: an amendment extends an existing counter, a reauthorization starts a new one, and the two have different lead times and different documentation packets.

### 1.7 Retro-authorization (retrospective authorization)

A request submitted after services were rendered, asking the payer to authorize them retroactively. Distinct from **backdating**, in which a payer issues an authorization with an effective date earlier than the request date. Payers treat these as different things and grant them on different terms. Published windows range from "will not" through "2 days" to "5 business days" — see §2.3.

### 1.8 Appeal

Formal challenge to a denial. In Medicare Advantage, appeal rates are low and overturn rates are high — 11.5% of denied requests were appealed in 2024, and 80.7% of those appeals were overturned in whole or in part ([KFF, Jan 28, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/), analyzing CMS Part C reporting). The 2025 data show 67% of MA denials overturned on appeal ([KFF, Aug 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/)).

### 1.9 The orthogonal gate: the physician order

Every Medicare-certified home health episode also requires a signed plan of care and a face-to-face encounter, independent of payer authorization. The Health Affairs Scholar study calls this out as "another layer to the authorization process" — an agency can hold a valid payer authorization and still be unable to bill. Jefferson Health Plans requires either a "VALID verbal signature in 5 days" or a signed plan of care by the certifying practitioner, with a "signed POC required every 60 days" ([Jefferson Health Plans, Oct 14, 2024](https://www.jeffersonhealthplans.com/providers/provider-news/medicare-home-care-utilization-review-process/)).

**A scheduling system that models only payer authorization will schedule visits that cannot be billed.** Two independent gates must both be open.

---

## 2. Pending / provisional authorization

### 2.1 What it actually means

There is no industry-standard definition. In published payer material, three distinct constructs travel under the label:

| Construct | What it is | Contractual force |
|---|---|---|
| **Request pending decision** | A submitted request the payer has not yet adjudicated. In X12 278 terms, an `HCR*A4` "pended" response. | None. Confers no right to deliver care. |
| **Payer-granted start-of-care allowance** | The payer affirmatively permits a bounded volume of care before authorization, and commits to pay if the subsequent request is approved. | Real, and payer-specific. This is the only construct that makes care safe to schedule. |
| **Agency risk-start** | The agency starts care without payer sanction, intending to seek retro-auth. | None. Pure agency financial risk. |

Field usage collapses all three into "pending auth." A rules library must keep them separate, because only the middle one is schedulable.

### 2.2 Which payer types offer a genuine start-of-care allowance, and how large

Published examples, all from primary payer or network sources:

| Payer / manager | Allowance before authorization must be in hand | Source |
|---|---|---|
| **UnitedHealthcare MA via Home & Community (formerly naviHealth)** | **First 30 days of care.** "Documentation is NOT required for authorization of services provided in the first 30 days of care… Your agency should provide care based on your home care orders for the first 30 days of care." Referral to the network within 5 days of SOC. Days 31–60 requested by day 25. | [Option Care / CSI guide, rev. 8/2024, p. 6](https://optioncarehealth.com/wp-content/uploads/Authorization-Guide.-Ohio-rev8.2024.pdf) |
| **UnitedHealthcare MA via Optum** | **Days 1–14.** "Prior authorization is required for all home health services after the initial start of care (SOC) and subsequent visits between days 1-14. Optum will NOT backdate after day fourteen (14) of the first certification period." SOC reported to the network within 72 hours; days 15–60 requested around day 7. | Same guide, p. 4 |
| **Highmark BCBS Medicare Advantage (HRT prefix)** | **Evaluation visit only.** "only allows eval visits upfront for the Initial authorization request." Ongoing auth must then be requested with eval notes attached. Commercial Highmark plans vary; "Your initial Provider Auth Form will indicate EVAL only or 1 visit approved per discipline." | Same guide, p. 3 |
| **Jefferson Health Plans (Medicare)** | **Initial evaluation only, no prior auth.** "A prior authorization for initial evaluations for home care services is not required." Request must be faxed within five business days of the initial visit. "If further treatment is needed following the initial evaluation, a prior authorization will be required." | [Jefferson Health Plans, Oct 14, 2024](https://www.jeffersonhealthplans.com/providers/provider-news/medicare-home-care-utilization-review-process/) |
| **Sunshine Health (Centene, FL Medicaid)** | **Initial nurse evaluation visit only.** "Home health and home infusion (initial nurse evaluation visit does not require a prior authorization)." | [Sunshine Health Prior Authorization](https://www.sunshinehealth.com/members/medicaid/resources/Prior-Authorization.html) |
| **MA plans generally (qualitative)** | Reported allowances of "15 visits" auto-approved, "30 units right up front without any concurrent review," and "100% of any referral that comes out of a facility" auto-approved — alongside plans authorizing only "two nursing visits" at a time. | [Thomas KS et al., *Health Affairs Scholar*, March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917) |
| **Montana Medicaid (FFS)** | **None.** "Home Health services must be prior authorized before the services are delivered… The Department will not back date prior authorizations." A five-business-day post-visit request window nonetheless exists (see §2.4). | [Montana Home Health Policy 410](https://dphhs.mt.gov/assets/sltc/HomeHealth/Section400/HH410PrAuth.pdf), p. 1–2 |
| **The Health Plan / Hometown** | **None.** "The Health Plan will not provide a retro authorization. If services are rendered after hours, over the weekend or on a holiday, providers are required to request authorization the next business day." | Option Care / CSI guide, p. 4 |

**Pattern:** the largest allowances come from delegated post-acute vendors managing Medicare Advantage lives (14 to 30 days), the smallest from Medicaid fee-for-service and small regional plans (zero). Commercial and Medicaid managed care cluster at "evaluation visit only."

**Important currency caveat.** The Option Care / CSI guide is dated 8/2024. UnitedHealthcare announced that effective **April 1, 2025**, prior authorization and concurrent review are no longer required for home health services managed by Home & Community across 41 states and D.C., for MA and D-SNP plans, with carve-outs for Florida and Tennessee D-SNP plans not managed by Home & Community ([UHCprovider.com, published March 1, 2025](https://www.uhcprovider.com/en/resource-library/news/2025/home-health-prior-auth-changing.html)). The 30-day allowance described above has, for that book of business, been superseded by no authorization requirement at all. **This is the single largest structural change in home health authorization in the study period, and it is payer-specific, not industry-wide.**

### 2.3 Are services delivered against a pending auth retroactively payable?

This is the question the field most needs answered and it has no general answer. What published language exists is specific and grudging.

**Payers publish backdating windows, in days, and they are short.**

- Anthem commercial, Ohio: "Ohio plans will only back date 2 days." Out-of-state Anthem: "backdates can be 0-5 days." (Option Care / CSI guide, p. 3)
- Blue Cross / Blue Shield plans generally: "Ohio and Out of State varies on backdates per plan." (p. 3)
- Carelon (formerly myNexus): "The time limit for accepting a backdated authorization request under CSI is five (5) business days." (p. 7)
- Optum: will not backdate after day 14 of the first certification period. (p. 4)
- Montana Medicaid: "The Department will not back date prior authorizations," stated twice, once for initial and once for extended services. (Policy 410, pp. 1, 4)
- The Health Plan / Hometown: "will not provide a retro authorization." (p. 4)

**And every payer reserves the right not to pay anyway.** The near-universal disclaimer, quoted here from the Option Care guide (p. 1): *"Authorization is NOT a guarantee of payment. Reimbursement is subject to medical necessity and patient's eligibility with the Payer at the time the service is rendered."* This language appears in essentially every provider manual reviewed. Its practical effect is that even a *granted* authorization is a conditional promise; a *pending* one is not a promise at all.

**The one clear published rule about non-payment after a pending state** is Jefferson Health Plans': "services will only be reimbursable for 48 hours after Jefferson Health Plans has instructed the provider that further services are denied" ([Jefferson Health Plans, Oct 14, 2024](https://www.jeffersonhealthplans.com/providers/provider-news/medicare-home-care-utilization-review-process/)). That is a *wind-down* allowance, not a pending-auth allowance, and it is 48 hours.

**Conclusion.** Where a payer publishes an explicit start-of-care allowance (Optum days 1–14, Home & Community first 30 days, evaluation-visit exemptions), services in that window are payable on subsequent approval — that is the point of the allowance. Where a payer publishes only a backdating window, services in that window are payable *only if the request lands inside the window and is approved*, and the window is typically 2 to 5 days. Where a payer publishes neither, or publishes "no retro authorization," services delivered before an authorization number exists are at agency risk with no published recourse.

**No authoritative public source** quantifies how often pending-auth visits are ultimately paid. The Health Affairs Scholar study records agencies facing "write-offs" when authorizations are denied retroactively, and notes the structural bind: Medicare Conditions of Participation obligate timely care while payer authorization lags. It does not quantify the write-off rate.

### 2.4 Where practice varies from published rule

Three documented tensions:

1. **Montana Medicaid simultaneously requires authorization before delivery and gives the provider "five business days from the initial visit to request authorization"** (Policy 410, pp. 1–2). Both statements are in the same policy. The operative reading is that the first visit is tolerated and the authorization must catch up within five business days — but the policy never says the first visit is payable, and it says twice that the Department will not backdate. This is a published rule that cannot be followed literally.

2. **UMR imposes the penalty on the patient, not the agency.** "UMR may require 48 hours advance notice for start of care. If that criteria are not met, UMR may impose a financial penalty on the patient. Both the initial and ongoing authorization requests must be requested two business days in advance." (Option Care / CSI guide, p. 4). A scheduling system that treats authorization risk as purely a revenue question misses this.

3. **Hospitalization mid-episode may or may not void the authorization.** Optum: "any auth that was not used prior to their hospitalization is still valid within that certification period" (p. 5). But the same guide's general instructions warn: "When a patient is hospitalized during an authorization period, notification to CSI is needed as some payers may require a new auth upon resumption of care" (p. 1). Resumption-of-care behavior is payer-specific and must be a modeled field.

---

## 3. Reauthorization gates

Three gate types appear in published policy. They are not mutually exclusive; several payers apply two at once, and the binding gate is whichever fires first.

### 3.1 Completion-based gates (a proportion of authorized visits used)

The agency must request the next authorization when a threshold share of the current authorization has been consumed.

**The clearest published example is Montana Medicaid**, which sets the gate in *remaining visits*, not percentage: extended-service requests "must be submitted no later than **14 business days before the 180-visit limit is reached** in order to assure timely approval," with the reminder that "The Department will not backdate prior authorization requests" ([Montana Home Health Policy 410](https://dphhs.mt.gov/assets/sltc/HomeHealth/Section400/HH410PrAuth.pdf), p. 4). Because the gate is expressed in *business days at current utilization*, satisfying it requires the agency to project its own visit burn rate forward — a scheduling computation, not a clerical one.

Montana also documents the amendment path as an unbounded loop: "The process for amending prior authorizations continues until the Home Health visit limit of 180 visits is reached or 365 days from the start of care has been reached" (p. 3).

**The Option Care guide describes the completion gate informally for Optum-managed UHC**: agencies request days 15–60 "around day seven (7) of the first 14 days," i.e. at roughly 50% of the provisional window consumed (p. 4).

**No authoritative public source** was found for a payer publishing a percentage-of-visits threshold (e.g. "request reauthorization at 80% utilization") in home health. Percentage-based triggers are common in EMR configuration and in agency internal policy, but the author found no payer manual stating one. Treat percentage thresholds as an agency-side safety margin, not a payer rule.

### 3.2 Documentation-based gates (clinical justification of continued need)

The most common type. The authorization is not granted on the calendar; it is granted on the arrival of a specific documentation packet.

Published packets:

- **Optum-managed UHC**, for days 15–60: 485/plan of care, start-of-care OASIS, discipline-specific evaluations, documentation supporting homebound status and need for intermittent care, physician orders not on the 485, wound care notes if applicable, and "Last two (2) visit notes for each discipline involved." (Option Care / CSI guide, p. 4)
- **Home & Community-managed UHC**, for days 31–60, by day 25: the same packet plus "Visit logs for each discipline – this will be compared to home care order." (p. 6)
- **Montana Medicaid** amendments: SLTC 124 form flagged as amendment, "Two nursing/therapy visit notes," and a re-signed SLTC 126 plan of care "if more than 60 days has elapsed since the last physician certification date." (Policy 410, p. 2)
- **Option Care baseline ongoing packet**: "Current signed 485 and any subsequent order; Oasis/Evaluations; Recent (2-3) visit notes for each discipline… For PDN include last 7-14 days of visit notes, for all other services include last 3-5 days of visit notes." (p. 2)

**The documentation gate has a hidden clock-restart hazard.** For BCBS plans: "These plans can take up to 14 days to review documentation and approve authorizations. If ALL clinicals are not available for CSI to upload to the payer, when additional clinicals must be requested, the 14 days can start over again when the additional clinicals are uploaded to the payer" (p. 3). The general note adds that "some payers will restart the clinical review once all documents are received" (p. 2). **An incomplete packet does not delay the decision by the time to complete it; it can reset the entire review clock.** This is the single highest-leverage operational fact in the reauthorization process.

### 3.3 Calendar / benefit-window gates

The authorization expires on a date regardless of visits used.

- **Carelon Post Acute Solutions** introduced "a standardized 30-day review period for all home health authorizations" effective **May 16, 2025** ([Carelon Post Acute Solutions — Home Health Program](https://providers.carelonmedicalbenefitsmanagement.com/postacute/provider-materials/anthem-provider-resources/home-health/)). Carelon manages most Aetna MA plans in OH, KY, WV, PA and specified Anthem MA prefixes in OH and IN (Option Care / CSI guide, p. 7).
- **Optum-managed UHC recertification**: "All recertifications require prior authorization in 60-day increment. Between days 40 to 50 provide disciplines and number of visits needed for the new cert period." (p. 5) — a calendar gate with a 10-day submission *window*, not a deadline.
- **Home & Community-managed UHC recertification**: "submit your recertification authorization request… in days 56 to 60 of the previous certification period." (p. 6) — a 5-day window, closing on the last day of the period.
- **Montana Medicaid extended services**: "Authorized services will have an authorized date span not to exceed 60 days from the date of the Extended Service request." (Policy 410, p. 4) — note the span runs from the *request* date, not from the exhaustion date, so late requests shorten the resulting authorization.
- **Some payers key ongoing requests to a date range rather than the certification period at all**: "Some payers ongoing auth request is based on date range i.e., Anthem, 3rd party Aetna, Frontpath, OSU and OH PPO Connect - CSI's auth team will advise your agency if it is NOT by certification period for future requests" (Option Care / CSI guide, p. 2). **The reauthorization cadence and the clinical certification cadence are independent and frequently misaligned.**

### 3.4 The submission-window shape matters as much as the trigger

Note the variety: Optum days 40–50 (a 10-day window in the middle of the period), Home & Community days 56–60 (a 5-day window at the end), Montana "no later than 14 business days before the limit is reached" (a rolling deadline computed from burn rate). A rules library needs to represent an *open* date and a *close* date for the reauthorization window, not a single due date — early submission is disallowed by some payers and mandatory for others.

---

## 4. Benefit windows keyed to a date other than start of care

These exist, they are published, and they are the most under-modeled construct in home health scheduling.

### 4.1 The verified example: California Health & Safety Code § 1374.10

California's mandated home health benefit is anchored to **the end of inpatient confinement**, not to start of care. Quoted verbatim from the statute as reproduced in UnitedHealthcare's own benefit policy:

> "(ii) the home health treatment plan is established and approved by a physician **within 14 days after an inpatient hospital confinement has ended** and such treatment plan is for the same or related condition for which the covered person was hospitalized; and (iii) home health care **commences within 14 days after the hospital confinement has ended**."

([California Health & Safety Code § 1374.10](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1374.10&lawCode=HSC), effective Jan 1, 1979, as reproduced in [UnitedHealthcare West Benefit Interpretation Policy BIP075.O, "Home Health Care," effective 10/01/2025](https://www.uhcprovider.com/content/dam/provider/docs/public/policies/signaturevalue-bip/home-health-care-ca.pdf), p. 1.)

Two clocks, both starting at discharge, both 14 days: the physician's plan of care must be established, *and* care must commence. The same statute caps the benefit at not less than 100 visits per calendar year and specifies that "each visit by a representative of a home health agency shall be considered as one home health care visit. A visit of four hours or less by a home health aide shall be considered as one home health visit."

### 4.2 Medicare's post-institutional home health benefit

Under traditional Medicare, the first 100 visits of a home health spell of illness are paid under Part A rather than Part B where the beneficiary had a qualifying 3-day inpatient stay or SNF stay and home health begins **within 14 days of discharge**. The canonical source is the [Medicare Benefit Policy Manual, Chapter 7 — Home Health Services](https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/bp102c07.pdf); CMS returned HTTP 403 to automated retrieval in this session, so the specific section numbers are not quoted here. This rule allocates cost between Part A and Part B rather than gating coverage, so its scheduling consequence is financial rather than access-limiting — but it is the origin of the 14-day convention that appears throughout commercial and state-mandated benefit language.

### 4.3 The scheduling consequence of days lost before admission

This is the mechanism that makes discharge-keyed windows dangerous.

Under a start-of-care-keyed authorization, delay before admission costs nothing but time-to-care. Under a discharge-keyed window, **every day between discharge and admission is consumed from the benefit itself.** A referral that sits three days in intake against a 14-day discharge-keyed commencement requirement has spent 21% of the window before a clinician has been assigned. If the plan-of-care signature is also discharge-keyed — as it is in California — the agency must obtain a physician signature inside the same shrinking window, and the two clocks do not run independently; they run out together.

The compounding case is documented in the Health Affairs Scholar study: hospitals request an initial visit within "24 to 48 hours" of discharge, while authorization turnaround from MA plans and post-acute management companies runs "three to six days, maybe a week," with an extreme case of "14 days from the Medicare Advantage plan" ([Thomas KS et al., March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917)). Where a discharge-keyed 14-day commencement rule meets a 14-day authorization turnaround, the window can close before the authorization arrives.

**Practical rule for a scheduling platform:** the anchor date of a benefit window is a required field with three legal values at minimum — start of care, hospital/facility discharge date, and calendar/plan year — and days-elapsed-since-anchor must be computed at referral intake, not at admission. Where the anchor is discharge, the referral's remaining window shrinks in the queue.

### 4.4 Other anchors observed

The WellCare 2026 home health authorization request form carries a discrete field: "Are services needed for discharge planning? ☐ Yes ☐ No  Discharge Date: __/__/__" ([WellCare Home Health Authorization Request Form, form ID 5715951_NA6PCARFRME, internally approved 02/03/2026](https://www.wellcare.com/-/media/pdfs/na/provider/forms/auth/na_care_prov_home_health_auth_request_form_2026_r.ashx)). The discharge date is captured separately from the requested service start date, which implies it drives something in adjudication — but WellCare does not publish what.

Montana Medicaid anchors its annual limit to the **initial service visit**: "Home Health services are limited to 180 visits within 365 days of the initial service visit" (Policy 410, p. 1) — a rolling patient-specific year, not a calendar year. A system that assumes calendar-year benefit accumulators will mis-project this.

---

## 5. Shared discipline pools

A single visit allowance drawn on by multiple disciplines together. Published examples exist and they are common enough to be a first-class modeling requirement.

### 5.1 Verified home-health examples

**Montana Medicaid — 180 visits, all disciplines, one pool, one authorization number.** The pool is stated as an undifferentiated total: "Home Health services are limited to 180 visits within 365 days of the initial service visit." The shared nature is demonstrated by the worked example in the policy: an initial authorization for **25 skilled nursing visits** is later amended to add **10 therapy visits**, and "The Contractor amends the initial prior authorization to reflect the additional therapy services **using the same authorization number**" ([Montana Home Health Policy 410](https://dphhs.mt.gov/assets/sltc/HomeHealth/Section400/HH410PrAuth.pdf), pp. 2–3). Nursing and therapy draw on one counter under one authorization.

**California statutory home health benefit — 100 visits, all disciplines, one pool.** § 1374.10(c) counts "each visit by a representative of a home health agency" as one visit against a floor of 100 per calendar year, with home health services defined in § 1374.10(b) to include nursing, aide, and physical/occupational/speech therapy. All disciplines share the counter. Aide visits of four hours or less count as one visit ([as reproduced in UHC BIP075.O](https://www.uhcprovider.com/content/dam/provider/docs/public/policies/signaturevalue-bip/home-health-care-ca.pdf), p. 2).

### 5.2 Adjacent examples (therapy pools, not home health specific — labeled)

These establish that pooled-therapy design is standard payer practice, but they govern outpatient or specialized therapy, not home health:

- **FEP Blue** (Blue Cross Blue Shield Federal Employee Program), 2025 brochure: Basic Option 50 visits and Standard Option 75 visits per person per calendar year for "physical, occupational, or speech therapy, **or a combination of all three**" ([FEP 2025 Standard and Basic Options brochure](https://www.2025-standard-and-basic-options.fepbrochures-bcbsa.com/)).
- **North Carolina Medicaid**, Clinical Coverage Policy 10A: "a total maximum of 30 treatment visits per calendar year combined across occupational and physical therapy" ([NC Medicaid, July 1, 2024](https://medicaid.ncdhhs.gov/blog/2024/07/01/updates-clinical-coverage-policy-10a-outpatient-specialized-therapies)).
- **Vermont Medicaid** explicitly *disapplies* its combined outpatient therapy limit to home health: "The 30 combined visit limit for outpatient therapy does not apply to services provided by home health agencies," and home health PT/OT/SLP is covered up to 4 months on physician order with PA beyond ([Vermont DVHA PT/OT/ST supplement](https://dvha.vermont.gov/sites/dvha/files/documents/providers/Forms/PT_OT_STSupplement.pdf)). Vermont further removed PA for home health PT/OT/SLP effective 1/1/26 per the same source — a useful illustration that pooling and PA rules are set independently.

### 5.3 The counter-pattern: strictly per-discipline bundles

Cigna's HealthSpring publishes diagnosis-driven bundles that are strictly **per-discipline**, with separate counts per discipline per 60-day period ([HealthSpring Home Health Care Authorization](https://www.healthspring.com/providers/home-health-authorization)):

| Diagnosis | SN (1st/2nd 60d) | PT | OT | ST | HHA | MSW |
|---|---|---|---|---|---|---|
| Generic | 3 / 2 | 3 / 3 | 1 / 1 | 1 / 1 | 3 / 3 | 1 / 1 |
| Orthopedic | 6 / 3 | 12 / 8 | 4 / 4 | 1 / 1 | 6 / 3 | 1 / 1 |
| Heart failure | 12 / 8 | 12 / 8 | 8 / 4 | 1 / 1 | 12 / 6 | 1 / 1 |
| COPD | 12 / 8 | 12 / 8 | 8 / 4 | 1 / 1 | 12 / 6 | 1 / 1 |
| Stroke / TIA | 12 / 8 | 16 / 12 | 8 / 6 | 8 / 4 | 12 / 8 | 1 / 1 |
| Open wound | 20 / 10 | 12 / 8 | 8 / 4 | 1 / 1 | 3 / 2 | 1 / 1 |
| Oncology | 16 / 12 | 16 / 12 | 8 / 4 | 1 / 1 | 12 / 8 | 1 / 1 |
| Diabetes | 16 / 8 | 12 / 6 | 8 / 4 | 1 / 1 | 3 / 1 | 1 / 1 |
| CKD / ESRD | 16 / 10 | 12 / 8 | 4 / 2 | 1 / 1 | 3 / 3 | 1 / 1 |

Two things follow. First, **the initial authorization is a function of the working diagnosis** — a data element usually not final at referral. Second, note the ST column: 1 visit for every diagnosis except stroke. A speech-therapy plan of care for a COPD patient requires an amendment before the second ST visit can be scheduled.

### 5.4 Modeling implication

Pooling is not a payer-level attribute; it is a benefit-level attribute that can differ between two products from the same payer. A rules library must be able to express: a set of disciplines, a shared counter, per-discipline sub-caps inside the shared counter (common: a pooled total with an aide sub-cap), and unit-of-count semantics (a 4-hour aide visit counting as one visit is a published rule, not a convention).

---

## 6. Transaction mechanics

### 6.1 The X12 278

The HIPAA standard for authorization is the **ASC X12N 278 Health Care Services Review**, implementation guide 005010X217, in request (278-A1) and response (278-A3) flavors ([Stedi X12 HIPAA 278 guides](https://www.stedi.com/edi/hipaa/transaction-set/278-A3)).

The response conveys the decision in the **HCR segment**:

| Code | Meaning |
|---|---|
| A1 | Certified in total |
| A2 | Not certified |
| A3 | Certified in part |
| A4 | Pended |
| A6 | Modified |
| CT | Contact payer |

Volume is conveyed in the **HSD** segment with a quantity qualifier — `VS` for visits — and can express a *pattern*, not just a total. `HSD*VS*1*DA*3*7*21~` means one visit every three days for 21 days ([Stedi 278-A3 guide](https://www.stedi.com/edi/hipaa/transaction-set/278-A3)). Date ranges ride in **DTP** segments; the authorization number returns in HCR02 and/or a **REF** administrative reference number. X12's own worked example returns `HCR*A1*AUTH0001~` with `HSD*VS*1~` and `DTP*AAH*RD8*20050502-20050602~` ([X12, Example 1b: Response to the Request for Review](https://x12.org/examples/005010x217/example-1b-response-request-review)).

Home health has a specific data requirement in the guide: requests for home health care must include a principal diagnosis (`HI01=BK`) and principal diagnosis date in the HI segment of Loop 2000E.

**The 278 is expressive enough for home health.** It can carry per-discipline service lines, visit counts, frequency patterns, date spans, a pended state, and a partial certification. The problem is not the standard.

### 6.2 Why adoption is uneven

Adoption of fully electronic prior authorization in the medical industry, per the CAQH Index:

| Year | Fully electronic (X12 278) | Partially electronic (portal, IVR) | Fully manual (phone, mail, fax, email) |
|---|---|---|---|
| 2022 | 28% | 35% | 37% |
| 2023 | 31% | 39% | 33% |
| 2024 | 35% | 43% | 22% |
| 2025 | 40% | not extracted | not extracted |

(2022–2024: [2024 CAQH Index Report](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf), p. 19. 2025 figure: [AJMC coverage of the 2025 CAQH Index](https://www.ajmc.com/view/caqh-index-finds-20-billion-in-cost-savings-opportunities).)

**Prior authorization is the only major HIPAA transaction where the portal, not the standard, is the dominant channel.** By comparison, eligibility verification and claim submission are each over 90% electronic. CAQH names the causes: "the structure of the transaction, lack of mandated operating rules that support electronic exchange, and limited infrastructure for electronic submissions of clinical documentation" ([CAQH CORE Priority Topics](https://www.caqh.org/core/priority-topics)).

The clinical-documentation point is the decisive one for home health. Home health authorization is adjudicated on OASIS, the 485, discipline evaluations, visit logs, and wound notes — a documentation packet, not a code. The 278 can *reference* attachments via PWK segments pointing at an X12 275, but the attachment standard was never mandated, so in practice the clinical packet moves by fax or portal upload while the 278 carries only the skeleton. A transaction that cannot carry the thing the decision is made on does not eliminate the manual step.

### 6.3 Portal vs fax vs phone, as actually practiced in home health

All three remain live, often for the same payer:

- **Portal, with fax fallback.** Carelon: "Carelon encourages providers to utilize the online provider portal to submit authorization requests" at portalct.mynexuscare.com, with an "Initial authorization request form" and a separate "Re-authorization request form" available for fax ([Carelon Post Acute Solutions Home Health Program](https://providers.carelonmedicalbenefitsmanagement.com/postacute/provider-materials/anthem-provider-resources/home-health/)). Option Care's guide likewise: "When the portal is not available you can Fax the authorization request to 440.550.8835" (p. 1).
- **Fax as primary.** WellCare's 2026 home health authorization request form is a fax form with thirteen state-specific Medicare fax numbers on the back page ([WellCare form 5715951_NA6PCARFRME](https://www.wellcare.com/-/media/pdfs/na/provider/forms/auth/na_care_prov_home_health_auth_request_form_2026_r.ashx)). Jefferson Health Plans requires the initial evaluation request and signed NOMNC "faxed to 215-967-4491 within five business days of the initial visit" ([Jefferson, Oct 14, 2024](https://www.jeffersonhealthplans.com/providers/provider-news/medicare-home-care-utilization-review-process/)).
- **Portal proliferation is the actual burden.** The Health Affairs Scholar study records agencies managing "four or five different portals," and up to "10+" separate systems across plans ([Thomas KS et al., March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917)).

Multi-payer portal aggregators exist. Availity's Authorizations tool uses the HIPAA 278, supports electronic attachment of "supporting medical documentation," and offers a cross-payer dashboard to "review pending authorizations for all health plans" ([Availity Prior Authorizations](https://www.availity.com/authorizations/)). Availity does not mention home health specifically and publishes no auto-approval or turnaround statistics.

### 6.4 CMS-0057-F: what is live in 2026, what arrives in 2027

The CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F, published January 2024) binds **Medicare Advantage organizations, state Medicaid and CHIP fee-for-service agencies, Medicaid and CHIP managed care entities, and Qualified Health Plan issuers on the federally facilitated exchanges**. Canonical source: the [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f) (CMS returned HTTP 403 to automated retrieval in this session; the compliance dates below are quoted from CAQH, which restates them).

The rule splits into two compliance waves:

**Live as of January 1, 2026 — operational provisions, no technology required.** CAQH states it plainly: "Implementers have until January 1, 2026 to integrate changes, such as decision timeframes and reasons for denial, into their workflows" ([2024 CAQH Index Report](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf), p. 20). Those provisions are:

- **Decision timeframes**: 72 hours for expedited requests, 7 calendar days for standard requests. Payers have restated this in their own 2026 material — Humana's provider guidance states "Effective Jan. 1, 2026, CMS requires prior authorization decisions within 7 days for certain medical items/services requests" ([Humana provider prior authorizations](https://provider.humana.com/coverage-claims/prior-authorizations)).
- **Specific reason for denial** must be given.
- **Public reporting of prior authorization metrics**, beginning 2026.

**Arriving January 1, 2027 — the APIs.** "They have until January 1, 2027 to deploy HL7 FHIR-based Prior Authorization APIs" (CAQH, same page). Four APIs are in scope: Patient Access API (extended to include prior authorization information), Provider Access API, Payer-to-Payer API, and the Prior Authorization API. Drugs are excluded from the prior authorization provisions.

**One consequential side effect for anyone building on the 278:** "CMS has since exercised enforcement discretion of the X12 278 transaction for HIPAA-covered entities that conduct prior authorization workflows electronically using HL7 FHIR… It is anticipated that use of the X12 278 will decrease as industry approaches regulatory deadlines" ([2024 CAQH Index](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf), p. 17). **Building a 2026-era integration strategy on the 278 alone is building on a standard CMS has already begun to deprecate in practice.**

### 6.5 What an agency can realistically automate today

Honest assessment, given the above:

| Function | Automatable today? | Basis |
|---|---|---|
| Eligibility verification (270/271) | **Yes, fully.** | 84%+ industry electronic adoption; sub-$0.05 plan cost. Most home health EMRs and clearinghouses support it. |
| Determining whether home health needs prior auth for this member | **Partially.** | Requires a maintained payer rules library. No transaction returns this reliably. Delegation routing (Optum vs Home & Community vs Carelon vs direct) is keyed to plan and sometimes to member-ID prefix. |
| Submitting the authorization request skeleton | **Partially.** | 278 works where the payer accepts it; portal RPA otherwise. 40% electronic industry-wide as of the 2025 CAQH Index. |
| Submitting the clinical documentation packet | **Largely no.** | No mandated attachment standard. Portal upload or fax. This is the binding constraint. |
| Status polling and pended-state detection | **Yes, where 278 or portal API exists.** | HCR code A4 is machine-readable. |
| Decrementing visit counters against the authorization | **Yes — this is agency-side and requires no payer cooperation.** | Entirely within the EMR/scheduling system's control. See §9 for how poorly it is done. |
| Computing the reauthorization trigger date | **Yes — agency-side.** | Requires the rules library in §10. No payer dependency. |
| Detecting that a scheduled visit will exceed the authorization | **Yes — agency-side.** | See §9: most systems warn rather than block. |

**The strategic point:** the two highest-value automations — counter decrementing and reauthorization trigger computation — require no payer integration at all. They require a rules library and a scheduling engine that reads it. Everything that requires payer cooperation is bottlenecked on an attachment standard that does not exist.

---

## 7. Turnaround times, denial rates, appeals

### 7.1 Turnaround — regulatory floor

| Requirement | Standard | Expedited | Effective | Source |
|---|---|---|---|---|
| CMS-0057-F (MA, Medicaid/CHIP FFS & MCO, FFE QHPs) | 7 calendar days | 72 hours | Jan 1, 2026 | [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f); dates restated in [2024 CAQH Index](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf) p. 20 |
| Florida Statewide Medicaid Managed Care (SMMC 3.0) | 5 calendar days | — | Feb 2025 contracts | Reported in FL Medicaid plan material; see Sunshine Health below |
| Sunshine Health (Centene FL Medicaid) | 5 calendar days | 48 hours if urgent | current | [Sunshine Health Prior Authorization](https://www.sunshinehealth.com/members/medicaid/resources/Prior-Authorization.html) |

### 7.2 Turnaround — measured, general-medical (labeled)

**KFF, from insurer-reported 2025 metrics** ([KFF, Aug 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/)) — *general medical, all services, not home health*:

| Market | Median standard decision | Median expedited decision |
|---|---|---|
| Medicare Advantage | ~0.9 days | 0.4 days |
| Medicaid managed care | ~0.9 days | ~0.4–1 day |
| ACA marketplace | ~0.9 days | ~1 day |

These medians sit far inside the regulatory limits. **They should be treated with caution for home health planning.** A median across all services is dominated by high-volume, low-complexity, algorithmically-adjudicated requests (imaging, drugs). Home health authorization is adjudicated on a clinical documentation packet and clusters in the tail. KFF itself flags the limitation: insurers report percentages without numerators, use no mandatory template, and provide no service-level detail — "Aggregated data prevents understanding which specific services drive denial patterns."

**HHS OIG measured a 5-to-6-day average delay to initial denial for post-acute care** ([reported in KFF, July 6, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-deny-prior-authorization-requests-for-post-acute-care-at-substantially-higher-rates-than-the-overall-denial-rate/)).

### 7.3 Turnaround — home health specific

**No authoritative public dataset exists for home health authorization turnaround.** No payer publishes it by service line; CMS does not collect it by service line ([KFF, Jan 28, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/): CMS "does not collect or report this information" by type of service).

What exists is two credible non-statistical sources.

**Payer-specific commitments and observed ranges, from a network operator's published guide** ([Option Care Health / CSI Authorization Guide, Ohio, rev. 8/2024](https://optioncarehealth.com/wp-content/uploads/Authorization-Guide.-Ohio-rev8.2024.pdf)):

| Payer | Stated turnaround |
|---|---|
| Anthem commercial, Ohio | "Auth approval is usually 3-5 days" |
| Anthem commercial, out-of-state | "Auth approvals can be 7-14 days" |
| Blue Cross / Blue Shield plans | "can take up to 14 days to review documentation and approve authorizations," with clock restart on late clinicals |
| UHC managed by UMR | "can take 4-14 days for both initial and ongoing" |

**Qualitative measurement from the peer-reviewed literature** ([Thomas KS et al., *Health Affairs Scholar*, March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917)): additional-visit authorization delays of "three to six days, maybe a week"; a worst case of "14 days from the Medicare Advantage plan" against a hospital request for a 24–48 hour initial visit; longest delays attributed to post-acute management companies with repeated resubmission cycles and lost requests. Counterpoint from the same study: some managers return "approval right in the system… within two minutes" by algorithm.

**Planning conclusion:** the operationally relevant number for home health is not the median. It is the width of the distribution — same-day algorithmic approval at one end, 14 days with a restartable clock at the other, with the payer and the completeness of the clinical packet determining which. A scheduling platform should model turnaround as a payer-specific range with a documented restart hazard, not a point estimate.

### 7.4 Denial rates

**Medicare Advantage, all services** ([KFF, Jan 28, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/), from CMS Part C reporting, contract year 2024):

- 52.8 million prior authorization determinations
- 4.1 million denied = **7.7%**
- 1.7 requests per enrollee
- By insurer: Elevance 4.2%, Humana 5.8%, Centene 12.3%, UnitedHealth Group 12.8%

**2025 insurer-reported metrics** ([KFF, Aug 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/)):

| Market | Standard requests denied | Expedited requests denied |
|---|---|---|
| Medicare Advantage | 12% | 10% |
| Medicaid managed care | 14% | 12% |
| ACA marketplace | 18% | 16% |

**Post-acute care specifically** ([KFF, July 6, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-deny-prior-authorization-requests-for-post-acute-care-at-substantially-higher-rates-than-the-overall-denial-rate/), citing OIG, 2024 data):

| Setting | Denial rate | Appeal rate | Overturn rate |
|---|---|---|---|
| Long-term acute care hospitals | 65% | 36% | 36% |
| Inpatient rehabilitation facilities | 54% | 31% | 43% |
| Skilled nursing facilities | 12% | 18% | 95% |
| MA overall | <8% | — | — |

**Home health is not broken out in this analysis.** This is explicit in the KFF piece and is the central data gap in the whole subject area.

**HHS OIG's structural finding** ([*Some Medicare Advantage Organization Denials of Prior Authorization Requests Raise Concerns About Beneficiary Access to Medically Necessary Care*, OEI-09-18-00260, April 2022](https://oig.hhs.gov/oei/reports/OEI-09-18-00260.pdf)): 13% of MA prior authorization denials were for service requests that **met Medicare coverage rules**, and 18% of payment denials were for claims that met both Medicare coverage rules and MAO billing rules. The mechanisms OIG identified were MAO clinical criteria not contained in Medicare coverage rules, requests for unnecessary documentation, and manual/system review errors. "Stays in post-acute facilities" is one of three prominent service categories in the denials reviewed.

**An important nuance for home health specifically.** OIG's post-acute findings largely concern MA plans denying *facility* post-acute care on the grounds that "a lower level of care (home health services) could meet the beneficiary's needs" (OEI-09-18-00260, case narratives). Utilization management pressure in Medicare Advantage tends to *push volume toward* home health while *constraining* the authorization granted for it. High MA post-acute denial rates are therefore not evidence of high home health denial rates — they are partly the mechanism generating home health referrals.

### 7.5 Home-health-specific denial rates and top denial reasons

**No authoritative public source** exists for home health prior authorization denial rates. The only quantitative signals located are self-reported and from interested parties:

- One MA plan self-reported "authorizing like 95% of our home health requests"; one post-acute management company reported an approval rate "in the 80s" when clinical necessity was documented ([Thomas KS et al., March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917)). These are interview self-reports in a qualitative study, not measurements.
- Homecare Homebase's outsourced revenue cycle service advertises a "2.5% Denial Rate" for its clients ([HCHB Services](https://hchb.com/hchb-services/)) — a vendor claim about *claim* denials for a selected client population, not an industry figure and not authorization-specific.

**Top denial reasons for home health authorizations: no authoritative public source.** The nearest general-medical proxy is Experian Health's State of Claims 2025, in which 50% of provider respondents named missing or inaccurate claim data as the leading contributor to rising denials, with authorizations among the top three reasons overall, and 41% of providers reporting at least 10% of claims denied (up from 38% in 2024 and 30% in 2022) ([Experian Health, State of Claims 2025](https://www.experian.com/blogs/healthcare/healthcare-claim-denials-statistics-state-of-claims-report/)). **This is general medical, not home health, and should not be presented as home health data.**

What *is* well documented for home health is the *mechanism* of authorization-related payment loss, from the payer manuals themselves: request submitted outside the backdating window (Anthem 2 days, Carelon 5 business days, Optum day 14), authorization not obtained before the requested start date for added visits, review clock restarted by an incomplete clinical packet, and NOA not filed within 5 days of start of care ([Jefferson Health Plans](https://www.jeffersonhealthplans.com/providers/provider-news/medicare-home-care-utilization-review-process/): "If NOA is not submitted within 5 days of start of care, services prior to receiving the NOA would not be reimbursable").

### 7.6 Appeal overturn rates

| Market | Denials appealed | Appeals overturned | Year | Source |
|---|---|---|---|---|
| Medicare Advantage | 11.5% | 80.7% | 2024 | [KFF, Jan 28, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/) |
| Medicare Advantage | — | 67% | 2025 | [KFF, Aug 13, 2026](https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/) |
| Medicaid managed care | — | 47% | 2025 | KFF, Aug 13, 2026 |
| ACA marketplace | — | 43% | 2025 | KFF, Aug 13, 2026 |
| SNF (post-acute) | 18% | 95% | 2024 | [KFF, July 6, 2026](https://www.kff.org/medicare/medicare-advantage-insurers-deny-prior-authorization-requests-for-post-acute-care-at-substantially-higher-rates-than-the-overall-denial-rate/) |

Overturn rates by MA insurer, 2025: Centene 93%, CVS 89%, Elevance 75%, Humana 64%, UnitedHealth Group 60%, Kaiser Permanente 40% (KFF, Aug 13, 2026).

**The asymmetry is the finding.** Two thirds to four fifths of appealed denials are overturned, but only about one in nine denials is appealed. Physicians explain why in the AMA survey: 59% do not believe the appeal will succeed based on past experience, 52% have insufficient staff resources or time, and 49% say patient care cannot wait for the health plan to approve ([2025 AMA prior authorization physician survey](https://www.ama-assn.org/system/files/prior-authorization-survey.pdf)). **A high overturn rate against a low appeal rate is a measurable, unexploited revenue position — bounded by the cost of appealing.**

---

## 8. Cost of the authorization function

### 8.1 Cost per prior authorization — the anchor numbers

From the [2024 CAQH Index Report](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf) (published Jan 2025), medical prior authorization, per transaction:

| Mode | Plan cost | Provider cost | Industry cost | Provider savings opportunity |
|---|---|---|---|---|
| Manual (phone, mail, fax, email) | $3.41 | **$12.88** | $16.29 | $7.50 |
| Partial (portal, IVR) | $0.05 | **$8.93** | $8.98 | $3.55 |
| Fully electronic (278) | $0.05 | **$5.38** | $5.43 | — |

The prior-year figures, for trend ([2023 CAQH Index Report](https://caqh.org/hubfs/43908627/drupal/2024-01/2023_CAQH_Index_Report.pdf)): manual provider cost $10.97, electronic $5.79. **Manual provider cost rose 17% year over year while electronic cost fell.** The gap is widening, not closing.

Two things about these figures matter for home health. First, **the burden is asymmetric by a factor of roughly 4:1 to 100:1** — $12.88 provider versus $3.41 plan on manual, $5.38 versus $0.05 on electronic. Prior authorization is a cost transfer, and the transfer ratio worsens as the plan automates. Second, **even full electronic adoption only halves provider cost.** Unlike eligibility (manual $8.57 → electronic $2.00), prior authorization retains a large irreducible human component even when the transaction is electronic, because the clinical judgment and documentation assembly do not go away.

### 8.2 Time per prior authorization

From the same report (p. 18):

- **24 minutes** per prior authorization using phone, fax, or email
- **16 minutes** per prior authorization using a health plan portal — "the highest time spent conducting an administrative transaction using a portal" of any transaction measured
- **14 minutes** average time savings opportunity per transaction from full electronic adoption

### 8.3 Industry-level burden

- Medical prior authorization cost savings opportunity: **$515 million** industry-wide ($414M provider, $101M plan), 2024 ([2024 CAQH Index](https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf), p. 19–20).
- 2024 national volume, provider side: 24M manual, 65M portal, 47M electronic prior authorizations (p. 19).
- The 2025 CAQH Index reports $20 billion in total administrative cost savings opportunity across all transactions and $258 billion in costs avoided ([AJMC](https://www.ajmc.com/view/caqh-index-finds-20-billion-in-cost-savings-opportunities); [2025 CAQH Index announcement](https://www.dataspring.com/blog/2025-caqh-index-shows-u.s.-healthcare-avoided-258-billion-and-accelerated-automation-interoperability-and-ai-adoption)).

### 8.4 Staffing burden — general medical (labeled)

From the [2025 AMA prior authorization physician survey](https://www.ama-assn.org/system/files/prior-authorization-survey.pdf) (n = 1,000 practicing physicians, 400 primary care / 600 specialists) — *general medical, physician practices, not home health*:

- **40 prior authorizations per physician per week**, on average
- **13 hours per week** per physician-and-staff completing prior authorizations
- **40% of physicians have staff who work exclusively on prior authorization**
- 95% report care delays; 26% report PA has led to a serious adverse event for a patient in their care
- 32% report PAs are often or always denied; 74% say denials have increased over the last five years
- 21% always appeal an adverse decision
- 94% report PA increases physician burnout
- 60% are concerned that AI increases or will increase PA denial rates

### 8.5 Staffing ratios in home health

**No authoritative public source.** No published benchmark was located for authorization coordinators per referral volume, per census, or per branch in home health. The absence is notable given how mature home health financial benchmarking otherwise is.

What exists is qualitative and directional, from the peer-reviewed literature ([Thomas KS et al., *Health Affairs Scholar*, March 2025](https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917)):

- Agencies describe "a whole team of people… just managing authorizations and documentation," characterized as "like pulling teeth."
- Some agencies outsource entirely: contracting "with a company… that does our eligibility, our authorization, and billing."
- One agency quantified the delegated-vendor overhead: working with a post-acute management company "increases my overhead admin… by 25%" while paying "ridiculously hideous rates."

That 25% figure is a single operator's self-report in a qualitative study of 44 interviews. **It is the only quantification of home health authorization overhead located in any published source, and it should be cited as illustrative, not as a benchmark.**

Corroborating the outsourcing trend from the vendor side: Homecare Homebase sells an Authorizations service in which HCHB staff "perform follow-up tasks to resolve pending authorizations and handle verification within payer required timelines" and "help your team perform appeals against denials" ([HCHB Services](https://hchb.com/hchb-services/)). Option Care Health's CSI network performs benefit verification and secures authorizations on member agencies' behalf ([CSI Authorization Guide](https://optioncarehealth.com/wp-content/uploads/Authorization-Guide.-Ohio-rev8.2024.pdf), p. 1). **A market exists for outsourcing this function, which is itself evidence that in-house software has not solved it.**

---

## 9. What home health EMR/EHR systems actually do with authorization today

### 9.1 The finding, stated plainly

Across the major home health EMRs, authorization is modeled as a **record to be entered and a warning to be shown** — not as a constraint on scheduling. The best-documented behavior in the category is a soft warning that permits the user to proceed.

### 9.2 Axxess (best-documented, primary source)

Axxess Home Health's Insurance Authorization module is the most transparently documented of the major vendors ([Axxess Help Center — Insurance Authorization](https://www.axxess.com/help/agencycore/intakescheduling/insurance-authorization/)).

- **Authorization types are explicitly modeled** as three variants: date range and units, date range only, or units only. This is a real and correct abstraction — it recognizes that some authorizations bound time, some bound volume, and some bound both.
- **Record contents**: payer/insurance, authorization type, authorized dates, authorized units, disciplines, comments, attached documents. An authorization *number* field is not documented on this page.
- **Enforcement is a soft warning, not a block.** Verbatim: *"a warning symbol will show on the left side of the task if it is not in the correct authorization range!"* The system triggers warnings when *"scheduled tasks exceed the number of visits/units authorized"* — **and does not prevent scheduling.** Clicking the warning lets the user attach the visit to a different authorization.
- **Attachment of visits to authorizations is a manual act.** Users select unauthorized tasks and click authorize. There is no documented automatic decrement on schedule or on completion.
- An **"Authorization Utilization"** report exists under Schedule Reports.
- Axxess Hospice separately added room-and-board authorization tracking ([Axxess Hospice — Room and Board Authorization Tracking](https://www.axxess.com/help/axxesshospice/software-updates/room-and-board-authorization-tracking/)), which is evidence that authorization tracking is being extended feature-by-feature rather than existing as a platform primitive.

### 9.3 Homecare Homebase

HCHB's public authorization material is marketing-level. Its "Streamlined Authorizations" page claims the platform "reduces the administrative burden on your staff" and includes "tracking of authorization requests and approval statuses and smooth integration with other patient management functions," plus "regular updates and integration with payer systems" ([HCHB — Streamlined Authorizations](https://hchb.com/functionality/streamlined-authorizations/)).

**No published documentation** was located specifying whether HCHB decrements visit counts automatically, whether it hard-blocks scheduling beyond an authorization, or which payer systems it integrates with. The claims are unquantified.

The more informative signal is adjacent: HCHB sells **Authorizations as a managed service**, with HCHB staff resolving pending authorizations and assisting with appeals ([HCHB Services](https://hchb.com/hchb-services/)). A platform vendor selling humans to operate its own authorization module is a strong indicator of where the software's boundary sits.

### 9.4 WellSky

WellSky's home health product page describes intake and scheduling that "optimizes intake, eligibility, and scheduling — with AI-powered referral management embedded directly in your workflow." Direct retrieval of wellsky.com returned HTTP 403 in this session, so this claim is taken from the indexed page description rather than a verified fetch, and should be re-verified. **No authoritative public documentation** was located for WellSky authorization record structure, automatic decrementing, alerting behavior, or 278 support.

### 9.5 MatrixCare

MatrixCare's home health page documents **eligibility** capabilities — "Verify commercial eligibility status with automatic and on-demand checks" and electronic verification of "a patient's Medicaid/Commercial eligibility" — plus electronic claim submission via eClaims and "advance alerts for Medicare receivables at risk" ([MatrixCare Home Health Software](https://www.matrixcare.com/home-health-software/)). **Authorization tracking, visit counts against authorizations, and electronic authorization submission are not mentioned on this page.** Eligibility is productized; authorization is not.

### 9.6 Netsmart myUnity

Netsmart's home care and hospice care-setting page describes myUnity as "a single EHR for home health, hospice, senior living, skilled nursing, palliative, adult day and personal care" and makes **no claims about authorization tracking, visit counts, alerts, or 270/271/278 transactions** ([Netsmart — Home Care and Hospice](https://www.ntst.com/solutions-and-services/care-settings/home-care-and-hospice)). **No authoritative public source** for myUnity authorization functionality was located.

### 9.7 Commure

Commure's published product lineup includes **Orchestrator**, described as "Unified, AI-powered referral intake," alongside RCM ("End-to-end medical billing automation" covering denial management and appeal automation), Ambient AI, Engage, Commure Pro, Strongline, and Athelas Home (point-of-care blood diagnostics for home settings) ([commure.com](https://commure.com/)).

**Prior authorization is not a standalone Commure product.** It appears only as a capability listed under "Care Navigation," alongside appointment scheduling and patient intake. Commure references home health agencies in blog content, but **no published material was located describing a home-health-specific authorization or benefit-tracking product.** The referral-intake product (Orchestrator) is the adjacent piece; a dedicated product page for it returned HTTP 404 in this session.

### 9.8 The gap, and who is naming it

The clearest articulation of the gap comes from a smaller vendor, CareVoyant, in a post explicitly framed around authorization mismanagement in home care ([CareVoyant, Dec 23, 2025](https://www.carevoyant.com/home-health-blog/authorization-mismanagement-home-care) — vendor content, treat claims accordingly). The failure modes it names map exactly onto what the major vendors' documentation does not cover:

- **Manual tracking of authorization dates and units** leading to missed renewals
- **Overscheduling** past approved visit limits
- **Expired authorizations** causing care interruption
- **Data silos** — "Authorization details live separately in intake forms, spreadsheets, and billing systems"
- **Underutilization** — approved visits going unused, i.e. lost revenue on the other side of the ledger

CareVoyant claims hard-stop validation ("If a caregiver tries to schedule beyond the approved limit or outside the authorization date range, the system flags it instantly"), configurable expiration alerts at 15–30 day lead times, and tracking of underutilized authorized hours. These are vendor claims, not verified functionality — but the fact that a vendor is marketing *against* the incumbents on precisely these points, and that Axxess's own documentation confirms a soft warning rather than a block, corroborates the gap.

### 9.9 Cross-vendor summary

| Capability | Documented state across major home health EMRs |
|---|---|
| Authorization record with payer, dates, units, disciplines | Yes, at least in Axxess. Structure elsewhere not publicly documented. |
| Authorization type modeling (date-only / units-only / both) | Documented only in Axxess. |
| Automatic decrement on schedule or completion | **No authoritative public source** for any major vendor. Axxess documents manual attachment of visits to authorizations. |
| Warning on scheduling beyond authorization | Yes in Axxess — **soft warning, does not block.** |
| Hard block on scheduling beyond authorization | Claimed by CareVoyant. **Not documented in any major vendor's published material.** |
| Expiration / renewal lead-time alerting | Claimed by CareVoyant (15–30 days configurable). Not documented for majors. |
| Shared/pooled discipline counters | **No authoritative public source** for any vendor. Axxess's model attaches disciplines to an authorization, which is compatible with pooling, but pooling behavior is not documented. |
| Eligibility 270/271 | Documented for MatrixCare. Referenced for WellSky. |
| Authorization 278 submission | **No authoritative public source** for any home health EMR. |
| Outsourced authorization service offered by the vendor | Yes — HCHB. |

**The load-bearing conclusion for a capacity-and-scheduling platform:** the authorization data model in existing home health EMRs is a *record*, and the scheduling engine treats it as *advisory*. Nothing in the published documentation of the major vendors models an authorization as a consumable resource that scheduling must reserve against. That is the gap.

---

## 10. Data fields an authorization rules library must hold to drive scheduling safely

The following is the minimum field set implied by the published payer behavior documented above. Each field is justified by a specific finding.

### 10.1 Payer identity and routing

| Field | Type | Why | Evidence |
|---|---|---|---|
| `payer_id`, `plan_id`, `product_line` | enum | Rules differ between products of one payer. | Option Care guide: Aetna commercial requires no HH auth; third-party Aetna (Meritain) requires all. |
| `delegated_manager` | enum: none / Optum / Home&Community / Carelon / EviCore / Coastal Care / other | Determines the entire ruleset, not a detail of it. | Option Care guide pp. 4–7; WellCare form: "PT, OT and other home health services may be delegated to EviCore or Coastal Care." |
| `delegation_routing_key` | rule (member-ID prefix list, state, plan code) | Delegation is sometimes keyed to a member-ID substring. | Anthem MA Ohio routes to Carelon only for prefixes JRI, JRG, VOC, VOD, ZVR, AFH; Indiana K2Y, VOK, WSP, XPF, XPG, XPK, YVK. |
| `submission_channels` | set: 278 / portal / fax / phone, with URL, fax number, ordered by preference | Fallback channels are the norm, not the exception. | Carelon portal + fax forms; Option Care fax fallback; WellCare 13 state-specific fax lines. |
| `state_scope` | set of states | Same payer, different rules by state. | UHC April 2025 change applies to 41 states + DC with FL/TN D-SNP carve-outs. |

### 10.2 Authorization requirement

| Field | Type | Why |
|---|---|---|
| `auth_required_by_discipline` | map: discipline → bool | Aetna commercial: no auth for SN/PT/OT/ST/MSW/HHA but auth required for PDN and IV nursing. |
| `disciplines_excluded_from_initial_request` | set | ST, MSW, HHA excluded from initial requests by several payers — can only be added at reauthorization. |
| `diagnosis_drives_initial_allowance` | bool + lookup table | Cigna HealthSpring bundles initial visit counts by diagnosis category. |
| `billing_pairing_rules` | set of constraints | "All claims for HHA must include the SN or PT on the same claim" — an aide visit cannot be scheduled as the only visit on a date. |

### 10.3 The provisional / start-of-care window — the field set that makes care schedulable

| Field | Type | Why |
|---|---|---|
| `provisional_allowance_type` | enum: none / eval_visit_only / n_visits / n_days / first_cert_period_partial | The three-way distinction in §2.1. Only a payer-granted allowance is schedulable. |
| `provisional_allowance_value` | int | Optum 14 days; Home & Community 30 days; Highmark HRT 1 eval visit. |
| `provisional_allowance_unit` | enum: visits / days / calendar days from SOC | Units are not interchangeable. |
| `provisional_visits_retro_payable` | enum: yes_on_approval / only_if_request_within_backdate_window / no / unknown | The §2.3 question. `unknown` must be a legal value — most payers do not publish it. |
| `notification_deadline_from_soc` | duration | Optum: SOC reported within 72 hours. Home & Community: referral within 5 days. Jefferson: fax within 5 business days of initial visit. |
| `advance_notice_required_before_soc` | duration + penalty target | UMR: 48 hours advance notice, "may impose a financial penalty on **the patient**." Penalty target must be a field. |
| `backdate_window` | duration, or `none` | Anthem OH 2 days; Anthem out-of-state 0–5 days; Carelon 5 business days; Optum none after day 14; Montana none; The Health Plan none. |
| `backdate_window_business_days` | bool | Carelon's window is business days; others are calendar. |
| `retro_auth_accepted` | bool + window | Distinct from backdating. The Health Plan: "will not provide a retro authorization." |

### 10.4 Authorization contents and counters

| Field | Type | Why |
|---|---|---|
| `authorization_number` | string | Required for billing; amendments reuse it, reauthorizations mint a new one (Montana). |
| `auth_scope_type` | enum: date_range_and_units / date_range_only / units_only | Axxess models exactly these three; the distinction is real. |
| `effective_date`, `expiration_date` | date | — |
| `counter_model` | enum: per_discipline / shared_pool / shared_pool_with_subcaps | Montana = shared pool; Cigna HealthSpring = per discipline; many commercial = pool with an aide sub-cap. |
| `pool_members` | set of disciplines | Which disciplines draw on the shared counter. |
| `subcaps` | map: discipline → int | Per-discipline ceilings inside a shared pool. |
| `authorized_units` | int, per counter | — |
| `unit_semantics` | enum: visit / hour / day / unit + conversion rule | CA § 1374.10: "A visit of four hours or less by a home health aide shall be considered as one home health visit." Conversion rules are published and payer-specific. |
| `frequency_pattern` | structured (n per m period for k duration) | The 278 HSD segment carries this natively (`HSD*VS*1*DA*3*7*21`). An authorization can constrain *cadence*, not just total. |
| `units_consumed_on` | enum: scheduled / completed / billed | Determines when the counter decrements. No vendor documents this; it must be an explicit decision. |
| `units_released_on_cancellation` | bool | A cancelled visit that already decremented is silent revenue loss. |
| `unused_units_survive_hospitalization` | bool | Optum: yes within the cert period. Others may require a new auth on resumption of care. |

### 10.5 Benefit-window anchoring

| Field | Type | Why |
|---|---|---|
| `benefit_window_anchor` | enum: start_of_care / facility_discharge_date / calendar_year / plan_year / first_service_visit | The §4 finding. Montana anchors to first service visit; CA § 1374.10 anchors to end of inpatient confinement. |
| `commencement_deadline_from_anchor` | duration | CA: care must commence within 14 days after hospital confinement ends. |
| `plan_of_care_deadline_from_anchor` | duration | CA: treatment plan established and approved by a physician within 14 days after confinement ends — a *second* clock on the same anchor. |
| `window_length` | duration | Montana: 365 days from initial service visit. |
| `days_elapsed_since_anchor` | computed, at referral intake | Must be computed in the referral queue, not at admission. |

### 10.6 Reauthorization gates

| Field | Type | Why |
|---|---|---|
| `reauth_gate_types` | set: completion / documentation / calendar | Multiple gates can apply; the binding one is whichever fires first. |
| `completion_gate_threshold` | int remaining units, or % consumed | Montana: submit no later than 14 business days before the 180-visit limit is reached — expressed in *projected burn rate*, so the trigger requires a forecast. |
| `completion_gate_expressed_as` | enum: remaining_units / percent_consumed / lead_time_at_current_rate | Montana's is the third form and is the hardest to implement. |
| `calendar_gate_window_open`, `calendar_gate_window_close` | day offsets within the period | Optum: days 40–50. Home & Community: days 56–60. **Early submission is disallowed by some payers**, so this is a window, not a due date. |
| `authorization_period_length` | duration | Carelon standardized 30 days (eff. 5/16/2025); Optum 60-day cert increments; Montana extended services ≤60 days. |
| `period_aligns_to_certification_period` | bool | Option Care: Anthem, third-party Aetna, Frontpath, OSU, OH PPO Connect request by **date range, not certification period**. Reauth cadence and clinical cert cadence are independent. |
| `extended_auth_span_runs_from` | enum: exhaustion_date / request_date | Montana: 60 days **from the date of the Extended Service request** — a late request yields a shorter authorization. |
| `amendment_vs_reauth_boundary` | rule | Amendments extend an existing counter under the same auth number; reauthorizations mint a new number. Different lead times, different packets. |

### 10.7 Documentation packet requirements

| Field | Type | Why |
|---|---|---|
| `initial_packet_items` | set | Orders, discharge summary if facility-sourced, updated clinical/H&P. |
| `reauth_packet_items` | set | 485/POC, OASIS, discipline evaluations, visit logs, wound notes, physician orders not on 485, "last two visit notes for each discipline involved." |
| `visit_note_lookback` | duration or count, per service type | Option Care: PDN 7–14 days of notes; all other services 3–5 days. |
| `visit_logs_required` | bool | Home & Community compares submitted visit logs against home care orders. |
| `poc_recertification_max_span` | duration | Montana: "Physician certifications may cover a period of less than but not greater than 60 days." |
| `incomplete_packet_restarts_review_clock` | bool | **The highest-leverage field in this table.** BCBS: "the 14 days can start over again when the additional clinicals are uploaded." An incomplete submission is worse than a late complete one. |
| `payer_outreach_attempts_before_denial` | int | Carelon: "Per CMS guidelines Carelon will make two outreach attempts for additional information." |

### 10.8 Turnaround and SLA

| Field | Type | Why |
|---|---|---|
| `sla_standard`, `sla_expedited` | duration | CMS-0057-F: 7 calendar days / 72 hours from Jan 1, 2026, for MA, Medicaid FFS & MCO, FFE QHPs. State rules can be tighter (FL SMMC 5 calendar days). |
| `observed_turnaround_range` | min/max duration, per payer | Anthem OH 3–5 days; Anthem out-of-state 7–14; BCBS up to 14; UMR 4–14. A range, not a point. |
| `expedited_criteria` and `expedited_channel` | text + contact | WellCare: expedited requires a phone call to a specific number, not the fax form. |

### 10.9 Denial and appeal

| Field | Type | Why |
|---|---|---|
| `denial_reason_code` and `denial_reason_text` | structured | CMS-0057-F requires a specific reason from Jan 1, 2026 — newly available structured signal. |
| `appeal_window`, `appeal_channel`, `peer_to_peer_available` | duration, enum, bool | — |
| `historical_overturn_rate` | %, per payer | 60–93% by MA insurer in 2025. Drives whether an appeal is worth staffing. |
| `service_continuation_after_denial` | duration | Jefferson: "services will only be reimbursable for 48 hours after… the provider [is instructed] that further services are denied." A hard scheduling stop. |
| `nomnc_required` and `nomnc_routing` | bool + rule | Jefferson requires a signed NOMNC with the initial evaluation fax; Optum routes NOMNC responses directly to the agency, not the network. |

### 10.10 The orthogonal clinical gate

| Field | Type | Why |
|---|---|---|
| `f2f_encounter_window` | duration before / after SOC | Independent of payer authorization. |
| `verbal_order_grace_period` | duration | Jefferson: "VALID verbal signature in 5 days." |
| `signed_poc_deadline` and `poc_renewal_cadence` | duration | Jefferson: "Subsequent signed POC required every 60 days." |
| `noa_deadline` | duration | Jefferson: NOA within 5 days of SOC or "services prior to receiving the NOA would not be reimbursable." |

**A visit is safely schedulable only when both the payer gate and the clinical gate are open.** Modeling one without the other produces a schedule that looks compliant and does not pay.

---

## 11. Where no authoritative public source exists

Stated plainly, so these are not silently filled with plausible numbers:

1. **Home-health-specific prior authorization denial rates.** CMS does not collect prior authorization data by service type; KFF's post-acute analysis does not break out home health.
2. **Home-health-specific authorization turnaround times, measured.** Only payer-stated ranges and qualitative interview data exist.
3. **Top denial reasons for home health authorizations, ranked and quantified.** Only general-medical claim-denial surveys.
4. **Authorization staffing ratios in home health** — coordinators per referral, per census, or per branch. Nothing published. The single quantification located is one operator's "increases my overhead admin by 25%" in a qualitative study.
5. **The rate at which visits delivered under a pending authorization are ultimately paid.** No payer or trade body publishes it.
6. **A payer publishing a percentage-of-visits-consumed reauthorization threshold in home health.** Percentage triggers appear in EMR configuration and agency policy, not in payer manuals.
7. **Whether any major home health EMR automatically decrements authorized visit counts**, and on what event (schedule, completion, or billing). Not documented by HCHB, WellSky, MatrixCare, or Netsmart. Axxess documents manual attachment.
8. **Whether any major home health EMR models shared discipline pools.** Not documented by any vendor.
9. **X12 278 submission support in any home health EMR.** Not documented by any vendor reviewed.
10. **Commure home-health authorization functionality.** Orchestrator is a referral-intake product; prior authorization appears only as an unelaborated capability under Care Navigation.

---

## 12. Source list

**Peer-reviewed**
- Thomas KS, Daus M, Jones C, Bunker JN, Smith JM, Marr J, Gadbois EA. "Prior authorization and utilization management for post-acute home health in Medicare Advantage." *Health Affairs Scholar*, Vol 3, Issue 3, March 2025. https://academic.oup.com/healthaffairsscholar/article/3/3/qxaf020/7997917

**Government / oversight**
- HHS OIG. *Some Medicare Advantage Organization Denials of Prior Authorization Requests Raise Concerns About Beneficiary Access to Medically Necessary Care.* OEI-09-18-00260, April 2022. https://oig.hhs.gov/oei/reports/OEI-09-18-00260.pdf
- CMS. Interoperability and Prior Authorization Final Rule (CMS-0057-F) fact sheet, January 2024. https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f *(HTTP 403 to automated retrieval 2026-08-18; compliance dates verified via CAQH)*
- CMS. Medicare Benefit Policy Manual, Chapter 7 — Home Health Services. https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/bp102c07.pdf *(HTTP 403 to automated retrieval 2026-08-18)*
- Montana DPHHS, Senior & Long Term Care Division. Home Health Policy 410, "Prior Authorization Process: Initial and Extended Prior Authorizations," issued April 1, 2019. https://dphhs.mt.gov/assets/sltc/HomeHealth/Section400/HH410PrAuth.pdf
- California Health & Safety Code § 1374.10. https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1374.10&lawCode=HSC
- NC Medicaid. Updates to Clinical Coverage Policy 10A, July 1, 2024. https://medicaid.ncdhhs.gov/blog/2024/07/01/updates-clinical-coverage-policy-10a-outpatient-specialized-therapies
- Vermont DVHA. PT/OT/ST Supplement. https://dvha.vermont.gov/sites/dvha/files/documents/providers/Forms/PT_OT_STSupplement.pdf

**Payer and network primary sources**
- Option Care Health / CSI. Authorization Guide, Ohio, rev. 8/2024. https://optioncarehealth.com/wp-content/uploads/Authorization-Guide.-Ohio-rev8.2024.pdf
- Jefferson Health Plans. "Medicare Home Care Utilization Review Process," October 14, 2024. https://www.jeffersonhealthplans.com/providers/provider-news/medicare-home-care-utilization-review-process/
- UnitedHealthcare. "Home health prior authorization review process no longer required," March 1, 2025. https://www.uhcprovider.com/en/resource-library/news/2025/home-health-prior-auth-changing.html
- UnitedHealthcare West. Benefit Interpretation Policy BIP075.O, "Home Health Care," effective October 1, 2025. https://www.uhcprovider.com/content/dam/provider/docs/public/policies/signaturevalue-bip/home-health-care-ca.pdf
- Cigna / HealthSpring. Home Health Care Authorization. https://www.healthspring.com/providers/home-health-authorization
- WellCare. Home Health Authorization Request Form, form 5715951_NA6PCARFRME, internally approved February 3, 2026. https://www.wellcare.com/-/media/pdfs/na/provider/forms/auth/na_care_prov_home_health_auth_request_form_2026_r.ashx
- Carelon Post Acute Solutions. Home Health Program (Anthem provider resources). https://providers.carelonmedicalbenefitsmanagement.com/postacute/provider-materials/anthem-provider-resources/home-health/
- Sunshine Health. Prior Authorization. https://www.sunshinehealth.com/members/medicaid/resources/Prior-Authorization.html
- Humana. Authorization Submission Information for Healthcare Providers. https://provider.humana.com/coverage-claims/prior-authorizations

**Industry data**
- CAQH. 2024 CAQH Index Report. https://www.caqh.org/hubfs/Index/2024%20Index%20Report/CAQH_IndexReport_2024_FINAL.pdf
- CAQH. 2023 CAQH Index Report. https://caqh.org/hubfs/43908627/drupal/2024-01/2023_CAQH_Index_Report.pdf
- AJMC. "CAQH Index Finds $20 Billion in Cost Savings Opportunities" (2025 Index coverage). https://www.ajmc.com/view/caqh-index-finds-20-billion-in-cost-savings-opportunities
- CAQH CORE. Priority Topics. https://www.caqh.org/core/priority-topics
- AMA. 2025 AMA prior authorization physician survey. https://www.ama-assn.org/system/files/prior-authorization-survey.pdf
- KFF. "Medicare Advantage Insurers Made Nearly 53 Million Prior Authorization Determinations in 2024," January 28, 2026. https://www.kff.org/medicare/medicare-advantage-insurers-made-nearly-53-million-prior-authorization-determinations-in-2024/
- KFF. "Prior Authorization Metrics Provide New Insights into Insurer Practices, but Gaps Remain," August 13, 2026. https://www.kff.org/patient-consumer-protections/prior-authorization-metrics-provide-new-insights-into-insurer-practices-but-gaps-remain/
- KFF. "Medicare Advantage Insurers Deny Prior Authorization Requests for Post Acute Care at Substantially Higher Rates Than the Overall Denial Rate," July 6, 2026. https://www.kff.org/medicare/medicare-advantage-insurers-deny-prior-authorization-requests-for-post-acute-care-at-substantially-higher-rates-than-the-overall-denial-rate/
- Experian Health. State of Claims Report 2025. https://www.experian.com/blogs/healthcare/healthcare-claim-denials-statistics-state-of-claims-report/

**Transaction standards**
- X12. Example 1b: Response to the Request for Review (005010X217). https://x12.org/examples/005010x217/example-1b-response-request-review
- Stedi. X12 HIPAA 278 Health Care Services Review — Response (X217). https://www.stedi.com/edi/hipaa/transaction-set/278-A3
- Stedi. X12 HIPAA 278 Health Care Services Review — Review (X217). https://www.stedi.com/edi/hipaa/transaction-set/278-A1
- Availity. Prior authorizations for providers. https://www.availity.com/authorizations/

**Vendor documentation**
- Axxess. Insurance Authorization (AgencyCore help). https://www.axxess.com/help/agencycore/intakescheduling/insurance-authorization/
- Axxess. Room and Board Authorization Tracking (Hospice). https://www.axxess.com/help/axxesshospice/software-updates/room-and-board-authorization-tracking/
- Homecare Homebase. Streamlined Authorizations. https://hchb.com/functionality/streamlined-authorizations/
- Homecare Homebase. Services (Revenue Cycle & Authorizations). https://hchb.com/hchb-services/
- MatrixCare. Home Health Software. https://www.matrixcare.com/home-health-software/
- Netsmart. Home Care and Hospice. https://www.ntst.com/solutions-and-services/care-settings/home-care-and-hospice
- WellSky. Home Health Software. https://wellsky.com/home-health-software/ *(HTTP 403 to automated retrieval 2026-08-18)*
- Commure. https://commure.com/
- CareVoyant. "Hidden Costs of Authorization Mismanagement in Home Care," December 23, 2025 *(vendor content)*. https://www.carevoyant.com/home-health-blog/authorization-mismanagement-home-care
