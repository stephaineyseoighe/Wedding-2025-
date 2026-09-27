# Review r7 — conditions c14, c19, c21

Reviewer: adversarial fact-check pass (26–27/09/2026). Files: records/cond_c14.py, records/cond_c19.py, records/cond_c21.py.
All three files pass `python3 check_records.py` after the edits.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| cond_c19.py | Genetic syndromes | prevalence | "Williams, PWS, Angelman, Rett … 1 in 10,000 to 1 in 20,000 (Williams: Strømme et al., 2002 …)" | Williams about 1 in 7,500 (Strømme et al., 2002); PWS 1 in 10,000–30,000 (Cassidy et al., 2012); others similar order; check | Strømme et al. (2002) estimated 1 in 7,500, so the source was cited for a figure it does not give. |
| cond_c19.py | Genetic syndromes | prevalence | Fragile X "1 in 4,000 males / 1 in 8,000 females … (Hagerman et al., 2017)" | Commonly cited figure kept, but no longer credited to Hagerman; notes that meta-analytic estimates are lower; check | The review does not clearly give this figure. Meta-analysis (Hunter et al., 2014) gives lower frequencies (about 1 in 7,000 males, 1 in 11,000 females). |
| cond_c19.py | Genetic syndromes | code | "Down syndrome LD40.0; Fragile X syndrome LD55" | "Down syndrome — complete trisomy 21 — LD40.0; Fragile X — ICD-11 title 'Fragile X chromosome' — LD55" | ICD-11 MMS titles: LD40.0 = Complete trisomy 21 (mosaic and translocation forms are coded elsewhere); LD55 = Fragile X chromosome. |
| cond_c14.py | Binge-Eating Disorder | prevalence | "DSM-5-TR reports … 1.6% females, 0.8% males" | Says these are DSM-5 (2013) figures; DSM-5-TR may cite newer, lower US data; check the text | 1.6% and 0.8% are the DSM-5 figures. Newer US survey data (Udo & Grilo, 2018, NESARC-III) give 0.44% overall. I could not confirm which figure the DSM-5-TR text uses. |
| cond_c14.py | all 8 entries (shared CP_ROUTE) | red_flags | ends "…duty under the Children First Act 2015." | adds "Supervision follows action; it does not replace it." | Brief safety standard. |
| cond_c14.py | Encopresis | red_flags | neglect indicators → "discuss with DLP and follow the child protection route" | "report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty. Supervision follows action." | The old wording implied the DLP route was enough (Children First Act 2015). |
| cond_c21.py | Personality disorders | citations | NICE CG78 "…a replacement guideline has been in development" | "check the NICE website for its current status and any update before quoting" | Could not confirm that a replacement is in development; NICE surveillance reviews decided not to update. Claim removed. |

## Checked and confirmed (brief)

**Codes**
- ICD-11: 6B80 AN, 6B81 BN, 6B82 BED, 6B83 ARFID, 6B84 Pica, 6B85 Rumination-regurgitation, 6C00 Enuresis, 6C01 Encopresis.
- ICD-11: 6B60 / 6B61 / 6B64 / 6B65 / 6B66 dissociative; 6D10.0–.2 PD severity, 6D11 traits, 6D11.5 borderline pattern.
- ICD-11: 6A40 / 6A41 / 6A4Z / 6E69 catatonia; 6A0Y / 6A0Z; HA60 / HA61 in Chapter 17; LD40.0; LD55.
- DSM-5-TR: F64.2 (children) and F64.0 (adolescents/adults; F64.1 in DSM-5); F88 / F89.

**DSM-5-TR criteria**
- Gender dysphoria: children 6 of 8 (A1 required); adolescents/adults 2 of 6; both ≥6 months.
- Enuresis: ≥5 years; twice a week for 3 months, or distress.
- Encopresis: ≥4 years; once a month for 3 months.
- BN / BED: once a week for 3 months.
- Pica: ≥1 month, minimum age about 2.
- Rumination: ≥1 month.
- Catatonia: 3 of 12 features.
- Amenorrhoea removed as an AN criterion in DSM-5.
- PD under 18: features for ≥1 year; ASPD cannot be diagnosed under 18.
- ND-PAE is the example for "other specified"; Rett was removed in DSM-5.

