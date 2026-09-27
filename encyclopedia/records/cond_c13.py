# CONDS batch c13 — addictive behaviours.
# 1 Substance use disorders · 2 Gambling Disorder · 3 Gaming Disorder
# Context: Reference Part D, 2. BEHAVIOUR (2.2) — referral routes NEPS / CAMHS / Addiction services / Tusla.
# Stance throughout: non-judgemental, harm-reduction-aware, formulate before labelling.
# The EP does not diagnose, screen clinically for substance use or advise on medication (PSI 2.2.2).
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c13.py

NEPS_ADD = ("2. BEHAVIOUR (2.2 Behaviour during break times and around the school) — and 3. EMOTIONAL "
            "(3.4 Mood · 3.7 Risk and safeguarding)")
CORU = "3.1 · 3.2 · 3.4 · 3.10 · 3.12 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32 · 5.34"
PSI = "2.2.2 · 2.2.4 · 2.3.1 · 1.3.1 · 1.2.8 · 1.1.4"
LAW_SUB = ("Children First Act 2015 · Children First National Guidance (2017) · Misuse of Drugs Acts 1977–2016 · "
           "Intoxicating Liquor Acts (sale to under-18s) · Education Act 1998 · Education (Welfare) Act 2000 · "
           "Equal Status Acts 2000–2018 · GDPR / Data Protection Act 2018 (special category health data)")
LAW_GAMB = ("Children First Act 2015 · Children First National Guidance (2017) · Gambling Regulation Act 2024 "
            "(check commencement of each part) · Education Act 1998 · Equal Status Acts 2000–2018 · "
            "GDPR / Data Protection Act 2018")
LAW_GAME = ("Children First Act 2015 · Children First National Guidance (2017) · Online Safety and Media "
            "Regulation Act 2022 · Education Act 1998 · Education (Welfare) Act 2000 · Equal Status Acts "
            "2000–2018 · GDPR / Data Protection Act 2018")

CIT_DSM = ("American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders "
           "(5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787")
CIT_ICD = ("World Health Organization. (2019). International classification of diseases for mortality and "
           "morbidity statistics (11th rev.). https://icd.who.int/ — check codes before quoting.")
CIT_MR = "Miller, W. R., & Rollnick, S. (2013). Motivational interviewing: Helping people change (3rd ed.). Guilford Press."
CIT_STEIN = ("Steinberg, L. (2008). A social neuroscience perspective on adolescent risk-taking. Developmental "
             "Review, 28(1), 78–106.")
CIT_DOH = ("Department of Health. (2017). Reducing harm, supporting recovery: A health-led response to drug and "
           "alcohol use in Ireland 2017–2025. Government of Ireland. — check for the successor strategy.")
CIT_HH = ("Health Service Executive & Tusla – Child and Family Agency. (2019). Hidden Harm strategic statement: "
          "Seeing through hidden harm to brighter futures. HSE & Tusla. — check for updates and the companion "
          "Practice Guide.")
CIT_CF = ("Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection "
          "and welfare of children. Government Publications.")

CONDS = []

