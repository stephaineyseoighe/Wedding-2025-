# Check before quoting

Everything the fact-checkers could not settle from a source, gathered from the fifteen review logs in `review/`.
Each item is already hedged in the workbook text ("check before quoting"); this is the list to work through with the source documents, the manuals, or your supervisor.

Also always true: PSI Code and CORU SoP clause numbers were copied from the workbook's own Standard column and were not re-checked against the source texts; UCD Handbook sections are cited but their contents were not available; confirm in writing with UCD whether you are a mandated person as a trainee.

## Review r1 — Conditions c01–c03

**Could not resolve (left as is, flagged)**

- PSI / CORU clause numbers used inline: PSI 4.2.2 (DCD), 4.5.1 (RAD), 4.1.2, 2.2.1, 2.2.3; CORU 5.44, 5.45. I had no source to verify them — check them against the PSI and CORU codes.
- Norbury (2016) sex ratio and DSM-5-TR DCD sex ratio: already hedged; not verified.
- Kearney (2008) peak ages (school entry, 10–11): already hedged "check".
- Whether "My Thoughts About School" (NEPS, cited in c01/c03) is a separate current NEPS resource from "My Views about School" (Appendix B of the 2023 guide) — check the URL and title before quoting.
- Mental Health Act 2001 amendment status (GAD `law` field): already hedged.

## Review r2 — conditions c04–c06

**Unresolved / for the owner**

- DMDD: I could not access the DSM-5-TR prevalence paragraph to confirm whether it still says 2–5%. The text is now hedged. Check the manual before quoting.
- DMDD code line includes "Part D lists 6A70–6A7Z, the depressive-disorders block". This is an internal cross-reference and not wrong, but a reader could take it as meaning DMDD has an ICD-11 code there. Consider removing it.
- Williams & Hanke (2007) "Drawing the Ideal School" is cited in the ODD child_voice field but is not in the ODD citation list, which is already at the maximum of 10. I added it to the DMDD citation list (see the change table).
- Kearney & Albano (2007) is in the panic citation list but is not referenced in that entry's text. Harmless.

## Review r3: conditions c07–c09

**Unresolved / notes**

- Maercker et al. (2013) still carries "[check full author list]". The citation itself is real. It needs full APA 7 author formatting.
- Kaufmann et al. (2013) uses "et al." in the reference list. APA 7 requires all authors up to 20. This is a style issue only.
- Stuttering recovery percentage: no figure is given now. If one is wanted, take it from the body of Yairi & Ambrose (2013) and check it first.
- "Reference Part D" / "macro skill 18" are internal cross-references. I did not verify them against the workbook.

## Review r4: conditions c10–c12

**Unresolved (hedged, not changed)**

- DSM-5-TR excoriation prevalence wording (1.4% vs 3.1%): hedged, see above.
- Which Irish Tourette's organisation is currently active: Tourette's Support NI & ROI is confirmed active; TSAI status is unknown.
- Andrén et al. (2022) is cited for "tics worsen with stress / after school". The claim is plausible, but that guideline is Part II (interventions), so I could not confirm the exact location. Left as "e.g." with its existing hedge.
- NEPS category for tics (1.6 Co-ordination) is a questionable choice but not a factual error; left as is.
- CIT_ICD in cond_c12 uses "(2019/2022)" rather than a single APA year. This is minor and was left.

## Review r5 — Conditions c13, c15, c16

**Not resolved / for the lead**

- NEPS referral category numbers (e.g., "2.2 Behaviour during break times…" used for substance use, "5.1 Vision", "5.2 Hearing", "3.6 School attendance"). These match other records, but I could not verify them against a NEPS source. The 2.2 choice for substance use reads oddly. Check against the source list.
- CORU/PSI standard numbers (e.g., PSI 2.2.4, 1.1.4, 2.3.3) were not verified.
- ISL Act 2017: I could not fetch the statute text (403). The wording "native and independent language" is widely used, but check it against s.3 before quoting. The commencement date (23/12/2020) is verified.
- Marcus et al. (2012): the 0–5.7% range comes from the companion technical report (Pediatrics 130(3) e714–e755), not the 576–584 guideline. Left as a hedged "roughly 1–5%".

