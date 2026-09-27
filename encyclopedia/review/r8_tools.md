# r8 — tool facts review (records/tools_t1.py – tools_t4.py)

Reviewer: adversarial fact-check, 27/09/2026. All four files pass `python3 check_records.py`.
Primary source for RACE: SEC (2025) *Reasonable Accommodations at the 2026 Certificate Examinations: Instructions for Schools* (PDF, October 2025), read in full text on 27/09/2026.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| tools_t1.py | WISC-V UK | interpret[1] | GAI when scatter "more than 23 points … heuristic used in … Flanagan & Alfonso, 2017" | "23 points or more (about 1.5 SD)" attributed to Flanagan & Kaufman (2004, *Essentials of WISC-IV*), written for WISC-IV, not a WISC-V manual rule; Pearson holds FSIQ can stay valid; GAI helps only when scatter comes from WMI/PSI; confirm service practice | Wrong attribution and wrong boundary (the original rule is ≥23). Heuristic now hedged |
| tools_t1.py | WISC-V UK | before[1] | practice effects "especially on Processing Speed and Visual Spatial" | "larger on some indices than others — check the retest gains by index in the technical manual" | Unverified index-specific claim, now hedged |
| tools_t1.py | WPPSI-IV UK | before[1] | "a Full Scale IQ with all five primary indices is available only in the older band" | both bands give FSIQ; younger band has 3 primary indices (VCI, VSI, WMI); all 5 only at 4:0–7:7 | The old wording read as if the younger band had no FSIQ |
| tools_t1.py | CELF-5 UK | before[1] | indexes "… language content and language structure (and language memory for older ages)" | Receptive, Expressive, Language Content; Language Structure at 5–8, Language Memory at 9–21 | Language Structure is not given at 9–21 (Pearson CELF-5 record forms 5–8 / 9–21) |
| tools_t2.py | RCADS | administer[2] | "a report to Tusla where there is a child protection concern" | "…to Tusla as soon as practicable where…" | Safety wording from the brief (Children First Act 2015) |
| tools_t3.py | Renfrew | before[2] | "Age 3:0–8:11 … (tool catalogue)" | catalogue gives 3:0–8:11, but 5th ed. (2019, re-standardised) has norms only to about 8:5; check your edition | NDCS summary of RAPT 5th ed.: "age norms to eight years five months" |
| tools_t3.py | Renfrew | read[0] | Renfrew (1997 and later revisions) | Renfrew, C. (2019). *Action Picture Test* (5th ed.). Speechmark/Routledge; earlier editions have older norms | Current edition (Routledge ISBN 9781138586208) |
| tools_t3.py | PhAB2 | before[0] | "PhAB2 … with separate primary and secondary versions … (catalogue 5:0–14:11)" | PhAB2 Primary (Gibbs & Bodman, 2014) 5–11; no PhAB2 secondary; original PhAB 6–14 for older pupils; the catalogue merges the two | GL Assessment product page and 2014 launch notice |
| tools_t3.py | PhAB2 | read[0] | "PhAB2 manual (primary or secondary) … check authors" | Gibbs, S., & Bodman, S. (2014). PhAB2 Primary manual. GL Assessment. | As above; the non-existent secondary manual is removed |
| tools_t3.py | Sandwell | before[0], before[2] | "revised form (SENT-R)"; 4:0–14:0 "most informative for younger…" | two versions: SENT-R 4–8 and SENT KS2–KS3 8–14; the catalogue range covers both; use the right one | GL Education product page |
| tools_t4.py | WRAT-5 | before[1] | "do not repeat it within a short interval" | the SEC does not accept retest results unless an administration or scoring error is shown (SEC 2025, 9.1) | SEC 2026 Instructions, s.9.1 |
| tools_t4.py | WRAT-5 | administer[1] | "Math Computation and parts of Spelling have time limits" | "Math Computation is timed; entry points and any time limits differ by subtest — check" | Spelling time limit not verified, now hedged |
| tools_t4.py | RACE | before[1] | the psych-report / professional-report / error-rate statements cited to "section 4.1" | cited to s.9.1; adds that attainment scores must be from the 12 months before application, and psych-report scores are usable only where the school has none; NEPS role stays at s.4.1 | SEC 2026 Instructions pp. 47–48 (s.9.1) and p. 11 (s.4.1(c)) |
| tools_t4.py | RACE | before[2] | "has piloted additional-time changes" | 2026 Instructions announced a planned pilot of expanded additional time for candidates already RACE-eligible (reported as 10 min per paper, check before quoting) | SEC 2026 Instructions p. 6; Dyslexia Ireland RACE 2026 page |
| tools_t4.py | RACE | read[1] | "Circular Letter 0001/2023 — standardised tests approved for use…" | correct title (Advice on the use of assessment instruments/tests for Guidance and for additional and special educational needs (SEN) in post-primary schools); SEC still cites "01/2023", but it has since been replaced by 0084/2024 and then 0023/2026 (May 2026) | gov.ie circular pages; SEC 2026 Instructions s.9.1 |

