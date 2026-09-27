# Review r2 — conditions c04–c06

Files: records/cond_c04.py (EAL/DLD, MDD, PDD), records/cond_c05.py (ODD, CD, DMDD), records/cond_c06.py (Selective Mutism, Specific Phobia, Panic Disorder & Agoraphobia).
All three pass `python3 check_records.py` after edits.

## Changes

| file | entry | field | before (short) | after (short) | reason / source |
|---|---|---|---|---|---|
| cond_c05.py | DMDD | prevalence (OVERALL) | "DSM-5-TR estimates 6-month to 1-year prevalence ... 2–5%, higher in males and school-age ... (APA, 2022)" | Attributed to the original DSM-5 text (2013); DSM-5-TR section "may differ — check" | The 2–5% / "higher in school-age" wording is the 2013 DSM-5 text (confirmed via PsychDB, DSM-5 summaries). I could not confirm DSM-5-TR kept it, and later community data (Copeland 2013) put the rate lower and highest in preschoolers. Hedged; no new figure invented. |
| cond_c05.py | DMDD | prevalence (Copeland) | "roughly 1–3% in the preschool-to-adolescent range" | "3-month rates roughly 0.8–3.3%, HIGHEST in the preschool sample (age-of-onset rule set aside)" | Copeland et al. (2013) abstract, AJP 170(2): 3-month prevalence 0.8–3.3%, highest in preschoolers. The old wording hid the fact that this contradicts "higher in school-age". |
| cond_c05.py | DMDD | bands.School Age.prevalence | "DSM-5-TR estimates about 2–5% ... higher in school-age males (APA, 2022)" | "Original DSM-5 text (2013) ... community data are lower (Copeland et al., 2013) — check DSM-5-TR" | Same as row 1 |
| cond_c05.py | DMDD | bands.Adolescent.prevalence | "Lower than in school age (APA, 2022)" | "Expected to be lower than in school age (original DSM-5 text; Copeland et al., 2013)" | Same as row 1 |
| cond_c05.py | DMDD | citations | (Williams & Hanke 2007 cited in text, missing from the list) | added full APA reference | The in-text citation had no matching reference |
| cond_c06.py | Selective Mutism | prevalence (SEX RATIO) | "more common in girls in most studies (Viana et al., 2009)" | More girls in many clinical samples, but the DSM-5 text says prevalence "does not seem to vary by sex" — do not quote a ratio | DSM-5 prevalence text (via PsychDB/ASHA summaries). The entry gave a one-sided picture and left out what the manual says. |

## Claims checked and confirmed correct (no change)

**ICD / DSM codes:** 6A70 single-episode and 6A71 recurrent depressive disorder; 6A72 dysthymic disorder; 6C90 ODD (with/without chronic irritability-anger qualifier); 6C91 conduct-dissocial disorder (childhood/adolescent onset, limited prosocial emotions qualifier); ICD-11 has no DMDD category; 6B06 selective mutism; 6B03 specific phobia; 6B01 panic disorder; 6B02 agoraphobia. ICD-10-CM: F91.3 ODD; F91.1/F91.2/F91.9 CD; F34.81 DMDD; F94.0 SM; F41.0 panic; F40.00 agoraphobia.

**DSM-5-TR criteria wording:** MDD (5 of 9, 2 weeks, irritable mood allowed in young people, failure to make expected weight gain); PDD (1 year in young people, irritable mood, 2 of 6 symptoms, never symptom-free for more than 2 months; DSM-5 merger of dysthymia and chronic MDD); ODD (4 of 8, 6 months, frequency rule for under-5s and 5-plus, severity set by number of settings, DMDD exclusion); CD (3 of 15 in 12 months with 1 in 6 months, onset before 10 for the childhood-onset specifier, 2 of 4 for the limited-prosocial-emotions specifier, the ASPD rule after 18); DMDD (outbursts 3 or more times a week, 12 months with no break of 3 months, 2 of 3 settings, not first diagnosed before 6 or after 18, onset before 10, cannot co-exist with ODD/IED/bipolar, the 1-day mania rule); SM (1 month, not the first month of school, language exclusion, onset usually before 5, "elective" renamed in DSM-IV 1994); specific phobia (6 months, five specifiers); panic attack (4 of 13, peaks within minutes); panic disorder (1 month of worry or behaviour change); agoraphobia (2 of 5 situations, 6 months, a separate diagnosis since DSM-5).