**DSM-5-TR prevalence (hedged in the text)**
- AN about 0.4% of young females; about 10:1 female:male in clinical populations.
- BN 1%–1.5%; about 10:1.
- Enuresis 5–10% at 5 years, 3–5% at 10, about 1% at 15+; nocturnal more common in males, diurnal in females.
- Encopresis about 1% of 5-year-olds; more common in males.

**Other figures**
- hEDS Beighton cut-offs ≥6 / ≥5 / ≥4 (Malfait et al., 2017).
- ICD-11 HA61 about 2 years; in effect from 01/01/2022.
- Wing & Shah (2000): 17% of those aged 15+ in a referred sample.
- Hunter et al. (2004): depersonalisation/derealisation 1–2%.
- 22q11.2 about 1 in 3,000–6,000.
- Down Syndrome Ireland "1 in 444": the charity's own figure, already hedged.

**Guidelines and documents**
- NICE NG69 (2017; family therapy first-line for AN and BN in young people).
- NICE CG111 (2010; no exclusion on age alone; reward behaviours, not dry nights), CG99 (2010), CG89 (2009), NG217 (2022), NG225 (2022), CG78 (2009).
- RCPsych MEED CR233 (2022).
- HSE Eating Disorder Model of Care (2018).
- Cass Review final report April 2024, including "social transition as an active intervention"; GIDS closed 2024.
- Gender Recognition Act 2015: 16–17 by court order; none under 16; self-declaration from 18.
- Cineáltas (2022) / Bí Cineálta (2024); Children First (2017); Circular 0013/2017; NEPS Continuum (2007); Well-being in post-primary schools (2013).

**Helplines**
- Samaritans 116 123; Pieta 1800 247 247; text 50808; Childline 1800 66 66 66.

**Citations**
- About 70 author–year–journal–volume–page pairings checked, with no errors found. Includes Fisher 2014; Cermak 2010; Taylor 2015; Bryant-Waugh 2019; McAdam 2004; Rose 2000; Williams & McAdam 2012; Halland 2018; Hyams 2016; Arcelus 2011; Eisler 2016; Treasure 2020; Westwood & Tchanturia 2017; Russell 1979; Stice 2002; Hudson 2007; Neumark-Sztainer 2006; Puhl & Latner 2007; Tanofsky-Kraff 2008; Austin 2016; Nevéus 2020; von Gontard 2011; Joinson 2006; Tabbers 2014; Azrin & Foxx 1971; Dykens 1995; Fidler 2005; Mervis & John 2010; Cassidy 2012; Neul 2010; Strømme 2002; Moeschler 2014; Castori / Malfait / Engelbert / Bulbena 2017; Kirby & Davies 2007; Csecs 2022; Beighton 1973; Coleman 2022; Steensma 2013; Temple Newhook 2018; Warrier 2020; de Graaf 2018; Meyer 2003; Hendricks & Testa 2012; Ryan 2010; ISSTD 2004; Putnam 1993; Armstrong 1997; Dalenberg 2012; Lynn 2012; Bach & First 2018; Chanen 2017; Kaess 2014; Sharp & Fonagy 2015; Mehlum 2014; McCauley 2018; Rossouw & Fonagy 2012; Benarous 2018; Consoli 2012; Cornic 2009; Breen & Hare 2017; Gillberg 2010; Astle 2022; Moran 2001.

## Unresolved / for a human check
- DSM-5-TR text for AN, BN and BED prevalence: the TR may have updated some figures from NESARC-III. All are hedged "check before quoting".
- Waite et al. (2014), Tofts et al. (2023), Csecs et al. (2022) and McNamara et al. (2024) are believed correct and already carry "check details" flags.
- NICE CG78 current status: I could not reach the NICE site (403).
- Down Syndrome Ireland "1 in 444": this is the charity's claim; the primary registry source is not identified.
