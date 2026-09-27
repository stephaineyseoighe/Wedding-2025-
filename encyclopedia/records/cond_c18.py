# CONDS records: Muscular dystrophy; Acquired brain injury; Foetal Alcohol Spectrum Disorder.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c18.py

NEPS_MED = "5. OTHER (5.3 Medical condition or other diagnosis)"

CONDS = [

# =====================================================================================
# 1. MUSCULAR DYSTROPHY
# =====================================================================================
{
 "name": "Muscular dystrophy",
 "code": "Medical, not a DSM-5-TR diagnosis · ICD-11 Chapter 08 (Diseases of the nervous system) — muscular dystrophies; check the subtype code (e.g. Duchenne, Becker, myotonic) before quoting · ICD-10 G71.0 (muscular dystrophy); myotonic dystrophy is coded separately — check",
 "neps": NEPS_MED + " — and 1. LEARNING (1.2 Language skills · 1.1 Attention) where the Duchenne cognitive profile is present · 3. EMOTIONAL (3.5 Trauma, attachment and loss) where progression, bereavement or anticipatory grief is the focus",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Disability Act 2005 (Assessment of Need) · EPSEN Act 2004 · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR (special category health data)",

 "what_it_is": [
  "A GROUP of inherited muscle conditions that cause progressive weakness and wasting of muscle because a protein needed for muscle fibre integrity is missing or faulty. There are many types, with very different ages of onset, rates of progression and effects on learning. ALWAYS ask 'which muscular dystrophy?' — the answer changes almost everything in this row (Mercuri, Bönnemann & Muntoni, 2019).",
  "DUCHENNE MUSCULAR DYSTROPHY (DMD) is the type you are most likely to meet in primary school. It is X-linked, caused by mutations in the dystrophin gene, and affects almost exclusively boys; some girls and women who carry the gene have symptoms ('manifesting carriers'). Early signs in the pre-school years include late walking, frequent falls, difficulty running and climbing stairs, enlarged calves and using the hands to 'walk up' the legs to stand (Gowers' manoeuvre) (Birnkrant et al., 2018a).",
  "PROGRESSION IN DMD: weakness progresses through childhood; most boys lose independent walking, commonly in the early teens where corticosteroids are used (Birnkrant et al., 2018a — check current figures), followed by increasing upper-limb, respiratory and cardiac involvement. Survival into adulthood is now usual with multidisciplinary care; do not quote a life expectancy figure — check with the medical team and never offer one to a family.",
  "THE BRAIN IS INVOLVED TOO IN DMD. Dystrophin isoforms are expressed in the brain, and cognitive and neurodevelopmental differences are part of the condition — NOT a reaction to disability and NOT caused by the weakness. They are present from early childhood and are generally described as NON-PROGRESSIVE, unlike the muscle disease (Ricotti et al., 2016; Birnkrant et al., 2018b).",
  "THE DMD LEARNING PROFILE: a meta-analysis found mean full-scale IQ about one standard deviation below the population mean, with verbal IQ lower than performance IQ (Cotton, Voudouris & Greenwood, 2001 — check exact figures); a selective difficulty with VERBAL WORKING MEMORY / verbal span (Hinton et al., 2000); and elevated rates of reading difficulty, language difficulty, ADHD, autism and anxiety (Ricotti et al., 2016; Banihani et al., 2015). Many boys have general ability in the typical range, but the whole distribution is shifted down and a substantial minority have an intellectual disability — proportion not stated here, check.",
  "OTHER TYPES YOU MAY MEET: BECKER (dystrophin reduced rather than absent; later onset, slower course); MYOTONIC DYSTROPHY TYPE 1 — the CONGENITAL and CHILDHOOD-ONSET forms are associated with intellectual disability or learning difficulty, communication difficulty, fatigue and daytime sleepiness that are easily misread as low motivation (check with the medical team); FACIOSCAPULOHUMERAL, LIMB-GIRDLE and CONGENITAL muscular dystrophies, some with and many without cognitive involvement.",
  "TREATMENT is medical and changing fast: corticosteroids are standard in DMD and can affect mood, behaviour, weight, bone health and sleep; genetic therapies (e.g. exon-skipping) are licensed for some mutations in some jurisdictions and are the subject of trials. The EP does not advise on medication (PSI 2.2.2) but should know when a boy is starting or changing treatment, because behaviour and fatigue may change (Birnkrant et al., 2018a).",
  "IRISH CONTEXT: diagnosis and medical care sit with paediatric neurology / the national paediatric neuromuscular service within Children's Health Ireland (check the current location and referral route); therapy with the CDNT (physiotherapy, OT, psychology); school supports through the SENO and NCSE; family support from Muscular Dystrophy Ireland, which runs family support and a youth service with Youth Support Workers (MDI, n.d. — check current services).",
 ],

 "what_it_is_not": [
  "NOT one condition. 'Muscular dystrophy' on a file tells you almost nothing until you know the type. Duchenne, Becker, myotonic, facioscapulohumeral and limb-girdle dystrophies differ in onset, course and cognitive involvement (Mercuri et al., 2019).",
  "NOT only a physical condition in Duchenne. Learning, language, attention and social-communication difficulties are part of the condition itself (Ricotti et al., 2016). A boy whose reading is behind is not behind 'because of all the hospital appointments' until you have assessed it.",
  "NOT a cognitive decline. In DMD the muscles deteriorate; the cognitive profile does not follow the same course (Birnkrant et al., 2018b). Do not write 'cognitive skills likely to deteriorate' — it is wrong and frightening.",
  "NOT laziness or low motivation. Fatigue, weakness, steroid side effects, poor sleep (including sleep-disordered breathing later in DMD) and daytime sleepiness in myotonic dystrophy all look like disengagement. Ask about sleep and energy before formulating motivation.",
  "NOT a reason to excuse a boy from learning or from ordinary expectations. Adjust access; keep academic, social and behavioural expectations high. Children with progressive conditions still need a future-oriented education.",
  "NOT a reason to avoid talking about the future — or to impose that conversation. Families differ in what they have shared with the child and with siblings. Follow the family's lead on what the child knows, and never be the first to disclose prognosis.",
  "NOT something the EP diagnoses or explains medically. Diagnosis is genetic and neurological. The EP describes learning and wellbeing, formulates, plans and supports the school and family (PSI 2.2.2).",
 ],

 "prevalence": [
  "DMD: newborn screening data suggest about 1 in 5,000 male births (Mendell et al., 2012 — check the exact figure before quoting). Other published estimates vary with method and population.",
  "ALL MUSCULAR DYSTROPHIES: prevalence varies greatly by type and study — figure not stated here, check (Mercuri et al., 2019).",
  "IRELAND: no Irish population prevalence figure is cited here — check before quoting. Muscular Dystrophy Ireland describes a membership of several hundred individuals and families (MDI, n.d. — check), which reflects membership, not prevalence.",
  "SEX RATIO: DMD and Becker are X-linked and affect almost exclusively males; female carriers can have symptoms (Birnkrant et al., 2018a). Myotonic, facioscapulohumeral and limb-girdle types affect both sexes.",
  "DMD COGNITIVE PROFILE: rates of intellectual disability, ADHD, autism, specific reading difficulty and anxiety are all ELEVATED compared with the general population (Banihani et al., 2015; Ricotti et al., 2016) — exact proportions differ between studies; not stated here, check before quoting.",
  "AGE: DMD is often diagnosed in the early years (commonly around ages 3–5), though diagnostic delay after first parental concern is common — check before quoting a figure. Newborn screening is not routine in Ireland — check current policy.",
 ],

 "cooccurring": [
  {"name": "SPECIFIC LEARNING DIFFICULTY (especially reading)",
   "rate": "elevated in DMD — rate not stated here, check (Ricotti et al., 2016)",
   "presents": "slow decoding, weak phonological skills and poor spelling that are attributed to missed school or fatigue. Assess literacy in its own right, early; it responds to the same structured intervention as in other children."},
  {"name": "VERBAL WORKING MEMORY AND LANGUAGE DIFFICULTY",
   "rate": "characteristic of DMD as a group (Hinton et al., 2000) — rate not stated here",
   "presents": "losing track of multi-step spoken instructions, difficulty following long explanations, weak recall of what was just said. Looks like inattention. Reduce verbal load, write steps down and check understanding by asking him to show you."},
  {"name": "ADHD",
   "rate": "elevated in DMD — rate not stated here, check (Banihani et al., 2015)",
   "presents": "inattention and impulsivity that may be put down to boredom from sitting out of physical activities, or to steroids. Assess across settings; refer via GP to CAMHS or paediatrics for diagnostic assessment if indicated. Medication decisions are medical."},
  {"name": "AUTISM",
   "rate": "elevated in DMD — rate not stated here, check (Ricotti et al., 2016)",
   "presents": "social-communication differences and rigidity that are overlooked because the physical diagnosis dominates. Diagnostic overshadowing is the risk; refer to the CDNT for autism assessment if the profile fits."},
  {"name": "INTELLECTUAL DISABILITY",
   "rate": "a minority of boys with DMD; more likely with some mutation locations (Ricotti et al., 2016) — rate not stated here, check",
   "presents": "global learning difficulty across subjects and in everyday adaptive skills. Adaptive measures must separate what he cannot physically do from what he does not yet know how to do."},
  {"name": "ANXIETY, LOW MOOD AND ADJUSTMENT",
   "rate": "elevated — rate not stated here, check (Colvin et al., 2018)",
   "presents": "worry about falls, hospital, or the future; withdrawal as friends' play becomes more physical; irritability that may be partly steroid-related. Often peaks at loss of walking, at post-primary transition and in adolescence. Ask; refer to CAMHS or the neuromuscular team psychology service if needs meet thresholds."},
  {"name": "FATIGUE AND SLEEP DIFFICULTY",
   "rate": "common — rate not stated here, check",
   "presents": "declining stamina across the day and week, poor sleep, morning headaches or daytime sleepiness (which can signal night-time breathing problems in DMD — medical review). In myotonic dystrophy daytime sleepiness is a feature of the condition."},
 ],

 "recommendations": [
  "FIND OUT WHICH TYPE AND WHAT HAS BEEN SHARED. Before writing anything, establish the type, the current stage, current treatment, and what the child and siblings have been told. Write this into your notes, not your report, unless the family agrees.",
  "ASSESS LEARNING IN ITS OWN RIGHT (DMD): cognitive, language and literacy assessment early in primary, not only when he is 'falling behind'. Choose tasks that do not depend on motor speed or dexterity, and state in the report which scores are affected by motor demands (e.g. timed or manipulative subtests) and were interpreted with caution.",
  "REDUCE VERBAL WORKING MEMORY LOAD: one instruction at a time, written or visual task steps, key vocabulary pre-taught, checking understanding by demonstration. This matches the DMD profile (Hinton et al., 2000) and helps every child in the room.",
  "PLAN FOR ENERGY, NOT JUST ACCESS: rest breaks, reduced handwriting (typing, speech-to-text, scribe as needs change), reduced copying, two sets of books to avoid carrying, heavier cognitive work earlier in the day. Review as stamina changes — a plan written at 7 will be wrong by 10.",
  "PLAN FOR CHANGE AHEAD OF TIME: anticipate transitions such as starting to use a wheelchair, post-primary transfer and building access. Work with the family, OT, physiotherapist and SENO so the environment is ready BEFORE it is needed. Check current NCSE and Department of Education arrangements for SNA support (care needs), assistive technology and building adaptations — they change.",
  "PARTICIPATION AND BELONGING: adapted PE and yard play designed with the physiotherapist; roles in teams and clubs; sustained friendships as play becomes less physical. Protect social time — it is often the first thing sacrificed to therapy and rest.",
  "EMOTIONAL WELLBEING: a named trusted adult; space to talk about what is changing if and when he wants to; staff briefed on how the family talks about the condition. Refer to CAMHS or the neuromuscular team psychology service where anxiety or low mood meet thresholds.",
  "STATE EXAMS: gather evidence early for RACE (reader, scribe or word processor, rest breaks, separate centre etc. — check current SEC categories and criteria each year).",
  "CONTINUUM LEVEL: usually School Support Plus, because several outside services are involved and needs change. Name the level and why.",
  "REFER: CDNT (physiotherapy, OT, psychology, SLT) if not already involved; GP / paediatric neurology for any new medical concern; CAMHS if mental health needs meet thresholds; SENO for SNA, transport and placement; Muscular Dystrophy Ireland for family and youth support. DO NOT comment on prognosis, treatment or medication, and do not raise end-of-life questions with a child or family unless they lead.",
 ],

 "explain_parent": [
  "'Duchenne affects how muscles work, and the same gene is also active in the brain. That's why some boys with Duchenne find reading, remembering a list of spoken instructions or concentrating harder. It isn't caused by being tired or missing school, and it isn't something he's doing wrong.'",
  "'The learning side doesn't get worse the way the muscles do. What he learns, he keeps. So it's worth putting real effort into reading and maths now.'",
  "'Some things will change over the next few years — how far he can walk, how much writing he can do. We want the school to plan for those changes a term ahead, so he never has to struggle before help arrives.'",
  "'You know best what he knows about his condition and what his brothers and sisters have been told. Tell me what words you use, and I'll make sure the school uses the same ones.'",
  "'You don't have to have every conversation with the school yourself. If you'd like, I can help set up one meeting where the key people hear the plan together.'",
  "SIGNPOST: Muscular Dystrophy Ireland (family support, youth service, information — mdi.ie); the CDNT key worker; the neuromuscular team at Children's Health Ireland; the SENO for school supports; LauraLynn Ireland's Children's Hospice and HSE children's palliative care services if and when the family's medical team raises them (check current services).",
 ],

 "explain_teacher": [
  "'Think energy, not ability, for the physical side: he may manage the first hour brilliantly and be spent by lunchtime. Put the demanding thinking early and plan rest into the day.'",
  "'Think working memory for the learning side: give one instruction at a time, write the steps down, and ask him to show you rather than tell you he understood.'",
  "'Assess his reading and maths properly. Boys with Duchenne have higher rates of reading difficulty, and it's easy to blame it on appointments. Structured literacy intervention works for him the same as anyone.'",
  "'Keep expectations high. Adjust how he gets there, not where he's going.'",
  "'Follow the family's words. If they haven't used a word like \"wheelchair\" or talked about the future with him, don't be the one to introduce it. If he asks you something you can't answer, say \"That's a really good question — let's ask Mam and Dad together.\"'",
  "'Plan PE and yard with the physiotherapist so he's included in a real role, not sitting on the bench.'",
 ],

 "explain_child": [
  "YOUNGER (6–9), using the family's words: 'Your muscles get tired more quickly than other people's, so we're going to make some things easier — like typing instead of writing lots, and having rests.'",
  "YOUNGER, ABOUT LEARNING: 'Some children have muscles that work differently and also find it tricky to remember a long list of instructions. That's not your fault and it's not because you're not clever. We'll write things down so your brain can concentrate on the thinking.'",
  "OLDER (10+): 'What's making school harder at the moment — the tiredness, the getting around, the work, or other people? What do you want the teachers to know, and what do you not want them to know?'",
  "OLDER, CONTROL: give him real choices about how supports are introduced — who knows, what equipment he uses in front of peers, and when. Choice matters more as physical control reduces.",
  "IF HE ASKS ABOUT THE FUTURE OR DYING: do not answer beyond what the family has shared. 'That's a big question and a really important one. Who do you like to talk to about things like that? Would you like me to help you ask Mam or Dad, or your doctor?' Tell the family the same day and bring it to supervision.",
  "QUESTIONS TO ASK: 'What's the best part of your day?' 'When do you feel most tired?' 'What would make lunchtime better?' 'Is there anything you've stopped doing that you'd like to do again, a different way?'",
 ],

 "analogies": [
  "THE PHONE BATTERY: 'He starts the day at 100% like everyone else, but his battery drains faster and doesn't fully recharge at break. Plan the day so the important apps run while the battery is high.' Good with teachers and SNAs.",
  "TWO SEPARATE STORIES: 'There's a muscle story and a learning story. They come from the same gene, but they go at different speeds — the muscle story changes over time; the learning story is more like a learning difference that stays the same shape.' Good with parents who fear cognitive decline.",
  "THE NOTEPAD: 'Some of us hold a phone number in our heads; he needs to write it down. Give him the notepad — written steps — and his thinking is as good as anyone's.' Good for verbal working memory.",
  "PLANNING A JOURNEY: 'We know the road has hills ahead, so we pack for them before we reach them.' Good for explaining anticipatory planning to a school without naming milestones in front of the child.",
  "CAUTION: avoid battle or 'fighter' metaphors and 'brave' language unless the family uses them; many young people find them burdensome. Avoid any image of decline applied to learning.",
 ],

 "language": [
  "Use the specific name the family and medical team use ('Duchenne', 'DMD', 'Becker', 'myotonic dystrophy'). 'Muscular dystrophy' alone is imprecise.",
  "Person-first or identity-first: ask the young person. Many say 'I have Duchenne'. Avoid 'suffers from', 'wheelchair-bound' or 'confined to a wheelchair' — say 'uses a wheelchair'.",
  "Say 'loss of walking' or 'no longer walking independently' only when the family uses those terms; in school records use functional descriptions ('uses a powered wheelchair for all mobility').",
  "Around the future, use the family's language. Some families speak openly about life-limiting illness; others do not use the phrase at all. 'Life-limiting' is the term used in children's palliative care — never introduce it yourself.",
  "Describe the learning profile as part of the condition ('the learning profile associated with Duchenne'), not as a separate deficit or as a reaction to disability.",
 ],

 "red_flags": [
  "RED FLAG — sudden change: new breathlessness, chest pain, fainting, morning headaches with daytime sleepiness, or a fall with injury. Medical — tell the family the same day and advise contact with the GP or the medical team; follow the school's care plan and emergency procedures.",
  "RED FLAG — low mood with hopelessness, talk of not wanting to be alive, or self-harm. Same-day risk route: ask directly, do not leave the young person alone if at immediate risk, contact parents, follow NEPS and service risk procedures, and refer urgently (CAMHS / GP / emergency services as needed). Supervision follows action, never replaces it.",
  "RED FLAG — signs of abuse or neglect, including missed essential medical care. Disabled children are at higher risk of abuse and may be less able to disclose. A mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty. Act first; supervision follows.",
  "BOUNDARY — you do not diagnose, give prognosis, or advise on steroids, exon-skipping or other treatment (PSI 2.2.2). You describe learning and wellbeing, plan, and refer.",
  "BOUNDARY — end-of-life and palliative conversations belong to the family and the medical / palliative team. The EP supports the school to respond well, and supports the school community after a death through the NEPS critical incident approach (check current NEPS guidance).",
  "WATCH — learning difficulties attributed to the physical condition or absence and never assessed. Diagnostic overshadowing costs literacy years.",
  "WATCH — staff grief and anxiety. Teachers and SNAs who have known a child for years may be struggling; this affects how they respond. Name it and signpost support (e.g. the school's Employee Assistance Service — check).",
 ],

 "child_voice": [
  "TALKING MATS — good because the young person can sort 'what's going well / not sure / not going well' across school topics without sustained verbal explanation, and it separates having a view from being able to say it. → https://www.talkingmats.com/",
  "'A DAY IN MY LIFE' ENERGY MAPPING — the young person rates energy and enjoyment hour by hour across a school day. Good because it gives you the fatigue data teachers need, in his own words, and shows where to move demanding work.",
  "PERSONAL CONSTRUCT / 'IDEAL SELF' DRAWING (Moran, 2001) — good for older children; lets him describe the pupil he wants to be and the school he wants, which keeps the focus on hopes rather than loss. Adapt for fine motor limits (you draw, he directs).",
  "ONE-PAGE PROFILE WRITTEN WITH HIM — what people like about me, what's important to me, how best to support me. Good because it travels to new teachers and SNAs and gives him control over what is shared.",
  "YOUTH SERVICE AND PEER CONTACT — Muscular Dystrophy Ireland's youth service offers contact with young people with neuromuscular conditions (check current programmes). Good because peers can say things adults cannot, and it builds identity beyond the diagnosis.",
 ],

 "questions": [
  "Q: 'Will his learning get worse as his muscles get weaker?' — A: 'No. In Duchenne the learning differences are there from early on and don't follow the same path as the muscles. What he learns, he keeps — so it's worth investing in reading and maths now.'",
  "Q: 'Is his reading problem just because he's missed so much school?' — A: 'It might be part of it, but boys with Duchenne have higher rates of reading difficulty as part of the condition itself. Let's assess it properly so we know what to teach.'",
  "Q (from a teacher): 'He asked me if he's going to die. What do I say?' — A: 'You did right to come to me. Don't answer beyond what the family has shared. Acknowledge the question, stay with him, and say you'll help him ask his parents. We tell the parents today, and I'll support you with it.'",
  "Q: 'Should he still do Irish / a full subject load?' — A: 'That depends on his energy and his goals, not the diagnosis. Let's look at his week, what matters most to him, and what the current exemption rules allow — they have specific criteria, so we check them rather than assume.'",
  "Q: 'Is the steroid making him cross?' — A: 'Steroids can affect mood and behaviour in some boys, but that's a question for his medical team. What I can do is help the school keep a simple record of when things are harder, so you have something useful to bring to his next appointment.'",
  "Q: 'Should we tell his class?' — A: 'That's his and your decision. Some families and young people like a short, positive explanation for classmates; some prefer not. If you'd like to, Muscular Dystrophy Ireland may have materials — we can plan it together, and he decides how much is said.'",
  "Q: 'Does he need a special school?' — A: 'Not because of the diagnosis. Most children with muscular dystrophy attend mainstream school. What matters is access, support and what he needs to learn — the SENO can go through options if needs change.'",
 ],

 "supervision": [
  "Bring the question of what the child knows about his condition, and how you will keep your work within what the family has shared.",
  "Ask how your service supports schools where a pupil has a life-limiting condition, and what NEPS critical incident support looks like if a pupil dies.",
  "Discuss how you chose and adapted cognitive tasks for a child with motor weakness, and how you reported the adaptation.",
  "Bring your own reaction. Work with progressive and life-limiting conditions is emotionally demanding; supervision is where you notice whether it is shaping your judgement (e.g. lowering expectations out of sympathy).",
  "Ask about the local routes to the CDNT, the neuromuscular service and children's palliative care, and who coordinates when several services are involved.",
 ],

 "reflection": [
  "ON THE PROFILE — Did I assess learning in its own right, or did I accept 'missed school' and 'tiredness' as the explanation?",
  "ON EXPECTATIONS — Did I adjust access while keeping expectations high, or did sympathy lower what I asked of him and the school?",
  "ON WHAT IS SHARED — Did I check what the child and siblings know before I spoke? Did anything I wrote risk telling the child more than the family chose to?",
  "ON ANTICIPATION — Did my plan look a term or a year ahead, or only at today?",
  "ON MY OWN FEELINGS — How did working with a progressive condition affect me? Where did I notice it in my language or decisions?",
  "WHAT GOOD LOOKS LIKE: 'I separated the muscle story from the learning story, assessed his reading and working memory, and planned typing and rest breaks for next year before he needed them. The family's words were used throughout.'",
  "WHAT POOR LOOKS LIKE: 'Pupil has muscular dystrophy; academic difficulties expected to increase as condition progresses. Reduce workload.' — a factual error about cognition, a lowered ceiling and no plan.",
 ],

 "citations": [
  "Banihani, R., Smile, S., Yoon, G., Dupuis, A., Mosleh, M., Snider, A., & McAdam, L. (2015). Cognitive and neurobehavioral profile in boys with Duchenne muscular dystrophy. Journal of Child Neurology, 30(11), 1472–1482. https://doi.org/10.1177/0883073815570154",
  "Birnkrant, D. J., Bushby, K., Bann, C. M., Apkon, S. D., Blackwell, A., Brumbaugh, D., Case, L. E., Clemens, P. R., Hadjiyannakis, S., Pandya, S., Street, N., Tomezsko, J., Wagner, K. R., Ward, L. M., & Weber, D. R. (2018a). Diagnosis and management of Duchenne muscular dystrophy, part 1. The Lancet Neurology, 17(3), 251–267.",
  "Birnkrant, D. J., Bushby, K., Bann, C. M., Alman, B. A., Apkon, S. D., Blackwell, A., Case, L. E., Cripe, L., Hadjiyannakis, S., Olson, A. K., Sheehan, D. W., Bolen, J., Weber, D. R., & Ward, L. M. (2018b). Diagnosis and management of Duchenne muscular dystrophy, part 3: Primary care, emergency management, psychosocial care, and transitions of care across the lifespan. The Lancet Neurology, 17(5), 445–455.",
  "Colvin, M. K., Poysky, J., Kinnett, K., Damiani, M., Gibbons, M., Hoskin, J., Moreland, S., Trout, C. J., & Weidner, N. (2018). Psychosocial management of the patient with Duchenne muscular dystrophy. Pediatrics, 142(Suppl. 2), S99–S109. (Check details.)",
  "Cotton, S., Voudouris, N. J., & Greenwood, K. M. (2001). Intelligence and Duchenne muscular dystrophy: Full-scale, verbal, and performance intelligence quotients. Developmental Medicine & Child Neurology, 43(7), 497–501.",
  "Hinton, V. J., De Vivo, D. C., Nereo, N. E., Goldstein, E., & Stern, Y. (2000). Poor verbal working memory across intellectual level in boys with Duchenne dystrophy. Neurology, 54(11), 2127–2132.",
  "Mendell, J. R., Shilling, C., Leslie, N. D., Flanigan, K. M., al-Dahhak, R., Gastier-Foster, J., et al. (2012). Evidence-based path to newborn screening for Duchenne muscular dystrophy. Annals of Neurology, 71(3), 304–313. (Check details.)",
  "Mercuri, E., Bönnemann, C. G., & Muntoni, F. (2019). Muscular dystrophies. The Lancet, 394(10213), 2025–2038.",
  "Ricotti, V., Mandy, W. P. L., Scoto, M., Pane, M., Deconinck, N., Messina, S., Mercuri, E., Skuse, D. H., & Muntoni, F. (2016). Neurodevelopmental, emotional, and behavioural problems in Duchenne muscular dystrophy in relation to underlying dystrophin gene mutations. Developmental Medicine & Child Neurology, 58(1), 77–84.",
  "Muscular Dystrophy Ireland. (n.d.). About us; Our services; Youth service. https://www.mdi.ie (Retrieved 27/09/2026 — check for updates.)",
 ],

 "pathway": {
  "age": "DMD: signs usually appear in the pre-school years (late walking, falls, difficulty with stairs and running, Gowers' manoeuvre) and diagnosis is commonly made in the early years, often after a delay from first parental concern (Birnkrant et al., 2018a — check timings). Other types range from birth (congenital forms) to adolescence or adulthood. Learning concerns in DMD are often raised in junior classes but attributed to the physical condition.",
  "who_diagnoses": "Ireland: paediatrician and paediatric neurology / the national paediatric neuromuscular service (Children's Health Ireland — check current service location), with genetic testing to confirm the type and mutation. A raised creatine kinase blood test is often the first clue in DMD. The EP does not diagnose. Autism, ADHD or ID assessment for a boy with DMD follows the ordinary CDNT / CAMHS routes.",
  "who_wrote_report": "Neurology or neuromuscular clinic letter; genetics report; CDNT physiotherapy, OT and psychology reports; possibly a neuropsychology report from the hospital; Assessment of Need report and Service Statement (Disability Act 2005). Letters may say little about learning — ask specifically.",
  "refer_to": "CDNT for physiotherapy, OT, SLT and psychology if not already involved; GP / neuromuscular team for any new medical concern; CAMHS where mental health needs meet thresholds; SENO for SNA, transport and placement; Muscular Dystrophy Ireland for family and youth support; children's palliative care only via the medical team; Tusla for any child protection concern.",
  "sooner": "'You noticed something was different and you kept asking — that's how he was diagnosed. Many families wait a long time for a diagnosis because the early signs look like ordinary clumsiness. What matters now is planning ahead, and you're doing that.'",
 },

 "differential": [
  "WHICH TYPE? — Duchenne vs Becker vs myotonic vs other dystrophies: medical and genetic question, but it changes the learning profile you should expect.",
  "DCD / DEVELOPMENTAL MOTOR DELAY — clumsiness and falls WITHOUT progressive weakness; a child who is getting weaker, or who uses Gowers' manoeuvre, needs medical review, not a DCD referral.",
  "OTHER NEUROMUSCULAR CONDITIONS — spinal muscular atrophy, congenital myopathies, hereditary neuropathies; medical diagnosis.",
  "LEARNING DIFFICULTY ATTRIBUTED TO ABSENCE OR FATIGUE — assess learning directly before accepting either explanation.",
  "LOW MOOD / ADJUSTMENT vs STEROID EFFECTS vs SLEEP-DISORDERED BREATHING — each can look like withdrawal or irritability; the medical questions go to the medical team.",
 ],

 "next": [
  "Establish the type, current stage, treatment and what the child knows — with consent.",
  "Assess learning, language, literacy and attention directly, adapting for motor demands and recording the adaptation.",
  "Build a plan for energy, access and participation, and a term-ahead plan for foreseeable changes.",
  "Liaise with the CDNT, neuromuscular team and SENO; name who coordinates.",
  "Check wellbeing and risk; know the route if the young person raises hopelessness or the future.",
 ],

 "presentations": [
  "Physical disability (non-cerebral palsy)",
  "Fatigue and stamina needs",
  "Chronic illness affecting school",
  "Medication effects on attention and learning",
  "Missed curriculum from hospital admissions",
  "Working memory difficulty",
  "Reading difficulty",
  "Anticipatory grief and bereavement in a school community",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — DMD signs and diagnosis usually emerge in the pre-school years",
   "prevalence": "DMD about 1 in 5,000 male births (Mendell et al., 2012 — check); no Irish figure.",
   "see": "Late walking, frequent falls, difficulty with stairs and running, getting up from the floor using the hands, sometimes speech and language delay. Families are often newly diagnosed and grieving. EP role is usually consultation with pre-school and school about transition, language and early learning; the CDNT and neuromuscular team lead.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Griffiths III", "Preschool Language Scales-5 (PLS-5)", "Vineland-3", "SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — the main band for identifying the DMD learning profile and planning access",
   "prevalence": "Elevated rates of reading difficulty, ADHD, autism and ID in DMD (Ricotti et al., 2016) — rates not stated here, check.",
   "see": "A boy who is still walking but tiring, falling more and sitting out of PE; weak verbal working memory and slower reading that are blamed on absence. Friendships shift as play becomes more physical. Towards the end of primary, many boys with DMD move to wheelchair use for longer distances — plan post-primary transfer and access early.",
   "tools": ["WISC-V UK", "WIAT-III UK", "Phonological Assessment Battery (PhAB2)", "CELF-5 UK", "BRIEF-2", "Conners-4", "SDQ", "ABAS-3"],
  },
  "Adolescent": {
   "applies": "YES — loss of walking, adolescence and post-primary demands often coincide",
   "prevalence": "No band-specific figure — check.",
   "see": "Wheelchair use, reduced arm function affecting writing, fatigue, possible respiratory and cardiac care, and the ordinary adolescent wish for privacy and independence. Anxiety and low mood can rise; peer exclusion from social life is common. Plan RACE, typing or speech-to-text, subject load and a future-oriented transition plan.",
   "tools": ["WISC-V UK", "WIAT-III UK", "Access arrangements evidence (RACE)", "BRIEF-2 self-report", "RCADS self-report", "Beck Youth Inventories-2", "ABAS-3"],
  },
  "Young Adult": {
   "applies": "YES — increasingly, as survival into adulthood is now usual in DMD",
   "prevalence": "No band-specific figure — check.",
   "see": "Transition from paediatric to adult neuromuscular care, further education or training, personal assistance and independent living. The EP contribution is transition planning, accommodations evidence and signposting to disability support in further and higher education (e.g. DARE and college disability services — check current schemes).",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — most children with muscular dystrophy attend mainstream; some with ID or complex needs attend special classes or schools",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A child with DMD and intellectual disability or autism, or with a congenital muscular dystrophy or congenital myotonic dystrophy and complex needs. Adaptive assessment must separate motor limitation from learning; communication access and care planning (nursing, hoists, positioning) sit alongside the curriculum. Staff may need support with anticipatory grief.",
   "tools": ["Vineland-3 / ABAS-3", "Adaptive measure in place of IQ", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 2. ACQUIRED BRAIN INJURY
# =====================================================================================
{
 "name": "Acquired brain injury",
 "code": "Medical, not a DSM-5-TR diagnosis in itself · no single code: coded by cause (e.g. ICD-11 Chapter 22 intracranial injury for traumatic brain injury; stroke, tumour, encephalitis, meningitis and hypoxic injury coded separately) — check before quoting · DSM-5-TR Mild / Major Neurocognitive Disorder due to Traumatic Brain Injury exists but is rarely used for school-age children — check",
 "neps": NEPS_MED + " — and 1. LEARNING (1.1 Attention, concentration and work skills) · 2. BEHAVIOUR / 3. EMOTIONAL where post-injury changes in behaviour or mood are the referral",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Disability Act 2005 (Assessment of Need) · EPSEN Act 2004 · Equal Status Acts 2000–2018 · Children First Act 2015 (non-accidental injury) · GDPR (special category health data)",

 "what_it_is": [
  "An injury to the brain that happens AFTER birth and is not hereditary, congenital or degenerative. Two broad groups: TRAUMATIC brain injury (TBI) — falls, road traffic collisions, sport and play, assaults, and non-accidental head injury in infants; and NON-TRAUMATIC injury — stroke, brain tumour and its treatment, encephalitis, meningitis, hypoxia (e.g. near-drowning, cardiac arrest), and some metabolic or toxic events (Acquired Brain Injury Ireland, n.d.; Anderson et al., 2011).",
  "SEVERITY RANGES from concussion (mild TBI) to severe injury with prolonged coma. Medical severity (e.g. Glasgow Coma Scale, length of post-traumatic amnesia, imaging) predicts outcome at group level but poorly for an individual child. Your job is to describe the child's functioning now, and how it changes.",
  "COMMON CONSEQUENCES: fatigue (often the most disabling and least visible), slowed processing speed, attention difficulty, difficulty with new learning and memory, executive function difficulty (planning, organisation, initiation, flexibility, self-monitoring), changes in social cognition, irritability, emotional lability, headaches and sensory sensitivity (Anderson et al., 2011; Ylvisaker et al., 2005). Old knowledge and skills are often better preserved than the capacity to learn new ones — so the child can 'seem fine'.",
  "THE 'HIDDEN DISABILITY' PROBLEM: after a visible recovery (walking, talking, back in class), difficulties in fatigue, speed and executive function are easily misread as laziness, defiance or emotional reaction. Many children with ABI are never identified to the school as having one.",
  "GROWING INTO DEFICIT: the developing brain is not simply 'more plastic'. Younger age at injury and greater severity are associated with poorer outcomes in many studies (Anderson et al., 2005; Anderson et al., 2011), and skills that should mature LATER — especially executive function and abstract reasoning — may show difficulty only years after the injury, when the curriculum demands them.",
  "CHANGE OVER TIME: recovery is often fastest in the first months and continues more slowly after; new difficulties can emerge at transitions. Assessment is therefore repeated: an early baseline, then reassessment (commonly suggested at 6–12 months and at key transitions — check local neuropsychology practice), rather than a one-off verdict.",
  "CONCUSSION is a mild TBI. Most children and adolescents recover within about four weeks; persisting symptoms beyond that warrant medical review (Patricios et al., 2023, Amsterdam consensus). The consensus recommends a brief period of relative rest (about 24–48 hours) followed by a GRADUAL, symptom-guided RETURN TO LEARN, with return to school prioritised before full return to sport (Patricios et al., 2023 — check current version).",
  "IRISH CONTEXT: acute care in Children's Health Ireland hospitals; specialist inpatient and family-centred rehabilitation through the National Rehabilitation Hospital paediatric programme; community therapy through the CDNT or Primary Care; family and school support and training from Acquired Brain Injury Ireland (ABI Ireland, n.d.). Specialist paediatric rehabilitation capacity in Ireland is limited and waits can be long (Children's Health Ireland et al., 2023 — check), so schools often carry more than they should.",
 ],

 "what_it_is_not": [
  "NOT 'the young brain bounces back'. The Kennard principle of greater plasticity in the young brain is not supported as a general rule; early and severe injuries often have worse long-term outcomes (Anderson et al., 2011).",
  "NOT over when the child looks well. Walking and talking normally does not mean fatigue, processing speed or executive skills have recovered. Ask about these specifically.",
  "NOT a developmental disorder. Onset after a period of typical development matters: a post-injury attention or learning difficulty is described as ABI-related, not as newly 'discovered' ADHD or dyslexia — although pre-existing conditions can co-exist and must be identified from pre-injury records.",
  "NOT captured by a single IQ score. A child can score in the average range on a structured one-to-one test and struggle badly in a noisy, fast, unstructured classroom. The test environment compensates for exactly the executive skills that are impaired (Ylvisaker et al., 2005).",
  "NOT defiance or laziness. Irritability, disinhibition, inflexibility and low initiation are recognised consequences of injury to frontal systems. Behaviour plans built on reward and sanction alone often fail; environmental support and routine work better (Ylvisaker et al., 2007).",
  "NOT 'rest in a dark room until all symptoms go' for concussion. Current consensus favours brief relative rest then gradual return to activity and learning (Patricios et al., 2023).",
  "NOT something the EP diagnoses. Medical teams diagnose ABI; paediatric neuropsychologists assess its cognitive effects in depth. The EP describes functioning in school, plans the return and monitors change (PSI 2.2.2).",
 ],

 "prevalence": [
  "OVERALL: traumatic brain injury is a leading cause of acquired disability in childhood internationally; incidence figures vary widely with definition (especially of mild TBI) and setting — figure not stated here, check before quoting.",
  "IRELAND: no national paediatric ABI register. The 2023 strategic direction paper estimates about 450 children a year sustain a moderate-to-severe TBI in Ireland (Children's Health Ireland et al., 2023 — an estimate; check before quoting).",
  "CONCUSSION: very common in childhood and adolescent sport and play; most cases are never seen in hospital, so hospital figures under-count — rate not stated here, check.",
  "SEX RATIO: TBI is more common in boys in most studies, especially in adolescence — ratio not stated here, check.",
  "AGE PEAKS: infants and toddlers (falls; non-accidental injury) and adolescents (sport, road traffic, assault) are described as higher-risk groups in the literature — check figures before quoting.",
  "NON-TRAUMATIC ABI: brain tumour, stroke and encephalitis are individually rare in childhood — rates not stated here, check.",
 ],

 "cooccurring": [
  {"name": "ATTENTION DIFFICULTY (including 'secondary ADHD')",
   "rate": "common after moderate–severe TBI — rate not stated here, check",
   "presents": "distractibility, slowness and impulsivity that are new since the injury. Check pre-injury school reports to separate new from pre-existing difficulty; medical review via the treating team rather than a fresh ADHD referral in isolation."},
  {"name": "FATIGUE AND SLEEP DISTURBANCE",
   "rate": "very common — rate not stated here, check",
   "presents": "a child who manages mornings and falls apart after lunch, headaches later in the day, irritability when tired, and a 'boom-and-bust' pattern after a good day. Plan the timetable around energy."},
  {"name": "EXECUTIVE FUNCTION DIFFICULTY",
   "rate": "common, and may emerge years later ('growing into deficit') — rate not stated here",
   "presents": "trouble starting work, planning multi-step tasks, switching, and monitoring errors; often most visible at post-primary transfer, when organisational demands jump."},
  {"name": "ANXIETY, LOW MOOD AND POST-TRAUMATIC STRESS",
   "rate": "elevated — rate not stated here, check",
   "presents": "fear of re-injury, avoidance of the place or activity, nightmares, grief for the 'old me', and loss of friendships. Assess mood directly; refer to CAMHS or the rehabilitation team psychology service where needs meet thresholds."},
  {"name": "SOCIAL COMMUNICATION AND PEER DIFFICULTY",
   "rate": "common after moderate–severe injury — rate not stated here",
   "presents": "misreading social cues, talking too much or off-topic, disinhibited comments; friends drift away. SLT (pragmatics) and structured social support help."},
  {"name": "EPILEPSY (post-traumatic or with the underlying cause)",
   "rate": "elevated after moderate–severe injury — rate not stated here, check",
   "presents": "absences mistaken for inattention, post-seizure fatigue, medication effects. Medical — know the seizure care plan."},
  {"name": "PRE-EXISTING NEURODEVELOPMENTAL CONDITIONS",
   "rate": "ADHD and similar conditions are over-represented among children who sustain injuries — rate not stated here, check",
   "presents": "difficulties that were there before the injury. Pre-injury school reports and standardised test results are the evidence; without them the injury may be blamed for everything, or for nothing."},
 ],

 "recommendations": [
  "GET PRE-INJURY INFORMATION: standardised test results, school reports and teacher recollection from before the injury are your baseline. Write them into the report — they are the only way to describe change.",
  "PLAN THE RETURN BEFORE IT HAPPENS: a meeting (hospital or rehabilitation team, family, school, EP) before or at return; a graded timetable (e.g. starting with part-days and building up — pace agreed with the treating team); a named key person; a quiet rest space; a simple daily communication record between home and school. Hospital-school liaison varies — check local arrangements.",
  "CONCUSSION — RETURN TO LEARN: follow the medical advice and a stepwise plan: short periods of cognitive activity at home → part-days with adjustments (breaks, reduced screen time, no tests, reduced homework) → full days with adjustments → full return. Advance a step only if symptoms are not substantially worsened; return to school comes before full return to contact sport (Patricios et al., 2023 — check current version). If symptoms persist beyond about four weeks, advise medical review.",
  "MANAGE FATIGUE AND SPEED: scheduled breaks before fatigue hits, demanding work early, reduced volume of written output, extra time, notes provided rather than copied, one task at a time.",
  "SUPPORT EXECUTIVE FUNCTION EXTERNALLY: visual timetables, checklists, written instructions, a homework planner checked by an adult, predictable routines, advance warning of change. Teach strategies explicitly and practise them in context (Ylvisaker et al., 2005).",
  "BEHAVIOUR: use antecedent-focused, positive behaviour support — routine, choice, errorless learning, reduced demands when fatigued — rather than consequence-only systems (Ylvisaker et al., 2007).",
  "MONITOR AND REASSESS: set review dates (e.g. end of each term in the first year) and a formal reassessment, commonly at around 6–12 months and before each transition — check with the treating neuropsychologist. Record what changes.",
  "CONTINUUM LEVEL: School Support Plus for moderate–severe ABI (outside services involved, needs changing); concussion usually needs a time-limited Classroom Support or School Support plan. Name the level and why.",
  "REFER: back to the treating medical / rehabilitation team for new or worsening symptoms; paediatric neuropsychology (via the treating team — access varies, check) for detailed cognitive assessment; CDNT or Primary Care for therapy; CAMHS where mental health needs meet thresholds; SENO for SNA, transport or placement; home tuition scheme during prolonged absence — check current Department of Education criteria; Acquired Brain Injury Ireland for family support and school training.",
  "DO NOT diagnose ADHD, dyslexia or another developmental condition from post-injury difficulties alone; do not interpret a single post-injury score as permanent; do not advise on medication or on return to sport.",
 ],

 "explain_parent": [
  "'The brain injury can affect how quickly he thinks, how long he can concentrate and how tired he gets, even though he looks well. It's common for these \"invisible\" effects to be the biggest problem at school.'",
  "'Things will keep changing, especially over the first year. So we'll make a plan now, check it often, and look again properly in a few months.'",
  "'Some skills, like planning and organising, develop later in childhood. Sometimes difficulties only show up when school asks for those skills. That's why we'll keep an eye on things at secondary school too — not because we expect problems, but so we're ready.'",
  "'Tell us about what he was like before — school reports, test results, what his teachers said. That helps us see what has changed.'",
  "'If he's irritable or exhausted after school, that's usually the injury and the effort he's putting in, not bad behaviour. Let's plan the day so he has something left for home.'",
  "SIGNPOST: Acquired Brain Injury Ireland (parent and carer programmes, school training — abiireland.ie); the treating team or rehabilitation service; the CDNT key worker; the SENO; Brain Tumour Ireland where relevant (check current services).",
 ],

 "explain_teacher": [
  "'He may look completely fine. Watch for fatigue, slowness and losing track rather than for obvious problems.'",
  "'Things he knew before the injury may still be there; learning NEW things is often harder. Revise more, introduce less at once, and check it stuck the next day.'",
  "'Plan for his energy: short tasks, breaks before he's exhausted, and the hard thinking in the morning. A good morning doesn't mean he can do the whole day.'",
  "'If he's irritable, rigid or impulsive, that may be the injury. Structure, warning of changes and a calm exit route will work better than sanctions.'",
  "'For concussion: follow the return-to-learn steps — shorter days, no tests, less screen work, and tell us if symptoms get worse. School comes back before sport.'",
  "'Keep a short note of what changes week to week. That record is what the medical team and I need.'",
 ],

 "explain_child": [
  "YOUNGER: 'When you hurt your head, your brain got hurt too. Brains heal slowly, like a broken arm, but you can't see it. For a while you might get tired quickly or forget things, and that's not your fault.'",
  "YOUNGER: 'When your head starts to hurt or you feel really tired, you can show the teacher this card and have a rest. That helps your brain get better.'",
  "OLDER: 'Brain injuries often affect energy, speed and organisation more than intelligence. You're not less clever — your brain is working harder to do the same things, so it tires sooner.'",
  "OLDER: 'What's different since the injury? What's harder, what's the same, and what do you miss? What do you want your friends and teachers to know?'",
  "OLDER, CONCUSSION: 'Going back gradually isn't a punishment. If you push through a headache, recovery usually takes longer. Tell someone when symptoms get worse — that's how we know when to step up.'",
  "ASK: 'When in the day do you feel best?' 'What helps when your head hurts?' 'Is anything about school scary now?' 'Who do you go to when things get too much?'",
 ],

 "analogies": [
  "THE BROKEN ARM YOU CAN'T SEE: 'If he'd broken his arm, nobody would ask him to write for an hour. His brain has had an injury and is still healing — you just can't see the cast.' Good with teachers and peers.",
  "THE PHONE BATTERY AND THE APPS: 'Everything he does uses battery, and thinking hard uses a lot. His battery is smaller for now, and it drains faster when lots of apps are open — noise, crowds, lots of instructions.' Good for fatigue and overload.",
  "THE LIBRARY AND THE NEW DELIVERIES: 'The books he already had are mostly still on the shelves. It's the new deliveries that are hard to unpack and shelve.' Good for explaining preserved old knowledge and difficult new learning.",
  "THE ROADWORKS: 'The brain is re-routing traffic around the damaged road. It gets there, but it takes longer and it's more tiring.' Good for processing speed with older students.",
  "CAUTION: avoid 'he'll be back to normal soon' and 'the young brain rewires itself'. Both make promises the evidence does not support (Anderson et al., 2011).",
 ],

 "language": [
  "'Acquired brain injury' (ABI) is the umbrella term used by services in Ireland (e.g. Acquired Brain Injury Ireland); 'traumatic brain injury' and 'concussion' are subtypes. Use the cause the medical team uses.",
  "Prefer 'since the injury' and describe specific changes ('processing is slower than before; fatigue by early afternoon') over 'brain damaged'.",
  "Avoid 'recovered' as a verdict; say 'current functioning' and give the date. Change continues.",
  "Many young people and families describe grief for the 'old me' or 'the child we had before'. Acknowledge it in their words; do not correct it.",
  "For concussion, 'mild' refers to the medical category, not the impact on the child — say so if a family feels dismissed.",
 ],

 "red_flags": [
  "RED FLAG — after a head injury: worsening headache, repeated vomiting, increasing drowsiness, confusion, seizure, weakness, slurred speech, unequal pupils or loss of consciousness. Medical emergency — follow school first aid and emergency procedures and call emergency services.",
  "RED FLAG — unexplained head injury in an infant or young child, inconsistent explanations, or injuries in a non-mobile child. Possible non-accidental injury. Children First: a mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty. Act first; supervision follows.",
  "RED FLAG — hopelessness, suicidal thoughts or self-harm after injury (grief, loss of identity, chronic pain, isolation). Same-day risk route: ask directly, ensure safety, contact parents, follow service risk procedures, urgent referral.",
  "RED FLAG — new symptoms months after an apparently settled recovery (new seizures, worsening headaches, loss of skills) — medical review; in children treated for brain tumour, tell the family to contact the oncology team.",
  "BOUNDARY — you do not diagnose ABI or its severity, advise on medication, or clear a young person to return to sport (PSI 2.2.2). You describe school functioning, plan the return and monitor.",
  "WATCH — ABI never mentioned by the family or school, discovered only in developmental history. Ask about head injuries, meningitis and hospital admissions routinely.",
  "WATCH — risk-taking, disinhibition or vulnerability to exploitation in adolescents after ABI. Plan explicitly for safety.",
 ],

 "child_voice": [
  "'THEN AND NOW' INTERVIEW — ask the young person to compare school before and after the injury: what is harder, the same, easier. Good because it gives you their own account of change and often surfaces grief and identity issues.",
  "ENERGY AND SYMPTOM DIARY (older children) — ratings of tiredness and headache across the day. Good because fatigue is invisible to adults and the young person becomes the expert on their own pacing.",
  "TALKING MATS — good for children whose language, speed or fatigue makes open questions hard; they sort topics visually at their own pace. → https://www.talkingmats.com/",
  "SCALING AND SOLUTION-FOCUSED QUESTIONS — 'On a scale of 1–10, how is school going? What would one point higher look like?' Good because it is short, concrete and future-focused, which suits reduced working memory and low mood.",
  "SIBLING AND PEER VOICE (with consent) — good because friends notice social changes first and siblings often carry hidden worry.",
 ],

 "questions": [
  "Q: 'He's scoring average on the tests now — does that mean he's fine?' — A: 'It's good news, but the test room is quiet, one-to-one and structured — the opposite of a classroom. We also need to know about his energy, speed and organisation in real lessons, and to look again as school demands change.'",
  "Q: 'Young children recover better, don't they?' — A: 'That's a common belief, but research shows it isn't that simple. Some skills that develop later can show difficulties years afterwards. So we plan to keep checking, especially at transitions.'",
  "Q (after concussion): 'Should he stay home until all his symptoms are gone?' — A: 'Current advice is a short period of rest, then a gradual return, with school coming before sport. We'll build up step by step and slow down if symptoms get much worse. His doctor guides the medical side.'",
  "Q: 'Is this ADHD now?' — A: 'Attention problems are common after a brain injury. Whether they're called ADHD is a medical question for his treating team — what I can do is describe exactly what's happening in class and set up supports that help straight away.'",
  "Q: 'Can he play rugby / hurling again?' — A: 'That's a decision for his doctor, not the school or me. Once he's cleared, we'll make sure the school side supports it.'",
  "Q (from a teacher): 'He's so rude since he came back.' — A: 'That may well be the injury — it can affect how people control what they say and manage frustration. Let's look at when it happens; it's often when he's tired or overloaded. Changing the demands usually helps more than consequences.'",
  "Q: 'How long will this last?' — A: 'I can't give you a timeline — nobody honestly can for an individual child. Most change happens in the first year, and some continues after. We'll review regularly so the plan keeps up with him.'",
 ],

 "supervision": [
  "Bring the plan for reassessment: when, by whom, and how you will separate recovery from growing into deficit.",
  "Ask what access your service has to paediatric neuropsychology and rehabilitation teams, and how liaison with the hospital works locally.",
  "Discuss how you will interpret cognitive scores that are inconsistent with classroom functioning, and how you report that.",
  "Bring any unexplained or poorly explained head injury in a young child — after you have taken Children First action.",
  "Discuss the emotional side: families grieving the 'child before', and your own reaction to serious injury in a child.",
 ],

 "reflection": [
  "ON BASELINE — Did I get pre-injury evidence, or did I interpret post-injury scores in a vacuum?",
  "ON THE TEST ROOM — Did I account for how the one-to-one test setting compensated for exactly the executive difficulties the classroom exposes?",
  "ON TIME — Did I describe the child as 'recovered' or 'impaired' as if it were final? Did I build reassessment into the plan?",
  "ON BEHAVIOUR — Did I read post-injury behaviour as choice, or did I look for fatigue, overload and executive factors first?",
  "ON SAFETY — Did I ask how the injury happened, and was I satisfied with the explanation?",
  "WHAT GOOD LOOKS LIKE: 'I gathered his 2nd-class standardised scores and teacher reports, compared them with now, set a graded timetable with the rehabilitation team, and booked a review before post-primary transfer.'",
  "WHAT POOR LOOKS LIKE: 'Cognitive assessment in average range; no further input required.' — six weeks after a severe TBI, with no baseline, no fatigue information and no review.",
 ],

 "citations": [
  "Acquired Brain Injury Ireland. (n.d.). Programme for parents and carers of under 18s; What is acquired brain injury? https://www.abiireland.ie (Retrieved 27/09/2026 — check for updates.)",
  "Anderson, V., Catroppa, C., Morse, S., Haritou, F., & Rosenfeld, J. (2005). Functional plasticity or vulnerability after early brain injury? Pediatrics, 116(6), 1374–1382.",
  "Anderson, V., Spencer-Smith, M., & Wood, A. (2011). Do children really recover better? Neurobehavioural plasticity after early brain insult. Brain, 134(8), 2197–2221.",
  "Children's Health Ireland, National Rehabilitation Hospital, Acquired Brain Injury Ireland, & Brain Tumour Ireland. (2023). Rehabilitation for children and young people in Ireland following acquired brain injury: Current services and potential future directions [Strategic direction paper]. Children's Health Ireland. https://www.childrenshealthireland.ie/ (Title confirmed 27/09/2026; CHI lists the partners as NRH, ABI Ireland, CHI and Brain Tumour Ireland — check author order on the cover.)",
  "Patricios, J. S., Schneider, K. J., Dvorak, J., et al. (2023). Consensus statement on concussion in sport: The 6th International Conference on Concussion in Sport — Amsterdam, October 2022. British Journal of Sports Medicine, 57(11), 695–711. (Check for updates.)",
  "Ylvisaker, M., Adelson, P. D., Braga, L. W., Burnett, S. M., Glang, A., Feeney, T., Moore, W., Rumney, P., & Todis, B. (2005). Rehabilitation and ongoing support after pediatric TBI: Twenty years of progress. Journal of Head Trauma Rehabilitation, 20(1), 95–109.",
  "Ylvisaker, M., Turkstra, L., Coelho, C., Yorkston, K., Kennedy, M., Sohlberg, M. M., & Avery, J. (2007). Behavioural interventions for children and adults with behaviour disorders after TBI: A systematic review of the evidence. Brain Injury, 21(8), 769–805. (Check details.)",
  "Babikian, T., & Asarnow, R. (2009). Neurocognitive outcomes and recovery after pediatric TBI: Meta-analytic review of the literature. Neuropsychology, 23(3), 283–296.",
 ],

 "pathway": {
  "age": "Any age. Infants and toddlers (falls, non-accidental injury) and adolescents (sport, road traffic, assault) are the higher-risk groups for TBI. The school usually learns of a severe ABI at the point of return; mild injury and concussion are often not reported unless asked. Later difficulties may surface at post-primary transfer, when executive demands rise.",
  "who_diagnoses": "Ireland: emergency and acute medical teams (Children's Health Ireland and regional hospitals), neurosurgery, neurology or oncology depending on cause; paediatric rehabilitation (including the National Rehabilitation Hospital paediatric programme) and paediatric neuropsychology describe cognitive consequences. GPs manage many concussions. The EP does not diagnose.",
  "who_wrote_report": "Hospital discharge summary; neurosurgical or neurology letter; rehabilitation team report (physiotherapy, OT, SLT, psychology); paediatric neuropsychology report; oncology letters for tumour survivors; sometimes a CDNT or Primary Care report. Check the date — reports go out of date quickly after ABI.",
  "refer_to": "Treating medical or rehabilitation team for new or worsening symptoms and for neuropsychology; CDNT or Primary Care for community therapy; CAMHS for mental health needs meeting thresholds; SENO for SNA, transport or placement; home tuition scheme during prolonged absence (check criteria); Acquired Brain Injury Ireland for family support and school training; Tusla for any suspicion of non-accidental injury.",
  "sooner": "'Many of the effects of a brain injury only become clear when a child is back in the full school day, or years later as school asks for new skills. Noticing now is exactly when it's useful. What matters is that we plan and keep checking.'",
 },

 "differential": [
  "PRE-EXISTING ADHD, SLD OR DLD — use pre-injury records; both may be present.",
  "POST-TRAUMATIC STRESS, ANXIETY OR LOW MOOD — can mimic cognitive difficulty (poor concentration, memory complaints); assess mood directly.",
  "PERSISTING POST-CONCUSSION SYMPTOMS vs OTHER CAUSES — headache, sleep, mood and vestibular problems; medical review if beyond about four weeks.",
  "EFFECTS OF TREATMENT — medication, cranial radiotherapy or chemotherapy in tumour survivors can have their own late cognitive effects; oncology team.",
  "SEIZURES — absences or post-ictal states mistaken for inattention; medical review.",
 ],

 "next": [
  "Gather pre-injury evidence and the latest medical and rehabilitation reports (with consent).",
  "Plan a graded return with the family, treating team and school; name a key person.",
  "Assess school functioning — fatigue, speed, attention, executive function, mood — not only a cognitive score.",
  "Set review dates and a formal reassessment, especially before transitions.",
  "Check the circumstances of the injury and act on any safeguarding concern.",
 ],

 "presentations": [
  "Re-entry to school after illness",
  "Fatigue and stamina needs",
  "Executive function difficulty",
  "Attention and concentration difficulty",
  "Processing speed difficulty",
  "Working memory difficulty",
  "Emotional regulation difficulty",
  "Missed curriculum from hospital admissions",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — falls and non-accidental injury are important causes at this age; effects may only show later",
   "prevalence": "No Irish figure — check; infants and toddlers are a higher-risk group for TBI.",
   "see": "Irritability, sleep and feeding change, loss of recently acquired skills, delayed language or motor development after injury, meningitis or encephalitis. Effects on skills not yet developed cannot be measured yet. Always consider how the injury happened. Pre-school consultation and a flag for monitoring into school are the EP contribution.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Griffiths III", "Bayley-4", "Vineland-3", "SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — return to school, concussion from play and sport, and later-emerging difficulty",
   "prevalence": "No Irish figure — rate not stated here, check.",
   "see": "A child back in class who looks well but tires by lunchtime, is slow, forgets new material and is more irritable or impulsive than before. Concussion from play or sport needs a return-to-learn plan. Compare with pre-injury standardised scores and teacher reports.",
   "tools": ["WISC-V UK", "WIAT-III UK", "BRIEF-2", "TEA-Ch2", "Conners-4", "SDQ", "ABAS-3", "NEPSY-II — AGE 3–16 · MEASURES: neuropsychological domains (attention/executive, language, memory and learning, sensorimotor, social perception, visuospatial) · CANNOT TELL YOU: classroom functioning or fatigue across a day; usually given by neuropsychology · TIME: variable by subtests selected — check the manual"],
  },
  "Adolescent": {
   "applies": "YES — sport, road traffic and assault peak; executive demands of post-primary expose difficulty",
   "prevalence": "No Irish figure — rate not stated here, check.",
   "see": "Concussion from contact sport; more severe injury from road traffic or assault. Organisation, homework and independent study break down; social changes, disinhibition and risk-taking, low mood and loss of identity. Plan RACE evidence, subject load and a structured return; watch for substance use and exploitation.",
   "tools": ["WISC-V UK", "WIAT-III UK", "BRIEF-2 self-report", "Conners-4 self-report", "RCADS self-report", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — transition to further education, work and adult rehabilitation services",
   "prevalence": "No Irish figure — rate not stated here, check.",
   "see": "Difficulties with independent study, time management and fatigue in further or higher education; employment and driving questions; adult rehabilitation and community services (Acquired Brain Injury Ireland provides adult services — check). EP contribution is transition planning and accommodations evidence.",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — some children with severe ABI move to special classes or schools, sometimes after a period in mainstream",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A child with severe ABI and complex motor, communication and learning needs, sometimes with epilepsy. Staff may not know the child's pre-injury abilities, and families may grieve that loss. Plan with the rehabilitation team; use adaptive and communication assessment; review regularly because change continues.",
   "tools": ["Vineland-3 / ABAS-3", "Adaptive measure in place of IQ", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 3. FOETAL ALCOHOL SPECTRUM DISORDER
# =====================================================================================
{
 "name": "Foetal Alcohol Spectrum Disorder",
 "code": "NOT a DSM-5-TR diagnosis in its own right: DSM-5-TR includes Neurobehavioral Disorder Associated with Prenatal Alcohol Exposure (ND-PAE) in Section III 'Conditions for Further Study'; clinicians may record it as Other Specified Neurodevelopmental Disorder (F88 — check) · ICD-11: fetal alcohol syndrome is listed (code — check before quoting) · Diagnostic framework used in the UK: SIGN 156 (2019) — check for updates",
 "neps": "1. LEARNING (1.3 Comprehension and general ability · 1.1 Attention) — and 2. BEHAVIOUR / 4. SOCIAL where self-regulation and social vulnerability are the referral · " + NEPS_MED,
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Disability Act 2005 (Assessment of Need) · EPSEN Act 2004 · Child Care Act 1991 (children in care) · Children First Act 2015 · Equal Status Acts 2000–2018 · GDPR (special category health data)",

 "what_it_is": [
  "A lifelong NEURODEVELOPMENTAL condition resulting from PRENATAL ALCOHOL EXPOSURE (PAE). Alcohol crosses the placenta and can affect brain development at any stage of pregnancy. The result is a spectrum: some people have characteristic facial features and growth effects; most do not, but have significant difficulties in brain-based functions (SIGN, 2019; Cook et al., 2016).",
  "SIGN 156 (2019) uses the umbrella term FASD with two diagnostic categories: FASD WITH SENTINEL FACIAL FEATURES (short palpebral fissures, smooth philtrum, thin upper lip) and FASD WITHOUT SENTINEL FACIAL FEATURES (which requires CONFIRMED PAE); plus a designation for children 'at risk of neurodevelopmental disorder and FASD, associated with prenatal alcohol exposure' who do not meet criteria (e.g. too young to assess). Both diagnoses require severe impairment in several brain domains — three or more in the Canadian framework SIGN adapted (Cook et al., 2016 — check the domain list and threshold in SIGN 156 before quoting).",
  "BRAIN DOMAINS assessed include motor skills, neuroanatomy/neurophysiology, cognition, language, academic achievement, memory, attention, executive function (including impulse control and hyperactivity), affect regulation, and adaptive behaviour / social skills / social communication (Cook et al., 2016 — check). This is why diagnosis needs a MULTIDISCIPLINARY team: paediatrics, psychology, SLT, OT at minimum.",
  "DSM-5-TR does not list FASD as a disorder. It includes ND-PAE — impairment in neurocognition, self-regulation and adaptive functioning following more than minimal PAE — as a condition for further study; clinicians can record it as Other Specified Neurodevelopmental Disorder (APA, 2022; Kable et al., 2016). You may see either 'FASD' or 'ND-PAE' on a report depending on the clinician's framework.",
  "THE TYPICAL SCHOOL PROFILE: uneven skills (often better expressive language than comprehension, so the child SOUNDS more able than they are); difficulty learning from consequences and generalising; poor working memory; difficulty with abstract concepts (time, money, maths); impulsivity; slow processing; sensory differences; 'good days and bad days' — inconsistent performance that is read as wilful. Many have IQ scores in the typical range yet significant adaptive difficulty (SIGN, 2019; Streissguth et al., 2004).",
  "SECONDARY OUTCOMES are not inevitable. Streissguth et al. (2004) reported high rates of disrupted schooling, trouble with the law and mental health difficulty in adolescents and adults with FASD, and identified PROTECTIVE factors: early diagnosis and a stable, nurturing home. Identification and understanding matter.",
  "IRISH CONTEXT: at the time of writing there is no national HSE diagnostic pathway or statutory guideline for FASD in Ireland (FASD Ireland, n.d.; Dáil debate records — check current position). Children may be assessed privately, through CDNT or CAMHS where a team has the expertise, or abroad. The HSE has a position on FASD prevention. Family support and signposting: FASD Ireland and its FASD Hub Ireland (check current services).",
 ],

 "what_it_is_not": [
  "NOT a judgement on the birth mother. Many pregnancies are unplanned and alcohol is consumed before pregnancy is known; alcohol use is widespread and socially normalised in Ireland; addiction is a health condition. Use neutral language ('prenatal alcohol exposure'), never 'the mother drank'.",
  "NOT only the 'facial features' condition. Most people with FASD do not have sentinel facial features (SIGN, 2019). Absence of the face does not rule it out.",
  "NOT the same as intellectual disability. Many children with FASD have IQ scores in the typical range; the disability is in adaptive functioning, self-regulation, memory and executive function. Services that gate on IQ often exclude them.",
  "NOT 'won't'. Children with FASD often cannot link a rule to a consequence, remember yesterday's lesson, or stop an impulse — even though they can recite the rule. 'Can't, not won't' is the reframe used by FASD practitioners (e.g. Malbin, 2002 — check source).",
  "NOT something the EP can diagnose. Diagnosis requires a specialist multidisciplinary team, confirmation of PAE (or sentinel facial features), physical examination and assessment across brain domains (SIGN, 2019). The EP contributes assessment of cognition, learning and adaptive function, and describes the school profile (PSI 2.2.2).",
  "NOT explained away by trauma or attachment. Many children with FASD are care-experienced and have trauma histories too. Both can be present; trauma-informed approaches alone may not address the brain-based difficulties, and vice versa.",
  "NOT outgrown or cured. It is lifelong, but outcomes improve with understanding, environmental adaptation and stable care (Streissguth et al., 2004).",
 ],

 "prevalence": [
  "GLOBAL: a meta-analysis estimated FASD prevalence in the general population at 7.7 per 1,000, with the highest regional estimate in Europe (Lange et al., 2017 — check figures before quoting).",
  "IRELAND: there is NO Irish population prevalence study cited here. Modelled estimates place Ireland among the highest in the world (Lange et al., 2017, as quoted by FASD Ireland) — these are MODELLED from alcohol use in pregnancy, not measured; say so if you quote them, and check the figure.",
  "ALCOHOL USE IN PREGNANCY: Popova et al. (2017) estimated Ireland among the countries with the highest prevalence of alcohol use during pregnancy — modelled; check the figure before quoting.",
  "CHILDREN IN CARE AND ADOPTED CHILDREN: rates are far higher than in the general population in international studies (Lange et al., 2013 — check figures). Children adopted from countries with high alcohol use are also over-represented. Relevant for any Tusla-involved or adopted child you see.",
  "UNDER-DIAGNOSIS: most people with FASD are thought to be undiagnosed or diagnosed with something else (e.g. ADHD alone) — international literature; proportion not stated here, check.",
  "SEX RATIO: not stated here — check before quoting.",
 ],

 "cooccurring": [
  {"name": "ADHD",
   "rate": "very common in FASD — rate not stated here, check",
   "presents": "inattention, hyperactivity and impulsivity; may be the only diagnosis the child has. Some clinicians consider the ADHD-like profile in FASD to differ (e.g. more difficulty with encoding and shifting) — medication response is a medical matter. Describe, and refer via GP / CAMHS for assessment."},
  {"name": "TRAUMA, ATTACHMENT DIFFICULTY AND CARE EXPERIENCE",
   "rate": "very common overlap — rate not stated here, check",
   "presents": "hypervigilance, relationship difficulty, dysregulation. Separate what fits trauma, what fits a brain-based difficulty, and what fits both. A child can have FASD and RAD or DSED; each needs a different part of the plan."},
  {"name": "LANGUAGE DISORDER (especially comprehension and pragmatics)",
   "rate": "common — rate not stated here, check",
   "presents": "fluent, chatty speech that masks poor understanding; confabulation (filling memory gaps with invented detail) that is taken as lying. SLT assessment of comprehension and social communication."},
  {"name": "INTELLECTUAL DISABILITY OR LEARNING DIFFICULTY (especially maths)",
   "rate": "a minority have ID; specific difficulties common — rate not stated here, check",
   "presents": "difficulty with number, time, money and abstract reasoning; skills 'lost' from one day to the next. Adaptive functioning is often lower than IQ predicts — measure both."},
  {"name": "AUTISM",
   "rate": "elevated — rate not stated here, check",
   "presents": "social-communication difficulty and sensory sensitivities that overlap with FASD. Differential diagnosis is specialist; the child may meet criteria for both."},
  {"name": "ANXIETY, LOW MOOD AND LATER SUBSTANCE USE",
   "rate": "elevated, especially in adolescence (Streissguth et al., 2004) — rate not stated here",
   "presents": "school refusal, withdrawal, self-harm, early alcohol or drug use. Ask directly and non-judgementally; same-day risk route where there is risk."},
  {"name": "SLEEP AND SENSORY DIFFERENCES",
   "rate": "common — rate not stated here, check",
   "presents": "poor sleep, over- or under-reaction to noise, touch and busy environments; afternoons and transitions are worst. OT input; reduce sensory load."},
 ],

 "recommendations": [
  "CHANGE THE ENVIRONMENT, NOT THE CHILD, FIRST. Structure, routine, consistency, repetition, simplicity, supervision and concrete, specific language are the core adaptations described in FASD guidance and training (SIGN, 2019; strategy lists such as the 'Eight Magic Keys' — check source before citing).",
  "TEACH CONCRETELY AND RE-TEACH: hands-on materials, visual supports, the same words every time, and daily re-teaching of routines and rules. Expect skills to come and go; do not treat a 'bad day' as proof the child 'knew it yesterday so is choosing not to'.",
  "SUPERVISION, NOT CONSEQUENCES: unstructured times (yard, corridors, transitions, school trips) need adult oversight. Children with FASD often cannot learn from consequences; replace sanction-based plans with prevention, cueing and co-regulation.",
  "CHECK COMPREHENSION, NOT CONVERSATION: ask the child to show or do, not to say they understand. Break instructions into one step at a time and give them in writing or pictures.",
  "MEASURE ADAPTIVE FUNCTIONING (ABAS-3 / Vineland-3) alongside cognition. The gap between the two is often the most important finding for planning and for services.",
  "COORDINATE WITH CARE TEAMS: for care-experienced children, work with the Tusla social worker and foster or kinship carers; share a single consistent plan across home and school. Recommend trauma-informed AND FASD-informed practice.",
  "PLAN TRANSITIONS EARLY: post-primary transfer (many teachers, rooms, timetables) is a high-risk point; consider a key person, a simplified timetable, a quiet base and graduated induction. Check eligibility for special class or L2LP routes only on assessed need — check NCCA guidance.",
  "CONTINUUM LEVEL: usually School Support Plus (multiple services, complex needs). Name the level and why.",
  "REFER: GP / paediatrics for consideration of FASD assessment (diagnostic pathways vary and may not exist locally — check); CDNT for multidisciplinary needs; CAMHS for mental health needs meeting thresholds; SLT for comprehension and pragmatics; Tusla social worker for children in care; FASD Ireland for family support and signposting.",
  "DO NOT diagnose FASD or state that a child 'has FASD' or 'appears to have FASD' in a report; do not ask about or record maternal drinking without a clear purpose, consent and sensitivity; do not assume PAE from a care history.",
 ],

 "explain_parent": [
  "TO FOSTER, KINSHIP OR ADOPTIVE PARENTS: 'FASD is a brain-based difference caused by alcohol before birth. It means she may not be able to learn from consequences or remember what she knew yesterday — it's not that she won't, it's that her brain works differently. That changes how we support her.'",
  "TO BIRTH PARENTS (if a diagnosis has been made and they are involved): 'Lots of pregnancies aren't planned, and many people drink before they know they're pregnant. What matters now is understanding how her brain works and getting the right support. You coming here today is part of that.'",
  "'Her talking can make her seem more able than she is. So we'll check what she understands by what she does, not what she says.'",
  "'Structure and routine are her best friends. The more the same things happen in the same way at home and at school, the better she'll manage.'",
  "'She'll have good days and bad days. A bad day doesn't mean she's being defiant. It usually means she's tired, overloaded or something changed.'",
  "SIGNPOST: FASD Ireland and FASD Hub Ireland (information and signposting; no diagnosis needed to contact — fasdireland.ie); the Tusla social worker for children in care; the CDNT key worker; the GP for assessment questions; the SENO for school supports.",
 ],

 "explain_teacher": [
  "'Think \"brain-based\", not \"behaviour\". She may know the rule and still not be able to follow it in the moment.'",
  "'Structure, routine, supervision — especially at yard, lining up and transitions. That's where things go wrong.'",
  "'One step at a time, in pictures or writing. Ask her to show you, not tell you, that she understood.'",
  "'Re-teach every day. Forgetting yesterday's lesson is part of the condition, not carelessness.'",
  "'Consequences that happen later (losing Golden Time on Friday) won't work. Prevention and immediate, calm redirection will.'",
  "'If she tells you a story that isn't true, it may be confabulation — filling memory gaps — rather than deliberate lying. Check facts gently; don't label her a liar.'",
 ],

 "explain_child": [
  "YOUNGER: 'Your brain is really good at some things — like [strength]. Some things are tricky, like remembering what to do next or waiting. That's how your brain grew, and it's not your fault. We'll help with pictures and reminders.'",
  "YOUNGER, WHEN IN TROUBLE: 'You're not bad. Your brain finds it hard to stop and think sometimes. Let's work out what would help next time.'",
  "OLDER (only if the young person knows the diagnosis, and in the words the family uses): 'FASD means your brain grew differently before you were born. It isn't anyone's fault that you're dealing with it now, and it isn't about how clever you are. It explains why some things feel harder.'",
  "OLDER, SELF-ADVOCACY: 'What do you want teachers to know about how you learn best? What helps on a bad day? Who do you trust at school?'",
  "DISCLOSURE is a decision for the young person's parents or carers and social worker (and, as they get older, the young person). Never introduce the words 'alcohol' or 'FASD' to a child who has not been told.",
  "QUESTIONS TO ASK: 'What does a good day look like?' 'What makes things go wrong?' 'Which adults help you calm down?' 'What's hard about yard?'",
 ],

 "analogies": [
  "THE FILING CABINET WITH A BROKEN DRAWER: 'She learns it and files it — but sometimes the drawer jams, so she can't find it tomorrow. Re-teaching is putting a copy on the desk.' Good with teachers frustrated by inconsistency.",
  "THE EXTERNAL BRAIN: 'Adults, routines and visual supports act as her external brain — doing the planning and remembering hers finds hard. Take them away and it isn't a test of independence, it's removing a ramp.' Good for explaining supervision needs.",
  "THE FLUENT TOURIST: 'Like someone who has learned to say lots of phrases in a language fluently but only understands part of the reply — she sounds more able than she understands.' Good for the expressive–receptive gap.",
  "TRYING DIFFERENTLY, NOT HARDER: 'Asking her to try harder is like asking someone with short sight to squint harder. Change the conditions instead.' (After Malbin's 'trying differently rather than harder' — check source.) Good with parents and staff.",
  "CAUTION: avoid 'damaged', 'broken' or 'poisoned' imagery about the child's brain. Avoid any analogy that blames the birth mother.",
 ],

 "language": [
  "'Foetal Alcohol Spectrum Disorder' (FASD) is the term used by SIGN (2019) and FASD Ireland; 'fetal' in US spelling. Older terms (FAS, partial FAS, ARND, 'FAE') appear on older reports — note them, and ask the diagnosing team what they now correspond to.",
  "Use 'prenatal alcohol exposure' (PAE), not 'the mother drank' or 'alcohol-damaged child'. Refer to 'birth mother' or 'birth parents' where relevant.",
  "Person-first ('a child with FASD') is common in FASD organisations; some adults prefer identity-first. Ask.",
  "Avoid 'FAS kid', 'damaged', 'bad', 'manipulative', 'liar' — replace with a description of the brain-based difficulty ('memory gaps; may confabulate').",
  "Be careful where the information is recorded: PAE is sensitive health and family information about a third party (the birth mother). Record only what is necessary, with consent and in line with GDPR and service policy.",
 ],

 "red_flags": [
  "RED FLAG — current child protection or welfare concern (e.g. ongoing parental substance misuse affecting care, neglect). Children First: a mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty. Act first; supervision follows.",
  "RED FLAG — self-harm, suicidal talk or hopelessness, especially in adolescence. Same-day risk route: ask directly, ensure safety, contact parents or carers and the social worker, follow service procedures, urgent referral.",
  "RED FLAG — exploitation risk: young people with FASD are highly suggestible and may be drawn into criminal, sexual or financial exploitation. Treat concerns as safeguarding, not behaviour.",
  "RED FLAG — early alcohol or drug use. Ask non-judgementally; refer to local youth substance use services; involve parents or carers and the social worker.",
  "BOUNDARY — you do not diagnose FASD or ND-PAE, confirm PAE, or comment on medication (PSI 2.2.2). You describe functioning, formulate, recommend and refer.",
  "WATCH — a behaviour-only formulation for a care-experienced child with memory, comprehension and adaptive difficulties. Consider whether FASD has been considered by a medical team.",
  "WATCH — exclusions and reduced timetables. Sanction-based responses to brain-based difficulty often escalate; review the plan before the next exclusion.",
 ],

 "child_voice": [
  "VISUAL, CONCRETE METHODS — drawing, photos, scaling with pictures, Talking Mats. Good because abstract questions ('How do you feel about school?') are hard for children with FASD; concrete choices get more reliable answers. → https://www.talkingmats.com/",
  "SHORT, REPEATED CONVERSATIONS rather than one long interview. Good because memory and attention vary day to day; views gathered on several occasions are more reliable.",
  "OBSERVATION ACROSS THE DAY — especially yard and transitions. Good because what the child does in unstructured time tells you more than what they say about it.",
  "ONE-PAGE PROFILE / 'ALL ABOUT ME' built with the child and carers. Good because it gives strengths first and travels to every new adult, reducing re-explaining.",
  "CHECK FOR SUGGESTIBILITY: use open, non-leading questions and avoid yes/no questions; children with FASD may agree with whatever is suggested. Good practice for all voice work, essential here.",
 ],

 "questions": [
  "Q: 'She knows the rules — she can tell you them. So why does she keep breaking them?' — A: 'Knowing a rule and being able to use it in the moment are different brain skills. In FASD, the second one is often the problem. Reminders, supervision and prevention work better than consequences.'",
  "Q: 'Her IQ is average — how can she need so much help?' — A: 'IQ tests measure some skills in a quiet one-to-one setting. Her difficulties are in memory, self-regulation and everyday adaptive skills, which is why we measure those too. The gap is common in FASD.'",
  "Q (from a foster carer): 'Can you diagnose FASD?' — A: 'No — it needs a specialist medical and multidisciplinary team, and confirmation of alcohol exposure. What I can do is assess her learning and everyday skills, which that team would need, and help you ask the GP about a referral.'",
  "Q: 'Isn't this just trauma?' — A: 'Trauma may well be part of it, and we'll plan for that. But some of what we see — memory, maths, understanding language — looks brain-based too. The two often go together, and she needs support for both.'",
  "Q: 'Should we tell the school about the alcohol?' — A: 'The school needs to understand how she learns and what helps, not necessarily the history. With you and her social worker, we can decide what's shared and write the plan around her needs.'",
  "Q: 'Will she grow out of it?' — A: 'FASD is lifelong, but the outlook is much better when the people around her understand it and life is stable and structured. That's exactly what we're building.'",
  "Q (from a teacher): 'She lies all the time.' — A: 'Sometimes children with FASD fill memory gaps with things that seem true to them — it's called confabulation. Check facts gently and avoid accusing; ask \"What happened next?\" rather than \"Did you do it?\"'",
 ],

 "supervision": [
  "Bring any case where FASD might be relevant and discuss whether and how to raise PAE — with whom, with what purpose and with what consent.",
  "Ask what diagnostic routes exist locally (CDNT, CAMHS, paediatrics, private) and what your service's position is on recommending FASD assessment.",
  "Discuss how you are holding trauma, attachment, ADHD and FASD hypotheses together without collapsing into one explanation.",
  "Bring your own reactions — to birth parents, to the child's behaviour, to the system gaps — and check your report language for judgement.",
  "Confirm Children First actions for any current welfare concern before discussing formulation.",
 ],

 "reflection": [
  "ON JUDGEMENT — Did my language, spoken or written, carry any blame towards the birth mother? Would I be comfortable if she read my report?",
  "ON THE PROFILE — Did I measure adaptive functioning and comprehension, or did an average IQ and fluent speech reassure me?",
  "ON COMPETING EXPLANATIONS — Did I hold trauma, attachment, ADHD and FASD together, or did one explanation push out the others?",
  "ON THE PLAN — Did I recommend changing the environment, or did I write another consequence-based behaviour plan?",
  "ON ROLE — Did I stay within describing, formulating and referring, or did I drift towards diagnosis?",
  "WHAT GOOD LOOKS LIKE: 'I measured adaptive functioning alongside cognition, described the gap, wrote a plan built on structure, supervision and re-teaching, and — with the social worker's agreement — recommended a GP referral for FASD consideration without recording unnecessary history.'",
  "WHAT POOR LOOKS LIKE: 'Child presents with probable FASD due to maternal alcohol abuse; behaviour is manipulative. Recommend loss of privileges.' — a diagnosis the EP cannot make, blaming language, and a plan that will not work.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Section III, Conditions for Further Study: Neurobehavioral Disorder Associated with Prenatal Alcohol Exposure.",
  "Cook, J. L., Green, C. R., Lilley, C. M., Anderson, S. M., Baldwin, M. E., Chudley, A. E., Conry, J. L., LeBlanc, N., Loock, C. A., Lutke, J., Mallon, B. F., McFarlane, A. A., Temple, V. K., & Rosales, T. (2016). Fetal alcohol spectrum disorder: A guideline for diagnosis across the lifespan. CMAJ, 188(3), 191–197.",
  "Kable, J. A., O'Connor, M. J., Olson, H. C., Paley, B., Mattson, S. N., Anderson, S. M., & Riley, E. P. (2016). Neurobehavioral disorder associated with prenatal alcohol exposure (ND-PAE): Proposed DSM-5 diagnosis. Child Psychiatry & Human Development, 47(2), 335–346. (Check details.)",
  "Lange, S., Probst, C., Gmel, G., Rehm, J., Burd, L., & Popova, S. (2017). Global prevalence of fetal alcohol spectrum disorder among children and youth: A systematic review and meta-analysis. JAMA Pediatrics, 171(10), 948–956.",
  "Lange, S., Shield, K., Rehm, J., & Popova, S. (2013). Prevalence of fetal alcohol spectrum disorders in child care settings: A meta-analysis. Pediatrics, 132(4), e980–e995.",
  "Popova, S., Lange, S., Probst, C., Gmel, G., & Rehm, J. (2017). Estimation of national, regional, and global prevalence of alcohol use during pregnancy and fetal alcohol syndrome: A systematic review and meta-analysis. The Lancet Global Health, 5(3), e290–e299.",
  "Scottish Intercollegiate Guidelines Network. (2019). Children and young people exposed prenatally to alcohol (SIGN publication no. 156). SIGN. (Check for updates.)",
  "Streissguth, A. P., Bookstein, F. L., Barr, H. M., Sampson, P. D., O'Malley, K., & Young, J. K. (2004). Risk factors for adverse life outcomes in fetal alcohol syndrome and fetal alcohol effects. Journal of Developmental & Behavioral Pediatrics, 25(4), 228–238.",
  "National Institute for Health and Care Excellence. (2022). Fetal alcohol spectrum disorder (Quality standard QS204). NICE. (Check for updates.)",
  "FASD Ireland. (n.d.). FASD Hub Ireland. https://www.fasdireland.ie (Retrieved 27/09/2026 — check for updates.)",
 ],

 "pathway": {
  "age": "Sentinel facial features may be recognised in infancy, but most children are identified — if at all — in primary school, when learning, memory and behaviour difficulties become clear, or in adolescence after school breakdown or contact with justice services. SIGN (2019) allows an 'at risk' designation for young children who cannot yet be fully assessed. Many are never diagnosed.",
  "who_diagnoses": "Ireland: no national HSE diagnostic pathway at the time of writing (check current position). Diagnosis may be made by a paediatrician with a multidisciplinary team (CDNT or CAMHS where expertise exists), privately, or abroad, following frameworks such as SIGN 156 or the Canadian guideline. It requires evidence of PAE (or sentinel facial features) plus multidomain neurodevelopmental assessment. The EP does not diagnose.",
  "who_wrote_report": "Paediatric or multidisciplinary FASD assessment report; CDNT or CAMHS reports; private clinic reports; overseas reports for internationally adopted children; Tusla care planning documents. Older reports may use FAS, pFAS, ARND or 'FAE'. Earlier reports may give ADHD, attachment disorder or behaviour labels only.",
  "refer_to": "GP / paediatrics for FASD consideration (route varies — check locally); CDNT for multidisciplinary needs; CAMHS for mental health needs meeting thresholds; SLT; OT for sensory needs; the Tusla social worker for children in care; FASD Ireland / FASD Hub Ireland for family support and signposting; Tusla (Children First) for any current welfare concern.",
  "sooner": "'FASD is one of the hardest conditions to recognise, and there's no clear pathway in Ireland, so many families wait years or never get an answer. Understanding it now still makes a real difference — especially for secondary school and the teenage years.'",
 },

 "differential": [
  "ADHD ALONE — attention and impulsivity without the memory, adaptive and comprehension profile; the two may co-occur.",
  "TRAUMA / ATTACHMENT DIFFICULTY — dysregulation and relational difficulty from early adversity; may co-occur.",
  "INTELLECTUAL DISABILITY OR GENETIC SYNDROME — some syndromes share facial or growth features; medical genetics question.",
  "LANGUAGE DISORDER — comprehension difficulty with fluent speech; SLT assessment.",
  "AUTISM — social-communication and sensory differences; specialist assessment.",
 ],

 "next": [
  "Gather history with care: care history, known exposures and existing reports — only what is needed, with consent.",
  "Assess cognition, comprehension, memory, attention and adaptive functioning; observe unstructured times.",
  "Write an environment-first plan with the family or carers, school and social worker.",
  "Recommend GP / paediatric referral for FASD consideration where indicated, stating it as a question, not a conclusion.",
  "Check safeguarding and risk; plan for transitions.",
 ],

 "presentations": [
  "Self-regulation difficulty",
  "Working memory difficulty",
  "Difficulty learning from consequences",
  "Inconsistent performance day to day",
  "Social vulnerability and suggestibility",
  "Care-experienced children (foster, kinship, residential, aftercare)",
  "Sensory processing differences",
  "Attention and concentration difficulty",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — diagnosed when sentinel features are clear; otherwise 'at risk' designation (SIGN, 2019)",
   "prevalence": "No Irish figure — modelled estimates only (Lange et al., 2017 — check).",
   "see": "Low birth weight and growth, feeding and sleep difficulties, irritability, developmental delay, sensory sensitivity, high activity. Many young children with PAE are in foster or kinship care. The EP role is consultation with pre-school and carers, and making sure development is monitored into school.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Griffiths III", "Vineland-3", "SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — the band where difficulties in learning, memory and behaviour usually become clear",
   "prevalence": "No Irish figure; much higher in care-experienced and adopted children (Lange et al., 2013 — check).",
   "see": "A chatty, likeable child who seems able but cannot follow multi-step instructions, forgets yesterday's learning, struggles with maths, money and time, and repeats the same 'mistakes' despite consequences. Yard and transitions go badly. Often already labelled ADHD or 'attachment'.",
   "tools": ["WISC-V UK", "WIAT-III UK", "ABAS-3", "Vineland-3", "CELF-5 UK", "BRIEF-2", "Conners-4", "SDQ"],
  },
  "Adolescent": {
   "applies": "YES — high-risk band for school breakdown, exploitation, substance use and justice contact",
   "prevalence": "No Irish figure — check.",
   "see": "Post-primary organisation collapses; suggestibility and poor judgement lead to exploitation and trouble; mood difficulty and substance use emerge. The gap between how able the young person sounds and what they can manage independently widens. Plan supervision, RACE evidence and transition carefully.",
   "tools": ["WISC-V UK", "WIAT-III UK", "ABAS-3", "BRIEF-2 self-report", "RCADS self-report", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — adult services, independence and justice systems often meet undiagnosed FASD",
   "prevalence": "No Irish figure — check.",
   "see": "Difficulty living independently, managing money, holding jobs and following through on appointments; vulnerability to exploitation; care leavers needing aftercare. EP contribution is transition planning and adaptive evidence for adult services.",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Vineland-3 adult"],
  },
  "Special Setting": {
   "applies": "YES — some young people with FASD are placed in special classes or schools, often for behaviour",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A young person placed for behaviour or ID whose memory, comprehension and adaptive difficulties have not been named. Structure and supervision in special settings often help; staff need FASD-informed approaches rather than sanction systems.",
   "tools": ["Vineland-3 / ABAS-3", "Adaptive measure in place of IQ", "Functional behaviour assessment (ABC)"],
  },
 },
},

]