**Prevalence:** Costello, Erkanli & Angold (2006): about 2.8% under 13 and 5.6% at 13–18, so "roughly 3% / nearer 6%" is right. Polanczyk et al. (2015): ODD 3.6%, CD 2.1%, disruptive behaviour disorders overall 5.7%. DSM ODD range 1–11% and sex ratio 1.4:1 before adolescence. DSM CD 2–>10%, median 4%. Bergman et al. (2002): 0.71%. DSM SM 0.03–1%. Specific phobia about 5% in children, about 16% at 13–17, 7–9% in US adults, about 2:1 female. Panic below 0.4% under 14, 2–3% 12-month, about 2:1 female. Agoraphobia 1.7%. Norbury et al. (2016) DLD about 7%.

**Guidelines, law, helplines:** NICE NG134 (2019); NICE CG158 (2013, updated 2017), with parent training at 3–11, child problem-solving at 9–14 and multimodal work for adolescents; Wellbeing Policy Statement 2018–2023 (revised 2019); Well-being in Post-Primary Schools (2013); Children First 2017; Education Act 1998 s.29 (the 20-day suspension appeal); Tusla Education Support Service and reduced-school-days guidelines (2021, hedged); SEC RACE scheme. Helplines: Pieta 1800 247 247, Samaritans 116 123, text 50808, Childline 1800 66 66 66. Jigsaw serves ages 12–25.

**Theory:** Cummins BICS/CALP (about 2 years for conversational English, 5–7 years for academic English, already hedged as broad estimates); Cummins 1979 (Working Papers on Bilingualism 19) and 1981 (Applied Linguistics 2(2)).

**Citations verified (author, year, title, journal, volume, pages):** Bedore & Peña 2008; Bishop et al. 2017; Kohnert 2010; Paradis et al. 2011; Peña et al. 2014; Norbury et al. 2016; Strand & Lindsay 2009; Tabors 2008; Thapar et al. 2012; Dazzi et al. 2014; Dooley & Fitzgerald 2012; Dooley et al. 2019; Beck 1967; Keller & Shapiro 1982; Kovacs et al. 1994; Hollo et al. 2014; McGilloway et al. 2012; Polanczyk et al. 2015; Stringaris & Goodman 2009; Burke et al. 2002; Patterson 1982; Newson et al. 2003; Moffitt 1993; Frick et al. 2014; Moran 2001; Leibenluft 2011; Copeland et al. 2013; Stringaris et al. 2018; Frederickson & Cline 2015; Greene 2014 (5th ed., already flagged to check for the current edition); Johnson & Wintgens 2016 (Resource Manual 2nd ed., Speechmark) and 2012 (Can I tell you…, JKP); Cohan et al. 2006; Kristensen 2000; Muris & Ollendick 2015; Toppelberg et al. 2005; Viana et al. 2009; Craske et al. 2014; Creswell & Willetts 2019; Gullone 2000; James et al. 2020; Lebowitz et al. 2013; Ollendick et al. 2009; Öst & Sterner 1987; van Steensel et al. 2011; White & Epston 1990; Clark 1986; Kearney & Albano 2007; Pincus et al. 2010.

**Safety wording:** every risk and child-protection red flag says to report to Tusla as soon as practicable, that telling the DLP does not discharge the mandated person's duty, and that supervision follows action. No medication advice and no EP diagnosis anywhere. Confirmed in all 9 entries.

## Unresolved / for the owner

- DMDD: I could not access the DSM-5-TR prevalence paragraph to confirm whether it still says 2–5%. The text is now hedged. Check the manual before quoting.
- DMDD code line includes "Part D lists 6A70–6A7Z, the depressive-disorders block". This is an internal cross-reference and not wrong, but a reader could take it as meaning DMDD has an ICD-11 code there. Consider removing it.
- Williams & Hanke (2007) "Drawing the Ideal School" is cited in the ODD child_voice field but is not in the ODD citation list, which is already at the maximum of 10. I added it to the DMDD citation list (see the change table).
- Kearney & Albano (2007) is in the panic citation list but is not referenced in that entry's text. Harmless.
