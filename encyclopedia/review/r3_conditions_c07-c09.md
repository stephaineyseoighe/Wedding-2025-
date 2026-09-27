# Review r3: conditions c07–c09

Files: records/cond_c07.py (Adjustment Disorder, Acute Stress Disorder, Prolonged Grief Disorder) · records/cond_c08.py (Speech Sound Disorder, Childhood-Onset Fluency Disorder, SPCD) · records/cond_c09.py (GDD, BIF, SLD-maths)

All three files pass `python3 check_records.py` after the edits.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| cond_c07.py | Prolonged Grief Disorder | code | F43.8x, check the current sub-code | F43.81 (ICD-10-CM code since 01/10/2022; early DSM-5-TR printings show F43.8) | ICD-10-CM FY2023 added F43.81 Prolonged grief disorder, and the DSM-5-TR coding update adopted it |
| cond_c08.py | Stuttering | prevalence (incidence) | lifetime incidence of about 5–8% | incidence may be higher than the 5% traditionally cited; check the exact figure | Yairi & Ambrose (2013) abstract, conclusion 2 |
| cond_c08.py | Stuttering | prevalence (prevalence) | about 1% widely cited (attributed to Y&A) | 1% widely cited, but Y&A conclude the lifespan average may be lower than 1% | Y&A (2013) abstract, conclusion 3. The paper disputes the 1% figure, so it should not be cited for it |
| cond_c08.py | Stuttering | prevalence (recovery) | often cited as about 80% (Y&A, 2013) | Y&A report high natural recovery, higher than earlier estimates; the exact % depends on definition | The 80% figure could not be confirmed from Y&A (2013), whose review argues rates are higher than earlier figures |
| cond_c08.py | Stuttering | prevalence (sex ratio) | close to even at onset | the ratio near onset is smaller than older estimates suggested | Y&A (2013) abstract, conclusion 1. "Close to even" overstates it |
| cond_c08.py | Stuttering | bands School Age / Young Adult prevalence | 1% often cited (Y&A, 2013) | 1% often cited; Y&A suggest the lifespan average may be lower | Same point as the prevalence bullet above |
| cond_c09.py | GDD | what_it_is | "significant", check the exact threshold | 2 SD or more below the mean on standardised norm-referenced testing | Shevell et al. (2003) practice parameter definition |
| cond_c09.py | BIF | recommendations (post-primary) | L2LP may be appropriate, check eligibility | NCCA designed L2LPs for GLD in the low mild to high moderate range, so BIF usually NOT eligible | NCCA L2LP guidance. The earlier wording pointed trainees to a route that BIF students normally do not qualify for |
| cond_c09.py | BIF | bands Adolescent see | "L2LP where eligible" | L2LP is designed for low mild to high moderate GLD, so usually not for BIF | Same as the row above |

## Claims checked and confirmed (no change)

**c07 Adjustment Disorder:**
- DSM-5-TR onset is within 3 months, with no persistence beyond 6 months after the stressor ends. The acute and persistent specifiers and the six subtypes / F43.2x codes are correct.
- The exclusion of normal bereavement and PGD is correct.
- ICD-11 6B43: preoccupation and failure to adapt, onset usually within 1 month, resolution within 6 months unless the stressor persists. ICD-11 has no subtypes. All correct.
- Citations correct: Casey & Bailey 2011 WP 10(1); O'Donnell et al. 2019 IJERPH 16(14):2537; Portzky et al. 2005 JAD 87; Maercker et al. 2013 WP 12(3); Masten 2001; DCYA 2017.
- The Tusla / DLP / supervision wording is correct.

**c07 Acute Stress Disorder:**
- F43.0, 3 days to 1 month, and 9 of 14 symptoms across 5 categories are correct.
- The exposure criterion is correct, including media exposure counting only when work-related.
- ICD-11 QE84 sits in the "factors influencing health status" chapter and is not a mental disorder. Correct.
- There are no preschool ASD criteria. Correct.
- Citations correct: Hiller et al. 2016 JCPP 57(8) (prevalence roughly halves over months); Bryant 2011 JCP 72(2); Kassam-Adams & Winston 2004 JAACAP 43(4); Hobfoll et al. 2007; Rose et al. 2002 Cochrane CD000560; NICE NG116 (2018); PFA WHO/WTF/WVI 2011; Perrin et al. 2005 CRIES.
- NEPS (2016) *Responding to Critical Incidents: Guidelines and Resource Materials for Schools*: the title and year are correct.

