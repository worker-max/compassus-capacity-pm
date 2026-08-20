# Commercial Insurance and Medicaid Payment for Skilled Home Health

Research file for the CCSI branch capacity-and-scheduling platform.
Compiled 2026-08-18. All sources fetched or search-verified on that date unless noted.

## How to read this file

Every factual claim is followed by an inline source URL and the publication or revision
date of the source document. Three labels are used throughout:

- **[PUBLISHED]** — the claim is stated in a document I fetched and read. The quote or
  number is in that document.
- **[SEARCH-VERIFIED]** — the claim appeared in a search-engine summary of a named page
  that I could not fetch directly (usually because the payer's site blocks automated
  fetching). The URL is real; the detail should be re-confirmed by a human before it is
  relied on operationally.
- **[PATTERN]** — general industry practice. Not attributable to a single published
  document. Treat as a working assumption to be validated per contract.
- **[UNVERIFIED]** — a specific claim that could not be confirmed against a primary source
  in this research pass, either because the source blocks automated fetching or because the
  information is not published. **Do not put an [UNVERIFIED] item into a product spec
  without closing it first** — see the open-questions table in §8.2.

**Staleness flags.** Any figure marked ⚠️ **STALE-RISK** is a fee-schedule number, a
visit cap, or an authorization interval tied to a specific payer, state, and plan year.
These change annually — some mid-year. Do not hardcode them. Re-pull before any release.


## Contents

| Part | Subject |
|---|---|
| **1** | Blue Cross Blue Shield and skilled home health — the federation pattern, six concrete licensees, published FEP visit caps, the CY2026 Medicare per-visit benchmark |
| **2** | BlueCard — host plan vs home plan, and why out-of-area auth rules cannot be pre-computed |
| **3** | Self-funded ERISA plans — the deemer clause, the 67% number, real employer visit caps, federal appeal timeframes |
| **4** | Cigna, Aetna commercial, UnitedHealthcare commercial — auth posture and payment model |
| **5** | Medicaid — 42 CFR 440.70 vs 440.180, Indiana, Ohio, Texas, Michigan, Florida, and the HCBS-waiver distinction |
| **6** | Medicaid MCO authorization mechanics — the 2026 federal turnaround change, retro authorization, transition of care |
| **7** | Dual eligibles — FIDE / HIDE / coordination-only, QMB, EVV asymmetry, the discharge cliff |
| **8** | Staleness register and open questions |
| **9** | What this means for a branch capacity-and-scheduling platform |

### The five load-bearing conclusions

1. **Commercial home health is per-visit against an annual cap; Medicare Advantage home
   health is episodic against 30-day authorization periods.** Verified in UHC reimbursement
   policy 2026R5036A, the 2026 FEP brochures, Aetna CPB 0201, and BCBSNC's move to 30-day MA
   intervals. Modeling commercial against PDGM is modeling the wrong object.
2. **An authorization is a per-discipline quantity inside a dated window, not a number** —
   and there are at least six different rules for what date the window starts from.
3. **The member ID card does not tell you the rules.** Not for self-funding (67% of covered
   workers), not for BlueCard, not for which vendor holds the case, not for dual integration
   tier, not for whether a dual even has a Medicaid aide benefit.
4. **Medicare Advantage home health is being delegated to vendors that take the network, the
   authorization *and* the claim** — tango for BCBSM, Carelon for Anthem and Aetna, eviCore
   for Cigna and parts of Aetna. The payer ID on the claim is not the payer on the card.
5. **Medicaid state plan home health and HCBS waiver services are two different benefits on
   the same patient, with different authorizers, different clocks, and — in Ohio — a
   legislated two-hour separation between them.** They cannot share one authorization model.

---

# Part 1 — Blue Cross Blue Shield and skilled home health

## 1.1 Why "BCBS" is not one payer

The Blue Cross Blue Shield Association is a federation of independent, locally operated
licensees. **[PUBLISHED]** BCBSA describes itself as "independent, community-based and
locally operated Blue Cross and Blue Shield (BCBS) health insurance companies"
(https://www.bcbs.com/about-us, accessed 2026-08-18) — it does not publish a count on that
page, and the count changes with mergers, so do not hardcode one. Several licensees are
holding companies operating multiple state licenses: **HCSC** (Illinois, Texas, Oklahoma,
New Mexico, Montana), **Elevance Health** (formerly Anthem, multiple states), **Highmark**
(Pennsylvania, Delaware, West Virginia, New York). Each of the examples below is a
separate licensee with separately published rules.

The operational consequence for a scheduling platform: **there is no such thing as "the
BCBS home health rule."** Authorization posture, the entity that performs the review, the
submission channel, the authorization interval, and the payment model all vary by
licensee, by product line within a licensee, and by funding arrangement within a product
line. The examples below show four licensees whose home health rules are materially
different from one another as of mid-2026.

## 1.2 The recurring structural pattern

Across every Blue licensee examined, the same four-axis split shows up:

| Axis | Typical split |
|---|---|
| Product line | Commercial (fully insured), Commercial (ASO/self-funded), Medicare Advantage, Medicaid managed care, Federal Employee Program |
| Who reviews | Plan's own UM department, or a delegated post-acute vendor (Carelon, tango, CareCentrix, eviCore) |
| Payment model | Per-visit fee-for-service on the commercial side; episodic / PDGM-aligned 30-day periods on the Medicare Advantage side |
| Auth interval | Commercial: often none, but a hard annual visit cap. MA: 30-day authorization periods, converging on PDGM |

**[PATTERN]** The single most reliable generalization: **commercial Blue plans pay skilled
home health per visit and control utilization with an annual visit maximum; Medicare
Advantage Blue plans pay episodically and control utilization with prior authorization on
30-day periods.** The FEP, BCBSNC and BCBSM evidence below all point the same way.

The second most reliable generalization: **Medicare Advantage home health is being handed
to delegated vendors, and those vendors are taking the network, the authorization, and the
claim.** BCBSM's move to tango and Anthem's use of Carelon Post Acute Solutions are the
same play. For a scheduling platform this matters more than the clinical criteria: it
changes which portal the branch logs into, which payer ID the claim carries, and who the
branch calls when an auth stalls.

---

## 1.3 Concrete example 1 — Blue Cross Blue Shield of Michigan

**[PUBLISHED]** BCBSM's consolidated prior authorization document, *Prior authorization
requirements for Michigan and non-Michigan providers, For Blue Cross commercial and
Medicare Plus Blue*, **Revised June 2026**:
https://www.bcbsm.com/amslibs/content/dam/public/providers/documents/preauthorization-precertification-requirements.pdf

Two findings, and the contrast between them is the point:

**Commercial (non-Medicare).** Home health care does **not** appear as a prior-authorization
requirement for Blue Cross commercial products. The document's "Home health care" section
lists **Medicare Plus Blue only**. What *does* require prior authorization on the commercial
side is **private duty nursing**, for dates of service on or after Oct. 1, 2022, submitted
through the **e-referral** system, billed as **S9123 (RN) or S9124 (LPN)** with **total hours
as units, 1 unit = 1 hour**.

**Medicare Plus Blue (and BCN Advantage).** Home health is delegated to **tango**:

> "Blue Cross contracts with tango, an independent company, to manage the network of home
> health care providers, coordinate referrals, manage prior authorizations and process
> claims."

- Episodes of care starting **on or after March 1, 2026** — prior authorization required
  through tango.
- Episodes starting **before March 1, 2026 that continue through or beyond March 1, 2026**
  — prior authorization also required. ⚠️ **STALE-RISK** (transition rule, 2026-specific).
- Episodes that start **and end** before March 1, 2026 — no prior authorization.

**[PUBLISHED]** *Home health care provider network management — Frequently asked questions,
For Medicare Plus Blue and BCN Advantage*, **February 2026**:
https://www.bcbsm.com/amslibs/content/dam/public/providers/documents/home-health-care-provider-network-faq.pdf

- **Starting March 2, 2026, tango manages the home health provider network.** Michigan
  agencies "must contract with tango to provide services to those members as in-network
  providers."
- **Claims go to tango, not to Blue Cross.** "For episodes of care that start on or after
  March 1, 2026, home health care providers must bill tango for home health services."
- But there is a **claims split** that a scheduling/billing system has to model: agencies
  "should continue to bill Blue Cross or BCN for durable medical equipment and supplies
  provided in conjunction with skilled home health visits, home infusion therapy and
  stand-alone wound care." One visit can therefore generate two claims to two payers.
- Tango's portal is **ProNet Connect**; claims visibility inside the portal was targeted
  for release **early April 2026**; claims inquiries route through **FreshDesk** inside
  ProNet Connect. Claims email: claims@tangocare.com.
- **Out-of-state carve-out:** "Medicare Advantage members who receive services outside of
  Michigan" do not need a tango-contracted agency. Neither do Blue Cross commercial or BCN
  commercial members.
- **Tango calls the member after the first visit.** "Tango reaches out to members following
  the first home health agency visit to confirm the start of care, assess service quality
  and identify emerging needs or changes in condition." A scheduling platform should expect
  the first visit to be a verification event, not just a service event.

**[PUBLISHED]** *Medicare Plus Blue PPO Provider Manual*, **revised July 1, 2026**:
https://www.bcbsm.com/amslibs/content/dam/public/providers/documents/medicare-plus-blue-ppo-manual.pdf

- "Tango will authorize and coordinate clinical services in the home such as skilled
  nursing and physical, occupational and speech therapies." (p. 73–74)
- Home health agencies must issue the **NOMNC (CMS-10123)** on termination of services, and
  "failure to deliver a valid NOMNC may result in the provider being held financially
  liable for the continued services until two days after the member receives a valid
  notice." (p. 75) This is a hard scheduling dependency: the last-visit date and the NOMNC
  delivery date are coupled.

**Submission channel:** tango's ProNet Connect for MA home health; BCBSM's **e-referral**
for commercial private duty nursing; **Availity** payer spaces for eviCore-managed services.

**Published per-visit rates:** none. BCBSM does not publish home health rates; they are
contract terms.

---

## 1.4 Concrete example 2 — Anthem / Elevance Health (via Carelon Post Acute Solutions)

**[PUBLISHED]** Carelon Post Acute Solutions, *Anthem provider resources — Home Health*:
https://providers.carelonmedicalbenefitsmanagement.com/postacute/provider-materials/anthem-provider-resources/home-health/

- **Prior authorization is required** for in-scope Anthem plans. Scope is defined by a
  published plan grid spreadsheet (by state), not by a simple rule:
  https://providers.carelonmedicalbenefitsmanagement.com/postacute/wp-content/uploads/sites/52/2023/04/0626_HH_Anthem-Plan-Grid-062626.xlsx
  ⚠️ **STALE-RISK** — the grid filename carries a date stamp and is re-issued periodically.
- **Standardized 30-day review period.** "On May 16, 2025, Carelon will introduce a
  standardized 30-day review period for all home health authorizations." This is the single
  most schedule-relevant fact in the Anthem stack: **every 30 days the branch must produce a
  reauthorization packet**, regardless of the clinical episode length.
- **Submission channel:** the provider portal at **https://portalct.mynexuscare.com**
  (Carelon acquired myNEXUS; the myNEXUS portal hostname persists). Fax forms exist for
  initial and re-authorization. Phone **844-411-9622**.
- **Claims go to Carelon, not Anthem.** Carelon payer ID **34009**; claims phone
  **833-241-0428**.
- **Criteria:** "Carelon utilizes CMS National and Local Coverage Determinations (NCD and
  LCDs) when applicable, or Anthem medical policies and clinical Utilization Management
  guidelines." **[SEARCH-VERIFIED]** IV skilled nursing reviews additionally weigh
  "caregiver's ability/willingness" —
  https://providers.carelonmedicalbenefitsmanagement.com/postacute/provider-materials/anthem-provider-resources/home-health/

**[PUBLISHED] The Carelon home health authorization forms are the most operationally
specific commercial home health documents found in this entire research pass.** Both are
© 2025 Carelon Medical Benefits Management.

*Home Health Care Initial Authorization Form* (fax 844-834-2908; questions 833-585-6262):
https://providers.carelonmedicalbenefitsmanagement.com/postacute/wp-content/uploads/sites/52/2023/04/1125-carelon-HH-reauth-request-form-Anthem-011426.pdf

- The request is structured as **"Review Period A (first 30 Days): Requested Number of
  Visits"** with a **separate visit count and date-of-first-visit per discipline** —
  Skilled Nursing, Physical Therapy, Occupational Therapy, Speech Therapy, Home Health
  Aide, Medical Social Work. **The authorization is a per-discipline visit budget inside a
  30-day window.** A scheduling engine must model auth as a 6-row vector, not a scalar.
- Requester must assert **homebound status (Y/N)** and **"Able/Willing/Teachable Caregiver
  (Y/N)"** — with a free-text explanation if No. Caregiver availability is an explicit
  authorization input.
- Also required: **HIPPS code**, start of care date, date of discharge from facility or
  office visit, referral source (Hospital / MD Office / SNF-Rehab), and a **Primary Subtype**
  picked from a fixed clinical list (B-12, UTI, CHF, COPD, CVA, Sepsis, Ostomy, General,
  Diabetes, Heart Surgery, Wound Care, Wound Vac, Neuromuscular Maintenance, Neuromuscular
  Restorative, Total Hip Replacement, Total Knee Replacement, Chemotherapy, Foley Catheter).
- **At least one** of: H&P, inpatient discharge summary, notes from hospital or SNF, MD
  office notes, or wound care notes with measurements.
- Three request types are on the form: **Standard, Retro, Urgent.** Retroactive requests are
  a first-class supported path. Expedited/urgent determinations "can only be requested by
  the Member, Member Representative, or a Physician" per CMS 40.8 — **an agency cannot
  self-declare urgency.**

*Home Health Care Re-Authorization Form* (fax 844-834-2908; questions 844-411-9622):
https://providers.carelonmedicalbenefitsmanagement.com/postacute/wp-content/uploads/sites/52/2023/04/0525-carelon-HH-reauth-request-form-Anthem-051325.pdf

- Carries a **Certification Period (From / To)** *and* a **"30-Day Review Period (make
  selection): A or B."** So a 60-day certification period is administratively split into
  two 30-day review periods. **The clinical cert period and the authorization period are
  different objects with different dates** — a scheduling platform must store both.
- Per discipline it captures **date of last visit, number of visits requested, and plan of
  care frequency.**
- Also captures **residence type** (private residence / assisted living / independent
  living / long term care / other) — which can affect coverage.
- **Required reauthorization checklist, verbatim:**
  1. Verbal or signed order (including frequency and duration to cover requested visits) if
     a new skill is being requested OR if not submitted with initial request.
  2. Completed signed **SOC OASIS** for first reauthorization request.
  3. Updated clinical documentation (**completed ROC OASIS, signed 485/POC**) for all
     services being requested, along with all visit notes; ensure the evaluation is being
     or has been submitted.
  4. Wound measurements from previous visits, if applicable.

- **[PUBLISHED]** Carelon also administers Anthem programs for DMEPOS, DMEPOS Medicaid,
  PAC-IM, SDoH and Wound Care Connect —
  https://providers.carelonmedicalbenefitsmanagement.com/postacute/provider-materials/anthem-provider-resources/
  A single Anthem patient can therefore sit behind several Carelon programs at once, each
  with its own auth.

**Anthem state variation is real.** Anthem publishes prior-authorization requirements
per state, not federation-wide. Example landing page (Ohio):
https://providers.anthem.com/ohio-provider/resources/prior-authorization-requirements
Anthem also runs a per-state Prior Authorization Lookup Tool, e.g.
https://providers.anthem.com/new-york-provider/claims/prior-authorization-lookup-tool
**The lookup tool is the operational source of truth, not the medical policy.**

---

## 1.5 Concrete example 3 — Highmark

**[PUBLISHED]** *Highmark Provider Manual*, Chapter 5 Unit 2 — Authorizations:
https://providers.highmark.com/resources-and-education/highmark-provider-manual/chapter-5-care-and-quality-management/unit-2-authorizations.html

- **Authorization is required** for home health.
- **Submission channel is mandatory, not optional:** "Participating home health care
  providers must use the home health care authorization request submission process through
  Availity Essentials®, Highmark's provider portal." Non-Availity providers may fax the
  **Home Health Precertification Worksheet** or call Clinical Services.
- **Documentation required with the request — this is the most specific published
  documentation requirement found for any commercial plan:**
  - an **OASIS file upload**, and
  - the **CMS-485** (home health certification and plan of care).
  A scheduling platform that cannot surface the OASIS and the 485 at the point of auth
  submission will bottleneck Highmark cases.
- **Criteria:** "The MCG Care Guidelines are applied to assess acute adult, acute
  pediatric, acute rehabilitative, long-term acute, skilled nursing, and home health
  services."
- **Decision turnaround:** **15 calendar days** after receipt for non-urgent; **3 calendar
  days** for urgent.
- **Standard disclaimer, and it matters for revenue modeling:** "Authorization does not
  guarantee payment. A service or supply will be reimbursed by Highmark only if it is
  medically necessary, a covered service, and provided to an eligible member."
- The manual makes **no distinction between fully insured and self-funded groups** for home
  health authorization. That silence is itself a finding — see Part 3.

**[PUBLISHED]** Highmark's BlueCard unit (Chapter 2 Unit 6) is the cleanest published
statement of the inter-plan rules — see Part 2:
https://providers.highmark.com/resources-and-education/highmark-provider-manual/chapter-2-product-information/unit-6-the-bluecard-program.html

---

## 1.6 Concrete example 4 — Blue Cross NC

**[PUBLISHED]** Commercial medical policy, *Skilled Nursing Services*, **last reviewed
February 2026**:
https://www.bcbsnc.com/providers/policies-guidelines-codes/commercial/home-health-dme/updates/skilled-nursing-services

- "Prior review/authorization is required for skilled nursing visits."
- Homebound status is a coverage criterion on the **commercial** side, not just Medicare —
  criteria include physical assistance needs, infrequent absences for medical treatment, or
  active cancer treatment.
- **Documentation required:** "medical diagnosis, proposed frequency of services, proposed
  duration of services, documentation of the patient's home bound status, and a social
  assessment." The **social assessment** requirement is unusual and easy to miss.
- **Published service-specific caps** ⚠️ **STALE-RISK** (policy reviewed Feb 2026):
  rehabilitation nursing limited to **5 visits** in the home; medical gas administration
  limited to **5 visits** in the home; postoperative colostomy care limited to **14 days**
  post-surgery.
- Not covered: family-provided care, custodial services, services "primarily for the
  comfort or convenience of the member or their family."

**[PUBLISHED]** Provider news, *Change in prior authorization requirements for PPS Home
Health providers* (2026):
https://www.bcbsnc.com/providers/provider-news/2026/change-in-prior-authorization-requirements-for-pps-home-health-p

- **"Prior authorizations will now be issued in 30-day intervals,"** replacing the previous
  60-day episode structure, to align with CMS's **PDGM** payment methodology.
- **Effective May 1, 2026** (originally announced for April 2, 2026 — the date moved).
  ⚠️ **STALE-RISK.**
- Applies **only** to episodic PPS home health providers serving **Medicare Advantage**
  plans. **Commercial, Inter-Plan Program (BlueCard), and Federal Employee Program plans
  are unaffected.**