# ============================================================================ 1 · SUBSTANCE USE DISORDERS
CONDS.append({
 "name": "Substance use disorders",
 "code": ("DSM-5-TR Substance-Related and Addictive Disorders (substance use disorder, specified by substance; "
          "mild / moderate / severe) · ICD-11 6C40–6C4H Disorders due to substance use (e.g., 6C40 alcohol, "
          "6C41 cannabis, 6C4A nicotine) · hazardous alcohol / drug use QE10–QE11 (not disorders) — check codes "
          "before quoting"),
 "neps": NEPS_ADD,
 "coru": CORU,
 "psi": PSI,
 "law": LAW_SUB,

 "what_it_is": [
  "DSM-5-TR merged the old 'abuse' and 'dependence' into one SUBSTANCE USE DISORDER per substance (alcohol, cannabis, opioid, stimulant, tobacco, inhalant, sedative, hallucinogen and others). A problematic pattern leading to clinically significant impairment or distress, with at least two of eleven criteria within 12 months (APA, 2022).",
  "The eleven criteria fall into four groups: IMPAIRED CONTROL (more or longer than intended; wanting or failing to cut down; much time spent; craving), SOCIAL IMPAIRMENT (failing role obligations such as school; use despite relationship problems; giving up activities), RISKY USE (in hazardous situations; despite known physical or psychological harm) and PHARMACOLOGICAL (tolerance; withdrawal) (APA, 2022).",
  "SEVERITY is a count: mild = 2–3 criteria, moderate = 4–5, severe = 6 or more (APA, 2022). Tolerance and withdrawal from medically prescribed use do not count.",
  "ICD-11 keeps separate categories: a SINGLE EPISODE OF HARMFUL USE, a HARMFUL PATTERN OF USE, and SUBSTANCE DEPENDENCE (impaired control, increasing precedence over other activities, and physiological features such as tolerance and withdrawal). HAZARDOUS USE sits outside the disorders, in the chapter on factors influencing health (WHO, 2019) — check codes.",
  "IN ADOLESCENCE most substance use is EXPERIMENTAL or SOCIAL and does not progress to a disorder. Adolescent risk-taking is partly developmental: the reward system matures faster than cognitive control, and peers heighten reward sensitivity (Steinberg, 2008). Early onset and heavy use are the concern, not all use.",
  "Use is best understood FUNCTIONALLY: what does it do for this young person? Belonging, relief from anxiety, low mood or trauma memories, sleep, boredom, coping with ADHD restlessness, or income. The function shapes the plan.",
  "For the EP the job is RECOGNISE, FORMULATE, ASK ABOUT RISK AND SAFEGUARDING, SUPPORT THE SCHOOL RESPONSE, AND REFER. Substance screening and treatment are not NEPS work (Reference Part D); diagnosis is by addiction services, CAMHS (where there is co-occurring mental health difficulty) or medical colleagues."
 ],

 "what_it_is_not": [
  "NOT the same as any use. Trying alcohol or cannabis in mid-adolescence is common and most young people do not develop a disorder. Treating every disclosure as addiction damages trust and stops young people telling adults anything.",
  "NOT a moral failing or a discipline problem alone. A substance use disorder is a health condition with psychological and social drivers. Exclusion without support removes one of the strongest protective factors — connection to school.",
  "NOT made better by scare tactics. Fear-based and information-only drug education has a weak evidence base; approaches that build social and personal skills and address norms do better (Faggiano et al., 2014, Cochrane review of school-based prevention — check before quoting). Say so if a school proposes a 'shock' talk.",
  "NOT 'harmless because it's only cannabis'. Early, frequent and high-potency cannabis use is associated with increased risk of psychosis (Arseneault et al., 2002; Di Forti et al., 2019) and with poorer educational outcomes. Associations, not certainty — but real.",
  "NOT a matter only for the young person. Parental substance use is a separate, major concern: HIDDEN HARM is the term used by HSE and Tusla (2019) for the impact of parental alcohol and drug use on children. It is a child welfare and protection issue, not a diagnosis in the child.",
  "NOT something the EP assesses clinically or advises medication for. The EP does not administer drug screens, judge dependence, or advise on detox, opioid substitution or any medication (PSI 2.2.2).",
  "NOT always the primary problem. Substance use frequently sits on top of trauma, anxiety, depression or ADHD; treating use alone and ignoring the driver is a common failure."
 ],

 "prevalence": [
  "OVERALL: substance use rises steeply across adolescence; substance use DISORDER is much rarer than use. Rates vary widely by country, substance and method — rate not stated here, check before quoting.",
  "IRELAND — USE: national school surveys (ESPAD Ireland; HBSC Ireland, University of Galway; My World Survey 2, Dooley et al., 2019) report adolescent alcohol, vaping, tobacco and cannabis use. Figures change survey to survey — check the most recent edition before quoting any rate.",
  "IRELAND — TREATMENT: the HRB National Drug Treatment Reporting System (NDTRS) publishes annual data on young people entering treatment; cannabis has been reported as the main problem drug for under-18s in treatment — check the current HRB bulletin before quoting.",
  "HIDDEN HARM: a substantial minority of Irish children live with parental problem alcohol or drug use; Hope (2011) is commonly cited for an estimate — check the figure and source before quoting.",
  "SEX RATIO: historically higher in boys for disorder and heavy use; the gap has narrowed for alcohol in some surveys — check before quoting.",
  "HIGHER RISK GROUPS: young people with ADHD or conduct difficulties, those who have experienced trauma or abuse, young people in care, young people whose parents use substances problematically, those out of school, and LGBTI+ young people — rates not stated here, check."
 ],

 "cooccurring": [
  {"name": "ADHD", "rate": "elevated — rate not stated here, check",
   "presents": "early onset of use, impulsive risk-taking, cannabis used 'to calm down' or to sleep. Assess attention history separately; untreated ADHD is a risk factor, and ADHD medication decisions stay with the prescriber."},
  {"name": "CONDUCT DIFFICULTY / CONDUCT DISORDER", "rate": "strongly associated — rate not stated here, check",
   "presents": "use as part of a wider pattern of rule-breaking, older peer group, exclusion from school. The behaviour gets the response; ask what else is happening."},
  {"name": "DEPRESSION AND SELF-HARM", "rate": "elevated — rate not stated here, check",
   "presents": "alcohol or cannabis used to blunt low mood or sleep; intoxication raises the risk of impulsive self-harm. Always ask about suicidal thoughts when use and low mood co-occur."},
  {"name": "ANXIETY DISORDERS", "rate": "elevated — rate not stated here, check",
   "presents": "use before social situations or to sleep; social anxiety masked by drinking at parties. Anxiety is often the earlier target."},
  {"name": "TRAUMA / PTSD / ADVERSE CHILDHOOD EXPERIENCES", "rate": "strongly associated — rate not stated here, check",
   "presents": "use to manage intrusive memories, hyperarousal or numbness. Ask what has happened, not just what is used; trauma-informed services matter."},
  {"name": "PSYCHOSIS (cannabis-associated risk)", "rate": "uncommon but serious — rate not stated here, check",
   "presents": "unusual beliefs, suspiciousness, hearing voices, marked decline in functioning in a young person using cannabis heavily. Urgent GP / CAMHS / Early Intervention in Psychosis referral."},
  {"name": "SPECIFIC LEARNING DIFFICULTY / DLD", "rate": "elevated in young people out of school — rate not stated here, check",
   "presents": "long-standing academic failure, disengagement from school, peer group outside school. Unidentified language or literacy needs can sit under the whole picture."},
  {"name": "FOETAL ALCOHOL SPECTRUM DISORDER (in children of drinking parents)", "rate": "prenatal exposure — rate not stated here, check",
   "presents": "in the child, not the parent: attention, memory and executive difficulties, sometimes with growth or facial features. See the FASD entry; diagnosis is medical."}
 ],

 "recommendations": [
  "SAFETY AND SAFEGUARDING FIRST. Acute intoxication, overdose or unconsciousness in school is a MEDICAL EMERGENCY — 112/999. Any disclosure of harm, neglect, sexual or criminal exploitation, drug debt or intimidation → child protection route: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty (Children First Act 2015).",
  "HIDDEN HARM: where the concern is PARENTAL substance use, consider the child's safety and welfare under Children First (2017). Below the threshold for a report, Tusla's Meitheal model or family support may fit; where there is reasonable concern of neglect or harm, report. Discuss with your supervisor the same day, but supervision follows action, never replaces it.",
  "RISK: when substance use co-occurs with low mood, ask directly about suicidal thoughts and self-harm, and follow the same-day risk route if present.",
  "FORMULATE THE FUNCTION. Write what the use does for the young person (belonging, relief, sleep, coping) and what maintains it. Recommend support for the driver — anxiety, low mood, trauma, ADHD, learning need — not only the substance.",
  "REFER: HSE drug and alcohol services for young people (e.g., adolescent addiction or youth drug and alcohol services, Youth Health Service where available — names and age ranges vary by area, check locally); GP; CAMHS where there is moderate to severe co-occurring mental health difficulty (check local acceptance criteria for dual diagnosis); Local and Regional Drug and Alcohol Task Force youth projects. HSE Drugs and Alcohol Helpline and drugs.ie for information — check the number is current.",
  "IN SCHOOL — KEEP HIM IN. Recommend that any sanction under the Code of Behaviour sits alongside support, and that exclusion is a last resort; school connectedness is protective. Check the school's substance use policy (Department of Education and Science, 2002 guidelines — check for updates).",
  "A NAMED ADULT who can have a brief, non-judgemental conversation using SAOR (Support, Ask and assess, Offer assistance, Refer — the HSE brief intervention model; check the current edition) or motivational interviewing principles (Miller & Rollnick, 2013). Curiosity, not interrogation.",
  "WHOLE-SCHOOL: prevention through SPHE, social and personal skills, and accurate norms ('most students your age are not doing this'), not shock tactics. In the West of Ireland, the Planet Youth (Icelandic model) community approach has been piloted — check local involvement.",
  "CONTINUUM LEVEL: School Support, or School Support Plus where addiction services, CAMHS or Tusla are involved. Coordinate so the school plan and the service plan match.",
  "DO NOT diagnose a substance use disorder, advise on medication, detox or drug testing, or promise confidentiality about risk. DO NOT recommend exclusion as the intervention."
 ],

 "explain_parent": [
  "'A lot of young people try alcohol or cannabis. Most don't go on to have a serious problem. What we're looking at is how often, how much, and what it's doing for him — and what it's costing him.'",
  "'Very often young people use to manage something else — worry, low mood, sleep, fitting in. If we only focus on the drink or the drugs, we miss that.'",
  "'Keeping the conversation open at home is the most protective thing. Calm, curious questions — \"what's it like for you?\" — get further than lectures or searches, even though the worry is huge.'",
  "'If he's ever very drunk or you can't wake him, that's an emergency — ring 112 or 999 and put him in the recovery position. Don't wait.'",
  "'The next step is the youth drug and alcohol service or the GP. They're used to working with families, not just the young person. I'll write to support the referral.'",
  "SIGNPOST: GP; HSE Drugs and Alcohol Helpline and drugs.ie; local youth drug and alcohol service; Family Support Network groups for families affected by a relative's drug use; Al-Anon/Alateen for families affected by alcohol. Check names, numbers and local availability before giving them."
 ],

 "explain_teacher": [
  "'Most substance use at this age is experimental. The things that worry me are frequency, using alone or in school, using to cope, and falling attendance or grades.'",
  "'He's more likely to talk to an adult who stays calm and curious than one who reacts. You don't have to be an expert — \"I've noticed you seem wrecked in the mornings; what's going on?\" is enough to open it.'",
  "'Keeping him in school is protective. Suspension without support usually means more unsupervised time with the same peer group.'",
  "'If he seems intoxicated or unwell, treat it as a medical issue first — don't leave him alone, get first aid and ring 112 if he's not responsive.'",
  "'If there's any hint of someone older supplying him, drug debt, threats, or harm at home, that goes to the DLP today, and it's a Tusla report. Don't promise to keep it secret.'",
  "'If a student is caring for a parent who drinks or uses, you may see tiredness, lateness, missing homework and worry. That's Hidden Harm — tell the DLP, and be kind about the homework.'"
 ],

 "explain_child": [
  "YOUNGER (Hidden Harm — a child worried about a parent): 'Sometimes grown-ups drink too much or take drugs, and it can make home feel scary or confusing. It is never your fault, and it's not your job to fix it. It's OK to tell someone.'",
  "OLDER: 'I'm not here to give out or tell you what to do. I'm interested in what it does for you — the good bits and the not-so-good bits. Lots of people use to cope with stuff. Let's figure out what's going on.'",
  "EXPLAIN CONFIDENTIALITY FIRST: 'Most of what we talk about stays between us. If I think you or someone else is in danger — like being hurt, threatened or pushed into something — I'll have to tell someone who can help, and I'll tell you first.'",
  "ASK (motivational, not interrogating): 'What do you like about it? What are the not-so-good things? On a scale of 0 to 10, how much do you want anything to change?'",
  "ASK ABOUT SAFETY PLAINLY: 'Have you ever been really unwell after using? Has anyone ever put pressure on you to carry or sell, or said you owe them?' And, where mood is low: 'Have you had thoughts of hurting yourself?'",
  "AVOID: 'Just say no', 'you're throwing your life away', 'druggie', threatening to tell parents or gardaí as leverage. These end the conversation."
 ],

 "analogies": [
  "THE PAINKILLER: 'For a lot of young people it's a painkiller for something else — worry, sadness, a bad memory. Take the painkiller away without treating the pain, and they'll find another one.' Works with parents and teachers; shifts focus to function.",
  "THE ACCELERATOR AND THE BRAKES: 'In the teenage brain the accelerator — the part that loves excitement and friends — is fully built before the brakes are. That's normal; it's why friends and risk go together at this age.' Based on Steinberg (2008); works with parents and adolescents.",
  "THE SEESAW (decisional balance): 'On one side are the things you like about it, on the other the things that cost you. We're just looking at what's on each side.' Works with older adolescents; the core of a motivational conversation.",
  "THE BACKPACK (Hidden Harm): 'Some children come to school carrying a heavy backpack from home that nobody can see — worry, broken sleep, looking after a parent.' Works with teachers."
 ],

 "language": [
  "PERSON-FIRST, NON-STIGMATISING: 'young person who uses drugs', 'substance use', 'alcohol problem'. Avoid 'addict', 'junkie', 'druggie', 'alco', 'clean/dirty' (for test results).",
  "'Substance use disorder' only where diagnosed. Otherwise describe: 'reports using cannabis most weekends', in the young person's own words where possible.",
  "'Harm reduction' is an accepted, evidence-informed public health approach and part of Irish national drug strategy (Department of Health, 2017); it is not 'condoning'. Use the term accurately.",
  "'Hidden Harm' for the impact of parental substance use on children — the HSE/Tusla term (2019). Avoid describing parents as 'alcoholics' or 'addicts' in reports; describe impact on the child.",
  "In reports, record what was observed and what was said, and label opinion as opinion (PSI 1.2.8). Consider carefully what goes in a report that may be shared — disclosures of illegal activity need a supervisor discussion before being written."
 ],

 "red_flags": [
  "RED FLAG — intoxication, overdose, unconsciousness, seizure or chest pain: MEDICAL EMERGENCY, 112/999. Do not leave the young person alone.",
  "RED FLAG — criminal or sexual exploitation, drug debt, intimidation, older adults supplying, or harm or neglect at home linked to parental use. Child protection route: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty under the Children First Act 2015. Gardaí where there is immediate danger.",
  "RED FLAG — substance use with suicidal ideation or self-harm. Same-day risk route: supervisor the same day, parents unless that increases risk, GP/CAMHS, ED or emergency services if imminent. Supervision follows action; it does not replace it.",
  "RED FLAG — new unusual beliefs, suspiciousness, hearing voices or rapid decline in a young person using cannabis or stimulants. Urgent GP / CAMHS / Early Intervention in Psychosis referral.",
  "BOUNDARY — you do not screen clinically, diagnose, drug-test, or advise on medication, detox or substitution treatment (PSI 2.2.2). Substance screening is not NEPS work — refer (Reference Part D).",
  "WATCH — the quiet young person who is tired, late and anxious about home. Hidden Harm is under-reported because children protect their parents.",
  "WATCH — your own reactions. Judgement, alarm or collusion ('it's only a bit of weed') both close down the conversation and distort the formulation."
 ],

 "child_voice": [
  "SOLUTION-FOCUSED PUPIL INTERVIEW with scaling — good because it gives the young person control, looks for times when things were better, and does not start from the problem the adults have named.",
  "DECISIONAL BALANCE (pros and cons grid) — good because it is the core motivational interviewing tool (Miller & Rollnick, 2013): the young person names their own reasons, and ambivalence becomes visible without an argument.",
  "A TYPICAL-DAY OR TIMELINE INTERVIEW — good because it shows when and with whom use happens, what comes before it, and what it replaces, which is the functional formulation in the young person's words.",
  "RCADS OR MFQ SELF-REPORT completed WITH the young person — good because anxiety and low mood are common drivers, and the EP stays present to follow up any risk item the same session.",
  "DRAWINGS, 'THREE HOUSES' OR 'MY WORLD' TRIANGLE for younger children affected by Hidden Harm — good because they allow a child to show home life without having to 'tell on' a parent directly. Follow any disclosure through the child protection route.",
  "SPUNOUT and DRUGS.IE youth-facing materials — Irish, non-judgemental, accurate. Good because young people often check facts privately. → https://spunout.ie/ · https://www.drugs.ie/"
 ],

 "questions": [
  "Q: 'Should we search his room / drug-test him?' — A: 'That's a family decision and I wouldn't advise on testing. What I'd say is that searching and testing can damage trust, which is the thing that keeps him talking to you. The youth drug and alcohol service can talk through this with you.'",
  "Q: 'Is cannabis really that harmful? Everyone says it's natural.' — A: 'For most occasional users the risks are modest, but for young people using often, especially strong cannabis, there's a real link with mental health problems including psychosis, and with doing less well at school. Age and frequency matter.'",
  "Q: 'Will the school expel her?' — A: 'That's for the school under its Code of Behaviour, and I can't promise an outcome. What I'll recommend is that support sits alongside any sanction, because being in school is one of the things that protects her.'",
  "Q: 'Will you tell the guards?' — A: 'My job is her welfare, not policing. If I thought she or someone else was in danger — being threatened or exploited — I'd have to act, and that might involve Tusla or gardaí. I'd tell her first.'",
  "Q: 'Is this our fault?' — A: 'There's rarely one cause. Friends, stress, how she's feeling, what's around — all play a part. Blame won't help; staying connected and getting support will.'",
  "Q (teacher): 'He told me he drinks every weekend and asked me not to tell anyone.' — A: 'You don't need to panic, but don't promise secrecy. Tell him you're glad he told you and that you'll need to talk to the DLP so he gets support. Then go today. If there's anything about harm, exploitation or danger, it's a Tusla report.'",
  "Q (teacher): 'A child in my class says her mam is \"always sick\" and she has to mind the babies.' — A: 'That could be Hidden Harm. Record exactly what she said, don't question her further, and go to the DLP today. Think about whether it meets the threshold for a Tusla report — if in doubt, consult Tusla.'"
 ],

 "supervision": [
  "Rehearse a non-judgemental opening question about substance use, and what you say if the answer is 'yes, every day'.",
  "Clarify the local routes: which HSE drug and alcohol service sees under-18s, what age ranges, whether CAMHS accepts dual diagnosis, and the local Drug and Alcohol Task Force youth projects.",
  "Discuss thresholds: adolescent use alone vs exploitation, drug debt, parental use and neglect — when is it a Tusla report, and who makes it (you, as a mandated person)?",
  "Discuss what to record in a report about illegal activity disclosed by a young person, and how to balance accuracy with PSI 1.2.8.",
  "Bring your own reactions — to drug use, to parents who use, or from personal or family experience. These shape practice and belong in supervision.",
  "Ask how the service responds after a drug-related death or critical incident in a school community."
 ],

 "reflection": [
  "ON STANCE — did I stay curious and non-judgemental, or did alarm or disapproval show? What did the young person do next?",
  "ON FUNCTION — did I formulate what the use does for this young person, or only record what and how much?",
  "ON SAFEGUARDING — did I ask about exploitation, debt, home and parental use? If a threshold was met, did I report to Tusla myself, and did supervision come after action?",
  "ON RISK — where mood was low, did I ask directly about suicidal thoughts?",
  "ON THE SCHOOL RESPONSE — did my recommendations keep the young person connected to school, or did they read as support for exclusion?",
  "ON MY ROLE — did I stay out of drug testing, detox and medication advice while still being useful?",
  "WHAT GOOD LOOKS LIKE: 'Referral: \"smoking cannabis at lunch\". In interview he said it was the only thing that stopped the racing thoughts at night. I asked about low mood (yes), self-harm (no), debt (no). The formulation named anxiety and sleep; the recommendations were a named adult, GP and youth drug and alcohol service referral, and school support instead of suspension.'",
  "WHAT POOR LOOKS LIKE: 'Student admits drug use. Recommend strict sanctions and parents to monitor.' — no function, no risk, no safeguarding, no referral."
 ],

 "citations": [
  CIT_DSM,
  CIT_ICD,
  CIT_STEIN,
  CIT_MR,
  CIT_DOH,
  CIT_HH,
  CIT_CF,
  "Arseneault, L., Cannon, M., Poulton, R., Murray, R., Caspi, A., & Moffitt, T. E. (2002). Cannabis use in adolescence and risk for adult psychosis: Longitudinal prospective study. BMJ, 325(7374), 1212–1213.",
  "Di Forti, M., Quattrone, D., Freeman, T. P., Tripoli, G., Gayer-Anderson, C., Quigley, H., et al. (2019). The contribution of cannabis use to variation in the incidence of psychotic disorder across Europe (EU-GEI): A multicentre case-control study. The Lancet Psychiatry, 6(5), 427–436.",
  "Faggiano, F., Minozzi, S., Versino, E., & Buscemi, D. (2014). Universal school-based prevention for illicit drug use. Cochrane Database of Systematic Reviews, 2014(12), CD003020. — check before quoting."
 ],

 "pathway": {
  "age": "Use typically begins in mid-adolescence; concern in schools usually surfaces in the post-primary years, via an incident in school, falling attendance, a change of peer group or a disclosure. A disorder is rarely identified before mid-adolescence. In primary school the substance issue is almost always PARENTAL (Hidden Harm), not the child's own use.",
  "who_diagnoses": "Ireland: HSE addiction / drug and alcohol services (adolescent or youth services where they exist — check locally), CAMHS where there is significant co-occurring mental health difficulty (check dual diagnosis acceptance), GP, and adult addiction services from 18. Medication (e.g., detox, substitution) is prescribed only by a doctor.",
  "who_wrote_report": "Youth drug and alcohol service key worker or clinician; CAMHS psychiatrist or psychologist; GP letter; Tusla social worker (for Hidden Harm or welfare concerns); probation or Garda Youth Diversion Project worker. A school incident report is not an assessment.",
  "refer_to": "HSE youth drug and alcohol service or adolescent addiction service (check local name and age range); GP; CAMHS for co-occurring moderate to severe mental health difficulty; Tusla where harm, neglect, exploitation or Hidden Harm concerns meet threshold (or Meitheal below it); ED / 112 for intoxication or overdose; Early Intervention in Psychosis where available.",
  "sooner": "'Young people are very good at keeping this from adults, and it usually starts as something lots of teenagers try. You noticed it's become a problem, and you're here — that's what matters now.'"
 },

 "differential": [
  "EXPERIMENTAL OR SOCIAL USE WITHOUT DISORDER — occasional use, no loss of control, no impairment. Common; respond with information and connection, not a treatment referral.",
  "SELF-MEDICATION OF ANOTHER CONDITION — anxiety, depression, PTSD, ADHD or insomnia driving use. The underlying condition may be the primary need.",
  "CONDUCT DISORDER — use as one part of a broad pattern of rule-breaking; both may apply.",
  "PSYCHOSIS OR BIPOLAR DISORDER — unusual beliefs, perceptual changes or elevated mood; substance-induced vs primary is a psychiatric judgement. Urgent referral.",
  "MEDICAL CAUSES of apparent intoxication — hypoglycaemia (diabetes), head injury, seizures, prescribed medication effects. Treat as medical until known otherwise.",
  "HIDDEN HARM WITHOUT CHILD USE — the child's tiredness, lateness, worry or behaviour driven by a parent's substance use."
 ],

 "next": [
  "If there is a medical emergency, risk to life or a child protection concern: act first (112, same-day risk route, Tusla report), then inform your supervisor.",
  "Meet the young person with a non-judgemental, motivational stance; formulate the function of use and screen for mood, anxiety and trauma drivers.",
  "Support a referral to the local youth drug and alcohol service or GP, with a brief factual letter; link with CAMHS where mental health needs are significant.",
  "Agree a school plan at School Support or School Support Plus: named adult, attendance, support alongside sanctions, review date."
 ],

 "presentations": [
  "Adolescent substance misuse / dual diagnosis",
  "Risk-taking without a diagnosis attached",
  "Group dynamics and peer influence",
  "Falling attendance and disengagement from school",
  "Parental substance use (Hidden Harm) affecting the child",
  "Low mood with alcohol or cannabis used to cope",
  "Sleep disruption and daytime tiredness"
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — for the child's own use. Relevant only as family context: parental substance use (Hidden Harm) and prenatal exposure (see FASD).",
   "prevalence": "Not applicable for the child's own use; Hidden Harm exposure rate not stated here — check.",
   "see": "No substance use disorder in the child. What you may see is the impact of parental use: inconsistent care, missed appointments, developmental delay, unsettled or hypervigilant behaviour. That is a welfare and protection question — Children First (2017) and Tusla — and possibly an FASD question for medical colleagues.",
   "tools": []
  },
  "School Age": {
   "applies": "RARELY — own use is rare in primary; the common issue is FAMILY CONTEXT (parental substance use = Hidden Harm, a child protection and welfare matter for Tusla).",
   "prevalence": "Own use: rare, rate not stated here. Hidden Harm: Irish estimates exist (e.g., Hope, 2011) — check before quoting.",
   "see": "Tiredness, lateness, hunger, missed homework, anxiety about home, caring for siblings or a parent, reluctance to go home. Occasionally early experimentation in senior classes, usually with older siblings or peers. Respond through the DLP and Tusla (report or Meitheal depending on threshold); support the child in school.",
   "tools": ["SDQ", "RCADS", "Piers-Harris 3"]
  },
  "Adolescent": {
   "applies": "YES — main band. Use rises steeply through post-primary; most is experimental, a minority develops a disorder.",
   "prevalence": "Use: see ESPAD / HBSC Ireland (latest edition) — check before quoting. Disorder: much lower, rate not stated here.",
   "see": "Incidents in school, smell of cannabis, change in peer group, money problems, falling attendance and grades, sleep disruption, low mood or anxiety. Formulate function; ask about mood, self-harm, exploitation and home. Clinical screening sits with health services.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "SDQ", "BASC-3 SRP",
             "CRAFFT 2.1 — AGE 12–21 · MEASURES: brief screen for risky alcohol and drug use (health-setting tool; Knight et al., 1999, current version from Boston Children's Hospital — check) · CANNOT TELL YOU: diagnosis, severity or function; not for EP administration without service agreement · TIME: 2–5 min"]
  },
  "Young Adult": {
   "applies": "YES — peak age for heavy episodic drinking and some drug use; usually adult services territory. EP role is recognition, risk response and referral (e.g., in Youthreach, further education or transition work).",
   "prevalence": "See HRB Irish National Drug and Alcohol Survey (latest edition) — check before quoting.",
   "see": "Use tied to transitions — leaving school, college, work, living independently. Services change at 18; CAMHS-to-adult and youth-to-adult addiction transitions are risk points. Refer via GP, adult HSE addiction services or college health/counselling services.",
   "tools": ["Adult self-report measures via the service", "BASC-3 SRP"]
  },
  "Special Setting": {
   "applies": "RARELY — own use is less common but may be missed; vulnerability to exploitation is higher. Hidden Harm applies as in all settings.",
   "prevalence": "Rate not stated here — check.",
   "see": "Young people with intellectual disability or autism may be more vulnerable to being given substances or used to carry or sell by others. Change from baseline behaviour, money going missing, new 'friends'. Treat exploitation as a child protection matter (Tusla); involve CDNT and families.",
   "tools": ["SDQ", "Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)"]
  }
 },
})