## R6 review: records/cond_c17.py, cond_c18.py, cond_c20.py

**Unresolved / left hedged**

- CHI et al. (2023): author order on the cover not confirmed.
- Photosensitive epilepsy proportion, CP sex ratio, NTD rates in Ireland, DMD ID proportion: hedged in the file, left as they are.
- "Malbin (2002)" and "Eight Magic Keys": already flagged "check source"; plausible, not verified.
- PSI 4.1.2 / CORU 5.45 mapping in c20 supervision: outside what this pass could verify.

## Review r7 — conditions c14, c19, c21

**Unresolved / for a human check**

- DSM-5-TR text for AN, BN and BED prevalence: the TR may have updated some figures from NESARC-III. All are hedged "check before quoting".
- Waite et al. (2014), Tofts et al. (2023), Csecs et al. (2022) and McNamara et al. (2024) are believed correct and already carry "check details" flags.
- NICE CG78 current status: I could not reach the NICE site (403).
- Down Syndrome Ireland "1 in 444": this is the charity's claim; the primary registry source is not identified.

## r8 — tool facts review (records/tools_t1.py – tools_t4.py)

**Tool catalogue (src/tool_catalogue.json) values that are wrong or need a hedge — NOT edited (out of scope)**

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

**Unresolved / for the next reviewer**

- **Instructions for the 2027 exams:** on 27/09/2026 these had probably not yet issued (they normally issue in October). The RACE entry already says to check.
- **Additional-time pilot for 2026:** the "10 extra minutes per paper" figure comes from a secondary source (Dyslexia Ireland). The entry hedges it. Confirm against the SEC circular.
- **Circular 0023/2026:** title, date (reported as 18/05/2026) and list taken from gov.ie search listings. The gov.ie page returned 403, so this was not read directly.
- **Renfrew:** first publication year ("1966") not verified. The entry already hedges the edition.
- **DysCalculiUM:** author and year (Beacham & Trott) and its age range not verified. The entry hedges them.
- **Griffiths III:** the 13-author list is not re-verified. The entry says to check it against your copy.
- **Ashwood et al. (2016):** the full author list is not re-verified. The entry already says to check it.

## Review r9: Part H methods (m1–m3)

**Unresolved / for the next reviewer**

- **NEPS "Managing Reluctant Attendance…" guide:** I could not confirm the original publication year. The citation is now hedged.
- **NEPS guide internals:** not checked against the PDF. This covers the appendix letters (A, B, D, F, H, I), the Step 2 key adult, the sample steps and the Step 4 CAMHS advice. The PDF could not be text-extracted in this container.
- **CORU/PSI standard numbers:** not checked against the standards text. This covers PSI 1.2.10, 3.1.8, 3.3.7 and 4.2.3, and CORU 5.38 "individual, group and organisational". It is an internal cross-reference to Reference Part B.
- **Clarke, Bunting & Barry (2014):** the actual outcomes are not summarised in the file. The file already says "read before citing".
- **Nolan & Moreland (2014):** the characterisation is reasonable but was not checked against the abstract.
- **DARE document deadline:** stated only as "a March deadline". Check the exact date in the 2026/2027 handbook.

## Review r10 — micro_new.py