This is the cleanest single illustration of the whole problem: **inside one Blue licensee,
in one calendar year, the same agency serving the same clinical case has a 30-day
authorization cycle for MA members, a per-visit prior-authorized commercial benefit for
local members, and a third set of rules for BlueCard members** — and each has a different
renewal cadence the scheduler must track.

Related BCBSNC pages:
- Private Duty Nursing Services policy: https://www.bcbsnc.com/providers/policies-guidelines-codes/commercial/home-health-dme/updates/private-duty-nursing-services
- Prior Plan Review: https://www.bluecrossnc.com/providers/medical-policies-and-coverage/prior-plan-review
- Home Health & Nursing Services auth request tool: https://providers.bcbsnc.com/help/files/hh_input.htm

---

## 1.7 Concrete example 5 — HCSC (BCBS of Texas / Illinois / Oklahoma / New Mexico / Montana)

**[PUBLISHED]** *Prior Authorization Services For Fully Insured and ASO*:
https://www.bcbstx.com/provider/claims/claims-eligibility/um/pri-aso

- HCSC maintains **separate prior-authorization code lists** for "Fully Insured & Certain
  Administrative Services Only Groups" versus "Other ASO Groups."
- **How to tell which one applies: "look for the TDI on their member ID card."** Texas
  fully insured plans are regulated by the Texas Department of Insurance and carry a TDI
  marker. This is the rare case where the card *does* carry a funding-status signal — and
  it is state-specific, so it does not generalize.
- Standing instruction: "always check eligibility and benefits through Availity® Essentials
  or your preferred vendor."
- **Home health does not appear on this prior-authorization services page.**

**[PUBLISHED]** *How to Request Prior Authorization*:
https://www.bcbstx.com/provider/claims/claims-eligibility/um/request-auth
Submission is via the **Availity Authorizations & Referrals** tool, or to the delegated
vendor: **eviCore** (855-252-1117), **Carelon Medical Benefits Management** (800-859-5299),
**Alacura** for medical transport. The page does not address home health, home infusion, or
private duty nursing.

**[PUBLISHED]** *Prior Authorization Changes … Effective Jan. 1, 2026*:
https://www.bcbstx.com/provider/education/education/news/2025/10-01-2025-prior-authorization-changes
The Jan. 1, 2026 changes added advanced imaging, sleep and genetic testing to Carelon for
commercial, and specialty drugs plus molecular genetic lab testing to eviCore for
government programs. **No home health changes.**

**[PUBLISHED]** Operational note for 2026 ⚠️ **STALE-RISK**: BCBSTX is moving auth
decision letters to digital-only. From **July 18, 2026** approval/denial letters for
commercial members are available in Availity; from **Sept. 8, 2026** approval letters
**stop being mailed**:
https://www.bcbstx.com/provider/education/education/news/2026/6-8-2026-digital-access-to-prior-authorization-decision-letters-via-availity-essentials
A scheduling platform that relies on scanned mailed auth letters will silently lose its
input after September 2026 in Texas.

---

## 1.8 Concrete example 6 — Horizon BCBSNJ

