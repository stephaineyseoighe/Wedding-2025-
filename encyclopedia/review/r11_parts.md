# Review r11 — parts/ micro-skill files

Reviewer brief: adversarial fact-check (citations, attributed findings, Irish policy facts, UCD Handbook/Appendix content, PSI/CORU clause glosses, ghost-written reflection, child protection wording). Every file validated with `python3 check_part.py <file>` after editing. PASS TEST lines untouched.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| formulation_b | Recognise where the sequence is genuinely unclear | why | "PSI Code 2.3.1 and 4.2.5 (distinguishing facts, opinions and hypotheses)" | clauses mapped; "read the clauses for their wording" | Gloss of PSI clause content unverified; standard column only maps the numbers. |
| formulation_b | Consider twice-exceptionality | why | "the NCSE has published on twice-exceptional learners" | NCSE has no dedicated 2e guidance (check); NCCA Exceptionally Able Students: Draft Guidelines (2007) | Wrong attribution. Educ. Sci. 2025, 15(12), 1600 notes NCSE provides no guidance on 2e; NCCA 2007 draft guidelines exist (ncca.ie). |
| formulation_b | Consider twice-exceptionality | s5 | "what the NCSE material says" | "what the NCCA (2007) draft guidelines say" | As above. |
| formulation_b | Recognise when risk crosses a safeguarding threshold | why | "CORU SoP 1.12 (limits of confidentiality)" | "read both clauses for their wording" | Clause content gloss unverified. |
| formulation_b | State explicitly which need is primary | s5 | "literacy-to-behaviour pathway (Snowling & Hulme, 2012)" | "(on direction of effect, see Trzesniewski et al., Child Development, 2006)" | Snowling & Hulme 2012 (JCPP annual review on classification of reading disorders) is not a source on the reading–behaviour pathway. Trzesniewski, Moffitt, Caspi, Taylor & Maughan (2006) Child Dev 77(1) is. |
| intervention_a | Know the evidence base for what you recommend | why | "misrepresent effectiveness — which PSI Code 4.2.2 prohibits" | "where PSI Code 4.2.2 is mapped (read the clause for its wording)" | Gloss of clause content unverified. |
| intervention_a | Co-facilitate rather than only observe | s2 | disclosure "goes to the DLP the same day through the child protection route" | DLP informed and Tusla report as soon as practicable; DLP does not discharge duty; supervision after | Child protection wording implied DLP route sufficient (Children First Act 2015; cf. CORRECTIONS.md). |
| intervention_a | Leave the teacher able to run it | s2 | "disclosure route to the DLP" | "(inform the DLP; report to Tusla as soon as practicable)" | As above. |
| intervention_a | Leave the teacher able to run it | why | "ten-week placement" | "eleven-week placement" | Cavan 05/10/2026–18/12/2026 is 11 weeks (HANDOVER Facts to hold). |
| intervention_a | Know the onward referral route and use it | why | "Tusla, and for any child protection concern the school's DLP" | Tusla report as soon as practicable alongside informing DLP; DLP does not discharge duty | Child protection wording. |
| intervention_b | Ask what the parent hopes to hear before starting | why | "2.14 concerns awareness of power in the relationship" | "read both for their wording before saying what they require" | Gloss of CORU clause content unverified. |
| others_a | Meet the child at their level | why | "Assessment of Children: Cognitive Foundations, 6th ed., 2018" | "…Cognitive Foundations and Applications, 6th ed., 2018" | Title of the 6th edition (Sattler, 2018); "Cognitive Foundations" alone is the 5th ed. (2008). |
| others_a | Notice and respond to reluctance | why | "CORU SoP 5.31 … — adapting and re-evaluating as appropriate" (clause gloss) | "(read the clause for its wording)" | Gloss of CORU clause content unverified. |
| others_b | Name the framework in the formulation | why | "Monsen & Frederickson, 2008, as cited there … check the citation" | full citation: chapter 'The Monsen et al. problem-solving model ten years on', in Kelly, Woolfson & Boyle (Eds.), Frameworks for Practice in EP (2008) | Citation verified (Jessica Kingsley, 2008); hedge no longer needed. |
| others_b | Name the framework in the formulation | s5 | "two frameworks named in the UCD Handbook" | "(check which frameworks the UCD Handbook names — read it for the wording)" | UCD Handbook content asserted without source. |
| others_b | Change register between family and professional audiences | why | "CORU SoP 2.2 and 5.25 both require communication adapted to the audience" | "are mapped here (read both for their wording)" | Clause-content gloss unverified. |
| systemic | Ask your supervisor which model they use | why | "The BPS Standards for Accreditation (2023) name consultation as a competency" | BPS EP doctoral accreditation standards treat consultation as a core function (check current edition and year) | Year/title unverified: EP doctoral standards date from 2019 handbook; BPS reviewed overarching standards in 2023. Hedged, not replaced. |
| systemic | Prepare something to contribute | why | "which CORU SoP 2.16 names directly" | "CORU SoP 2.16 is mapped here (read the clause for its wording)" | Clause-content gloss unverified. |
| supervision_a | Bring a draft to week one | why, s5 | "Page and Wosket (Supervising the Counsellor; edition — check)" / "(… Page & Wosket)" | "Supervising the Counsellor and Psychotherapist, 3rd ed., 2015" / "Page & Wosket, 2015" | Title was truncated and undated; 3rd ed. Routledge 2015. |
| supervision_a | Include at least one thing that went badly | why | "CORU SoP 4.3 (reflecting critically on your own practice)" | gloss removed; "read both for their exact wording" retained | Clause-content gloss unverified. |
| supervision_a | Record what they did that you would not have | why | "CORU SoP 4.3 … — reflecting critically on your own practice" | "(read the clause for its wording)" | As above. |
| supervision_b | Present a case at least once a trimester | why | "CORU SoP 4.5 (seeking peer review)" | "(read the clause for its wording)" | Clause-content gloss unverified. |
| supervision_b | Offer something useful to someone else's case | why | "CORU SoP 5.8 (mentoring and supervision)" | "(read the clause for its wording)" | As above. |
| supervision_b | Name a self-care strategy and evidence it works | why | "Burnout builds slowly (Maslach & Jackson, 1981)" | "builds over time — Maslach and Jackson (1981) describe it as emotional exhaustion, depersonalisation and reduced personal accomplishment" | Maslach & Jackson (1981, J. Occupational Behaviour) is the MBI measurement paper; it defines the three dimensions, not a time course. Attribution corrected. |
| research | Judge applicability to this child in this context | why | "CORU SoP 5.4 (translating theory and evidence into practice)" | "(read the clause for its wording)" | Clause-content gloss unverified. |
| research | Follow up whether anyone acted on it | why | "CORU SoP 3.9 (monitoring and auditing…) and PSI Code 3.1.2 (monitoring and recording…)" | "read both for their wording before quoting what they require" | As above. |