## Tool catalogue (src/tool_catalogue.json) values that are wrong or need a hedge — NOT edited (out of scope)

| catalogue key | field | current | problem |
|---|---|---|---|
| WISC-V UK | CANNOT TELL YOU | "Where index scatter exceeds 23 points, report GAI rather than FSIQ and say why." | Stated as a rule and unhedged. The original heuristic is ≥23 points (Flanagan & Kaufman, 2004, WISC-IV), not ">23". It is not a WISC-V manual rule, and GAI only helps when the scatter is driven by WMI/PSI. Reword it as a heuristic |
| Phonological Assessment Battery (PhAB2) | AGE | 5:0–14:11 | Merges PhAB2 Primary (5–11) with the original PhAB (6–14). No PhAB2 covers 12–14 |
| Renfrew Action Picture Test | AGE | 3:0–8:11 | 5th ed. (2019) norms run only to about 8:5. Check the edition |
| Piers-Harris 3 | AGE | 7–18 | That is the Piers-Harris 2 range. The third edition (2018) is published as 6–22 (my own knowledge, not re-verified online; the t3 entry already flags it) |
| Dyscalculia Screener / DysCalculiUM | AGE | 6:0+ / 15+ | The Dyscalculia Screener is normed for about 6–14 ("6:0+" has no upper limit). DysCalculiUM's lower age was not verified |
| MFQ | AGE | 8–18 | Not verified. Published descriptions vary (some say 6/7–17/18). Hedge it |
| DASH-17+ | AGE | 17:0–25:0 | Normally given as 17:0–25:11 (minor) |
| Sandwell Early Numeracy Test | AGE | 4:0–14:0 | Correct only across two versions (SENT-R 4–8; SENT KS2–KS3 8–14). Add a note |

All other catalogue ages for the tools in t1–t4 match my checks (see below).

## Claims checked and confirmed (brief)