# ============================================================================ 2 · GAMBLING DISORDER
CONDS.append({
 "name": "Gambling Disorder",
 "code": ("DSM-5-TR Gambling Disorder (Non-Substance-Related Disorders, within Substance-Related and Addictive "
          "Disorders) · ICD-11 6C50 Gambling disorder (6C50.0 predominantly offline · 6C50.1 predominantly "
          "online) · hazardous gambling QE21 (not a disorder) — check codes before quoting"),
 "neps": NEPS_ADD,
 "coru": CORU,
 "psi": PSI,
 "law": LAW_GAMB,

 "what_it_is": [
  "A persistent and recurrent pattern of problematic gambling leading to clinically significant impairment or distress. DSM-5-TR requires at least FOUR of NINE criteria in 12 months; severity mild = 4–5, moderate = 6–7, severe = 8–9 (APA, 2022).",
  "The nine criteria: needing to gamble with increasing amounts; restlessness or irritability when cutting down; repeated failed attempts to stop; preoccupation; gambling when distressed; CHASING LOSSES; lying to conceal gambling; jeopardising a relationship, job or education; relying on others for money to relieve a desperate financial situation (APA, 2022).",
  "DSM-5 (2013) moved it from the impulse-control chapter ('pathological gambling', DSM-IV) to sit alongside substance use disorders, reflecting shared features of reward, craving and loss of control. Older reports may say 'pathological gambling' or 'compulsive gambling'.",
  "ICD-11 defines it by IMPAIRED CONTROL, INCREASING PRIORITY given to gambling over other interests, and CONTINUATION DESPITE NEGATIVE CONSEQUENCES, with significant impairment, normally evident over at least 12 months (WHO, 2019). ICD-11 separates online and offline gambling — check subcodes.",
  "IN ADOLESCENCE gambling is increasingly DIGITAL and blurred with gaming: online betting (often on a parent's or older friend's account), in-game LOOT BOXES, skin betting, social casino games and sports betting normalised through advertising. The legal gambling age in Ireland is 18.",
  "The harms go beyond the individual: debt, theft from family, conflict, and, in adults, elevated suicidality (Karlsson & Håkansson, 2018). PARENTAL gambling can harm children in the same way as parental substance use — financial hardship, conflict and neglect.",
  "The EP recognises, formulates, asks about risk and safeguarding, supports the family and school, and refers. Diagnosis and treatment sit with specialist addiction services, CAMHS (where co-occurring) or GP."
 ],

 "what_it_is_not": [
  "NOT the same as having a bet. Many adolescents gamble occasionally (a Lotto ticket from a parent, a bet on a match) without harm. The disorder is about loss of control, escalating priority and harm.",
  "NOT only about money. Young people may have little money; the features to watch are preoccupation, lying, chasing losses, borrowing or stealing, and use to escape mood.",
  "NOT 'just a game' when it involves loot boxes or skin betting. Research shows a consistent association between loot-box spending and problem gambling symptoms in adolescents and adults (Zendle & Cairns, 2018; Spicer et al., 2022). Association, not proven cause — but worth asking about.",
  "NOT a sign of bad character or greed. Gambling products are designed to reward intermittently, which strongly maintains behaviour (variable-ratio reinforcement, Skinner). The environment matters as well as the person.",
  "NOT something the EP diagnoses or treats. The EP describes, formulates and refers (PSI 2.2.2).",
  "NOT always the primary problem. Gambling can be a way of escaping low mood, anxiety or trauma, and often co-occurs with substance use and ADHD."
 ],

 "prevalence": [
  "OVERALL — ADOLESCENTS: a systematic review found problem gambling prevalence among adolescents ranged from 0.2% to 12.3% across studies, depending on country, measure and time frame (Calado, Alexandre & Griffiths, 2017) — check before quoting; the wide range reflects measurement differences.",
  "IRELAND: gambling questions appear in ESPAD Ireland and in the HRB Irish National Drug and Alcohol Survey (adults and older adolescents) — check the latest editions before quoting any rate.",
  "SEX RATIO: problem gambling is consistently reported as more common in boys and young men (Calado et al., 2017) — ratio not stated here, check.",
  "LOOT BOXES: many adolescent gamers report buying loot boxes; exact proportions vary by study — rate not stated here, check (see Zendle & Cairns, 2018; Spicer et al., 2022).",
  "HIGHER RISK GROUPS: young people with ADHD, substance use, a parent with a gambling problem, and heavy sports-betting peer groups — rates not stated here, check."
 ],

 "cooccurring": [
  {"name": "SUBSTANCE USE", "rate": "commonly co-occurs — rate not stated here, check",
   "presents": "alcohol or cannabis use alongside betting, often in the same peer group; each lowers restraint on the other. Ask about both."},
  {"name": "ADHD", "rate": "elevated — rate not stated here, check",
   "presents": "impulsivity, reward-seeking and difficulty delaying gratification; fast online products suit this profile. Assess attention separately."},
  {"name": "DEPRESSION AND SUICIDALITY", "rate": "elevated — rate not stated here, check",
   "presents": "gambling to escape low mood, then low mood worsened by losses, debt and shame. Ask directly about suicidal thoughts (Karlsson & Håkansson, 2018, adult register data)."},
  {"name": "ANXIETY DISORDERS", "rate": "elevated — rate not stated here, check",
   "presents": "gambling as escape from worry; anxiety about debt and discovery. Anxiety may be driver and consequence."},
  {"name": "GAMING DISORDER / HEAVY GAMING", "rate": "overlapping — rate not stated here, check",
   "presents": "loot boxes, skin betting and in-game purchases in a young person who games heavily. The line between gaming and gambling is blurred by design."},
  {"name": "CONDUCT DIFFICULTY", "rate": "associated — rate not stated here, check",
   "presents": "stealing from family or others to fund gambling, lying, conflict at home. Ask what the money is for."}
 ],

 "recommendations": [
  "SAFETY AND SAFEGUARDING FIRST. Debt to older people, threats, pressure to steal or carry, or harm at home → child protection route: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty (Children First Act 2015). Gardaí where there is immediate danger.",
  "RISK: ask directly about suicidal thoughts where there is low mood, debt or shame. Same-day risk route if present; supervision follows action.",
  "PARENTAL GAMBLING: consider the child's welfare in the same way as Hidden Harm — financial hardship, conflict, neglect. Welfare concerns may fit Meitheal / family support; reasonable concern of harm or neglect is a Tusla report.",
  "FORMULATE THE FUNCTION: excitement, belonging (betting with friends on matches), escape from mood, or trying to win back losses (chasing). Recommend support for the driver as well as the behaviour.",
  "PRACTICAL HARM REDUCTION WITH THE FAMILY: remove saved card details from devices and gaming accounts, use platform spending limits and parental controls, and check whether a parent's betting account is being used. Frame this as reducing access, not punishment.",
  "REFER: GP; HSE addiction services (some provide gambling treatment — check locally for under-18s); CAMHS where there is significant co-occurring mental health difficulty; national gambling support services and helplines — check current Irish services, including any established under the Gambling Regulation Act 2024 and the Gambling Regulatory Authority of Ireland.",
  "IN SCHOOL: support digital and financial literacy through SPHE (odds, how products are designed, advertising); do not treat sports betting chat as harmless background. A named adult who can check in.",
  "CONTINUUM LEVEL: School Support, or School Support Plus where outside services are involved.",
  "DO NOT diagnose Gambling Disorder, advise on medication, or promise confidentiality about risk or exploitation. DO NOT shame; shame drives concealment."
 ],

 "explain_parent": [
  "'Gambling for young people now is mostly on phones — betting apps, often on someone else's account, and things inside games like loot boxes that work in a very similar way.'",
  "'The warning signs aren't just the money. It's thinking about it all the time, lying about it, trying to win back what's been lost, and getting irritable when he can't.'",
  "'Very practical steps help: take saved card details off phones, consoles and game accounts, set spending limits, and check that no one's betting account is being used. That's about access, not punishment.'",
  "'If he owes money to anyone, or anyone is pressuring him, I need to know, because that's a safety issue.'",
  "'The next step is the GP and the local addiction service or a gambling support service. I'll write to support that, and I'll check what's available for his age here.'",
  "SIGNPOST: GP; HSE addiction services (check which accept under-18s); national problem-gambling helplines and Gamblers Anonymous / GamAnon for families; Webwise for parental controls. Check names, numbers and local availability before giving them."
 ],

 "explain_teacher": [
  "'Gambling at this age is mostly online and very normalised — sports betting chat, apps, loot boxes. It's worth taking seriously when it's constant, secretive or linked to money trouble.'",
  "'Signs: preoccupation, checking odds or scores all day, borrowing money, selling things, stealing, mood swings linked to results.'",
  "'If a student mentions owing money, being threatened or being asked to do things to pay off a debt, go to the DLP today. That's a child protection concern.'",
  "'In SPHE, teaching how odds and games are designed is more effective than warnings. Young people respond to being treated as smart enough to spot manipulation.'",
  "'If a student seems really low after losses, ask how they are and pass it on. Gambling is linked with low mood and, in some people, suicidal thinking.'"
 ],

 "explain_child": [
  "YOUNGER (loot boxes and in-game spending): 'Some games have mystery boxes you pay for without knowing what's inside. They're designed to make you want to keep opening them. It's not your fault if it's hard to stop — lots of grown-ups find it hard too.'",
  "OLDER: 'Betting apps and games are designed by clever people to keep you coming back. It's not a weakness to get hooked — it's what they're built for. What I want to know is what it's like for you.'",
  "EXPLAIN CONFIDENTIALITY FIRST: 'Most of this stays between us. If you tell me you're in danger — like someone threatening you over money — I'll need to get help, and I'll tell you first.'",
  "ASK: 'When you lose, what do you do next?' (chasing). 'Has it ever made you lie or borrow money?' 'What would you be doing if you weren't betting?'",
  "ASK ABOUT MOOD AND SAFETY: 'Does it ever leave you feeling really low? Have you had thoughts of hurting yourself?' 'Do you owe anyone money?'",
  "AVOID: 'Gambling is for losers', 'you're stupid to fall for it'. Shame drives secrecy."
 ],

 "analogies": [
  "THE SLOT MACHINE IN THE POCKET: 'The app is a slot machine that never closes and is always in his pocket.' Works with parents; explains availability and why access matters.",
  "THE MYSTERY BAG: 'A loot box is a mystery bag you pay for — sometimes something great, usually not. Not knowing is what keeps you buying.' Works with younger children and parents; explains intermittent reward.",
  "DIGGING TO GET OUT OF A HOLE: 'Chasing losses is like digging deeper to get out of a hole.' Works with adolescents; names chasing without blame.",
  "THE HOUSE ALWAYS WINS: 'The odds are built so the company wins over time — that's the business.' Works with older adolescents in SPHE and in interview; builds critical thinking."
 ],

 "language": [
  "'Gambling Disorder' only where diagnosed. Otherwise: 'gambling that is causing harm', 'problem gambling', or describe behaviour in the young person's words.",
  "Avoid 'compulsive gambler', 'degenerate', 'addict'. Older reports may use 'pathological gambling' (DSM-IV) — translate it for families.",
  "'Gambling harm' is increasingly used in public health to include harm to families and communities, not only the individual. Useful when talking about parental gambling.",
  "In reports, describe frequency, spending, debt, concealment and impact; label opinion as opinion (PSI 1.2.8). Do not record details of other people's illegal activity without supervisor discussion."
 ],

 "red_flags": [
  "RED FLAG — debt to older people, threats, intimidation, pressure to steal, sell or carry. Child protection route: report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty under the Children First Act 2015. Gardaí where there is immediate danger.",
  "RED FLAG — suicidal ideation, hopelessness or self-harm linked to losses or debt. Same-day risk route: supervisor the same day, parents unless that increases risk, GP/CAMHS, ED or emergency services if imminent. Supervision follows action; it does not replace it.",
  "RED FLAG — parental gambling with children going without food, heat or care, or domestic conflict and violence. Welfare/protection concern — Tusla.",
  "BOUNDARY — you do not diagnose Gambling Disorder or advise on medication or treatment (PSI 2.2.2). Describe, formulate and refer.",
  "WATCH — stealing from home or school, selling possessions, sudden money or new items. Ask what it is funding before treating it as conduct alone.",
  "WATCH — heavy loot-box or in-game spending in a younger child. Not a diagnosis, but a conversation with parents about access and design."
 ],

 "child_voice": [
  "SOLUTION-FOCUSED INTERVIEW with scaling — good because it finds times when the young person was in control and builds from their own goals rather than the adults' alarm.",
  "DECISIONAL BALANCE (pros and cons) — good because motivational interviewing principles (Miller & Rollnick, 2013) let the young person name the costs themselves, which predicts change better than being told.",
  "A WEEK TIMELINE of when betting or buying happens, with mood before and after — good because it shows triggers (boredom, matches, low mood, payday) and the function in the young person's terms.",
  "MFQ OR RCADS SELF-REPORT completed with the young person — good because low mood and anxiety commonly sit alongside; the EP follows up any risk item in the session.",
  "WEBWISE and SPUNOUT materials on online gambling and in-game spending — Irish and youth-facing. Good because they respect the young person's intelligence. → https://www.webwise.ie/ · https://spunout.ie/"
 ],

 "questions": [
  "Q: 'He's only 15 — how can he even gamble?' — A: 'Mostly online: a parent's or older friend's account, apps that don't check age properly, or gambling-style features inside games like loot boxes and skin betting. It's worth checking whose account is being used.'",
  "Q: 'Are loot boxes gambling?' — A: 'Legally that depends on the country, and it's still being debated. What research shows is that heavy loot-box spending goes along with problem gambling symptoms. It's worth treating as a warning sign and setting limits.'",
  "Q: 'Should we pay off his debt?' — A: 'That's a family decision, and it's worth getting advice from the gambling service first. If the debt is to someone threatening him, that's a safety issue and needs a different response — please tell me.'",
  "Q: 'Is it our fault? His dad bets.' — A: 'Seeing betting as normal at home can play a part, but blame won't help. Support for the whole family, including your husband if he wants it, can help everyone.'",
  "Q: 'Will he grow out of it?' — A: 'Many young people's gambling does settle, but some go on to have problems as adults, especially if it starts early and heavily. That's why acting now makes sense.'",
  "Q (teacher): 'Half my class talk about accumulators every Monday — is that a problem?' — A: 'It shows how normal betting has become. It's a good moment for SPHE on odds and design. The individual students I'd worry about are those who are preoccupied, secretive, borrowing, or very up and down with results.'"
 ],

 "supervision": [
  "Clarify which local services treat gambling in under-18s and young adults — this varies and changes, especially as the Gambling Regulatory Authority of Ireland beds in.",
  "Discuss how to ask about debt and exploitation, and the threshold for a Tusla report.",
  "Bring any case where money was going missing and the explanation was assumed to be conduct — was gambling asked about?",
  "Rehearse the conversation with parents about practical access controls without it becoming blame.",
  "Discuss your own views on gambling and betting culture (e.g., in sport) and how they shape your responses."
 ],

 "reflection": [
  "ON ASKING — did I ask about online betting, loot boxes and in-game spending, or assume gambling was only for adults?",
  "ON FUNCTION — did I understand what gambling does for this young person (excitement, belonging, escape, chasing)?",
  "ON SAFEGUARDING — did I ask about debt and pressure from others? If a threshold was met, did I report to Tusla myself?",
  "ON RISK — where there were losses, shame or low mood, did I ask directly about suicidal thoughts?",
  "ON THE FAMILY — did I consider parental gambling and its impact on the child, without blame?",
  "WHAT GOOD LOOKS LIKE: 'Referral: money missing from school tuck shop. In interview he described betting on his brother's account most nights and chasing losses. I asked about mood (low), suicidal thoughts (none), debt (owes a friend €60, no threats). Parents removed card details, the GP referral went in, and SPHE covered odds with the class.'",
  "WHAT POOR LOOKS LIKE: 'Student involved in theft. Recommend behaviour contract.' — gambling not asked about, no function, no risk, no referral."
 ],

 "citations": [
  CIT_DSM,
  CIT_ICD,
  "Calado, F., Alexandre, J., & Griffiths, M. D. (2017). Prevalence of adolescent problem gambling: A systematic review of recent research. Journal of Gambling Studies, 33(2), 397–424.",
  "Zendle, D., & Cairns, P. (2018). Video game loot boxes are linked to problem gambling: Results of a large-scale survey. PLOS ONE, 13(11), e0206767.",
  "Spicer, S. G., Nicklin, L. L., Uther, M., Lloyd, J., Lloyd, H., & Close, J. (2022). Loot boxes, problem gambling and problem video gaming: A systematic review and meta-synthesis. New Media & Society, 24(4), 1001–1022. — check details before quoting.",
  "Karlsson, A., & Håkansson, A. (2018). Gambling disorder, increased mortality, suicidality, and associated comorbidity: A longitudinal nationwide register study. Journal of Behavioral Addictions, 7(4), 1091–1099.",
  CIT_MR,
  CIT_CF,
  "Gambling Regulation Act 2024 (Ireland). https://www.irishstatutebook.ie/ — check commencement and current provisions."
 ],

 "pathway": {
  "age": "Gambling behaviour can begin in late primary through gaming-linked features (loot boxes, in-game spending) and becomes more common in post-primary, especially among boys around sport. Problems usually surface in the mid-to-late teens through missing money, debt, conflict at home or a disclosure; disorder is more often identified in young adulthood.",
  "who_diagnoses": "Ireland: HSE addiction services and specialist gambling treatment services (check which see under-18s locally); CAMHS where there is significant co-occurring mental health difficulty; GP; adult services and private clinicians from 18. Medication is a medical decision only.",
  "who_wrote_report": "Addiction service counsellor or clinician; CAMHS psychiatrist or psychologist; GP letter; Tusla social worker where family harm is involved; Garda Youth Diversion Project worker where theft was involved. A school incident report is not an assessment.",
  "refer_to": "GP; HSE addiction services / gambling treatment service (check local age range); CAMHS for co-occurring moderate to severe mental health difficulty; Tusla where debt, exploitation or family harm meets threshold; ED / emergency services if suicide risk is imminent.",
  "sooner": "'Gambling is one of the easiest things to hide — there's no smell, no stagger, and it's all on a phone. You noticed, and that's what matters now.'"
 },

 "differential": [
  "RECREATIONAL GAMBLING WITHOUT DISORDER — occasional, within limits, no chasing, no concealment, no harm.",
  "BIPOLAR DISORDER (manic or hypomanic episode) — DSM-5-TR excludes gambling better explained by a manic episode (APA, 2022). Elevated mood, reduced need for sleep and grandiosity — urgent medical referral.",
  "CONDUCT DISORDER — stealing and lying as part of a broad pattern rather than to fund gambling. Both may apply.",
  "GAMING DISORDER / HEAVY GAMING — preoccupation with gaming, where spending is incidental. Loot boxes blur the line.",
  "SUBSTANCE USE — money going to drugs or alcohol, not gambling. Ask what the money is for."
 ],

 "next": [
  "If there is exploitation, debt with threats, family harm or suicide risk: act first (Tusla report, same-day risk route), then inform your supervisor.",
  "Meet the young person with a non-judgemental, motivational stance; formulate function; screen mood and anxiety.",
  "Meet parents: practical access controls, parental gambling considered without blame, referral route agreed.",
  "Support a GP / addiction service referral with a factual letter; agree a school plan at School Support level with a review date."
 ],

 "presentations": [
  "Risk-taking without a diagnosis attached",
  "Money or possessions going missing",
  "In-game spending and loot-box use",
  "Group dynamics and peer influence",
  "Low mood linked to losses or debt",
  "Parental gambling affecting the child"
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — for the child's own gambling. Relevant only as family context (parental gambling harm).",
   "prevalence": "Not applicable for the child's own behaviour; family-harm rate not stated here — check.",
   "see": "No gambling disorder in the child. Parental gambling may show as financial hardship, conflict, inconsistent care or neglect. That is a welfare and protection question under Children First (2017) — Tusla or family support.",
   "tools": []
  },
  "School Age": {
   "applies": "RARELY — own gambling disorder is rare; relevant as in-game spending and loot boxes, and as FAMILY CONTEXT (parental gambling harm — a Tusla welfare question where it affects care).",
   "prevalence": "Disorder: rare, rate not stated here. Loot-box and in-game spending: common, rate not stated here — check.",
   "see": "Heavy loot-box or in-game spending, distress when purchases are blocked, using a parent's card without permission. Usually a parenting and access conversation, not a clinical referral. Where a parent gambles and the child goes without, follow the welfare / protection route.",
   "tools": ["SDQ"]
  },
  "Adolescent": {
   "applies": "YES — main band for emerging problems: online betting, sports betting peer culture, loot boxes, skin betting.",
   "prevalence": "Problem gambling 0.2–12.3% across adolescent studies (Calado et al., 2017) — wide range, check before quoting; Irish rate not stated here.",
   "see": "Preoccupation with odds and results, secrecy, borrowing, selling possessions, stealing, mood swings tied to wins and losses, falling attendance. Formulate function; ask about debt, exploitation, mood and suicide risk. Refer via GP / addiction services.",
   "tools": ["MFQ (Mood and Feelings Questionnaire)", "RCADS self-report", "SDQ", "BASC-3 SRP",
             "DSM-IV-MR-J — AGE adolescents (approx. 11–16; Fisher, 2000) · MEASURES: problem gambling screen based on adapted DSM-IV criteria (research/health-setting tool) · CANNOT TELL YOU: diagnosis, function or DSM-5-TR severity · TIME: about 5 min — check version before use"]
  },
  "Young Adult": {
   "applies": "YES — peak age for problem gambling onset in young men; usually adult services territory. EP role is recognition, risk response and referral.",
   "prevalence": "See HRB Irish National Drug and Alcohol Survey (gambling module, latest edition) — check before quoting.",
   "see": "Online sports betting and casino apps, debt, loans, relationship and college or work problems, shame and low mood. Services change at 18; refer via GP, adult addiction and gambling services, college counselling.",
   "tools": ["Adult self-report measures via the service"]
  },
  "Special Setting": {
   "applies": "RARELY — less common, but vulnerability to in-game spending and to financial exploitation is higher.",
   "prevalence": "Rate not stated here — check.",
   "see": "Young people with intellectual disability or autism may not understand chance, value or in-game purchase mechanics, and may be targeted by others. Focus on access controls, supported understanding of money, and exploitation risk (Tusla). Involve CDNT and families.",
   "tools": ["Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)"]
  }
 },
})