**c07 PGD:**
- DSM-5-TR requires 12 months since the death for adults and 6 months for children and adolescents. The yearning/preoccupation criterion, the 3-of-8 list and the note on children's preoccupation with the circumstances of the death are all correct.
- ICD-11 6B42 uses 6 months with cultural variation. Correct.
- Citations correct: Prigerson et al. 2021 WP 20(1); Melhem et al. 2011 AGP 68(9); Lundorff et al. 2017 JAD 212 (about 10%); Stroebe & Schut 1999; Klass et al. 1996; Dyregrov 2008; Cohen et al. 2017; Tonkin 1996. The IPG-C/IPG-A reference (Spuij et al. 2012) is correct.

**c08 SSD:**
- F80.0 and ICD-11 6A01.0 are correct.
- DSM exclusions and Dodd's four subgroups are correct.
- Eadie et al. (2015): 3.4% at 4 years, DMCN 57(6). Correct.
- Wren et al. (2016): 3.6% at 8 years, JSLHR 59(4). Correct.
- Citations correct: Bishop & Adams 1990; Nathan et al. 2004; Hayiou-Thomas et al. 2017; McCormack et al. 2009; Hickey 2007; Stackhouse & Wells 1997; ASHA 2007; DEAP ages 3;0–6;11.

**c08 Stuttering:**
- F80.81 and ICD-11 6A01.1 are correct.
- Reilly et al. (2013) Pediatrics 132(3): cumulative incidence of about 11% by age 4. Correct.
- Citations correct: Iverach & Rapee 2014; Sheehan 1970 (iceberg); Ward 2006; Kelman & Nicholas 2020; Constantino et al. 2022.

**c08 SPCD:**
- F80.82 is correct.
- ICD-11 6A01.22 (DLD with impairment of mainly pragmatic language) is the right nearest code, confirmed.
- DSM criteria: four areas, the RRB exclusion, and diagnosis rare under age 4. Correct.
- Citations correct: Norbury 2014; Swineford et al. 2014; Gibson et al. 2013; Mandy et al. 2017; Bishop 2000; Adams et al. 2012 (mixed primary outcome); Gray 1994; CCC-2 ages 4–16.

**c09 GDD:**
- F88 is correct.
- ICD-11 6A00.4 is "provisional". Correct.
- DSM "under 5, reassessment required" is correct.
- Shevell et al. (2003): two or more domains and 1–3% prevalence. Correct.
- Citations correct: Moeschler & Shevell 2014 Pediatrics 134(3); Riou et al. 2009 DMCN 51(8); Clark & Moss 2011.
- Assessment of Need eligibility (born on or after 01/06/2002) is correct.

**c09 BIF:**
- R41.83 is correct, and so is V62.89 in DSM-5 (2013).
- "Other Conditions That May Be a Focus of Clinical Attention" is correct.
- DSM-IV-TR range of 71–84 is correct.
- Irish "borderline mild GLD" band of approx 70–79 is correct.
- Circular SP ED 02/05 is correct (title and GAM high-incidence grouping). Circulars 0013/2017 and 0014/2017 are correct.
- 13.6% between 70 and 85 (−2 SD to −1 SD) is correct.
- Citations correct: Peltopuro et al. 2014; Emerson et al. 2010; Wieland & Zitman 2016.

**c09 Dyscalculia:**
- F81.2 and ICD-11 6A03.2 are correct.
- DSM-5-TR: the four maths subskills, the dyscalculia note, 6 months despite intervention, the exclusions, IQ above about 70 ± 5, and 5–15% for all SLD across languages and cultures. All correct.
- Citations correct: Butterworth 2005; Butterworth et al. 2011; Gersten et al. 2009; Dowker 2004 RR554; Devine et al. 2013; Ashcraft 2002; Geary 2004; Kaufmann et al. 2013; Siegler & Booth 2004.

## Unresolved / notes

- Maercker et al. (2013) still carries "[check full author list]". The citation itself is real. It needs full APA 7 author formatting.
- Kaufmann et al. (2013) uses "et al." in the reference list. APA 7 requires all authors up to 20. This is a style issue only.
- Stuttering recovery percentage: no figure is given now. If one is wanted, take it from the body of Yairi & Ambrose (2013) and check it first.
- "Reference Part D" / "macro skill 18" are internal cross-references. I did not verify them against the workbook.
