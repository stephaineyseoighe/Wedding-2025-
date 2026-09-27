# Review r10 — micro_new.py

Reviewer: adversarial fact-check pass (r10). Validator: `python3 -c "import micro_new; print(len(micro_new.MICRO))"` → **81** (imports cleanly).

**Entry count discrepancy:** the brief says 136 entries. The file holds **81** unique keys (81 `("` key lines, no duplicates, 81 PASS TEST lines) and ends at `# BATCH9` after 'Include the child's construction of the problem'. Nothing was deleted in this review. Either the brief's count is wrong or the later Formulation entries were never written or were lost. **Unresolved — check before merging.**

PASS TEST lines: all 81 checked byte-identical before/after.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| micro_new.py | Guardianship · Establish who holds guardianship before contact | why | "unmarried father may or may not be, depending on cohabitation, agreement or court order" | Automatic only after 12 consecutive months' cohabitation with the mother after 18/01/2016, incl. ≥3 months with mother and child after the birth; otherwise statutory declaration or court order | Guardianship of Infants Act 1964 s.2(4A) as inserted by CFRA 2015; Citizens Information / Treoir |
| micro_new.py | Complete service induction · Identify the DLP by name in week one | why | "Every organisation … must have a DLP (CFNG 2017)" | CFNG 2017: organisations *should* appoint a DLP; schools *must* appoint a DLP and deputy under Child Protection Procedures for Primary and Post-Primary Schools 2017 (revised 2023) | Overstated source. DE procedures revised 2023, effective 01/09/2023 (gov.ie) |
| micro_new.py | Complete service induction · Ask which tools you may administer independently here | why | "PSI Code 3.3.6 is the standard mapped here." | + note: not to be confused with PSI accreditation criterion 3.3.6 (placement settings); read the Code clause before citing | Clashes with HANDOVER "Facts to hold" (PSI 3.3.6 = settings criterion). The mapping comes from the workbook's Standard column, so it was kept and flagged, not changed |
| micro_new.py | Limits of competence · Know your publisher competence level for every tool | why | "PSI Code 3.3.6 is the clause mapped here." | same clarification added | as above |
| micro_new.py | Behavioural and emotional rating scales · Distinguish elevated from clinically significant | s3 | "fewer than about one in fifty children … scored this high" | "only about two in every hundred children …" | T ≥ 70 = +2 SD ≈ 2.3% (≈1 in 44), which is more than 1 in 50, so "fewer than" was wrong |
| micro_new.py | Child protection · Act the same day without waiting for supervision | why | "delay is the commonest way trainees fall short of the duty" | "delay is a common way to fall short of the duty" | Unsourced superlative |
| micro_new.py | Synthesise findings · Write an integration section rather than a list | why | "the commonest reason a trainee's report is returned" | "a common reason for a trainee's report to be sent back" | Unsourced superlative |

## Checked and confirmed correct