## Summary

All nine files done (181 entries). Every file passes `check_part.py`; keys, labels and PASS TEST lines are unchanged.
About 150 claims checked. 26 cells edited: 10 corrections and 16 hedges. One citation was removed and replaced (Snowling & Hulme, 2012, replaced by Trzesniewski et al., 2006).

## Checked and confirmed (brief)

- **Citations, author–year–venue correct:**
  - Monsen, Graham, Frederickson & Cameron (1998, EPiP); Monsen & Frederickson (2008, ch. in Kelly, Woolfson & Boyle).
  - Kaplan et al. (2001, JLD); Pennington (2006, Cognition); Reiss, Levitan & Szyszko (1982).
  - Masten (2014, Child Dev); Rutter (2012, Dev Psychopathol); Oliver (2013, Disability & Society); Engel (1977, Science).
  - Cummins (1979); Bronfenbrenner & Morris (2006); Carr (2015, 3rd ed.; some catalogues give 2016).
  - NRP (2000); Ehri (2005); Snowling & Hulme (2011, BJEP); Deno (1985; 2003); Bruner (1966).
  - Gersten et al. (2009); Butterworth, Varma & Laurillard (2011); Dowker (2004).
  - Durlak et al. (2011); Kuyken et al. (2022, MYRIAD); Dishion, McCord & Poulin (1999); Weare & Nind (2011); Kelly & Perkins (2012).
  - Egan & Reese (2021 EMEA edition exists; 11th ed. 2019); Rogers (1957); Rowe (1974); Ratner, George & Iveson (2012).
  - Durlak & DuPre (2008); Buckley & Epstein (2004); Baile et al. (2000, SPIKES); Schillinger et al. (2003).
  - Bergan & Kratochwill (1990); Bergan & Tombari (1976); Wagner (2000, EPiP 16(1); 2008 chapter); Rhodes & Ajmal (1995); de Shazer (1985).
  - Gutkin & Curtis (2009); Schein (1999); Sattler (2018); Lundy (2007, BERJ); Stone, Patton & Heen (2010); Stone & Heen (2014).
  - Kessels (2003, JRSM); Tervalon & Murray-García (1998); Lichtenberger et al. (2004); Harvey (2006, J Clin Psychol).
  - Fullan (2016, 5th ed.); Frederickson & Cline (2009); Hall (2005, JIC 19 S1); Frost & Robinson (2007, CAR 16(3)).
  - Joyce & Showers (2002); Kirkpatrick & Kirkpatrick (2006).
  - Proctor (1986; 2008); Kadushin (1976); Scaife (2019); Carroll (2014); Hawkins & McMahon (2020); Ladany et al. (1996, JCP); Bandura (1977); Polanyi (1966); Schön (1983); Boud, Keogh & Walker (1985); Gibbs (1988).
  - Richardson et al. (1995); Sackett et al. (1996); Page et al. (2021, PRISMA 2020); Wolf et al. (2020); Cohen (1988); Cartwright & Hardie (2012); Fixsen et al. (2005); Kiresuk & Sherman (1968); Kazdin (2011); APA (2020).
