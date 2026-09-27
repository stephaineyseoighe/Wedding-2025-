# CONDS records, batch c19: Genetic syndromes (Down, Fragile X, 22q11.2, Williams,
# Prader-Willi, Angelman, Rett); Hypermobility spectrum disorder; Gender dysphoria in
# children and adolescents.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c19.py

CONDS = [

# =====================================================================================
# 1. GENETIC SYNDROMES
# =====================================================================================
{
 "name": "Genetic syndromes (Down, Fragile X, 22q11.2, Williams, Prader-Willi, Angelman, Rett)",
 "code": "Medical / genetic diagnoses — ICD-11 Chapter 20 'Developmental anomalies' (e.g. Down syndrome LD40.0; Fragile X syndrome LD55 — check each code before quoting) · NOT DSM-5-TR mental disorders · DSM-5-TR records an associated known genetic condition as a specifier (e.g. 'autism spectrum disorder associated with a known genetic condition') · Irish education: the GLD category, if any, is decided by assessment, not by the syndrome",
 "neps": "5. OTHER (5.3 Medical condition or other diagnosis) — and 1. LEARNING (1.3 Comprehension and general ability) · 1.2 Language skills where communication is the main barrier",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Disability Act 2005 (Assessment of Need) · EPSEN Act 2004 · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR (genetic and health data are special-category data)",

 "what_it_is": [
  "A GENETIC SYNDROME is a medically diagnosed condition with a known genetic cause (an extra or missing chromosome, a deletion, a single-gene change or an imprinting difference) and a recognisable cluster of physical, health and developmental features. The diagnosis is made by clinical genetics or paediatrics on the basis of testing — never by the EP.",
  "BEHAVIOURAL PHENOTYPE — THE KEY IDEA, AND THE KEY HEDGE. Dykens (1995) defined a behavioural phenotype as a HEIGHTENED PROBABILITY that people with a given syndrome will show certain behavioural or developmental features, relative to people without it. It is a probability, not a prediction: not every child with the syndrome shows the feature, and the feature is not unique to the syndrome. Every bullet below is a group-level tendency — describe THIS child.",
  "WHY IT STILL MATTERS: knowing the phenotype helps you ask the right questions sooner (e.g. hearing in Down syndrome, food security in Prader-Willi, anxiety in Williams, mental-state change in 22q11.2) and helps a team stop reading syndrome-typical behaviour as 'naughty' or as 'just the syndrome' (Waite et al., 2014).",
  "DOWN SYNDROME (trisomy 21): usually diagnosed prenatally or at birth. Group-level profile reported in the literature: relative strength in visual processing and visual learning, and in social engagement; expressive language and speech intelligibility weaker than receptive language; verbal short-term memory a relative weakness (Fidler, 2005). Hearing loss, vision problems, thyroid problems, heart conditions and sleep-disordered breathing are common health issues — check the medical file. Many children learn to read, and reading is often used to support language (Buckley — Down Syndrome Education International; check specific paper).",
  "FRAGILE X SYNDROME (FMR1 gene, X-linked): the most common inherited single-gene cause of intellectual disability (Hagerman et al., 2017). Boys are usually more affected than girls. Reported group tendencies: social anxiety and gaze avoidance, hyperarousal and sensory sensitivity, attention difficulties, repetitive or perseverative speech, hand-flapping or hand-biting when overwhelmed; a high proportion of boys meet autism criteria (Hagerman et al., 2017 — check figure). Girls may present with shyness, anxiety and maths difficulty and can be missed. Carrier status has implications for the wider family — genetics service, not school.",
  "22q11.2 DELETION SYNDROME (formerly DiGeorge / velocardiofacial): very variable. Health features may include heart defects, palate differences, immune and calcium problems. Reported learning profile: verbal skills often stronger than non-verbal, with maths and abstract reasoning difficulty; attention difficulties and anxiety common; and an elevated risk of psychosis emerging in adolescence and early adulthood (McDonald-McGinn et al., 2015 — check the figure before quoting). This is the syndrome where the EP must watch for change in mental state over time.",
  "WILLIAMS SYNDROME (7q11.23 deletion): reported group tendencies include a striking social interest in people (including strangers), relative strength in expressive vocabulary and face processing, a marked visuospatial weakness (copying, construction, spatial layout, handwriting), high rates of anxiety and specific fears, and sensitivity to sound (Mervis & John, 2010). Fluent chat can hide weak comprehension and weak reasoning — adults overestimate the child.",
  "PRADER-WILLI SYNDROME (loss of paternal 15q11–q13 expression): low muscle tone and feeding difficulty in infancy, then from early childhood an increasing preoccupation with food (hyperphagia), with food seeking, and a group tendency to temper outbursts, rigidity and insistence on sameness, and skin picking (Cassidy et al., 2012). Food security — predictable, supervised, non-negotiable access to food — is a safety matter, not a behaviour plan. Diet and growth hormone are medical.",
  "ANGELMAN SYNDROME (loss of maternal UBE3A function, 15q11–q13): usually severe intellectual disability, minimal or no speech with understanding ahead of expression, movement and balance difficulties, epilepsy in most, sleep difficulties, and a characteristically happy, excitable demeanour with frequent laughter (Williams et al., 2006 consensus criteria). Communication through AAC, gesture and signs is the priority; the laughter is not evidence of understanding or of consent.",
  "RETT SYNDROME (mainly MECP2, almost always girls): a period of apparently typical early development, then REGRESSION — loss of purposeful hand use and of spoken language — followed by hand stereotypies (wringing, clapping, mouthing), gait difficulties, breathing irregularities, epilepsy and scoliosis (Neul et al., 2010 revised criteria). Many girls communicate through eye gaze; understanding is frequently underestimated. DSM-IV listed Rett disorder; DSM-5 removed it (APA, 2013).",
  "IRISH CONTEXT: diagnosis and genetic counselling sit with the national clinical genetics service at Children's Health Ireland (CHI) and with paediatrics; ongoing support usually with the CDNT. Syndrome-specific health surveillance (e.g. Down syndrome clinics) exists in some areas — check local arrangements. Family organisations exist for several syndromes (Down Syndrome Ireland and others) — check current names and contact details before signposting.",
 ],

 "what_it_is_not": [
  "NOT DETERMINISTIC. 'Children with Williams syndrome are sociable' is a group tendency; this child may be withdrawn. 'Children with Down syndrome are happy' is a stereotype that hides depression and anxiety. A phenotype tells you what to look for, not what you will find (Dykens, 1995).",
  "NOT A LEVEL OF ABILITY. The same syndrome spans a wide range of cognitive and adaptive functioning. The syndrome does not tell you whether a child has a mild, moderate, severe or no general learning disability — assessment of intellectual AND adaptive functioning does (APA, 2022). Do not write 'Down syndrome — moderate GLD' without evidence.",
  "NOT AN EXPLANATION FOR EVERYTHING. Diagnostic overshadowing — attributing new pain, distress, regression or behaviour change to 'the syndrome' — is one of the main ways children with syndromes are failed. New behaviour needs a new question: pain, hearing, sleep, seizures, thyroid, bullying, loss, abuse.",
  "NOT A REASON FOR A PARTICULAR PLACEMENT. Children with every one of these syndromes attend mainstream classes, special classes and special schools. Placement follows current needs and what a setting can offer, reviewed over time — not the diagnosis.",
  "NOT SOMETHING THE EP DIAGNOSES OR SCREENS FOR. If you suspect an undiagnosed syndrome (features, family history, a distinctive profile), the route is the GP / paediatrician, who decides on genetic referral. Do not write 'possible Fragile X' in a school report; write what you observed and recommend medical review (PSI 2.2.2).",
  "NOT A MEDICAL-ADVICE ROLE. Diet in Prader-Willi, seizure medication in Angelman or Rett, heart surveillance in Williams, psychosis treatment in 22q11.2 — all medical. You can make sure the school plan fits the medical plan; you do not advise on it.",
  "NOT FIXED OVER TIME. Profiles change with age: Prader-Willi food seeking emerges in childhood; 22q11.2 mental-health risk rises in adolescence; Rett regression and then relative stability; adults with Down syndrome have an elevated risk of early-onset Alzheimer's disease. Review, don't file.",
 ],

 "prevalence": [
  "DOWN SYNDROME: the most common chromosomal cause of intellectual disability. Ireland has been reported to have one of the higher live-birth rates in Europe; Down Syndrome Ireland has cited about 1 in 444 live births — check the current figure and its source before quoting.",
  "FRAGILE X: commonly cited as about 1 in 4,000 males and 1 in 8,000 females for the full mutation, with estimates varying by study (Hagerman et al., 2017) — check before quoting.",
  "22q11.2 DELETION: commonly cited as about 1 in 3,000–6,000 live births, and likely under-diagnosed because of its variability (McDonald-McGinn et al., 2015) — check.",
  "WILLIAMS, PRADER-WILLI, ANGELMAN, RETT: each rare — estimates in the order of 1 in 10,000 to 1 in 20,000 births are commonly cited (Williams syndrome: Strømme et al., 2002; Prader-Willi: Cassidy et al., 2012; Angelman: Williams et al., 2006; Rett, in females: Neul et al., 2010). Exact figures vary — check each source before quoting.",
  "IRELAND: no single Irish register covers all syndromes. The National Intellectual Disability Database (Health Research Board) records people receiving ID services, not syndromes as such — rate not stated here, check.",
  "SEX RATIO: Fragile X more severe in males (X-linked); Rett almost exclusively diagnosed in females; the others affect both sexes — check syndrome-specific sources.",
  "IN YOUR CASELOAD: expect Down syndrome often, the others rarely. You may be the first professional to hold several of these in mind at once — which is why a structured approach matters more than recall.",
 ],

 "cooccurring": [
  {"name": "INTELLECTUAL DISABILITY / GENERAL LEARNING DISABILITY",
   "rate": "common across these syndromes but not universal and of variable degree — rate not stated here, check per syndrome",
   "presents": "a general learning profile that still needs its own assessment of intellectual AND adaptive functioning. The syndrome is the cause; the level of support needed is a separate question answered by assessment and observation."},
  {"name": "AUTISM",
   "rate": "elevated in several syndromes, notably Fragile X (especially boys), and reported in Down syndrome, 22q11.2 and Angelman — figures vary, check",
   "presents": "social communication differences beyond what the learning profile explains. Easily missed in Down syndrome (where sociability is assumed) and over-called in Williams (where social approach is atypical but intense). Refer to CDNT for assessment; DSM-5-TR allows the 'associated with a known genetic condition' specifier."},
  {"name": "ANXIETY",
   "rate": "high rates reported in Williams, Fragile X and 22q11.2 — check figures",
   "presents": "fears, avoidance, repeated questioning, meltdowns at change, gaze avoidance, physical complaints. Often read as behaviour or as 'part of the syndrome'. Needs adapted anxiety work, predictable routine and a plan for transitions."},
  {"name": "ADHD / ATTENTION DIFFICULTIES",
   "rate": "elevated in Fragile X, 22q11.2 and Williams — check figures",
   "presents": "short attention, impulsivity, overactivity. First check that work is pitched at the child's level and that hearing and sleep are addressed; then consider referral. Medication questions go to the treating doctor."},
  {"name": "HEARING AND VISION IMPAIRMENT",
   "rate": "very common in Down syndrome; checks needed in all — check figures",
   "presents": "poor response to instruction, speech difficulty, apparent inattention, reluctance with close work. Ask for dates of the last audiology and ophthalmology review before interpreting any score."},
  {"name": "EPILEPSY",
   "rate": "very common in Angelman and Rett; elevated in several others — check",
   "presents": "absences mistaken for day-dreaming, drops in performance, fatigue after seizures, medication side effects. The school needs a seizure care plan from the medical team — you make sure the learning plan takes it into account."},
  {"name": "SLEEP DIFFICULTIES",
   "rate": "common, especially Angelman, Rett, Down syndrome (sleep-disordered breathing) — check",
   "presents": "daytime tiredness, irritability, poor concentration and behaviour change. Ask the family directly; refer via GP where sleep has not been looked at."},
  {"name": "MENTAL HEALTH CHANGE IN ADOLESCENCE AND ADULTHOOD",
   "rate": "elevated — e.g. psychosis risk in 22q11.2; depression and regression reported in young adults with Down syndrome; psychosis reported in some Prader-Willi subtypes — check each",
   "presents": "withdrawal, loss of skills, new odd beliefs or perceptions, sleep and appetite change, loss of interest. This is not 'the syndrome' and not 'adolescence' until a doctor has looked. Refer via GP / CAMHS; same-day route if risk."},
  {"name": "BEHAVIOURS OF CONCERN (self-injury, aggression, food seeking, skin picking)",
   "rate": "reported in several syndromes; profiles differ (e.g. skin picking and food seeking in Prader-Willi, hand-biting in Fragile X) — check",
   "presents": "behaviour that communicates pain, anxiety, sensory overload, a need or a wish. A functional behaviour assessment plus the syndrome knowledge gives a better hypothesis than either alone (Waite et al., 2014)."},
 ],

 "recommendations": [
  "DESCRIBE THE CHILD FIRST, THE SYNDROME SECOND. Report structure: what the child does now in communication, learning, social, motor and self-care, with examples; then 'what the literature on [syndrome] suggests may be worth watching', attributed and hedged. Never write the phenotype as though it were an assessment finding.",
  "USE THE PHENOTYPE AS A CHECKLIST OF QUESTIONS, NOT CONCLUSIONS: Down syndrome → hearing, vision, thyroid, visual supports, reading to support language; Fragile X → anxiety, arousal, sensory load, indirect social demands; 22q11.2 → maths, abstract language, anxiety, mental-state monitoring; Williams → comprehension behind fluent speech, visuospatial support, anxiety, stranger safety; Prader-Willi → food security, routine, change warnings; Angelman / Rett → AAC and access to communication all day, seizures, positioning.",
  "COMMUNICATION IS THE PRIORITY WHERE SPEECH IS LIMITED. Write a named total-communication approach: Lámh signing (Ireland's key word sign system), visual supports, AAC or eye-gaze systems with SLT. Every adult uses it, every day, across the day. For Angelman and Rett, presume understanding is greater than expression until shown otherwise.",
  "VISUAL, CONCRETE, REPEATED. For most of these profiles: visual timetables, demonstration, short spoken instructions, concrete materials, lots of repetition, and teaching for generalisation in the setting where the skill is needed (see GLD entry).",
  "PLAN FOR ANXIETY AND CHANGE: warn of changes, use visual schedules for the day, have a named adult, build calm spaces and exit routes; in Fragile X reduce direct demands for eye contact and face-to-face questioning; in Williams address specific fears and noise sensitivity.",
  "PRADER-WILLI FOOD SECURITY: write it as a whole-school safety requirement agreed with parents and the medical team — supervised food, no food rewards, secured bins and lunches, clear routines, briefing for substitute staff and for school trips. Behaviour around food is not wilful and is not treated as a discipline matter.",
  "HEALTH IN THE PLAN: ask the family for the relevant medical plans (seizures, cardiac, diet) with consent, and reflect their educational implications — fatigue, absence, medication timing, physical activity limits.",
  "CURRICULUM AND TRANSITION: pitch to the current profile; at post-primary consider L1LP / L2LP routes early; start transition planning from about 14; adult services have long lead times. Check current NCSE and HSE processes before advising.",
  "CONTINUUM LEVEL: usually School Support Plus because medical, CDNT and often SLT / OT are involved; some children with milder profiles are well served at School Support. Name the level and say why.",
  "REFER: GP / paediatrics (and through them clinical genetics) if a syndrome is suspected but undiagnosed, or for new health or mental-state concerns; CDNT for multidisciplinary support; SLT for communication and AAC; OT / physiotherapy for motor and seating; CAMHS via GP for mental-health concerns; SENO for placement and SNA questions; Tusla for any child protection concern.",
  "DO NOT diagnose or suggest a specific syndrome in a report, advise on genetic testing, diet, medication or seizure management, or attribute new behaviour to the syndrome without asking what else has changed.",
 ],

 "explain_parent": [
  "'You know far more about [syndrome] than most professionals will. What I want to know is what [child] is like — what she loves, what's hard, what helps. The syndrome gives us some things to keep an eye on; it doesn't tell us who she is.'",
  "'The research describes things that are MORE LIKELY in children with this syndrome, not things that will definitely happen. So I'll ask about some of them — sleep, hearing, worries — not because I expect them, but because it's easy to miss them.'",
  "'When his behaviour changes, I'd always want to rule out something new — pain, ears, sleep, something upsetting at school — before anyone says \"that's just the syndrome\".'",
  "'Questions about genes, testing, what it means for brothers and sisters or future pregnancies are for the genetics service — they have genetic counsellors whose job this is. I can help you write down your questions.'",
  "'The support she gets in school depends on what she needs day to day, not on the name of the syndrome. My job is to describe those needs clearly so the school and the SENO can plan properly.'",
  "SIGNPOST: the CDNT key worker; the clinical genetics service (through the GP or paediatrician); Down Syndrome Ireland and other syndrome-specific family organisations (check current Irish groups for Fragile X, 22q11.2, Williams, Prader-Willi, Angelman and Rett); Inclusion Ireland; Lámh for signing courses; the SENO for placement.",
 ],

 "explain_teacher": [
  "'Please read the syndrome as a list of things to watch for, not a description of this child. If what you see doesn't fit the leaflet, trust what you see and tell us.'",
  "'For her, show rather than tell: visual timetable, demonstrate the task, short instructions, then check by asking her to show you — not by asking \"do you understand?\"'",
  "'He talks really well, but his understanding is behind his talking. Check comprehension every time — ask him to tell you in his own words or show you — and simplify written tasks.' (Williams / 22q11.2)",
  "'Direct eye contact and being put on the spot are very hard for him. Side-by-side, fewer direct questions, a warning before he's asked to answer, and somewhere to go when he's overwhelmed.' (Fragile X)",
  "'Food needs to be secured and supervised all day — including classroom treats, trips and the staffroom. This is part of her medical safety, not a behaviour issue.' (Prader-Willi)",
  "'Keep a short note of any change — new behaviours, sleepiness, staring spells, loss of skills, odd comments. You see her more than anyone except her parents; your notes may be what gets her seen.'",
 ],

 "explain_child": [
  "YOUNGER / LIMITED SPEECH: you don't explain the syndrome. You explain what's happening now, with objects, photos or signs: 'I'm going to play with you and see what you like.' Offer choices and watch for yes and no signals the family has taught you.",
  "OLDER, WHO KNOW THEY HAVE A SYNDROME: many young people with Down syndrome, Williams or 22q11.2 know the name and have views on it. Ask: 'What do you call it? What do you want people to know about you?'",
  "'Everybody's body and brain are made a bit differently. Some things are easier for you and some are harder. We're working out what helps you learn best.'",
  "IF ASKED 'WHY AM I DIFFERENT?': 'You were born with something a bit different in your genes — the instructions that make your body. It's nobody's fault. It's part of you, not all of you.' Agree the wording with parents first — some families use the syndrome name with their child, some don't yet.",
  "QUESTIONS TO ASK: 'What's the best part of school?' 'What's the hardest part?' 'Who helps you?' 'What makes you worried?' — with visual supports or Talking Mats if needed.",
 ],

 "analogies": [
  "THE WEATHER FORECAST FOR A REGION: 'The syndrome tells you the weather that's more likely in this region — it doesn't tell you what's happening in your garden today.' Good with teachers who treat phenotype leaflets as descriptions of the child.",
  "THE RECIPE WITH A CHANGED INGREDIENT: 'Genes are like a recipe. In his case one part of the recipe is different, which changes some things about how he grows and learns. Lots of the recipe is the same as everyone's.' Good with siblings and older children; check the family is comfortable with genetic explanations.",
  "THE ICEBERG OF CHAT: 'His talk is the tip of the iceberg you can see; his understanding is the part underwater, and it's smaller than it looks.' Good for Williams and 22q11.2 profiles where speech overestimates comprehension.",
  "THE SMOKE ALARM: 'When behaviour changes suddenly, treat it as a smoke alarm — something new is going on. Don't take the batteries out by saying it's the syndrome.' Good for diagnostic overshadowing in team meetings.",
  "CAUTION: avoid 'eternal child', 'angel' (including for Angelman) or 'always happy' images — they deny a child's age, distress and rights.",
 ],

 "language": [
  "Use the syndrome's current name: 'Down syndrome' (not 'Down's' in formal writing — Down Syndrome Ireland uses 'Down syndrome'; check current preference); '22q11.2 deletion syndrome' (older reports say DiGeorge or velocardiofacial syndrome); 'Fragile X syndrome'.",
  "Person-first is the common preference in the Down syndrome community ('a child with Down syndrome', not 'a Down syndrome child' or 'a Down's child'). Ask each family and each young person what they prefer.",
  "Never use historical terms ('mongolism', 'mental handicap', 'retarded') — flag them if you find them in old reports.",
  "Avoid 'suffers from' and 'afflicted with'. Say 'has' or 'lives with'.",
  "Write 'reported in the literature on [syndrome]' or 'may be more likely' — never 'children with [syndrome] are…'.",
  "Genetic information is sensitive health data: record only what is needed for the educational plan, with consent, and do not share details of family carrier status.",
 ],

 "red_flags": [
  "RED FLAG — LOSS OF SKILLS (speech, hand use, walking, toileting, self-care) or a clear change in personality or mental state. Urgent medical review via GP / paediatrics the same day you learn of it; do not attribute it to the syndrome, to puberty or to behaviour.",
  "RED FLAG — new unusual beliefs, hearing or seeing things others don't, marked withdrawal or confusion, especially in an adolescent with 22q11.2. Refer via GP / CAMHS; if there is any risk to self or others, use the same-day risk route.",
  "RED FLAG — self-harm, suicidal talk, or signs of abuse or neglect. Children with disabilities are at higher risk of abuse and less able to disclose. Follow Children First: a mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty. Act first, then bring it to supervision.",
  "RED FLAG — unsecured food access, food theft or rapid weight gain in a child with Prader-Willi. This is a medical safety issue — tell parents and ask them to involve the medical team; review the school food plan the same week.",
  "RED FLAG — staring spells, jerks, drops or unexplained falls. Possible seizures — medical referral via GP / paediatrics; ask whether a seizure care plan exists.",
  "BOUNDARY — you do not diagnose, suggest or rule out a syndrome, interpret genetic results, or advise on diet, medication or testing. You describe functioning and needs, and refer (PSI 2.2.2).",
  "WATCH — a plan that has not changed since the diagnosis. Profiles change with age; review at every transition.",
 ],

 "child_voice": [
  "TALKING MATS — good because it separates having a view from being able to say it, and works with symbols for young people with limited speech. → https://www.talkingmats.com/",
  "AAC AND EYE-GAZE, USING THE CHILD'S OWN SYSTEM — good because asking a child with Angelman or Rett syndrome to answer in speech measures their speech, not their views. Ask the SLT and family how the child says yes, no and 'stop'.",
  "OBSERVATION OF PREFERENCE AND CHOICE — offer real choices across the day and record what the child chooses, returns to, and avoids. Good because choice is voice for children with severe ID.",
  "PHOTO AND VIDEO TOURS (Mosaic approach; Clark & Moss, 2011) — the child shows you the places and people that matter. Good because it does not depend on answering questions.",
  "SEMI-STRUCTURED INTERVIEW WITH VISUALS for verbally able young people (e.g. Williams, 22q11.2, many with Down syndrome) — good because it respects their capacity to speak for themselves; check understanding by asking them to show or retell.",
  "PARENT AND KEY-ADULT REPORT, LABELLED AS SUCH — 'mother reports that she…' — good because they know the child's signals; bad if presented as the child's own voice.",
 ],

 "questions": [
  "Q: 'Will she be able to go to an ordinary school?' — A: 'Many children with Down syndrome do very well in mainstream classes, and some are better served in a special class or school. It depends on what she needs and what each setting can offer, and it can be reviewed. I'll describe her needs so the decision is well informed, and the SENO can talk you through options.'",
  "Q: 'The leaflet says children with Williams syndrome are very sociable — why is he so anxious?' — A: 'The leaflets describe what's more common across lots of children, and anxiety is actually reported a lot in Williams syndrome too. He's himself first. Let's look at what's making him anxious and what helps.'",
  "Q: 'Is his behaviour the syndrome or is it him?' — A: 'That's the right question, and the honest answer is usually both and neither. Behaviour is almost always telling us something — pain, worry, too much noise, wanting something. The syndrome can make some of those more likely. Let's work out what it's telling us.'",
  "Q: 'Should we have our other children tested?' — A: 'That's a question for the genetics service — it depends on the syndrome and how it happened, and they have genetic counsellors for exactly this. Your GP or paediatrician can refer you.'",
  "Q (teacher): 'She's got Angelman — is there any point in teaching her to read?' — A: 'Her understanding is likely to be ahead of what she can show, so we assume competence and give her ways to show us. Literacy experiences, symbols and AAC all belong in her day. Let's set targets with the SLT rather than decide in advance what she can't do.'",
  "Q (teacher): 'He keeps taking food from other children's bags — how do we discipline that?' — A: 'In Prader-Willi syndrome, food seeking is driven by the condition, not by wilfulness, so punishment won't work and can make things worse. What works is making food secure and predictable so he doesn't have to look for it. Let's write a food-security plan with his parents.'",
  "Q (parent of an adolescent with 22q11.2): 'He's become very quiet and says odd things — is that just being a teenager?' — A: 'It might be, but in 22q11.2 we don't wait to find out. I'd like you to see your GP this week and mention the syndrome. If you're worried about his safety at any point, go the same day.'",
  "Q: 'Did something I did cause this?' — A: 'No. These genetic differences happen at conception or are inherited through no action of anyone's. The genetics service can explain exactly how it happened for your family.'",
 ],

 "supervision": [
  "Ask how your service reads syndrome-specific information: which sources your supervisor trusts (e.g. SSBP syndrome sheets, syndrome organisation guidance) and how they phrase phenotype information in reports without being deterministic.",
  "Bring a case where behaviour was put down to 'the syndrome' and ask what else should have been checked — pain, hearing, seizures, sleep, bullying, abuse.",
  "Ask about AAC and communication access for children with little or no speech: how your supervisor assesses a child's views when speech is not available, and how they record it.",
  "Discuss consent and data: how much medical and genetic information belongs in a school-facing report, and how to handle family carrier information you are told.",
  "Bring any safeguarding concern about a disabled child and confirm the Children First action taken before discussing formulation.",
 ],

 "reflection": [
  "ON DETERMINISM — Did I write anything that sounds like 'children with X are…'? Did I describe this child first and the syndrome second?",
  "ON OVERSHADOWING — When behaviour changed, did I ask what else was new before accepting 'it's the syndrome'?",
  "ON COMMUNICATION — Did the child have a way to tell me what they thought? If not, whose voice did I record, and did I label it honestly?",
  "ON EXPECTATIONS — Did the phenotype lower my expectations (e.g. literacy in Angelman or Down syndrome) without evidence from this child?",
  "ON BOUNDARY — Did I stray into genetics, diet, medication or seizure management? Did I refer rather than advise?",
  "WHAT GOOD LOOKS LIKE: 'I described what she does in each area, then added: \"The literature on Williams syndrome reports high rates of anxiety and a visuospatial weakness (Mervis & John, 2010); both fit what staff describe and are addressed below.\" Hedged, attributed, and tied to this child.'",
  "WHAT POOR LOOKS LIKE: 'As is typical in Down syndrome, he is a happy, sociable visual learner with moderate GLD.' — a stereotype, an unassessed ability level and no child in it.",
 ],

 "citations": [
  "Dykens, E. M. (1995). Measuring behavioral phenotypes: Provocations from the 'new genetics'. American Journal on Mental Retardation, 99(5), 522–532.",
  "Fidler, D. J. (2005). The emerging Down syndrome behavioral phenotype in early childhood: Implications for practice. Infants & Young Children, 18(2), 86–103.",
  "Hagerman, R. J., Berry-Kravis, E., Hazlett, H. C., et al. (2017). Fragile X syndrome. Nature Reviews Disease Primers, 3, 17065.",
  "McDonald-McGinn, D. M., Sullivan, K. E., Marino, B., et al. (2015). 22q11.2 deletion syndrome. Nature Reviews Disease Primers, 1, 15071.",
  "Mervis, C. B., & John, A. E. (2010). Cognitive and behavioral characteristics of children with Williams syndrome: Implications for intervention approaches. American Journal of Medical Genetics Part C, 154C(2), 229–248.",
  "Cassidy, S. B., Schwartz, S., Miller, J. L., & Driscoll, D. J. (2012). Prader-Willi syndrome. Genetics in Medicine, 14(1), 10–26.",
  "Williams, C. A., Beaudet, A. L., Clayton-Smith, J., et al. (2006). Angelman syndrome 2005: Updated consensus for diagnostic criteria. American Journal of Medical Genetics Part A, 140(5), 413–418.",
  "Neul, J. L., Kaufmann, W. E., Glaze, D. G., et al. (2010). Rett syndrome: Revised diagnostic criteria and nomenclature. Annals of Neurology, 68(6), 944–950.",
  "Waite, J., Heald, M., Wilde, L., Woodcock, K., Welham, A., Adams, D., & Oliver, C. (2014). The importance of understanding the behavioural phenotypes of genetic syndromes associated with intellectual disability. Paediatrics and Child Health, 24(10), 468–472. (Check details before quoting.)",
  "Strømme, P., Bjørnstad, P. G., & Ramstad, K. (2002). Prevalence estimation of Williams syndrome. Journal of Child Neurology, 17(4), 269–271.",
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.).",
  "Clark, A., & Moss, P. (2011). Listening to young children: The Mosaic approach (2nd ed.). National Children's Bureau.",
  "Moeschler, J. B., Shevell, M., & Committee on Genetics. (2014). Comprehensive evaluation of the child with intellectual disability or global developmental delays. Pediatrics, 134(3), e903–e918.",
 ],

 "pathway": {
  "age": "Down syndrome: usually prenatally or at birth. Prader-Willi and Angelman: often in infancy (low tone, feeding, seizures, delay). Rett: after regression, typically in the second year or later. Fragile X, 22q11.2 and Williams: anywhere from infancy to school age or later, because the features vary and may only come together as learning or health problems emerge — some are first diagnosed after genetic testing for developmental delay or autism.",
  "who_diagnoses": "Ireland: clinical genetics (the national service at Children's Health Ireland — check current arrangements) and paediatrics, on the basis of genetic testing ordered by a doctor. Neonatology for diagnoses at birth. The CDNT then usually leads developmental support. The EP never diagnoses a syndrome.",
  "who_wrote_report": "Genetics or paediatric letter (diagnosis, test result, health surveillance); CDNT multidisciplinary reports (psychology, SLT, OT, physiotherapy); Assessment of Need report and Service Statement; cardiology, neurology, endocrinology or dietetic letters; private assessments. Check dates — early reports predate much of the child's development.",
  "refer_to": "GP / paediatrics (and through them clinical genetics) for suspected undiagnosed syndromes or new health concerns; CDNT for multidisciplinary support; SLT for communication and AAC; OT and physiotherapy for motor, seating and self-care; audiology and ophthalmology; CAMHS via GP for mental-health concerns; SENO for placement and SNA; Tusla for child protection.",
  "sooner": "'Some syndromes are hard to spot because every child looks different — it's common for a diagnosis to come after years of questions. What matters is that you kept asking. The diagnosis now helps us know what to watch for and helps you connect with other families and the right services.'",
 },

 "differential": [
  "NON-SYNDROMIC INTELLECTUAL DISABILITY OR GDD — the same learning profile without an identified genetic cause; the majority of children with ID have no single identified cause (Moeschler et al., 2014 — check).",
  "AUTISM WITHOUT A SYNDROME — social communication profile without the physical and health features; genetic testing is a medical decision.",
  "FOETAL ALCOHOL SPECTRUM DISORDER — can overlap with some features (learning, attention, facial features); medical assessment.",
  "HEARING OR VISION IMPAIRMENT — can mimic or add to a learning or communication profile; check first.",
  "DEPRIVATION, TRAUMA OR NEGLECT — delays and behaviour that improve with good care; take the history and act on any concern.",
  "REGRESSIVE NEUROLOGICAL OR METABOLIC CONDITION — loss of skills needs urgent medical review (Rett is one cause, not the only one).",
 ],

 "next": [
  "Read the medical and CDNT reports for the diagnosis date, health issues (hearing, vision, heart, seizures, diet) and what was assessed — then ask the family what has changed since.",
  "Use the syndrome as a question checklist, not a description; observe the child and describe current functioning by domain.",
  "Establish how the child communicates and make sure every adult uses that system.",
  "Write a plan that includes health, communication, anxiety and change, with a review date at every transition.",
  "Refer on for anything new — skill loss, mental-state change, seizures, weight or food concerns — and act the same day on any risk.",
 ],

 "presentations": [
  "Communication without speech (gesture, signs, AAC)",
  "Curriculum access at the current level",
  "Anxiety and difficulty with change",
  "Behaviours of concern (self-injury, aggression, food seeking)",
  "Physical disability and motor needs",
  "Fatigue and stamina needs",
  "Transition to post-primary and adult services",
  "Loss of skills (regression) — medical referral",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — Down, Prader-Willi and Angelman are usually diagnosed in this band; the others may be",
   "prevalence": "Down syndrome is the most common; Ireland's live-birth rate is reported to be relatively high (check current figure). Others rare — see prevalence.",
   "see": "Low tone, feeding difficulty, delayed milestones, limited speech, early health appointments. Families are absorbing the diagnosis and managing medical care; CDNT usually leads. The EP's contribution is mainly at pre-school and school-entry transition: describe what the child does, check hearing and vision, and set up communication supports (e.g. Lámh) that will carry into school.",
   "tools": ["Griffiths III", "Bayley-4", "Vineland-3", "ABAS-3", "Schedule of Growing Skills II", "Communication Matrix / AAC review"],
  },
  "School Age": {
   "applies": "YES — the main band for EP involvement and for later diagnoses (Fragile X, 22q11.2, Williams)",
   "prevalence": "Low overall — any single syndrome is rare in a given school; Down syndrome is the one most schools will meet. Figures: check.",
   "see": "Learning profile unfolding against the curriculum; relative strengths and weaknesses become visible (e.g. visual learning in Down syndrome, visuospatial difficulty in Williams, maths in 22q11.2 and Fragile X girls). Anxiety, attention and social difficulties may become the referral reason. Prader-Willi food seeking and Rett stability-after-regression shape the school day. Assess current functioning and adapt.",
   "tools": ["WISC-V UK", "Leiter-3", "WNV (Wechsler Non-Verbal)", "Vineland-3", "ABAS-3", "Communication Matrix / AAC review", "SDQ", "Functional behaviour assessment (ABC)", "BRIEF-2"],
  },
  "Adolescent": {
   "applies": "YES — watch for mental-health change and plan transition",
   "prevalence": "As for school age; mental-health risks rise (e.g. psychosis in 22q11.2) — check figures.",
   "see": "Curriculum route (L1LP / L2LP / Junior Cycle), RACE and transition to adult services become central. Anxiety and low mood may increase; in 22q11.2, watch closely for changes in thinking, perception and withdrawal. Puberty brings new health and safety questions (relationships, online safety, personal care) — plan with parents and the CDNT.",
   "tools": ["WISC-V UK", "WAIS-IV UK", "ABAS-3", "Vineland-3", "SDQ", "RCADS", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — transition to adult disability and health services",
   "prevalence": "Not a school-population figure; adult ID services data via the National Intellectual Disability Database — check.",
   "see": "Transition to further education, training, day services or work. Evidence of onset in the developmental period supports adult-service eligibility. Adults with Down syndrome have an elevated risk of early-onset dementia and of depression; a young adult who loses skills needs medical review, not a new behaviour plan. Refer on to adult services.",
   "tools": ["WAIS-IV UK", "ABAS-3 adult form", "Vineland-3 adult"],
  },
  "Special Setting": {
   "applies": "YES — children with these syndromes are over-represented in special classes and special schools, though many attend mainstream",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A class where several children have different syndromes and severe or profound needs. Priorities: communication access for every child, seizure and health plans, positioning and physical care, food security where relevant, and a behaviour plan that asks what the behaviour communicates. Use adaptive and observational measures against the setting curriculum rather than IQ tests.",
   "tools": ["Adaptive measure in place of IQ", "Vineland-3 / ABAS-3", "Communication Matrix / AAC review", "Functional behaviour assessment (ABC)", "Leiter-3"],
  },
 },
},