- **Children First Act 2015:** harm = assault, ill-treatment, neglect, sexual abuse; "seriously affected" threshold, with no seriousness qualifier for sexual abuse; s.14 duty to report "as soon as practicable"; joint reports allowed; telling the DLP does not discharge the duty. Schedule 2 lists psychologists "eligible for registration in the register (if any)", and the entry correctly leaves trainee status to be confirmed in writing. CFNG 2017 chapter 3 covers mandated persons, including the 16–17-year-old provision.
- **Tusla out of hours:** the mandated-report line is 0818 776 315, and Tusla says to contact the Gardaí if a child is in immediate danger. The entry's wording is consistent (tusla.ie).
- **Supervision and DLP:** the "supervision follows action" order and DLP-not-discharging wording are correct and consistent across the child protection block.
- **Garda vetting:** National Vetting Bureau (Children and Vulnerable Persons) Acts 2012–2016 bar relevant work until a disclosure is received. Tusla "Introduction to Children First" e-learning exists.
- **Data protection:** GDPR Art. 9 (special category / health data); Art. 33 72-hour notification "where required"; Data Protection Act 2018.
- **ADMCA 2015:** commenced 26/04/2023; s.3 functional test; s.8 guiding principles (presumption of capacity, all practicable steps, unwise decision is not incapacity).
- **Other law and circulars:** Equal Status Acts 2000–2018 (reasonable accommodation); Disability Act 2005 Assessment of Need; DES Circulars 0013/2017 (primary) and 0014/2017 (post-primary).
- **Standards for Educational and Psychological Testing (AERA/APA/NCME, 2014):** accommodations vs modifications.
- **CTOPP-2:** Wagner, Torgesen, Rashotte & Pearson 2013; scaled 10/3 and composites 100/15; composite make-up differs by age band (4–6 vs 7–24).
- **BASC-3:** Reynolds & Kamphaus 2015; clinical scales 60–69 at-risk, ≥70 clinically significant.
- **ASEBA:** Achenbach & Rescorla 2001; syndrome scales 65–69 borderline, ≥70 clinical.
- **SDQ:** Goodman 1997; self-report ages 11–17.
- **SCQ and SRS-2:** Rutter, Bailey & Lord 2003; Constantino & Gruber 2012.
- **Citations:**
  - Achenbach, McConaughy & Howell 1987 (Psychol Bull)
  - De Los Reyes & Kazdin 2005 (Psychol Bull)
  - De Los Reyes et al. 2015 (Psychol Bull)
  - Gough & Tunmer 1986 (RASE)
  - Stanovich 1988 (J Learn Disabil, phonological-core)
  - Wolf & Bowers 1999 (J Educ Psychol, double deficit)
  - Rose 2009 (title correct)
  - Hull et al. 2017 (JADD, camouflaging)
  - Loomes, Hull & Mandy 2017 (JAACAP, ~3:1)
  - Lundy 2007 (BERJ; space, voice, audience, influence)
  - Maslach & Jackson 1981 (J Occup Behav; three dimensions)
  - Lichtenberger, Mather, Kaufman & Kaufman 2004 (Essentials of Assessment Report Writing)
  - Denzin 1978 (The Research Act, 2nd ed.)
  - Monsen & Frederickson 2008 and Gameson & Rhydderch 2008, both in Kelly, Woolfson & Boyle 2008
  - Frederickson & Cline 2009
  - PSI autism guidelines 2022 exist (Professional Practice Guidelines for the Assessment, Formulation and Diagnosis of Autism in Children and Adolescents, 2nd ed.)
- **Guardianship of married parents:** the mother and a father married to her are automatic guardians.

## Not resolved (left as written, already hedged or mapped from the workbook's Standard column)

- The PSI Code and CORU SoP clause numbers are copied from the workbook's "Standard" column. None could be checked against the source texts here: PSI Code 1.2.9, 1.3.5, 1.3.10, 1.4.3, 2.2.2, 2.2.3, 2.3.1, 2.5.1, 3.3.6, 3.4.3, 4.1.2, 4.2.2, 4.2.5, 4.2.6; CORU SoP 1.2, 1.12, 1.15, 1.18, 2.8, 3.4, 3.5, 3.12, 3.13, 3.14, 4.5, 5.11, 5.44, 5.45. The PSI Code "Appendix A" seven-step procedure is also unchecked. Check before quoting.
- Carr's model is cited as "Carr, 2015". The Handbook of Child and Adolescent Clinical Psychology (3rd ed.) is usually dated 2016. Check against Handbook §2.1.
- De Los Reyes et al. (2015) is credited with the Operations Triad Model. The model was introduced by De Los Reyes, Thomas, Goodman & Kundey (2013, Annu Rev Clin Psychol); the 2015 paper applies it. Acceptable as worded, but cite 2013 if the model's origin is the point.
- UCD Handbook §5 (seven-day duty), §6, §6.2 and §2.1 were not available to check. The entries already hedge.