- **Ages:** WISC-V UK 6:0–16:11; WPPSI-IV UK 2:6–7:7 (bands 2:6–3:11 / 4:0–7:7); WAIS-IV UK 16:0–90:11; Griffiths III 0–6; ASQ-3 1–66 months; Bayley-4 16 days–42 months; CELF-5 UK 5:0–21:11 (Pearson UK); BPVS-3 3:0–16:11; Conners-4 6–18 (self-report 8+); Conners EC 2–6; BRIEF-2 5–18 (self-report 11–18); SDQ 4–17 / 11–17 self / 2–4 version; RCADS about 8–18 (grades 3–12); BASC-3 2–21 (SRP to college); SCQ 4+ with mental age >2; Vineland-3 birth–90; TEA-Ch2 5–15; Leiter-3 3–75+; WNV 4:0–21:11; BAS-3 3:0–17:11; Beery VMI 2–100; PLS-5 birth–7:11; SGS II 0–5; YARC about 4–16; NARA II 6–12; BYI-2 7–18; AQ 16+; WRAT-5 5–85+.
- **Structures and scores:** WISC-V scaled scores are M10/SD3 and indices M100/SD15, so "scaled 7 = index 85 = −1 SD" is correct. CTOPP-2 subtests are M10/SD3 and composites M100/SD15. WNV subtests are T-scores and its full scale is M100/SD15. Griffiths III has five subscales A–E. Bayley-4 has Cognitive, Language, Motor, plus Social-Emotional and Adaptive by caregiver questionnaire. RCADS has six subscales on a 4-point scale. BRIEF-2 has nine scales, the Negativity/Inconsistency/Infrequency validity scales, and the BRI/ERI/CRI/GEC indexes. PLS-5 has AC, EC and Total Language. WAIS-IV has four indices with ten core subtests. WRAT-5 has four subtests plus the Reading Composite and parallel forms. MFQ uses a 3-point scale over the past two weeks, with the SMFQ at 13 items. BYI-2 has five inventories on a 4-point scale. Piers-Harris 3 has six domains and the Inconsistent Responding / Response Bias indices. Communication Matrix has seven levels and four reasons. SENT has five strands. ADOS-2 has a Toddler module and Modules 1–4 by language level. The Dyscalculia Screener tasks are dot enumeration, number comparison and arithmetic.
- **Citations verified (author–year–journal–volume–pages):** Canivez et al. 2017; Watkins 2000; Flanagan & Alfonso 2017; Velikonja et al. 2017; Hack et al. 2005; Raiford & Coalson 2014; Bishop et al. 2017 (CATALISE-2); De Los Reyes et al. 2015; Achenbach et al. 1987; Toplak et al. 2013; Goodman 1997, 1999; Chorpita et al. 2000; Ebesutani et al. 2010; De Los Reyes & Kazdin 2005; Gotham et al. 2009; Berument et al. 1999; Chandler et al. 2007; Tassé et al. 2012; Manly et al. 2001; Feder & Majnemer 2007; Clarke et al. 2010; Gough & Tunmer 1986; Stanovich 1988; Wolf & Bowers 1999; Butterworth et al. 2011; Dowker 2004 (RR554); Rose 2009; Harter 2012; Angold et al. 1995; Thabrew et al. 2018; Baron-Cohen et al. 2001; Allison et al. 2012; Ashwood et al. 2016; Hull et al. 2017; Rowland 2011; Millar et al. 2006; Sennott et al. 2016; Light 1989; Snowling & Hulme 2011; Lichtenberger & Kaufman 2013; Weiss et al. 2010. Test manuals and publishers: Wechsler/Pearson, Hogrefe (Griffiths), Brookes (ASQ), WPS (ADOS-2, SCQ, Piers-Harris 3), MHS (Conners), PAR (BRIEF-2), Stoelting (Leiter-3), GL (BAS-3, BPVS-3, YARC, PhAB, SENT), Pro-Ed (CTOPP-2).
- **Guidelines:** NICE NG87 (2018, updated 2019) says ADHD must not be diagnosed on rating-scale or observation data alone. Also confirmed: NICE CG128 (2011, updated 2017); CG142 (2012, updated 2021); NG134 (2019); PSI autism guidelines (2nd ed., 2022) exist; Children First guidance (DCYA, 2017); Disability Act 2005 (Assessment of Need).
- **RACE (against the SEC 2026 Instructions):**
  - s.4.1(a): Junior Cycle accommodations are reactivated at Leaving Certificate, and a Junior Cycle scribe is expected to move to a word processor or recording device.
  - s.4.1(b): no cognitive ability scores and no diagnosis are needed.
  - s.4.1(c): NEPS role.
  - s.4.1(h): Independent Appeals Committee, then the Ombudsman (18+) or the Ombudsman for Children (under 18); closing dates are strict.
  - s.5.1: a scribe only "in very exceptional circumstances".
  - s.5.1.4: mental health falls under Physical Difficulty.
  - s.5.6: trauma and adversity are outside scope; NEPS supports schools in crises.
  - s.9.1: WRAT-5 is listed for reading and spelling and must be individually administered; evidence is kept until the Leaving Certificate is completed.
  - s.9.1.5: alternative criteria for Irish-medium candidates, on request.
  - The October webinar exists. The Instructions for the 2026 exams issued in October 2025.
- **Safety wording:** the MFQ, BYI-2, Piers-Harris 3, Communication Matrix and AQ entries already say "Tusla as soon as practicable", that telling the DLP does not discharge the duty, and that supervision follows the action. RCADS is now fixed. No entry advises on medication or has the EP diagnosing.

## Unresolved / for the next reviewer

- **Instructions for the 2027 exams:** on 27/09/2026 these had probably not yet issued (they normally issue in October). The RACE entry already says to check.
- **Additional-time pilot for 2026:** the "10 extra minutes per paper" figure comes from a secondary source (Dyslexia Ireland). The entry hedges it. Confirm against the SEC circular.
- **Circular 0023/2026:** title, date (reported as 18/05/2026) and list taken from gov.ie search listings. The gov.ie page returned 403, so this was not read directly.
- **Renfrew:** first publication year ("1966") not verified. The entry already hedges the edition.
- **DysCalculiUM:** author and year (Beacham & Trott) and its age range not verified. The entry hedges them.
- **Griffiths III:** the 13-author list is not re-verified. The entry says to check it against your copy.
- **Ashwood et al. (2016):** the full author list is not re-verified. The entry already says to check it.