- **Irish policy:**
  - NEPS Continuum levels, primary (2007) and post-primary (2010) guidelines; Student Support File; Student Support Team.
  - SET allocation Circulars 0013/2017 and 0014/2017 (already hedged "check current"). SNA scheme is for care needs (Circular 0030/2014).
  - SENO role; EPSEN Act 2004; UNCRPD ratified 2018; UNCRC Art. 12.
  - Children First Act 2015 and Guidance (DCYA 2017), including joint reports; Equal Status Acts 2000–2018.
  - GDPR Arts 5, 9, 15 and 33; Data Protection Act 2018.
  - PSI Supervision Guidelines (October 2024 update, replacing 2017); PSI Code 5th rev. 2025 and Accreditation Standards 2022 (as recorded in the workbook's Sources sheet); PSI DECAP.
- **Internal facts:**
  - Cavan 05/10–18/12/2026, four days a week; PSI 3.3.6 unmet; Table 3 Early Years and Young Adult unevidenced; 84-day log.
  - The "your review named X" claims all trace to text on the workbook Reference sheet.
- **Ghost-writing:** no drafted reflections found. The Appendix 5, 6 and 7, essay and dilemma rows are prompts and structure only, and they say so.
- **Child protection:** supervision_a, supervision_b and formulation_b already carried the correct Tusla / DLP / supervision-follows-action wording.

## Not resolved

- CORU SoP numbers and PSI Code clause numbers are reproduced as mapped in the workbook's Standard column. I did not check them against the source documents. Where a row glossed what a clause *says*, I removed the gloss or added "read the clause for its wording". The exception is where the gloss is quoted from the Reference sheet, as with CORU 5.44 and 5.45.
- UCD Handbook section numbers (§4.5a, §4.5b, §6.1, §6.2, §6.4.3, Appendices 1, 5, 6, 7 and 8) are not verifiable here. Each row already tells the reader to read the Handbook for the wording.
- BPS EP accreditation standards: year and edition not confirmed (hedged).
- Whether a trainee EP is a mandated person under Schedule 2 is not settled. The files already say "check with UCD and the service".