# =====================================================================================
# 2. HYPERMOBILITY SPECTRUM DISORDER
# =====================================================================================
{
 "name": "Hypermobility spectrum disorder (HSD) and joint hypermobility",
 "code": "Medical — NOT a DSM-5-TR diagnosis · classification from the International Consortium on Ehlers-Danlos syndromes and related disorders (Castori et al., 2017; Malfait et al., 2017) · ICD-11: no dedicated HSD code identified here; hypermobile Ehlers-Danlos syndrome sits within the Ehlers-Danlos syndromes (Chapter 20) — check codes before quoting · older reports: 'joint hypermobility syndrome (JHS)' or 'benign joint hypermobility'",
 "neps": "1. LEARNING (1.6 Co-ordination — fine motor / handwriting, gross motor / PE skills) — and 5. OTHER (5.3 Medical condition or other diagnosis) · 3. EMOTIONAL (3.2 Anxiety · 3.6 School attendance) where pain, fatigue or anxiety drive the referral",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Equal Status Acts 2000–2018 (reasonable accommodation) · EPSEN Act 2004 · Disability Act 2005 · Children First Act 2015 · GDPR",

 "what_it_is": [
  "JOINT HYPERMOBILITY means joints that move beyond the typical range. On its own it is common, especially in young children, girls and some ethnic groups, and it is often an asset (dancers, gymnasts, musicians). It is a physical trait, not a diagnosis (Castori et al., 2017).",
  "HYPERMOBILITY SPECTRUM DISORDER (HSD) is the label introduced in 2017 by the International Consortium on the Ehlers-Danlos syndromes for people whose joint hypermobility comes with SYMPTOMS — pain, recurrent sprains or subluxations, fatigue, and other problems — who do not meet the criteria for hypermobile Ehlers-Danlos syndrome (hEDS) or another connective tissue disorder (Castori et al., 2017). It replaced the older 'joint hypermobility syndrome'.",
  "hEDS is a separate, tighter clinical diagnosis with specific criteria (Malfait et al., 2017). The 2017 hEDS criteria use the Beighton score with age-related thresholds (reported as ≥6 for pre-pubertal children and adolescents, ≥5 for pubertal people up to 50, ≥4 over 50 — check the paper before quoting). Other EDS types are diagnosed by genetic testing. Distinguishing them is a medical (rheumatology / genetics) job.",
  "CHILDREN ARE A SPECIAL CASE: hypermobility is normal in many young children and reduces with age, so diagnosing HSD or hEDS before puberty is contested. A paediatric framework has been proposed (Tofts et al., 2023) — check what the treating team uses. Expect reports to vary.",
  "WHAT MATTERS IN SCHOOL is function, not joint range: pain (hands, knees, back), fatigue and stamina, handwriting speed and comfort, clumsiness and falls, difficulty with prolonged sitting or standing, and absences for appointments or flare-ups. Physiotherapy and OT lead on management; exercise and strengthening are central (Engelbert et al., 2017).",
  "ASSOCIATIONS — HOLD LIGHTLY: studies report associations between joint hypermobility and anxiety (Bulbena et al., 2017), with DCD / motor co-ordination difficulties (Kirby & Davies, 2007), and with autism and ADHD (e.g. Csecs et al., 2022). These are associations at group level, the mechanisms are not established, and hypermobility does not cause or explain these conditions in an individual child. Some people also describe dizziness on standing, gut symptoms and sleep problems — medical questions.",
  "IRISH CONTEXT: usually identified by a GP, physiotherapist, paediatrician or paediatric rheumatology (national paediatric rheumatology at Children's Health Ireland — check current arrangements). Primary Care physiotherapy and OT typically provide ongoing support; CDNT only where needs are complex and meet criteria. It is not a NEPS or EP diagnosis.",
 ],

 "what_it_is_not": [
  "NOT A PSYCHOLOGICAL OR DSM DIAGNOSIS. HSD is a medical classification. The EP describes the educational impact (pain, fatigue, handwriting, attendance, anxiety) and refers — does not identify or 'screen' for HSD (PSI 2.2.2).",
  "NOT THE SAME AS BEING FLEXIBLE. Many children are hypermobile with no symptoms; that is not a disorder and needs no plan. The disorder is hypermobility PLUS problems (Castori et al., 2017).",
  "NOT A REASON TO STOP PE. Guidance for children with symptomatic hypermobility generally emphasises staying active with strengthening and graded activity, adapted as needed, with physiotherapy advice (Engelbert et al., 2017). Blanket exclusion from PE risks deconditioning and isolation — follow the physio's plan.",
  "NOT 'ALL IN THE MIND'. Pain and fatigue are real even when scans and blood tests are normal. Equally, anxiety can amplify pain and pain can drive anxiety — both are addressed, neither dismisses the other.",
  "NOT AN EXPLANATION FOR AUTISM, ADHD OR ANXIETY. The research associations are real but do not mean one causes the other. Each needs its own assessment through the usual route.",
  "NOT THE SAME AS DCD. A hypermobile child's handwriting may be slow because of pain, grip or fatigue, not because of a motor-planning disorder. DCD and hypermobility can co-occur (Kirby & Davies, 2007); the OT distinguishes them.",
  "NOT EVIDENCE OF OR AGAINST ABUSE. Easy bruising occurs in some connective tissue disorders; unexplained injuries still follow Children First. A diagnosis does not close a child protection question, and a child protection concern does not dismiss a diagnosis.",
 ],

 "prevalence": [
  "GENERALISED JOINT HYPERMOBILITY in children: widely reported as common, with estimates varying greatly by age, sex, ethnicity and the Beighton cut-off used — rate not stated here, check before quoting.",
  "HSD / hEDS: prevalence not well established because the 2017 criteria are recent and applied inconsistently in children — rate not stated here, check.",
  "SEX RATIO: joint hypermobility and symptomatic presentations are reported more often in girls and women (Castori et al., 2017 — check); ratio not stated here.",
  "IRELAND: no Irish prevalence figure identified — check before quoting.",
  "AGE: hypermobility generally decreases with age; symptoms often become more of a problem around puberty and in adolescence, when growth, school demands (writing volume, exams) and sport intensity increase.",
  "IN YOUR CASELOAD: you are more likely to meet it as a line in an OT, physio or paediatric report for a child referred for handwriting, DCD, attendance or anxiety than as the referral reason itself.",
 ],

 "cooccurring": [
  {"name": "DEVELOPMENTAL COORDINATION DISORDER (DCD)",
   "rate": "overlap reported (Kirby & Davies, 2007) — rate not stated here, check",
   "presents": "clumsiness, falls, poor ball skills, slow effortful handwriting. Ask the OT or physio which parts are motor planning (DCD) and which are joint stability, pain or fatigue (hypermobility) — the supports differ."},
  {"name": "ANXIETY",
   "rate": "association reported (Bulbena et al., 2017) — rate not stated here, check",
   "presents": "worry about pain, injury or PE; physical symptoms of anxiety; avoidance of activities or of school. Treat anxiety with the usual approaches; pain and anxiety feed each other, so address both."},
  {"name": "AUTISM AND ADHD",
   "rate": "association reported in several studies (e.g. Csecs et al., 2022) — rate not stated here, check",
   "presents": "sensory sensitivity, fidgeting and movement seeking, difficulty with sitting still — which can also reflect discomfort. Assess each through its usual route; do not let hypermobility explain away, or be explained away by, neurodevelopmental needs."},
  {"name": "CHRONIC PAIN AND FATIGUE",
   "rate": "common in symptomatic presentations — rate not stated here, check",
   "presents": "tired by midday, sore hands after writing, knee or back pain, reduced concentration late in the day, 'boom and bust' activity. Needs pacing, rest breaks and medical / physio management; mood effects are common."},
  {"name": "SCHOOL ATTENDANCE DIFFICULTY (EBSA)",
   "rate": "not stated here — check",
   "presents": "absences for appointments, flare-ups and fatigue, which then become anxiety about returning and catching up. Distinguish medical absence from anxiety-based avoidance; often both. See the EBSA entry."},
  {"name": "DIZZINESS ON STANDING, GUT AND SLEEP PROBLEMS",
   "rate": "reported in some people with hEDS / HSD — rate not stated here, check",
   "presents": "light-headedness, fainting, nausea, abdominal pain, poor sleep, fatigue. All medical questions — note them and ask whether the GP or paediatrician knows; they affect concentration and attendance."},
  {"name": "LOW MOOD",
   "rate": "not stated here — check",
   "presents": "withdrawal and loss of interest, often linked to pain, missed activities and friendships, and feeling disbelieved. Screen gently; follow the usual route, including the same-day route for any self-harm or suicidal talk."},
 ],

 "recommendations": [
  "WRITE THE FUNCTIONAL IMPACT, NOT THE DIAGNOSIS: 'Hand pain after about [x] minutes of writing; fatigue by early afternoon; avoids PE when knees are sore; missed [n] days this term.' That is what a school can act on.",
  "HANDWRITING: reduce copying; accept typed or scribed work for extended tasks; allow rest breaks; try pencil grips and wider pens as advised by OT; consider a laptop with keyboard skills training; check sitting posture, chair and table height. Measure speed and comfort (e.g. DASH) and record pain as well as speed.",
  "STATE EXAMS: where handwriting is slow or painful, gather evidence early for Reasonable Accommodations (RACE) — e.g. word processor, rest breaks — in line with current SEC criteria. Check the current SEC scheme and deadlines before advising.",
  "PE AND MOVEMENT: follow the physiotherapist's plan; adapt rather than exclude; avoid pushing joints to end of range; allow warm-up, alternative activities and rest; include the child in team activities where possible.",
  "PACING AND FATIGUE: plan the timetable to spread demanding tasks; allow movement breaks and a place to rest; send reduced homework on flare-up days; agree a flexible plan for mornings after bad nights.",
  "ANXIETY AND PAIN TOGETHER: teach and model calm responses to pain; support graded return to feared activities in line with physio advice; use CBT-informed anxiety work where anxiety is significant; avoid both dismissing pain and catastrophising about it.",
  "ATTENDANCE: a return-to-school and catch-up plan for absences; prioritise essential content; a named adult; distinguish medical absence from anxiety-based avoidance and address both.",
  "CONTINUUM LEVEL: usually Classroom Support or School Support; School Support Plus where OT / physio / paediatrics are actively involved or where anxiety or attendance are significant. Name the level and say why.",
  "REFER: GP (and through them paediatrics / paediatric rheumatology) for diagnosis and medical symptoms; Primary Care physiotherapy and OT for joint protection, strengthening, handwriting and equipment; CDNT only if complex needs meet criteria; CAMHS via GP for significant anxiety or low mood; Tusla for any child protection concern.",
  "DO NOT diagnose HSD, carry out a Beighton score yourself, advise on exercise programmes, splints or medication, or attribute anxiety, autism or ADHD to hypermobility.",
 ],

 "explain_parent": [
  "'Hypermobility just means her joints are more bendy than most. Lots of children are like that and have no problems. When it comes with pain and tiredness, doctors may call it hypermobility spectrum disorder. That's a medical diagnosis — the physio and doctor lead on it.'",
  "'My part is how it affects school: writing, tiredness, PE and how she's feeling about it all. Let's work out what's hardest in the school day.'",
  "'The research shows that children with hypermobility report anxiety a bit more often than others. That doesn't mean one causes the other, and it doesn't mean her pain isn't real. We'll look at both.'",
  "'The physio's advice is usually to keep moving and get stronger, with changes to protect her joints — not to stop everything. I'd like the school to follow that plan so PE is adapted rather than dropped.'",
  "SIGNPOST: GP and physiotherapy for medical questions; the treating team for information on HSD / hEDS; reliable international sources such as The Ehlers-Danlos Society, and UK charity information (e.g. the Hypermobility Syndromes Association) — check for current Irish support groups and remind families that online information varies in quality.",
 ],

 "explain_teacher": [
  "'Her joints are loose and they get sore and tired, especially her hands. Writing for long periods hurts. Please give her breaks, reduce copying and let her type longer pieces.'",
  "'Tiredness is part of this. She may be fine at 9 and drained by 1. Put the hardest work early where you can, and don't read afternoon slumps as laziness.'",
  "'For PE, the physio says adapt, don't exclude. She can warm up, skip high-impact bits on sore days and stay part of the team.'",
  "'If she says it hurts, believe her and give her the agreed options — rest, a different task, a quick break. Keep calm and matter-of-fact; big reactions can make pain and worry worse.'",
  "'Let me know if she's missing more days, avoiding things she used to enjoy, or seems down. Pain and worry can build on each other.'",
 ],

 "explain_child": [
  "YOUNGER: 'Your joints are extra bendy — like a rubber band that stretches a lot. That's why your hands get tired when you write lots. We're going to find ways to make writing easier for you.'",
  "OLDER: 'Your joints have more give than most people's, so your muscles work harder to keep them steady. That's why you get sore and tired. The physio helps make the muscles stronger; school's job is to make the day manageable.'",
  "'Tell us when it hurts — you won't get in trouble and you're not making a fuss. Let's agree a signal you can use in class.'",
  "QUESTIONS TO ASK: 'Which part of the school day is hardest for your body?' 'What happens when you're sore?' 'What helps?' 'Is there anything you've stopped doing that you miss?' 'Do you worry about it?'",
  "FOR ADOLESCENTS: involve them in their own plan and exam accommodations; ask how they want it explained to classmates, if at all.",
 ],

 "analogies": [
  "THE LOOSE TENT: 'Her joints are like a tent with slack guy-ropes — the tent still stands, but the poles (her muscles) have to work harder to hold it up, and they tire.' Good for teachers and parents.",
  "THE PHONE BATTERY: 'She starts the day with a battery that drains faster than other children's. Rest breaks and pacing are like a charger.' Good for fatigue and pacing with children and teachers.",
  "THE SMOKE AND THE ALARM: 'Pain is real, and worry can turn up the volume on the alarm. We help both — look after the body and calm the alarm.' Good for explaining the pain–anxiety link without dismissing pain.",
  "CAUTION: avoid 'double-jointed' (inaccurate) and 'fragile' or 'made of glass' images — they increase fear and inactivity.",
 ],

 "language": [
  "Use 'hypermobility spectrum disorder (HSD)' or 'hypermobile Ehlers-Danlos syndrome (hEDS)' only as given in the medical report, with its date and author. Older reports may say 'joint hypermobility syndrome' — note the change in terms (Castori et al., 2017).",
  "Use 'joint hypermobility' or 'hypermobile joints' for the physical trait; avoid 'double-jointed'.",
  "Describe symptoms in the child's words ('my hands go achy') alongside functional description.",
  "Avoid 'attention-seeking', 'fussy', 'lazy' or 'fake' for pain and fatigue behaviour — in writing and in meetings.",
  "Community language varies (some people prefer 'zebra', 'bendy', 'hypermobile'); ask the young person what they want used.",
 ],

 "red_flags": [
  "RED FLAG — a hot, swollen or very painful joint, fever, night pain, weight loss or a limp that does not settle. These are not typical of HSD — medical referral via GP promptly.",
  "RED FLAG — unexplained bruising or injuries, or an account that does not fit. A diagnosis of hypermobility or EDS does not remove the Children First duty: a mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty. Act first, then bring it to supervision.",
  "RED FLAG — fainting, collapse or chest pain in school. Emergency first aid and medical follow-up — not an EP matter, but ask whether the school has a health plan.",
  "RED FLAG — low mood, hopelessness, self-harm or suicidal talk in a young person with chronic pain. Same-day risk route: supervisor the same day, parents unless that increases risk, GP / CAMHS, emergency services if imminent.",
  "BOUNDARY — you do not diagnose HSD, score joint range or advise on exercise, splints, diet or medication. You describe educational impact and refer (PSI 2.2.2).",
  "WATCH — rising absence with a shrinking life (friends, hobbies, sport dropped). The combination of pain, fatigue and anxiety can spiral; early joint planning with health professionals matters.",
 ],

 "child_voice": [
  "BODY MAP OR PAIN DIARY — the child colours where it hurts and when, across a week. Good because it gives the child a concrete way to show pain and shows patterns (after writing, after PE, afternoons).",
  "ENERGY OR 'SPOON' DIARY FOR OLDER PUPILS — rating energy across the day. Good because it makes fatigue visible and supports pacing decisions the young person owns.",
  "SOLUTION-FOCUSED INTERVIEW — 'on a good day, what's different?' Good because it moves from symptoms to what already helps and gives the child agency.",
  "SCALING QUESTIONS ON PAIN, WORRY AND COPING — good because they separate the three and show which is driving avoidance.",
  "INVOLVING THE YOUNG PERSON IN THE PLAN AND IN RACE DECISIONS — good because adolescents are more likely to use supports they helped choose.",
 ],

 "questions": [
  "Q: 'Does she have a disability?' — A: 'Hypermobility itself is common and often not a problem. When it causes pain and tiredness that affect her day, it can count as a disability for reasonable accommodations. What matters for school is what she needs, and we can write that down.'",
  "Q: 'Should she stop PE?' — A: 'The usual advice is to keep moving and get stronger, with changes to protect her joints — stopping altogether can make things worse. The physio should set the limits. I'd like the school to adapt PE to their plan.'",
  "Q: 'Is her anxiety caused by the hypermobility?' — A: 'Studies do find anxiety more often in people with hypermobility, but no one can say one causes the other in her. Pain and worry feed each other, so we'll help both. The anxiety deserves support in its own right.'",
  "Q: 'Could this be why he's so clumsy? We were told he might have dyspraxia.' — A: 'Possibly part of it — loose joints make control harder. Dyspraxia (DCD) is a different thing that can occur alongside. The OT is best placed to tease them apart, and the supports overlap a lot.'",
  "Q: 'Can he get extra time or a laptop in the Junior Cert / Leaving Cert?' — A: 'If handwriting is slow or painful, he may be eligible for reasonable accommodations — but the criteria and deadlines are set by the SEC and change. Let's gather evidence early — speed, pain, what he uses in class — and the school can check the current scheme.'",
  "Q (teacher): 'She was fine yesterday — is she just avoiding work?' — A: 'Symptoms really do fluctuate day to day. The agreed plan should cover good and bad days, so you don't have to decide each time whether she's genuine. If avoidance is growing, let's look at anxiety too.'",
  "Q: 'We read online it's Ehlers-Danlos — should we push for testing?' — A: 'That's a question for your GP or the paediatrician — they decide what investigations are needed. I can write down how it affects her at school, which helps them.'",
 ],

 "supervision": [
  "Ask how your service handles referrals where the medical picture is unclear — pain, fatigue and anxiety with a 'possible hypermobility' label — and where the EP role starts and stops.",
  "Bring a case where handwriting difficulty was attributed to DCD, hypermobility or effort, and discuss how you would gather evidence without overstepping into OT assessment.",
  "Discuss how to write about research associations (anxiety, autism, ADHD) without implying causation.",
  "Ask about RACE evidence: what your supervisor includes for a pupil with slow or painful handwriting, and when in the school year.",
  "Bring any case with unexplained injuries or a concern about fabricated or induced illness, and confirm the Children First action taken before formulating.",
 ],

 "reflection": [
  "ON BOUNDARY — Did I describe educational impact, or did I drift into diagnosing or giving physio-style advice?",
  "ON BELIEF — Did the child and family feel believed about pain and fatigue? Did my language imply 'it's anxiety' as a way of dismissing pain?",
  "ON CAUSATION — Did I write any research association as if it applied to this child?",
  "ON INCLUSION — Did my recommendations keep the child in PE, sport and friendships, or remove them?",
  "ON THE WHOLE DAY — Did I look at the afternoon, homework and mornings after a bad night, or only the lesson I observed?",
  "WHAT GOOD LOOKS LIKE: 'I recorded that hand pain begins after about ten minutes of writing (pupil pain diary; OT report dated …), recommended typed extended work and early RACE evidence, and wrote: \"Research reports an association between hypermobility and anxiety (Bulbena et al., 2017); her anxiety is addressed below in its own right.\"'",
  "WHAT POOR LOOKS LIKE: 'Hypermobile, therefore anxious. Excused from PE and written work.' — causation assumed, inclusion removed and no functional description.",
 ],

 "citations": [
  "Castori, M., Tinkle, B., Levy, H., Grahame, R., Malfait, F., & Hakim, A. (2017). A framework for the classification of joint hypermobility and related conditions. American Journal of Medical Genetics Part C, 175(1), 148–157.",
  "Malfait, F., Francomano, C., Byers, P., et al. (2017). The 2017 international classification of the Ehlers–Danlos syndromes. American Journal of Medical Genetics Part C, 175(1), 8–26.",
  "Tofts, L. J., Simmonds, J., Schwartz, S. B., et al. (2023). Pediatric joint hypermobility: A diagnostic framework and narrative review. Orphanet Journal of Rare Diseases, 18, 104. (Check details before quoting.)",
  "Engelbert, R. H. H., Juul-Kristensen, B., Pacey, V., et al. (2017). The evidence-based rationale for physical therapy treatment of children, adolescents, and adults diagnosed with joint hypermobility syndrome/hypermobile Ehlers Danlos syndrome. American Journal of Medical Genetics Part C, 175(1), 158–167.",
  "Kirby, A., & Davies, R. (2007). Developmental coordination disorder and joint hypermobility syndrome — overlapping disorders? Implications for research and clinical practice. Child: Care, Health and Development, 33(5), 513–519.",
  "Bulbena, A., Baeza-Velasco, C., Bulbena-Cabré, A., et al. (2017). Psychiatric and psychological aspects in the Ehlers–Danlos syndromes. American Journal of Medical Genetics Part C, 175(1), 237–245.",
  "Csecs, J. L. L., Iodice, V., Rae, C. L., et al. (2022). Joint hypermobility links neurodivergence to dysautonomia and pain. Frontiers in Psychiatry, 12, 786916. (Check details before quoting.)",
  "Beighton, P., Solomon, L., & Soskolne, C. L. (1973). Articular mobility in an African population. Annals of the Rheumatic Diseases, 32(5), 413–418.",
 ],

 "pathway": {
  "age": "Joint hypermobility may be noticed at any age, but diagnosis of HSD or hEDS is usually made later — often in late childhood or adolescence — because hypermobility is normal in young children and symptoms (pain, fatigue, injuries) typically increase around puberty, with growth, sport and exam-year writing loads. Diagnosis in pre-pubertal children is contested (Tofts et al., 2023).",
  "who_diagnoses": "Ireland: GP, paediatrician, paediatric rheumatology (national service at Children's Health Ireland — check current arrangements), sometimes clinical genetics where another EDS type or connective tissue disorder is considered. Physiotherapists often identify hypermobility and refer back. Not the EP, not NEPS, not the CDNT as a rule.",
  "who_wrote_report": "GP or paediatric letter; rheumatology clinic letter; Primary Care or private physiotherapy report (may include a Beighton score); OT report on handwriting, grip and equipment; occasionally a genetics letter. Private reports vary in which criteria they used — check the classification and the date.",
  "refer_to": "GP (and through them paediatrics / rheumatology) for diagnosis and new symptoms; Primary Care physiotherapy for strengthening and activity advice; OT for handwriting, grip, posture and equipment; CAMHS via GP for significant anxiety or low mood; SEC reasonable accommodations process (via school) for state exams; Tusla for any child protection concern.",
  "sooner": "'Hypermobility is really common in children and usually causes no problems, so it's often only recognised once the pain and tiredness start to affect things. You noticed and asked. The helpful part now is getting the school day to fit how her body works.'",
 },

 "differential": [
  "DCD (DYSPRAXIA) — a motor-planning disorder; may co-occur; OT / physio distinguish.",
  "OTHER CONNECTIVE TISSUE OR GENETIC CONDITIONS (other EDS types, Marfan syndrome and others) — medical and genetic assessment.",
  "INFLAMMATORY OR OTHER JOINT CONDITIONS (e.g. juvenile idiopathic arthritis) — swollen, hot or stiff joints, morning stiffness; urgent medical review.",
  "ANXIETY OR SOMATIC SYMPTOM PRESENTATIONS — pain and fatigue driven mainly by distress; can co-exist with hypermobility; assessment by health professionals.",
  "LOW MUSCLE TONE (hypotonia) in the context of another neurological or genetic condition — medical assessment.",
  "EFFORT OR MOTIVATION EXPLANATIONS — rarely the whole story; check pain, fatigue and handwriting mechanics before accepting them.",
 ],

 "next": [
  "Read the medical, physio and OT reports: which classification was used, when, and what they advise for school (PE, handwriting, equipment).",
  "Describe function: writing speed and comfort, fatigue across the day, PE participation, attendance, mood — ideally with the child's own diary.",
  "Agree school adjustments (handwriting, PE, pacing, rest) aligned with the physio and OT plan; start RACE evidence early at post-primary.",
  "Screen for anxiety, low mood and attendance difficulty; refer via GP if significant.",
  "Review each term, and after any flare-up, injury or change of school.",
 ],

 "presentations": [
  "Handwriting difficulty — speed, legibility and comfort",
  "Fatigue and stamina needs",
  "Chronic pain affecting school participation",
  "Clumsiness, falls and PE participation",
  "Anxiety linked to physical symptoms",
  "School attendance difficulty linked to health",
  "Reasonable accommodations evidence for state exams",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — hypermobility is normal in many young children; HSD / hEDS is seldom diagnosed at this age",
   "prevalence": "Joint hypermobility common in young children; diagnostic rates not established — check.",
   "see": "A young child who is 'floppy', tires on walks, falls often, sits in W-position, or is late with fine-motor skills. Physiotherapy or OT may be involved. The EP role is limited: note fatigue and motor needs in pre-school and school-entry planning; do not treat 'bendy' as a diagnosis.",
   "tools": [],
  },
  "School Age": {
   "applies": "YES — handwriting, fatigue and PE issues emerge as demands rise",
   "prevalence": "Rate not stated here — check; varies with age, sex and Beighton threshold.",
   "see": "Slow or painful handwriting, sore hands, knees or back, tiredness by afternoon, avoiding PE or yard games, clumsiness, and sometimes worry about pain or injury. Referral may come as 'handwriting', 'DCD query' or 'anxiety'. Describe function, seek OT / physio input, adapt the school day.",
   "tools": ["DCD-Q", "Movement ABC-2", "Beery VMI", "DASH", "SDQ", "RCADS", "Beighton score — AGE: any; administered by physio / doctor · MEASURES: joint range at nine sites (0–9) · CANNOT TELL YOU: diagnosis, pain, fatigue or function · TIME: about 5 min"],
  },
  "Adolescent": {
   "applies": "YES — the band where diagnosis is most often made and where exam and attendance issues peak",
   "prevalence": "Rate not stated here — check; symptomatic presentations reported more often in girls.",
   "see": "Pain and fatigue with growth, sport and exam-year writing loads; subluxations or sprains; absences; anxiety and low mood; dizziness on standing in some. Key EP work: RACE evidence, attendance and return plans, anxiety support, pacing, and keeping the young person involved in activities and friendships.",
   "tools": ["DASH", "Access arrangements evidence (RACE)", "RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2"],
  },
  "Young Adult": {
   "applies": "YES — transition to adult health services and further / higher education supports",
   "prevalence": "Rate not stated here — check.",
   "see": "Managing pain and fatigue independently; transition from paediatric to adult services; disability supports in further and higher education (e.g. access services — check current schemes); DASH-17+ for handwriting speed evidence where needed.",
   "tools": ["DASH-17+", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — hypermobility and low tone are common in some groups (e.g. Down syndrome) and may affect posture, mobility and self-care",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Ligamentous laxity and low tone within a wider disability profile, affecting seating, positioning, handwriting or AAC access, toileting and mobility. Pain may be communicated through behaviour. Ask the physio and OT for positioning and handling plans; consider pain whenever behaviour changes.",
   "tools": ["Vineland-3 / ABAS-3", "Functional behaviour assessment (ABC)", "Communication Matrix / AAC review"],
  },
 },
},