# ============================================================================ 3 · GAMING DISORDER
CONDS.append({
 "name": "Gaming Disorder",
 "code": ("ICD-11 6C51 Gaming disorder (6C51.0 predominantly online · 6C51.1 predominantly offline) · hazardous "
          "gaming QE22 (not a disorder) · DSM-5-TR: NOT a DSM diagnosis — 'Internet Gaming Disorder' is listed "
          "only in Section III, Conditions for Further Study — check codes before quoting"),
 "neps": NEPS_ADD + " · 3.6 School attendance where gaming displaces attendance",
 "coru": CORU,
 "psi": PSI,
 "law": LAW_GAME,

 "what_it_is": [
  "ICD-11 (in effect from 01/01/2022) defines Gaming Disorder as a pattern of gaming (online or offline) with IMPAIRED CONTROL, INCREASING PRIORITY over other interests and daily activities, and CONTINUATION OR ESCALATION DESPITE NEGATIVE CONSEQUENCES, causing significant impairment in personal, family, social, educational or occupational functioning (WHO, 2019).",
  "ICD-11: the pattern is normally evident over at least 12 MONTHS, though a shorter period may be enough if all requirements are met and symptoms are severe (WHO, 2019) — check wording before quoting.",
  "DSM-5-TR DOES NOT include Gaming Disorder as a diagnosis. 'Internet Gaming Disorder' appears only in Section III as a CONDITION FOR FURTHER STUDY, with nine proposed criteria (five or more in 12 months) — preoccupation, withdrawal when gaming is removed, tolerance, failed attempts to control, loss of other interests, continued excessive use despite problems, deceiving others, gaming to escape negative mood, and jeopardising relationships or education (APA, 2022). A US report cannot give a DSM diagnosis of it.",
  "The key is IMPAIRMENT, NOT HOURS. A young person who games for many hours but sleeps, attends school, keeps friends and can stop does not meet the definition. A lot of gaming is sociable, skilled and enjoyable.",
  "Its inclusion in ICD-11 was DEBATED: some researchers argued it risked pathologising a normal pastime and fuelling moral panic (Aarseth et al., 2017); others argued a small group has genuine, impairing problems that need recognition and treatment (Rumpf et al., 2018). Hold both.",
  "Gaming is often a FUNCTION: escape from anxiety, low mood, bullying or family stress; a place of competence and friendship for young people who struggle socially (including many autistic young people); or simply the most rewarding thing available. Formulate before labelling.",
  "The EP recognises, formulates, supports families and schools with balanced advice, and refers where impairment is significant. Diagnosis sits with CAMHS, specialist services or medical colleagues."
 ],

 "what_it_is_not": [
  "NOT 'screen time'. Gaming Disorder is a narrow clinical category defined by loss of control and impairment. Large studies find the association between digital technology use and adolescent wellbeing is very small on average (Orben & Przybylski, 2019). Avoid moral panic.",
  "NOT defined by hours played. Hours are a poor guide; impairment and loss of control are the test (WHO, 2019).",
  "NOT a DSM-5-TR diagnosis. If a report says 'Internet Gaming Disorder', check what framework was used — DSM-5-TR lists it only for further study (APA, 2022).",
  "NOT always the cause. Gaming is frequently a symptom or coping strategy for anxiety, depression, social difficulty, bullying or school avoidance. Removing the game without addressing the driver often makes things worse.",
  "NOT only a problem for boys. It is reported more in boys, but girls and young women game too; mobile and social gaming are often overlooked.",
  "NOT something the EP diagnoses or treats with medication advice (PSI 2.2.2).",
  "NOT the same as gambling — although loot boxes, skin betting and in-game purchases blur the boundary. Ask about spending."
 ],

 "prevalence": [
  "OVERALL: a meta-analysis estimated global gaming disorder prevalence around 3%, lower when only stringent studies were included (Stevens, Dorstyn, Delfabbro & King, 2021) — check before quoting; rates vary hugely by definition and measure.",
  "Using DSM-5 IGD criteria, Przybylski, Weinstein and Murayama (2017) found very few people met the proposed threshold, and questioned how distinct it is from other mental health problems — check figures before quoting.",
  "IRELAND: no national prevalence of Gaming Disorder identified here — rate not stated, check.",
  "SEX RATIO: reported more often in boys and young men (Stevens et al., 2021) — ratio not stated here, check.",
  "HIGHER RISK GROUPS: young people with ADHD, autism, anxiety, depression, social isolation or school avoidance — rates not stated here, check (see Mazurek & Engelhardt, 2013, for gaming patterns in autism and ADHD)."
 ],

 "cooccurring": [
  {"name": "ADHD", "rate": "elevated — rate not stated here, check",
   "presents": "difficulty stopping, strong pull of immediate reward, conflict at transitions away from the screen. Boys with ADHD were found to show more problematic video game use than typically developing peers (Mazurek & Engelhardt, 2013)."},
  {"name": "AUTISM", "rate": "elevated — rate not stated here, check",
   "presents": "gaming as a focused interest, a predictable world and a place for friendship. Distinguish an intense interest that brings joy from loss of control with impairment."},
  {"name": "ANXIETY / SOCIAL ANXIETY", "rate": "elevated — rate not stated here, check",
   "presents": "gaming as a safe place away from anxiety-provoking situations; night-time gaming to avoid school the next day."},
  {"name": "DEPRESSION", "rate": "elevated — rate not stated here, check",
   "presents": "gaming to escape low mood, withdrawal from other activities, sleep reversal. Ask about mood and suicidal thoughts."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE", "rate": "commonly linked — rate not stated here, check",
   "presents": "a young person at home all day gaming, with gaming blamed for the non-attendance. Often the avoidance came first; gaming fills the day."},
  {"name": "SLEEP PROBLEMS", "rate": "common — rate not stated here, check",
   "presents": "late-night gaming, delayed sleep phase, exhaustion and lateness. Sleep is often the most practical first target."},
  {"name": "GAMBLING / IN-GAME SPENDING", "rate": "overlapping — rate not stated here, check",
   "presents": "loot boxes, skin betting, spending a parent's money. See Gambling Disorder."}
 ],

 "recommendations": [
  "BALANCE FIRST. In the report, separate heavy gaming that is healthy or neutral from gaming with loss of control and impairment. Name the positives (friendship, skill, relaxation) as well as the costs; families trust balanced advice.",
  "FORMULATE THE FUNCTION. What does gaming give this young person (belonging, competence, escape, calm) and what is it replacing? Recommend support for any driver — anxiety, low mood, bullying, EBSA, unidentified learning need.",
  "SLEEP AND ROUTINE: agree device-free bedtimes and devices out of the bedroom overnight, negotiated rather than imposed. Sleep is a concrete, measurable first target.",
  "NEGOTIATED LIMITS, NOT SUDDEN REMOVAL: collaborative agreements (times, conditions, what comes first) with the young person, using motivational principles (Miller & Rollnick, 2013). Abrupt removal can trigger conflict and, for some, distress — plan it.",
  "BUILD ALTERNATIVES that meet the same need: a club, esports or coding club in school, a role that gives status and friendship offline.",
  "ATTENDANCE: where gaming coincides with non-attendance, treat as EBSA until shown otherwise and plan a graded return (NEPS EBSA guidance — check current version).",
  "REFER: GP; CAMHS where there is significant co-occurring mental health difficulty or risk; Primary Care Psychology for milder difficulty; HSE addiction or specialist services where they treat gaming (check locally — availability for under-18s varies). Webwise for parent guidance on settings and controls.",
  "RISK AND SAFEGUARDING: ask about online contact, grooming, sextortion, bullying and in-game spending. Any child protection concern → report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty. Where mood is low, ask directly about suicidal thoughts.",
  "CONTINUUM LEVEL: Classroom Support or School Support for most; School Support Plus where outside services are involved.",
  "DO NOT diagnose Gaming Disorder, label a young person 'addicted' on hours alone, advise on medication, or recommend confiscation as the whole plan."
 ],

 "explain_parent": [
  "'Gaming itself isn't the problem for most young people — lots of it is social and skilled. What we look at is whether he can stop when he needs to, and whether it's pushing out sleep, school, friends and family.'",
  "'For a lot of young people games are where they feel good at something and have friends. If that's true for him, taking it away completely can make things worse. We want to add things, not just subtract.'",
  "'Sleep is a good place to start. Agreeing that devices charge outside the bedroom at night makes a big difference, and it's easier to agree than hours.'",
  "'Try to make the rules together with him, and write them down. Rules he helped make are the ones that last.'",
  "'If he's not going to school and gaming all day, the gaming is often filling the gap, not causing it. Let's look at why school is hard.'",
  "SIGNPOST: GP; Webwise parents' hub for settings and conversation guides; CAMHS or Primary Care via GP where mood or anxiety is significant. Check local availability of any specialist gaming service before naming it."
 ],

 "explain_teacher": [
  "'Most students who game a lot are fine. The ones I'd worry about are exhausted every day, have dropped everything else, or can't stop even when it's costing them.'",
  "'Ask about it with genuine interest — \"what are you playing? what are you good at?\" — before you ask about the problem. You'll learn more, and it's often a route into a relationship.'",
  "'If a student seems wrecked every morning, ask about sleep, and pass it on. It may be gaming, or something else keeping them awake.'",
  "'Online games are also a place where bullying, grooming and pressure to share images can happen. If a student mentions any of that, it goes to the DLP today.'",
  "'A school esports, coding or games-design club can give a heavy gamer status and friendship in school. That's protective.'"
 ],

 "explain_child": [
  "YOUNGER: 'Games are made to be really fun and hard to stop — that's what the people who make them want. Lots of kids find it hard to switch off. Let's work out a plan with your family that's fair.'",
  "OLDER: 'I'm not anti-gaming. I want to know what it's like for you — what you get from it, and whether anything's getting squeezed out that you'd miss.'",
  "ASK: 'What are you good at in the game? Who do you play with?' (strengths, belonging). 'When you want to stop, can you?' 'What happens when your parents turn it off?'",
  "ASK: 'Is gaming a way of not thinking about something?' 'How are you sleeping?' Where mood seems low: 'Have you had thoughts of hurting yourself?'",
  "ASK ABOUT ONLINE SAFETY: 'Has anyone online ever made you uncomfortable, asked for pictures, or pressured you?' Explain confidentiality limits first.",
  "AVOID: 'You're addicted', 'it's rotting your brain', 'waste of time'. They close the conversation and are not accurate."
 ],

 "analogies": [
  "THE HOBBY THAT GREW TOO BIG: 'A hobby that's healthy fits around your life. When it starts taking the space of sleep, school and friends, it's grown too big — the hobby isn't bad, it just needs to fit again.' Works with adolescents and parents.",
  "THE ESCAPE HATCH: 'Games can be an escape hatch — a great place to go when things are hard. The question is whether you're coming back out.' Works with anxious or low young people; names function.",
  "THE BUILT-IN HOOKS: 'Games are designed by teams of experts to keep you playing — daily rewards, streaks, levels. Finding it hard to stop isn't weakness; it's design.' Works with adolescents; reduces shame.",
  "THE SEESAW: 'On one side, what gaming gives you; on the other, what it costs. We're just looking at the balance.' Works with older adolescents (decisional balance)."
 ],

 "language": [
  "'Gaming Disorder' only where diagnosed under ICD-11. Otherwise: 'heavy gaming', 'gaming that is causing difficulty', or describe the impact in the young person's words.",
  "Avoid 'game addict', 'screen addiction', 'digital heroin' and similar. These are inaccurate and alienate young people and families.",
  "Be precise about framework: 'Internet Gaming Disorder' is a DSM-5-TR condition for further study, not a DSM diagnosis (APA, 2022).",
  "Many young people call gaming a hobby, a sport (esports) or a social life. Using their language shows respect and gets better information.",
  "In reports, describe hours only alongside impact (sleep, attendance, relationships); label opinion as opinion (PSI 1.2.8)."
 ],

 "red_flags": [
  "RED FLAG — online grooming, sextortion, sharing of intimate images, or threats via games or chat platforms. Child protection route: report to Tusla as soon as practicable, and gardaí where there is immediate danger; telling the DLP does not discharge a mandated person's duty under the Children First Act 2015.",
  "RED FLAG — suicidal ideation or self-harm, including in the context of devices being removed. Same-day risk route: supervisor the same day, parents unless that increases risk, GP/CAMHS, ED or emergency services if imminent. Supervision follows action; it does not replace it.",
  "RED FLAG — prolonged non-attendance with isolation at home. Treat as EBSA and a welfare concern; involve the school's attendance procedures and, where needed, Tusla Education Support Service.",
  "BOUNDARY — you do not diagnose Gaming Disorder or advise on medication (PSI 2.2.2). Describe, formulate and refer.",
  "WATCH — your own and the school's assumptions about gaming. Moral panic leads to confiscation plans that ignore function and damage relationships.",
  "WATCH — aggression when devices are removed. Plan transitions and removal carefully with families; ask what the aggression is about (loss of friendship, loss of escape)."
 ],

 "child_voice": [
  "GAMING INTERVIEW WITH GENUINE INTEREST — 'show me what you play' — good because it builds rapport, reveals strengths, belonging and function, and signals respect before any question about the problem.",
  "DECISIONAL BALANCE (what gaming gives / what it costs) — good because the young person names costs themselves; motivational principles predict change better than instruction (Miller & Rollnick, 2013).",
  "A 24-HOUR OR WEEK TIMELINE of sleep, school, gaming and mood — good because it shows what gaming is displacing, and gives a shared, factual picture for the family plan.",
  "RCADS OR MFQ SELF-REPORT completed with the young person — good because anxiety and low mood are common drivers; follow up any risk item in session.",
  "WEBWISE youth and parent materials — Irish, balanced, practical on settings and online safety. Good because they support a shared family conversation. → https://www.webwise.ie/"
 ],

 "questions": [
  "Q: 'How many hours is too many?' — A: 'There isn't a magic number. What matters more is whether he's sleeping, going to school, seeing people, and can stop when he needs to. Hours matter less than what's being pushed out.'",
  "Q: 'Is he addicted?' — A: 'Gaming Disorder is a real diagnosis in the WHO's ICD-11, but it's for a small group where gaming is out of control and causing serious problems for a long time. That's a diagnosis for a doctor or specialist, not me. What I can do is look at what's going on and what would help.'",
  "Q: 'Should we just take the console away?' — A: 'Sometimes limits are needed, but taking it away suddenly often leads to big conflict, and if gaming is where he has friends or copes with worry, that gap needs filling. A plan made with him usually works better.'",
  "Q: 'Isn't gaming making him violent?' — A: 'The research on that is contested and doesn't show a simple link. If he's aggressive when it's turned off, that's usually about the transition and what he's losing — we can plan for that.'",
  "Q: 'He won't go to school and games all day — isn't gaming the problem?' — A: 'It might be part of it, but often something makes school hard first, and gaming fills the day. Let's find out what's going on at school as well.'",
  "Q (teacher): 'Should we ban phones and games talk in school?' — A: 'That's a school policy decision. From a psychological point of view, taking an interest in what students play is often a way in. The students to worry about are those whose gaming is costing them sleep, attendance and friends.'"
 ],

 "supervision": [
  "Discuss your own views on gaming and screen time, and how they might bias a formulation either way (panic or dismissal).",
  "Clarify local services: who, if anyone, treats gaming problems in under-18s; when CAMHS or Primary Care is the better route.",
  "Bring a case where gaming was blamed for non-attendance and check whether the EBSA formulation was done.",
  "Rehearse how to ask about online grooming and sextortion within a gaming conversation, and the Tusla route if disclosed.",
  "Discuss how to write balanced advice on gaming for families from different cultures and parenting styles."
 ],

 "reflection": [
  "ON BALANCE — did my report name what gaming gives this young person, as well as what it costs?",
  "ON THE TEST — did I judge by impairment and control, or by hours?",
  "ON FUNCTION — did I ask what gaming is helping with (anxiety, low mood, loneliness, school avoidance)?",
  "ON SAFETY — did I ask about online contact, pressure and spending? If a concern emerged, did I report to Tusla myself?",
  "ON THE PLAN — did I recommend negotiated limits and alternatives, or a confiscation plan likely to fail?",
  "WHAT GOOD LOOKS LIKE: 'Referral: \"gaming addiction, not attending\". He showed me his game — he leads a team of friends. He described panic on Sunday nights. Formulation: EBSA with gaming as escape and belonging. Plan: graded return, esports club at lunch, devices out of the bedroom agreed with him, GP for anxiety.'",
  "WHAT POOR LOOKS LIKE: 'Student is addicted to video games. Recommend parents remove console.' — diagnosis by the EP, hours not impairment, no function, no plan for the anxiety."
 ],

 "citations": [
  CIT_ICD,
  CIT_DSM,
  "Aarseth, E., Bean, A. M., Boonen, H., Colder Carras, M., Coulson, M., Das, D., et al. (2017). Scholars' open debate paper on the World Health Organization ICD-11 Gaming Disorder proposal. Journal of Behavioral Addictions, 6(3), 267–270.",
  "Rumpf, H.-J., Achab, S., Billieux, J., Bowden-Jones, H., Carragher, N., Demetrovics, Z., et al. (2018). Including gaming disorder in the ICD-11: The need to do so from a clinical and public health perspective. Journal of Behavioral Addictions, 7(3), 556–561.",
  "Orben, A., & Przybylski, A. K. (2019). The association between adolescent well-being and digital technology use. Nature Human Behaviour, 3(2), 173–182.",
  "Przybylski, A. K., Weinstein, N., & Murayama, K. (2017). Internet gaming disorder: Investigating the clinical relevance of a new phenomenon. American Journal of Psychiatry, 174(3), 230–236.",
  "Stevens, M. W. R., Dorstyn, D., Delfabbro, P. H., & King, D. L. (2021). Global prevalence of gaming disorder: A systematic review and meta-analysis. Australian & New Zealand Journal of Psychiatry, 55(6), 553–568.",
  "Mazurek, M. O., & Engelhardt, C. R. (2013). Video game use in boys with autism spectrum disorder, ADHD, or typical development. Pediatrics, 132(2), 260–266.",
  "Pontes, H. M., & Griffiths, M. D. (2015). Measuring DSM-5 internet gaming disorder: Development and validation of a short psychometric scale. Computers in Human Behavior, 45, 137–143.",
  CIT_MR
 ],

 "pathway": {
  "age": "Concern usually arises in late primary and post-primary, when independent device access, online multiplayer games and night-time gaming increase. It is often raised by parents in the context of conflict at home, sleep reversal or non-attendance. By ICD-11, the pattern normally needs to be evident over about 12 months, so identification is rarely quick.",
  "who_diagnoses": "Ireland: CAMHS (where co-occurring mental health difficulty is significant), specialist or HSE addiction services that treat behavioural addictions (check locally — availability for under-18s is limited and varies), psychiatrists and clinical psychologists privately. Diagnosis is under ICD-11; DSM-5-TR has no Gaming Disorder diagnosis.",
  "who_wrote_report": "CAMHS psychiatrist or psychologist; private clinician; addiction or behavioural-addiction service. Watch for reports that use 'Internet Gaming Disorder' as if it were a DSM diagnosis, or 'screen addiction' as a label. A parent questionnaire on hours is not an assessment.",
  "refer_to": "GP first; CAMHS for moderate to severe co-occurring mental health difficulty or risk; Primary Care Psychology for milder difficulty; HSE or specialist services treating gaming problems (check local availability); Tusla where online harm or exploitation meets threshold; Webwise for family guidance.",
  "sooner": "'It's really hard to tell when gaming has gone from a big hobby to a problem — even the experts argue about it. You've noticed it's affecting him, and that's the right time to look.'"
 },

 "differential": [
  "HEAVY BUT HEALTHY GAMING — many hours, but sleep, school, friendships and control intact. Not a disorder; no referral needed.",
  "EMOTIONALLY BASED SCHOOL AVOIDANCE — gaming fills time created by avoidance; the avoidance is primary.",
  "DEPRESSION OR ANXIETY — gaming as escape; the mood or anxiety disorder is the primary target.",
  "AUTISM — intense focused interest that brings joy and structure; impairment and loss of control distinguish a problem from an interest.",
  "GAMBLING DISORDER — where spending, loot boxes or skin betting dominate. Both may apply."
 ],

 "next": [
  "If there is online exploitation, a child protection concern or suicide risk: act first (Tusla report, same-day risk route), then inform your supervisor.",
  "Meet the young person with genuine interest; formulate function, sleep and what is being displaced; screen mood and anxiety.",
  "Meet parents with balanced advice: sleep first, negotiated limits, alternatives, online safety settings (Webwise).",
  "Where impairment is significant or co-occurring difficulties are present, support a GP referral; agree a school plan with a review date."
 ],

 "presentations": [
  "Heavy gaming without impairment",
  "Sleep disruption and daytime tiredness",
  "School refusal / emotionally based school avoidance",
  "Withdrawal from peers",
  "In-game spending and loot-box use",
  "Conflict at home around devices",
  "Risk-taking without a diagnosis attached"
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — Gaming Disorder is not identified at this age. Screen use in early years is a parenting and development conversation, not a diagnosis.",
   "prevalence": "Not applicable — rate not stated here.",
   "see": "Heavy screen use may come up in the context of language delay, sleep or behaviour. Frame it around interaction, sleep and play, and follow current public health advice on young children's screen use (check the current HSE / WHO guidance). Avoid blame.",
   "tools": []
  },
  "School Age": {
   "applies": "RARELY — for disorder; heavy gaming, conflict over devices and in-game spending are common family concerns in senior primary.",
   "prevalence": "Disorder rare at this age — rate not stated here, check.",
   "see": "Conflict at home when devices are switched off, late-night gaming, tiredness in school, in-game spending. Usually a parenting and routines conversation; look for anxiety, ADHD or social difficulty behind it. Online safety (grooming, contact) is a real risk at this age — ask.",
   "tools": ["SDQ", "RCADS", "Conners-4", "BRIEF-2"]
  },
  "Adolescent": {
   "applies": "YES — main band; the ICD-11 pattern is most often identified in adolescent and young adult males, but most heavy gaming is not disordered.",
   "prevalence": "Pooled global estimate around 3% (Stevens et al., 2021), varying widely by measure — check before quoting; no Irish figure stated here.",
   "see": "Sleep reversal, falling attendance, loss of other interests, conflict when limits are set, gaming to escape mood. Formulate function; screen mood and anxiety; ask about online safety and spending; separate impairment from hours.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "SDQ", "BASC-3 SRP", "Conners-4 self-report",
             "IGDS9-SF — AGE adolescents and adults (Pontes & Griffiths, 2015) · MEASURES: severity of the nine proposed DSM-5 IGD criteria (research screen) · CANNOT TELL YOU: diagnosis, function, or whether heavy gaming is healthy · TIME: 2–3 min"]
  },
  "Young Adult": {
   "applies": "YES — gaming problems can peak here, often with transitions (college, unemployment, living alone). EP role is recognition and referral.",
   "prevalence": "Rate not stated here — check before quoting.",
   "see": "Gaming displacing college, work or relationships, isolation, sleep reversal, low mood. Services change at 18; refer via GP, college counselling, adult mental health or specialist services.",
   "tools": ["Adult self-report measures via the service"]
  },
  "Special Setting": {
   "applies": "RARELY — for disorder; gaming is often a valued interest and a regulation strategy. Distinguish interest from impairment.",
   "prevalence": "Rate not stated here — check.",
   "see": "For many autistic pupils or pupils with intellectual disability, gaming is a preferred activity, calming and a route to peers. Distress at transitions away from screens is common; plan transitions visually and predictably. Watch for online exploitation and in-game spending; involve CDNT and families.",
   "tools": ["Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)", "SDQ"]
  }
 },
})