**Not resolved (left as written, already hedged or mapped from the workbook's Standard column)**

- The PSI Code and CORU SoP clause numbers are copied from the workbook's "Standard" column. None could be checked against the source texts here: PSI Code 1.2.9, 1.3.5, 1.3.10, 1.4.3, 2.2.2, 2.2.3, 2.3.1, 2.5.1, 3.3.6, 3.4.3, 4.1.2, 4.2.2, 4.2.5, 4.2.6; CORU SoP 1.2, 1.12, 1.15, 1.18, 2.8, 3.4, 3.5, 3.12, 3.13, 3.14, 4.5, 5.11, 5.44, 5.45. The PSI Code "Appendix A" seven-step procedure is also unchecked. Check before quoting.
- Carr's model is cited as "Carr, 2015". The Handbook of Child and Adolescent Clinical Psychology (3rd ed.) is usually dated 2016. Check against Handbook §2.1.
- De Los Reyes et al. (2015) is credited with the Operations Triad Model. The model was introduced by De Los Reyes, Thomas, Goodman & Kundey (2013, Annu Rev Clin Psychol); the 2015 paper applies it. Acceptable as worded, but cite 2013 if the model's origin is the point.
- UCD Handbook §5 (seven-day duty), §6, §6.2 and §2.1 were not available to check. The entries already hedge.

## Review r11 — parts/ micro-skill files

**Not resolved**

- CORU SoP numbers and PSI Code clause numbers are reproduced as mapped in the workbook's Standard column. I did not check them against the source documents. Where a row glossed what a clause *says*, I removed the gloss or added "read the clause for its wording". The exception is where the gloss is quoted from the Reference sheet, as with CORU 5.44 and 5.45.
- UCD Handbook section numbers (§4.5a, §4.5b, §6.1, §6.2, §6.4.3, Appendices 1, 5, 6, 7 and 8) are not verifiable here. Each row already tells the reader to read the Handbook for the wording.
- BPS EP accreditation standards: year and edition not confirmed (hedged).
- Whether a trainee EP is a mandated person under Schedule 2 is not settled. The files already say "check with UCD and the service".

## r12 — records/pres_p1.py, records/pres_p2.py (40 PRES)

**Unresolved**

- Whether the Education Act 1998 s.2 wording "exceptionally able students" survives the EPSEN s.52 amendment — secondary sources disagree; irishstatutebook.ie returned 403. Hedged in text; check the Law Reform Commission revised Act.
- "NEPS interpreter request form" (EAL, Interpreter entries) comes from Part D; not independently verified; hedged.
- German (2000) is a test manual cited for a rapid-naming association — acceptable but weak; left.

## Review r13 — records/pres_p3.py, records/pres_p4.py (40 PRES entries)

**Not resolved / flagged for the owner**

- NCSE (2018) SNA review: the full title is long. The wording given matches the published title as far as I could check without the PDF.
- Emerson (1995) first-edition subtitle is "…in People with Learning Difficulties". Kept as written. Later editions changed the wording.
- "Asking about suicide does not increase risk" (pres_p4, Risk-taking) is correct but has no attribution. There is no room in the citation list (5/5), so no source was added. Dazzi et al. (2014, Psychological Medicine) is the usual source.
- The DoE Behaviours of Concern Guidelines had a later circular on training, monitoring and oversight. Its number and year were not checked. The text says "check for update circulars".

## Review r14: presentations p5, p7 and p8

**Unresolved**

- **Rose et al. (2015), emotion coaching:** cited in the text of p5 "Complex trauma" and "Trauma-informed classroom practice" but missing from their reference lists. I was not certain enough of the journal details to add it. Next reviewer: add the full reference (Rose, Gilbert & McGuire-Snieckus, 2015) after checking.
- **Stallard et al. (2012), Kuyken et al. (2022) and Ttofi & Farrington (2011):** also cited in text without references. All three are real studies.
- **NEPS "Managing reluctant attendance…" year:** I could not open the PDF metadata. Now "n.d."; confirm the year on gov.ie.
- **Children First Act 2015, Schedule 2 wording for psychologists:** the entries assume the EP is a mandated person. That is consistent with the rest of the workbook, but the exact Schedule 2 wording was not re-checked here.
- **Durlak & DuPre (2008), "two to three times":** hedged from memory of the paper's text; confirm against the full text if the figure is to be quoted.

## r15 — records/pres_p6.py (20 PRES: 4.1 social, 4.2 relationships with adults, 5.1 vision, 5.2 hearing, 5.3 physical)

**Unresolved / for the author**

- **EAL vs SEN:** I could not find an Irish Department, NEPS or NCCA document that states "EAL is not a SEN" in those words. The entry now rests on the EPSEN definition and the English Code of Practice, with a hedge.
- **HSE position on gender services after Cass:** the entry says "check current HSE position". I did not verify the details of HSE's current model of care.
- **Circular 0030/2014:** reported as under review (2025). Recheck before Cavan (05/10/2026) in case a replacement has been issued.