# =====================================================================================
# 3. GENDER DYSPHORIA IN CHILDREN AND ADOLESCENTS
# =====================================================================================
{
 "name": "Gender dysphoria in children and adolescents",
 "code": "DSM-5-TR Gender Dysphoria in Children (F64.2) · Gender Dysphoria in Adolescents and Adults (F64.0 in DSM-5-TR; F64.1 in DSM-5, 2013 — check) · ICD-11 HA61 Gender incongruence of childhood · HA60 Gender incongruence of adolescence or adulthood — in Chapter 17 'Conditions related to sexual health', OUTSIDE the mental, behavioural and neurodevelopmental disorders chapter",
 "neps": "4. SOCIAL (4.2 Relationships with adults) — and 3. EMOTIONAL (3.4 Mood · 3.2 Anxiety) where distress is present · 3.7 Risk and safeguarding where there is self-harm, suicidal ideation or harm at home",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · Equal Status Acts 2000–2018 (gender ground) · Gender Recognition Act 2015 · Education Act 1998 · GDPR (special-category data) · Department of Education Cineáltas (2022) and Bí Cineálta procedures (2024) — check current versions",

 "what_it_is": [
  "TERMS FIRST. GENDER IDENTITY is a person's inner sense of their gender. GENDER INCONGRUENCE is a mismatch between that identity and the sex recorded at birth. GENDER DYSPHORIA (DSM-5-TR) is the DISTRESS or impairment that can accompany that incongruence (APA, 2022). Many transgender and gender-diverse people do not have, or no longer have, gender dysphoria. Being trans or gender-questioning is not in itself a disorder.",
  "DSM-5-TR, CHILDREN: a marked incongruence between experienced / expressed gender and assigned gender, lasting at least 6 months, shown by at least SIX of eight indicators, one of which MUST be a strong desire to be of another gender or an insistence that one is; the others concern clothing, fantasy play, toys and activities, playmates, rejection of typical toys and activities, dislike of one's sexual anatomy and desire for the sex characteristics of the experienced gender. Plus clinically significant distress or impairment (APA, 2022 — check exact wording).",
  "DSM-5-TR, ADOLESCENTS AND ADULTS: at least 6 months' incongruence shown by at least TWO of six indicators (e.g. incongruence with one's sex characteristics, a strong desire to be rid of them or to have those of another gender, to be of or be treated as another gender, a conviction of having that gender's typical feelings), plus clinically significant distress or impairment (APA, 2022). DSM-5-TR updated its language, e.g. 'experienced gender' and 'gender-affirming' treatment — check the text.",
  "ICD-11 (WHO, 2019; in effect from 01/01/2022) moved the category OUT of mental disorders into 'Conditions related to sexual health', renamed it GENDER INCONGRUENCE, and does not require distress. HA61 (childhood) applies to pre-pubertal children with marked incongruence persisting about two years, and states that gender-variant behaviour and preferences alone are not a basis for the diagnosis; HA60 covers adolescence and adulthood — check exact criteria before quoting. The move reflects a view that the diagnosis is kept to support access to health care, not because gender diversity is a mental illness.",
  "EVIDENCE IS CONTESTED AND CHANGING. The Independent Review of Gender Identity Services for Children and Young People (Cass, 2024; final report April 2024, England) concluded that the evidence base for medical interventions in young people is weak, recommended holistic assessment of the whole young person, and described social transition as an active intervention rather than a neutral act. The review's methods and conclusions have also been criticised (e.g. McNamara et al., 2024) and international guidelines differ (e.g. WPATH Standards of Care 8; Coleman et al., 2022). Know that this is contested; do not take sides in front of a family; check for updates.",
  "OUTCOMES FOR YOUNGER CHILDREN VARY. Older clinic studies reported that many pre-pubertal children with gender dysphoria did not continue to experience it in adolescence (e.g. Steensma et al., 2013); those studies have been criticised on methodological grounds (Temple Newhook et al., 2018). No one can predict an individual child's path — which is exactly why the EP does not assess or forecast gender identity.",
  "THE EP ROLE IN ONE LINE: wellbeing, belonging, safety and learning — anti-bullying, inclusion, school guidance and signposting, and the same-day risk route when needed. NOT assessment of gender identity, NOT a view on whether a child 'is' trans, and NOT advice on social or medical transition (PSI 2.2.2).",
  "IRISH CONTEXT: HSE provision for under-18s has been limited and has been under review, particularly since the Cass Review and the closure in 2024 of the Tavistock GIDS in England, to which Irish children were historically referred. The HSE National Gender Service works with adults. Check the current HSE model of care and referral route (via GP) before saying anything to a family. Legal gender recognition: the Gender Recognition Act 2015 allows 16–17-year-olds to apply with a court order; under-16s cannot — check current law.",
 ],

 "what_it_is_not": [
  "NOT THE SAME AS BEING TRANSGENDER OR GENDER-DIVERSE. Gender dysphoria is a clinical term for distress. Many trans young people are well and thriving when safe and supported. Do not use 'gender dysphoria' as a synonym for a child's identity.",
  "NOT GENDER-NONCONFORMING PLAY OR APPEARANCE. A boy who loves dresses, a girl who wants short hair and plays football — this is common, and ICD-11 explicitly says gender-variant behaviour alone is not a basis for diagnosis (WHO, 2019). Do not pathologise it.",
  "NOT SEXUAL ORIENTATION. Gender identity is who you are; sexual orientation is who you are attracted to. They are separate, though often confused by adults.",
  "NOT A CHILD PROTECTION CONCERN IN ITSELF. A child exploring gender is not a safeguarding matter. Harm, abuse, rejection or threats at home or online, self-harm and suicidal ideation ARE — and follow Children First and the risk route like any other.",
  "NOT SOMETHING THE EP ASSESSES, CONFIRMS OR RULES OUT. There is no psychometric test of gender identity; do not administer one, and do not write a view on whether the child 'is really' trans. That belongs, where needed, to specialist health services.",
  "NOT A SINGLE-EXPLANATION STORY. Neither 'all his distress is because he's trans' nor 'it's just the autism / trauma / a phase' is a formulation. Hold the whole young person — identity, mental health, neurodevelopment, relationships, experiences — as the Cass Review (2024) and others recommend.",
  "NOT A SCHOOL POLICY DECISION FOR THE EP. Names, pronouns, uniforms, toilets, changing rooms and sports are decided by the school under its policies, the law and with parents. The EP can help the school think about wellbeing and inclusion; the decisions are the school's and the family's.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR prevalence estimates are drawn from specialist-clinic data and are widely regarded as underestimates — check the text before quoting any figure (APA, 2022). Population surveys asking about gender identity give higher and more variable figures depending on the question — rate not stated here, check.",
  "REFERRALS: referrals of young people to specialist gender services in England rose sharply from the mid-2010s, with a shift from mostly birth-registered males in childhood to mostly birth-registered females in adolescence (de Graaf et al., 2018; Cass, 2024). Reasons are debated — do not quote a single explanation.",
  "IRELAND: no Irish population prevalence figure is stated here — check. Irish surveys of LGBTQI+ young people (Higgins et al., 2016; Higgins et al., 2024) report high rates of distress, self-harm and bullying among trans and non-binary respondents — check figures before quoting.",
  "SEX RATIO: in current adolescent referrals, birth-registered females outnumber birth-registered males (de Graaf et al., 2018; Cass, 2024) — ratio not stated here, check.",
  "CO-OCCURRING DIFFICULTIES: elevated rates of anxiety, depression, self-harm and autism are consistently reported among gender-diverse young people and clinic populations (Warrier et al., 2020; Cass, 2024) — figures vary by study; check before quoting.",
 ],

 "cooccurring": [
  {"name": "ANXIETY AND DEPRESSION",
   "rate": "elevated in clinic and community samples (Cass, 2024; Higgins et al., 2016) — rate not stated here, check",
   "presents": "withdrawal, low mood, avoidance of school, PE, changing rooms or social situations; irritability; sleep problems. Minority stress (Meyer, 2003; Hendricks & Testa, 2012) and co-occurring difficulties both contribute. Support and refer through the usual route; do not attribute all distress to gender or all gender-related feeling to distress."},
  {"name": "SELF-HARM AND SUICIDAL IDEATION",
   "rate": "elevated — Irish survey data report high rates among trans young people (Higgins et al., 2016; 2024) — check figures before quoting",
   "presents": "disclosure, marks, hopelessness, talk of not being here. SAME-DAY RISK ROUTE: supervisor the same day, parents unless that would increase risk, GP / CAMHS, emergency services or ED if imminent; Tusla where there is a child protection concern."},
  {"name": "AUTISM",
   "rate": "elevated rates of autism and autistic traits reported in gender-diverse people (Warrier et al., 2020) — rate not stated here, check",
   "presents": "a young person who may describe gender in direct or detailed ways, with sensory and social differences. Autism does not invalidate gender identity, and gender identity does not explain autistic traits. Assess each through its own route; adapt communication."},
  {"name": "BULLYING AND VICTIMISATION",
   "rate": "high rates reported in Irish school-climate and LGBTQI+ surveys — check before quoting",
   "presents": "name-calling, deliberate misgendering, exclusion, online abuse, avoidance of toilets and changing rooms, falling attendance. Identity-based bullying is named in Cineáltas (Department of Education, 2022) — the school's anti-bullying procedures apply."},
  {"name": "EATING DIFFICULTIES",
   "rate": "reported as elevated in some studies — rate not stated here, check",
   "presents": "restriction or change in eating linked to body distress, weight or shape, or suppressing puberty-related changes. Medical and CAMHS referral via GP; weight loss or physical signs are urgent."},
  {"name": "TRAUMA AND ADVERSE EXPERIENCES",
   "rate": "reported as elevated — rate not stated here, check",
   "presents": "hypervigilance, avoidance, relationship difficulties; experiences may include rejection, harassment or abuse. Do not assume trauma explains identity, and do not overlook trauma because identity is the referral focus. Children First for any current harm."},
  {"name": "ADHD",
   "rate": "reported as elevated in some clinic samples — rate not stated here, check",
   "presents": "attention and organisation difficulties that interact with stress and absence. Assess through the usual route."},
  {"name": "FAMILY CONFLICT OR RELATIONAL STRESS",
   "rate": "common in clinical accounts — rate not stated here, check",
   "presents": "disagreement between parents, or between parents and young person, about identity, names or next steps; siblings affected. Family acceptance is associated with better outcomes in LGBT young people (Ryan et al., 2010). Signpost family support; stay neutral on decisions."},
 ],

 "recommendations": [
  "FRAME THE REFERRAL AS WELLBEING AND INCLUSION: 'The referral concerns [young person]'s wellbeing, safety and participation in school.' Describe mood, anxiety, attendance, relationships, bullying and learning — not gender identity itself.",
  "SAFETY FIRST, EVERY TIME: ask about self-harm and suicidal thoughts directly and sensitively in any consultation where distress is present; if present, the same-day risk route before anything else. Record what was asked and the action taken.",
  "ANTI-BULLYING: recommend that the school applies its anti-bullying procedures (Cineáltas 2022; Bí Cineálta 2024 — check current versions) to identity-based and online bullying, records incidents, and reviews supervision of unstructured times, toilets and changing areas.",
  "A TRUSTED ADULT AND A SAFE SPACE: a named staff member the young person chooses, regular brief check-ins, and a quiet space. Belonging and one good adult are protective across the literature on young people's mental health.",
  "PRACTICAL INCLUSION WITHIN SCHOOL POLICY: help the school think through PE, changing, toilets, uniform, trips and residentials in a way that protects dignity, privacy and safety for all pupils — decisions made by the school with the young person and parents, under school policy and legal advice, and in light of current guidance (check for any Department of Education guidance and the Cass Review, 2024).",
  "PARENTS: recommend that the school follows its policies and the law on involving parents; parents are usually central partners. Where a young person does not want parents told, do not promise confidentiality; consider age, maturity, welfare and risk; take advice from the principal / DLP and your supervisor. If there is a risk of harm at home, follow Children First.",
  "MENTAL HEALTH SUPPORT: where distress is significant, recommend referral via GP to CAMHS or Primary Care Psychology for assessment of mental health; school-based wellbeing work (e.g. SPHE, guidance counsellor, NEPS-supported approaches) in parallel. Name co-occurring needs (autism, ADHD, learning) and route each through its usual pathway.",
  "CONTINUUM LEVEL: Classroom Support (whole-school inclusion, anti-bullying, SPHE / RSE) for most; School Support where a plan with a key adult and check-ins is needed; School Support Plus where CAMHS or other services are involved or distress is significant. Name the level and say why.",
  "REFER: GP (for any health question, including referral to HSE gender services — check current route); CAMHS / Primary Care Psychology via GP for mental-health difficulty; Tusla for any child protection concern; signpost Irish support organisations for young people and families (e.g. BeLonG To for LGBTQ+ youth; TENI; Jigsaw for youth mental health) — check current services.",
  "DO NOT assess, confirm or question gender identity; do not advise for or against social transition, puberty blockers, hormones or any medical step; do not give opinions on whether identity is 'a phase', 'caused by' anything, or 'real'; do not disclose identity to others without a lawful and considered basis.",
 ],

 "explain_parent": [
  "'I'm here because the school is concerned about how [young person] is doing — mood, friendships, feeling safe. My job is to help with that. It's not my job to decide anything about gender identity, and I won't be assessing that.'",
  "'You might be feeling all sorts of things — worry, confusion, protectiveness. That's normal. What we know helps young people's mental health is feeling safe, having adults who listen, and not being bullied.'",
  "'Questions about health care or next steps are for your GP, who can advise on current HSE services. The guidance in this area has been changing — including a big review in England in 2024 — so please get current advice rather than relying on what you read online.'",
  "'Whatever happens with gender, the things I'd like us to focus on in school are the same: is she safe, is she coping, is she learning, does she have people.'",
  "'If you're ever worried about her safety — self-harm or talk of not wanting to be here — that's the same day: GP, out-of-hours, or the emergency department.'",
  "SIGNPOST: GP; CAMHS via GP if needed; family support through Irish LGBTQ+ organisations (e.g. BeLonG To, TENI — check current parent supports); Jigsaw; Samaritans (116 123) or text services for crisis support — check current numbers.",
 ],

 "explain_teacher": [
  "'Our focus is wellbeing and safety in school — the same as for any pupil who is struggling. You don't need to be an expert on gender; you need to be a calm, reliable adult.'",
  "'Challenge bullying and deliberate hurtful comments the way you would any identity-based bullying, and record it under the school's procedures.'",
  "'Decisions about names, pronouns, uniform, toilets and PE are for the school, with the young person and parents, under school policy. If you're unsure what's agreed, ask the principal rather than improvising.'",
  "'Watch for withdrawal, avoiding PE or toilets, missing school, marks or talk of self-harm. If you see or hear anything about self-harm, tell the DLP the same day — and remember, as a mandated person, telling the DLP doesn't discharge your own duty where it applies.'",
  "'Keep what you're told private. Don't share a pupil's gender identity with other staff or pupils unless there's a clear, agreed reason.'",
 ],

 "explain_child": [
  "YOUNGER: 'I'm here to find out how school is going for you — what's good, what's hard, and who helps.' Follow the child's lead; use their words. Do not introduce gender topics the child has not raised.",
  "YOUNGER, IF THE CHILD RAISES IT: 'Thank you for telling me. It's OK to feel how you feel and to talk about it. Is there anything at school that makes it hard?' Keep it about their experience and safety.",
  "OLDER: 'I'm not here to decide anything about your identity. I'm here because people care how you're doing — are you OK, do you feel safe, is anyone giving you a hard time?'",
  "OLDER — ON CONFIDENTIALITY, BEFORE THEY SAY MUCH: 'Most of what you tell me stays between us and the people who need it to help you. If I'm worried about your safety, I'll have to tell someone — and I'd talk to you first about who and how.'",
  "QUESTIONS TO ASK: 'What would make school feel safer?' 'Who is someone you trust here?' 'What name would you like me to use when we talk?' 'How have you been sleeping and feeling lately?' 'Have you ever felt so bad you thought about hurting yourself?'",
 ],

 "analogies": [
  "THE UMBRELLA, NOT THE WEATHER: 'We're not here to argue about the weather. We're making sure she has an umbrella — safety, friends, a trusted adult — whatever the weather does.' Good with staff and parents who want the EP to take a position.",
  "THE WHOLE JIGSAW: 'Gender is one piece of the jigsaw. We're looking at all the pieces — mood, friendships, learning, home, school — not just one.' Good for explaining holistic, non-single-explanation formulation.",
  "THE THERMOMETER: 'Distress is the temperature we're measuring and working to bring down. We don't need to know every cause to act to keep her safe and well.' Good for focusing a meeting on wellbeing and risk.",
  "CAUTION: avoid analogies that imply identity is a phase, a trend, an illness or a 'wrong body' unless the young person uses that language themselves.",
 ],

 "language": [
  "In direct work, ask the young person what name and pronouns they would like used with you; how they are recorded in school records and reports follows school policy, parental involvement and legal advice — agree the approach with your supervisor before writing.",
  "Use 'transgender', 'trans', 'non-binary', 'gender-questioning' or 'gender-diverse' as the young person does. Use 'gender dysphoria' only for the clinical diagnosis where one has been made, with its source and date.",
  "Say 'sex registered at birth' or 'assigned sex at birth' rather than 'biological boy / girl' in professional writing; DSM-5-TR uses 'assigned gender' and 'experienced gender' (APA, 2022).",
  "Avoid 'a phase', 'confused', 'lifestyle', 'choice', 'social contagion' or 'transgenderism' as descriptions of a young person — whatever the debate, they are not neutral and can hurt.",
  "Avoid 'deadnaming' in conversation where the young person has asked otherwise; where official records must use a legal name, explain that neutrally.",
 ],

 "red_flags": [
  "RED FLAG — self-harm, suicidal ideation, a plan or recent attempt. SAME-DAY RISK ROUTE: supervisor the same day, parents unless that would increase risk, GP / CAMHS, emergency services or ED if imminent; do not leave the young person alone if risk is imminent. Supervision follows action; it does not replace it.",
  "RED FLAG — abuse, threats, rejection, being put out of home, or coercion (including online exploitation). Follow Children First: a mandated person reports to Tusla as soon as practicable; telling the DLP does not discharge that duty.",
  "RED FLAG — marked weight loss, restrictive eating or physical signs of an eating difficulty. Urgent referral via GP.",
  "RED FLAG — accessing medication or hormones outside medical care (e.g. online). A physical health risk — inform parents unless that would increase risk, and GP the same day; discuss with supervisor.",
  "BOUNDARY — you do not assess or confirm gender identity, and you do not advise on social or medical transition, puberty blockers or hormones. You describe wellbeing, support inclusion and refer (PSI 2.2.2).",
  "BOUNDARY — do not let your own views, in any direction, shape the report. If you notice strong feelings, bring them to supervision.",
  "WATCH — falling attendance, avoidance of PE, toilets or changing rooms, and withdrawal from friends: early signs of bullying or distress.",
 ],

 "child_voice": [
  "SOLUTION-FOCUSED INTERVIEW — 'what would a better week at school look like?' Good because it focuses on what the young person wants from school, not on their identity, and builds agency.",
  "SCALING QUESTIONS FOR SAFETY, MOOD AND BELONGING — good because they give a quick, repeatable picture and open the door to asking about self-harm.",
  "SCHOOL MAP / SAFE AND UNSAFE PLACES — the young person marks where they feel safe and unsafe. Good because it locates bullying and avoidance (toilets, corridors, changing rooms) concretely.",
  "LETTING THE YOUNG PERSON CHOOSE HOW TO BE DESCRIBED IN THE REPORT — good because it respects their voice; balance it with school policy and parental involvement, and agree it with your supervisor.",
  "STANDARDISED SELF-REPORT FOR MOOD AND ANXIETY (e.g. RCADS, MFQ) — good because they measure distress, which is the EP's legitimate focus, not identity.",
 ],

 "questions": [
  "Q (parent): 'Do you think my child is really trans?' — A: 'That's not something I assess, and I don't think anyone can answer it from the outside. What I can do is help make sure she's safe and coping at school. For health questions, your GP is the starting point.'",
  "Q (parent): 'Should we let him change his name at school?' — A: 'That's a decision for you, him and the school, under the school's policy. The guidance has been changing, including the Cass Review in 2024, which called social transition an active step that deserves careful thought. I'm not in a position to advise for or against — but I can help the school focus on his wellbeing whatever is decided.'",
  "Q (teacher): 'She's asked us not to tell her parents she's using a different name. What do we do?' — A: 'Don't promise secrecy. Bring it to the principal, who will apply the school's policy and take advice. Think about her age, maturity, welfare and any risk at home. If there's a safety concern, Children First applies. Let's make sure she knows who she can talk to in the meantime.'",
  "Q (teacher): 'Isn't this just social media / a phase?' — A: 'People hold strong views on why referrals have increased, and the research isn't settled. For us, it doesn't change the job: this young person is distressed, and we help with that, stop any bullying, and keep her safe.'",
  "Q (young person): 'Are you going to tell my parents?' — A: 'I won't share things without talking to you first, unless I'm worried about your safety — then I'd have to. Parents are usually part of helping, and I can help you think about how and when to talk to them.'",
  "Q (principal): 'Can you write a report saying which toilet she should use?' — A: 'That's a school policy decision, not a psychological one. I can describe her wellbeing, her anxiety about particular spaces and what would help her feel safe, and the school can weigh that alongside its duties to all pupils and legal advice.'",
  "Q (parent): 'Are there services in Ireland?' — A: 'HSE services for young people in this area have been under review, so I'd ask your GP what the current route is — I don't want to give you out-of-date information. If there are mental-health concerns, CAMHS through the GP is the route for those.'",
 ],

 "supervision": [
  "Bring your own views and feelings about gender identity, in whatever direction, and how they might shape your questions, your report or your tone.",
  "Ask how your service handles referrals where gender identity is mentioned: what the EP role is, what it is not, and what current guidance the service follows (with dates).",
  "Discuss confidentiality and parental involvement: what you would do if a young person asks you not to tell parents, and how that differs from a disclosure of risk.",
  "Rehearse the risk conversation: how you ask about self-harm and suicidal thoughts, and the same-day actions you would take.",
  "Bring any report draft that mentions gender and check the language, the naming decision and whether anything strays outside the EP role.",
 ],

 "reflection": [
  "ON MY ROLE — Did I stay with wellbeing, safety, inclusion and learning? Did anything I said or wrote amount to assessing identity or advising on transition?",
  "ON BALANCE — Did I present contested evidence as settled, in either direction? Did I cite current guidance with its date and note that it may change?",
  "ON THE WHOLE PERSON — Did I avoid explaining all distress by gender, or explaining away gender by another diagnosis?",
  "ON SAFETY — Did I ask about self-harm and suicidal thoughts? If a risk emerged, did I act the same day before reflecting?",
  "ON VOICE AND DIGNITY — Did the young person feel heard and respected? How did I handle names and pronouns in the room and on paper, and did I agree that approach with my supervisor?",
  "WHAT GOOD LOOKS LIKE: 'I framed the referral around low mood and attendance, asked about self-harm (none reported; safety plan agreed and supervisor informed), recommended anti-bullying action on corridor incidents and a named key adult, and signposted the GP for health questions. I noted that guidance in this area changed in 2024 and should be checked.'",
  "WHAT POOR LOOKS LIKE: 'Presents with gender dysphoria, likely secondary to autism; recommend social transition be avoided.' — a diagnosis the EP cannot make, a causal claim and advice outside the role.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Gender Dysphoria.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — HA60 Gender incongruence of adolescence or adulthood; HA61 Gender incongruence of childhood. https://icd.who.int/",
  "Cass, H. (2024). Independent review of gender identity services for children and young people: Final report. NHS England. (April 2024 — check for subsequent implementation updates.)",
  "Coleman, E., Radix, A. E., Bouman, W. P., et al. (2022). Standards of care for the health of transgender and gender diverse people, version 8. International Journal of Transgender Health, 23(Suppl. 1), S1–S259.",
  "McNamara, M., Baker, K., Connelly, K., et al. (2024). An evidence-based critique of 'The Cass Review' on gender-affirming care for adolescent gender dysphoria. Yale School of Medicine Integrity Project. (Check details and status before quoting.)",
  "Steensma, T. D., McGuire, J. K., Kreukels, B. P. C., Beekman, A. J., & Cohen-Kettenis, P. T. (2013). Factors associated with desistence and persistence of childhood gender dysphoria: A quantitative follow-up study. Journal of the American Academy of Child & Adolescent Psychiatry, 52(6), 582–590.",
  "Temple Newhook, J., Pyne, J., Winters, K., et al. (2018). A critical commentary on follow-up studies and 'desistance' theories about transgender and gender-nonconforming children. International Journal of Transgenderism, 19(2), 212–224.",
  "Warrier, V., Greenberg, D. M., Weir, E., et al. (2020). Elevated rates of autism, other neurodevelopmental and psychiatric diagnoses, and autistic traits in transgender and gender-diverse individuals. Nature Communications, 11, 3959.",
  "de Graaf, N. M., Carmichael, P., Steensma, T. D., & Zucker, K. J. (2018). Evidence for a change in the sex ratio of children referred for gender dysphoria: Data from the Gender Identity Development Service in London (2000–2017). Journal of Sexual Medicine, 15(10), 1381–1383.",
  "Meyer, I. H. (2003). Prejudice, social stress, and mental health in lesbian, gay, and bisexual populations: Conceptual issues and research evidence. Psychological Bulletin, 129(5), 674–697.",
  "Hendricks, M. L., & Testa, R. J. (2012). A conceptual framework for clinical work with transgender and gender nonconforming clients: An adaptation of the Minority Stress Model. Professional Psychology: Research and Practice, 43(5), 460–467.",
  "Higgins, A., Doyle, L., Downes, C., et al. (2016). The LGBTIreland report: National study of the mental health and wellbeing of lesbian, gay, bisexual, transgender and intersex people in Ireland. GLEN and BeLonG To. (Also: Being LGBTQI+ in Ireland, 2024 — check details.)",
  "Ryan, C., Russell, S. T., Huebner, D., Diaz, R., & Sanchez, J. (2010). Family acceptance in adolescence and the health of LGBT young adults. Journal of Child and Adolescent Psychiatric Nursing, 23(4), 205–213.",
  "Department of Education. (2022). Cineáltas: Action plan on bullying. Government of Ireland. — and Department of Education. (2024). Bí Cineálta: Procedures to prevent and address bullying behaviour for primary and post-primary schools. (Check current versions.)",
 ],

 "pathway": {
  "age": "Gender-diverse feelings or expression may be noticed in early childhood; many referrals to specialist services now occur in early to mid-adolescence, often around puberty, when body changes can intensify distress (de Graaf et al., 2018; Cass, 2024). The EP usually meets it through a referral for mood, anxiety, attendance or bullying rather than for gender itself.",
  "who_diagnoses": "Ireland: a diagnosis of gender dysphoria / gender incongruence is made, where needed, by specialist health services — for under-18s via GP referral to HSE services (current model of care under review — check), or historically through referral abroad. Psychiatry (including CAMHS) may assess co-occurring mental-health needs. Not the EP, not NEPS, not the school.",
  "who_wrote_report": "A specialist gender service or clinician; a CAMHS or private psychiatry / psychology report addressing mental health; a GP letter. Many young people you meet will have no report at all — and none is needed for the school to support wellbeing and prevent bullying. Check the date and the service; practice has changed quickly.",
  "refer_to": "GP (health questions, including current HSE gender service route); CAMHS or Primary Care Psychology via GP for mental-health difficulty; same-day risk route for self-harm or suicidal ideation; Tusla for any child protection concern; signpost BeLonG To, TENI and Jigsaw for support (check current services).",
  "sooner": "'There's no \"should\" here. Young people talk about this when they're ready, and families take time to understand. What matters now is that she's safe, supported and able to get on with school — and that's what we're focusing on.'",
 },

 "differential": [
  "GENDER-NONCONFORMING EXPRESSION OR PLAY without distress or incongruence — common and not a clinical matter (WHO, 2019).",
  "DISTRESS WITH OTHER DRIVERS (depression, anxiety, trauma, bullying, body-image difficulties) — may co-exist with gender questioning; each needs its own attention.",
  "BODY DYSMORPHIC DISORDER OR EATING DISORDER — body-focused distress with different content; clinical assessment.",
  "AUTISM — may co-occur; does not invalidate identity; assess separately.",
  "ADOLESCENT IDENTITY EXPLORATION more broadly — exploration is developmentally normal; the EP does not need to categorise it.",
 ],

 "next": [
  "Ask about safety first; if self-harm or suicidal ideation is present, the same-day risk route before anything else.",
  "Frame the work around wellbeing, bullying, attendance and learning, and agree the approach to names and records with your supervisor.",
  "Recommend anti-bullying action, a trusted adult and practical inclusion within school policy, with parents involved per policy and law.",
  "Refer for mental-health support via GP where needed; signpost health questions to the GP and support organisations.",
  "Check current guidance (HSE, Department of Education, Cass Review implementation) before any meeting — note the date you checked.",
 ],

 "presentations": [
  "LGBTQ+ identity support",
  "Low mood and withdrawal",
  "Anxiety about PE, toilets and changing rooms",
  "Identity-based bullying",
  "School attendance difficulty",
  "Self-harm and suicidal ideation — same-day risk route",
  "Family conflict and relational stress",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — DSM-5-TR childhood criteria can apply, but EP involvement at this age is rare and gender-diverse play is common",
   "prevalence": "Rate not stated here — check; gender-nonconforming play is common and is not in itself a diagnosis.",
   "see": "A young child who insists on being another gender or strongly prefers the clothes, toys and roles associated with another gender. Families may seek reassurance. The EP role is limited to wellbeing and inclusion in the setting; do not pathologise play and do not predict outcomes. Health questions go to the GP.",
   "tools": ["SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — ICD-11 childhood category applies to pre-pubertal children; EP involvement is usually about wellbeing or bullying",
   "prevalence": "Rate not stated here — check.",
   "see": "A child whose gender expression or statements draw attention from peers or adults; possible teasing, exclusion, anxiety about toilets or PE, and family uncertainty. Focus on safety, friendships, bullying and a trusted adult. Decisions about names or presentation are for the family and the school under policy; current guidance (Cass, 2024) urges particular care with pre-pubertal children — check.",
   "tools": ["SDQ", "RCADS", "Piers-Harris 3"],
  },
  "Adolescent": {
   "applies": "YES — the most common band for referral and for co-occurring distress",
   "prevalence": "Rate not stated here — check; referral numbers rose from the mid-2010s, mostly birth-registered females (de Graaf et al., 2018).",
   "see": "Distress linked to puberty and body changes, social pressure and bullying, avoidance of PE and changing rooms, attendance problems, and elevated anxiety, low mood and self-harm. Ask about risk directly. Support wellbeing and inclusion, involve parents per policy and law, refer mental-health concerns via GP, and signpost health questions to the GP.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Beck Youth Inventories-2", "BASC-3 SRP", "SDQ"],
  },
  "Young Adult": {
   "applies": "YES — DSM-5-TR adolescent / adult criteria; transition to adult services",
   "prevalence": "Rate not stated here — check.",
   "see": "Transition from school to further or higher education, work and adult health services (HSE National Gender Service for adults — check current route). Legal gender recognition possible from 18 without court order (Gender Recognition Act 2015 — check). EP involvement is rare; if it occurs, it concerns wellbeing, study supports and signposting.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — including autistic young people and those with intellectual disability",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "A young person in a special class or school, often autistic, raising gender-related feelings, sometimes with communication differences that make it harder to express. Adapt communication, take their views seriously, support wellbeing and safety, and involve parents and the wider team; capacity and consent questions go to supervision and the treating health team.",
   "tools": ["SDQ", "Communication Matrix / AAC review"],
  },
 },
},

]