**[SEARCH-VERIFIED]** Horizon's own page states that home health services — in-home
nursing, PT, OT and ST — require prior authorization submitted through **Horizon's online
utilization management request tool via Availity Essentials**, and that **Horizon itself**
(not CareCentrix) reviews home health:
https://www.horizonblue.com/providers/products-programs/utilization-management-programs/horizon-care-home/prior-authorization-pre-service-registration
*(horizonblue.com blocks automated fetching — Imperva. Detail above comes from the search
engine's summary of that page. Confirm with a human before relying on it.)*

**[PUBLISHED]** The division of labor is confirmed by CareCentrix's own quick reference
guide, *Horizon Supportive Care / Braven Health Supportive Care*, **June 2022**:
https://help.carecentrix.com/ProviderResources/ep/horizon/Horizon-Braven_QRG_Final.pdf
CareCentrix manages **SNF, subacute rehab, subacute rehab with ventilator, transitional
care unit and inpatient rehab** authorizations for Horizon Medicare Advantage, Braven
Health and Horizon Commercial Fully Insured members — **home health is not in that list.**

That QRG also publishes the most explicit **continuation-of-services** documentation list
found in this research. Even though it is written for facility PAC, it is the best
available model of what a concurrent-review packet looks like:

| Request type | Required |
|---|---|
| All requests | Patient name, DOB, home address, phone, member ID |
| Initial | Start of care date, ordering physician + phone, diagnosis, H&P, medication list, prior level of function, prior living situation, current cognitive status, recent physician/nursing/therapy notes |
| Continuation | Level of care requested, recent notes **including progress toward goals** (completed within 72 hours of submission), therapy treatment logs, changes in clinical status, discharge plan, IDT care plan note, anticipated discharge date, current functional status, current medication list |

> "Continuation of Services Requests should be submitted at least 72 hours prior to the
> expiration of the current authorization."

**[PATTERN]** That 72-hour lead time is the general commercial norm and is the number a
scheduling platform should default to when it does not know a payer's specific rule.

**[PUBLISHED]** Historical but structurally important — *Horizon BCBSNJ Traditional Home
Care and Private Duty Nursing Transition FAQs*:
https://help.carecentrix.com/ProviderResources/Horizon/Horizon_THH_PDN_Transition_FAQ.pdf
Effective **November 1, 2016**, Traditional Home Health (skilled nursing, home health aide,
PT/OT/ST) and PDN moved **from CareCentrix back to Horizon**. Two durable lessons:

1. **Vendor transitions split claims mid-episode.** "Claims containing any dates of service
   on or after November 1, 2016 will be rejected… claim lines must be split on separate
   claims." Any vendor cutover — BCBSM/tango in March 2026 is the current instance —
   forces a mid-episode claim split. A scheduling system needs a payer-effective-date
   concept, not just a payer field.
2. **Home infusion nursing stayed with CareCentrix** while the rest of home health moved.
   The nurse who administers an infusion drug can be authorized by a different entity than
   the nurse who does the wound care two days later, for the same patient.
3. The FAQ explicitly applies to "Horizon BCBSNJ **and ITS Host Members**" — i.e. BlueCard
   host members are pulled into the host plan's vendor arrangement for claims routing. See
   Part 2.

---

## 1.9 Published BCBS benefit limits that you can actually see — the Federal Employee Program

Commercial Blue rates and most commercial benefit maxima are contract-confidential. The
**one large Blue book of business with fully published benefit design is FEP**, because OPM
publishes the brochures. These are the most concrete, verifiable BCBS home health numbers
available, and they are an excellent proxy for how commercial Blue benefit design is
shaped.

**[PUBLISHED]** *2026 Blue Cross and Blue Shield Service Benefit Plan, Standard and Basic
Option*, brochure RI 71-005, Section 5(a) "Home Health Services", p. 59:
https://www.opm.gov/healthcare-insurance/healthcare/plan-information/plans/pdf/2026/brochures/71-005.pdf

**[PUBLISHED]** *2026 … FEP Blue Focus*, brochure RI 71-017, Section 5(a), p. 52:
https://www.opm.gov/healthcare-insurance/healthcare/plan-information/plans/pdf/2026/brochures/71-017.pdf

⚠️ **STALE-RISK — all figures are plan year 2026.**

| FEP option | Covered benefit | Annual visit cap | Member cost share (Preferred) | Non-preferred |
|---|---|---|---|---|
| Standard Option | Skilled home nursing, **2 hours per day**, RN or LPN, physician-ordered | **50 visits per person per calendar year** | 15% of Plan allowance, deductible applies | Participating and Non-participating: 35% of allowance + balance billing risk |
| Basic Option | Same | **25 visits per person per calendar year** | **$35 copayment per visit** | You pay all charges |
| FEP Blue Focus | Same, **limited to 10 visits** | **10 visits** | **$25 copayment per visit** | You pay all charges |

Four details that matter operationally:

1. **Payment is per visit.** A copayment "per visit" is unambiguous: this is not episodic.
2. **The cap is a hard accumulator and it counts pre-deductible visits.** Standard Option:
   "Visits that you pay for while meeting your calendar year deductible count toward the
   annual visit limit." A scheduler that only counts *paid* visits will overrun the cap.
3. **Home health aide and private duty nursing are excluded across all three options.**
   Not covered: "Private duty nursing"; "Services primarily for bathing, feeding,
   exercising, moving the patient, homemaking, giving medication, or acting as a companion
   or sitter"; nursing care requested for the patient's or family's convenience.
4. **No prior approval requirement for home health.** The FEP prior-approval list in
   Section 3 of RI 71-005 covers medical benefit drugs, sleep studies, ABA, genetic
   testing, hearing aids, a named surgical list, proton beam therapy, stereotactic
   radiosurgery, reproductive services, sperm/egg storage and transplants. **Home nursing
   is not on it.** FEP controls home health with a benefit cap, not with authorization.

**This is the single best worked example of the "cap, not auth" model**, and it is a real,
large, national book of business a branch will see.

---

## 1.10 The one published rate benchmark

There is no published commercial per-visit fee schedule for any Blue plan. The benchmark
the whole market is priced against is the Medicare per-visit (LUPA) rate.

**[PUBLISHED]** CY 2026 HH PPS final rule **[CMS-1828-F]**, RIN 0938-AV53, scheduled for
Federal Register publication **12/02/2025**, Table 16 "Final CY 2026 National Per-Visit
Payment Amounts":
https://public-inspection.federalregister.gov/2025-21767.pdf
Canonical: https://federalregister.gov/d/2025-21767

⚠️ **STALE-RISK — CY2026 only; these are national, pre-wage-index amounts, for HHAs that
submit required quality data.**

| Discipline | CY2025 | CY2026 |
|---|---|---|
| Skilled Nursing | $172.73 | **$176.96** |
| Physical Therapy | $188.79 | **$193.42** |
| Occupational Therapy | $190.08 | **$194.74** |
| Speech-Language Pathology | $205.22 | **$210.25** |
| Medical Social Services | $276.85 | **$283.64** |
| Home Health Aide | $78.20 | **$80.12** |

CY2026 payment update factor 1.0240 (2.4%); wage index budget neutrality factor 1.0005.
The rule also finalizes a **-1.023% permanent prospective adjustment** to the CY2026 HH
payment rate for PDGM behavior-change impacts, and updates LUPA thresholds using CY2024
claims data. Effective for discharges on or after **January 1, 2026**.

**[PATTERN]** Commercial per-visit contracts are typically negotiated as a percentage of
these rates or as flat per-visit rates in a similar band; MA episodic contracts are
typically PDGM-referenced. Treat any specific percentage as contract-specific and unknown
until the branch's contract is read.

---

# Part 2 — BlueCard: the host-plan / home-plan problem

## 2.1 The rule, stated precisely

**[PUBLISHED]** *BlueCard Program — Answers to Frequently Asked Questions*, BCBS of
Oklahoma (HCSC), "Medical, Benefit, Payment Policy" section:
https://www.bcbsok.com/docs/provider/ok/claims/tips/bluecard-faq.pdf

> "Only a member's Blue Plan Medical Policy applies to BlueCard claims. The member's Blue
> Plan Medical Policy applies to the interpretation and determination of medical necessity,
> medical appropriateness, investigational/experimental care, and clinical reviews as
> related to administration of the member's benefits and coverage."

The split of responsibilities is explicit in the same document:

| Function | Which plan |
|---|---|
| Medical policy, medical necessity, clinical review | **Home plan** (member's Blue plan) |
| Benefits, eligibility, adjudication | **Home plan** |
| Prior authorization / pre-certification decisions | **Home plan** |
| Claim pricing and reimbursement rules per provider contract | **Host plan** (local plan) |
| Single point of contact for the provider — claims payment, customer service, adjustments, appeals | **Host plan** |
| Provider network status, contracting, audit | **Host plan** |

Highmark's manual says the same from the other side:
https://providers.highmark.com/resources-and-education/highmark-provider-manual/chapter-2-product-information/unit-6-the-bluecard-program.html

## 2.2 Why this is a scheduling problem, not just a billing problem

**[PUBLISHED]** From the BCBSOK FAQ:

> "While out-of-area BlueCard members are currently responsible for obtaining prior
> authorization or pre-certification from their BCBS Plans, most providers choose to handle
> this obligation on the member's behalf. Members may be held financially responsible if
> necessary approvals are not obtained and the claim is denied. The provider may have to
> manage debt collection in this situation."

**[PUBLISHED]** BCBSTX states the financial consequence more bluntly:
https://www.bcbstx.com/provider/claims/claims-eligibility/bluecard-preauth

> "Failure to prior authorize may result in reduced payment or denial and health care
> providers cannot collect these fees from the members."

**[PUBLISHED]** Highmark: "Highmark participating providers are also required to hold
members harmless if the member's plan requires pre-service review and the provider did not
attempt to acquire an authorization."

So: the *nominal* obligation sits with the member; the *actual* financial exposure sits
with the agency; and the rules that must be followed are published by a plan the agency
has no contract with and no portal login for.

## 2.3 How you actually find the out-of-area rules

Three published mechanisms, all of them manual:

1. **The three-character alpha prefix on the member card** identifies the home plan.
   Highmark: "The prefix identifies the Blue Plan or national account to which the member
   belongs. It is critical for confirming a patient's membership and coverage."
2. **The Medical Policy and Pre-Certification/Pre-Authorization Router for Out-of-Area
   Members.** Every Blue licensee hosts one, keyed by alpha prefix. Examples:
   - Highmark: Provider Resource Center → Provider Network → Inter-Plan Programs →
     Medical Policy and Pre-Certification/Pre-Authorization Router
     (https://providers.highmark.com/provider-network/inter-plan-programs/bluecard-information-center.html)
   - BCBSTX: `/provider/standards/standards-requirements/mppc`
     (https://www.bcbstx.com/provider/claims/claims-eligibility/bluecard-preauth)
3. **1-800-676-BLUE (2583)** — the BlueCard Eligibility line. BCBSOK notes calls route to
   one of four queues: Medical/Surgical, Behavioral Health, Diagnostic Imaging/Radiology,
   Durable/Home Medical Equipment. **There is no "home health" queue** — home health
   requests land in Medical/Surgical.

**[PUBLISHED]** Eligibility should be checked by **HIPAA 270/271** through the local plan,
but the FAQ warns that generic service type codes are inadequate: "Use of the general
Service Type '30' (Health Benefit Plan Coverage) or Service Type '1' (Medical Care) may not
provide enough information… and does not include information on Benefit Limitations and
Place of Service requirements." For home health, the relevant service type codes are the
home-health-specific ones — a platform doing automated eligibility should request them
explicitly or it will not get back the visit-cap accumulator it needs.

## 2.4 The scheduling consequences, concretely

- **You cannot pre-compute BlueCard auth rules.** The rule set is a function of the alpha
  prefix, and there are dozens of home plans with materially different home health posture
  (compare BCBSM commercial: no auth; BCBSNC commercial: auth required with a social
  assessment; Highmark: auth required with OASIS + 485 upload). A branch intake workflow
  must branch on alpha prefix and route to a manual lookup.
- **Turnaround is unpredictable.** Highmark's own members get 15 calendar days non-urgent /
  3 days urgent. A BlueCard member's home plan may have different statutory timeframes,
  and for a self-funded home plan, ERISA timeframes apply instead of the host state's.
- **Vendor arrangements can still capture host members.** Horizon's THH/PDN transition FAQ
  applies to "Horizon BCBSNJ **and ITS Host Members**" —
  https://help.carecentrix.com/ProviderResources/Horizon/Horizon_THH_PDN_Transition_FAQ.pdf
  So a host-state vendor change can change where an out-of-area member's claim goes, even
  though the home plan still owns medical policy.
- **BCBSNC explicitly excludes Inter-Plan Program plans** from its 30-day MA authorization
  change — https://www.bcbsnc.com/providers/provider-news/2026/change-in-prior-authorization-requirements-for-pps-home-health-p
  So a local rule change does *not* propagate to BlueCard members. A platform that models
  "the payer" as one object will get this wrong.
- **[PATTERN]** Practical field rule: for BlueCard, assume auth is required until proven
  otherwise, submit as early as possible, and log the reference number plus the name of the
  home-plan reviewer. The host plan cannot tell you the answer and will not be liable for
  a wrong one.

---

# Part 3 — Self-funded ERISA plans

## 3.1 The core distinction

**[PATTERN, with published anchors]** In a **fully insured** plan, the carrier collects
premium, bears the claims risk, and the plan is an insurance product regulated by the
state insurance department. In a **self-funded (ASO) plan**, the employer is the plan
sponsor and bears the claims risk; the carrier is only a third-party administrator selling
administrative services. ERISA preempts state insurance regulation of self-funded plans, so
state benefit mandates, state prompt-pay statutes, state UM turnaround statutes and state
external-review programs generally **do not apply**.

**[PUBLISHED]** The clearest carrier-side confirmation that the two are administered
differently is HCSC's maintenance of **separate prior-authorization code lists** for
"Fully Insured & Certain Administrative Services Only Groups" versus "Other ASO Groups":
https://www.bcbstx.com/provider/claims/claims-eligibility/um/pri-aso

**[PUBLISHED]** BCBSM's musculoskeletal program scoping shows the same thing at group
granularity — the TurningPoint program applies to "Most fully insured groups — Excludes
MESSA members" and "Select self-funded groups — Includes UAW Retiree Medical Benefits
Trust non-Medicare members":
https://www.bcbsm.com/amslibs/content/dam/public/providers/documents/preauthorization-precertification-requirements.pdf
(Revised June 2026). **Utilization management programs are sold group by group.** Two
patients with identical BCBSM cards can be in and out of the same program.

## 3.2 Why the card does not tell you the rules

- The card shows the **administrator's** brand, not the risk-bearer. "Administered by" or
  "Administrative services provided by" language is the strongest hint, but it is not
  standardized and not always present.
- **[PUBLISHED]** The one clean counter-example found: Texas requires a **TDI** marker on
  fully insured cards, so in Texas the absence of "TDI" is a positive signal of
  self-funding — https://www.bcbstx.com/provider/claims/claims-eligibility/um/pri-aso
  This is a **state-specific** convention and does not generalize.
- **[PATTERN]** The reliable signals are all off-card: the 271 eligibility response
  (accumulators and plan-level benefit maxima come back from the plan's own configuration),
  the group number mapped to an ASO group list, and the payer's own prior-auth lookup tool
  queried **with the member ID**, not with the plan name.
- **[PUBLISHED]** Every payer page examined repeats the same instruction, and it is the
  correct operational answer: "always check eligibility and benefits through Availity®
  Essentials or your preferred vendor" — https://www.bcbstx.com/provider/claims/claims-eligibility/um/request-auth
  and "Check eligibility and benefits… prior to rendering services to confirm prior
  authorization requirements."

## 3.3 What actually differs for a home health branch

| Dimension | Fully insured | Self-funded (ASO) |
|---|---|---|
| Benefit maximum (e.g. annual HH visit cap) | Set by the filed plan; state mandates may set a floor | **Set by the employer in the plan document / SPD**; can be lower, higher, or absent |
| Medical policy | Carrier's published policy | Carrier's policy **unless the plan document overrides it** |
| Prior auth program participation | Generally uniform across the book | **Sold group by group** — group may be in or out |
| Turnaround standards | State UM statute + NCQA | **ERISA claims-procedure timeframes** |
| Appeals / external review | State external review | Plan's internal process, then ERISA §502(a); federal external review under the ACA where applicable |
| Prompt pay | State prompt-pay statute | Not applicable |

**[PATTERN]** The practical consequence for scheduling: **an authorization approval from a
self-funded plan's TPA can still be overridden at adjudication by a plan-document benefit
maximum the TPA's UM system did not check.** Highmark states the general principle
explicitly: "Authorization does not guarantee payment."
(https://providers.highmark.com/resources-and-education/highmark-provider-manual/chapter-5-care-and-quality-management/unit-2-authorizations.html)

## 3.4 The statutory mechanism — why state law stops at the plan door

**[PUBLISHED]** ERISA § 514, 29 U.S.C. § 1144 — https://www.law.cornell.edu/uscode/text/29/1144
(retrieved 2026-08-18):

- **§ 1144(a) preemption clause** — ERISA supersedes state laws that "relate to" any
  employee benefit plan.
- **§ 1144(b)(2)(A) savings clause** — state laws that regulate insurance are saved from
  preemption.
- **§ 1144(b)(2)(B) deemer clause**, verbatim: "Neither an employee benefit plan described
  in section 1003(a) of this title… **nor any trust established under such a plan, shall be
  deemed to be an insurance company or other insurer**… or to be engaged in the business of
  insurance… for purposes of any law of any State purporting to regulate insurance
  companies, insurance contracts, banks, trust companies, or investment companies."

The mechanism in one sentence: a state can regulate the *insurance policy* a fully insured
plan buys, which is how state mandates reach fully insured coverage — but a self-funded
plan buys no policy, and the deemer clause forbids the state from treating the plan itself
as an insurer, so the savings clause cannot reach it.

**[UNVERIFIED]** *FMC Corp. v. Holliday*, 498 U.S. 52 (1990) is the controlling Supreme
Court case on the deemer clause. Not confirmed against a primary government source in this
research pass — **cite the statute, not the case, in any client-facing material.**

**[PUBLISHED]** KFF states the consequence directly: federal law "**exempts self-funded
plans established by private employers (but not public employers) from most state insurance
laws, including reserve requirements, mandated benefits, premium taxes, and some consumer
protection regulations**" — https://www.kff.org/health-costs/2025-employer-health-benefits-survey/
(2025 Employer Health Benefits Survey, Section 10: Plan Funding, published 2025-10-22).

**[PUBLISHED]** Cigna's own employer-facing page is a clean carrier-side statement of the
arrangement: "In self-funded solutions, employers pay an administrator to manage the plan
while **the employer funds claim expenses from their own bank accounts**. Cigna Healthcare
offers three self-funded solutions based on an **Administrative Service Agreement**" —
https://www.cigna.com/employers/cost-control/funding-solutions (retrieved 2026-08-18). Its
funding table shows ASO available at 200+ eligible employees with 100% real-time claims
surplus share and **optional** stop-loss, versus fully insured at 0% surplus share.

**Two carve-outs from ERISA entirely.** **[PUBLISHED]** DOL: ERISA "does not cover group
health plans established or maintained by **governmental entities, churches** for their
employees, or plans which are maintained solely to comply with applicable workers
compensation, unemployment, or disability laws" — https://www.dol.gov/general/topic/health-plans/erisa
(retrieved 2026-08-18). Self-funded state and local government plans are instead governed
by PHS Act Title XXVII and enforced by CMS under PHS Act § 2723(b)(1)(B) —
https://www.cms.gov/marketplace/private-health-insurance/self-funded-non-federal-governmental-plans
(retrieved 2026-08-18). **A self-funded school district or municipality is a third
regulatory species** — neither state-regulated insurance nor ERISA. Treat it as its own
payer category.

## 3.5 How much of the market this is

**[PUBLISHED]** KFF 2025 Employer Health Benefits Survey, published **2025-10-22** — the
most recent available as of August 2026 (the 2026 survey is not yet released) —
https://www.kff.org/health-costs/2025-employer-health-benefits-survey/ ⚠️ **STALE-RISK
(annual survey).** Verbatim:

> "**Sixty-seven percent of covered workers, including 27% of covered workers at firms with
> 10 to 199 workers and 80% at larger firms, are enrolled in plans that are self-funded.**"

The 67% figure is stable: 65% last year, 69% five years ago, 66% ten years ago. But the
composition is shifting — **"37% of covered workers in firms with 10 to 199 workers are
covered by a level-funded plan."** Level-funded plans are nominally self-funded
arrangements packaged with heavy stop-loss; KFF notes they "use health status in rating and
underwriting, and **are not required to provide all of the essential health benefits** that
are mandatory for insured plans."

**Two-thirds of commercially covered patients are in a plan whose rules the carrier did not
write.** And the level-funded growth means small-employer patients — historically the
safest assumption for fully insured, state-regulated coverage — increasingly are not.

## 3.6 The employer-set visit cap, with real numbers

This is the concrete answer to "what actually differs." Four published self-funded plan
documents, four different home health caps, **none of which appear in any carrier's
published medical policy.** ⚠️ **STALE-RISK — plan-year specific.** *(URLs appeared
verbatim in search results; the individual SPDs were not each fetched in full.)*

| Plan document | Home health cap |
|---|---|
| City of Gainesville Employee Benefit Plan, 2025 Healthgram HDHP SPD — https://www.gainesville.org/DocumentCenter/View/11129/2025-Healthgram-HDHP-SPD-PDF | "Limited to **60 visits** per calendar year. Payable at 90% after deductible." |
| Ardent Benefits, 2026 i360 PPO Premier HDHP — https://getardentbenefits.com/sites/default/files/2026%20i360%20PPO%20Premier%20HDHP.pdf | "Home Health Care is limited to **100 visits** per Calendar Year." |
| Luther College UMR SPD 2025 — https://www.luther.edu/wp-content/uploads/2025/02/UMR-Health-Insurance-Summary-Plan-Description-2025.pdf | "Maximum Visits Per Calendar Year: **45 Visits**. Paid By Plan After Deductible 80%." |
| Windstream Benefits health booklet — https://windstreambenefits.com/wp-content/uploads/2017/08/02-Book-01-01-2017-Active-00-BP-057-072-077-Class-A30-A42-A53-7470.pdf | "Maximum Visits Per Calendar Year: **40 Visits**." |

40, 45, 60, 100. **The cap is a per-employer data element, not a carrier constant.** A
capacity model that treats "commercial home health visit limit" as a carrier-level value
will be wrong for most commercially covered patients. Note also that these documents define
a "visit" locally — several carry their own "A Home Health Care Visit is defined as…"
language — so the **unit** is plan-specific too, and it may or may not match Aetna's
4-hours-equals-one-visit rule (§4.2).

## 3.7 Appeals and turnaround run on federal rules

**[PUBLISHED]** ERISA claims procedure, 29 CFR § 2560.503-1 —
https://www.ecfr.gov/current/title-29/section-2560.503-1 (retrieved 2026-08-18):

| Claim type | Initial decision | Appeal decision |
|---|---|---|
| **Urgent care** | **72 hours**; if information is missing, notify within 24 hrs, claimant gets ≥48 hrs to respond, then decide within 48 hrs | **72 hours** |
| **Pre-service** (the home health authorization case) | **15 days**, one 15-day extension | **30 days** (one-level) or **15 days each** (two-level) |
| **Post-service** | **30 days**, one 15-day extension | **60 days** (one-level) or **30 days each** (two-level) |

Claimants get **at least 60 days** to file an appeal after an adverse determination.

Two provisions the agency's clinical staff can use directly:

- **§ 2560.503-1(m)(1)(iii):** "Any claim that a physician with knowledge of the claimant's
  medical condition determines is a 'claim involving urgent care'… **shall be treated as** a
  'claim involving urgent care.'" The treating physician's determination is binding on the
  plan's classification.
- **§ 2560.503-1(b)(4):** for urgent claims "a health care professional… with knowledge of a
  claimant's medical condition **shall be permitted to act as the authorized
  representative** of the claimant." **The agency's own clinician can appeal directly**
  without a separate signed representation form.

**External review is federal, not state.** Self-insured plans use either an
accredited-IRO private process or the HHS-administered federal external review process —
DOL Technical Release 2011-02
(https://www.dol.gov/agencies/ebsa/employers-and-advisers/guidance/technical-releases/11-02)
and CMS, External Appeals
(https://www.cms.gov/marketplace/about/affordable-care-act/external-appeals). The
HHS-administered process is free:
https://www.cms.gov/cciio/programs-and-initiatives/consumer-support-and-information/csg-ext-appeals-facts
*(These three URLs appeared verbatim in search results; not individually fetched.)*

**Escalating a self-funded denial to the state insurance commissioner is a wasted step.**
The DOI has no jurisdiction. Build the escalation path around the plan's internal appeal →
federal external review, and around ERISA § 502(a).

## 3.8 The No Surprises Act does apply — and a self-funded plan can opt into state law

The NSA's requirements for ERISA group health plans are codified at **29 CFR part 2590,
subpart B**, which governs ERISA group health plans regardless of funding — structurally
confirmed at 29 CFR § 2590.716-4
(https://www.ecfr.gov/current/title-29/section-2590.716-4, retrieved 2026-08-18).

**[PUBLISHED]** 29 CFR § 2590.716-3, definition of *Specified State law* —
https://www.ecfr.gov/current/title-29/section-2590.716-3 (retrieved 2026-08-18), verbatim:

> "…a State law that provides for a method for determining the total amount payable under a
> group health plan… (including where it applies because **the State has allowed a plan that
> is not otherwise subject to applicable State law an opportunity to opt in, subject to
> section 514 of ERISA**). A group health plan that opts into such a specified State law
> **must do so for all items and services** to which the specified State law applies… and
> must **prominently display in its plan materials** describing the coverage of
> out-of-network services a statement that the plan has opted into the specified State law,
> identify the relevant State (or States), and include a general description of the items
> and services…"

So the plan document is again the source of truth: a self-funded plan may **voluntarily
adopt** a state balance-billing law, and if it does, it must say so prominently in its
materials. "Self-funded therefore no state law" is a default, not an absolute.

---

# Part 4 — Other major commercial carriers

**Headline for a capacity model:** none of Cigna, Aetna commercial, or UnitedHealthcare
commercial uses a Medicare-style episodic bundle for home health. All three are per-visit
or per-unit fee-for-service against a **plan-level visit cap**. Anyone modeling commercial
home health against a PDGM 30-day period is modeling the wrong object.

A second, non-obvious finding runs through all three: **the standard intermittent home
health visit codes (G0151–G0164, G0299/G0300) are largely absent from commercial prior
authorization lists.** Commercial PA is architected around the **per-hour / per-diem
nursing and aide codes** — S9122, S9123, S9124, T1000, T1002, T1003 — i.e. around private
duty and shift nursing, not around intermittent skilled visits. The clinical gate on
intermittent visits is applied through the **benefit cap and the coverage policy**, not
through an authorization queue.

## 4.1 Cigna Healthcare

| | Detail |
|---|---|
| PA required | Yes, on an **11-code list**, effective **03/07/2026** ⚠️ **STALE-RISK** |
| Codes | 99512, H0045, S5150, S5151, **S9122** (aide/hr), **S9123** (RN/hr), **S9124** (LPN/hr), S9125, **T1000** (PDN), T1005, T2044 — all marked "Intake Only," platform CareCore National |
| Codes **not** on the list | G0151–G0164, G0299/G0300 |
| Vendor | **eviCore (EviCore by Evernorth) — intake only** |
| Clinical decision | **Cigna itself** |
| Portal / contacts | evicore.com/provider; intake 866-668-9250; HH fax 855-826-3724 |
| Claims | To Cigna, payer ID **62308** |
| Retro requests | **Go directly to Cigna, not eviCore** |
| Turnaround | ~2 business days after all clinical received; urgent **72 hours** |
| Authorization duration | **90–180 days**, varying by service type, plan and state |
| Criteria | **MCG**, behind login |
| Payment | Per-unit FFS inferred from the code architecture; **rate methodology not published** |

**[PUBLISHED]** Cigna Home Health Commercial Code List, effective 03/07/2026:
https://www.evicore.com/sites/default/files/resources/2026-03/Cigna%20Home%20Health%20Commercial%20Code%20List_eff03.07.2026_Pub03.04.2026.pdf

**[PUBLISHED]** eviCore's Cigna Commercial HH provider orientation, 2026-05-26 — the
division of labor, verbatim: "Users can now submit prior authorization requests for Home
Health services for Cigna Healthcare members via the EviCore by Evernorth (EviCore) portal.
**The clinical review will be performed by Cigna.**"
https://www.evicore.com/sites/default/files/resources/2026-05/Cigna%20Healthcare%20HH%20provider%20orientation%205.26.26.pdf
Corroborated on Cigna's own CHCP page (effective March 7, 2026): "EviCore forwards
precertification request/information over to Cigna Healthcare for review and final
determination" — https://static.cigna.com/assets/chcp/resourceLibrary/preCertification/durable.html

**[PUBLISHED]** Cigna Precertification Services HH Quick Reference Guide, 2025-12-18:
https://www.evicore.com/sites/default/files/resources/2025-12/Cigna%20Precertification%20Services%20HH%20-%20QRG_12-18-2025.pdf

**[PUBLISHED]** Cigna–EviCore HH FAQ, 2026-05-26 (source of the 90–180 day auth validity and
the Time Audit Tool requirement for PDN):
https://www.evicore.com/sites/default/files/resources/2026-05/Cigna-EviCore%20HH%20Frequently%20Asked%20Questions_5.26.26.pdf

**[PUBLISHED]** Master Precertification List for Providers, cover date **July 2026**:
https://www.cigna.com/static/www-cigna-com/docs/master-precertification-list-for-providers.pdf
S9122 precerts under Complete / PHS+ / Preferred only; S9123, S9124 and T1000 precert under
both Complete/Preferred and Basic Standard. Basic Standard's limited outpatient precert set
is "radiation therapy, medical oncology, medical injectables, home infusion therapy and
**private duty nursing**." **The precert requirement varies by Cigna product line** —
another reason the card alone is insufficient.

**[PUBLISHED]** There is **no public Cigna "Home Health Care" medical coverage policy.** The
closest published artifact is administrative policy **A012, Custodial and Non-Skilled
Services** (effective 2025-09-15), which states that "When provided in the home, coverage
for custodial, non-skilled services is subject to the terms, conditions and limitations of
the applicable benefit plan's Home Health Services benefit," and excludes T1019/T1020
personal care outright:
https://static.cigna.com/assets/chcp/pdf/coveragePolicies/medical/ad_a012_administrativepolicy_custodial_and_non-skilled_services.pdf
Policy index: https://static.cigna.com/assets/chcp/resourceLibrary/coveragePolicies/medical/medical_a-z.html
MCG guideline access: https://www.evicore.com/cignaguidelines/ and
https://cignastatespecificguidelines.access.mcg.com/index

Cigna Hospital-at-Home is separately precertified at **revenue code 0161** — a distinct
service line a scheduling platform should not fold into home health.

## 4.2 Aetna commercial (CVS Health)

**[PUBLISHED]** Three Clinical Policy Bulletins govern, not one:

| CPB | Title | URL | Last review |
|---|---|---|---|
| **0201** | Skilled Home Health Care Nursing Services | https://www.aetna.com/cpb/medical/data/200_299/0201.html | 2026-04-22 |
| **0218** | Home Health Aides | https://www.aetna.com/cpb/medical/data/200_299/0218.html | 2026-04-22 |
| **0136** | Skilled Home Private Duty Nursing Care | https://www.aetna.com/cpb/medical/data/100_199/0136.html | 2026-04-07 |

Also relevant: CPB 0730 Home Behavioral Healthcare; CPB 1054 Wound Care: Home or Outpatient
Setting. *(aetna.com returns 403 to default fetchers; a browser User-Agent returns 200.)*

**CPB 0201 coverage criteria — all must be met:** homebound because of illness or injury
(with a note that some state Medicaid programs waive homebound); not primarily
comfort/convenience or custodial; ordered by a physician/PA/NP under an active plan of
care; provided **in lieu of** continued hospitalization or SNF confinement; appropriate for
active treatment to avoid serious complications; **intermittent or hourly in nature**;
appropriate in time, frequency and duration.

**The two definitions that determine how many "visits" a shift consumes — verbatim from
CPB 0201, and the most billing-critical sentences in this section:**

> "Intermittent or part time skilled home care nursing is defined as a **visit of up to 4
> hours** in duration."

> "Home health skilled nursing care is defined as a **consecutive 4-hour period of time
> (i.e., an 8-hour shift equals 2 visits)**."

An 8-hour shift burns two visits against the member's annual cap. **A scheduling platform
that counts one visit per caregiver-arrival will under-consume the Aetna benefit in its
model and over-promise capacity.**

CPB 0201 also holds that home infusion and its related nursing are **not** part of the home
health benefit and "do[es] not accumulate toward any associated Home or Skilled Nursing
benefit limits."

**Published initial allowance — the closest thing any of the three carriers publishes.**
CPB 0218 (Home Health Aides), verbatim:

> "Home Health Aide services are intended to be short-term. Note: **The initial
> authorization should be for a period not longer than 3 months, with one extension of
> another 3 months permitted.** After the member has been receiving intermittent home
> health aide services for a period of 6 months or more… other information should be
> provided…"

CPB 0201 continuation criteria require documented ongoing need, reasonable expectation of
improvement, and "documented efforts to transition care to the member/caregiver," with the
explicit exclusion: "Visits made because of on-going social situations (homelessness,
protective services, etc.) do not constitute an ongoing need for home care services."

**[PUBLISHED]** Participating provider precertification list, updated **2026-08-01**:
https://www.aetna.com/content/dam/aetna/pdfs/aetnacom/healthcare-professionals/2026_Precert_List.pdf
(current per https://www.aetna.com/health-care-professionals/precertification/precertification-lists.html)

**Key scoping finding: home health care is not a line item on the national commercial
precert table.** The only home-based entry among the 40 national items is **#29 Private
duty nursing — S9123, S9124, T1000, T1030, T1031.** "Home health care" appears only under
**Special programs**, and every delegation there is **Medicare-scoped**:

| Vendor | Scope | States |
|---|---|---|
| **Carelon Post Acute Solutions** (formerly myNEXUS) | All **Medicare** home health — SN, PT, OT, ST, HHA, MSW | FL, GA, KY, OH, OK, TX, VA (*exception: OK and VA D-SNPs*) |
| **eviCore healthcare** | All **Medicare Advantage** home health, same scope | NJ, NY, PA, WV |

Codes listed: G0151–G0162, G0299, G0300, G0493–G0496. Carelon provider line
1-833-585-6262, portal Portal.mynexuscare.com. eviCore 1-888-622-7329.

⚠️ **Read this carefully:** the national list is **silent** on commercial home health, not
affirmatively negative. Confirm at plan-document level before relying on "no PA." Aetna's
online code-lookup tool is **not usable as evidence** — it renders client-side and returns
identical boilerplate for every code tested (G0151, G0154, S9123, T1021).

**Portal: Availity, decisively.** From the 2026 precert list itself: "You can submit most
requests through our **Availity® provider portal**… Go to Availity.com to start a request."
Phone fallback: commercial 1-888-632-3862; Medicare 1-800-624-0756.

**[UNVERIFIED]** CareCentrix ownership by CVS Health, and any Aetna home health routing
through CareCentrix. Zero mentions of CareCentrix appear in the 2026 Aetna precertification
list; carecentrix.com discloses no parent company and names no health plan clients. **The
verified Aetna post-acute delegations are Carelon and eviCore, both Medicare-only. Do not
build on a CareCentrix assumption for Aetna.**

**Payment:** no published fee schedule. CPB 0201's 4-hour visit arithmetic plus the
benefit-limit accumulation language is primary-source evidence of a **per-visit,
benefit-limited** model, not an episodic bundle.

## 4.3 UnitedHealthcare commercial

**[PUBLISHED]** UHC Commercial Advance Notification and Prior Authorization Requirements,
effective **2026-07-01** (PCA-1-26-00657):
https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/commercial/UHC-Commercial-Advance-Notification-PA-Requirements-7-2026.pdf

> **Home health care – non-nutritional:** "Prior authorization required only in outpatient
> settings, to include the member's home." — **T1000, T1002, T1003**

T1000 = private duty / independent nursing per 15 min; T1002 = RN per 15 min; T1003 =
LPN/LVN per 15 min. **Absent: G0151–G0164, S9122–S9131, 99500–99602, T1021, T1030, T1031.**
**Standard intermittent home health visit codes require no UHC commercial prior
authorization at all.**

**Individual Exchange** (effective 2026-08-01): no "home health care" category — only
**private duty nursing, T1002/T1003**, and that is excluded in AL, AZ, FL, GA, MS, NM, SC,
TN, TX, WI, WA:
https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/exchanges/UHC-Exchange-Plans-Advance-Notification-PA-Eff-8-1-26.pdf

Landing pages:
https://www.uhcprovider.com/en/prior-auth-advance-notification/adv-notification-plan-reqs.html
and https://www.uhcprovider.com/en/prior-auth-advance-notification.html
Commercial and Exchange home health PA is **administered by UHC directly** through the
Provider Portal — **no vendor is named.**

**[UNVERIFIED]** A UHC program branded "Home Health Care Prior Authorization **and Site of
Service**" could not be confirmed. Site of Service is a **separate** program in the same
document, applied to surgical/procedural categories; the home health row carries no SOS
notation.

**naviHealth rebrand — confirmed, and it no longer touches home health.** naviHealth became
**Optum Home & Community Care** (announced Oct 2023, effective Q1 2024);
https://business.optum.com/en/access/home-and-community.html no longer mentions naviHealth.
The legacy name persists in UHC's 2026 MA PA document ("Home & Community Care (formerly
naviHealth) manages prior authorization for in-scope membership"), but its remaining PA
authority is post-acute **inpatient** — SNF, IRF, LTAC — not home health, which was removed
from its scope in April 2025.

**The prior-authorization reduction cycle — direct answer on whether home health was
affected:** ⚠️ **STALE-RISK, all dates 2025–2026**

| Event | Effect on home health |
|---|---|
| Home health PA no longer required, effective **2025-04-01** — "we'll no longer require prior authorization or concurrent review processes for home health services managed by Home & Community" — https://www.uhcprovider.com/en/resource-library/news/2025/home-health-prior-auth-changing.html | **Removed — Medicare Advantage + D-SNP only, 41 jurisdictions.** No commercial or Exchange application. |
| 2026 Summary of Changes — "Medicare Advantage \| **Add** \| Home Health \| **S9122, S9123, S9124** \| **02/01/2026** \| Add PA" — https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/multi/2026-Summary-of-Changes-AdvNotice-and-PriorAuth.pdf | **Partially re-added for MA, Feb 2026.** No commercial or Exchange home health changes. |
| UHG Newsroom, **2026-05-05**, 30% PA reduction — https://www.unitedhealthgroup.com/newsroom/2026/2026-05-05-uhc-cuts-prior-authorization-requirements-by-30-percent.html | Named categories: select outpatient surgeries, diagnostic tests, certain outpatient therapies, chiropractic. **Home health not mentioned.** |
| National Gold Card CPT list — https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/gold/UHC-Gold-Card-CPT-List.pdf | **Zero hits** for T1000/T1002/T1003, G0151–G0164, S9122–S9131. Home health has never been in Gold Card. |

**The direction of travel is not uniformly deregulatory** — MA home health PA was removed in
April 2025 and partially re-added in February 2026. Commercial T1000/T1002/T1003 has been
stable throughout.

**MA home health PA now survives only as three carve-outs** (Med Adv/Dual, effective
2026-08-01): Erickson Advantage; **Tennessee D-SNP** (S9122, S9123, T1000); **Peoples
Health** (full discipline-by-discipline code set):
https://www.uhcprovider.com/content/dam/provider/docs/public/prior-auth/pa-requirements/medicare/Med-Adv-Dual-Eff-8-1-26.pdf
That document also states "AIP DSNP plans should not route to naviHealth and are serviced
by the Optum PACM team" — **direct confirmation that Applicable Integrated Plan status
changes the routing** (see Part 7).

**Payment: per-visit FFS, and this one is explicitly published.** Home Health Services
Policy, Professional — **2026R5036A, effective 2026-07-01**, applying to all UHC Commercial
and all Individual Exchange plans:
https://www.uhcprovider.com/content/dam/provider/docs/public/policies/comm-reimbursement/COMM-IEX-Home-Health-Services-Professional.pdf
**CMS-1500 professional claim, POS 12** — per-code / per-unit fee-for-service. The
commercial reimbursement policy index lists exactly one home health policy, the
professional one; **there is no facility / UB-04 home health reimbursement policy**, which
is where an episodic PPS-style methodology would have to live:
https://www.uhcprovider.com/en/policies-protocols/commercial-policies/commercial-reimbursement-policies.html
Rules worth encoding: inpatient supersedes POS 12 on overlapping dates; physician-billed
status-indicator E/I/X home health HCPCS are denied but "continue to be considered for
reimbursement when appropriately submitted by home health providers."

**Coverage policy and the real utilization gate.** *Home Health, Skilled, and Custodial Care
Services*, **MP.022.28, effective 2026-07-01**, using **InterQual LOC: Home Care**:
https://www.uhcprovider.com/content/dam/provider/docs/public/policies/comm-medical-drug/home-health-care.pdf
Gate criteria, verbatim, require services be "Provided in the home **in lieu of skilled care
in another setting**… Clinically appropriate and **not more costly than an alternative
health service**; and **Intermittent and part time (typically provided for less than 4 hours
per day)**."

**That "<4 hours per day" intermittency threshold is UHC's de facto site-of-service lever.**
Anything more intensive is pushed into the private duty nursing policy (MP.017.22, which
requires a **CMS-485**:
https://www.uhcprovider.com/content/dam/provider/docs/public/policies/comm-medical-drug/private-duty-nursing-services.pdf)
or into a facility benefit. Also material: therapy in the home **from a home health agency**
falls under the home health benefit; therapy from an **independent therapist** falls under
the outpatient therapy benefit — two different accumulators for the same visit type.
No policy-level visit cap: "Refer to the member specific benefit plan document for any
applicable visit limitations."

**Notification timing — the single most schedule-relevant UHC rule.** 2026 Administrative
Guide: "Following a facility discharge, advance notification for home health services and
DME is required **within 2 business days after the start of service**." Standard otherwise
is **≥5 business days before service**. Decisions: standard 15 calendar days (7 for MA),
expedited 72 hours.
https://www.uhcprovider.com/content/dam/provider/docs/public/admin-guides/2026-UHC-Administrative-Guide.pdf

## 4.4 Cross-carrier comparison

| | **Cigna Commercial** | **Aetna Commercial** | **UHC Commercial** |
|---|---|---|---|
| HH PA required | Yes — 11 codes, eff. 2026-03-07 | **Not on national list**; PDN is (S9123/S9124/T1000/T1030/T1031); plan-level otherwise | Yes — **T1000, T1002, T1003 only** |
| G0151–G0162 on PA list | No | Medicare delegations only | No |
| Vendor | eviCore — **intake only** | **None for commercial.** Carelon (Medicare, 7 states) / eviCore (MA, 4 states) | **None** — UHC direct |
| Clinical decision by | **Cigna** | Aetna | UHC |
| Portal | evicore.com Provider's Hub | **Availity.com** | UHC Provider Portal |
| Criteria source | **MCG** (not public) + Admin Policy A012 | **CPB 0201 / 0218 / 0136** (public) | **InterQual LOC: Home Care** via MP.022.28 |
| The real gate | Per-hour/per-diem code architecture | "4 hours = 1 visit" + plan visit cap | **"<4 hrs/day, intermittent and part time"** + "in lieu of skilled care in another setting" |
| Auth duration | **90–180 days** | HHA: **3 months + one 3-month extension** | Not published |
| Turnaround | ~2 business days; urgent 72 hrs | Submit ≥2 weeks ahead | Standard 15 days (MA 7); expedited 72 hrs |
| Payment model | Per-unit FFS (inferred); rate not published | Per-visit, benefit-limited (inferred); rate not published | **Per-visit FFS, CMS-1500/POS 12 — verified in 2026R5036A** |
| Episodic/bundled arrangement | None published | None published | **None — no UB-04 HH reimbursement policy exists** |
| Published initial-visit allowance | None | **None numeric**; CPB 0218's 3-month HHA window is closest | None |

---

# Part 5 — Medicaid and skilled home health

## 5.0 The federal backbone — read this before any state detail

Two federal regulations do most of the conceptual work, and getting them straight
prevents the most common and most expensive mistake in this domain: conflating the
**state plan home health benefit** with **HCBS waiver services**.

### 5.0.1 State plan home health — 42 CFR § 440.70

**[PUBLISHED]** eCFR, 42 CFR § 440.70 "Home health services," current text retrieved
2026-08-18: https://www.ecfr.gov/current/title-42/section-440.70

Home health is a **mandatory** Medicaid state plan benefit. The regulation defines it as
services provided at the beneficiary's place of residence on written orders as part of a
written plan of care. Six points matter operationally:

1. **Who may order.** "On orders written by a **physician, nurse practitioner, clinical
   nurse specialist or physician assistant**, working in accordance with State law." This is
   broader than Medicare's certifying-physician rule.
2. **The 60-day plan-of-care review is federal.** The ordering practitioner "reviews
   [the plan of care] **every 60 days**" for nursing, aide, and therapy services. When a
   state's home health benefit window is 60 days, this is where it comes from — the
   **plan-of-care review cycle**, not a payment episode.
3. **Required vs optional components:**
   - Required: **(1) nursing** on a part-time or intermittent basis; **(2) home health aide**
     service; **(3) medical supplies, equipment and appliances**.
   - **Optional: (4) physical therapy, occupational therapy, speech pathology and
     audiology.** Therapy under the home health benefit is a **state option**. This is the
     single biggest source of state-to-state variation in therapy coverage and caps.
4. **No homebound requirement.** "Home health services **cannot be limited to services
   furnished to beneficiaries who are homebound**." A Medicaid home health patient does not
   have to be homebound. This is a hard contrast with Medicare and with several commercial
   policies (BCBSNC's commercial policy *does* require homebound status — §1.6).
5. **No skilled-need gateway for the aide benefit.** "Coverage of home health services
   cannot be contingent upon the beneficiary needing nursing or therapy services." Under
   Medicaid an aide-only case is permissible; under Medicare it is not.
6. **Place of residence excludes** a hospital, nursing facility, or ICF/IID (with a narrow
   ICF/IID exception). It expressly includes "any setting in which normal life activities
   take place."

**[PUBLISHED]** A "home health agency" for Medicaid purposes "means a public or private
agency or organization… that meets requirements for participation in **Medicare**,
including the capitalization requirements under § 489.28." Medicare certification is the
gate to the Medicaid home health benefit.

### 5.0.2 HCBS waiver services — 42 CFR § 440.180

**[PUBLISHED]** eCFR, 42 CFR § 440.180 "Home and community-based waiver services," current
text retrieved 2026-08-18: https://www.ecfr.gov/current/title-42/section-440.180

The definitional sentence settles the whole question:

> "'Home or community-based services' means services, **not otherwise furnished under the
> State's Medicaid plan**, that are furnished under a waiver granted under the provisions
> of part 441, subpart G of this chapter."

**HCBS waiver services are, by definition, services that are *not* the state plan
benefit.** They are a different benefit, authorized by a different entity, under a
different plan of care, at a different rate, with different documentation.

The § 440.180(b) list of includable waiver services is: case management, **homemaker**,
**home health aide**, **personal care**, adult day health, habilitation, respite care,
day treatment / psychosocial rehab / clinic services for chronic mental illness, and
"other services requested by the agency and approved by CMS as cost effective and
necessary to avoid institutionalization." Waiver services are subject to health-and-welfare
assurances (§ 441.302(a)) and FFP limits (§ 441.310).

### 5.0.3 The practical contrast a scheduling platform must encode

| | State plan home health (§ 440.70) | HCBS waiver (§ 440.180, 1915(c)) |
|---|---|---|
| Mandatory? | **Yes** — every state must cover it | No — state option, capped enrollment, waiting lists |
| Core services | Skilled nursing, home health aide, supplies/DME; therapy at state option | Personal care, homemaker, aide, respite, habilitation, case management |
| Authorizing document | **Plan of care reviewed every 60 days** by physician/NP/CNS/PA | **Person-centered service plan** authorized by a case manager / care manager / AAA |
| Who authorizes | State Medicaid agency (FFS) or the MCO's UM department | Waiver case manager / care management entity — usually **not** the health plan's UM nurse |
| Homebound required | **No** (prohibited) | No |
| Skilled need required | **No** — aide-only permitted | No |
| Billing unit | Typically per visit for skilled; per unit/hour for aide | Typically per unit (15-min or hourly) |
| Enrollment limits | None — entitlement | Capped slots, waiting lists, cost-neutrality tests |

**[PATTERN]** The conflation failure mode in the field: a branch takes a referral for
"Medicaid home care," staffs it as an aide case under a waiver service plan, and then
tries to bill skilled nursing visits against the state plan benefit without a plan of care
or a prior authorization. Or the reverse: a skilled nursing patient's waiver aide hours run
out and the scheduler assumes the skilled auth covers them. **They are two independent
authorizations on the same patient, on different clocks, from different authorizers.** The
platform needs to model them as separate authorization objects, not as one "Medicaid auth."

## 5.1 Indiana Medicaid (IHCP) — a prior-authorize-everything state

**[PUBLISHED]** Primary source: IHCP *Home Health Services* provider reference module,
**PROMOD00032, Version 8.1, published 2026-03-10**, stating "policies and procedures as of
**April 1, 2025**":
https://www.in.gov/medicaid/providers/files/modules/home-health-services.pdf
Secondary: IHCP Quick Reference Guide, **Version 14.1, May 2026**:
https://www.in.gov/medicaid/providers/files/quick-reference.pdf
Regulation: 405 IAC 5-16 (and 405 IAC 5-16-3, -3.1); nursing must also meet 405 IAC 5-22-2.
Cornell mirror of 405 IAC 5-16-3.1: https://www.law.cornell.edu/regulations/indiana/405-IAC-5-16-3.1

⚠️ **Note the built-in lag: the module is dated March 2026 but its policies are current only
to April 1, 2025.** Check IHCP Bulletins for anything after that date before relying on it.

### The headline

> "All home health services require prior authorization (PA), except as outlined in PA
> Exception for Hospital Discharge section."

**There is no routine visits-before-PA allowance in Indiana.** The only PA-free window is
the post-hospital-discharge exception.

### The one PA-free window — and the date it starts from

Requires a written practitioner order issued **before** discharge.

| Discipline | PA-free allowance | Window |
|---|---|---|
| RN + LPN + home health aide (**combined**) | **120 units** | 30 calendar days following discharge |
| PT + OT + SLP (**any combination**) | **30 units** | 30 calendar days following discharge |

**The clock anchor, verbatim: "The hospital discharge date is counted as day 1."** Not the
first visit, not the order date, not the PA approval date.

Billing mechanic: **occurrence code 42** with the discharge date in fields 31a–34b of the
UB-04 bypasses the PA edit. Exceed the limit without PA and "CoreMMIS automatically denies
or cuts back units on the remittance advice."

### Therapy disciplines share a combined allowance — confirmed

Under the discharge exception, OT/PT/SLP share **one pooled 30-unit allowance** — "any
combination of therapy services, not to exceed 30 units." **The disciplines do not get
separate allowances.** Beyond that window all therapy is prior-authorized, requested
per-discipline via the G-codes.

### Billing units — the asymmetry a scheduling engine must encode

| Code | Discipline | Unit |
|---|---|---|
| 99600 TD | Registered nurse | **1 unit = 1 hour** |
| 99600 TE | Licensed practical nurse | **1 unit = 1 hour** |
| 99600 | Home health aide | **1 unit = 1 hour** |
| G0151 | Physical therapist | **1 unit = 15 minutes** |
| G0152 | Occupational therapist | **1 unit = 15 minutes** |
| G0153 | Speech-language pathologist | **1 unit = 15 minutes** |
| Occurrence code 73 | Overhead | 1 unit per provider per member per day |

**Nursing and aide bill in hours; therapy bills in 15-minute units.** Rounding differs too:
therapy rounds up at **8 minutes** into a 15-minute unit (under 8 minutes is unbillable);
nursing/aide bills a full first hour if any service was provided, with subsequent hours
rounding up at **30 minutes** and down at 29. Worked examples from the module: 85 billable
minutes → 1 unit; 95 minutes → 2 units.

**PA quirk worth encoding:** nursing PA is requested **only** as `99600 TD` regardless of RN
vs LPN — "CoreMMIS uses the PA units approved for the nursing service as 99600 TD." The
RN/LPN distinction appears only on the claim, not on the authorization.

### Benefit window and clock anchors

Indiana does **not** publish a fixed FFS authorization-period length. The governing cycles
are:

- **Plan of care review: every 60 days** by the qualified attending practitioner, who must
  reorder if still medically necessary.
- **Initial face-to-face encounter:** no more than **90 days before or 30 days after the
  start of services** — anchored to start of care, not the order date or PA date.
- **Long-term care:** face-to-face on a rolling 12-month basis, within 90 days before / 30
  days after the **anniversary of the previous year's encounter**.
- **"Interruption" — a real scheduling trap:** an interruption is **60 days or more from the
  end of the last authorization period**, and an interruption **re-triggers the full
  face-to-face requirement.** A 61-day gap is not a resumption; it is a new start of care.

⚠️ **[UNVERIFIED]** The authorization period length is set per-request by the PA contractor
rather than by published rule. Would need the IHCP Prior Authorization module or an actual
PA determination letter to confirm.

### Hourly determination guidelines — soft tiers, not hard caps

The module publishes tiers explicitly labelled "guidelines only":

| Tier | Applies to |
|---|---|
| **Up to 12 hrs/day** | Members requiring 24-hour monitoring — ventilator dependence, tracheostomy, severe respiratory/neuromuscular conditions |
| **Up to 16 hrs/day** | Case-by-case: single caregiver working full time, or significant additional childcare burden (≥3 children under 6, ≥4 under 10, or ≥1 child with special medical needs) |
| **8 hrs/day** | Extensive care and daily monitoring without rapid-deterioration risk |
| **3–7 hrs/day** | Heavy physical care with some skilled monitoring; aide up to 4 hrs/day for employed adults with disabilities, **splittable AM/PM** |

### PA vendor and submission channel

**Acentra Health** is the FFS Prior Authorization and Utilization Management contractor for
medical, dental and SUD. ⚠️ **STALE-RISK — PA vendor contracts re-procure; Indiana already
moved Kepro → Acentra (Kepro and CNSI merged into Acentra).**

- Portal: **Atrezzo Provider Portal, atrezzo.acentra.com**
- Phone 866-725-9991 · Fax 800-261-2774
- Channels: Atrezzo portal, **278 electronic transaction**, mail, fax or phone (phone still
  requires supporting documentation).
- **Gainwell Technologies** operates CoreMMIS as fiscal agent — **not** the PA vendor.
  **Myers and Stauffer** handles long-term care rate-setting and audits only. Do not confuse
  either with PA.

### Managed care programs and entities

The module is explicit that it covers **FFS only**: "For information about services provided
through the managed care delivery system … providers must contact the member's managed care
entity (MCE) or refer to the MCE provider manual."

| Program | Population | MCEs |
|---|---|---|
| Healthy Indiana Plan (HIP) | Adults 19–64 | Anthem, CareSource, MHS (Centene), MDwise (+UnitedHealthcare — see caveat) |
| Hoosier Healthwise | Children, pregnant members | Same pool |
| Hoosier Care Connect | Aged/blind/disabled not in LTSS | Same pool |
| **Indiana PathWays for Aging** | **65+ LTSS — managed LTSS** | **Anthem, Humana (Healthy Horizons), UnitedHealthcare** |

**PathWays for Aging status: CONFIRMED LIVE.** It has its own Maximus enrollment broker line
(877-284-9294), its own MCE contacts, dedicated LTSS provider-relations mailboxes, and a
"PathWays Dual Care" product with a separate dental benefit manager (Liberty Dental).
Module version 8.0 explicitly "Added PathWays to initial note."

⚠️ **Routing hazard:** Anthem's PathWays PA line (**844-284-1798**) is different from its
HIP/HHW PA line (**844-533-1995**). Same carrier, same state, different queue.

⚠️ **[UNVERIFIED]** UnitedHealthcare's participation in HIP specifically. Anthem, CareSource,
MHS and MDwise were directly observed on the HIP/HHW/HCC page; Anthem, Humana and
UnitedHealthcare on the PathWays page.

### Other Indiana details that affect scheduling

- **Claims are institutional (UB-04 / 837I), not professional.** Unusual, and different from
  most states' home health billing.
- Services must be "intermittent or part time, **except for ventilator-dependent patients**
  who have a developed plan of home health care" (405 IAC 5-16-3.1). Homemaker/chore/sitter
  services are excluded "except as specified under applicable Medicaid waiver programs."
- **A one-time nursing visit requires no PA** when a member already has authorized home
  health and the attending physician orders a single visit due to a change in condition to
  prevent deterioration.
- **ALF residents:** the PA must carry **POS code 13**, and the agency must verify services
  are not duplicative of the ALF per diem.
- **Multiple members in one household** = a "multiple-member care situation," which must be
  reported on **each** member's individual PA.
- **Hospice:** members 21+ cannot concurrently receive home health for the terminal
  diagnosis; members ≤20 can (concurrent care).
- Agency staff **may** be the member's own parent or legally responsible individual and
  still bill, within scope of practice.
- Home health is **not** limited to homebound members (consistent with 42 CFR 440.70).
- **EVV applies** to home health services.

---

## 5.2 Ohio Medicaid — hard hour caps and legislated visit spacing

**[PUBLISHED]** All fetched from codes.ohio.gov, 2026-08-18:

| Rule | Subject | Effective |
|---|---|---|
| OAC 5160-12-01 — https://codes.ohio.gov/ohio-administrative-code/rule-5160-12-01 | Home health services: provision requirements, coverage, service specification | **2021-03-07** |
| OAC 5160-12-02 — https://codes.ohio.gov/ohio-administrative-code/rule-5160-12-02 | Private duty nursing | **2021-03-07** |
| OAC 5160-12-04 — https://codes.ohio.gov/ohio-administrative-code/rule-5160-12-04 | Home health and PDN: visit policy | **2021-03-07** |
| OAC 5160-12-05 — https://codes.ohio.gov/ohio-administrative-code/rule-5160-12-05 | Reimbursement: home health services | **2024-01-01** |
| Chapter index — https://codes.ohio.gov/ohio-administrative-code/chapter-5160-12 | "Ohio Medicaid State Plan Home Health and Nursing Services" | — |

Other rules in the chapter: 5160-12-02.3 PDN service authorization · 5160-12-03
Medicare-certified HHA qualifications · 5160-12-03.1 non-agency nurses / otherwise-accredited
agencies · 5160-12-06 PDN reimbursement · 5160-12-07 reimbursement exceptions · 5160-12-08 RN
assessment/consultation.

⚠️ Note the drift: the **clinical rule is effective 2021**; the **payment rule is effective
2024.** They are not revised together.

### Service limits — and the combined-vs-separate answer

| Limit | Value | Scope | Cite |
|---|---|---|---|
| Per-day combined | **8 hours/day** | nursing **+** aide **+** skilled therapies — *all three* | 5160-12-01(C)(1) |
| Per-week combined | **14 hours/week** | nursing **+** aide **only** — therapies **excluded** | 5160-12-01(C)(2) |
| Per-visit | **4 hours max** | any single visit | 5160-12-01(C) |
| Post-discharge enhanced | **28 hours/week for 60 consecutive days** | nursing + aide | 5160-12-01(D) |

**The key asymmetry: skilled therapies count against the daily 8-hour cap but not against
the weekly 14-hour cap.** Therapies have no published per-discipline visit count and no
combined therapy allowance — they are constrained only by the 8 hr/day ceiling, the 4-hour
visit cap, medical necessity and PA. **That is the opposite of Indiana's pooled 30-unit
therapy construct.** Two neighbouring states, two incompatible therapy models.

Exceeding 14 hrs/week requires PA: "except as specified in paragraphs (D) and (H) of this
rule **or as prior authorized by ODM or its designee**."

**Paragraph (H) — increased services.** Members under 21, members on HCBS waivers, or
members meeting institutional level-of-care criteria may exceed standard limits when
medically necessary. Billing flag: **modifier U5** — "The use of the U5 modifier indicates
that all conditions of this paragraph were met."

### The 60-day period and what date it starts from

The **60-day enhanced post-discharge period** (28 hrs/week) requires a **3+ day inpatient
hospital stay** and a comparable level-of-care finding. For the parallel PDN construct,
5160-12-02 states the anchor plainly:

> "The sixty days will begin **when the individual is discharged from the hospital to the
> individual's place of residence**."

**So Ohio, like Indiana, anchors its post-acute window to the discharge date** — not the
first visit, not the order date, not PA approval. (Indiana counts discharge day as day 1
over 30 days; Ohio runs 60 consecutive days from discharge to residence.)

Separately, the **face-to-face encounter** must be documented "within ninety days prior to
the start of care date, or within thirty days following the start of care date" — anchored
to **start of care**, and identical in shape to Indiana's 90/30 rule (both track 42 CFR
440.70(f), §5.0.1). Telehealth permitted.

### Correcting a common misreading: there is no "14 units per visit" rule

The 14 is **hours per week**. The actual per-visit billing structure under **5160-12-05
(effective 2024-01-01)** is a **base rate + increment** model:

- **Base rate** covers the initial **35–60 minutes** of aide or nursing service, **or up to
  4 units of initial skilled therapy**.
- **Unit rate** applies in **15-minute increments** when a visit exceeds 60 minutes, or is
  under 35 minutes.
- Under 15 min → 1 unit max. 16–34 min → 2 units max. 35–60 min → base rate. Beyond 1 hr →
  base + additional units, capped by the 4-hour visit limit.
- Codes: **G0299** (RN), **G0300** (LPN). Modifier **HQ** = group setting, reimbursed at
  **75%** of the maximum. **U1** = home infusion therapy. **POS 02** = telehealth.
- Payment = "the lesser of the provider's billed charge or the medicaid maximum rate."

### Visit policy (5160-12-04) — the hardest scheduling constraints found anywhere

A "visit" = the duration a covered service is provided during an in-person or telehealth
encounter to **one or more** Medicaid individuals at the same residence on the same date
during the same time period.

**Rules a capacity engine must enforce as constraints, not warnings:**

- **A minimum 2-hour gap must separate consecutive visits of the same service type.**
- **A 2-hour interval is required between home health nursing and PDN on the same day.**
- **A 2-hour separation is required when HCBS waiver services of the same scope overlap
  home health / PDN.**
- One procedure code = one visit; each visit is a separate claim line item.
- Same-day repeat visits by the same provider need documented medical necessity: **2nd visit
  = modifier U2; 3rd and beyond = modifier U3.**
- All visits require an **ODM-approved EVV system** per rule 5160-1-40.

**Ohio is the strongest published evidence that visit spacing is a payment rule, not just an
operational preference.** A router that packs two nursing visits 90 minutes apart in Ohio
produces an unpayable claim.

### Prior authorization: state vs plan

**5160-12-01(F)(6)** routes managed care members to the plan: "Access home health services in
accordance with the individual's managed care plan when the individual is enrolled in a
medicaid managed care plan." FFS authority is "**ODM or its designee**."

For PDN (5160-12-02) the review authority splits **three** ways: **ODM or designee**
(non-waiver members and ODA-waivered adults), **DODD via the county board**
(DODD-administered waivers), and **the managed care plan** (MMC enrollees). Expect the same
tri-partite logic to shape home health routing.

**Retroactive authorization is contemplated in rule** for emergency PDN — approvable
retroactively when "the provider has an existing prior authorization to provide PDN to the
individual" and services were medically necessary "to protect the health and welfare of the
individual." **Note the precondition: a pre-existing PA relationship. There is no cold-start
retro path in Ohio rule.**

⚠️ **[UNVERIFIED]** 5160-12-02 does not specify review turnaround timeframes or a standing
authorization-period length. Those live in plan contracts and the ODM PA rules, not this
chapter. (The federal ceiling in §6.0.2 still applies to MCOs.)

### Managed care architecture (2026)

⚠️ **[SEARCH-VERIFIED]** — the ODM managed-care pages returned 404 on direct fetch. Treat
this roster as high-confidence-but-secondary and confirm with ODM.

- **Next Generation managed care** launched **2023-02-01**. Seven statewide general-Medicaid
  MCOs: **AmeriHealth Caritas Ohio, Anthem BCBS, Buckeye Health Plan, CareSource, Humana
  Healthy Horizons, Molina Healthcare of Ohio, UnitedHealthcare Community Plan.**
  ⚠️ Search results consistently listed those seven, with **Aetna Better Health serving
  OhioRISE rather than general Medicaid.** Verify before relying on it.
- **OhioRISE** — separate specialized managed care program for children and youth with
  complex behavioral health needs, administered by **Aetna Better Health of Ohio**.
- **Next Generation MyCare** — the dual-eligible program across 29 counties, **launched
  January 2026** with four MCOs: **Anthem, Buckeye, CareSource, Molina.** ⚠️ **STALE-RISK —
  this is the freshest moving part in Ohio and is mid-transition right now.**
- **Single Pharmacy Benefit Manager (SPBM)** operated by **Gainwell**, replacing per-plan PBMs.
- **Centralized credentialing** — Next Gen consolidated credentialing and claims-processing
  standards so a provider does not maintain separate credentialing per plan.

⚠️ **[UNVERIFIED — industry pattern]** The **PNM (Provider Network Management) module** is
understood to be the single ODM front door for provider enrollment, revalidation and
centralized credentialing, fronting a **Fiscal Intermediary (FI)** that routes claims and PA
transactions to the correct MCO or to FFS. No ODM primary page describing PNM could be
fetched. **Confirm directly with ODM before building against it.**

---

## 5.3 Contrast states

### Texas — deliver first, authorize after, and a rolling authorization week

**[PUBLISHED]** *Home Health Nursing and Private Duty Nursing Services Handbook*, Texas
Medicaid Provider Procedures Manual, **March 2026 edition** (42 pp), fetched in full:
https://www.tmhp.com/sites/default/files/file-library/resources/provider-manuals/tmppm/pdf-chapters/2026/2026-03-march/2_10_hh_nursing_and_pdn_srvs.pdf
Manual index: https://www.tmhp.com/resources/provider-manuals/tmppm

**Texas has no visit-count cap — it has a time-shape cap.** "Part-time is defined as SN or
HHA visits provided less than eight hours per day for any number of days per week.
**Part-time visits may be continuous up to 7.5 hours per day (not to exceed a combined total
of three 2.5 hour visits).**" "Acute" is defined as expected to resolve **within 60 days**.

**All SN and HHA services require PA — but Texas requires you to deliver before you are
authorized:**

> "Providers must obtain authorization **within three business days of the SOC date** for an
> initial authorization. For recertifications, providers must obtain authorization **within
> seven business days of the new SOC date**. **During the authorization process, providers
> are required to deliver the requested services from the SOC date.**"

**The clock anchor is the SOC (start of care) date** — "the date agreed to by the physician
or allowed practitioner, the RN, the Home Health Agency, and the client, parent, guardian,
or caregiver," documented on the plan of care. Not the order date, not the PA date.

**Retroactive rules — precise and punitive:**
- Late requests: "If a request is received more than three business days after the SOC, or
  after **5 p.m., Central Time, on the third day**, authorization is given for dates of
  service **beginning three business days before receipt** of the completed request."
  Everything earlier is unpaid.
- "The TMHP Prior Authorization Department **does not prior authorize an SOC date earlier
  than seven calendar days before contact** with TMHP."
- **PDN initial requests may be prior authorized for a maximum of 90 days.**

**The single most scheduling-hostile rule found in this research — the authorization week is
a rolling 7-day window keyed to the authorization start day, not a calendar week:**

> "A prior authorized week coverage period begins from the day of the week the prior
> authorization period begins on and continues for seven days. For example, if the prior
> authorization starts on a Thursday, the prior authorization week runs Thursday through
> Wednesday. The number of nursing hours authorized for a week must be contained in that
> prior authorization week. **Hours billed in excess of those authorized for the PAN week
> are subject to recoupment.**"

A scheduling engine that meters against Sunday–Saturday weeks will over-deliver in some
Texas PAN weeks and under-deliver in others, and the over-delivery is recouped.

**Plan-of-care mechanics:** POC must be signed and dated by the assessing RN **before** PA
is requested; the physician signature is **not** required before requesting PA but must be
obtained "no later than 30 days from the SOC date" and before claim submission.
Services/frequency may not be added after physician signature. POC updated at least every
**60 days**; physician reviews/approves at least every **60 days**. Verbal orders reduced to
writing and physician-signed **within two weeks** (or per agency policy if shorter);
telephone orders signed within **14 calendar days**.

**RN supervision cadence — staffing-model relevant:**

| Case mix | RN supervisory visit |
|---|---|
| HHA only | Every **60 days** |
| SN / PT / OT alongside HHA | Every **2 weeks** |
| PT / OT only alongside HHA | The therapist may substitute for the RN |

The supervisory visit must occur **while the aide is delivering care** — i.e. it is a
co-scheduling constraint, not a standalone appointment.

**FFS vs MCO:** the handbook is FFS-only — "For information about managed care services,
refer to the Medicaid Managed Care Handbook. **Managed care carve-out services are
administered as fee-for-service benefits.**" Texas managed care runs **STAR, STAR+PLUS and
STAR Kids**. PDN denial logic references "the TMHP Prior Authorization Department **or
MCO**," and requires a Medical Director to attempt physician contact before an adverse
determination — a due-process step that applies in both lanes.
⚠️ **[UNVERIFIED]** The specific STAR / STAR+PLUS / STAR Kids population mapping — it lives
in the Medicaid Managed Care Handbook, not fetched.

Also verified: the **Home Health Services (Title XIX) DME/Medical Supplies Physician Order
Form** is referenced for DME and supplies bundled with professional services; the agency's
**DME NPI** must appear on the POC; incidental supplies used during a visit are bundled into
the G0299/G0300 rate.

### Michigan — no PA for the first 90 days, then a 36-visit aide cap

**[PUBLISHED]** MDHHS Medicaid Provider Manual, Home Health chapter, **version dated
2026-07-01** (2,678 pp; downloaded and searched directly — too large for standard fetch):
https://www.mdch.state.mi.us/dch-medicaid/manuals/MedicaidProviderManual.pdf

**Michigan's PA burden sits on the home health aide, not on skilled nursing:**

> "Home health aide services for Medicaid beneficiaries must be authorized by the **MDHHS
> Program Review Division after the initial 90 days, and every 90 days thereafter** if
> continued services are deemed medically necessary."

**So the first 90 days of aide service need no PA.** After that: "home health aide services
may be provided up to a maximum of **36 visits within 90 consecutive calendar days**."
Beyond 36 visits per 90 days, the request is reviewed for medical appropriateness, the
availability of family or another entity (**Home Help Program** or **MI Choice Waiver**), and
the cost-effectiveness of alternatives.

**PA is required each time services are requested for:** continuation beyond the initial 90
days; renewal beyond the current authorization end date; an **increase** in services; **or a
decrease in services.** *(Requiring PA for a decrease is unusual and easy to miss.)*

**What the window starts from:** the initial 90 days runs from **when services were first
provided** — corroborated by the documentation rule: "The **anniversary date is the date 12
months from the date services were first provided**," at which point full documentation must
be resubmitted.

**Renewal timing — a hard operational deadline:** the renewal MSA-181 "must be received by
the Program Review Division **no less than 15 business days before the end of the current
authorization period**. Failure to do so may result in a delay of authorization … which, in
turn, may result in delayed services or **no payment for services rendered without
authorization**."

**Ordering-authority ladder:** the **first** PA must be ordered by a physician; continuation
beyond the initial 90 days must be ordered by a **physician**; renewals, increases and
decreases may be ordered by a physician **or NPP**.

**Documentation with every initial MSA-181:** face-to-face encounter documentation; all POC
components per 42 CFR § 484; **OASIS**; plus anything else MDHHS requests. The same package
again at 12-month intervals.

**PA decision timeframes — new subsection added 2026-07-01 per bulletin MMP 26-02:**
standard PA determinations "in no case later than **seven calendar days**" after MDHHS
receives the request, extendable by up to **14 calendar days**. ⚠️ **STALE-RISK — brand new,
and note it mirrors the federal managed-care ceiling in §6.0.2.**

**Codes** (identical G-code set to Indiana), all EVV-required: G0151 PT, G0152 OT, G0153
Speech, G0156 HHA, G0299 RN, G0300 LPN.
**EVV exclusions: hospice, DME, and — significantly — "HHCS visits for beneficiaries who are
dually enrolled with Medicare and Medicaid are excluded from EVV requirements."** That is a
state-specific carve-out that cuts against the general dual-eligible EVV asymmetry in §7.5.

⚠️ **[UNVERIFIED]** Whether home health is carved into Michigan's Medicaid Health Plans
(MHPs) or retained FFS. The PA text above describes the MDHHS Program Review Division path,
which is the FFS path. Michigan splits between FFS (billed through **CHAMPS**) and MHPs,
with **ICOs / HIDE SNPs** for duals (revised per bulletin MMP 25-47); MI Choice Waiver is the
separate HCBS lane. **Confirm carve-in status before building.**

⚠️ **[UNVERIFIED]** Michigan skilled nursing and PT/OT/ST **visit caps** under the home
health benefit. The aide limits are confirmed precisely; no corresponding SN or therapy cap
was located in the Home Health chapter. **Do not import Michigan's outpatient/habilitative
therapy caps** (144 fifteen-minute units per calendar year PT/OT, 36 visits/year speech,
Healthy Michigan Plan chapter) — that is a different benefit.

### Florida — a per-day visit cap, a QIO, and the only published MCO parity floor

**[PUBLISHED]** Fla. Admin. Code **59G-4.130, "Home Health Visit Services," effective
2024-10-01** — https://www.flrules.org/gateway/ruleNo.asp?id=59G-4.130 — incorporating by
reference the **Florida Medicaid Home Health Visit Services Coverage Policy, September 2024**
(Ref-16937, adopted 2024-08-09):
https://www.flrules.org/gateway/readRefFile.asp?refId=16937&filename=59G-4.130%20Home%20Health%20Visit%20Services%20Coverage%20Policy_FINAL.pdf

| Population | Intermittent home health visits per day |
|---|---|
| Recipients **under 21** | **Up to 4** |
| **Pregnant** recipients 21+ | **Up to 4** |
| **Non-pregnant** recipients 21+ | **Up to 3** |

"Home health visits" in Florida means **skilled nursing and home health aide services
only** — PT/OT/ST are not in this policy, and PDN, personal care and family home health aide
are separate coverage policies.

**Authorization — a distinct third model: neither the state nor the plan, but a vendor.**

> "Providers must obtain authorization from the **Medicaid-contracted Quality Improvement
> Organization (QIO) every 60 days**, or more frequently, if there is a change in the
> recipient's condition requiring an increase or decrease in authorized services."

A **60-day recurring cycle** applicable to the fee-for-service delivery system. EPSDT
override: recipients under 21 may exceed the stated limits when medically necessary "to
correct or ameliorate" a condition.

**The most important MCO rule found anywhere in this research — Florida states the FFS/MCO
relationship as a floor, not a ceiling:**

> "Florida Medicaid managed care plans must comply with the coverage requirements outlined
> in this policy, unless otherwise specified in the AHCA contract … The provision of
> services to recipients enrolled in a Florida Medicaid managed care plan **must not be
> subject to more stringent coverage limits than specified in Florida Medicaid policies**."

That is a directly citable constraint: an SMMC plan may be *more* generous than 3–4
visits/day, never less. Contrast with Ohio and Indiana, where the state rule governs FFS and
plan rules govern plan members with no published parity floor in the rule text.

**Non-covered, with scheduling implications:** "**Services rendered prior to the development
and approval of the POC**" are not covered. **Florida is the strict opposite of Texas's
deliver-from-SOC posture.** Also excluded: travel time to and from the residence, physician
certification of the POC, babysitting, homework help, pet care, yard work, and services
duplicating those of a residential/assisted living facility or PPEC.

**Independent RN/LPN carve-out:** Florida covers skilled nursing by an independent RN/LPN
under 42 CFR 440.70(b)(1) **only when no home health agency is available in the area**, with
physician direction and availability to consult.

⚠️ **[UNVERIFIED]** The 2025 SMMC re-procurement plan roster and regional assignments.
**Confirm the current SMMC plan/region map with AHCA before use.**

### Cross-state comparison — the axes that actually differ

| | Indiana | Ohio | Texas | Michigan | Florida |
|---|---|---|---|---|---|
| **PA posture** | PA on everything | PA above 14 hr/wk | PA on all SN/HHA, but **deliver first** | **No PA first 90 days** (aide) | QIO auth every 60 days |
| **Cap type** | Hours/day guidance tiers | Hours/day + hours/week | Visit-shape (3 × 2.5 hr) | Visits per 90 days (aide) | **Visits per day** |
| **Cap value** | 3–16 hr/day tiers | 8 hr/day; 14 hr/wk | <8 hr/day, ≤7.5 hr continuous | 36 visits / 90 days | 3–4 visits/day |
| **Therapy allowance** | **Combined/pooled** (30 units) | **Excluded from weekly cap** | Separate handbook | Not verified | Separate policy |
| **Post-acute window** | 30 days, **discharge = day 1** | 60 days from **discharge to residence** | n/a ("acute" = 60 days) | n/a | n/a |
| **Recurring cycle** | POC review q60d | — | POC q60d | **PA q90d** | **Auth q60d** |
| **Window anchor** | Discharge date / start of care | Discharge date / start of care | **SOC date** | **Date services first provided** | Auth date |
| **Authorizing body** | **Acentra Health** (FFS) | ODM or designee / MCO | TMHP or MCO | **MDHHS Program Review Division** | **Contracted QIO** |
| **Retro posture** | None published | Emergency PDN only, w/ existing PA | 3 business days before receipt | None — no payment w/o auth | **POC must precede service** |

**Five states, five different authorizing bodies, five different cap *types*, and five
different clock anchors.** There is no shared abstraction here beyond "an authorization has
a start, an end, and a quantity." Everything above that has to be state configuration.

---

## 5.4 HCBS waiver vs state plan — concrete state evidence

§5.0.2 established the federal definition. This section shows the distinction operating in
real state documents.

**Note on sourcing:** medicaid.gov's HCBS authorities page returns HTTP 403 and blocks
automated fetching. However, **42 CFR § 440.70 and § 440.180 were fetched directly from the
eCFR API** for §5.0 above, so the federal definitions in this file are primary-sourced. The
1915(c)/(i)/(k) *program-design* framing below (statewideness, comparability, cost
neutrality, LOC tests) is **[UNVERIFIED — standard framing]**, not fetched from CMS this
pass. State documents citing 42 CFR 440.70 are verified: Indiana ("In accordance with Code of
Federal Regulations 42 CFR 440.70, the Indiana Health Coverage Programs defines 'home health
services' as services provided on a **part-time and intermittent basis** to Medicaid members
of **any age**") and Florida ("Home health services are authorized by … Section 1861(m) of
the Social Security Act; Title 42 CFR section 440.70; Section 409.905, F.S.").

### Eight operational differences, each grounded in a fetched document

**1. Different authorizing artifact.** State plan = a **prior authorization for a quantity of
units/visits** issued by a UM entity (Acentra in Indiana; ODM or designee in Ohio; TMHP in
Texas; MDHHS Program Review in Michigan; a QIO in Florida). Waiver = a **person-centered
services plan (PCSP)** maintained by a case manager. **[PUBLISHED]** OAC 5160-46-04
(**effective 2025-09-22**) — https://codes.ohio.gov/ohio-administrative-code/rule-5160-46-04 —
is explicit: Ohio Home Care Waiver personal care aide services must be delivered "in
accordance with the individual's PCSP," and specifically "**do not include services performed
in excess of the number of hours approved pursuant to the PCSP**."

**There is no PA number; the PCSP *is* the authorization.** A data model keyed to
`authorization_number + units_approved + valid_from/valid_to` cannot represent a PCSP line
item, and vice versa.

**2. Different renderer licensure.** State plan home health requires licensed clinicians —
Indiana enumerates RNs, LPNs, home health aides, PTs, OTs, SLPs; Ohio 5160-12-01 defines home
health nursing as requiring "the skills of and … performed by a registered nurse, or a
licensed practical nurse at the direction of a registered nurse," with RN-only tasks (IV
insertion, IV medications, pump programming, infusion initiation, central line dressing
changes, blood product administration). Waiver personal care aide services under 5160-46-04
may be rendered by "**non-agency personal care aides**" — **unlicensed, and not necessarily
attached to any agency.** Credentialing, competency tracking and scope-of-practice validation
are structurally different objects.

**3. Different clinical purpose — and an explicit prohibition.** Ohio 5160-12-01 bars state
plan home health from providing "habilitative care, or respite care," and bars skilled
therapies from supporting "**maintenance care**, habilitative care or respite care" — where
maintenance care is "the care given to an individual for the prevention of deteriorating or
worsening medical conditions or the management of stabilized chronic diseases or
conditions." **Maintenance and habilitation are precisely what waivers fund.** The two
benefits are definitionally non-overlapping in intent.

**4. Payer-of-last-resort ordering.** Waiver enrollment requires at least one monthly waiver
service "**otherwise unavailable through another source (including private pay, community
resources and/or the medicaid state plan)**." *(From a search summary of OAC 5160-46-02 —
⚠️ not directly fetched.)* Operationally: **the state plan benefit must be exhausted first**,
and the waiver fills the gap. A scheduling platform must model *both* concurrently for the
same patient with correct precedence — **not as alternative payers.**

**5. Different documentation.** State plan: skilled nursing note + physician-signed plan of
care reviewed **every 60 days** + **face-to-face encounter** + **OASIS** (Indiana requires
"data items from the current version of the Start-of-Care Outcome and Assessment Information
Set (OASIS)" per 42 CFR 484.55(c); Michigan requires OASIS with every initial MSA-181).
Waiver: task-based attendant logs against PCSP-approved hours. Different retention
obligations, different audit exposure.

**6. Different billing rails — stated outright.** Indiana's module carries an explicit
boundary notice: "**These billing instructions do not apply to home-based services provided
through an HCBS waiver program. See the Home- and Community-Based Services Billing Guidelines
module for information about billing HCBS waiver services.**" Different module, different
guidelines, different rails — from the same agency, for the same patient, in the same house,
potentially on the same day.

**7. Different rate structure.** State plan skilled home health is per-visit or per-hour with
an overhead add-on (Indiana: occurrence code 73, one unit per provider per member per day;
Ohio: base rate + 15-minute increments). Waiver attendant services are per-15-minute-unit
against a PCSP allotment. Different rate tables, different unit math, different rounding.

**8. They collide on the schedule — and states legislate the collision.** This is the
strongest available proof that the two benefits are distinct objects:

- **Ohio requires a 2-hour separation "when HCBS waiver services overlap with home health/PDN
  services having the same scope"** (5160-12-04).
- **Indiana** requires the PA request to list "all other supportive services and therapies the
  member is receiving, including … **Medicaid HCBS waiver services, such as Structured Family
  Caregiving and Attendant Care**."
- **Ohio's paragraph (H)** grants *increased* state plan limits partly **on the basis of HCBS
  waiver enrollment.**
- **Michigan** routes aide-service PA decisions through an assessment of "the availability of
  the family or another entity (e.g., **Home Help Program or MI Choice Waiver**)."

**A scheduling platform must hold both authorization types simultaneously for one patient and
enforce inter-benefit temporal rules between them.** That is the decisive argument against a
single shared authorization model.

### Concrete state examples

**Ohio — verified.** State plan home health lives in **OAC Chapter 5160-12** ("Ohio Medicaid
State Plan Home Health and Nursing Services"). The **Ohio Home Care Waiver** lives in **OAC
Chapters 5160-44, 5160-45 and 5160-46**, administered by **ODM** for people **aged 0–59 with
physical disabilities**. **PASSPORT** is administered separately through the **Ohio Department
of Aging / Area Agencies on Aging** (OAC 5160-31 series). Different chapters, different
agencies, different case management, different services — for the same underlying activity in
the same home. Ohio even bridges them with parallel rules: RN consultation is required by
**5160-12-08** for state plan home health nursing, **5160-12-02** for PDN, and **5160-46-04**
for *waiver* nursing — three separate rules for one clinical function, one per benefit lane.
⚠️ *The Ohio Home Care Waiver / PASSPORT administrative split is from search summaries; only
5160-46-04 was directly fetched.*

**Indiana — partially verified.** **PathWays for Aging is confirmed live** as managed LTSS for
65+ (Anthem, Humana, UnitedHealthcare), with its own enrollment broker and PA lines. The home
health module names specific waiver services — **Structured Family Caregiving** and
**Attendant Care** — that must be disclosed on a state plan PA request. Notably, **module
version 8.1 (2026-03-10) removed the section "Coordinating Home Health Services With
Attendant Care and Structured Family Caregiving for HCBS Waiver Members,"** indicating this
coordination guidance is actively in flux. Indiana also lists **CHOICE** (Community and Home
Option to Institutional Care for the Elderly and Disabled) as a separate **non-Medicaid**
program that must be accounted for in hour determinations.

⚠️ **[UNVERIFIED — material open question]** The current 1915(c) status of Indiana's **Aged &
Disabled waiver** — specifically whether A&D survives as a standalone waiver, was renamed, or
was folded into PathWays managed LTSS as of 2026. **Confirm with FSSA before modeling Indiana
waiver authorizations.**

---

# Part 6 — Medicaid MCO authorization mechanics

## 6.0 The federal floor — 42 CFR Part 438

State-by-state MCO detail is in Part 6b. But the federal managed-care rule sets a floor
that constrains every state and every MCO, and it changed materially for 2026. Read this
first; it answers most "can the MCO do that?" questions.

**[PUBLISHED]** eCFR, 42 CFR § 438.210 "Coverage and authorization of services," current
text retrieved 2026-08-18: https://www.ecfr.gov/current/title-42/section-438.210

### 6.0.1 An MCO may not be stingier than FFS on amount, duration and scope

> § 438.210(a)(2) — services must be "furnished in an amount, duration, and scope that is
> **no less than** the amount, duration, and scope for the same services furnished to
> beneficiaries under FFS Medicaid, as set forth in § 440.230."

And on medical necessity, § 438.210(a)(5)(i) requires the MCO's definition to be

> "**no more restrictive** than that used in the State Medicaid program, **including
> quantitative and non-quantitative treatment limits**, as indicated in State statutes and
> regulations, the State Plan, and other State policy and procedures."

**So: a state's FFS home health visit cap is a floor, not a ceiling, for its MCOs.** An MCO
in Indiana or Ohio cannot cover fewer skilled nursing visits than the state plan allows.
It *can* cover more, and several do as a competitive differentiator.

**What the MCO *can* do differently** is the process: § 438.210(a)(4)(ii) permits limits
"for the purpose of utilization control." That is where the divergence actually lives —
**different PA thresholds, different submission portals, different documentation, different
reauthorization cadence, different vendors.** The *benefit* converges; the *paperwork*
diverges. For a scheduling platform, the paperwork is the thing that has to be modeled.

### 6.0.2 The 2026 turnaround-time change — this is the headline

**[PUBLISHED]** § 438.210(d)(1)(i):

| Decision type | Rating periods starting **before** Jan 1, 2026 | Rating periods starting **on or after Jan 1, 2026** |
|---|---|---|
| Standard authorization | State timeframe, **not to exceed 14 calendar days** | State timeframe, **not to exceed 7 calendar days** |
| Extension | Up to **14 additional calendar days**, on enrollee/provider request or justified need for information | Same |
| Expedited (life/health/function at risk) | **72 hours**, extendable up to 14 calendar days | Same |

⚠️ **STALE-RISK / high value:** the standard-decision ceiling **halved from 14 to 7 calendar
days** for rating periods beginning on or after **January 1, 2026**. This is a federal
change, so it hits every Medicaid MCO in every state as each state's rating period rolls
over. States may set *shorter* timeframes; the regulation only sets the ceiling. A
scheduling platform's "expected auth turnaround" default should be re-pulled state by
state during 2026 because many state contracts are mid-transition.

Note also § 438.210(d)(2)(i): the expedited path triggers when **"a provider indicates, or
the MCO… determines"** that the standard timeframe could seriously jeopardize life, health,
or "ability to attain, maintain, or regain maximum function." **Under Medicaid managed care
the provider can invoke expedited review** — unlike the Anthem/Carelon Medicare Advantage
form (§1.4), where only the member, member representative or physician may request an
expedited organization determination.

### 6.0.3 LTSS and chronic-condition cases get special protection

- § 438.210(a)(4)(ii)(B): services "supporting individuals with ongoing or chronic
  conditions or who require long-term services and supports **are authorized in a manner
  that reflects the enrollee's ongoing need** for such services and supports." This is the
  anti-churn provision — the regulatory hook to argue against 30-day reauthorization cycles
  on a stable long-term case.
- § 438.210(b)(2)(iii): the MCO must "**authorize LTSS based on an enrollee's current needs
  assessment and consistent with the person-centered service plan**." For waiver/LTSS
  hours, the authorizing artifact is the person-centered service plan, not a clinical PA
  packet — the § 440.180 vs § 440.70 split from §5.0.3 reappears here at the MCO level.
- § 438.210(b)(3): a denial or a partial approval ("less than requested") must be made by
  someone with "appropriate expertise." A partial approval — 6 visits when 12 were
  requested — is legally an **adverse benefit determination** with full notice and appeal
  rights, and it is the single most common outcome a scheduler has to react to.

### 6.0.4 Transition of care — the plan-switch problem

**[PUBLISHED]** eCFR, 42 CFR § 438.62 "Continued services to enrollees," retrieved
2026-08-18: https://www.ecfr.gov/current/title-42/section-438.62

Every state must have a transition-of-care policy covering FFS→MCO and MCO→MCO moves,
and it must ensure:

> "(i) The enrollee has access to services consistent with the access they previously had,
> and **is permitted to retain their current provider for a period of time if that provider
> is not in the MCO, PIHP or PAHP network**."

Plus: referral to in-network providers, timely transfer of **historical utilization data**
from the old plan to the new one, and medical record access for new providers. The state
must **make the transition-of-care policy publicly available** (§ 438.62(b)(3)) and describe
it in the quality strategy under § 438.340.

**Operational reading:** when a Medicaid patient's plan changes mid-episode — which happens
constantly at annual open enrollment and on eligibility redetermination — the agency is
*not* automatically out of network and the visits are *not* automatically unpayable. There
is a published, state-specific continuity window. **Find each state's transition-of-care
policy document; it is required to be public.** This is one of the highest-leverage
artifacts for a scheduling platform serving Medicaid, and it is routinely ignored.

### 6.0.5 Dual-eligible cross-reference

**[PUBLISHED]** § 438.210(c) carves out integrated plans: for "Medicaid contracts with an
applicable integrated plan, as defined in § 422.561," the standard Medicaid
adverse-benefit-determination notice rules are replaced by the **integrated** rules at
**42 CFR §§ 422.629 through 422.634**, for "determinations affecting dually eligible
individuals who are also enrolled in a dual eligible special needs plan with **exclusively
aligned enrollment**."

That single sentence is the legal seam between Part 6 and Part 7: in an exclusively-aligned
D-SNP the Medicare and Medicaid authorization/appeal machinery is **merged**; in any other
dual arrangement it is **not**, and the patient has two authorizers with two clocks and two
notice regimes.

## 6.1 Retroactive authorization — one fully published MCO policy

**[PUBLISHED]** CareSource Ohio, *Retro Authorization Submission Guidelines*, notice date
**2022-03-15**, document ID OH-Multi-P-1208632, fetched and parsed in full:
https://www.caresource.com/documents/oh-multi-p-1208632-retro-authorization-submission-guidelines-network-notification_final.pdf
⚠️ **STALE-RISK — this is the oldest document cited in the Medicaid sections. Re-verify.**

**The window:**

> "CareSource shall permit retrospective review **within 30 days of the date of service, date
> of discharge, or retrospective enrollment** where a prior authorization was required but
> not obtained, often known as retro authorization. In these instances, the member's medical
> record is reviewed, and a decision is rendered **within thirty (30) calendar days** of
> receiving all information reasonably necessary to make a determination."

**The seven qualifying circumstances** — a retro request outside these is not processed:

1. The member cannot say which plan they are enrolled in because they are **unresponsive or
   incapacitated**.
2. The member is **retrospectively enrolled** covering the date of service.
3. An **urgent** service was performed and delay to obtain authorization would have been **to
   the member's detriment**.
4. The new service **was not known to be needed** at the time the originally authorized
   service was performed.
5. The need for the new service was **revealed during** the originally authorized service.
6. The service was **directly related to another already-authorized and already-performed**
   service.
7. For a **dual-eligible** member, the provider is notified that **Medicare benefits have been
   exhausted after delivery** of service.

**Will an MCO pay for visits delivered before authorization is granted?** Per this policy:
**no, by default.** "Submitting a claim for a service or provider requiring an authorization
without there being an authorization on file, **will result in a claim denial**." And
critically: "**Retroactive eligibility does not eliminate the need for medical necessity
review**" — being retro-enrolled gets you a review, not a payment.

**Circumstances 4, 5 and 6 are the operationally significant ones for home health.** A
mid-episode change in condition that generates a new service need has a legitimate retro
path — but it must be filed **within 30 days of the date of service** and must reference "the
authorization number of the previously authorized service that the request is related to."

**Product implication:** a scheduling system that surfaces "unauthorized visit delivered"
alerts on a **30-day clock, with the prior authorization number already attached**, captures
most of the recoverable revenue here. An alert without the prior auth number is not
actionable.

Submission: Provider Portal or fax. Ohio Medicaid outpatient retro fax **888-752-0012**; Ohio
MA / D-SNP / MyCare outpatient and inpatient **844-417-6157**.

**Note circumstance 7** — it is a dual-eligible-specific retro path triggered by *Medicare
benefit exhaustion discovered after the fact*. That is precisely the "discharge cliff"
scenario in §7.6, and it confirms plans have machinery for it. Use it.

## 6.2 How MCO rules diverge from state FFS rules in the same state

The federal floor (§6.0.1) says an MCO cannot be **stingier on amount, duration and scope**
than FFS. What states actually publish about the relationship varies a great deal:

| State | Published FFS/MCO relationship |
|---|---|
| **Florida** | **Explicit parity floor.** SMMC plans "must not be subject to more stringent coverage limits than specified in Florida Medicaid policies." Directly citable when a plan applies a tighter cap than 3–4 visits/day. |
| **Ohio** | **Routing only, no published floor.** OAC 5160-12-01(F)(6) simply directs members to "the individual's managed care plan." |
| **Indiana** | **Explicit disclaimer of applicability.** The module "applies to IHCP services provided under the fee-for-service (FFS) delivery system," and specific policies carry warnings such as "This policy applies to FFS coverage; **policies may vary for managed care members**." |
| **Texas** | **Shared due-process rule.** PDN adverse determinations require the Medical Director to contact the treating physician first, applied to "the TMHP Prior Authorization Department **or MCO**." |
| **Ohio (structural)** | **Administrative convergence via Next Gen** — centralized credentialing and the Gainwell SPBM make the administrative surface increasingly uniform even where clinical UM criteria diverge per plan. ⚠️ **[SEARCH-VERIFIED]** |

**The pattern:** the *benefit* converges (federal floor + occasional state parity floor); the
*process* diverges freely. Divergence lives in PA thresholds, submission portals, required
documentation, reauthorization cadence, and vendor delegation — all of which are exactly what
a scheduling platform has to model.

**Never treat a state FFS manual as authoritative for an MCO member.** Indiana and Texas both
open their manuals with that disclaimer.

## 6.3 Pending / provisional authorization

**[PUBLISHED] The clearest instance of mandated delivery under a pending authorization is a
state FFS rule, not an MCO rule.** Texas: "**During the authorization process, providers are
required to deliver the requested services from the SOC date**" — for both SN/HHA and PDN.
The provider carries the risk during the 3-business-day filing window; if the filing slips,
authorization backdates only 3 business days before receipt (§5.3).

**Florida is the opposite pole** — "Services rendered prior to the development and approval
of the POC" are not covered.

**[PUBLISHED]** Ohio contemplates retroactive authorization for **emergency PDN** only, and
only when "the provider has an existing prior authorization to provide PDN to the
individual." **No cold-start retro path.**

⚠️ **[UNVERIFIED — industry pattern]** Provisional or pended authorization as a general MCO
construct. Common practice is that plans issue a pended or provisional authorization while
clinical review runs, and that a start-of-care may proceed against it — but no specific plan
policy document was verified. **Do not build a "provisional auth" state into the data model
as though it has uniform payment semantics.** Model it as: authorization request submitted,
decision pending, visits delivered at risk — and surface the risk.

## 6.4 Transition of care when a member switches plans

**The federal requirement is established and citable** (§6.0.4, 42 CFR § 438.62): every state
must have a transition-of-care policy, it must permit the enrollee "to retain their current
provider for a period of time if that provider is not in the MCO … network," and **the state
must make that policy publicly available.**

⚠️ **[UNVERIFIED — the day count]** No specific transition period was verified in this
research pass. The CareSource Ohio Medicaid Provider Manual (112 pp) was fetched and searched
— https://www.caresource.com/documents/oh-provider-manual.pdf — and **its continuity-of-care
language is about care coordination between providers, not about honoring a prior plan's
authorization after a plan switch.** No transition-of-care period, no day count, and no
honor-the-prior-auth provision was found in the sections retrieved.

**[UNVERIFIED — industry pattern]** Medicaid managed care contracts typically require a new
plan to honor an existing authorization and allow continued use of an out-of-network provider
for a transition period commonly in the **30–90 day** range (often 90 days, or until the
member is reassessed), with additional protections for members in an active course of
treatment. **Do not build to a specific number.**

**Where the number actually lives: the state's MCO contract, not the plan's provider manual.**
For Ohio that is the ODM provider agreement; for Indiana the FSSA MCE contract. And under
§ 438.62(b)(3) the state's transition-of-care policy **must be public** — so the number is
obtainable. **This is the highest-value unresolved item in the Medicaid research.**

**One verified adjacent data point:** CareSource Ohio's retro-authorization policy treats "the
member is retrospectively enrolled and covers the date of service" as a qualifying retro
circumstance — the enrollment-gap analogue of a transition problem, confirming plans do have
machinery for authorizations that predate their own coverage.

---

# Part 7 — Dual-eligible members

## 7.0 The federal backbone — who authorizes depends on the integration tier

*(Practical Medicare-primary / Medicaid-secondary mechanics are in §7.1 onward. This
section establishes the definitional tiers first, because "dual eligible" is not one
operating model — it is at least four, and they differ in exactly the way a scheduler cares
about: how many authorizing entities the patient has.)*

**[PUBLISHED]** eCFR, 42 CFR § 422.2 (definitions), retrieved 2026-08-18:
https://www.ecfr.gov/current/title-42/section-422.2

**[PUBLISHED]** eCFR, 42 CFR § 422.561 (definition of "applicable integrated plan"),
retrieved 2026-08-18: https://www.ecfr.gov/current/title-42/section-422.561

### 7.0.1 The tiers

**D-SNP** — "a specialized MA plan for special needs individuals who are entitled to
medical assistance under a State plan under title XIX." A D-SNP must have a contract with
the State Medicaid agency under § 422.107 and, since Jan 1, 2021, must satisfy at least one
integration criterion: the § 422.107(d) coordination-only requirement, **or** be a HIDE SNP,
**or** be a FIDE SNP.

**Coordination-only D-SNP** (meets § 422.107(d) but is neither HIDE nor FIDE) — the plan
coordinates but **does not hold the Medicaid capitation for the services in question**.
The member's Medicaid benefits are authorized by a *different* entity — the state FFS
program or a separate Medicaid MCO. **Two authorizers.**

**HIDE SNP** — Medicaid benefits are covered under a capitated contract held by the MA
organization, its parent, or an affiliate. The capitated contract must cover **LTSS
(including community-based LTSS and some nursing facility days) *or* behavioral health**.
For plan year 2025 and later the contract must cover the D-SNP's entire service area.
**Note what is *not* required: home health.** A HIDE SNP may still leave the Medicaid home
health benefit outside the plan.

**FIDE SNP** — the strongest integration, and the one that changes the operating model.
Per § 422.2, a FIDE SNP provides Medicare and Medicaid benefits "under a **single entity**
that holds both an MA contract with CMS and a Medicaid managed care organization contract
under section 1903(m)," and its capitated contract with the state must cover:

- primary and acute care, and (for plan year 2025+) Medicare cost sharing;
- **LTSS, including nursing facility services for at least 180 days during the plan year**;
- (PY2025+) behavioral health services;
- **(PY2025+) home health services *as defined in 42 CFR § 440.70***; and
- (PY2025+) medical supplies, equipment and appliances as described in § 440.70(b)(3).

Plus: aligned care management, CMS/State-approved integrated communications, enrollment,
grievance and appeals and quality processes; **exclusively aligned enrollment** (PY2025+);
and full service-area coverage (PY2025+).

**This is the single most important dual-eligible fact for a home health scheduler:** from
plan year 2025 onward, a **FIDE SNP must hold the Medicaid § 440.70 home health benefit
under the same capitation as the Medicare benefit.** In a FIDE SNP, **one entity authorizes
both the Medicare home health episode and the Medicaid home health/aide services.** In a
HIDE SNP or a coordination-only D-SNP, it generally does not.

### 7.0.2 Exclusively aligned enrollment and "applicable integrated plan"

**[PUBLISHED]** § 422.2: "When State policy limits a D-SNP's membership to individuals with
aligned enrollment, this condition is referred to as **exclusively aligned enrollment**."
I.e. the member's Medicaid managed care plan and their D-SNP are the same organization,
by state rule.

**[PUBLISHED]** § 422.561, "Applicable integrated plan," on or after January 1, 2023, means
either:
1. a **FIDE SNP or HIDE SNP with exclusively aligned enrollment**, together with the
   Medicaid MCO through which it covers Medicaid services; **or**
2. a D-SNP and affiliated Medicaid managed care plan where state policy limits D-SNP
   enrollment to beneficiaries in that Medicaid MCO and a capitated contract links them.

When a plan is an **applicable integrated plan**, § 438.210(c) replaces the standard
Medicaid adverse-benefit-determination notice rules with the **integrated** rules at
42 CFR §§ 422.629–422.634. Practically: **one integrated organization determination, one
integrated notice, one integrated appeal** instead of parallel Medicare and Medicaid
tracks.

### 7.0.3 What this means at the schedule level

| Arrangement | Who authorizes the Medicare HH episode | Who authorizes Medicaid aide / LTSS hours | Auth objects on the schedule |
|---|---|---|---|
| Original Medicare + Medicaid FFS | Medicare (no PA in most states; review contractors) | State Medicaid agency / waiver case manager | **2**, different clocks |
| Original Medicare + Medicaid MCO | Medicare | Medicaid MCO (42 CFR 438 timeframes) | **2**, different clocks |
| Coordination-only D-SNP | The D-SNP (MA rules) | Separate Medicaid entity | **2**, different clocks |
| HIDE SNP | The D-SNP | The affiliated Medicaid MCO (may or may not include home health) | **2**, sometimes 1 |
| **FIDE SNP (PY2025+)** | The FIDE SNP | **The same FIDE SNP** — § 440.70 home health is inside the capitation | **1** |
| Applicable integrated plan | Integrated determination under §§ 422.629–422.634 | Same | **1**, integrated notice/appeal |

**[PATTERN]** The operational trap: staff assume "dual eligible" means one payer and one
auth. In every arrangement except a FIDE SNP / applicable integrated plan, the patient
carries **two independent authorizations with different unit counts, different periods,
different renewal dates, different documentation and — where the state requires EVV for the
Medicaid personal-care/aide hours but not for the Medicare skilled visits — different
visit-capture requirements on the same day, in the same home.** A scheduling platform that
models one auth per patient per payer will silently under-schedule or over-schedule duals.

## 7.1 Who pays — and the counterintuitive answer for home health

**[PUBLISHED]** Medicaid is payer of last resort. Medicaid.gov: "By law, all other available
third party resources must meet their legal obligation to pay claims before the Medicaid
program pays for the care of an individual eligible for Medicaid" —
https://www.medicaid.gov/medicaid/eligibility-policy/coordination-of-benefits-third-party-liability
(retrieved 2026-08-18). For a dual with a skilled need, the agency bills Medicare (or the
MA / D-SNP plan) first, always.

**[PUBLISHED]** Medicare home health has **no beneficiary cost sharing**. Medicare.gov, Home
health services: "**You pay nothing for covered home health services**" —
https://www.medicare.gov/coverage/home-health-services (retrieved 2026-08-18). The one
exception is DME furnished under the plan of care: 20% Part B coinsurance after the
deductible.

**The consequence most agencies get wrong: there is essentially nothing for Medicaid to
crossover-pay on a Medicare home health claim.** Zero coinsurance, zero copay, no
deductible. The crossover claim exists and pays $0. **Medicaid's relevance to a dual's home
care is not the home health claim.** It is:
1. aide hours and personal care beyond what Medicare covers;
2. everything after the Medicare benefit ends or the patient fails Medicare's criteria; and
3. DME coinsurance.

**One real exception — Medicare Advantage.** **[PUBLISHED]** 42 CFR § 422.100(j)(1)(i)(D) —
https://www.ecfr.gov/current/title-42/section-422.100 (retrieved 2026-08-18): an MA plan's
in-network home health cost sharing may not exceed original Medicare when the plan uses the
mandatory or intermediate MOOP type — but "**when the MA plan establishes the lower MOOP
type, the cost sharing must not be greater than 20 percent coinsurance or an actuarially
equivalent copayment.**" **A dual in a lower-MOOP MA plan can have real home health
coinsurance**, and that is the one place Medicaid crossover on a home health claim actually
has something to pay — and the one place a QMB balance-billing violation can occur on a home
health claim.

## 7.2 The Medicare eligibility gate, and what happens when the patient fails it

**[PUBLISHED]** 42 CFR § 409.42 —
https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-409/subpart-E/section-409.42
(retrieved 2026-08-18): the beneficiary "must be confined to the home or in an institution
that is not a hospital, SNF or nursing facility," must be under the care of a physician or
allowed practitioner who establishes the plan of care, and must need skilled services
certified per § 424.22 (which carries the face-to-face requirement).

**[PUBLISHED]** Medicare.gov adds the exclusion that matters most: Medicare "doesn't pay
for… custodial or personal care that helps you with daily living activities… **when this is
the only care you need**," and aide care is covered "only if you're also getting skilled
nursing care, physical therapy, speech-language pathology services, or occupational therapy
at the same time."

**When the patient fails homebound or skilled need, the case does not stop — it falls to
Medicaid on a completely different legal footing.** 42 CFR § 440.70(c)(1) (see §5.0.1)
prohibits limiting Medicaid home health to homebound beneficiaries, and § 440.70 makes it a
**mandatory** state plan benefit with no skilled-need gateway for the aide component.

| | **Medicare HH** | **Medicaid HH / personal care** |
|---|---|---|
| Homebound required | **Yes** (§ 409.42(a)) | **Prohibited as a limit** (§ 440.70(c)(1)) |
| Skilled need required | **Yes** | **No** — aide / PCS stand alone |
| Aide hours standalone | No | Yes |
| Authorizing entity | MAC / HHA certification, or the MA plan | State Medicaid agency or its MCO / MLTSS plan |
| Payment unit | 30-day period (PDGM) | Per-visit / per-hour / per-unit, state fee schedule |
| Beneficiary cost sharing | $0 | $0 or nominal |
| EVV | **No federal mandate** | **Federally mandated** (§ 7.5) |

The referral pathway forks completely. **This is not a coverage downgrade — it is a
different benefit with a different authorizer.** A scheduling platform should treat
"Medicare HH denial for non-homebound" as a **routing event into the Medicaid pathway**,
not as a discharge.

## 7.3 QMB and the balance-billing prohibition

**[PUBLISHED]** CMS MLN Booklet, *Prohibition on Billing Qualified Medicare Beneficiaries*:
https://www.cms.gov/files/document/mln7936176-prohibition-billing-qualified-medicare-beneficiaries.pdf
(retrieved 2026-08-18). Verbatim:

> "Federal law prohibits all Original Medicare and MA providers and suppliers (**not only
> those that accept Medicaid**) from billing QMBs for Part A and Part B cost sharing. **Even
> if you don't receive full payment from Medicaid, you must not bill a QMB.**"

> "You're violating your Medicare provider agreement or obligations under Medicare Part C
> and may be subject to sanctions if you don't follow QMB billing prohibitions (**even when
> Medicaid pays nothing**)."

Statutory basis: Social Security Act §§ 1902(n)(3)(B), 1902(n)(3)(C), 1905(p)(3),
1866(a)(1)(A), 1848(g)(3)(A).

Operational points from the same booklet:
- **Cross-state:** "You must not charge a patient enrolled as a QMB for Medicare
  cost-sharing amounts **even if their QMB benefit is from a different state** than the
  state where they get care."
- **No waiver:** "QMBs **may not elect** to pay Medicare deductibles, coinsurance, and
  copayments." You cannot obtain consent from the patient.
- Verification channels: MAC provider portal, HETS via clearinghouse, Medicare RA / MSN,
  state Medicaid eligibility verification system.
- Unpaid amounts may be pursued as Medicare **bad debt** under 42 CFR § 413.89 — but only
  after billing the state and receiving a Medicaid remittance advice.

Because Medicare home health cost sharing is $0, **QMB exposure on the home health claim
itself is nil.** QMB risk for a home health agency is concentrated in **DME (20% Part B
coinsurance)** and in **lower-MOOP MA plans with home health coinsurance** (§7.1). Those are
exactly the places a billing system will try to auto-generate a patient statement — so the
QMB flag must suppress statement generation, not merely annotate the account.

**Not every dual has Medicaid aide benefits.** **[PUBLISHED]** CMS categorizes D-SNP-eligible
Medicaid statuses as: Full Medicaid only, **QMB Only**, **QMB Plus**, SLMB Only, SLMB Plus,
QI, QDWI — https://www.cms.gov/medicare/enrollment-renewal/special-needs-plans/dual-eligible
(retrieved 2026-08-18). **Only QMB Plus and Full Medicaid carry full Medicaid benefits** —
i.e. aide hours and post-Medicare coverage. **A QMB Only dual has cost-sharing protection
but no Medicaid aide benefit.** This single field determines whether a second authorization
even exists, and it belongs in intake.

## 7.4 D-SNP contracting and the CY2026 rule changes

**[PUBLISHED]** 42 CFR § 422.107(b) —
https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-C/section-422.107
(retrieved 2026-08-18): "MA organizations seeking to offer a dual eligible special needs
plan must have a contract consistent with this section with the State Medicaid agency."
**The State Medicaid Agency Contract (SMAC) is the instrument that determines how much of
Medicaid the plan actually controls** — and SMACs are generally not public today.

**[PUBLISHED]** § 422.107(c)(9) requires the SMAC to mandate "the use of the unified appeals
and grievance procedures under §§ 422.629 through 422.634, 438.210, 438.400, and 438.402"
for applicable integrated plans.

**Coordination-only D-SNP obligations are thin.** § 422.107(d)(1) requires the plan to notify
the state (or its designee) "of hospital and skilled nursing facility admissions for at
least one group of high-risk full-benefit dual eligible individuals." **That is
coordination, not authorization.** The Medicare home health period is authorized by the
D-SNP; the Medicaid aide hours are authorized by the state or its separate MLTSS/MCO. Two
plans, two portals, two clocks.

**HIDE SNP amendment, CY2026.** The list of entities that may hold the Medicaid capitated
contract was expanded to include "a local nonprofit public benefit corporation of which the
MA organization, MA organization's parent organization, or another entity that is owned and
controlled by its parent organization is a founding member." Finalized in the CY2026 MA/
Part D final rule (issued 2025-04-04; 42 CFR § 422.2, discussed at 90 FR 15888–15889) —
https://www.integratedcareresourcecenter.com/sites/default/files/E-alert-CY2026-MAPD-Final-Rule.pdf

**Other CY2026/CY2027 changes worth tracking** (same ICRC alert): ⚠️ **STALE-RISK**
- **CY2026:** all SNPs must conduct the **initial health risk assessment within 90 days**
  (before or after) the enrollment effective date, and develop the individualized care plan
  within 90 days of the HRA or 90 days after the enrollment effective date, whichever is
  later. **A home health referral often lands inside that window** — the plan's own care
  plan may not exist yet when the agency asks for an authorization.
- **CY2027:** applicable integrated plans must issue **integrated member ID cards** serving
  as ID for both the Medicare and Medicaid plans, and must conduct a **single integrated
  HRA** rather than separate Medicare and Medicaid HRAs. The integrated card is the first
  time the card will actually tell you the integration tier.
- CMS solicited comment on **public posting of SMACs** and reported "overwhelming support."
  Worth monitoring — SMACs are where the aide-authorization authority is written.

**Look-alike D-SNP restriction.** **[PUBLISHED]** 42 CFR § 422.514(d) —
https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-K/section-422.514
(retrieved 2026-08-18). In any state with a D-SNP, CMS will not enter into or renew a
contract for a non-SNP MA plan whose dually eligible enrollment meets or exceeds:

| Plan year | Threshold (bid projection and renewal) |
|---|---|
| 2024 | 80% |
| 2025 | 70% |
| **2026 and subsequent years** | **60%** |

Renewal exception: plans active less than one year with ≤200 enrollees. § 422.514(e) governs
transition of affected enrollees into compliant plans or D-SNPs.

**Effect on an agency:** dual-heavy non-SNP MA books are being forcibly converted, so **a
patient's plan identity — and therefore the authorization pathway — can change on January 1
with no clinical change and no patient action.** Build the January payer-refresh sweep.

## 7.5 EVV — the hard asymmetry on a dual's schedule

**[PUBLISHED]** Section 12006(a) of the 21st Century Cures Act, per Medicaid.gov:
https://www.medicaid.gov/medicaid/home-community-based-services/guidance/electronic-visit-verification-evv
(retrieved 2026-08-18) — it "mandates that states implement EVV for all Medicaid personal
care services (PCS) and home health services (HHCS) that require an in-home visit by a
provider. This applies to PCS provided under sections 1905(a)(24), 1915(c), 1915(i),
1915(j), 1915(k), and Section 1115; and HHCS provided under 1905(a)(7)." Deadlines: **PCS by
January 1, 2020; HHCS by January 1, 2023**, with incremental FMAP reductions up to 1% for
non-compliance.

**Medicare home health has no equivalent federal EVV mandate.** So the same caregiver,
entering the same house on the same afternoon, may need to clock in through a state EVV
aggregator for the Medicaid aide visit and not for the Medicare skilled visit — and the
state EVV system's data elements (service code, unit rounding, geolocation, telephony
fallback) are state-specific and do not match the Medicare visit record.

## 7.6 The modeling requirement — two concurrent, non-aligned authorizations

| Axis | Medicare / MA home health auth | Medicaid aide / PCS auth |
|---|---|---|
| **Unit of measure** | Visits within a 30-day payment period (PDGM); disciplines certified via plan of care | **Hours or 15-minute units** per week/month (S9122, T1019, T1021 and state variants) |
| **Period** | 60-day certification, 30-day payment periods | State-set span — commonly 3, 6 or 12 months; MLTSS reassessment cycles |
| **Authorizing entity** | MAC (FFS), MA plan, or D-SNP | State Medicaid agency, MLTSS/MCO — or, in a FIDE SNP, **the same plan** |
| **Homebound** | Required (§ 409.42(a)) | Cannot be required (§ 440.70(c)(1)) |
| **Recert cadence** | 60-day recert, face-to-face per § 424.22 | 60-day plan-of-care review by ordering practitioner (§ 440.70(a)(2)); separate reassessment for waiver PCS |
| **EVV** | No federal requirement | **Mandatory** |
| **At Medicare discharge** | Period ends | **Auth continues** — the aide schedule must not stop |

**Three failure modes a scheduling system must handle:**

1. **Concurrent, differently-metered auths.** A visit-count-based Medicare period running
   alongside an hours-based Medicaid auth, with independent depletion tracking and
   independent expiry dates.
2. **The discharge cliff.** The Medicare period ends; the Medicaid aide authorization is
   still live. A system that tears down the case on Medicare discharge silently lapses
   coverage the patient is still entitled to. **This is the most common and most damaging
   dual-eligible scheduling defect.**
3. **Auth-source ambiguity.** In a FIDE SNP both authorizations come from one plan — one
   portal, one number, unified appeal under § 422.107(c)(9). In a coordination-only D-SNP
   they come from two entities with two clocks and two appeal tracks. **A plan's name does
   not tell you which; the FIDE / HIDE / coordination-only designation does.** That
   designation belongs in the payer master as a stored field, not derived at runtime.

## 7.7 PACE

**[PUBLISHED]** CMS, Program of All-Inclusive Care for the Elderly —
https://www.cms.gov/medicare/medicaid-coordination/about/pace (retrieved 2026-08-18; page
last modified 2026-03-16): "PACE provides comprehensive medical and social services to
certain frail, elderly people (participants) still living in the community. **Most of the
participants who are in PACE are dually eligible** for both Medicare and Medicaid."
Regulations at 42 CFR Part 460.

For a home health agency, PACE is the maximal-integration case: the PACE organization is the
sole payer and its interdisciplinary team is the sole authorizer for everything, Medicare
and Medicaid alike. There is no episode, no crossover, and typically no fee-for-service home
health claim; the PACE organization either delivers in-home care itself or contracts for it.
**A PACE participant should never be scheduled against a Medicare home health period.**

---

# Part 8 — Staleness register and open questions

## 8.1 Figures that will go stale, ranked by speed

**Do not hardcode anything in this section. Re-pull before any release.**

### Highest volatility — verify before every release

| Figure | Value | Published | Risk |
|---|---|---|---|
| BCBSM home health vendor / network | **tango**, PA from 2026-03-01, network from 2026-03-02 | BCBSM June/July 2026 docs | Mid-transition; claims portal features still shipping |
| BCBSNC MA authorization interval | **30-day intervals**, from **2026-05-01** (moved from 2026-04-02) | BCBSNC 2026 provider news | Date already slipped once |
| Anthem/Carelon HH review period | **Standardized 30 days** from 2025-05-16 | Carelon Anthem HH page | Plan grid re-issued periodically (filename is date-stamped) |
| Cigna commercial HH code list | 11 codes, eff. **2026-03-07** | eviCore, pub. 2026-03-04 | New program; list will move |
| UHC MA home health PA | Removed 2025-04-01, **partially re-added 2026-02-01** (S9122/S9123/S9124) | UHC 2026 Summary of Changes | Reversed once in 12 months |
| BCBSTX auth letters go digital-only | Availity from 2026-07-18; **mail stops 2026-09-08** | BCBSTX 2026-06-08 news | Imminent operational break |
| Federal Medicaid MCO standard decision ceiling | **14 → 7 calendar days** for rating periods starting on/after **2026-01-01** | 42 CFR 438.210(d)(1)(i) | States rolling over on different dates through 2026 |
| Ohio Next Gen **MyCare** roster | Anthem, Buckeye, CareSource, Molina | **Launched Jan 2026** | Active transition; search-sourced |
| Ohio general MCO roster | 7 plans | Feb 2023 | Search-sourced; Aetna's role unresolved |
| Indiana FFS PA vendor | **Acentra Health** | IHCP QRG v14.1, May 2026 | Already moved Kepro → Acentra |
| Indiana PathWays MCEs | Anthem, Humana, UnitedHealthcare | IHCP QRG v14.1, May 2026 | Program still stabilizing |
| Florida SMMC plan/region map | **NOT VERIFIED** | 2025 re-procurement | Recently re-procured |
| Michigan PA decision timeframe | 7 calendar days + 14-day extension | Added **2026-07-01**, MMP 26-02 | Brand new |

### Moderate volatility — annual

| Figure | Value | Published |
|---|---|---|
| **CMS CY2026 per-visit rates** (SN $176.96 / PT $193.42 / OT $194.74 / SLP $210.25 / MSS $283.64 / HHA $80.12) | CY2026 | CMS-1828-F, FR 2025-12-02 |
| **FEP 2026 home health visit caps** (Standard **50**, Basic **25**, Blue Focus **10**) | PY2026 | OPM brochures RI 71-005, RI 71-017 |
| KFF self-funded share | **67%** of covered workers | KFF 2025 EHBS, pub. 2025-10-22 |
| Look-alike D-SNP threshold | **60%** for 2026+ | 42 CFR 422.514(d) |
| Michigan aide cap | **36 visits / 90 consecutive days** | MDHHS manual 2026-07-01 |
| Michigan renewal lead time | **15 business days** | MDHHS manual 2026-07-01 |
| Florida visit caps | **3/day adult; 4/day child & pregnant** | Policy Sept 2024; rule eff. 2024-10-01 |
| Texas PDN initial auth max | **90 days** | TMPPM March 2026 |
| Texas filing windows | **3 business days** initial / **7** recert | TMPPM March 2026 |
| Ohio home health rates (base + unit) | Not extracted | OAC 5160-12-05, eff. 2024-01-01 |
| Indiana FFS rates per procedure code | Not extracted — "FSSA sets the rate for each procedure code" | Module v8.1, policies as of 2025-04-01 |
| CareSource Ohio retro window | **30 days** | Notice **2022-03-15** — oldest doc cited |
| BCBSNC service caps | Rehab nursing 5 visits; medical gas 5 visits; postop colostomy 14 days | Policy reviewed Feb 2026 |

### Lower volatility — codified, changes on rulemaking cycles

| Figure | Value | Source |
|---|---|---|
| Medicaid home health plan-of-care review | **Every 60 days** | 42 CFR 440.70(a)(2) |
| Medicaid home health homebound prohibition | Cannot be limited to homebound | 42 CFR 440.70(c)(1) |
| Face-to-face 90-before / 30-after | 90 / 30 | 42 CFR 440.70(f); mirrored in IN, OH |
| Ohio 8 hr/day; 14 hr/wk; 4-hr visit max | 8 / 14 / 4 | OAC 5160-12-01, eff. 2021-03-07 |
| Ohio 28 hr/wk × 60 days post-discharge | 28 / 60 | OAC 5160-12-01, eff. 2021-03-07 |
| Ohio 2-hour visit separation rules | 2 hrs | OAC 5160-12-04, eff. 2021-03-07 |
| Indiana discharge exception | **120 units / 30 units in 30 days** | Module v8.1, 2026-03-10 |
| ERISA claims-procedure timeframes | 72 hrs / 15 days / 30 days | 29 CFR 2560.503-1 |
| Medicaid MCO expedited decision | **72 hours** | 42 CFR 438.210(d)(2) |
| **G-code set** (G0151/52/53/56, G0299, G0300) | codes | IN, MI, OH — **the most stable item in this research** |

### Structural caveats that outrank any single number

1. **Indiana's module is dated 2026-03-10 but its policies are current only to 2025-04-01** —
   an ~11-month lag baked into the current publication.
2. **Ohio's clinical rule (5160-12-01) is effective 2021 while its payment rule (5160-12-05)
   is effective 2024.** They drift apart.
3. **Never treat a state FFS manual as authoritative for an MCO member.**
4. **Never treat a carrier's published medical policy as authoritative for a self-funded
   member.** The plan document controls.
5. **Never treat a host plan's rules as authoritative for a BlueCard member.** The home plan's
   medical policy controls.

## 8.2 Open questions worth closing before a product spec

| # | Question | Why it matters | Where to get it |
|---|---|---|---|
| 1 | **MCO transition-of-care day counts** per state | Determines whether visits are payable after a plan switch mid-episode | State MCO contracts (ODM provider agreement, FSSA MCE contract). **Required to be public** under 42 CFR 438.62(b)(3) |
| 2 | Michigan MHP carve-in status for home health | Decides whether the MDHHS Program Review path or a plan path applies | MDHHS / MHP contracts |
| 3 | Michigan skilled nursing and therapy caps under the home health benefit | Aide caps confirmed; SN/therapy not located | MDHHS Medicaid Provider Manual, Home Health chapter |
| 4 | Indiana Aged & Disabled waiver 2026 status | Whether A&D still exists standalone or was folded into PathWays | FSSA |
| 5 | Indiana FFS authorization period length | Not published; set per-request by Acentra | IHCP Prior Authorization module, or a live PA determination letter |
| 6 | Ohio PNM module and Fiscal Intermediary mechanics | Determines where PA and claims transactions actually route | ODM directly — pages returned 404 |
| 7 | Florida SMMC plan/region map after 2025 re-procurement | Plan identity per region | AHCA |
| 8 | Whether any Aetna commercial plan requires home health precert at plan level | National list is **silent**, not negative | Plan document / SPD |
| 9 | Cigna and Aetna home health payment methodology and rates | Neither publishes | Payer contract |
| 10 | Horizon BCBSNJ current home health auth detail | horizonblue.com blocks automated fetching | Human browser session, or Horizon provider services |
| 11 | Pennsylvania (Community HealthChoices, 55 Pa. Code Ch. 1249) | Not researched — a large MLTSS state | PA DHS |
| 12 | Anthem/Carelon in-scope plan grid, current version | Determines which Anthem members need Carelon auth at all | The date-stamped XLSX on the Carelon Anthem HH page |

---

# Part 9 — What this means for a branch capacity-and-scheduling platform

This section is synthesis, not new sourcing. Everything here traces to the cited material
above.

## 9.1 The authorization object is not a scalar

The single most repeated finding across every payer type: **an authorization is a
per-discipline quantity inside a dated window, not a number.**

- **Anthem/Carelon** requests visits per discipline (SN, PT, OT, ST, HHA, MSW) inside a
  **30-day review period labelled A or B**, nested inside a separate **certification
  period** (§1.4).
- **Indiana** pools PT/OT/SLP into **one 30-unit allowance** but meters nursing and aide in
  **hours** while therapy is in **15-minute units** (§5.1).
- **Ohio** applies an **8 hr/day cap across all disciplines** and a **14 hr/week cap that
  excludes therapy** (§5.2).
- **Texas** meters against a **rolling 7-day PAN week keyed to the authorization start day**
  (§5.3).
- **Aetna commercial** counts a **4-hour block as one visit**, so an 8-hour shift consumes
  two (§4.2).

Minimum viable authorization model: `payer × program × discipline × unit_type ×
quantity × window_start × window_end × window_anchor_rule`, with an explicit
`counts_toward` mapping so a single visit can decrement more than one accumulator (Ohio's
daily-yes / weekly-no therapy treatment is the canonical case).

## 9.2 There are at least six different "what date does the clock start from" answers

| Anchor | Where |
|---|---|
| **Hospital discharge date, counted as day 1** | Indiana 30-day PA exception |
| **Discharge from hospital to residence** | Ohio 60-day enhanced period |
| **Start of care (SOC) date** | Texas PA filing windows; IN/OH face-to-face 90/30 rule |
| **Date services were first provided** | Michigan 90-day aide window and 12-month anniversary |
| **Authorization start day** | Texas rolling PAN week; Anthem 30-day review periods |
| **Calendar year** | FEP and commercial visit caps; self-funded plan maxima |

**A single `start_date` field cannot carry this.** The anchor rule has to be payer
configuration.

## 9.3 Payment model splits cleanly on one axis

| | Episodic / period-based | Per-visit or per-unit |
|---|---|---|
| **Who** | Medicare FFS (PDGM); Medicare Advantage; MA-delegated vendors (tango, Carelon); BCBSNC's MA program | All commercial: FEP, BCBS commercial, Cigna, Aetna, UHC (verified in policy 2026R5036A); all Medicaid FFS |
| **Control mechanism** | Prior authorization on 30-day periods | **Annual visit cap** + coverage policy + (sometimes) PA on shift-nursing codes |
| **What the schedule optimizes** | Visits within the period against the case-mix payment | Visits against a depleting benefit accumulator |

**These are different optimization problems.** Episodic wants the right visit mix inside a
fixed payment; per-visit wants throughput until the cap. A platform that models only one will
misprice half the book.

## 9.4 Five things the member ID card cannot tell you

1. **Whether the plan is self-funded** — 67% of covered workers are (§3.5), and the plan
   document, not the carrier policy, sets the visit cap (40 / 45 / 60 / 100 in four real
   plans, §3.6). Texas's TDI marker is the only clean card-level signal found, and it is
   state-specific (§3.2).
2. **Whose rules apply for a Blue member** — the alpha prefix identifies the home plan, but
   the home plan's medical policy has to be looked up, and the rules can be the opposite of
   the local plan's (§2).
3. **Which authorization vendor holds the case** — tango, Carelon, eviCore, CareCentrix,
   Acentra, a QIO, or the plan itself, varying by product line *within* a carrier (§1, §4).
4. **Whether a dual has one authorizer or two** — that is the FIDE / HIDE / coordination-only
   designation, and it is not printed. (Integrated ID cards arrive **CY2027** for applicable
   integrated plans, §7.4.)
5. **Whether the member has a Medicaid aide benefit at all** — QMB Only vs QMB Plus vs Full
   Medicaid (§7.3).

**Implication: intake must resolve these as stored fields, not derive them at scheduling
time.** The eligibility check is the product's most important integration, and a generic
270/271 with service type 30 will not return what is needed (§2.3).

## 9.5 The visit-spacing and co-scheduling constraints are real payment rules

Not soft preferences — unpayable claims:

- **Ohio:** 2-hour gap between consecutive same-type visits; 2-hour interval between home
  health nursing and PDN on the same day; 2-hour separation from overlapping HCBS waiver
  services; modifiers U2/U3 for 2nd and 3rd same-day visits (§5.2).
- **Texas:** RN supervisory visit **while the aide is delivering care** — a co-scheduling
  requirement, every 2 weeks when skilled services are in the mix (§5.3).
- **Anthem/Carelon and Highmark:** reauthorization packets require **SOC OASIS / ROC OASIS
  and a signed 485**, which means the schedule must produce the assessment visit before the
  reauth deadline, not after (§1.4, §1.5).
- **Horizon/CareCentrix general norm:** continuation requests **72 hours before the current
  authorization expires** (§1.8).

A router that treats these as soft constraints will generate schedules that are clinically
fine and financially wrong.

## 9.6 The three highest-value alerts to build

1. **Reauthorization due, with the packet assembled.** Every payer with a short cycle
   (Anthem/Carelon 30 days, BCBSNC MA 30 days, Michigan 90 days with a **15-business-day
   lead**, Florida QIO 60 days, Texas 7 business days on recert) fails the same way: the
   packet is late. The alert must carry the required artifacts, not just the date.
2. **Unauthorized visit delivered, within the retro window.** CareSource Ohio's 30-day retro
   window with seven qualifying circumstances (§6.1) is recoverable revenue — but only if the
   alert fires inside 30 days and carries the prior authorization number.
3. **Medicare discharge with a live Medicaid authorization.** The "discharge cliff" (§7.6) —
   the schedule must not tear down when the Medicare period ends if aide hours are still
   authorized. This is the most damaging dual-eligible defect and it is entirely preventable.
