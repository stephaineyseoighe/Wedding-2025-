# CONDS records: Epilepsy, Cerebral palsy, Spina bifida.
# Medical / neurological conditions. The EP role is EDUCATIONAL IMPACT: describe, formulate, recommend, refer.
# The EP does not diagnose these conditions and does not advise on medication (PSI 2.2.2).
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c17.py

LAW_MED = ("Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · "
           "Equal Status Acts 2000–2018 · GDPR / Data Protection Act 2018 (health data is special-category data)")

CONDS = [

# =====================================================================================
# 1. EPILEPSY
# =====================================================================================
{
 "name": "Epilepsy (and its educational impact)",
 "code": "Not a DSM diagnosis · medical/neurological condition · ICD-11 code — check (epilepsy sits in Chapter 08, Diseases of the nervous system; verify the exact code in the ICD-11 browser before quoting)",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 1. LEARNING (1.1 Attention, concentration and work skills) where seizures or medication affect attention",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  LAW_MED,

 "what_it_is": [
  "A disease of the brain defined by an enduring predisposition to generate epileptic seizures. The ILAE practical definition (Fisher et al., 2014) is met by ANY of:\n▸ at least two unprovoked seizures more than 24 hours apart;\n▸ one unprovoked seizure plus a high probability of further seizures (similar to the recurrence risk after two);\n▸ diagnosis of an epilepsy syndrome.",
  "A SEIZURE is an event; EPILEPSY is the condition. A single seizure, a febrile convulsion in a toddler or a faint is not epilepsy. The distinction matters because school files often say 'had a seizure' and staff then treat it as epilepsy, or the reverse.",
  "Seizure types (ILAE 2017; Fisher et al., 2017) are classified by ONSET: FOCAL (one hemisphere — with or without impaired awareness), GENERALISED (both hemispheres from the start — e.g. tonic-clonic, ABSENCE, myoclonic, atonic) or UNKNOWN onset. 'Grand mal' and 'petit mal' are outdated terms you will still meet in files.",
  "ABSENCE SEIZURES are the ones an EP is most likely to meet undiagnosed: brief lapses of awareness lasting seconds, often many times a day, with staring and sometimes eyelid flicker, and no fall. The child resumes as if nothing happened — and has missed part of the instruction.",
  "The EDUCATIONAL impact comes from several sources at once, and you need to separate them:\n▸ the seizures themselves and the recovery (post-ictal) period;\n▸ subclinical epileptiform activity that can disrupt cognition without a visible seizure (Binnie, 2003);\n▸ the underlying brain cause, if there is one;\n▸ anti-seizure medication effects on alertness, memory or mood;\n▸ disrupted sleep, missed school and anxiety.",
  "Outcome varies enormously by syndrome. Some childhood epilepsies remit and cognition is typical; others (the developmental and epileptic encephalopathies) carry intellectual disability. The epilepsy label alone tells you almost nothing about the child's learning — the neurologist's syndrome diagnosis, if there is one, tells you more.",
  "The classification of epilepsies (Scheffer et al., 2017) explicitly asks clinicians to consider co-morbidities — learning, psychological and behavioural — at every level. That is the door the EP comes through.",
 ],

 "what_it_is_not": [
  "NOT an intellectual disability. Many children with epilepsy have typical or high ability. Where learning difficulty is present, it needs its own assessment rather than being assumed to follow from the diagnosis.",
  "NOT always convulsions. Most staff picture a tonic-clonic seizure. Absence and focal impaired-awareness seizures can look like daydreaming, 'switching off', confusion or odd behaviour, and are routinely missed or disciplined.",
  "NOT usually triggered by flashing lights. Photosensitive epilepsy is a minority of cases (proportion not stated here — check Epilepsy Ireland before quoting). Banning screens for every child with epilepsy is neither necessary nor evidence-based; the child's care plan should say if it applies.",
  "NOT a reason to exclude from PE, swimming, trips or science practicals by default. Restrictions should come from the child's medical team and care plan, individually risk-assessed — blanket exclusion is a disability-equality issue (Equal Status Acts 2000–2018).",
  "NOT 'attention-seeking' when events look unusual. Some seizures (especially frontal-lobe focal seizures) look behavioural. Equally, some events that look like epilepsy are functional/dissociative seizures. Neither judgement is the EP's or the school's — describe and refer back to neurology.",
  "NOT something to put in a spoon or hold down. Restraining a person or putting anything in their mouth during a seizure is dangerous. Staff first-aid training is the school's responsibility (Epilepsy Ireland provides training — check current offer).",
  "NOT a medication question for you. If attention, mood or memory has changed since a medication change, that is information for the parent to bring to neurology — you describe what you see, you do not comment on the medicine (PSI 2.2.2).",
 ],

 "prevalence": [
  "OVERALL: active epilepsy point prevalence around 6.4 per 1,000 people across international studies (Fiest et al., 2017, meta-analysis). Roughly one child in a large primary school, several in a large post-primary school.",
  "CHILDHOOD: a Norwegian national cohort (Aaberg et al., 2017) reported prevalence of about 0.6% at age 10 — check the exact figure before quoting. Incidence is highest in the first year of life.",
  "IRELAND: Epilepsy Ireland cites over 45,000 people living with epilepsy in Ireland — check the current figure on the Epilepsy Ireland website before quoting. No Irish child-specific prevalence figure is stated here.",
  "EARLY YEARS 0–5: highest incidence; includes infantile-onset syndromes, some with developmental impact. Febrile seizures are common at this age and are NOT epilepsy.",
  "SCHOOL AGE 6–12: childhood absence epilepsy and self-limited focal epilepsies typically present here (ILAE syndrome descriptions — check onset ranges before quoting).",
  "ADOLESCENT 13–16: juvenile myoclonic epilepsy and other adolescent-onset syndromes; sleep deprivation, exams and alcohol become practical triggers.",
  "CO-OCCURRENCE: Reilly et al. (2014), a population-based UK study of children with active epilepsy, found that the large majority had at least one neurobehavioural co-morbidity (learning, ADHD, autism, DCD) — check the exact figures before quoting.",
 ],

 "cooccurring": [
  {"name": "INTELLECTUAL DISABILITY / GENERAL LEARNING DIFFICULTY",
   "rate": "substantially elevated in population samples (Reilly et al., 2014) — rate not stated here, check",
   "presents": "difficulty across the curriculum, not only on seizure days. Assess cognition and adaptive functioning properly; do not attribute everything to 'the epilepsy' or to 'bad days'. Where a developmental and epileptic encephalopathy is diagnosed, ask neurology what trajectory to expect."},
  {"name": "ADHD / ATTENTION DIFFICULTY",
   "rate": "elevated (Reilly et al., 2014) — rate not stated here, check",
   "presents": "inattention that may be ADHD, absence seizures, subclinical discharges, medication effects or poor sleep — or several. Attention difficulty was present BEFORE treatment in many children with absence epilepsy (Masur et al., 2013). Describe the pattern (time of day, relation to seizures and dose times) and refer back to the medical team."},
  {"name": "AUTISM",
   "rate": "elevated (Reilly et al., 2014) — rate not stated here, check",
   "presents": "social-communication difference plus seizures; staring or unresponsiveness may be read as autistic withdrawal when it is a seizure, or vice versa. Seizure logs and CDNT input are needed; do not decide which it is."},
  {"name": "ANXIETY AND LOW MOOD",
   "rate": "elevated in young people with epilepsy — rate not stated here, check (NICE, 2022, advises attention to mental health)",
   "presents": "fear of having a seizure in front of peers, avoidance of school, social withdrawal, low self-esteem. Can be driven by stigma and unpredictability more than by the seizures themselves. Screen with self-report at adolescence."},
  {"name": "SPECIFIC LEARNING DIFFICULTY",
   "rate": "elevated — rate not stated here, check",
   "presents": "specific literacy or maths difficulty that persists on seizure-free days. Rule it in or out separately; the epilepsy should not become the explanation for a reading difficulty that would otherwise have been assessed."},
  {"name": "SLEEP DIFFICULTY",
   "rate": "common and bidirectional — rate not stated here, check",
   "presents": "tiredness, slowed processing and irritability, especially after nocturnal seizures. Sleep deprivation can also lower seizure threshold for some children. Always ask about last night."},
  {"name": "DCD / MOTOR DIFFICULTY",
   "rate": "elevated in population samples (Reilly et al., 2014) — rate not stated here, check",
   "presents": "slow, effortful handwriting and clumsiness that may be attributed to medication or tiredness. OT assessment via CDNT or Primary Care where it affects output."},
 ],

 "recommendations": [
  "NAME THE IMPACT, NOT THE DIAGNOSIS. 'Brief absences, observed up to X times in a 30-minute lesson, mean she misses parts of verbal instructions' is actionable; 'epilepsy may affect learning' is not.",
  "BUILD IN RECOVERY OF MISSED INFORMATION: instructions written or on the board, a 'buddy recap' routine, key points repeated after pauses, and checking understanding by asking the child to show you. This helps whether the gap was a seizure or not.",
  "INDIVIDUAL HEALTHCARE PLAN (IHCP) / EMERGENCY CARE PLAN: recommend that the school confirms one exists, is current, is signed off by parents with medical input, and that named staff are trained. The CONTENT (seizure description, when to give emergency medication, when to call an ambulance) is set by the medical team and school policy — NOT by the EP.",
  "SEIZURE AND LEARNING LOG: a simple shared record of seizure events, tiredness, post-ictal recovery time and lesson missed. It gives neurology better information and lets you see the real pattern of lost learning.",
  "POST-SEIZURE PLAN: agreed in advance — where the child rests, who stays with them, how and when they return to learning, whether they go home. Avoid testing, new learning or reprimand in the recovery period.",
  "FATIGUE AND TIMING: schedule demanding or assessed work at the child's better time of day; allow rest breaks; reduce homework volume on bad weeks; plan for catch-up after absences or hospital admissions.",
  "PARTICIPATION, NOT EXCLUSION: PE, swimming, trips and practicals individually risk-assessed from the care plan, with supervision arranged — rather than default exclusion.",
  "SOCIAL AND EMOTIONAL: with the young person's agreement, a planned, age-appropriate explanation to peers (Epilepsy Ireland has school resources — check); attention to anxiety, self-esteem and bullying.",
  "STATE EXAMS: where relevant, RACE applications (SEC — check current scheme and deadlines) and SEC arrangements for candidates affected by illness on the day — check current SEC provisions.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support where learning or attention is affected; School Support Plus where CDNT, neurology or CAMHS are involved. SNA support for care needs is an NCSE decision under the current allocation model (Circular 0030/2014 sets out SNA care-need scope — check current circular and model).",
  "REFER / LIAISE: with consent, back to the treating team (paediatric neurology, paediatrician, epilepsy specialist nurse) with a description of classroom observations; CDNT where there are complex needs; CAMHS or Primary Care Psychology where mood or anxiety meets their threshold.",
  "DO NOT comment on anti-seizure medication, doses, timing or side effects, and do not suggest that a child 'needs a medication review'. Say instead: 'the family may wish to share these observations with the neurology team.' Do not write emergency protocols.",
 ],

 "explain_parent": [
  "'My job is to look at how the epilepsy affects her learning and school day — not the seizures themselves. Her neurology team leads on that, and I'll make sure what I write fits with what they've said.'",
  "'Some seizures are very brief — a few seconds of switching off. If she has a lot of them, she can miss pieces of what the teacher says without anyone noticing. That's something we can plan around.'",
  "'Tiredness after a seizure, or after a bad night, can make it much harder to think and remember for a while. That isn't laziness, and we'll ask the school to plan for it.'",
  "'If you've noticed changes in her concentration, mood or memory — especially since any change in treatment — that's really useful for her neurologist. I won't comment on medication myself; that's their area.'",
  "'Epilepsy doesn't tell us how clever she is. Many children with epilepsy learn in the typical range. If there's a learning difficulty as well, it deserves its own look rather than being put down to the epilepsy.'",
  "SIGNPOST: Epilepsy Ireland (information, family support, school training — check current services) → https://www.epilepsy.ie/ ; the child's neurology team or epilepsy specialist nurse; the school's Individual Healthcare Plan process.",
 ],

 "explain_teacher": [
  "'What looks like daydreaming may be an absence — a few seconds of lost awareness. Don't reprimand staring spells; note the time and what happened and pass it to the parents via the agreed log.'",
  "'Assume she may have missed part of any verbal instruction. Put it on the board or on her desk, and check by asking her to show you what to do.'",
  "'After a seizure she needs recovery time. Follow the care plan, and don't expect new learning or testing until she's back to herself — sometimes that's the rest of the day.'",
  "'Emergency medication and when to call an ambulance are in the care plan and the school's policy. Know where the plan is and who is trained. That isn't something I decide, and it isn't something to improvise.'",
  "'Keep her in PE, trips and practicals where the risk assessment allows. Being left out because of epilepsy hurts more, for many young people, than the seizures do.'",
  "'Watch for changes over weeks — slower work, more tiredness, more absences, lower mood. Tell the parents; they're the route to the medical team.'",
 ],

 "explain_child": [
  "YOUNGER: 'Epilepsy means that sometimes your brain has a little electrical storm, called a seizure. It's not your fault and you can't catch it. Your grown-ups and teachers know what to do if it happens.'",
  "OLDER: 'Epilepsy means your brain sometimes has seizures. Some are big and some are so short you might not notice — but they can mean you miss bits of what's said. It's got nothing to do with how clever you are.'",
  "GIVE THEM A SCRIPT: 'Can you say that again? I think I missed it.' Practise it. Children with absences often don't know they missed something, only that they're lost.",
  "ASK: 'Do you ever feel you've missed something in class?' · 'How do you feel after a seizure — and how long until you feel like you again?' · 'What do you want your friends to know, and what do you want to keep private?'",
  "RESPECT CONTROL: older children and adolescents should decide, with their parents, what classmates are told. Being discussed without consent is a common source of distress.",
 ],

 "analogies": [
  "THE DROPPED CALL: 'It's like a phone call that cuts out for a few seconds. You come back and the other person's still talking, but you've lost a chunk and don't know what.' Explains absences to teachers and older children.",
  "THE ELECTRICAL STORM: 'The brain runs on tiny electrical signals. A seizure is a short storm where too many fire at once. Afterwards it takes a while for the lights to come back on properly.' Good for younger children and for explaining post-ictal recovery.",
  "THE PHONE AFTER A HEAVY DAY: 'After a seizure her battery is flat. She can still work, but it drains fast and everything is slower until it's recharged.' Good for teachers planning around fatigue.",
  "FOG ON THE WINDSCREEN: 'On some days the view is clear, on others it's foggy — from tiredness, a bad night or seizures nobody saw. Same driver, different visibility.' Explains variability to parents and teachers who say 'she can do it one day and not the next'.",
 ],

 "language": [
  "'Child/young person with epilepsy' is widely used; many people also say 'epileptic' of themselves. Avoid 'an epileptic' as a noun in reports unless it is the young person's own choice. Ask.",
  "Use 'seizure', not 'fit', 'attack' or 'turn' in reports — although families may use those words, and you should not correct them in conversation.",
  "Use current seizure terms (focal / generalised / absence / tonic-clonic) only as they appear in the medical report; quote them, don't reinterpret. 'Grand mal' and 'petit mal' are outdated.",
  "Avoid 'suffers from epilepsy' and avoid describing behaviour during or after a seizure as 'refusal', 'defiance' or 'zoning out on purpose' (PSI 1.2.8 — opinion labelled as opinion).",
  "Health information is special-category data under GDPR. Share seizure information on a need-to-know basis, with consent, and say in the report where it came from.",
 ],

 "red_flags": [
  "RED FLAG — a seizure during your assessment. Stop testing, follow the school's care plan and first-aid procedure, and make sure a trained adult takes over. Do not resume testing that session; record the event and the fact that the session's results are not valid.",
  "RED FLAG — LOSS of skills (language, learning or behaviour) in a child with epilepsy. Some epilepsy syndromes cause regression, including of language. This is a medical question — tell the parents and, with consent, the treating team promptly.",
  "RED FLAG — staring spells, 'blank' episodes or unexplained brief lapses in a child with NO diagnosis. Describe them precisely (duration, frequency, what happens) and advise the parent to see the GP. You do not say 'it might be epilepsy' as a conclusion.",
  "RED FLAG — low mood, hopelessness or self-harm in a young person with epilepsy. Mental health needs are elevated in epilepsy (NICE, 2022). Follow the same-day risk route; report to Tusla as soon as practicable where there is a child protection concern; telling the DLP does not discharge a mandated person's duty; supervision follows action.",
  "RED FLAG — a school with no emergency care plan, no trained staff or no clarity about emergency medication. Raise it with the principal and document that you raised it. Writing the protocol is not your job; noticing that it is missing is.",
  "BOUNDARY — you do not diagnose epilepsy, classify seizures, or advise on medication or emergency medication. You describe observed events and learning impact and refer (PSI 2.2.2).",
  "WATCH — test validity. A result obtained on a day with seizures, a bad night or a post-ictal child is not a stable estimate. Ask on the day and record it.",
 ],

 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, already in schools. Good because it surfaces which parts of the day are hard without making epilepsy the topic. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "DAY MAPPING WITH ENERGY LEVELS — the child marks a typical day and colours when they feel tired, foggy or fine. Good because it shows fatigue patterns that the timetable can be built around.",
  "'WHAT I WANT PEOPLE TO KNOW' ONE-PAGE PROFILE — the child decides what goes on it about their epilepsy and what stays private. Good because control over disclosure is a central concern for this group.",
  "SCALING (0–10: 'how worried are you about having a seizure in school?') — good because anticipatory anxiety is often greater than the seizure burden, and the follow-up ('what would make it a 3?') gives you the recommendation.",
  "EPILEPSY IRELAND young people's materials — Irish, written for children and teenagers. Good because they give the child language for their own condition before you ask them to use it. → https://www.epilepsy.ie/",
 ],

 "questions": [
  "Q: 'Will the epilepsy affect her learning?' — A: 'It depends on the kind of epilepsy, how often seizures happen, sleep, and a few other things. Many children with epilepsy learn in the typical range. What I can do is look at how she's learning now and what's getting in the way.'",
  "Q: 'Is it the medication that's making him slow?' — A: 'That's a really important question for his neurologist, and I'd encourage you to bring what you've noticed to them. I can describe what we see in school — how quick his work is, when he's tired — so that they have good information. I won't comment on the medication itself.'",
  "Q: 'Should we give her the emergency medication if a seizure goes on?' — A: 'That's set out in her care plan by her medical team and follows the school's policy on medication. The person to check with is the principal and whoever is trained. It isn't something I can advise on.'",
  "Q: 'The teacher says he's just daydreaming.' — A: 'Some seizures look exactly like daydreaming. I'd suggest noting when it happens, how long, and whether he can be brought back by calling his name — and sharing that with his parents for his medical team. It's worth finding out rather than assuming.'",
  "Q: 'Should she be kept out of PE and swimming?' — A: 'That's for her medical team and the school's risk assessment, based on her own seizures. For most children the answer is participation with the right supervision rather than exclusion.'",
  "Q: 'Can you test her while her seizures aren't controlled?' — A: 'I can, but I'd be careful about what the scores mean. A result on a bad day underestimates her. I'd note seizures and sleep on the day, and I may describe ranges and patterns rather than lean on one number.'",
  "Q: 'Will he be able to drive?' — A: 'That's a medical and licensing question — his neurologist and the Road Safety Authority's medical fitness rules decide it. It's worth raising with his team well before he's 17 so there are no surprises.'",
 ],

 "supervision": [
  "Bring a case where attention difficulty could be seizures, medication, ADHD or sleep, and talk through how to describe it without choosing between them.",
  "Ask what your service expects you to do if a child has a seizure in your session — before it happens.",
  "Ask how the service liaises with paediatric neurology and epilepsy nurses: consent, who writes, and what information is useful to them.",
  "Discuss how to report a cognitive assessment where seizure activity on or around the test day may have affected results.",
  "Discuss a school that is excluding a child from trips or PE because of epilepsy, and how to raise it without overstepping into the medical risk decision.",
  "Rehearse, word for word, how you answer a parent's medication question without advising.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I explain epilepsy, or did I explain what this child needs in class on Monday? Did the teacher leave knowing what to do about missed instructions and recovery time?",
  "ON THE ROLE BOUNDARY — When asked about medication or emergency medication, did I hold the boundary cleanly and still leave the family with somewhere to go?",
  "ON VALIDITY — Did I ask about seizures, sleep and timing on the day? Did I report scores as if they were stable when the conditions weren't?",
  "ON OVERSHADOWING — Did 'the epilepsy' become the explanation for everything? Did I assess literacy, attention and mood as their own questions?",
  "ON PARTICIPATION — Did my recommendations include the child in school life, or did they add restrictions nobody asked the medical team about?",
  "WHAT GOOD LOOKS LIKE: 'The teacher had described him as lazy in the afternoons. We set up a two-week log. Staring spells clustered after lunch and he was far slower on days after night seizures. The parents took the log to neurology; the school moved maths to the morning and put instructions on his desk.'",
  "WHAT POOR LOOKS LIKE: 'He has epilepsy, which may account for his difficulties. Medication review is recommended.' — no description, no classroom plan, and a medical recommendation the EP has no standing to make.",
 ],

 "citations": [
  "Fisher, R. S., Acevedo, C., Arzimanoglou, A., Bogacz, A., Cross, J. H., Elger, C. E., Engel, J., Jr., Forsgren, L., French, J. A., Glynn, M., Hesdorffer, D. C., Lee, B. I., Mathern, G. W., Moshé, S. L., Perucca, E., Scheffer, I. E., Tomson, T., Watanabe, M., & Wiebe, S. (2014). ILAE official report: A practical clinical definition of epilepsy. Epilepsia, 55(4), 475–482.",
  "Fisher, R. S., Cross, J. H., French, J. A., Higurashi, N., Hirsch, E., Jansen, F. E., Lagae, L., Moshé, S. L., Peltola, J., Roulet Perez, E., Scheffer, I. E., & Zuberi, S. M. (2017). Operational classification of seizure types by the International League Against Epilepsy: Position Paper of the ILAE Commission for Classification and Terminology. Epilepsia, 58(4), 522–530.",
  "Scheffer, I. E., Berkovic, S., Capovilla, G., Connolly, M. B., French, J., Guilhoto, L., Hirsch, E., Jain, S., Mathern, G. W., Moshé, S. L., Nordli, D. R., Perucca, E., Tomson, T., Wiebe, S., Zhang, Y.-H., & Zuberi, S. M. (2017). ILAE classification of the epilepsies: Position paper of the ILAE Commission for Classification and Terminology. Epilepsia, 58(4), 512–521.",
  "Fiest, K. M., Sauro, K. M., Wiebe, S., Patten, S. B., Kwon, C.-S., Dykeman, J., Pringsheim, T., Lorenzetti, D. L., & Jetté, N. (2017). Prevalence and incidence of epilepsy: A systematic review and meta-analysis of international studies. Neurology, 88(3), 296–303.",
  "Aaberg, K. M., Gunnes, N., Bakken, I. J., Lund Søraas, C., Berntsen, A., Magnus, P., Lossius, M. I., Stoltenberg, C., Chin, R., & Surén, P. (2017). Incidence and prevalence of childhood epilepsy: A nationwide cohort study. Pediatrics, 139(5), e20163908.",
  "Reilly, C., Atkinson, P., Das, K. B., Chin, R. F. M., Aylett, S. E., Burch, V., Gillberg, C., Scott, R. C., & Neville, B. G. R. (2014). Neurobehavioral comorbidities in children with active epilepsy: A population-based study. Pediatrics, 133(6), e1586–e1593.",
  "Masur, D., Shinnar, S., Cnaan, A., Shinnar, R. C., Clark, P., Wang, J., Weiss, E. F., Hirtz, D. G., & Glauser, T. A. (2013). Pretreatment cognitive deficits and treatment effects on attention in childhood absence epilepsy. Neurology, 81(18), 1572–1580.",
  "Binnie, C. D. (2003). Cognitive impairment during epileptiform discharges: Is it ever justifiable to treat the EEG? The Lancet Neurology, 2(12), 725–730.",
  "National Institute for Health and Care Excellence. (2022). Epilepsies in children, young people and adults (NICE guideline NG217). NICE. — check for updates.",
  "Epilepsy Ireland. (n.d.). Information for schools and teachers [Website]. https://www.epilepsy.ie/ — check current resources and training.",
 ],

 "pathway": {
  "age": "Any age. Incidence is highest in infancy; childhood absence epilepsy and self-limited focal epilepsies typically emerge in the primary years; juvenile myoclonic epilepsy in adolescence (ILAE syndrome descriptions — check onset ranges). In school, the EP most often meets a diagnosed child whose learning, attention or mood is causing concern — or an undiagnosed child with 'daydreaming' that turns out to be absences.",
  "who_diagnoses": "Ireland: a paediatrician or paediatric neurologist, usually with EEG and sometimes MRI; hospital-based paediatric neurology services (e.g. Children's Health Ireland) for complex cases; epilepsy specialist / advanced nurse practitioners support ongoing care in many areas — check local service. The GP is the usual first step. The EP never diagnoses epilepsy.",
  "who_wrote_report": "Paediatric neurologist or paediatrician (clinic letter); epilepsy specialist nurse (care plan, emergency medication plan); CDNT multidisciplinary report where there are wider developmental needs; neuropsychologist in a hospital service (detailed cognitive profile). An emergency care plan is a medical/school document, not a psychological report.",
  "refer_to": "Back to the treating team via the parents (with consent) for any change in seizures, learning, behaviour or mood. GP for undiagnosed episodes. CDNT where there are complex developmental needs. CAMHS or Primary Care Psychology for anxiety or low mood meeting their threshold. Department Home Tuition Scheme or hospital school for prolonged absence — check eligibility.",
  "sooner": "'Brief seizures are very easy to miss — they look like daydreaming, and nobody could have been expected to know. What matters now is that the school plans around what we know.'",
 },

 "differential": [
  "DAYDREAMING / INATTENTION (including ADHD, inattentive presentation) — can be interrupted by calling the child's name or touch; absences typically cannot. Describe; do not decide.",
  "FUNCTIONAL / DISSOCIATIVE SEIZURES (psychogenic non-epileptic seizures) — genuine, involuntary, not epileptic. A neurology diagnosis; handle with the same care and no suggestion of 'putting it on'.",
  "FAINTING (syncope), breath-holding spells and reflex anoxic events — common in children and not epilepsy. Medical question.",
  "TICS AND STEREOTYPIES — repetitive movements with awareness preserved. See Tourette's / tic disorders; CDNT or neurology.",
  "SLEEP DEPRIVATION OR SLEEP DISORDER — daytime lapses and fogginess; ask about sleep and refer via GP.",
  "TRAUMA-RELATED DISSOCIATION — 'blanking out' under stress; safeguarding lens and CAMHS / Tusla routes as appropriate.",
 ],

 "next": [
  "With consent, get the latest medical letter and the school's Individual Healthcare / emergency care plan; read the seizure description before observing.",
  "Ask the teacher to keep a two-week seizure-and-learning log (time, duration, what was missed, recovery).",
  "On assessment days, record seizures, sleep and timing; be ready to stop.",
  "Write classroom recommendations for missed information, recovery and fatigue at the right Continuum level, with named adult and review date.",
  "Share observations with the treating team via the parents; refer on for mood, learning or complex needs as indicated.",
 ],

 "presentations": [
  "Medication effects on attention and learning",
  "Fatigue, sleep and time-of-day effects on attention",
  "Fatigue and stamina needs",
  "Sustained attention in whole-class vs one-to-one",
  "Following multi-step verbal instructions",
  "Chronic illness affecting school",
  "Missed curriculum from hospital admissions",
  "Re-entry to school after illness",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — highest incidence; CDNT and paediatrics lead",
   "prevalence": "Incidence highest in infancy (Aaberg et al., 2017); febrile seizures are common and are NOT epilepsy.",
   "see": "Some infant and early-childhood epilepsies come with developmental delay; others do not. The EP question is usually developmental: milestones, play, communication and adaptive skills, and whether the preschool has a care plan and trained staff. Describe development; do not link it causally to the seizures without medical input.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Griffiths III", "Bayley-4", "Vineland-3", "WPPSI-IV UK"],
  },
  "School Age": {
   "applies": "YES — main window for absence epilepsy and for learning-impact questions",
   "prevalence": "About 0.6% at age 10 in a national cohort (Aaberg et al., 2017) — check before quoting.",
   "see": "Staring spells mistaken for daydreaming; missed instructions; variable performance day to day; tiredness after nocturnal seizures; slower processing. Anxiety about seizures in front of peers may emerge. Attention concerns need careful description rather than attribution.",
   "tools": ["WISC-V UK", "TEA-Ch2", "BRIEF-2", "Conners-4", "WIAT-III UK", "SDQ", "ABAS-3"],
  },
  "Adolescent": {
   "applies": "YES — new syndromes emerge; self-management, mood and exams dominate",
   "prevalence": "Adolescent-specific rate not stated here — check.",
   "see": "Sleep loss, exam stress and social life interact with seizure control. Stigma, disclosure to peers, low mood and anxiety become central. Practical questions: RACE, subject choices (e.g. practicals), driving and independence. Self-report is essential.",
   "tools": ["WISC-V UK", "BRIEF-2 self-report", "RCADS self-report", "Access arrangements evidence (RACE)", "WIAT-III UK"],
  },
  "Young Adult": {
   "applies": "YES — transition to adult neurology, further education and work",
   "prevalence": "Adult active epilepsy about 6.4 per 1,000 (Fiest et al., 2017).",
   "see": "Transition from paediatric to adult neurology, disclosure to colleges and employers, driving eligibility and independent medication management. The EP role is usually time-limited: supporting the transition plan and access supports at further or higher education (e.g. DARE, college disability services — check current names).",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — epilepsy is common in pupils with severe or profound intellectual disability and complex needs",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Seizures may be frequent, varied and hard to tell from other behaviours; nursing support, emergency medication protocols and staff training are core. The EP question is usually progress against the setting's own curriculum (L1LPs / L2LPs), communication and the effect of seizure-related fatigue on engagement.",
   "tools": ["Vineland-3 / ABAS-3", "Adaptive measure in place of IQ", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 2. CEREBRAL PALSY
# =====================================================================================
{
 "name": "Cerebral palsy (spastic / dyskinetic / ataxic / mixed)",
 "code": "Not a DSM diagnosis · medical/neurological condition · ICD-11 code — check (cerebral palsy sits in Chapter 08, Diseases of the nervous system; verify subtype codes in the ICD-11 browser before quoting)",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 1. LEARNING (1.6 Co-ordination; 1.2 Language skills where speech or communication is affected)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  LAW_MED,

 "what_it_is": [
  "'A group of permanent disorders of the development of movement and posture, causing activity limitation, that are attributed to non-progressive disturbances that occurred in the developing fetal or infant brain.' The same definition adds that the motor disorder is often accompanied by disturbances of sensation, perception, cognition, communication and behaviour, by epilepsy, and by secondary musculoskeletal problems (Rosenbaum et al., 2007).",
  "The brain injury is NON-PROGRESSIVE; the child's presentation is NOT static. Growth, tone, pain and musculoskeletal changes (e.g. hip displacement, contractures) alter function over time — so a report from age 4 may not describe the child at 11.",
  "Motor types (by predominant movement disorder): SPASTIC (increased tone; the most common), DYSKINETIC (involuntary movements — dystonic or choreoathetoid), ATAXIC (balance and coordination), and MIXED. Distribution is described as UNILATERAL (one side, 'hemiplegia') or BILATERAL ('diplegia' — legs more than arms; 'quadriplegia' — all four limbs).",
  "Function is described with classification systems you should recognise in reports:\n▸ GMFCS — Gross Motor Function Classification System, levels I–V (Palisano et al., 1997).\n▸ MACS — Manual Ability Classification System, I–V (Eliasson et al., 2006).\n▸ CFCS — Communication Function Classification System, I–V (Hidecker et al., 2011).\nLevel I is the least limited; V the most. Quote the level from the report; do not assign it yourself.",
  "Motor severity does NOT predict cognition. A child at GMFCS V with no functional speech may have typical intelligence; a child with mild hemiplegia may have a significant learning difficulty. Every child needs their cognition and communication assessed on their own terms.",
  "Associated difficulties are common and often more educationally significant than the motor impairment: pain, intellectual disability, epilepsy, speech and communication difficulty, visual impairment including cerebral visual impairment (CVI), hearing loss, sleep difficulty, and behaviour or emotional difficulty (Novak et al., 2012 — check proportions before quoting).",
  "Early diagnosis is now possible much earlier than in the past: Novak et al. (2017) recommend identification of high risk of CP before 6 months corrected age using MRI, the General Movements Assessment and the Hammersmith Infant Neurological Examination, so that early intervention can start.",
 ],

 "what_it_is_not": [
  "NOT an intellectual disability. Intellectual disability co-occurs in a substantial minority (Novak et al., 2012 — check proportion) and is absent in many. Assuming low ability because of motor or speech impairment is the most damaging error in this field.",
  "NOT progressive. The brain injury does not worsen. If a child is LOSING skills, that is not CP and needs urgent medical review.",
  "NOT a speech-equals-thought condition. Dysarthria (motor speech difficulty) or no speech tells you about the mouth and breathing muscles, not about understanding or reasoning.",
  "NOT only a physical access issue. Visual-perceptual difficulty, CVI, fatigue, pain and executive difficulty affect learning in ways ramps and lifts do not solve.",
  "NOT 'caused by the birth' in every case. Causes are varied and often prenatal; many have no single identifiable cause. Families frequently carry guilt or grievance — do not speculate on cause.",
  "NOT something that standard tests measure fairly without adaptation. Timed, motor-response or spoken-response items confound motor and speech impairment with cognition. A score obtained without adaptation, or without stating the adaptation, can be a measurement of the disability rather than the child.",
  "NOT the EP's to diagnose or to manage medically (tone management, surgery, orthotics, medication). Those sit with paediatrics, orthopaedics, physiotherapy and the CDNT.",
 ],

 "prevalence": [
  "OVERALL: about 2.1 per 1,000 live births (Oskoui et al., 2013, systematic review and meta-analysis). Roughly one child in 500 — so most schools will have at least one pupil with CP over a few years.",
  "TREND: several high-income countries report declining birth prevalence in recent cohorts — check current figures before quoting (e.g. international CP register data).",
  "IRELAND: no Irish population prevalence figure is stated here — check (Irish CP register / surveillance data, if current).",
  "RISK: higher in preterm and low-birth-weight infants and in multiple births (Oskoui et al., 2013) — do not quote group-specific rates without checking.",
  "EARLY YEARS 0–5: high-risk identification can now be made before 6 months corrected age (Novak et al., 2017); formal diagnosis often confirmed in the first two years.",
  "SCHOOL AGE / ADOLESCENT: prevalence stable (the condition is lifelong); needs change with growth, curriculum demands and independence.",
  "SEX RATIO: slight male excess reported in register studies — exact ratio not stated here, check before quoting.",
 ],

 "cooccurring": [
  {"name": "INTELLECTUAL DISABILITY",
   "rate": "around half in Novak et al. (2012) — check before quoting",
   "presents": "global difficulty with learning and adaptive functioning. Must be established with adapted, motor- and speech-fair methods and an adaptive measure — never inferred from motor severity or absence of speech."},
  {"name": "EPILEPSY",
   "rate": "around one in four in Novak et al. (2012) — check before quoting",
   "presents": "variable attention and performance, fatigue, absences. See the Epilepsy entry; ask whether there is a seizure care plan and whether seizures occurred on assessment days."},
  {"name": "SPEECH, LANGUAGE AND COMMUNICATION DIFFICULTY",
   "rate": "common — rate not stated here, check (Novak et al., 2012)",
   "presents": "dysarthria, no functional speech, or language difficulty. Separate motor speech from language comprehension. Many children need AAC; confirm what system is used and whether all staff use it."},
  {"name": "VISUAL IMPAIRMENT INCLUDING CEREBRAL VISUAL IMPAIRMENT (CVI)",
   "rate": "common — rate not stated here, check",
   "presents": "difficulty finding items on a busy page, recognising faces, navigating crowded spaces, or using pictures on a crowded AAC grid — with 'normal' eye tests. Ask about ophthalmology and a visiting teacher for visual impairment."},
  {"name": "VISUAL-PERCEPTUAL AND VISUOSPATIAL DIFFICULTY",
   "rate": "elevated, particularly in bilateral spastic CP associated with preterm birth — rate not stated here, check",
   "presents": "weak performance on visuospatial and construction tasks, maths layout, copying and map-reading. Separate this from the motor demand of the task."},
  {"name": "PAIN, FATIGUE AND SLEEP DIFFICULTY",
   "rate": "pain is very common (Novak et al., 2012) — check proportion before quoting",
   "presents": "irritability, withdrawal, reduced concentration and 'behaviour' that is actually pain or exhaustion. Ask the child and family directly about pain."},
  {"name": "EMOTIONAL AND BEHAVIOURAL DIFFICULTY",
   "rate": "elevated (Novak et al., 2012) — rate not stated here, check",
   "presents": "frustration, low mood, anxiety or social isolation, often linked to communication barriers, pain and exclusion. Screen for it; do not attribute it to 'the CP'."},
  {"name": "HEARING LOSS",
   "rate": "less common than visual difficulty — rate not stated here, check",
   "presents": "not responding to verbal instructions, which is then misread as cognitive or attention difficulty. Confirm audiology status."},
 ],

 "recommendations": [
  "START WITH ACCESS: seating and positioning (OT/physio), desk height, equipment, room and toilet access, evacuation plan (a Personal Emergency Evacuation Plan — check the school's process). A child who is uncomfortable or poorly positioned cannot demonstrate learning.",
  "COMMUNICATION ACCESS: confirm the child's communication system (speech, signs, AAC device, eye-gaze, partner-assisted scanning) and that ALL staff and peers use it, with the SLT's guidance. Allow wait time — responses can take much longer to produce.",
  "RECORDING WORK: alternatives to handwriting (scribe, keyboard, switch access, speech-to-text, eye-gaze), with OT input. Assistive technology via the Department's assistive technology scheme through the SENO — check current scheme and circular.",
  "FATIGUE AND PAIN: planned rest breaks, reduced written volume, timetabling of therapy so the same subject is not always missed, and a way for the child to signal pain or tiredness.",
  "VISUAL-PERCEPTUAL SUPPORT: uncluttered worksheets, enlarged and spaced materials, high contrast, consistent layouts, fewer items per page — especially where CVI is identified (with visiting teacher for visual impairment input).",
  "INTIMATE CARE AND DIGNITY: a written intimate care plan agreed with the child and parents, consistent trained staff, privacy and choice. The school's Child Safeguarding Statement should cover intimate care procedures (Children First Act 2015).",
  "PARTICIPATION: adapted PE, trips, yard and extracurricular activity, planned with physio/OT. Rosenbaum & Gorter's (2012) 'F-words' (function, family, fitness, fun, friends, future) are a useful frame for the plan.",
  "ASSESSMENT ADAPTATIONS: state every adaptation (response mode, timing, items omitted) and its effect on validity; report index scores that are fair and describe those that are not; use an adaptive measure alongside cognitive measures.",
  "CONTINUUM LEVEL: School Support Plus in most cases, given CDNT involvement. SNA support for care needs (mobility, feeding, toileting, positioning) is an NCSE decision under the current allocation model — check current model and Circular 0030/2014. Special class or special school placement is a NCSE / parent decision informed by your report.",
  "REFER / LIAISE: CDNT (physio, OT, SLT, psychology) is usually the lead; paediatrics / orthopaedics for medical management; ophthalmology and audiology where not current; visiting teacher service for sensory impairment; Enable Ireland and other disability organisations for family support — check current service configuration.",
  "DO NOT infer cognitive ability from motor severity or speech, report a Full Scale IQ from a battery the child could not physically access, or comment on medical treatments (tone management, surgery, medication).",
 ],

 "explain_parent": [
  "'Cerebral palsy affects how the brain controls movement and posture. The injury to the brain happened early and doesn't get worse — though how his body works can change as he grows.'",
  "'How much it affects his movement tells us very little about how he thinks and learns. My job is to find the fairest way for him to show what he knows.'",
  "'Some tests depend on speed, speaking or using your hands. I'll adapt them where I can and I'll say in the report exactly what I changed and which scores I trust.'",
  "'Many children with CP also have things we can't see — tiredness, pain, or difficulty making sense of what they see. Those often matter more in the classroom than the physical side, so I'll ask about them.'",
  "'You're the expert on him. Tell me how he communicates best, what tires him, and what he enjoys — that's where the recommendations come from.'",
  "SIGNPOST: the child's CDNT; Enable Ireland (services and family information — check current configuration since Progressing Disability Services reforms) → https://www.enableireland.ie/ ; Assessment of Need under the Disability Act 2005 via the HSE.",
 ],

 "explain_teacher": [
  "'Don't judge what she understands by how she moves or speaks. Give her a way to answer — pointing, eye-gaze, yes/no, her device — and give her time.'",
  "'Tiredness is real. Physical effort that you don't notice uses up her energy. Plan short, high-value tasks and let her record in whatever way costs her least.'",
  "'Check the page, not just the child. Busy worksheets, small print and crowded pictures may be hard for her to see even if her eye test was fine. Space it out.'",
  "'Her communication system only works if everyone uses it — you, the SNA and the class. Ask the SLT for a quick guide and keep it with the device.'",
  "'Intimate care is done with her, not to her: same people, private, her choices respected, following the written plan.'",
  "'Include her. Find the version of PE, yard and group work that she can take part in — the physio and OT can help design it.'",
 ],

 "explain_child": [
  "YOUNGER: 'Cerebral palsy means the part of your brain that tells your muscles what to do works a bit differently. It's not your fault and it's not catching. Your brain is still busy thinking and learning like everyone else's.'",
  "OLDER: 'CP affects movement and sometimes speech, vision or energy — not who you are or how clever you are. You know best what helps, so we want to hear it from you.'",
  "USE THEIR COMMUNICATION SYSTEM when you talk to them, not to the adult beside them. Address the child first; give real wait time.",
  "ASK (in the child's mode): 'What's the hardest part of the school day?' · 'When do you get most tired?' · 'Does anything hurt in school?' · 'What do you want to do that you're not getting to do?'",
  "SUPPORT SELF-ADVOCACY: help the child build a short script or device message — 'I need more time', 'Can I have it bigger?', 'I'm tired' — that they can use without an adult speaking for them.",
 ],

 "analogies": [
  "THE BAD PHONE LINE: 'The message leaves the brain fine but the line to the muscles is crackly, so the movement that arrives isn't quite what was sent.' Good for younger children and peers.",
  "THE LOCKED PIANO: 'The music is all there — you just can't get at the keys easily. Our job is to find another way to play.' Good for parents and teachers when explaining why standard tests can underestimate ability.",
  "THE HEAVY BACKPACK: 'Every movement she makes is like doing it with a heavy backpack on. By lunchtime she's more tired than anyone else in the room.' Explains fatigue to teachers.",
  "THE F-WORDS (Rosenbaum & Gorter, 2012): function, family, fitness, fun, friends, future — 'what does a good school year look like across all six?' Good for planning meetings; shifts the conversation from fixing to participating.",
 ],

 "language": [
  "'Child with cerebral palsy' or 'child with CP' is widely used. Some disabled people prefer identity-first language ('disabled child'), reflecting the social model. Ask the young person and family.",
  "Avoid 'suffers from', 'wheelchair-bound', 'confined to a wheelchair' — say 'uses a wheelchair'. Avoid 'spastic' as anything other than a quoted medical descriptor of tone; it is widely experienced as a slur.",
  "Avoid 'non-verbal' as shorthand for 'does not understand'. Say 'does not use speech; communicates using…'. 'Minimally speaking' and 'uses AAC' are more precise.",
  "Quote GMFCS / MACS / CFCS levels from the report as the source gives them; do not assign levels yourself.",
  "Describe what the child does with the right access — 'identified the target picture by eye-gaze on 9 of 10 items' — rather than only what they could not do under standard conditions.",
 ],

 "red_flags": [
  "RED FLAG — loss of skills or new neurological symptoms. CP is non-progressive; regression is not CP. Tell parents promptly and, with consent, the medical team.",
  "RED FLAG — signs of pain, distress or behaviour change that no one has explained. Pain is common in CP and under-reported by children who communicate differently. Raise it with parents and the CDNT.",
  "RED FLAG — safeguarding. Disabled children are at significantly higher risk of violence and abuse (Jones et al., 2012) and may be less able to disclose. Unexplained injuries, fear of particular carers or intimate care concerns go to the DLP and Tusla the same day; telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — a report stating a low IQ from a standard battery with no mention of motor, speech or visual adaptations. Treat it as a hypothesis, not a finding, and say so.",
  "BOUNDARY — you do not diagnose CP, classify GMFCS/MACS levels, or advise on medical treatment, orthotics or medication. You assess learning and participation and recommend educational supports (PSI 2.2.2).",
  "WATCH — communication access in your own assessment. If you could not establish a reliable yes/no or response mode, your results are not valid; say so and recommend SLT / AAC review first.",
 ],

 "child_voice": [
  "TALKING MATS — picture symbols placed under 'like / not sure / don't like'. Good because it can be done by pointing, eye-gaze or partner-assisted scanning, and gives children with little or no speech a real say. → https://www.talkingmats.com/",
  "THE CHILD'S OWN AAC SYSTEM — prepare vocabulary with the SLT in advance ('easy', 'hard', 'tired', 'hurts', 'want'). Good because asking a child to give their view in a mode they don't use is not consultation.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS), adapted with symbols and a scribe — good because it is familiar to staff and can be read aloud with yes/no responses. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "PHOTO TOUR OF THE SCHOOL DAY — the child (or a peer, directed by the child) photographs places that are easy, hard or inaccessible. Good because it locates barriers in the environment, not the child.",
  "OBSERVATION AT DIFFERENT TIMES OF DAY — good because fatigue and pain change what the child can show; their voice includes what their body is telling you.",
 ],

 "questions": [
  "Q: 'Does CP mean he has a learning disability?' — A: 'No. Some children with CP have a learning disability and many don't. How much his movement is affected doesn't predict how he thinks. We'll look at that properly, with tests adapted so his movement doesn't get in the way.'",
  "Q: 'Why didn't you give her a full IQ score?' — A: 'Because parts of the test needed speed or hand movements she can't do easily. A total score would have mixed up her movement difficulty with her thinking. I've reported the parts that were fair and explained the rest.'",
  "Q: 'Will he get worse?' — A: 'The brain injury itself doesn't get worse. His body can change as he grows — his physio and medical team keep an eye on that. If you ever see him losing skills, tell his doctor straight away.'",
  "Q: 'Does she need an SNA?' — A: 'SNA support is for care needs — things like mobility, toileting and positioning — and the NCSE decides allocation. My report can describe her care needs clearly so the school has what it needs to make the case.'",
  "Q: 'Should he be in a special school?' — A: 'That's a decision for you, with the SENO and the school, and it depends on what he needs and what each setting can offer. My job is to describe his learning and access needs accurately so you're making the decision with good information.'",
  "Q: 'How do we know what she understands if she can't talk?' — A: 'We give her a way to answer that doesn't need speech — pointing, eye-gaze, her device, yes/no — and we check it's reliable. Her SLT is key here.'",
 ],

 "supervision": [
  "Bring an assessment where you adapted the response mode, and discuss how to write up the adaptation and what it does to the norms.",
  "Ask what adapted or non-standard measures the service uses for children with significant motor or speech impairment, and what training you need first.",
  "Discuss how you establish a reliable yes/no response before testing, and what you do if you can't.",
  "Ask how the service works with CDNTs in this area — who leads, how reports are shared, and how to avoid duplicating assessment.",
  "Bring any intimate care or safeguarding concern and check you followed procedure, after you have acted on it.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I talk to the child in their own communication mode, or did I talk about them to the adult beside them?",
  "ON ASSUMPTIONS — Did the wheelchair or the absence of speech shape my expectations before I tested anything? What evidence did I use?",
  "ON VALIDITY — Did I record every adaptation, and did my conclusions stay within what the adapted assessment could support?",
  "ON THE INVISIBLE NEEDS — Did I ask about pain, fatigue, vision and seizures, or only about access and movement?",
  "ON PARTICIPATION — Do my recommendations get the child into the life of the class, or only into the classroom?",
  "WHAT GOOD LOOKS LIKE: 'I spent the first session establishing a reliable eye-gaze yes/no with the SLT present. Receptive vocabulary and non-verbal reasoning were then assessed by eye-gaze; both were in the average range. The report said so, explained the adaptations, and the school stopped differentiating her work down.'",
  "WHAT POOR LOOKS LIKE: 'Full Scale IQ extremely low; unable to complete Block Design, Coding or Symbol Search.' — a score that measures the motor impairment, with no adaptation recorded.",
 ],

 "citations": [
  "Rosenbaum, P., Paneth, N., Leviton, A., Goldstein, M., & Bax, M. (2007). A report: The definition and classification of cerebral palsy April 2006. Developmental Medicine & Child Neurology, 49(Suppl. 109), 8–14.",
  "Palisano, R., Rosenbaum, P., Walter, S., Russell, D., Wood, E., & Galuppi, B. (1997). Development and reliability of a system to classify gross motor function in children with cerebral palsy. Developmental Medicine & Child Neurology, 39(4), 214–223.",
  "Eliasson, A.-C., Krumlinde-Sundholm, L., Rösblad, B., Beckung, E., Arner, M., Öhrvall, A.-M., & Rosenbaum, P. (2006). The Manual Ability Classification System (MACS) for children with cerebral palsy: Scale development and evidence of validity and reliability. Developmental Medicine & Child Neurology, 48(7), 549–554.",
  "Hidecker, M. J. C., Paneth, N., Rosenbaum, P. L., Kent, R. D., Lillie, J., Eulenberg, J. B., Chester, K., Jr., Johnson, B., Michalsen, L., Evatt, M., & Taylor, K. (2011). Developing and validating the Communication Function Classification System for individuals with cerebral palsy. Developmental Medicine & Child Neurology, 53(8), 704–710.",
  "Oskoui, M., Coutinho, F., Dykeman, J., Jetté, N., & Pringsheim, T. (2013). An update on the prevalence of cerebral palsy: A systematic review and meta-analysis. Developmental Medicine & Child Neurology, 55(6), 509–519.",
  "Novak, I., Hines, M., Goldsmith, S., & Barclay, R. (2012). Clinical prognostic messages from a systematic review on cerebral palsy. Pediatrics, 130(5), e1285–e1312.",
  "Novak, I., Morgan, C., Adde, L., Blackman, J., Boyd, R. N., Brunstrom-Hernandez, J., Cioni, G., Damiano, D., Darrah, J., Eliasson, A.-C., de Vries, L. S., Einspieler, C., Fahey, M., Fehlings, D., Ferriero, D. M., Fetters, L., Fiori, S., Forssberg, H., Gordon, A. M., … Badawi, N. (2017). Early, accurate diagnosis and early intervention in cerebral palsy: Advances in diagnosis and treatment. JAMA Pediatrics, 171(9), 897–907.",
  "Rosenbaum, P., & Gorter, J. W. (2012). The 'F-words' in childhood disability: I swear this is how we should think! Child: Care, Health and Development, 38(4), 457–463.",
  "Jones, L., Bellis, M. A., Wood, S., Hughes, K., McCoy, E., Eckley, L., Bates, G., Mikton, C., Shakespeare, T., & Officer, A. (2012). Prevalence and risk of violence against children with disabilities: A systematic review and meta-analysis of observational studies. The Lancet, 380(9845), 899–907.",
 ],

 "pathway": {
  "age": "Increasingly in infancy: high risk of CP can be identified before 6 months corrected age (Novak et al., 2017), especially in infants followed up after preterm birth or neonatal intensive care. Milder unilateral CP may be noticed later, when hand preference appears unusually early or walking is delayed. By school entry almost all children with CP are diagnosed; the EP question is learning and access, not identification.",
  "who_diagnoses": "Ireland: a paediatrician, paediatric neurologist or neonatologist, usually with neuroimaging, often via neonatal follow-up clinics or the CDNT. Physiotherapists and OTs contribute functional classification (GMFCS, MACS). The EP does not diagnose CP.",
  "who_wrote_report": "Paediatrician or neurologist (diagnostic letter); CDNT multidisciplinary report (physio, OT, SLT, psychology); orthopaedic or gait-lab reports; Assessment of Need report (Disability Act 2005); earlier reports from services now reconfigured into CDNTs under Progressing Disability Services (e.g. Enable Ireland, Central Remedial Clinic — check current configuration).",
  "refer_to": "CDNT (usually already involved) for therapy and psychology; paediatrics for medical questions; ophthalmology / audiology if not current; visiting teacher service for visual or hearing impairment; SENO for SNA, assistive technology and placement questions; CAMHS or Primary Care Psychology for mental health needs meeting threshold.",
  "sooner": "'Most children with CP are picked up by services early, so that's rarely the question. What we can always do sooner is make sure she's being assessed fairly and that the school is planning for the things that can't be seen — tiredness, vision, pain.'",
 },

 "differential": [
  "DCD — motor coordination difficulty without the neurological signs of CP; much more common and milder. Physio / paediatric assessment separates them.",
  "PROGRESSIVE NEUROLOGICAL OR NEUROMUSCULAR CONDITIONS (e.g. muscular dystrophy, metabolic or neurodegenerative conditions) — loss of skills over time. Urgent medical review; not CP.",
  "ACQUIRED BRAIN INJURY — onset after early development (e.g. after infection or trauma in later childhood); different trajectory and rehabilitation pathway.",
  "GENETIC SYNDROMES with motor involvement — may present similarly; genetic testing sits with medical teams.",
  "SPINA BIFIDA — lower-limb and continence involvement from spinal-cord lesion rather than brain; see Spina bifida entry.",
 ],

 "next": [
  "With consent, get the CDNT and medical reports; note GMFCS / MACS / CFCS levels, communication system, vision and hearing status, and seizures.",
  "Plan the assessment around access: positioning, response mode, reliable yes/no, breaks — ideally with the SLT or OT before the session.",
  "Use adapted cognitive measures plus an adaptive measure; record every adaptation.",
  "Write recommendations for access, communication, recording, fatigue, vision and intimate care at School Support Plus, with named staff and review date.",
  "Liaise with the CDNT and the SENO; agree who leads.",
 ],

 "presentations": [
  "Physical disability (non-cerebral palsy)",
  "Multiple disabilities",
  "AAC and communication access",
  "Fatigue and stamina needs",
  "Fine motor difficulty (handwriting, pencil grip)",
  "Gross motor difficulty (PE, balance, ball skills)",
  "Handwriting speed and legibility under time pressure",
  "Assistive technology not yet trialled",
  "Chronic illness affecting school",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — identification and early intervention period; CDNT leads",
   "prevalence": "About 2.1 per 1,000 live births (Oskoui et al., 2013).",
   "see": "Delayed motor milestones, atypical tone or asymmetry; feeding and communication difficulties in some. The EP role is usually developmental and preschool-inclusion focused: communication, play, adaptive skills, AIM supports and transition to primary school. Standard developmental scales need adaptation for motor response.",
   "tools": ["Bayley-4", "Griffiths III", "Vineland-3", "Preschool Language Scales-5 (PLS-5)", "Communication Matrix / AAC review"],
  },
  "School Age": {
   "applies": "YES — learning, access and participation questions dominate",
   "prevalence": "Lifelong condition; school-age prevalence reflects birth prevalence (Oskoui et al., 2013).",
   "see": "Recording difficulty, fatigue, visual-perceptual difficulty and communication access are the main barriers. Learning profiles range from gifted to severe intellectual disability. Assessment must be adapted and every adaptation recorded; receptive and pointing-response measures are often fairer than full batteries.",
   "tools": ["BPVS-3", "WISC-V UK", "WNV (Wechsler Non-Verbal)", "ABAS-3", "Vineland-3", "Communication Matrix / AAC review"],
  },
  "Adolescent": {
   "applies": "YES — independence, identity, exams and transition",
   "prevalence": "Lifelong; adolescent rate as for childhood.",
   "see": "Growth can bring increased pain, fatigue or loss of mobility; social isolation and self-image become central. Practical questions: RACE (e.g. scribe, extra time, assistive technology), subject access, personal assistance and transition planning. The young person's own voice must lead.",
   "tools": ["WISC-V UK", "Access arrangements evidence (RACE)", "ABAS-3", "Communication Matrix / AAC review"],
  },
  "Young Adult": {
   "applies": "YES — transition to adult services, further or higher education and work",
   "prevalence": "Lifelong; adult rate not stated here — check.",
   "see": "Transition from CDNT to adult disability services; access routes into further and higher education (e.g. DARE, college disability services and supports — check current names); personal assistance, independent living and employment. The EP role is usually limited to contributing to the transition plan.",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Vineland-3 adult"],
  },
  "Special Setting": {
   "applies": "YES — many pupils with CP and complex needs attend special schools or classes",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Complex physical, communication, sensory and health needs; nursing and therapy on site in some settings. EP focus: communication access, meaningful curriculum (L1LPs / L2LPs), consistency of AAC across staff, and whether the child's cognition has been assessed fairly or assumed.",
   "tools": ["Communication Matrix / AAC review", "Vineland-3 / ABAS-3", "Adaptive measure in place of IQ"],
  },
 },
},

# =====================================================================================
# 3. SPINA BIFIDA
# =====================================================================================
{
 "name": "Spina bifida (including associated hydrocephalus)",
 "code": "Not a DSM diagnosis · medical/neurological condition · ICD-11 code — check (spina bifida is a neural tube defect; ICD-11 may place it in Chapter 20, Developmental anomalies, rather than Chapter 08 as Part D lists — verify in the ICD-11 browser before quoting)",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 1. LEARNING (1.5 Maths skills; 1.3 Comprehension and general ability; 1.1 Attention) where hydrocephalus affects learning",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  LAW_MED,

 "what_it_is": [
  "A NEURAL TUBE DEFECT: the spinal column does not close fully in the first weeks of pregnancy, affecting the spinal cord and nerves below the level of the lesion (Copp et al., 2015).",
  "Forms you will see in reports:\n▸ SPINA BIFIDA OCCULTA — a hidden gap in the vertebrae; usually no symptoms and usually NOT educationally relevant.\n▸ MENINGOCELE — a sac of fluid without spinal cord involvement; often milder effects.\n▸ MYELOMENINGOCELE (MMC) — spinal cord and nerves involved; the form with significant motor, sensory, continence and learning implications. Most educational literature is about MMC.",
  "Physical effects depend on the LEVEL of the lesion: weakness or paralysis of the legs, reduced sensation below the lesion (so injuries and pressure sores can go unnoticed), and NEUROGENIC BLADDER AND BOWEL — continence is managed, commonly by clean intermittent catheterisation and a bowel programme.",
  "HYDROCEPHALUS — build-up of cerebrospinal fluid in the brain — occurs in most children with MMC and is often treated with a SHUNT (Copp et al., 2015 — check proportion before quoting). It is usually accompanied by the Chiari II malformation of the hindbrain. Hydrocephalus, not the spinal lesion, drives most of the learning profile.",
  "The COGNITIVE PHENOTYPE (Dennis et al., 2006; Dennis & Barnes, 2010) is described as relative strength in 'assembled' skills — word decoding, vocabulary, grammar, fluent speech — alongside relative weakness in 'associative' skills that require integration — reading comprehension and inference, maths problem-solving, visuospatial processing, attention, time estimation and executive functions.",
  "That profile HIDES need. A child who reads aloud fluently and talks articulately may understand much less than they appear to, and may struggle markedly in maths. Teachers often judge ability by speech.",
  "Primary prevention is folic acid before and in early pregnancy (MRC Vitamin Study Research Group, 1991). Prenatal surgical repair in selected cases reduced the need for shunting in a major trial (Adzick et al., 2011). Neither changes what you do in school; both may come up in family conversations — do not comment beyond signposting.",
 ],

 "what_it_is_not": [
  "NOT always significant. Spina bifida occulta is common and usually of no educational consequence. Check which form is on the medical letter before assuming need.",
  "NOT only a physical disability. For children with MMC and hydrocephalus, learning, attention and executive needs are often more educationally significant than mobility — and more often missed.",
  "NOT captured by fluent speech or good reading aloud. Surface verbal skill can mask weak comprehension, weak inference and weak maths reasoning (Dennis & Barnes, 2010). The historical term 'cocktail party' speech described this and is best avoided in reports.",
  "NOT an intellectual disability by default. Many children with MMC have cognition in or near the typical range; intellectual disability occurs in some. A full profile, not an assumption, is needed.",
  "NOT a continence issue for the school to 'train'. Neurogenic bladder and bowel are medical; the child cannot control them by effort. They require a care plan, privacy, trained staff and dignity — never sanctions, comment or public management.",
  "NOT stable in every case. A blocked or failing shunt can cause deterioration, and a slow decline in school performance or behaviour may be an early sign. Change is information for the medical team, not a behaviour problem.",
  "NOT caused by anything the family did. Folic acid lowers risk; it does not eliminate it, and many causes are multifactorial. Do not raise prevention with parents of an affected child unless they ask; then signpost.",
 ],

 "prevalence": [
  "OVERALL: neural tube defects are among the most common serious congenital anomalies; birth prevalence varies by country and period and has fallen with folic acid and prenatal screening (Copp et al., 2015) — no figure stated here, check before quoting.",
  "IRELAND: Ireland has historically had among the higher neural tube defect rates in Europe; current rate not stated here — check (EUROCAT / Irish congenital anomaly surveillance, and Spina Bifida Hydrocephalus Ireland).",
  "HYDROCEPHALUS IN MMC: the majority of children with MMC have hydrocephalus and many have shunts (Copp et al., 2015) — proportion not stated here, check.",
  "EARLY YEARS 0–5: diagnosed prenatally or at birth; open lesions are repaired in the newborn period. Educational questions start with preschool inclusion.",
  "SCHOOL AGE 6–12: learning profile becomes visible as curriculum shifts from decoding to comprehension, and from number facts to problem-solving.",
  "ADOLESCENT 13–16: executive demands, independence in self-care (including catheterisation), body image and social life become central.",
  "SEX RATIO: reported slight female excess for neural tube defects in some studies — not stated here as a figure, check.",
 ],

 "cooccurring": [
  {"name": "HYDROCEPHALUS (with shunt) AND CHIARI II MALFORMATION",
   "rate": "majority of children with MMC — rate not stated here, check (Copp et al., 2015)",
   "presents": "the source of most learning and attention needs. Shunt malfunction can present as headache, vomiting, drowsiness, irritability or a drop in performance. Any such change goes to parents and the medical team the same day under the care plan."},
  {"name": "MATHS DIFFICULTY",
   "rate": "common in MMC (Dennis & Barnes, 2010) — rate not stated here, check",
   "presents": "weak number sense, estimation, word problems, geometry and multi-step calculation, sometimes with adequate recall of taught facts. Often more marked than literacy difficulty; assess maths specifically."},
  {"name": "READING COMPREHENSION DIFFICULTY (with adequate decoding)",
   "rate": "common in MMC (Dennis & Barnes, 2010) — rate not stated here, check",
   "presents": "fluent, accurate reading aloud with weak understanding, inference and integration across a text. A single-word or accuracy test will miss it; use a comprehension measure."},
  {"name": "ATTENTION DIFFICULTY / ADHD",
   "rate": "elevated in MMC, mainly inattentive — rate not stated here, check",
   "presents": "slow, drifting attention and difficulty shifting between tasks, rather than hyperactivity. Describe carefully; diagnosis is for CAMHS / CDNT."},
  {"name": "EXECUTIVE FUNCTION DIFFICULTY",
   "rate": "common (Dennis & Barnes, 2010) — rate not stated here, check",
   "presents": "difficulty planning, organising, managing time and self-care routines (including catheterisation schedules) independently. Becomes more visible with age as adult scaffolding is withdrawn."},
  {"name": "VISUOSPATIAL AND FINE MOTOR DIFFICULTY",
   "rate": "common — rate not stated here, check",
   "presents": "weak handwriting, copying, diagrams, map and graph work and construction tasks, including upper-limb clumsiness not explained by the spinal lesion."},
  {"name": "ANXIETY, LOW MOOD AND SOCIAL ISOLATION",
   "rate": "elevated in adolescence — rate not stated here, check",
   "presents": "withdrawal, school avoidance or low self-worth, often linked to continence worries, body image, hospital admissions and exclusion from peer activity. Ask directly and in private."},
 ],

 "recommendations": [
  "ASSESS BEYOND THE SURFACE. Measure reading comprehension (not only accuracy), maths reasoning, attention and executive function. Report the gap between fluent speech/decoding and comprehension explicitly — it is the finding teachers most need.",
  "CHECK UNDERSTANDING, NOT FLUENCY: ask the child to explain, predict or apply, rather than repeat. Teach inference explicitly; use graphic organisers to link ideas across a text.",
  "MATHS: concrete and visual materials, explicit teaching of problem-solving steps, worked examples, reduced visual clutter, and practice with estimation and number sense. Consider a targeted maths intervention at School Support.",
  "EXTERNAL EXECUTIVE SUPPORTS: visual schedules, checklists for multi-step tasks and self-care routines, timers, and explicit teaching of planning — with a plan to fade adult prompting gradually.",
  "CONTINENCE AND DIGNITY: an Individual Healthcare Plan and intimate care plan agreed with parents, the child and the medical team (continence nurse, if involved); private, accessible toilet facilities; trained, consistent staff; discreet timing so the child does not miss the same lesson every day; a plan for accidents that protects privacy. Build towards the young person's own independence in self-catheterisation where medically appropriate.",
  "SKIN AND SENSATION: with reduced sensation, pressure sores and injuries can go unnoticed. Positioning and movement breaks as per the care plan; care with hot surfaces and equipment. The care plan, not the EP, sets these.",
  "SHUNT AWARENESS: ensure the care plan names the signs of shunt problems and what staff do (contact parents, emergency services). The EP's contribution is to flag that a sustained change in learning or behaviour should be reported, not interpreted.",
  "CONTINUUM LEVEL: School Support Plus where the CDNT or hospital team is involved. SNA support for care needs (toileting, catheterisation, mobility) is an NCSE decision under the current allocation model — check current model and Circular 0030/2014.",
  "REFER / LIAISE: CDNT (physio, OT, psychology); hospital spina bifida / neurosurgery and urology teams via the parents; Spina Bifida Hydrocephalus Ireland for family support; CAMHS or Primary Care Psychology for mental health needs meeting threshold.",
  "DO NOT interpret continence as behaviour, comment on shunt function, surgery or medication, or conclude 'no learning difficulty' from good oral language and reading accuracy alone.",
 ],

 "explain_parent": [
  "'Spina bifida affects the spine and the nerves below it — that's the movement and continence side. The hydrocephalus is what can affect learning, and that's the part I'm looking at.'",
  "'A lot of children with spina bifida and hydrocephalus talk well and read aloud well. That's a real strength — but it can make people think they understand more than they do. So I test understanding directly, and maths, and planning.'",
  "'If you ever notice she's more tired, has headaches, is getting worse at school or just isn't herself for a while, tell her medical team. Those changes can matter with a shunt, and school should tell you too.'",
  "'Her continence care is a medical need. The school's job is to do it privately, respectfully and with trained people — and to help her do more of it herself as she gets older, at her pace.'",
  "'My recommendations will focus on how she learns best — explaining, checking understanding, and supporting maths and organisation.'",
  "SIGNPOST: Spina Bifida Hydrocephalus Ireland (SBHI — family support, education and continence information; check current services) → https://www.sbhi.ie/ ; the child's CDNT; the hospital spina bifida team.",
 ],

 "explain_teacher": [
  "'Don't judge his understanding by how well he talks or reads aloud. Ask him to explain it back, give an example, or tell you what happens next.'",
  "'Maths is often the hardest area — especially word problems, shape and space, and anything with several steps. Use concrete materials, worked examples and clean, uncluttered pages.'",
  "'Organisation doesn't come naturally. Give him checklists and routines, and plan to reduce the prompting slowly rather than all at once.'",
  "'Toileting and catheterisation are medical. Private, discreet, by the plan, never commented on in front of others — and never treated as behaviour.'",
  "'If his work or behaviour drops over days or weeks, or he complains of headaches or is unusually sleepy, tell his parents that day. With a shunt, changes like that need checking by his medical team.'",
  "'Keep him in PE, trips and yard with the right planning. Being left out hurts more than most of the physical difficulties.'",
 ],

 "explain_child": [
  "YOUNGER: 'Spina bifida means your back grew a bit differently before you were born. It changes how your legs and your wee and poo work. It's nobody's fault. Lots of grown-ups help so you can do everything at school.'",
  "OLDER: 'Spina bifida and hydrocephalus can affect movement and continence, and sometimes things like maths, organising or remembering what you read. You're good at talking and reading — we want to make sure the understanding keeps up with that.'",
  "ASK (in private): 'Is there anything about going to the toilet at school that bothers you?' · 'Which subjects feel hardest?' · 'Is there anything you'd like to do in school that you're not able to do yet?'",
  "RESPECT PRIVACY: never discuss continence in front of peers or without the child's agreement. Let them choose what classmates know.",
  "BUILD INDEPENDENCE: 'What part of your care would you like to do yourself this year?' — goals the child sets are more likely to be kept.",
 ],

 "analogies": [
  "THE BROKEN CABLE: 'Messages travel down the spine like a cable. Below the break, the messages don't get through as well — so legs, feeling and bladder work differently.' Good with younger children and peers.",
  "THE FLUENT TOUR GUIDE: 'She can read the whole guidebook aloud beautifully — but ask her how the rooms connect and it's much harder.' Explains the decoding-versus-comprehension gap to teachers and parents.",
  "THE PARTS WITHOUT THE PLAN: 'He has all the bricks — the facts and the words. Putting them together into a plan or a problem is the hard part.' Explains the assembled-versus-associative profile (Dennis & Barnes, 2010).",
  "THE DRAIN (for the shunt): 'The shunt is a drain that keeps fluid from building up. Most of the time you'd never know it's there — but if the drain blocks, things change, and that's why we tell the doctors.' Good for parents and staff.",
 ],

 "language": [
  "'Child/young person with spina bifida' is widely used; some disabled people prefer identity-first language. Ask.",
  "Use 'spina bifida' with the form where known — 'myelomeningocele', 'spina bifida occulta' — as it appears in the medical report. Don't simplify it into a single label that hides the difference.",
  "Avoid 'wheelchair-bound' ('uses a wheelchair'), 'incontinent' as a description of the child ('manages continence with…'), and 'accidents' in reports without context.",
  "Avoid 'cocktail party speech' or 'hyperverbal' in reports; describe the profile: 'fluent expressive language and accurate reading, with comprehension and inference significantly weaker'.",
  "Health and continence information is special-category data (GDPR). Share only what staff need, with consent.",
 ],

 "red_flags": [
  "RED FLAG — signs of possible shunt problems: headache, vomiting, unusual drowsiness, irritability, visual changes, seizures, or a decline in school performance or behaviour. Tell the parents and follow the care plan the same day; in an emergency, the school calls emergency services. Do not wait to 'see how it goes'.",
  "RED FLAG — gradual loss of skills, new weakness or changes in continence or walking. May indicate tethered cord or other medical issues. Medical, not educational — parents and medical team promptly.",
  "RED FLAG — safeguarding. Disabled children are at higher risk of abuse (Jones et al., 2012) and intimate care creates specific vulnerabilities. Concerns go to the DLP and Tusla the same day under Children First; telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — bullying or humiliation related to continence, or staff managing it publicly. Address immediately with the principal; it is both a welfare and a dignity issue.",
  "BOUNDARY — you do not diagnose, interpret shunt function, or advise on continence management, surgery or medication. You describe the learning profile and recommend educational supports (PSI 2.2.2).",
  "WATCH — a report stating 'no learning difficulty' based on vocabulary and reading accuracy alone. Check comprehension, maths and executive function before accepting it.",
 ],

 "child_voice": [
  "PRIVATE ONE-TO-ONE CONVERSATION with an agreed stop signal — good because continence and body image are the topics most likely to matter and least likely to be raised in company.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it gives a structured, familiar route into what is hard without starting from the condition. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "PHOTO OR MAP TOUR OF THE SCHOOL — the child marks places that are easy, hard or embarrassing to get to (including toilets). Good because it locates barriers in the building and routine.",
  "SCALING FOR INDEPENDENCE (0–10: 'how much of your care do you do yourself?' / 'where would you like to be by summer?') — good because it gives the child ownership of self-care goals.",
  "SBHI youth resources and peer groups — Irish and condition-specific. Good because meeting others with spina bifida can shape how a young person talks about their own needs. → https://www.sbhi.ie/",
 ],

 "questions": [
  "Q: 'She reads so well — how can she have a learning difficulty?' — A: 'Reading aloud and understanding are different skills. With hydrocephalus it's common for decoding and vocabulary to be strong while understanding, inference and maths are harder. That's why I test comprehension directly.'",
  "Q: 'Will the shunt affect his learning?' — A: 'The hydrocephalus the shunt treats can affect some areas of learning, like maths and organisation. How the shunt is working is for his medical team. What I'd ask is that any change in his schoolwork or how he seems is passed on to them.'",
  "Q: 'Who should do his catheterisation in school?' — A: 'That's set out in his care plan with the medical team, and staffing is for the school and the NCSE through the SNA process. What I can do is describe the care need clearly and make sure privacy and dignity are in the plan.'",
  "Q: 'Should she be doing it herself by now?' — A: 'Independence is a good goal, and it depends on her medical team's advice, her motor skills and her organisation. We can build the steps into her plan gradually, with her choosing the pace where possible.'",
  "Q: 'Is maths just not her thing?' — A: 'Maths difficulty is very common with spina bifida and hydrocephalus — it's about how the brain processes space, quantity and problem-solving, not about effort. The right teaching approach makes a difference.'",
  "Q: 'Could we have prevented this?' — A: 'Spina bifida has many contributing causes and it isn't anyone's fault. Spina Bifida Hydrocephalus Ireland has good information if you want to read more, and your medical team can talk it through with you.'",
 ],

 "supervision": [
  "Bring a case with a fluent-speech, weak-comprehension profile and discuss how to present the gap so teachers believe it.",
  "Ask what the school should do, and what you should do, if a child with a shunt seems unwell during your session.",
  "Discuss how to write about continence and intimate care in a report — what to include, how to protect dignity, and who reads the report.",
  "Ask how to liaise with hospital spina bifida teams as well as the CDNT, and how consent works across both.",
  "Discuss how to build independence goals into a plan without overriding medical advice.",
 ],

 "reflection": [
  "ON HOW I EXPLAINED IT — Did I explain the learning profile in a way the teacher can use tomorrow, or did I explain the anatomy?",
  "ON SURFACE SKILLS — Did fluent speech and reading lead me to under-assess? Did I measure comprehension, maths and executive function?",
  "ON DIGNITY — Did my report or my conversations expose continence details beyond what was needed? Would the young person be comfortable reading what I wrote?",
  "ON CHANGE OVER TIME — Did I ask whether anything has changed recently, and would I recognise a change that needs medical attention?",
  "ON INDEPENDENCE — Did the child have a say in the goals, or did the adults decide?",
  "WHAT GOOD LOOKS LIKE: 'The teacher saw a bright, chatty reader who was lazy in maths. Reading accuracy was high, comprehension and maths reasoning were low. I showed the teacher two comprehension questions the child answered fluently but wrongly. The plan changed to checking understanding and concrete maths, and the teacher stopped describing effort.'",
  "WHAT POOR LOOKS LIKE: 'Verbal skills average; reading age above chronological age; no further assessment indicated.' — the profile that spina bifida and hydrocephalus is known for, missed.",
 ],

 "citations": [
  "Copp, A. J., Adzick, N. S., Chitty, L. S., Fletcher, J. M., Holmbeck, G. N., & Shaw, G. M. (2015). Spina bifida. Nature Reviews Disease Primers, 1, 15007.",
  "Dennis, M., & Barnes, M. A. (2010). The cognitive phenotype of spina bifida meningomyelocele. Developmental Disabilities Research Reviews, 16(1), 31–39.",
  "Dennis, M., Landry, S. H., Barnes, M., & Fletcher, J. M. (2006). A model of neurocognitive function in spina bifida over the life span. Journal of the International Neuropsychological Society, 12(2), 285–296.",
  "Adzick, N. S., Thom, E. A., Spong, C. Y., Brock, J. W., III, Burrows, P. K., Johnson, M. P., Howell, L. J., Farrell, J. A., Dabrowiak, M. E., Sutton, L. N., Gupta, N., Tulipan, N. B., D'Alton, M. E., & Farmer, D. L. (2011). A randomized trial of prenatal versus postnatal repair of myelomeningocele. New England Journal of Medicine, 364(11), 993–1004.",
  "MRC Vitamin Study Research Group. (1991). Prevention of neural tube defects: Results of the Medical Research Council Vitamin Study. The Lancet, 338(8760), 131–137.",
  "Jones, L., Bellis, M. A., Wood, S., Hughes, K., McCoy, E., Eckley, L., Bates, G., Mikton, C., Shakespeare, T., & Officer, A. (2012). Prevalence and risk of violence against children with disabilities: A systematic review and meta-analysis of observational studies. The Lancet, 380(9845), 899–907.",
  "Spina Bifida Hydrocephalus Ireland. (n.d.). Information for families and schools [Website]. https://www.sbhi.ie/ — check current resources.",
 ],

 "pathway": {
  "age": "Usually diagnosed prenatally (routine anomaly scan) or at birth, with surgery in the newborn period for open lesions. Hydrocephalus is identified and often shunted in infancy. Spina bifida occulta may be found incidentally at any age. The EP usually meets the child at school entry or when the curriculum shifts to comprehension and problem-solving (middle primary), when the hidden learning profile shows.",
  "who_diagnoses": "Ireland: obstetric / fetal medicine services prenatally; neonatology, neurosurgery and paediatrics after birth; hospital-based spina bifida multidisciplinary clinics (e.g. within Children's Health Ireland — check current configuration) for ongoing care including urology and orthopaedics. The CDNT provides community therapy. The EP does not diagnose.",
  "who_wrote_report": "Hospital spina bifida team or neurosurgeon (medical letter); continence / urology nurse (continence plan); CDNT multidisciplinary report (physio, OT, psychology); Assessment of Need report; a hospital neuropsychologist (detailed cognitive profile) in some cases.",
  "refer_to": "Parents and the hospital team (via the care plan) for any medical change; CDNT for therapy and psychology; SENO for SNA, equipment and placement questions; SBHI for family support; CAMHS or Primary Care Psychology for mental health needs meeting threshold.",
  "sooner": "'The medical side was picked up early; the learning side often isn't, because children with spina bifida talk and read so well. Noticing it now, when the work is becoming more about understanding, is exactly when it usually shows.'",
 },

 "differential": [
  "SPINA BIFIDA OCCULTA vs MYELOMENINGOCELE — very different implications; check the medical letter before inferring any need.",
  "SPECIFIC LEARNING DIFFICULTY (maths, reading comprehension) — may be part of the spina bifida/hydrocephalus profile or independent; assess the same way, and describe the profile rather than guessing the cause.",
  "ADHD — inattention in MMC is common; diagnosis is a separate question for CAMHS / CDNT.",
  "DLD / SOCIAL (PRAGMATIC) COMMUNICATION DIFFICULTY — fluent but less content-rich talk may resemble a pragmatic difficulty; SLT assessment separates them.",
  "CEREBRAL PALSY — motor difficulty of brain origin rather than spinal; see Cerebral palsy entry.",
 ],

 "next": [
  "With consent, read the medical letter and care plan; confirm the form of spina bifida, whether there is a shunt, and the signs staff have been told to watch for.",
  "Assess reading comprehension, maths reasoning, attention and executive function — not only vocabulary and decoding.",
  "Check the Individual Healthcare Plan and intimate care plan exist and protect privacy; raise gaps with the principal.",
  "Write recommendations for comprehension, maths and organisation at School Support Plus, with named staff and review date.",
  "Liaise with the CDNT and SENO; signpost the family to SBHI.",
 ],

 "presentations": [
  "Physical disability (non-cerebral palsy)",
  "Chronic illness affecting school",
  "Missed curriculum from hospital admissions",
  "Re-entry to school after illness",
  "Numeracy difficulty not meeting SLD criteria",
  "Word problems",
  "Planning and organisation difficulty",
  "Fatigue and stamina needs",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — diagnosed prenatally or at birth; CDNT and hospital teams lead",
   "prevalence": "Birth prevalence not stated here — check (EUROCAT / Irish surveillance; Copp et al., 2015).",
   "see": "Mobility and continence planning for preschool; development of play, language and early number. Early language is often a relative strength; early visuospatial and motor skills may be weaker. EP role is usually preschool inclusion (AIM) and transition to primary school planning.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Griffiths III", "Bayley-4", "Vineland-3"],
  },
  "School Age": {
   "applies": "YES — the learning profile becomes visible as demands shift to comprehension and problem-solving",
   "prevalence": "Lifelong; school-age rate reflects birth prevalence — check.",
   "see": "Fluent speech and accurate decoding alongside weaker reading comprehension, maths reasoning, attention and organisation. Continence care and mobility planning in school. Teachers may judge ability by speech and interpret maths difficulty as effort.",
   "tools": ["WISC-V UK", "YARC (York Assessment of Reading for Comprehension)", "WIAT-III UK maths subtests", "BRIEF-2", "TEA-Ch2", "Beery VMI"],
  },
  "Adolescent": {
   "applies": "YES — executive demands, self-care independence and identity dominate",
   "prevalence": "Lifelong; adolescent rate not stated here — check.",
   "see": "Increasing curricular load exposes executive and comprehension needs; independence in catheterisation and bowel management is a key goal; body image, continence anxiety and social inclusion come to the fore. RACE, subject choices and transition planning are practical questions.",
   "tools": ["WISC-V UK", "WIAT-III UK", "BRIEF-2 self-report", "Access arrangements evidence (RACE)", "RCADS self-report"],
  },
  "Young Adult": {
   "applies": "YES — transition to adult medical and disability services, education and work",
   "prevalence": "Lifelong; adult rate not stated here — check.",
   "see": "Transition from paediatric to adult spina bifida care; independent living, self-care and executive demands of further or higher education (DARE and college disability services — check current names). The EP role is usually a contribution to transition planning.",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form"],
  },
  "Special Setting": {
   "applies": "YES — some pupils, especially with additional intellectual disability or complex health needs, attend special schools or classes",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Complex health care (continence, shunt monitoring, skin care) alongside learning needs. EP focus: whether the learning profile has been assessed rather than assumed, meaningful curriculum, and progress towards self-care independence.",
   "tools": ["Vineland-3 / ABAS-3", "Adaptive measure in place of IQ"],
  },
 },
},

]
