# PRES batch 7 — descriptive (non-diagnostic) presentations, Part I rows.
# Context: Reference Part D (rows 507–650), column N, under 5. OTHER.
#   5.3 Medical condition or other diagnosis — items 1–6 (all five bands)
#   5.4 Concerns about early development   — items 7–11 (Early Years, School Age retrospectively, Special Setting;
#                                             Part D has no 5.4 row at Adolescent or Young Adult)
#   5.5 Involvement of other services       — items 12–20 (all five bands)
# Part D, column O (who they are referred to) and column P (what you would do at this age) are
# reflected in the "assess" and "recommendations" fields.

N53 = "5. OTHER (5.3 Medical condition or other diagnosis)"
N54 = "5. OTHER (5.4 Concerns about early development)"
N55 = "5. OTHER (5.5 Involvement of other services)"

PRES = []

# ---------------------------------------------------------------- 1
PRES.append({
 "name": "Multiple disabilities",
 "neps": N53,
 "related_to": ["Cerebral palsy", "Genetic syndromes (Down, Fragile X, 22q11.2, Williams, Prader-Willi, Angelman, Rett)", "Intellectual Disability", "Epilepsy", "Visual impairment", "Hearing impairment", "Autism"],
 "what_it_is": [
  "A description of a child who has two or more significant impairments at once — for example a physical disability with a learning disability and a sensory loss — where the COMBINATION produces needs greater than any one condition alone. Part D files it under 5.3 as 'Medical': it is a description of the profile, not a diagnosis in its own right.",
  "At the severe end it overlaps with 'profound and multiple learning disabilities' (PMLD). Bellamy et al. (2010) found no single agreed definition of PMLD and proposed one built on profound intellectual disability plus additional sensory, physical or health needs and very early communication — useful when a report uses the term loosely.",
  "The educational question is rarely 'what is the child's IQ?'. It is: how does the child communicate, what can they perceive, how do they move and are they comfortable, how alert are they across the day, and what does learning look like for them. Imray and Hinchcliffe (2014) argue for curricula built on those questions rather than on a scaled-down mainstream curriculum.",
  "Care is almost always multi-disciplinary: CDNT (psychology, SLT, OT, physiotherapy, social work), paediatrics or neurology, nursing, the Visiting Teacher service for sensory loss, and the school team. The CDNT is usually the lead service; NEPS input is typically consultation on the school programme (Part D, 5.3).",
 ],
 "what_it_is_not": [
  "NOT a reason to skip assessment of the individual. Two children with 'CP and a learning disability' can differ completely in communication, vision, alertness and preferences. Describe this child, not the label.",
  "NOT the same as 'untestable'. Standardised cognitive tests are usually inappropriate, but structured observation, adaptive behaviour measures and communication profiling give a real, usable description. 'Could not be assessed' in a report usually means the wrong tool was chosen.",
  "NOT an automatic special-school placement. Placement is decided with parents and the NCSE (SENO) on the child's needs and the supports available locally — describe needs, do not prescribe a setting in your report.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: usually identified early through neonatal, paediatric and CDNT pathways. NEPS rarely leads; your contribution is often consultation on preschool or early intervention class programmes, and later on school placement planning with the SENO.",
  "SCHOOL AGE 6–12: most children are in special schools or special classes, some in mainstream with SNA and nursing support. Questions to you are about communication, behaviour that may signal pain or distress, and whether the programme matches the child's learning stage.",
  "ADOLESCENT 13–16: puberty, growth and health changes (seizure patterns, orthopaedic surgery, weight, positioning) can change alertness and comfort; review programmes when health changes rather than assuming a plateau.",
  "YOUNG ADULT / SPECIAL SETTING: school ends at 18 (check the current age-out rules for special schools); planning for adult day services through the HSE should start several years earlier. Part D (5.3 Special Setting) points to the care plan in the setting, nursing support and staff training needs.",
 ],
 "assess": [
  "READ FIRST: every CDNT, paediatric, vision, hearing and nursing report on file, with consent. Note which services are active so you do not duplicate (Part D, 5.5). Ask for the seizure plan and positioning or feeding plan if they exist.",
  "OBSERVE across the day and across people: alertness, how the child signals yes/no, like/dislike, pain and interest; what they attend to; what the adult does that works. A communication profile (Communication Matrix / AAC review — Part G) is more useful here than a cognitive test.",
  "ADAPTIVE BEHAVIOUR: Vineland-3 or ABAS-3 from parent and staff (Part G), interpreted with care — floor effects are common, so item-level description matters more than the standard score.",
  "ASK what the child's day is like at home: sleep, medication times, feeding, seizures. A child who is post-ictal or sedated in the morning is not showing you their learning.",
 ],
 "recommendations": [
  "SCHOOL SUPPORT PLUS: a single integrated plan that names each discipline's input (SLT communication targets, OT and physio positioning, nursing care, teacher curriculum targets) so the child does not have five separate plans pulling in different directions.",
  "Write a COMMUNICATION PASSPORT — how the child says yes, no, more, stop, pain and 'I like this' — so every adult, including substitutes and SNAs, responds the same way.",
  "Schedule demanding learning at the child's most alert times, and record alertness over a fortnight to find them; build rest and position changes in (OT/physio advice).",
  "Set targets in small, observable steps with a record of progress — e.g. 'anticipates the song routine by smiling before the first line on 4 of 5 occasions' — and review each term.",
  "REFER / LIAISE: CDNT for team input; SENO about resources and placement; Visiting Teacher service for vision or hearing; GP or paediatrics for any change in health. Staff training needs identified through casework should be named explicitly.",
  "DO NOT write 'untestable' or 'functioning at an age equivalent of X months' as a summary — it tells staff nothing and can shape expectations.",
 ],
 "explain_parent": [
  "'You know better than anyone how she tells you things. I'd like to learn that from you, so school can respond in the same way.'",
  "'I won't be giving her an IQ test — it wouldn't be fair or useful. I'll watch her across the day and talk with you and her team to describe how she learns best.'",
  "SIGNPOST: the CDNT key worker or team lead; the SENO for school resources; parent groups for specific syndromes where relevant.",
 ],
 "explain_teacher": [
  "'Start with how he communicates yes and no, and whether everyone reads it the same way. That's the foundation for everything else in the programme.'",
  "'If he seems switched off, check the obvious first — position, pain, tiredness, medication time, a seizure earlier — before deciding it's disengagement.'",
  "'Small steps count. Write down what you see him do, even if it's a look or a change in breathing — that's the evidence of learning here.'",
 ],
 "explain_child": [
  "Where the child has limited verbal understanding, 'explaining' means showing: use their objects of reference, photos, signing or their AAC system to show who you are and what you are doing.",
  "OLDER, with more understanding: 'I'm Anna. I'm here to find out what helps you learn and what you like at school. You can tell me with your talker, or by looking.'",
  "ASK (through their system): what they like, what they don't like, who helps. Record the child's own responses verbatim or described precisely in the report.",
 ],
 "red_flags": [
  "RED FLAG — a change in behaviour (crying, self-injury, withdrawal, new sleepiness) in a child who cannot say what is wrong: pain, illness, seizure change or medication change first. Ask parents and nurse to seek a medical review via GP or paediatrics.",
  "RED FLAG — children with disabilities are at greater risk of abuse and may not be able to disclose (Children First, 2017). Unexplained injuries, fearfulness of a particular person or care routine: follow Children First procedures and report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "BOUNDARY — you do not diagnose the conditions or advise on medication, feeding or positioning. Describe what you see and route it to the right discipline (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'What's her IQ?' A: 'For children with her profile an IQ test wouldn't give a fair or useful answer. I'd rather describe what she understands, how she communicates and how she learns, which is what the school programme needs.'",
  "Q: 'Will he ever talk?' A: 'I can't predict that, and neither can a test. What I can say is how he communicates now, and that his SLT is the right person to talk about the next steps in communication.'",
  "Q: 'Should she be in a special school?' A: 'That's a decision for you with the SENO, based on her needs and what's available. My report will describe her needs clearly so that decision is well informed.'",
  "Q: 'Who's in charge of her care?' A: 'The CDNT usually coordinates. Ask the team who her key worker is — that's the person to go to first.'",
 ],
 "supervision": [
  "Bring an observation of a child with multiple disabilities and ask your supervisor how they would write it up without an age equivalent or a standard score.",
  "Ask how the service divides roles with the CDNT for children in special schools, and when NEPS input is appropriate.",
  "Reflect on your own expectations: what did you assume the child could not do, and were you right?",
 ],
 "citations": [
  "Bellamy, G., Croot, L., Bush, A., Berry, H., & Smith, A. (2010). A study to define: Profound and multiple learning disabilities (PMLD). Journal of Intellectual Disabilities, 14(3), 221–235.",
  "Imray, P., & Hinchcliffe, V. (2014). Curricula for teaching children and young people with severe or profound and multiple learning difficulties. Routledge.",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
  "Rowland, C. (2004). Communication Matrix. Oregon Health & Science University. (Check for the current online edition.)",
 ],
})

# ---------------------------------------------------------------- 2
PRES.append({
 "name": "Chronic illness affecting school",
 "neps": N53,
 "related_to": ["Epilepsy", "Sleep disorders", "Feeding and eating disorders", "Somatic Symptom Disorder / Illness Anxiety / Conversion Disorder", "Adjustment Disorder", "Anxiety"],
 "what_it_is": [
  "A description of how a long-term physical health condition — for example type 1 diabetes, asthma, epilepsy, cystic fibrosis, inflammatory bowel disease, juvenile arthritis, sickle cell disease, or a cancer in treatment — is affecting attendance, energy, learning, peer relationships or wellbeing at school.",
  "The illness is diagnosed and managed by medicine; the EP's question is educational impact. Part D (5.3, School Age) is explicit: 'impact on school day (fatigue, medication timing, absence) · your role is educational impact, not diagnosis.'",
  "Effects work through several routes at once: direct (the condition or treatment affects the brain, energy or concentration), indirect (absence, missed teaching, fatigue), and psychosocial (anxiety, peer difference, family stress). Lum et al. (2017), in a meta-review, describe school experience as shaped by academic, social and emotional factors together.",
  "Children with chronic physical illness show somewhat raised rates of internalising difficulty on average (Pinquart & Shen, 2011) — effect sizes vary by condition, so check before quoting a figure. Many cope well; the point is to look, not to assume.",
 ],
 "what_it_is_not": [
  "NOT a learning difficulty by default. Low attainment may reflect missed teaching rather than a learning problem; establish what the child has actually been taught before interpreting test scores.",
  "NOT 'attention-seeking' or school avoidance when symptoms fluctuate. Many conditions are variable by nature. Where anxiety about symptoms is also present, both can be true at once — describe both.",
  "NOT only the nurse's or the parents' business. The school has a role in inclusion, reasonable accommodation (Equal Status Acts 2000–2018) and the Continuum of Support.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: management sits mainly with parents and preschool staff; questions are about safe inclusion in the preschool (AIM may be relevant) and preparing the primary school for enrolment.",
  "SCHOOL AGE 6–12: the child increasingly notices difference (blood tests, inhalers, special diet, missing school tours). Watch for attendance patterns, fatigue in the afternoon and peer questions.",
  "ADOLESCENT 13–16: self-management shifts from parents to the young person, and adherence often dips in adolescence; exam accommodations (RACE) and subject choice may need planning (Part D, 5.3 Adolescent).",
  "YOUNG ADULT 17–26: transfer from paediatric to adult health services and into further or higher education; disability supports (the Fund for Students with Disabilities; DARE) may be relevant — check current eligibility. SPECIAL SETTING: care plan and nursing support within the setting.",
 ],
 "assess": [
  "GET THE MEDICAL PICTURE with consent: a letter or report from the treating team describing the condition, treatment, known cognitive or energy effects and any restrictions. Do not rely on second-hand accounts.",
  "MAP THE SCHOOL DAY: attendance record (by day and by term), times of symptoms, medication times, periods of reduced timetable. A simple week grid with the teacher shows where the impact falls.",
  "ESTABLISH TEACHING MISSED before interpreting attainment. Compare attainment with what has been taught; a curriculum-based measure of recent work is often more informative than a standardised test.",
  "ASK THE CHILD about their illness at school — what they want peers to know, what is hard, what helps — and screen wellbeing with a brief measure where indicated (SDQ; RCADS for older children — Part G).",
 ],
 "recommendations": [
  "SCHOOL SUPPORT: an individual healthcare plan agreed with parents and the treating team (who does what, emergency steps, medication times), linked to the Student Support File so educational and health plans do not contradict each other. Check your school's own policy on administration of medicines.",
  "SCHOOL SUPPORT: a catch-up plan for missed work — prioritised essentials rather than everything — with a named teacher to coordinate, and work sent home during absence where the child is well enough.",
  "CLASSROOM SUPPORT: discreet arrangements for symptoms (toilet pass, water, snacks, rest, exit card) agreed with the child so they are not having to ask in front of peers.",
  "Plan for peer understanding only with the child's and parents' agreement — some children want the class told, others do not.",
  "REFER / LIAISE: treating team or paediatric liaison for medical questions; home tuition where absence is prolonged (Department of Education scheme — check current terms); Primary Care psychology or CAMHS if anxiety or low mood is significant.",
  "DO NOT recommend reducing expectations across the board. Adjust access and pacing, keep the learning goals.",
 ],
 "explain_parent": [
  "'My job isn't about the illness itself — your medical team handles that. I'm looking at how it affects his day at school and what school can do about it.'",
  "'Some of what looks like a learning gap is simply teaching he missed while he was unwell. We'll separate that out before drawing any conclusions.'",
  "SIGNPOST: the condition-specific charity where one exists; the treating team's nurse specialist; the school's healthcare plan process.",
 ],
 "explain_teacher": [
  "'When she's pale and quiet after lunch, that's likely the condition, not disengagement. Plan lighter tasks for that slot where you can.'",
  "'Keep a short record of days she's unwell in class — it helps the medical team and stops the picture relying on memory.'",
  "'Missed work: prioritise the three things she must have for the next topic, not everything the class did.'",
 ],
 "explain_child": [
  "YOUNGER: 'Your body needs extra looking after, and sometimes that makes school tiring or means you miss days. I want to help school make it easier for you.'",
  "OLDER: 'You know your condition better than most adults at school. What do you want teachers to know, and what do you want kept private?'",
  "ASK: 'What's the hardest bit of school when you're not feeling well?' and 'What do you wish teachers did?'",
 ],
 "red_flags": [
  "RED FLAG — signs of low mood, hopelessness or self-harm in a young person with a long-term condition: follow the same-day risk route; do not treat it as 'understandable given the illness'.",
  "RED FLAG — a sudden change in cognition, behaviour or alertness: may be medical (e.g. hypoglycaemia, seizure activity, treatment effect). Ask parents to contact the treating team promptly.",
  "BOUNDARY — you do not interpret medical results, change medical plans or advise on medication (PSI 2.2.2). Route questions to the treating team.",
 ],
 "questions": [
  "Q: 'Will his illness affect his learning long-term?' A: 'That depends on the condition and treatment, and the medical team is best placed to say. What I can do is look at how he's learning now and make sure missed teaching is caught up.'",
  "Q: 'Should the class be told?' A: 'Only if she wants that, and in the way she wants. Some children find it a relief; others want privacy. Ask her first.'",
  "Q: 'Can he get home tuition?' A: 'There is a Department of Education home tuition scheme for pupils who can't attend because of a medical condition. Eligibility and application go through the school — check the current circular.'",
 ],
 "supervision": [
  "Bring a case where you were unsure whether low attainment was a learning difficulty or missed teaching, and how you separated them.",
  "Ask how the service liaises with paediatric teams, and what consent is needed to request a medical report.",
  "Reflect on how the family's stress about the illness showed up in your meeting with them.",
 ],
 "citations": [
  "Lum, A., Wakefield, C. E., Donnan, B., Burns, M. A., Fardell, J. E., & Marshall, G. M. (2017). Understanding the school experience of children and adolescents with serious chronic illness: A systematic meta-review. Child: Care, Health and Development, 43(5), 645–662.",
  "Pinquart, M., & Shen, Y. (2011). Behavior problems in children and adolescents with chronic physical illness: A meta-analysis. Journal of Pediatric Psychology, 36(9), 1003–1016.",
  "Shaw, S. R., & McCabe, P. C. (2008). Hospital-to-school transition for children with chronic illness: Meeting the new challenges of an evolving health care system. Psychology in the Schools, 45(1), 74–87.",
  "Equal Status Acts 2000–2018 (Ireland).",
 ],
})

# ---------------------------------------------------------------- 3
PRES.append({
 "name": "Fatigue and stamina needs",
 "neps": N53,
 "related_to": ["Cerebral palsy", "Acquired brain injury", "Epilepsy", "Muscular dystrophy", "Sleep disorders", "Hypermobility spectrum disorder"],
 "what_it_is": [
  "A description of a child whose physical or mental energy runs out before the school day does — work quality drops across the day or week, the child needs recovery time after exertion, and symptoms are worse after PE, busy days or illness.",
  "Fatigue can be PHYSICAL (effortful movement in cerebral palsy or muscular dystrophy), COGNITIVE (sustained effort after acquired brain injury, or in children who are working harder to compensate), or linked to sleep, pain, medication or a condition such as ME/CFS or long COVID.",
  "Part D places it under 5.3 alongside chronic illness and medication effects. It is a description of need, not a diagnosis; the cause is for medicine to establish, the pattern is for school to plan around.",
  "NICE (2021) guidance on ME/CFS emphasises energy management and warns against unmonitored graded increases in activity — relevant where that diagnosis is in play. Check for updates before citing it.",
 ],
 "what_it_is_not": [
  "NOT laziness or low motivation. The tell-tale sign is a pattern — good in the morning, falling off in the afternoon, worse on Fridays or after PE — rather than general reluctance.",
  "NOT simply 'tired from late nights'. Poor sleep is worth asking about, but a sleep hygiene leaflet is not the answer when the fatigue is part of a condition.",
  "NOT the same as inattention. A fatigued child may look inattentive late in the day; attention that is good when fresh points away from an attention difficulty.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: shown as irritability, crying, lying down, or reluctance to join physical play; preschool sessions may need to be shorter at first.",
  "SCHOOL AGE 6–12: handwriting deteriorates across a task; the child asks to sit out of yard; homework becomes a battle at home. The longer day in senior classes can expose it.",
  "ADOLESCENT 13–16: moving between classrooms, carrying bags, a longer timetable and extra-curricular pressure add load; exam sittings of several hours may need planning (RACE — check current criteria for rest breaks).",
  "YOUNG ADULT / SPECIAL SETTING: timetable and course load design; in special settings, fatigue affects alertness for learning and should shape when demanding work is scheduled.",
 ],
 "assess": [
  "PLOT THE PATTERN: an energy diary across two weeks (child, parent, teacher each rating morning, midday, afternoon) with notes on PE, illness and sleep. The pattern is the finding.",
  "SAMPLE WORK across the day: compare a morning and an afternoon piece of written work for length, legibility and accuracy.",
  "ASK ABOUT sleep, pain, medication times and after-school activities, and whether the medical team has named fatigue as part of the condition. A structured fatigue scale such as the PedsQL Multidimensional Fatigue Scale — AGE child and parent versions · MEASURES: general, sleep/rest and cognitive fatigue · CANNOT TELL YOU: the cause · TIME: about 5 min — can support description; check licensing.",
  "IN YOUR OWN SESSION: note when performance falls off and schedule tests with breaks; record this, because a score after 90 minutes may describe stamina rather than ability.",
 ],
 "recommendations": [
  "CLASSROOM SUPPORT: timetable demanding work (new learning, writing, maths) when the child is freshest, usually mornings; use lighter tasks for known low points.",
  "CLASSROOM SUPPORT: planned rest breaks the child can use without asking publicly (a card, a quiet space), and reduced output — scribe, typing, fewer questions showing the same skill.",
  "SCHOOL SUPPORT: a pacing plan agreed with the child, parents and OT or medical team — including PE participation, trips, homework volume and reduced timetable if advised — reviewed every half term.",
  "SCHOOL SUPPORT: at post-primary, reduce physical load (locker access, lift pass, one set of books at home) and plan exam arrangements early.",
  "REFER / LIAISE: GP or treating team for unexplained or worsening fatigue; OT for energy conservation and equipment; CDNT where part of a disability profile.",
  "DO NOT recommend increasing effort or 'building stamina' through pushing — increases should be planned with the treating team.",
 ],
 "explain_parent": [
  "'The pattern you've noticed — good mornings, hard afternoons — is exactly what we'll plan around. It's not about trying harder.'",
  "'An energy diary for two weeks helps us all see the pattern clearly and gives the medical team useful information too.'",
  "SIGNPOST: GP or treating team; OT via CDNT or Primary Care for energy management.",
 ],
 "explain_teacher": [
  "'Look at his morning work against his afternoon work — that difference is the fatigue. Put new learning in the morning.'",
  "'A rest card he can put on the desk saves him asking in front of everyone. Agree it with him first.'",
  "'Fewer questions that show the same skill is not lowering the bar — it's the same learning with less output.'",
 ],
 "explain_child": [
  "YOUNGER: 'Your body has a battery, and yours runs down faster than some people's. We're going to find ways to save battery at school.'",
  "OLDER: 'Some days you start with less energy and it runs out faster. Planning where you spend it is a skill — not giving up.' The spoon analogy (Miserandino, 2003) works well with teenagers.",
  "ASK: 'When in the day is it hardest?' and 'What helps you get your energy back?'",
 ],
 "red_flags": [
  "RED FLAG — new or worsening fatigue, weight loss, pallor, night sweats or loss of skills: medical review via GP promptly.",
  "RED FLAG — fatigue with low mood, withdrawal and loss of interest: consider depression and screen; follow the risk route if there are thoughts of self-harm.",
  "BOUNDARY — you do not diagnose ME/CFS, sleep disorders or any cause of fatigue, and do not advise on activity programmes the treating team has not agreed (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'He manages football at the weekend — how can he be too tired for school?' A: 'Energy gets spent on what's chosen and enjoyed, and there's often a crash afterwards. The diary will show what happens after the match, too.'",
  "Q: 'Should she be on a reduced timetable?' A: 'Sometimes, for a set period, with a plan to review. It should be agreed with the medical team and reviewed, not left open-ended.'",
  "Q: 'Will extra time in exams help?' A: 'For fatigue, rest breaks are often more useful than extra time. Check what the State Examinations Commission currently allows and apply early.'",
 ],
 "supervision": [
  "Bring an energy diary and discuss how to present the pattern in a report without over-interpreting it.",
  "Discuss how you decided whether a test result reflected ability or stamina, and how you wrote that caveat.",
  "Ask about the service's approach to reduced timetables and how they are reviewed.",
 ],
 "citations": [
  "National Institute for Health and Care Excellence. (2021). Myalgic encephalomyelitis (or encephalopathy)/chronic fatigue syndrome: Diagnosis and management (NICE guideline NG206). (Check for updates.)",
  "Miserandino, C. (2003). The spoon theory. But You Don't Look Sick. [Online essay.]",
  "Varni, J. W., Burwinkle, T. M., Katz, E. R., Meeske, K., & Dickinson, P. (2002). The PedsQL in pediatric cancer: Reliability and validity of the Pediatric Quality of Life Inventory Generic Core Scales, Multidimensional Fatigue Scale, and Cancer Module. Cancer, 94(7), 2090–2106.",
 ],
})

# ---------------------------------------------------------------- 4
PRES.append({
 "name": "Medication effects on attention and learning",
 "neps": N53,
 "related_to": ["ADHD", "Epilepsy", "Autism", "Anxiety", "Sleep disorders", "Tourette's Disorder"],
 "what_it_is": [
  "A description of changes in a child's attention, alertness, mood, appetite or behaviour at school that may be linked to prescribed medication — its timing, dose, starting, stopping or wearing off.",
  "Common examples the EP meets: stimulant medication for ADHD wearing off in the afternoon or suppressing appetite at lunch; anti-seizure medication associated with drowsiness or slowed processing (Loring & Meador, 2004); sedating antihistamines; steroids affecting mood and sleep; medication changes affecting a child's usual profile.",
  "Part D (5.3) lists it as 'Added' — not a diagnosis, but a factor that must be considered when describing attention and learning, and when interpreting test results.",
  "The EP's role is to NOTICE, DESCRIBE and COMMUNICATE — with consent — what school sees, so the prescriber has good information. The EP never advises on starting, stopping or changing medication (PSI 2.2.2).",
 ],
 "what_it_is_not": [
  "NOT something the EP evaluates or recommends. 'Consider a medication review' is the prescriber's decision; your report can say 'school has observed X in the afternoons; parents may wish to share this with the prescribing doctor'.",
  "NOT always the explanation. A child whose attention dips in the afternoon may be tired, hungry, or struggling with afternoon subjects. Hold the medication hypothesis alongside others.",
  "NOT a reason to test only when 'on' or only when 'off'. Record what the child had and when, and interpret accordingly.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: stimulant medication is rarely used at this age (NICE NG87, 2018: do not offer ADHD medication to any child under 5 without a second specialist opinion from an ADHD service with expertise in young children — check for updates); anti-seizure medication and other medications may be. Preschool staff notes on alertness are valuable.",
  "SCHOOL AGE 6–12: the most frequent referral window. Note whether a dose is given at school, who gives it, and whether lunch is eaten. Teacher observations by time of day are the key evidence.",
  "ADOLESCENT 13–16: adherence varies; some young people stop medication without telling anyone, or use it selectively for exams. Ask the young person directly and without judgement.",
  "YOUNG ADULT / SPECIAL SETTING: adult services take over prescribing; in special settings, multiple medications are common, and staff may be the best observers of side effects in pupils who cannot report them.",
 ],
 "assess": [
  "RECORD: current medications, doses and times (from parents, with consent), recent changes, and when the child had their last dose relative to your session. Put this in the report's background.",
  "TIME-OF-DAY OBSERVATION: observe or ask the teacher to rate attention and work output in morning and afternoon blocks over a week; a simple grid is enough.",
  "RATING SCALES: if using Conners-4 or BRIEF-2 (Part G), note whether raters see the child on or off medication — teachers may see only the medicated child, parents the unmedicated evenings.",
  "ASK THE CHILD what they notice: 'Does your medicine make school different? When does it wear off?'",
 ],
 "recommendations": [
  "CLASSROOM SUPPORT: schedule demanding work within the window in which the child is most alert, and plan lighter tasks for known dips — the same principle as fatigue planning.",
  "CLASSROOM SUPPORT: protect lunch — some children on stimulants eat little at midday; a snack at a later break may help (parents to discuss with prescriber).",
  "SCHOOL SUPPORT: a simple observation record, shared with parents, that they can take to the prescriber. School should follow its own policy on administration and storage of medicines.",
  "REPORT WORDING: 'Assessment took place at [time]; [child] had taken [medication as reported by parent] at [time].' Add an interpretation caveat where relevant.",
  "REFER: prescriber (GP, paediatrician, CAMHS or neurology) via the parents for any question about effects. Pharmacists can answer factual questions for parents.",
  "DO NOT write 'medication should be reviewed/increased/started' — it is outside the EP role.",
 ],
 "explain_parent": [
  "'I'm not able to advise on medication — that's for his doctor. But school can keep a record of what they see at different times of day, and that can help the doctor.'",
  "'Could you let me know what he takes and when, so I can make sense of what I see in the session?'",
  "SIGNPOST: the prescribing doctor; community pharmacist for factual questions.",
 ],
 "explain_teacher": [
  "'Write down what you see and when — morning versus afternoon. That's more useful to the doctor than a general impression.'",
  "'If you think it's the medication, say what you've seen to the parents; don't suggest changes to the dose.'",
  "'Put the hardest work where he's sharpest, and don't read an afternoon slump as him not trying.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some medicines help your body or brain, and sometimes they make you feel sleepy or not hungry. It's OK to tell a grown-up how you feel.'",
  "OLDER: 'You're the one who notices what it's like. If there's a time of day when things get harder, telling your parents and doctor helps them get it right for you.'",
  "ASK: 'Is school different on days you take it?' and 'Is there anything about it you'd like the doctor to know?'",
 ],
 "red_flags": [
  "RED FLAG — marked mood change, agitation, new tics, low mood or suicidal thoughts after a medication change: parents should contact the prescriber urgently; follow the same-day risk route for any self-harm risk.",
  "RED FLAG — signs that a young person is sharing or selling prescribed stimulants, or misusing medication: follow school policy and the child welfare route.",
  "BOUNDARY — you do not advise on medication (PSI 2.2.2). If a parent asks 'should he stay on it?', redirect to the prescriber.",
 ],
 "questions": [
  "Q: 'Do you think he needs medication?' A: 'That's not something I can advise on. I can describe what I see in school and what helps, and you can talk with his doctor about medication.'",
  "Q: 'Should I give it on test days?' A: 'That's a question for the prescribing doctor. I'd just ask that you let the school know, so we can interpret results fairly.'",
  "Q: 'Was the assessment affected by his medication?' A: 'I recorded what he'd taken and when, and I've noted in the report where that may have affected his performance.'",
 ],
 "supervision": [
  "Bring a report sentence you drafted about medication and check it stays within the EP role.",
  "Ask how to respond when a teacher or parent presses for your opinion on medication.",
  "Discuss how you would interpret rating scales when home and school see the child in different medication states.",
 ],
 "citations": [
  "Loring, D. W., & Meador, K. J. (2004). Cognitive side effects of antiepileptic drugs in children. Neurology, 62(6), 872–877.",
  "National Institute for Health and Care Excellence. (2018). Attention deficit hyperactivity disorder: Diagnosis and management (NICE guideline NG87). (Check for updates.)",
  "National Institute for Health and Care Excellence. (2022). Epilepsies in children, young people and adults (NICE guideline NG217). (Check for updates.)",
 ],
})

# ---------------------------------------------------------------- 5
PRES.append({
 "name": "Missed curriculum from hospital admissions",
 "neps": N53,
 "related_to": ["Epilepsy", "Acquired brain injury", "Feeding and eating disorders", "Cerebral palsy", "Spina bifida", "Muscular dystrophy"],
 "what_it_is": [
  "A description of gaps in a child's learning caused by time in hospital — repeated short admissions, one long admission, or frequent outpatient days — rather than by a learning difficulty.",
  "The gap is often uneven: cumulative subjects (maths, Irish, modern languages, reading at the early stages) suffer most, because each step depends on the one before; topic-based subjects can be picked up more easily.",
  "Some children attend a hospital school or receive teaching on the ward during admissions; what they covered may not match the class programme. Shaw and McCabe (2008) describe the hospital-to-school interface as a frequent point of breakdown.",
  "Part D (5.3) lists it as 'Added'. The EP's job is to separate 'not taught' from 'not learned', and to help the school plan a realistic catch-up.",
 ],
 "what_it_is_not": [
  "NOT evidence of a specific learning difficulty. Standardised attainment scores after long absence describe current attainment, not underlying ability to learn. A diagnosis of dyslexia or dyscalculia should not be made on that basis.",
  "NOT solved by 'catching up everything'. Trying to cover all missed work overwhelms a child who may also be tired and anxious.",
  "NOT only an academic issue: missed curriculum usually comes with missed friendships, routines and class identity.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: missed preschool time affects social and early language experience more than 'curriculum'; the transition to primary may need extra planning.",
  "SCHOOL AGE 6–12: gaps in foundational literacy and number are the priority; a child who missed the teaching of place value or phonics may appear to have a specific difficulty.",
  "ADOLESCENT 13–16: examination courses make gaps visible — Junior Cycle and Leaving Certificate coursework and classroom-based assessments may be affected; subject levels and choices may need review.",
  "YOUNG ADULT / SPECIAL SETTING: further and higher education institutions may allow deferral or adjusted timetables; in special settings, loss of skills during admission (not just missed teaching) may occur and should be reviewed.",
 ],
 "assess": [
  "BUILD THE ABSENCE TIMELINE: dates and length of admissions and outpatient days (from the school's attendance record and parents), matched against what the class was being taught at the time.",
  "ASK what teaching happened in hospital (ward or hospital school) and get a note of topics covered where possible.",
  "USE CURRICULUM-BASED ASSESSMENT first: what does the child know of the key topics in the current and previous year's programme? Standardised tests (WIAT-III UK — Part G) can quantify current attainment but should be interpreted against the timeline.",
  "LOOK FOR the child who was struggling BEFORE the admissions: earlier school reports and teacher knowledge help separate pre-existing difficulty from absence.",
 ],
 "recommendations": [
  "SCHOOL SUPPORT: a prioritised catch-up plan — identify the few foundational skills needed for current class work and teach those first, with a named teacher coordinating.",
  "SCHOOL SUPPORT: short, frequent targeted sessions (e.g. place value, phonics gaps) rather than long catch-up blocks; review progress each half term to check whether the gap is closing.",
  "CLASSROOM SUPPORT: pre-teach vocabulary and key ideas for the current topic so the child can take part in class learning now, rather than always working on the past.",
  "Liaise with the hospital school or home tuition teacher (with consent) so work is continuous across settings; send work home during admissions where the child is well enough.",
  "REFER / LIAISE: home tuition where absence is prolonged (Department of Education scheme — check current terms); treating team where cognitive effects of the condition or treatment are possible.",
  "DO NOT label the child with a specific learning difficulty until the gap has been taught and progress monitored.",
 ],
 "explain_parent": [
  "'A lot of what looks like difficulty is teaching she wasn't there for. We'll teach the key bits she missed and see how quickly she picks them up — that tells us a lot.'",
  "'We won't try to catch up everything. We'll focus on the building blocks she needs for what the class is doing now.'",
  "SIGNPOST: school principal about home tuition; the hospital school teacher, who can share what was covered.",
 ],
 "explain_teacher": [
  "'Check what he was taught before you decide what he can't do. His gap in fractions lines up exactly with his admission.'",
  "'Pick the three things he needs for this term's work and teach those first. Let the rest go for now.'",
  "'If he picks them up quickly once taught, that's the answer. If he doesn't, then we look further.'",
 ],
 "explain_child": [
  "YOUNGER: 'When you were in hospital, the class learned some things without you. That's not your fault. We'll help you learn the important bits.'",
  "OLDER: 'Your gaps are about time missed, not about how clever you are. We'll pick what matters most and not try to cram everything.'",
  "ASK: 'What was it like coming back?' and 'Which subjects feel like you missed the most?'",
 ],
 "red_flags": [
  "RED FLAG — a child who does not make progress even when the missed content is taught: consider a learning difficulty or cognitive effects of the condition/treatment, and liaise with the treating team.",
  "RED FLAG — withdrawal, low mood or refusal to return after admissions: screen for anxiety or depression and plan a supported return; follow the risk route if indicated.",
  "BOUNDARY — you do not comment on the medical necessity of admissions or on treatment. Describe educational impact only (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Is she dyslexic? Her reading is behind.' A: 'She missed a lot of the early reading teaching. Let's teach the gaps and see how she responds before we think about dyslexia.'",
  "Q: 'Should he repeat the year?' A: 'Repeating a year is a big decision with mixed evidence. Let's look first at a targeted catch-up plan and review how he's progressing. Check with the school and Department guidance.'",
  "Q: 'Can the hospital school tell us what she covered?' A: 'Yes, with your consent — that helps us avoid repeating or skipping things.'",
 ],
 "supervision": [
  "Bring an absence timeline alongside attainment scores and discuss how you would write the interpretation.",
  "Ask how the service links with hospital schools and home tuition teachers.",
  "Discuss when to reconsider a learning difficulty if catch-up teaching is not working.",
 ],
 "citations": [
  "Shaw, S. R., & McCabe, P. C. (2008). Hospital-to-school transition for children with chronic illness: Meeting the new challenges of an evolving health care system. Psychology in the Schools, 45(1), 74–87.",
  "Lum, A., Wakefield, C. E., Donnan, B., Burns, M. A., Fardell, J. E., & Marshall, G. M. (2017). Understanding the school experience of children and adolescents with serious chronic illness: A systematic meta-review. Child: Care, Health and Development, 43(5), 645–662.",
  "Department of Education. (current). Home Tuition Grant Scheme — check the current circular and terms.",
 ],
})

# ---------------------------------------------------------------- 6
PRES.append({
 "name": "Re-entry to school after illness",
 "neps": N53,
 "related_to": ["Acquired brain injury", "Epilepsy", "Feeding and eating disorders", "Separation Anxiety Disorder", "Adjustment Disorder", "Posttraumatic Stress Disorder"],
 "what_it_is": [
  "A description of the planned return of a child to school after a significant illness, injury, surgery or hospital stay — for example after cancer treatment, an acquired brain injury, major orthopaedic surgery, an inpatient eating disorder admission or a long period of illness at home.",
  "Return is a transition in its own right: the child may come back physically changed (hair loss, weight change, wheelchair, scars), with new cognitive or energy limits, with anxiety, and to a class whose friendships and routines have moved on.",
  "School re-integration programmes for children with cancer — preparing the child, the family, the teachers and the peers — have a supportive evidence base (Prevatt et al., 2000). After acquired brain injury, re-entry needs particular care because difficulties may only emerge as demands rise over the following months and years (Ylvisaker et al., 2001).",
  "Part D (5.3) lists it as 'Added'. The EP's contribution is usually to the plan: who does what, what the class is told, how demands are built up, and how progress is reviewed.",
 ],
 "what_it_is_not": [
  "NOT 'back to normal' on the first day back. A full timetable on day one is a common cause of breakdown; a graded return is usually safer (agree with the treating team).",
  "NOT finished when attendance is restored. Cognitive, emotional and social effects may emerge later — particularly after brain injury — so review points must be scheduled beyond the first weeks.",
  "NOT school refusal if the child is anxious about returning. Anxiety after a frightening illness is understandable; plan for it rather than framing it as avoidance.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: separation anxiety on return to preschool is common after hospitalisation; a short, predictable session with a familiar adult helps.",
  "SCHOOL AGE 6–12: peer preparation matters — what will classmates notice and ask? With consent, a short class explanation (sometimes by a hospital liaison nurse) can prevent teasing and awkwardness.",
  "ADOLESCENT 13–16: appearance, independence and privacy dominate; the young person should decide what peers are told. Exam-year returns need early planning for subject levels and RACE (check current criteria).",
  "YOUNG ADULT / SPECIAL SETTING: return to college or work may involve disability services and phased return. In special settings, re-assess skills — some pupils lose skills during illness and need them re-taught.",
 ],
 "assess": [
  "BEFORE RETURN: with consent, a meeting or call with parents, the child and — where possible — the treating team or hospital liaison, covering medical restrictions, energy, cognition, emotional state, appearance changes and what the child wants others to know.",
  "ON RETURN: observe the first weeks (energy, peer contact, work output, mood) and gather teacher and child views; a brief wellbeing measure (SDQ, RCADS — Part G) as a baseline where helpful.",
  "AFTER BRAIN INJURY OR NEUROTOXIC TREATMENT: request the neuropsychology report if one exists rather than re-testing; plan re-assessment later, as recovery and new demands change the picture.",
  "REVIEW: set dates (e.g. 4 weeks, end of term, start of next school year) to look again at learning and wellbeing.",
 ],
 "recommendations": [
  "SCHOOL SUPPORT PLUS (initially): a written return plan — graded timetable, rest arrangements, a named key adult, what peers are told, how missed work will be handled — agreed with the child and parents and shared with all staff who teach the child.",
  "CLASSROOM SUPPORT: a 'safe base' and exit card for the first weeks; seating near the door or a friend; lift pass or adapted PE where needed.",
  "SCHOOL SUPPORT: peer preparation with consent — a short, honest explanation pitched to the class age, answering likely questions (e.g. 'you can't catch it').",
  "SCHOOL SUPPORT: prioritised catch-up (see 'Missed curriculum from hospital admissions') rather than all missed work.",
  "REFER / LIAISE: treating team or paediatric liaison; home tuition to bridge a phased return (check current scheme); Primary Care psychology or CAMHS if anxiety, trauma symptoms or low mood are significant; CDNT or neuropsychology after brain injury.",
  "Schedule a formal review at the start of the next school year — new teacher, new demands.",
 ],
 "explain_parent": [
  "'Coming back is a big step for her and for you. A gradual return with a clear plan usually works better than going straight back to full days.'",
  "'She should decide, with you, what her classmates are told. We'll help the school do that in a way she's comfortable with.'",
  "SIGNPOST: the hospital liaison nurse or treating team; condition-specific charities; home tuition via the school.",
 ],
 "explain_teacher": [
  "'Everyone who teaches him needs to see the return plan — including substitutes. Most breakdowns happen when one adult doesn't know.'",
  "'Things that look fine in week one can change later, especially after a brain injury. Keep noting what you see, and we'll review.'",
  "'He'll decide what the class is told. Please don't explain on his behalf without checking.'",
 ],
 "explain_child": [
  "YOUNGER: 'You've been through a lot. Going back to school can feel exciting and scary. We'll make a plan so you know exactly what's going to happen.'",
  "OLDER: 'It's your story. You decide what people get told. What do you want teachers to know, and what do you want them to leave alone?'",
  "ASK: 'What are you looking forward to?' 'What are you worried about?' 'Who do you want to be your go-to person?'",
 ],
 "red_flags": [
  "RED FLAG — intrusive memories, nightmares, avoidance of reminders or marked anxiety after a frightening illness or accident: consider traumatic stress and refer via GP to Primary Care psychology or CAMHS.",
  "RED FLAG — low mood, hopelessness or self-harm: same-day risk route.",
  "BOUNDARY — you do not determine medical fitness to return or set activity restrictions; take these from the treating team (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'She seems fine — why do we need a plan?' A: 'Most children seem fine in the first week. The plan is about the weeks after, when energy dips and the novelty wears off.'",
  "Q: 'What should we tell the class?' A: 'Whatever he's happy with — short, honest, and answering what children will actually ask. The hospital team sometimes helps with this.'",
  "Q: 'Will his brain injury affect his learning?' A: 'The medical and neuropsychology team are best placed to say what to expect. We'll watch closely and review as demands increase — some effects show up later.'",
  "Q: 'How long will the phased return last?' A: 'We'll set a review date and increase the timetable step by step as she manages each stage, in line with what the medical team advises.'",
 ],
 "supervision": [
  "Bring a draft return plan and discuss who needs to agree it and who needs to see it.",
  "Ask how the service handles peer preparation and consent for sharing health information with a class.",
  "Discuss how to build long-term review into a case that may otherwise be closed once attendance is restored.",
 ],
 "citations": [
  "Prevatt, F. F., Heffer, R. W., & Lowe, P. A. (2000). A review of school reintegration programs for children with cancer. Journal of School Psychology, 38(5), 447–467.",
  "Ylvisaker, M., Todis, B., Glang, A., Urbanczyk, B., Franklin, C., DePompei, R., Feeney, T., Maxwell, N. M., Pearson, S., & Tyler, J. S. (2001). Educating students with TBI: Themes and recommendations. Journal of Head Trauma Rehabilitation, 16(1), 76–93.",
  "Shaw, S. R., & McCabe, P. C. (2008). Hospital-to-school transition for children with chronic illness: Meeting the new challenges of an evolving health care system. Psychology in the Schools, 45(1), 74–87.",
 ],
})

# ---------------------------------------------------------------- 7
PRES.append({
 "name": "Parent-infant mental health / 0–3 attachment work",
 "neps": N54,
 "related_to": ["Reactive Attachment Disorder", "Disinhibited Social Engagement Disorder", "Relational problems (parent-child, sibling, upbringing away from parents)", "PTSD — preschool subtype", "Global Developmental Delay"],
 "what_it_is": [
  "Infant mental health is the developing capacity of a child from birth to three to experience, regulate and express emotions, form close relationships, and explore and learn — all in the context of the caregiving relationship (Zeanah, 2019). The unit of concern is the RELATIONSHIP, not the infant alone.",
  "Parent-infant work addresses that relationship: parental mental health (perinatal depression, anxiety, trauma), the parent's own history (Fraiberg et al., 1975, 'ghosts in the nursery'), and the parent's ability to read and respond to the baby's cues. Attachment theory (Bowlby, 1969; Ainsworth et al., 1978) underpins most approaches.",
  "Part D places it under 5.4 Concerns about early development as 'Not a DSM diagnosis'. Referral routes in Part D: CDNT 0–6 teams, Primary Care, Public Health Nurse, paediatrics. In Ireland, specialist perinatal mental health services sit within the HSE (HSE, 2017, model of care — check for updates).",
  "The EP in a school psychology service rarely delivers this work directly. It matters to you because (a) you will meet older children whose early history includes it, and (b) First 5 (Government of Ireland, 2018) makes early relationships a national priority, and some psychology services do offer early years consultation.",
 ],
 "what_it_is_not": [
  "NOT a judgement that a parent is 'bad'. Most relationship difficulties in infancy arise from stress, illness, depression, trauma or a difficult-to-soothe baby, not from lack of love.",
  "NOT the same as an attachment disorder. Reactive Attachment Disorder is a specific, relatively rare diagnosis made by a specialist, associated with severe neglect; insecure attachment patterns are common and are not disorders.",
  "NOT something to 'diagnose' from a school observation of an older child. Attachment language in reports ('attachment issues') is often used loosely — describe behaviour and relationships instead.",
 ],
 "by_age": [
  "EARLY YEARS 0–3: the core band. Signs of concern include a baby who rarely seeks comfort, a parent who seems unable to enjoy or read the baby, feeding and sleep difficulties with high parental distress, or a parent with significant low mood. PHN developmental checks are a key point of identification.",
  "EARLY YEARS 3–5: in preschool, a child who does not use adults for comfort, is indiscriminately friendly with strangers, or is very watchful may be showing the effects of early relational adversity; describe and consult rather than label.",
  "SCHOOL AGE 6–12: RETROSPECTIVE — early history informs the current picture (Part D, 5.4 School Age). Ask about the first years sensitively and with purpose.",
  "SPECIAL SETTING: early intervention classes may be the first educational setting to notice relational concerns; liaise with the CDNT and PHN.",
 ],
 "assess": [
  "DEVELOPMENTAL AND RELATIONAL HISTORY: pregnancy, birth, early feeding and sleep, parental health in the first year, who cared for the child, separations. Ask why you are asking, and only what you need.",
  "OBSERVE THE CHILD WITH THE PARENT (where appropriate and consented): who initiates, how the child seeks comfort, how the parent responds, shared enjoyment. Describe, do not score, unless trained in a specific tool.",
  "CONSULT with PHN, GP, CDNT or perinatal mental health if already involved (Part D, 5.5 — do not duplicate).",
  "SCREENING TOOLS at this age (ASQ-3; SDQ 2–4 version — Part G) describe development and behaviour, not attachment quality; do not over-interpret.",
 ],
 "recommendations": [
  "REFER / SIGNPOST: parent's own GP for perinatal or parental mental health; PHN; Primary Care psychology; CDNT 0–6 where development is also a concern; Tusla (via Meitheal or a welfare referral) where family support is needed.",
  "CONSULTATION to preschool (AIM and Better Start where relevant): a consistent key person, predictable routines, and responding to the child's need for comfort rather than to the behaviour — i.e. 'connection before correction'.",
  "Recommend evidence-based relationship programmes via the service that offers them — e.g. Circle of Security (Powell et al., 2014) or video interaction guidance — rather than generic parenting advice. Check local availability.",
  "For older children with this early history: a key-adult approach in school and consistent, predictable routines (see Part I trauma and attachment entries).",
  "DO NOT write 'attachment disorder' or 'attachment difficulties' as a finding; describe relationship behaviour and let specialists diagnose.",
 ],
 "explain_parent": [
  "'Babies and toddlers learn about the world through their closest relationships. When a parent is exhausted or low — which is really common — it can be harder to enjoy each other, and there's good help for that.'",
  "'Looking after yourself is looking after her. Your GP or PHN can link you in with support for how you're feeling.'",
  "SIGNPOST: GP; PHN; HSE perinatal mental health service where eligible; family resource centres; Tusla family support.",
 ],
 "explain_teacher": [
  "'She goes to any adult for a hug and doesn't seem to prefer anyone. That's worth noticing, but not labelling. A consistent key person helps her learn who is safe.'",
  "'When he's distressed, think comfort first, correction later. He may not have learned yet that adults can calm things down.'",
  "'Be curious about the relationship with parents, not judgemental — a stressed parent needs support, not blame.'",
 ],
 "explain_child": [
  "For toddlers and preschoolers, 'explaining' is relational: be predictable, name feelings simply ('you're sad Mammy went'), and help the child see that adults notice and respond.",
  "OLDER CHILD with this early history: 'When you were very small, things were hard at home. That's not your fault. Grown-ups at school are here to help you feel safe.' Only with careful planning and ideally by someone who knows the child.",
  "Gather the child's voice through play and drawing for preschoolers — who they go to, who helps — rather than direct questioning.",
 ],
 "red_flags": [
  "RED FLAG — any suspicion of neglect or abuse of an infant or young child (unexplained injuries, failure to thrive, severe lack of care): Children First procedures; report to Tusla as soon as practicable. Telling the DLP does not discharge a mandated person's duty.",
  "RED FLAG — a parent expressing thoughts of harming themselves or the baby, or appearing acutely unwell: same-day action — urgent GP/emergency route for the parent and child protection route for the child.",
  "BOUNDARY — you do not diagnose parental mental illness or attachment disorders and do not provide infant-parent psychotherapy without specific training and service remit (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Is it my fault he's like this?' A: 'Lots of things shape how young children behave — temperament, health, stress in the family. This isn't about blame; it's about what would help you both now.'",
  "Q: 'Does she have an attachment disorder?' A: 'That's a specific diagnosis made by specialists, and it's not common. What I can describe is how she uses adults for comfort, and what helps.'",
  "Q: 'Can NEPS work with my toddler?' A: 'NEPS works with school-age children. For under-threes, the PHN, GP, Primary Care and the CDNT are the right services — I can help you know who to contact.'",
 ],
 "supervision": [
  "Discuss the service's remit for 0–3 and where you would signpost a family.",
  "Bring any case where early relational history came up and reflect on how you asked about it and how you wrote it.",
  "Talk through the emotional impact of hearing about early adversity, and your own assumptions about parenting.",
 ],
 "citations": [
  "Fraiberg, S., Adelson, E., & Shapiro, V. (1975). Ghosts in the nursery: A psychoanalytic approach to the problems of impaired infant-mother relationships. Journal of the American Academy of Child Psychiatry, 14(3), 387–421.",
  "Zeanah, C. H. (Ed.). (2019). Handbook of infant mental health (4th ed.). Guilford Press.",
  "Powell, B., Cooper, G., Hoffman, K., & Marvin, B. (2014). The Circle of Security intervention: Enhancing attachment in early parent-child relationships. Guilford Press.",
  "Government of Ireland. (2018). First 5: A whole-of-Government strategy for babies, young children and their families 2019–2028. Government Publications.",
  "Health Service Executive. (2017). Specialist perinatal mental health services: Model of care for Ireland. HSE. (Check for updates.)",
 ],
})

# ---------------------------------------------------------------- 8
PRES.append({
 "name": "Early Intervention Team caseload (0–6, pre-diagnostic)",
 "neps": N54,
 "related_to": ["Global Developmental Delay", "Autism", "DLD", "Intellectual Disability", "Developmental Coordination Disorder", "Genetic syndromes"],
 "what_it_is": [
  "A description of a young child (0–6) who is known to, or waiting for, the HSE early intervention service because of developmental concerns, but who has no diagnosis yet. Under Progressing Disability Services, early intervention teams were reconfigured into Children's Disability Network Teams (CDNTs) serving 0–18; the older term persists in referral forms and in parents' language.",
  "CDNT services are intended to be based on need, not diagnosis — a child can receive input without a diagnosis. In practice waiting lists are long in many areas (check locally before giving families timescales).",
  "Part D (5.4) lists it as 'Not a DSM diagnosis' and notes that at this age 'NEPS involvement here is usually consultation, not assessment' and that the CDNT is usually the lead service.",
  "Guralnick's (2011) developmental systems approach frames early intervention as supporting family patterns of interaction and the child's experiences, not only delivering therapy sessions to the child.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis or a prediction. Many young children on early intervention caseloads make good progress; some later receive a diagnosis, some do not. Keep language open.",
  "NOT a reason for NEPS to duplicate a CDNT assessment. Read what has been done first (Part D, 5.5: 'do not duplicate an assessment another service has done').",
  "NOT the same as an Assessment of Need (Disability Act 2005). AON is a separate statutory process; a child can be on a CDNT caseload with or without having had one.",
 ],
 "by_age": [
  "EARLY YEARS 0–3: referral usually via PHN, GP or paediatrician; the concern is often motor, communication or global development.",
  "EARLY YEARS 3–5: preschool (ECCE) is where most pre-diagnostic children meet education; AIM supports may be in place (see that entry). Questions to the EP often arise at school enrolment and placement planning.",
  "SCHOOL AGE 5–6 (transition): the child moves from preschool to primary, often still undiagnosed; school-age NEPS involvement begins, and handover of CDNT and preschool information is critical.",
  "SPECIAL SETTING: early intervention classes (for example for autistic children aged 3–5) are attached to some primary schools — check current NCSE guidance on criteria.",
 ],
 "assess": [
  "FIND OUT WHAT EXISTS: with consent, request CDNT reports, the individual family service plan (IFSP) or goals, and any AON report. Note who the key worker is.",
  "CONSULT with preschool staff (and AIM/Better Start specialist if involved) about the child's participation, communication, play and self-care in the setting.",
  "OBSERVE in the preschool if appropriate; adaptive and developmental screening (ASQ-3, Schedule of Growing Skills II, Vineland-3 — Part G) can supplement, but formal cognitive testing (WPPSI-IV UK) is rarely needed pre-diagnostically and is interpreted cautiously at this age.",
  "ASK PARENTS what they have been told, what they understand, and what they are hoping for — waiting families often have questions nobody has answered.",
 ],
 "recommendations": [
  "CONSULTATION: agree with the CDNT who leads; NEPS input is typically around school readiness, enrolment and the first-year school plan.",
  "Plan the transition to primary with a meeting (with consent) between parents, preschool, receiving school, CDNT and SENO where relevant; use the NCCA Mo Scéal templates for sharing information.",
  "CLASSROOM SUPPORT (receiving school): plan from described needs, not from a diagnosis the child does not have — visual timetables, key adult, communication supports, sensory considerations as advised by OT.",
  "SCHOOL SUPPORT: the first-year Student Support Plan should state what is known, what is awaited (e.g. CDNT assessment), and when the plan will be reviewed.",
  "REFER / LIAISE: CDNT (the lead); SENO for school resources and special class options; GP or paediatrics for medical questions.",
  "DO NOT promise a diagnosis, an assessment date or a resource. Describe needs; resources are decided by others.",
 ],
 "explain_parent": [
  "'The team can support him based on what he needs, even without a diagnosis. My part is helping school be ready for him.'",
  "'Waiting is hard. Let's make sure school has a plan from the first day, so he's not waiting too.'",
  "SIGNPOST: CDNT key worker; SENO; the school principal about enrolment; parent support groups.",
 ],
 "explain_teacher": [
  "'She doesn't have a diagnosis yet, and she doesn't need one for us to plan. Here's what we know about how she communicates and what helps.'",
  "'The CDNT is the lead service. Ask the parents if you can speak with her key worker.'",
  "'Keep observations from the first weeks — they will help the CDNT and us review the plan.'",
 ],
 "explain_child": [
  "YOUNGER (3–5): use play and pictures — 'I'm here to see what you like doing at playschool and how we can make big school fun too.'",
  "Use photos of the new school, teacher and classroom (social story approach) to prepare the child for transition.",
  "Gather the child's voice through observation of play, what they gravitate to and what distresses them, and through parents' knowledge.",
 ],
 "red_flags": [
  "RED FLAG — loss of skills the child previously had (words, play, walking): medical review via GP or paediatrics promptly — regression is not a 'wait and see'.",
  "RED FLAG — a family with no service contact for a long time and growing distress: check the child is actually on the list, and signpost to support (GP, family resource centre, Tusla family support).",
  "BOUNDARY — you do not diagnose, and you do not tell parents that a diagnosis is likely or unlikely (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Will he get a diagnosis before school starts?' A: 'I can't predict the CDNT's timescales. What we can do is make sure school plans around his needs from day one, diagnosis or not.'",
  "Q: 'Should we apply for an Assessment of Need?' A: 'That's your right under the Disability Act 2005, and it's separate from the CDNT waiting list. The HSE Assessment Officer can explain the process — check current procedures locally.'",
  "Q: 'Can NEPS assess her before school?' A: 'NEPS usually becomes involved once children are in school, and before that it's mainly consultation. The CDNT is the lead service at this age.'",
 ],
 "supervision": [
  "Ask how your service divides responsibility with the local CDNT for children aged 4–6.",
  "Bring a transition plan for a pre-diagnostic child and discuss what can and cannot be promised.",
  "Plan deliberately for Early Years band evidence — Part D notes it is the hardest band to cover on placement.",
 ],
 "citations": [
  "Guralnick, M. J. (2011). Why early intervention works: A systems perspective. Infants & Young Children, 24(1), 6–28.",
  "Health Service Executive. (current). Progressing Disability Services for Children and Young People — check current policy documents and National Access Policy.",
  "Disability Act 2005 (Ireland), Part 2 (Assessment of Need).",
  "National Council for Curriculum and Assessment. (2018). Mo Scéal: Preschool to primary school transition initiative. NCCA.",
 ],
})

# ---------------------------------------------------------------- 9
PRES.append({
 "name": "Delayed developmental milestones",
 "neps": N54,
 "related_to": ["Global Developmental Delay", "Intellectual Disability", "DLD", "Autism", "Developmental Coordination Disorder", "Hearing impairment", "Genetic syndromes"],
 "what_it_is": [
  "A description of a young child who has not reached expected milestones in one or more areas — gross motor, fine motor, speech and language, social-emotional, self-care — at the usual age. It is a finding about timing, not an explanation.",
  "Delay may be in ONE domain (e.g. late talking with otherwise typical development) or across SEVERAL (which, in a child under five, may lead a specialist to consider Global Developmental Delay — a diagnosis made by paediatrics or the CDNT, not by the EP).",
  "Causes range widely: normal variation, hearing loss, limited opportunity, prematurity, genetic conditions, neurological conditions, neglect. Shevell et al. (2003) set out the medical evaluation of global delay — a reminder that medical investigation is part of the pathway.",
  "In Ireland, PHN developmental checks under the National Healthy Childhood Programme are the main route of early identification (check current schedule). Part D (5.4) lists Schedule of Growing Skills and Griffiths III (via CDNT) as the usual tools.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis or a forecast. Early milestones are only moderately predictive of later ability (e.g. Bayley scores in infancy predict later IQ poorly — see Part G, Bayley-4).",
  "NOT to be 'waited out' when it is significant or across several areas. 'He'll grow out of it' delays referral for the children who need it.",
  "NOT the same as regression. A child who loses skills needs urgent medical review; delay and loss are different signals.",
 ],
 "by_age": [
  "EARLY YEARS 0–3: identified by PHN, GP, parents; referral to CDNT, Primary Care SLT/OT/physio and paediatrics. Hearing and vision checks are early steps.",
  "EARLY YEARS 3–5: preschool staff notice differences in play, language and self-care; AIM supports may be accessed without a diagnosis.",
  "SCHOOL AGE 6–12: RETROSPECTIVE — milestone history informs the current picture (Part D, 5.4 School Age); e.g. late language milestones are relevant to a literacy referral.",
  "SPECIAL SETTING: early intervention classes and special schools often have children with documented delay; the question becomes current skills and next steps rather than milestone ages.",
 ],
 "assess": [
  "TAKE A DEVELOPMENTAL HISTORY: ages of sitting, walking, first words, two-word phrases, toilet training; pregnancy and birth; hearing tests; illnesses. Use the PHN record (with consent) — parent recall is less reliable over time.",
  "SCREEN with ASQ-3 or Schedule of Growing Skills II (Part G) to describe current development across domains; interpret as a description, not a diagnosis.",
  "ADAPTIVE BEHAVIOUR (Vineland-3, ABAS-3 — Part G) describes everyday functioning, which often matters more for planning than a developmental quotient.",
  "CHECK HEARING AND VISION have been tested; REQUEST CDNT or paediatric reports rather than duplicating.",
 ],
 "recommendations": [
  "REFER: GP or PHN for onward referral to CDNT, Primary Care therapies, paediatrics, audiology and ophthalmology as indicated; this is the core route at this age (Part D, 5.4 column O).",
  "CONSULTATION to preschool: targets pitched to the child's current developmental level (not age), embedded in play and routines, with a simple record of progress.",
  "Consider AIM supports in the ECCE preschool where the child needs them to participate — no diagnosis is required.",
  "Plan transition to primary early, with information shared via the NCCA Mo Scéal templates and a meeting with the receiving school where needs are significant.",
  "SCHOOL SUPPORT (on entry to school): plan from developmental level and adaptive functioning; review each term.",
  "DO NOT use the phrase 'Global Developmental Delay' as a finding in your report unless a diagnosing clinician has made it — say 'delay across several areas of development was reported/observed'.",
 ],
 "explain_parent": [
  "'Children reach milestones at different times, and she's later than usual in a few areas. That's worth checking properly — not to label her, but to get her the right help early.'",
  "'The first steps are usually hearing and vision checks and a referral to the children's disability team. Your PHN or GP can make those referrals.'",
  "SIGNPOST: PHN; GP; CDNT; AIM information for preschool supports.",
 ],
 "explain_teacher": [
  "'Pitch activities to where he is now, not his age. Small steps, lots of repetition, in play.'",
  "'Notice what he can do and what's just emerging — that's the zone to work in.'",
  "'Keep a short record of new skills. It helps the CDNT and shows progress that is easy to miss.'",
 ],
 "explain_child": [
  "For young children, explaining is showing: short, playful sessions, following the child's lead, with a familiar adult present.",
  "OLDER CHILD (later retrospective discussion rarely involves the child directly); if it does: 'Everyone learns to walk and talk at different times. Some things took you longer, and that's OK.'",
  "Gather the child's voice through play preferences and what they choose, recorded in your notes.",
 ],
 "red_flags": [
  "RED FLAG — loss of previously acquired skills (words, social engagement, motor skills) at any age: urgent medical review via GP or paediatrics.",
  "RED FLAG — delay with signs of neglect (poor growth, poor hygiene, untreated medical needs, lack of stimulation): Children First procedures; report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "BOUNDARY — you describe development; paediatrics and the CDNT diagnose and investigate cause (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Will she catch up?' A: 'Some children do, and some continue to need support. Nobody can say for sure at this stage. What we know is that early support helps, so let's get the right people involved.'",
  "Q: 'My mother says I was late too.' A: 'Family history is worth mentioning to the team. It doesn't mean we wait — we still check it out.'",
  "Q: 'Does he need a diagnosis to get help?' A: 'No. The CDNT and AIM can support based on need. A diagnosis may or may not come later.'",
 ],
 "supervision": [
  "Bring a developmental history you took and discuss what you asked, what you missed and how you recorded it.",
  "Discuss how your service handles referrals of preschool children with delay, and where your role ends.",
  "Reflect on how you talked with a parent worried about their child's future.",
 ],
 "citations": [
  "Shevell, M., Ashwal, S., Donley, D., Flint, J., Gingold, M., Hirtz, D., Majnemer, A., Noetzel, M., & Sheth, R. D. (2003). Practice parameter: Evaluation of the child with global developmental delay. Neurology, 60(3), 367–380.",
  "Squires, J., & Bricker, D. (2009). Ages & Stages Questionnaires (3rd ed.). Paul H. Brookes.",
  "Bellman, M., Byrne, O., & Sege, R. (2013). Developmental assessment of children. BMJ, 346, e8687.",
 ],
})

# ---------------------------------------------------------------- 10
PRES.append({
 "name": "AIM level and preschool support already in place",
 "neps": N54,
 "related_to": ["Autism", "Global Developmental Delay", "DLD", "Cerebral palsy", "Genetic syndromes", "Hearing impairment"],
 "what_it_is": [
  "A description of the supports a child already receives in the ECCE preschool under the Access and Inclusion Model (AIM), introduced in 2016 to support children with disabilities to access and participate fully in the free preschool programme.",
  "AIM has seven levels. Levels 1–3 are universal (inclusive culture, information, and staff qualifications such as the LINC programme for an Inclusion Coordinator). Levels 4–7 are targeted: 4 — expert early years advice (Better Start Early Years Specialists); 5 — equipment, appliances and minor alterations; 6 — therapeutic intervention; 7 — additional capacity (funding for extra assistance or a reduced ratio). Check current details, as the scheme is reviewed.",
  "AIM is based on need, not diagnosis — a child does not need a diagnosis to access targeted supports (Inter-Departmental Group report, Government of Ireland, 2015 — check current rules).",
  "Part D (5.4) lists it as 'Added': it matters to the EP because the AIM support history is evidence of need and response to support, and because AIM ends when the child leaves preschool — the school must plan what replaces it.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis or an indicator of severity on its own. A Level 7 allocation reflects the preschool's circumstances as well as the child's needs.",
  "NOT the same as an SNA allocation. AIM Level 7 funds additional capacity in the preschool room; SNA support in school is allocated through the NCSE under different criteria. Do not tell parents one leads to the other.",
  "NOT something the EP applies for. Applications are made by the preschool provider with parents; the EP may be asked for information.",
 ],
 "by_age": [
  "EARLY YEARS 2y8m–5: the core band (ECCE eligibility — check current age rules). Consult with the Inclusion Coordinator and Better Start specialist on what works in the room.",
  "TRANSITION TO SCHOOL AGE: AIM does not continue into primary school. Planning for school entry must start early in the final preschool year.",
  "SCHOOL AGE 6–12: RETROSPECTIVE — what AIM levels were in place, and how the child responded, is useful history for later assessment.",
  "SPECIAL SETTING: children attending an early intervention class in a primary school are in the school system rather than ECCE — AIM does not apply there; check the arrangements in each case.",
 ],
 "assess": [
  "ASK FOR (with consent): the AIM application, Better Start specialist's notes, the preschool's access and inclusion plan, and any therapy reports under Level 6.",
  "CONSULT with the Inclusion Coordinator: what the child does in the room, what supports are used, and which ones make a difference — this is 'response to support' evidence.",
  "OBSERVE in the preschool if possible, focusing on participation, communication, play, transitions and self-care.",
  "IDENTIFY what the receiving school will need to replicate or replace, and which supports were most effective.",
 ],
 "recommendations": [
  "TRANSITION: a planning meeting (with consent) involving parents, preschool (Inclusion Coordinator), Better Start specialist if involved, receiving school, CDNT and SENO where relevant, in good time before September.",
  "Share information using the NCCA Mo Scéal templates, adding the specific strategies that worked under AIM (e.g. visual schedule, adapted seating, key person).",
  "SCHOOL SUPPORT (on entry): a first-term plan that carries over effective strategies from day one, with a review at half term.",
  "Advise parents to contact the SENO early where the child may need SNA support, a special class or school transport — timescales vary, so check locally.",
  "DO NOT imply that an AIM level predicts or entitles the child to a particular school resource.",
 ],
 "explain_parent": [
  "'The preschool supports have been working because they were built around her. Our job now is making sure primary school knows what worked, so she doesn't start from scratch.'",
  "'AIM finishes when preschool finishes. School supports come through a different system, so it's worth talking to the SENO early.'",
  "SIGNPOST: preschool Inclusion Coordinator; SENO (via NCSE); CDNT key worker; AIM information on the government's AIM website (check current).",
 ],
 "explain_teacher": [
  "(Receiving teacher) 'The preschool has found three things that really help him — here they are. Start with those on day one.'",
  "(Preschool staff) 'Your notes on what works are the most useful evidence we have. Please write them down for the school.'",
  "'Don't wait for a diagnosis or an SNA decision to use what worked in preschool.'",
 ],
 "explain_child": [
  "Prepare the child for the change using photos of the new school, the teacher and the classroom; a transition book made with preschool staff works well.",
  "OLDER PRESCHOOLER: 'Soon you'll go to big school. Your teacher already knows about the things that help you, like your picture timetable.'",
  "Gather the child's voice through play and preschool staff's knowledge of what the child likes, what upsets them and who they trust.",
 ],
 "red_flags": [
  "RED FLAG — a gap between preschool supports ending and school supports starting, with no plan: raise it with the school and SENO promptly; transitions without continuity are a common point of breakdown.",
  "RED FLAG — any child protection concern raised by preschool staff: Children First procedures apply in early years settings too — report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "BOUNDARY — you do not allocate AIM supports, SNA support or school places; describe needs and signpost (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'She had an extra adult in preschool — will she get an SNA?' A: 'SNA support in school is decided by the NCSE under its own criteria. The preschool evidence helps, but it isn't automatic. Talk to the SENO early.'",
  "Q: 'Does AIM mean he has special needs?' A: 'It means the preschool needed support to include him fully. It isn't a diagnosis.'",
  "Q: 'What do we tell the new school?' A: 'What works — the specific strategies — and what's hard. The Mo Scéal templates give you a structure for this.'",
 ],
 "supervision": [
  "Ask how your service links with Better Start and preschools in the area, and whether NEPS consults at this stage.",
  "Bring a transition plan and discuss what evidence from AIM you included.",
  "Use AIM cases to plan Early Years band evidence for Table 3 deliberately.",
 ],
 "citations": [
  "Government of Ireland. (2015). Supporting access to the Early Childhood Care and Education (ECCE) programme for children with a disability: Report of the Inter-Departmental Group. (Check current AIM rules.)",
  "National Council for Curriculum and Assessment. (2018). Mo Scéal: Preschool to primary school transition initiative. NCCA.",
  "Government of Ireland. (2018). First 5: A whole-of-Government strategy for babies, young children and their families 2019–2028. Government Publications.",
 ],
})

# ---------------------------------------------------------------- 11
PRES.append({
 "name": "Transition from preschool to primary",
 "neps": N54,
 "related_to": ["Autism", "DLD", "Global Developmental Delay", "Separation Anxiety Disorder", "Selective mutism", "ADHD"],
 "what_it_is": [
  "A description of the move from an early years setting (or home) into junior infants, and the needs that arise for a particular child — adjusting to a larger group, new adults, longer and more structured days, new routines, and formal learning.",
  "Most children manage with ordinary school practices; some need planned support — children with disabilities or developmental concerns, children with anxiety, children new to English, care-experienced children, and those with no preschool experience. O'Kane (2016) reviewed transition in the Irish context for the NCCA.",
  "Good transition is relational as well as practical: continuity of information, relationships between settings and families, and the child's familiarity with the new setting (Dockett & Perry, 2007).",
  "Part D lists it under 5.4 as 'Added' (and 5.6 'Transition planning' covers other transitions). The NCCA Mo Scéal templates (2018) are the national tool for sharing information from preschool to primary.",
 ],
 "what_it_is_not": [
  "NOT a 'school readiness' test the child passes or fails. Readiness is shared — the school must be ready for the child, not only the child for school.",
  "NOT solved by delaying entry by a year as a default. Deferring may suit some children, but it is a decision to make with information, not a routine recommendation. The evidence on holding children back is mixed — check before advising.",
  "NOT over by the October break. Some children cope in September and struggle once novelty fades or demands increase.",
 ],
 "by_age": [
  "EARLY YEARS 4–5: the core band. Planning should start in the final preschool year, with visits, photos, meetings and Mo Scéal information.",
  "SCHOOL AGE 5–6 (junior and senior infants): the settling period; watch for separation difficulties, toileting, fatigue, peer difficulties and behaviour that signals overwhelm.",
  "SPECIAL SETTING: transition into an early intervention class, special class or special school involves the SENO and often the CDNT; planning is longer and more individual.",
  "LATER TRANSITIONS: patterns in this first transition are useful history for planning primary-to-post-primary transition (Part D, 5.6).",
 ],
 "assess": [
  "GATHER: Mo Scéal documents, AIM and preschool information, CDNT reports, and the parents' account of what helps and worries them.",
  "CONSULT with the preschool about the child's day: routines, separation, toileting, communication, play, triggers and calming strategies.",
  "AFTER ENTRY: observe in the classroom in the first half-term if concerns arise; an SDQ (Part G) from teacher and parent can describe emotional and behavioural adjustment.",
  "ASK THE CHILD (through play, drawing or a photo book) what they know and feel about the new school.",
 ],
 "recommendations": [
  "BEFORE ENTRY: a transition meeting where needed (parents, preschool, school, CDNT, SENO), plus extra visits, a photo book of the school and staff, and a clear plan for the first weeks.",
  "CLASSROOM SUPPORT: a consistent key adult, visual timetable, clear predictable routines, a quiet space, and explicit teaching of routines (lining up, toileting, lunch).",
  "CLASSROOM SUPPORT: a shortened day for the first weeks only where needed and agreed, with a clear plan to build up — not open-ended.",
  "SCHOOL SUPPORT: for children with identified needs, a Student Support Plan from the first term with a review at half term.",
  "REFER / LIAISE: CDNT where developmental concerns persist; Primary Care psychology or NEPS consultation where anxiety or behaviour is significant; SENO for resources.",
  "DO NOT recommend deferral of school entry without weighing the evidence and the child's circumstances with parents.",
 ],
 "explain_parent": [
  "'Starting school is a big change for every child. We'll plan it so he knows what to expect, and so school knows what helps him.'",
  "'Some wobbles in the first weeks are normal. We'll check in after a few weeks to see how he's settling.'",
  "SIGNPOST: the school's transition information; preschool staff; SENO where additional needs are identified.",
 ],
 "explain_teacher": [
  "'Here is what the preschool found works. Use it from the first day and adapt as you get to know her.'",
  "'Teach the routines explicitly — how to line up, where to go for the toilet — rather than expecting her to pick them up.'",
  "'If she seems fine in September but struggles in November, that's not unusual. Let's review then.'",
 ],
 "explain_child": [
  "YOUNGER: 'Soon you'll go to big school. Let's look at pictures of your new classroom and your teacher, and see where the toilets and the yard are.'",
  "Use a personalised transition book or social story, and let the child visit and play in the new classroom before September.",
  "ASK (through play or drawing): 'What will you do at big school?' 'What do you think it will be like?' 'Who will help you?'",
 ],
 "red_flags": [
  "RED FLAG — severe, persistent distress, refusal, or regression (e.g. loss of toileting, speech) beyond the settling period: look at what is happening and consider referral.",
  "RED FLAG — child protection concerns arising during transition (e.g. disclosure, unexplained injuries): Children First procedures apply — report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "BOUNDARY — decisions about school entry age and placement belong to parents with the school and SENO; you describe needs (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Should we keep her back a year?' A: 'It depends on her and on what support is available. Let's look at her needs and what school can do before deciding — deferring isn't automatically better.'",
  "Q: 'He cried every morning for a week — is something wrong?' A: 'Some upset in the first weeks is common. If it continues, or other things change, let's look more closely.'",
  "Q: 'What's Mo Scéal?' A: 'It's a set of templates from the NCCA for preschools, parents and children to share information with the new school.'",
 ],
 "supervision": [
  "Ask how your service supports preschool-to-primary transitions and whether NEPS attends transition meetings.",
  "Bring a transition plan and discuss what you would change for a child with more complex needs.",
  "Use transition work to build Early Years band evidence for Table 3.",
 ],
 "citations": [
  "O'Kane, M. (2016). Transition from preschool to primary school (NCCA Research Report No. 19). National Council for Curriculum and Assessment.",
  "National Council for Curriculum and Assessment. (2018). Mo Scéal: Preschool to primary school transition initiative. NCCA.",
  "Dockett, S., & Perry, B. (2007). Transitions to school: Perceptions, expectations, experiences. UNSW Press.",
 ],
})

# ---------------------------------------------------------------- 12
PRES.append({
 "name": "Care-experienced children (foster, kinship, residential, aftercare)",
 "neps": N55,
 "related_to": ["Reactive Attachment Disorder", "Disinhibited Social Engagement Disorder", "Posttraumatic Stress Disorder", "Complex PTSD", "Foetal Alcohol Spectrum Disorder", "Relational problems (parent-child, sibling, upbringing away from parents)", "ADHD"],
 "what_it_is": [
  "A description of a child or young person who is or has been in the care of the State — in general foster care, relative (kinship) foster care, residential care, or special care — or who is now in aftercare. In Ireland, Tusla is responsible under the Child Care Act 1991; the large majority of children in care are in foster care (check Tusla's current figures before quoting).",
  "Care status is not a diagnosis and not a problem in itself. Care-experienced children as a group have lower average educational outcomes, but Sebba et al. (2015) found that factors such as school changes, placement changes and time out of school explain much of that gap, and that longer-term stable care is associated with better progress than being in need but at home.",
  "Many children in care have experienced abuse, neglect, loss and multiple moves before and during care. The EP's task is to understand this child's history and current relationships — carefully and with the right consent — and to help school be a stable, predictable place.",
  "Aftercare: under the Child Care (Amendment) Act 2015, eligible young people are entitled to an assessment of need for aftercare and an aftercare plan; supports can continue into the early twenties for those in education or training (check current eligibility).",
 ],
 "what_it_is_not": [
  "NOT a reason to assume difficulties. Many care-experienced children do well; expectations shape outcomes. Avoid a report that reads as a list of deficits.",
  "NOT 'attachment disorder' by default. Relationship difficulties are common after adversity, but attachment disorders are specific diagnoses made by specialists. Describe behaviour and relationships.",
  "NOT the carer's or social worker's job alone. Schools are one of the most important protective factors for children in care (Sebba et al., 2015); school stability and a trusted adult matter.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: concerns may centre on development, regulation and relationships; FASD and the effects of prenatal exposure may be relevant. Consult with the social worker, carers and preschool.",
  "SCHOOL AGE 6–12: behaviour that looks like defiance may reflect hypervigilance, shame or fear of rejection; transitions (placement moves, access visits, holidays) can unsettle the child.",
  "ADOLESCENT 13–16: identity, contact with birth family, and placement stability are live issues; risk of disengagement, exclusion and exploitation increases. Plan for aftercare early (Part D, 5.5: 'service transitions at 16 and 18').",
  "YOUNG ADULT 17–26: aftercare; further and higher education access (e.g. DARE/HEAR schemes — check current criteria); transition to adult services. SPECIAL SETTING: care placements and school placements need joint planning.",
 ],
 "assess": [
  "CONSENT FIRST: establish who holds parental responsibility and who can consent (birth parents, Tusla under a care order, or both — varies by order type). Check with the social worker and your supervisor before proceeding.",
  "READ what is available: Tusla care plan (with consent), previous school records, CDNT or CAMHS reports. Avoid making the child tell their story again.",
  "CONSULT with carers, social worker and teachers about current relationships, triggers, strengths and the child's pattern across settings.",
  "ASSESS learning in the context of missed schooling and moves; screen wellbeing (SDQ, and Part G measures as appropriate) and describe relationships and regulation without over-labelling.",
 ],
 "recommendations": [
  "SCHOOL SUPPORT / SUPPORT PLUS: a named key adult in school with regular, predictable contact; a safe base; and an agreed plan for difficult times (e.g. before and after access visits).",
  "CLASSROOM SUPPORT: relational approaches — connection before correction, predictable routines, advance warning of changes, sensitivity with curriculum topics such as family trees and baby photos.",
  "SCHOOL SUPPORT: a plan for learning gaps from missed school or moves, reviewed each term; protect the child's place in school during placement changes where possible.",
  "Liaise (with consent) with the social worker so school is included in care planning; ask whether a care plan review is due and whether school input is wanted.",
  "REFER: CAMHS or Tusla-commissioned therapeutic services where trauma or mental health needs are significant; CDNT where developmental needs are present; aftercare worker for older young people.",
  "DO NOT include sensitive care history in a report beyond what is necessary and consented to.",
 ],
 "explain_parent": [
  "(Carer) 'You know her day-to-day better than anyone. I'd like to understand what helps her feel safe and settled, at home and at school.'",
  "(Birth parent, where involved) 'I'm here to help school support him. I'll be careful about what I write and who sees it.'",
  "SIGNPOST: social worker; Irish Foster Care Association (for carers); EPIC — Empowering People in Care (advocacy for young people).",
 ],
 "explain_teacher": [
  "'Behaviour that looks like defiance may be fear. Ask what she might be feeling before deciding on a consequence.'",
  "'Give her notice of changes — substitute teachers, trips, room moves. Surprises can feel threatening.'",
  "'Be careful with family-tree projects and baby photos; offer choices so she isn't exposed.'",
 ],
 "explain_child": [
  "YOUNGER: 'I'm here to help school be a good place for you. You don't have to tell me anything you don't want to.'",
  "OLDER: 'You've probably met lots of professionals. I'm the one who thinks about school. What would make school better for you?'",
  "ASK: 'Who at school do you trust?' 'What do teachers do that helps, and what makes things worse?' Record the young person's own words.",
 ],
 "red_flags": [
  "RED FLAG — any disclosure or sign of abuse (including in placement), exploitation or going missing: Children First procedures; report to Tusla as soon as practicable, and inform the allocated social worker.",
  "RED FLAG — self-harm, suicidal ideation or high-risk behaviour: same-day risk route.",
  "BOUNDARY — you do not assess placements, make decisions about contact, or diagnose attachment or trauma disorders (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Who signs the consent form?' A: 'It depends on the type of care order. Check with the social worker and your supervisor — don't assume the foster carer can consent.'",
  "Q: 'Should we tell the class he's in care?' A: 'Only if he wants that. It's his information.'",
  "Q: 'Why is she so good in school and so difficult at home (or vice versa)?' A: 'Children often feel safe enough to show their distress in one place. That tells us about safety, not about who's doing it right.'",
 ],
 "supervision": [
  "Bring the consent question for any care-experienced child before starting work.",
  "Discuss how to write about care history in a report — what is necessary, what is not.",
  "Reflect on the emotional impact of reading a care history and how it affects your view of the child.",
 ],
 "citations": [
  "Sebba, J., Berridge, D., Luke, N., Fletcher, J., Bell, K., Strand, S., Thomas, S., Sinclair, I., & O'Higgins, A. (2015). The educational progress of looked after children in England: Linking care and educational data. Rees Centre, University of Oxford.",
  "Child Care Act 1991 (Ireland); Child Care (Amendment) Act 2015 (Ireland).",
  "Darmody, M., McMahon, L., Banks, J., & Gilligan, R. (2013). Education of children in care in Ireland: An exploratory study. Ombudsman for Children's Office. (Check citation details.)",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
 ],
})

# ---------------------------------------------------------------- 13
PRES.append({
 "name": "Child protection and welfare concerns",
 "neps": N55,
 "related_to": ["Posttraumatic Stress Disorder", "Complex PTSD", "Reactive Attachment Disorder", "Relational problems (parent-child, sibling, upbringing away from parents)", "Adjustment Disorder"],
 "what_it_is": [
  "A description of a situation in which there is reasonable concern that a child has been, is being, or is at risk of being harmed — through neglect, emotional abuse, physical abuse or sexual abuse — or where the child's welfare needs are not being met. Children First (2017) defines the four categories and gives examples.",
  "Under the Children First Act 2015, psychologists are mandated persons. A mandated person who knows, believes or has reasonable grounds to suspect that a child has been harmed, is being harmed or is at risk of being harmed, above the threshold of harm set out in the Act, must report to Tusla as soon as practicable. Check the Act and Guidance for exact wording.",
  "Schools follow the Department of Education's Child Protection Procedures for Primary and Post-Primary Schools (2017; revised 2023 — check current version) and have a Designated Liaison Person (DLP) and Child Safeguarding Statement. Telling the DLP does NOT discharge a mandated person's duty; a joint report with the DLP is permitted.",
  "Part D places child protection under 5.5 (and 3.7 Risk and safeguarding as 'STOP — not an assessment area'). It is not something you assess or investigate; it is a route you follow.",
 ],
 "what_it_is_not": [
  "NOT an investigation. The EP does not question the child to establish facts, examine injuries, or decide whether abuse occurred — Tusla and An Garda Síochána do that.",
  "NOT a matter to hold for supervision first. Supervision follows action; it never replaces it. If a concern meets the threshold, report, then discuss.",
  "NOT confidential. You cannot promise a child or parent confidentiality where there is a child protection concern; say so at the start of work.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: young children cannot disclose verbally; concerns come from observation — injuries, failure to thrive, sexualised behaviour beyond developmental norms, extreme fearfulness. Preschools have their own safeguarding obligations.",
  "SCHOOL AGE 6–12: disclosures may be partial, indirect ('I have a secret'), or through drawing or play. Listen, do not lead, record verbatim, report.",
  "ADOLESCENT 13–16: concerns may include peer abuse, online exploitation, coercive relationships, and self-neglect. Young people may ask you to keep it secret — you cannot.",
  "YOUNG ADULT / SPECIAL SETTING: over 18, adult safeguarding (HSE Safeguarding and Protection Teams) applies; children with disabilities are at greater risk and may be less able to disclose (Children First, 2017).",
 ],
 "assess": [
  "DO NOT ASSESS the concern. Your 'assessment' role is limited to noticing, listening and recording.",
  "IF A CHILD DISCLOSES: listen calmly; do not ask leading questions; do not promise secrecy; reassure them they were right to tell; record their exact words, date, time and context, and sign it.",
  "IF YOU HAVE A CONCERN without disclosure: record what you observed factually, with dates, and consult the Children First Guidance on thresholds; consult your supervisor if unsure about threshold, but do not delay a report that is clearly required.",
  "CHECK whether Tusla or other services are already involved (Part D, 5.5) — this does not remove your duty to report new information.",
 ],
 "recommendations": [
  "ACTION: report to Tusla as soon as practicable (via the Tusla portal or local duty social work team — check current method); inform the school DLP; a joint report is permitted. Record what you did and when.",
  "RISK OF IMMEDIATE DANGER: contact An Garda Síochána (999/112).",
  "AFTER REPORTING: discuss with your supervisor; follow your service's procedures for notifying NEPS management and recording.",
  "SCHOOL SUPPORT: with Tusla's guidance, a plan for the child in school — a trusted adult, predictable routine, attention to learning and wellbeing — without investigating.",
  "IN REPORTS: record child protection information only as necessary and in line with your service's policy; do not include unverified allegations in an educational report.",
  "DO NOT confront alleged perpetrators, contact the family to 'check' before reporting when this may place the child at risk, or promise outcomes.",
 ],
 "explain_parent": [
  "(At the start of any work) 'What we talk about is confidential, with one exception — if I'm worried about a child's safety, I have to pass that on to Tusla.'",
  "(Where it is safe to inform parents — check with Tusla if unsure) 'I've had to make a report to Tusla. That's a legal duty for me. Tusla will be in touch to talk with you.'",
  "SIGNPOST: Tusla; the school's Child Safeguarding Statement; support services as advised by Tusla.",
 ],
 "explain_teacher": [
  "'If a child tells you something worrying, listen, don't question, don't promise to keep it secret, write down their exact words, and tell the DLP straight away.'",
  "'If you're a mandated person, telling the DLP doesn't discharge your own duty — you can report jointly.'",
  "'Our job is not to find out if it happened. That's Tusla's job.'",
 ],
 "explain_child": [
  "YOUNGER: 'You did the right thing telling me. I need to tell someone whose job is to keep children safe.'",
  "OLDER: 'I can't keep this secret, because it's about your safety. I'll tell you what happens next as much as I can.'",
  "DO NOT ask 'did he hurt you?' or other leading questions. Use open prompts only if needed: 'Tell me more.'",
 ],
 "red_flags": [
  "RED FLAG — immediate danger: contact An Garda Síochána.",
  "RED FLAG — a concern held without reporting because 'it might not reach threshold' when the Guidance examples clearly apply: report, then discuss in supervision.",
  "BOUNDARY — you do not investigate, interview, or make findings about abuse (PSI 2.2.2); Tusla and An Garda Síochána do.",
 ],
 "questions": [
  "Q: 'Do I need to report if the DLP already has?' A: 'If you're a mandated person with the information, you have your own duty. A joint report with the DLP covers both.'",
  "Q: 'What if I'm not sure it meets the threshold?' A: 'Check the Children First Guidance and consult your supervisor or Tusla promptly. Don't sit on it — Tusla can advise.'",
  "Q: 'Should I tell the parents I've made a report?' A: 'Usually parents are informed, but not if it would place the child at further risk. Take advice from Tusla if unsure.'",
  "Q: 'Can I put this in my psychological report?' A: 'Only what is necessary and in line with service policy. Child protection records are kept separately.'",
 ],
 "supervision": [
  "Know your service's child protection procedure and who to call before you need it.",
  "After any report, bring the case to supervision to reflect on your actions and the emotional impact.",
  "Discuss the threshold of harm with examples, so you are clearer when a real situation arises.",
 ],
 "citations": [
  "Children First Act 2015 (Ireland).",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
  "Department of Education. (2023). Child protection procedures for primary and post-primary schools (revised). Government of Ireland. (Check for the current version.)",
 ],
})

# ---------------------------------------------------------------- 14
PRES.append({
 "name": "Domestic violence exposure",
 "neps": N55,
 "related_to": ["Posttraumatic Stress Disorder", "Complex PTSD", "Separation Anxiety Disorder", "Oppositional Defiant Disorder", "Relational problems (parent-child, sibling, upbringing away from parents)"],
 "what_it_is": [
  "A description of a child living with, or who has lived with, domestic violence or abuse between adults in the home — physical, sexual, emotional, financial or coercive control. The Domestic Violence Act 2018 created an offence of coercive control in Ireland.",
  "Children are not 'witnesses' only: they hear, see, intervene, are used by the abuser, and live with the aftermath. Callaghan et al. (2018) describe children as directly experiencing coercive control and developing their own coping strategies.",
  "Holt, Buckley and Whelan (2008) reviewed impacts on children across development, including emotional, behavioural and learning effects, and noted that effects vary with the child's age, the severity and the protective factors available. Children First (2017) recognises exposure to domestic violence as a form of emotional abuse — check the wording in the current Guidance.",
  "Part D places it under 5.5 as 'Not a DSM diagnosis'. It is always a child protection and welfare matter to consider.",
 ],
 "what_it_is_not": [
  "NOT something that only harms a child who is physically hurt. Emotional harm from living with abuse is significant in itself.",
  "NOT resolved when the abuser leaves. Post-separation abuse, contact arrangements and court processes can continue the stress.",
  "NOT the non-abusing parent's fault. Avoid language that blames the victim-parent for 'failing to protect'; support safety instead.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: sleep problems, clinginess, regression, startle responses, aggressive play; very young children are highly dependent on the caregiver's own state.",
  "SCHOOL AGE 6–12: hypervigilance, difficulty concentrating, worry about the parent at home, aggression or withdrawal; may take on caring roles or feel responsible.",
  "ADOLESCENT 13–16: risk of anger, low mood, substance use, school disengagement, and experiencing abuse in their own relationships.",
  "YOUNG ADULT / SPECIAL SETTING: continuing effects on relationships and mental health; children with disabilities may be at greater risk and less able to disclose.",
 ],
 "assess": [
  "DO NOT INVESTIGATE. If DV exposure comes to light, follow Children First procedures first.",
  "IF ALREADY KNOWN (e.g. Tusla involved): with consent, ask what the child has experienced, what supports are in place, and the current safety situation.",
  "DESCRIBE the child's current functioning at school: concentration, peer relationships, emotional regulation, attendance, learning. SDQ or RCADS (Part G) where useful.",
  "BE CAREFUL with joint parent meetings: a parent may not be safe to speak in front of the other; check before arranging.",
 ],
 "recommendations": [
  "ACTION: report to Tusla as soon as practicable where there is concern, and inform the DLP; the child's safety comes first.",
  "SCHOOL SUPPORT: a trusted adult, a predictable routine, and a quiet space; the school as a safe, stable place.",
  "CLASSROOM SUPPORT: understand that concentration may be affected by worry and hypervigilance; avoid sudden loud noises or shouting where possible.",
  "Check information-sharing arrangements carefully: court orders, barring/safety orders, who can collect the child, whose address can be shared.",
  "REFER / SIGNPOST: Tusla; domestic violence services for the parent and children (Women's Aid, Safe Ireland, local services — check current); Primary Care psychology or CAMHS for significant trauma symptoms.",
  "DO NOT send reports to a parent whose access is restricted without checking the orders in place.",
 ],
 "explain_parent": [
  "(To the non-abusing parent) 'What's happened at home isn't your fault. My job is to make sure school is a safe place for him and that he gets the support he needs.'",
  "'I have a duty to share concerns about a child's safety with Tusla. That's about getting support in place.'",
  "SIGNPOST: Women's Aid national helpline; Safe Ireland; Tusla; GP.",
 ],
 "explain_teacher": [
  "'Her tiredness and poor focus may be about what's happening at home. Keep routines steady and give her a trusted adult.'",
  "'Check the orders about who can collect her and what information goes to whom.'",
  "'Don't ask her about home. If she tells you something, listen and follow the child protection procedure.'",
 ],
 "explain_child": [
  "YOUNGER: 'Grown-ups fighting isn't your fault. It's OK to feel scared or angry. School is a safe place, and you can talk to [key adult].'",
  "OLDER: 'Lots of young people live with this. It's not your job to fix it. If you want to talk, there are people who can help.'",
  "ASK (only with care and not to investigate): 'What helps you feel calm at school?' 'Who can you talk to?'",
 ],
 "red_flags": [
  "RED FLAG — immediate danger to child or parent: contact An Garda Síochána.",
  "RED FLAG — disclosure of harm, or concern the child is being harmed: report to Tusla as soon as practicable; inform the DLP.",
  "BOUNDARY — you do not assess risk from the abuser, advise on custody or access, or provide trauma therapy outside your remit (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Should I tell the father about the assessment?' A: 'Check who has guardianship and whether any orders limit contact or information sharing. Take advice from your supervisor and the school.'",
  "Q: 'He's aggressive in class — is it because of what happened at home?' A: 'It may be connected. Let's look at when it happens and what helps, and make sure he has a safe adult in school.'",
  "Q: 'Will she be OK?' A: 'Many children recover well with safety and support. School can be a big part of that.'",
 ],
 "supervision": [
  "Discuss information-sharing and guardianship issues in DV cases before sending any report.",
  "Reflect on how to avoid victim-blaming language in reports and meetings.",
  "Bring your own reactions to DV cases — these cases can be distressing.",
 ],
 "citations": [
  "Holt, S., Buckley, H., & Whelan, S. (2008). The impact of exposure to domestic violence on children and young people: A review of the literature. Child Abuse & Neglect, 32(8), 797–810.",
  "Callaghan, J. E. M., Alexander, J. H., Sixsmith, J., & Fellin, L. C. (2018). Beyond 'witnessing': Children's experiences of coercive control in domestic violence and abuse. Journal of Interpersonal Violence, 33(10), 1551–1581.",
  "Domestic Violence Act 2018 (Ireland).",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
 ],
})

# ---------------------------------------------------------------- 15
PRES.append({
 "name": "Parenting capacity concerns",
 "neps": N55,
 "related_to": ["Relational problems (parent-child, sibling, upbringing away from parents)", "Reactive Attachment Disorder", "Foetal Alcohol Spectrum Disorder", "Oppositional Defiant Disorder", "Adjustment Disorder"],
 "what_it_is": [
  "A description of concern about whether a parent or carer is able to meet a child's needs — for safety, care, emotional warmth, stimulation, guidance and stability — often in the context of parental mental illness, substance use, intellectual disability, domestic violence, or overwhelming stress.",
  "Parenting capacity is formally assessed by Tusla social workers and, in court proceedings, by specialist assessors, usually using an ecological framework that looks at the child's developmental needs, parenting capacity and family and environmental factors together (Cleaver et al., 2011; Donald & Jureidini, 2004).",
  "Part D places it under 5.5 as 'Not a DSM diagnosis'. The EP does not assess parenting capacity; the EP describes the child's needs and functioning at school, which may be relevant to those who do.",
  "Most families with parenting difficulties are helped through family support rather than child protection. In Ireland, Meitheal is Tusla's national practice model for early, voluntary, strengths-based family support.",
 ],
 "what_it_is_not": [
  "NOT a judgement about a parent's love or worth. Many parents under severe pressure love their children deeply and still struggle to meet their needs.",
  "NOT automatically a child protection matter. It becomes one when the concern reaches the threshold of harm in Children First — then it must be reported.",
  "NOT within the EP role to decide. Statements like 'the mother lacks capacity to parent' do not belong in an EP report.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: the child's development, growth, health appointments kept, and attunement between parent and child; PHN and GP are often the first to notice.",
  "SCHOOL AGE 6–12: attendance, punctuality, hygiene, lunches, homework support, and the child's emotional state; the child may be caring for a parent or siblings.",
  "ADOLESCENT 13–16: supervision, boundaries and emotional support; young carers may be hidden. Risk of disengagement and risk-taking.",
  "YOUNG ADULT / SPECIAL SETTING: parents of young people with complex needs may be exhausted and under-supported — respite and adult service planning matter.",
 ],
 "assess": [
  "DESCRIBE THE CHILD, not the parent: attendance, readiness to learn, emotional state, relationships at school, and changes over time. Factual, dated observations.",
  "ASK the parent about their situation, strengths and support network with warmth and without judgement; what would help?",
  "CHECK whether Tusla, Meitheal or other services are involved (Part D, 5.5); with consent, liaise rather than duplicate.",
  "CONSIDER the threshold: if concerns reach the level of harm or risk of harm, follow Children First procedures and report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
 ],
 "recommendations": [
  "SIGNPOST / REFER: Meitheal (via Tusla or a lead practitioner) for voluntary family support; family resource centres; Home School Community Liaison (HSCL) in DEIS schools; GP for parental health.",
  "SCHOOL SUPPORT: practical supports that reduce the child's disadvantage (breakfast club, homework club, uniform help — check what the school offers), and a trusted adult.",
  "Recommend evidence-based parenting programmes offered locally — e.g. Parents Plus, Incredible Years or Triple P — where appropriate and wanted; check availability.",
  "Where concerns meet threshold: report to Tusla as soon as practicable and inform the DLP; supervision follows action.",
  "IN REPORTS: describe the child's needs and what would help at home in practical terms; avoid judgemental statements about the parent.",
 ],
 "explain_parent": [
  "'Parenting is hard, and it's harder when you're dealing with a lot. I'm here to think about what would help him, and that includes what would help you.'",
  "'There are services that can help families — would you like me to tell you about them?'",
  "SIGNPOST: Meitheal (via school or Tusla); family resource centre; GP; parenting programmes locally.",
 ],
 "explain_teacher": [
  "'Notice and record what you see in the child — attendance, hunger, tiredness, mood — with dates. Facts help more than impressions.'",
  "'A warm relationship with the parent keeps the door open. Blame closes it.'",
  "'If you think it reaches child protection level, follow the procedure. Don't wait for more evidence.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes grown-ups at home have a lot to deal with. School can help make things a bit easier for you.'",
  "OLDER: 'It sounds like you do a lot at home. That's a lot to carry. Who helps you?' (Young carers may need specific support.)",
  "ASK: 'What's a good day like?' 'What would make things easier?' Record the child's words.",
 ],
 "red_flags": [
  "RED FLAG — signs of neglect (hunger, poor hygiene, untreated medical needs, lack of supervision) or abuse: Children First procedures; report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "RED FLAG — parent under the influence at collection time, or unable to care safely: follow the school's safeguarding procedure immediately.",
  "BOUNDARY — you do not assess parenting capacity or give opinions on it (PSI 2.2.2); you describe the child and refer.",
 ],
 "questions": [
  "Q: 'Can you write a report saying she's a good mother?' A: 'My report is about how he is doing in school and what helps him. I can describe the positive things I see, but I can't make judgements about parenting.'",
  "Q: 'What is Meitheal?' A: 'It's Tusla's way of bringing services together around a family, on a voluntary basis, to agree what help is needed. A lead practitioner coordinates it.'",
  "Q: 'Are you going to report us?' A: 'I have to report to Tusla if I believe a child is at risk of harm. Right now I'm here to help work out what support would help.' (Be honest; don't reassure beyond what you can.)",
 ],
 "supervision": [
  "Discuss the line between family support and child protection with a real or anonymised example.",
  "Bring report wording about home circumstances and check it for judgement.",
  "Reflect on your own assumptions about parenting and class.",
 ],
 "citations": [
  "Cleaver, H., Unell, I., & Aldgate, J. (2011). Children's needs — parenting capacity: Child abuse, parental mental illness, learning disability, substance misuse and domestic violence (2nd ed.). The Stationery Office.",
  "Donald, T., & Jureidini, J. (2004). Parenting capacity. Child Abuse Review, 13(1), 5–17.",
  "Tusla — Child and Family Agency. (current). Meitheal national practice model. Tusla. (Check for the current version.)",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
 ],
})

# ---------------------------------------------------------------- 16
PRES.append({
 "name": "Family functioning difficulties",
 "neps": N55,
 "related_to": ["Relational problems (parent-child, sibling, upbringing away from parents)", "Adjustment Disorder", "Oppositional Defiant Disorder", "Separation Anxiety Disorder", "Major Depressive Disorder"],
 "what_it_is": [
  "A description of patterns in a family — communication, conflict, roles, boundaries, emotional responsiveness, problem-solving — that are affecting the child's wellbeing or school functioning. Examples: high parental conflict, separation or divorce, bereavement, sibling difficulties, a family member's illness or addiction.",
  "Systemic approaches see the child's difficulties in the context of family relationships rather than located in the child alone (Carr, 2012). The McMaster model (Epstein et al., 1978) describes dimensions of family functioning — problem-solving, communication, roles, affective responsiveness, affective involvement and behaviour control — that can structure your thinking.",
  "Part D (5.5) lists it as 'Not a DSM diagnosis'; DSM-5-TR includes relational problems among 'Other conditions that may be a focus of clinical attention' (Z codes — check specific codes).",
  "The EP's role is to understand the family context as part of formulation, to work in partnership with parents, and to refer to family-focused services where needed — not to provide family therapy without training and remit.",
 ],
 "what_it_is_not": [
  "NOT 'a dysfunctional family'. All families have strengths and stresses; describe specific patterns, not labels.",
  "NOT the cause of every difficulty. Children's difficulties can also create family stress — the relationship is two-way.",
  "NOT a child protection concern unless it reaches the threshold of harm; then it must be reported.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: family stress shows in sleep, feeding, regression and behaviour; parent-child relationship support is key.",
  "SCHOOL AGE 6–12: children may bring worries to school (separation, conflict, illness); behaviour and concentration change; loyalty conflicts in separated families.",
  "ADOLESCENT 13–16: conflict over autonomy, risk-taking, withdrawal; young people may take sides or take on adult roles.",
  "YOUNG ADULT / SPECIAL SETTING: family stress around transition to adulthood and adult services; families of young people with complex needs may need respite and support.",
 ],
 "assess": [
  "ASK ABOUT FAMILY with purpose and sensitivity: who lives at home, recent changes, how decisions and conflicts are handled, what the family does well.",
  "HEAR EACH PERSPECTIVE where possible — both parents (if both hold guardianship), the child, and school.",
  "DESCRIBE how family factors appear in school: timing of changes in behaviour, what the child says, attendance patterns.",
  "USE formulation frameworks (e.g. Interactive Factors Framework — Reference sheet) to place family factors alongside child and school factors.",
 ],
 "recommendations": [
  "CLASSROOM SUPPORT: a trusted adult and predictable routines; flexibility at known difficult times (e.g. handovers between parents).",
  "SCHOOL SUPPORT: work with both parents where both hold guardianship — send information to both unless orders say otherwise.",
  "SIGNPOST / REFER: family resource centres; Primary Care psychology or social work; CAMHS where the child's mental health needs are moderate to severe; family therapy services (check local availability); Meitheal for coordinated family support; Rainbows (for loss and separation — check local availability).",
  "Recommend parenting programmes where appropriate — e.g. Parents Plus (an Irish-developed programme) — offered locally.",
  "DO NOT take sides in parental disputes in your report or meetings.",
 ],
 "explain_parent": [
  "'Children often feel what's going on at home, even when adults try to protect them. It's normal for that to show up in school.'",
  "'Both of you are important to her. Working together on what helps her at school will make a difference.'",
  "SIGNPOST: family resource centre; GP; family mediation services for separating parents (check current).",
 ],
 "explain_teacher": [
  "'His behaviour changed around the time things changed at home. That doesn't excuse it, but it helps us understand it.'",
  "'Send information to both parents unless there's an order in place.'",
  "'Stay neutral — don't get drawn into what's happening between the adults.'",
 ],
 "explain_child": [
  "YOUNGER: 'Lots of families have tricky times. It's not your fault. You can tell [key adult] how you're feeling.'",
  "OLDER: 'You don't have to choose sides or fix things. What would help you at school right now?'",
  "ASK: 'Who's in your family?' 'What's good at home?' 'What's hard?' — genograms or family drawings can help younger children.",
 ],
 "red_flags": [
  "RED FLAG — disclosure of violence, abuse or neglect: Children First procedures; report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "RED FLAG — the child expressing hopelessness, self-harm or suicidal thoughts: same-day risk route.",
  "BOUNDARY — you do not provide family therapy or mediation outside your training and remit, and you do not advise courts on custody (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Should I tell school about our separation?' A: 'It can help them understand changes in her behaviour, and they'll handle it sensitively. It's your choice what you share.'",
  "Q: 'Can you write a letter for court?' A: 'That's outside my role. My reports are about her education, and they may be requested through proper channels. Talk to your solicitor.'",
  "Q: 'Is it our fault?' A: 'Lots of things affect how children do. Looking for blame doesn't help; looking at what will help does.'",
 ],
 "supervision": [
  "Discuss how to handle requests from one parent to exclude the other, and requests for court reports.",
  "Bring a formulation where family factors were important and check you avoided blame.",
  "Reflect on your own family experiences and how they might influence your views.",
 ],
 "citations": [
  "Carr, A. (2012). Family therapy: Concepts, process and practice (3rd ed.). Wiley-Blackwell.",
  "Epstein, N. B., Bishop, D. S., & Levin, S. (1978). The McMaster model of family functioning. Journal of Marital and Family Therapy, 4(4), 19–31.",
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
 ],
})

# ---------------------------------------------------------------- 17
PRES.append({
 "name": "Housing and economic problems",
 "neps": N55,
 "related_to": ["Adjustment Disorder", "Separation Anxiety Disorder", "Major Depressive Disorder", "Posttraumatic Stress Disorder", "Relational problems (parent-child, sibling, upbringing away from parents)"],
 "what_it_is": [
  "A description of a child whose school life is affected by poverty, debt, food insecurity, overcrowding, poor housing, housing insecurity or homelessness — including families in emergency accommodation (hotels, B&Bs, family hubs).",
  "DSM-5-TR lists housing and economic problems among 'Other conditions that may be a focus of clinical attention' (Z codes — check specific codes); Part D (5.5) records it as 'DSM-5-TR Z-codes'. These are context, not disorders.",
  "Effects on school are practical and emotional: long commutes from emergency accommodation, nowhere to do homework, poor sleep, hunger, missed school, shame, and disrupted friendships. Growing Up in Ireland data link economic disadvantage with poorer outcomes (check specific findings before quoting).",
  "The Department of Education's DEIS programme (Delivering Equality of Opportunity in Schools) targets resources to schools serving concentrated disadvantage — including Home School Community Liaison and School Completion Programme — though many disadvantaged children attend non-DEIS schools.",
 ],
 "what_it_is_not": [
  "NOT a learning difficulty. Poor attainment in a child who is hungry, tired and moving between hotels should not be interpreted without that context.",
  "NOT a parenting failure. Structural factors (housing supply, income) are often the main cause.",
  "NOT something school can fix — but school can reduce its impact on the child's learning and belonging.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: developmental effects of cramped living, limited play space and parental stress; access to preschool may be disrupted.",
  "SCHOOL AGE 6–12: tiredness, hunger, lateness, lack of uniform or equipment, embarrassment; children may hide their situation.",
  "ADOLESCENT 13–16: shame, withdrawal from peers, part-time work, taking on adult worries; risk of early school leaving.",
  "YOUNG ADULT / SPECIAL SETTING: financial barriers to further education; supports such as SUSI grants (check current criteria). Families of children with complex needs may face extra costs.",
 ],
 "assess": [
  "ASK SENSITIVELY about practical circumstances: where the family is living, travel to school, space for homework, sleep, meals.",
  "DESCRIBE how circumstances affect school: attendance, punctuality, tiredness, equipment, homework completion, peer relationships.",
  "INTERPRET attainment and cognitive results in context — note circumstances in the report and caveat interpretations.",
  "CHECK what supports the school and family already access (HSCL, school meals, book schemes, Tusla, St Vincent de Paul, local authority).",
 ],
 "recommendations": [
  "SCHOOL SUPPORT: practical help — school meals, breakfast club, homework club, uniform and book support (check current schemes); discreet access so the child is not singled out.",
  "CLASSROOM SUPPORT: flexibility with homework and equipment; do not penalise lateness caused by long travel from emergency accommodation.",
  "Link with HSCL (DEIS schools) and the School Completion Programme; Tusla Education Support Service where attendance is affected.",
  "SIGNPOST: local authority housing; Citizens Information; MABS (Money Advice and Budgeting Service); Focus Ireland, Threshold or St Vincent de Paul (check current).",
  "IN REPORTS: note circumstances neutrally and with consent; recommendations must be achievable in the child's current living situation (e.g. no 'quiet study space at home' if there is none).",
 ],
 "explain_parent": [
  "'Where you're living is making school harder for him — the travel, the tiredness. That's not your fault. Let's think about what school can do to help.'",
  "'There are supports that might help — would it be OK if I linked you with the HSCL coordinator?'",
  "SIGNPOST: HSCL; Citizens Information; MABS; Focus Ireland or St Vincent de Paul.",
 ],
 "explain_teacher": [
  "'He's coming from a hotel on the other side of the city. The lateness is the journey, not the attitude.'",
  "'Homework in one room with the whole family isn't realistic. Can he do it in homework club?'",
  "'Make sure help is discreet — shame is a big part of this for children.'",
 ],
 "explain_child": [
  "YOUNGER: 'Moving and living in a new place is hard. School can help make some things easier.'",
  "OLDER: 'You've got a lot going on outside school. What would make school easier right now?'",
  "ASK: 'What's the hardest thing about getting to school?' 'Where do you do your homework?'",
 ],
 "red_flags": [
  "RED FLAG — signs of neglect (persistent hunger, untreated medical needs, lack of supervision): Children First procedures; report to Tusla as soon as practicable (telling the DLP does not discharge a mandated person's duty; supervision follows action).",
  "RED FLAG — a young person not attending or disappearing from school during a housing move: contact Tusla Education Support Service and follow attendance procedures.",
  "BOUNDARY — you do not advise on housing, welfare entitlements or finances; signpost to the right services (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Is it OK to put in the report that we're homeless?' A: 'Only with your agreement. It can help others understand what's affecting him, but it's your information.'",
  "Q: 'Will his results be lower because of this?' A: 'They might be, and I'll say so in the report so nobody misreads them.'",
  "Q: 'Can school help with books and uniform?' A: 'Many schools have supports and there are national schemes. Ask the principal or HSCL coordinator.'",
 ],
 "supervision": [
  "Bring a report where circumstances affected interpretation and check your wording.",
  "Discuss what supports are available locally and how to signpost without overstepping.",
  "Reflect on assumptions about families in poverty.",
 ],
 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
  "Department of Education. (2017). DEIS plan 2017: Delivering equality of opportunity in schools. Government of Ireland. (Check for updates.)",
  "Growing Up in Ireland. (current). National longitudinal study of children — reports. ESRI / Trinity College Dublin. (Check the specific report before quoting findings.)",
 ],
})

# ---------------------------------------------------------------- 18
PRES.append({
 "name": "Social exclusion, discrimination, acculturation difficulty",
 "neps": N55,
 "related_to": ["Adjustment Disorder", "Posttraumatic Stress Disorder", "Social Anxiety Disorder", "Major Depressive Disorder", "Selective mutism"],
 "what_it_is": [
  "A description of a child whose wellbeing or school functioning is affected by being excluded, discriminated against, or struggling to adapt between cultures — for example Traveller and Roma children, children of migrant families, children seeking or granted international protection, children arriving under temporary protection, LGBTQ+ young people, and children from minority faiths.",
  "Berry (1997) described acculturation as the process of cultural and psychological change when groups meet, with strategies such as integration, assimilation, separation and marginalisation; acculturative stress arises when the demands of adapting outstrip resources.",
  "DSM-5-TR lists acculturation difficulty, social exclusion or rejection, and target of perceived adverse discrimination or persecution among Z codes (Part D, 5.5: 'DSM-5-TR Z-codes'). These are contexts, not disorders — check specific codes.",
  "Ireland's Equal Status Acts 2000–2018 prohibit discrimination in education on nine grounds, including race and membership of the Traveller community. The State recognised Traveller ethnicity in 2017.",
 ],
 "what_it_is_not": [
  "NOT a learning difficulty. A child learning English as an additional language, or adapting to a new school system, may appear to struggle for reasons that are not about learning ability.",
  "NOT the child's problem to fix. Exclusion and discrimination are systemic; the response must include the school, not only the child.",
  "NOT to be assessed with tools normed on a different population without caution — standardised tests may be culturally and linguistically biased.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: children absorb messages about belonging early; home language development matters, and maintaining it supports later English learning.",
  "SCHOOL AGE 6–12: peer exclusion, name-calling, and difficulty with unfamiliar school routines; the child may act as interpreter for parents.",
  "ADOLESCENT 13–16: identity questions, experiences of racism or homophobia, intergenerational cultural conflict, risk of disengagement or early school leaving.",
  "YOUNG ADULT / SPECIAL SETTING: barriers to further education and employment; for young people with disabilities from minority groups, double disadvantage in access to services.",
 ],
 "assess": [
  "USE AN INTERPRETER (professional, not a child or family member) for parent meetings where needed; check your service's arrangements.",
  "GATHER HISTORY: languages spoken, schooling before arrival, migration experience (only as needed and with sensitivity), current circumstances.",
  "ASSESS WITH CARE: consider non-verbal measures (e.g. Leiter-3, WNV — Part G) and dynamic assessment; interpret standardised scores cautiously and say so.",
  "ASK about experiences of exclusion or discrimination at school, and look at the school's response to bullying and diversity.",
 ],
 "recommendations": [
  "CLASSROOM SUPPORT: welcoming practices — pronouncing names correctly, visible representation of the child's culture and language, buddy systems.",
  "SCHOOL SUPPORT: EAL support; valuing and encouraging the home language; explicit teaching of school routines and expectations.",
  "WHOLE-SCHOOL: anti-bullying procedures that name racism, homophobia and anti-Traveller discrimination (Cineáltas action plan, 2022, and the Bí Cineálta procedures for schools, 2024 — check the current version); staff training need identified through casework.",
  "REFER / SIGNPOST: Primary Care psychology or CAMHS where there is significant distress or trauma; specialist services for refugees and people seeking international protection (check current); Traveller and Roma organisations for family support and advocacy.",
  "IN REPORTS: describe the child's language and cultural context and its effect on assessment validity.",
 ],
 "explain_parent": [
  "'Your child's home language is a strength. Keeping it strong at home helps her learning in English too.'",
  "'If she's been treated unfairly or excluded at school, I want to know — it's school's responsibility to deal with that.'",
  "SIGNPOST: interpreter services; community organisations; school principal about anti-bullying procedures.",
 ],
 "explain_teacher": [
  "'His difficulties with English are not a learning difficulty. Give him time and support, and value his home language.'",
  "'Name-calling about ethnicity or family background is bullying — deal with it as such.'",
  "'Don't use children as interpreters for their parents in meetings.'",
 ],
 "explain_child": [
  "YOUNGER: 'You speak two languages — that's amazing. School should be a place where everyone belongs.'",
  "OLDER: 'Moving between two cultures can be hard. What's it like for you at school? Has anyone treated you unfairly?'",
  "ASK (with an interpreter if needed): 'What's good about school?' 'What's hard?' 'Do you feel you belong?'",
 ],
 "red_flags": [
  "RED FLAG — signs of trauma from pre-migration experiences (nightmares, hypervigilance, dissociation): refer via GP to Primary Care psychology or CAMHS; do not probe traumatic history in an educational assessment.",
  "RED FLAG — racist bullying, threats or violence: school must act under its anti-bullying and child safeguarding procedures; child protection procedures if harm.",
  "BOUNDARY — you do not advise on immigration or legal status; signpost (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Should we speak only English at home to help him?' A: 'No — keeping the home language strong actually supports learning English. Speak the language you're most comfortable in.'",
  "Q: 'Is her test score accurate?' A: 'Tests are designed for children who've grown up in a particular language and culture. I've interpreted her results with caution and explained why in the report.'",
  "Q: 'He's being called names — what can we do?' A: 'Tell the school. They must deal with it under their anti-bullying procedures.'",
 ],
 "supervision": [
  "Discuss assessment validity for children from minority language and cultural backgrounds.",
  "Reflect on your own cultural assumptions and how they shape your interpretation.",
  "Ask about interpreter arrangements in your service.",
 ],
 "citations": [
  "Berry, J. W. (1997). Immigration, acculturation, and adaptation. Applied Psychology, 46(1), 5–34.",
  "Equal Status Acts 2000–2018 (Ireland).",
  "Department of Education. (2022). Cineáltas: Action plan on bullying. Government of Ireland. (Check for current procedures.)",
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.). American Psychiatric Publishing.",
 ],
})

# ---------------------------------------------------------------- 19
PRES.append({
 "name": "Knowing which service does what, and the referral route",
 "neps": N55,
 "related_to": ["Autism", "ADHD", "Intellectual Disability", "Major Depressive Disorder", "Posttraumatic Stress Disorder", "DLD"],
 "what_it_is": [
  "A practitioner competence rather than a child presentation: knowing which Irish service is responsible for which need, what their criteria are, how to refer, and what the family can expect. Part D flags it as 'Added — your named development area'.",
  "Core services: NEPS (school psychology, Continuum of Support); HSE CDNTs (children with complex needs arising from disability, 0–18, under Progressing Disability Services); HSE Primary Care (psychology, SLT, OT, physio for non-complex needs); CAMHS (moderate to severe mental health disorders — check current operational guideline); Tusla (child protection and welfare, family support, Meitheal, Tusla Education Support Service); NCSE (SENOs, SNA allocation, special class and school placement, Visiting Teacher service and Inclusion Support Service — check current structures); GP and paediatrics.",
  "Assessment of Need (AON) under the Disability Act 2005 is a statutory right to have health needs arising from disability assessed; it is separate from CDNT service provision and from NEPS. Check current HSE procedures.",
  "Other services commonly met: Jigsaw (youth mental health, check age range and locations); audiology and ophthalmology (via GP or PHN); family resource centres; Garda Youth Diversion; Tusla Education Support Service (formerly the National Educational Welfare Board); SEC for exam accommodations (RACE).",
 ],
 "what_it_is_not": [
  "NOT a matter of 'refer to everyone'. Multiple referrals can confuse families and lead to rejected referrals; know the criteria first.",
  "NOT static. Services, criteria and structures change (e.g. PDS reconfiguration, NCSE absorbing new services). Check current information before advising families.",
  "NOT only about referral. Knowing what each service does also helps avoid duplication and informs what the EP should and should not do (Part D, 5.5).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: PHN, GP, CDNT, Primary Care, AIM (preschool), paediatrics; NEPS typically consultation only.",
  "SCHOOL AGE 6–12: NEPS, CDNT, Primary Care, CAMHS, Tusla, NCSE/SENO.",
  "ADOLESCENT 13–16: add Jigsaw, SEC (RACE), guidance counsellor, youth services; plan for transition from CAMHS at 18 and from CDNT at 18 (Part D: 'service transitions at 16 and 18 are a live issue').",
  "YOUNG ADULT 17–26: adult mental health, adult disability services, college disability services, aftercare. SPECIAL SETTING: multi-disciplinary team around the setting.",
 ],
 "assess": [
  "READ Form 2 section 2 (or your service's equivalent) to see what services are already involved, and ask the family (Part D, 5.5).",
  "IDENTIFY the need: educational, developmental/disability, mental health, child protection, medical, social.",
  "MATCH need to service using current criteria; check with your supervisor and service directory.",
  "CONSENT: the family must agree to referrals, except where a child protection report is required.",
 ],
 "recommendations": [
  "Keep an up-to-date local service map (service, criteria, contact, referral route, typical waiting time) — review it with your supervisor.",
  "IN REPORTS: name the service and the reason for referral clearly, and who makes the referral (school, GP, parent, NEPS).",
  "Tell families honestly about waiting times and what they can do while waiting.",
  "Follow up referrals — check they were received and not lost.",
  "Where two services could fit (e.g. Primary Care psychology vs CAMHS, Primary Care SLT vs CDNT), write down the reason for your choice against the published criteria, so a rejected referral can be re-routed quickly rather than started again.",
  "DO NOT promise that a service will accept a referral or provide a particular intervention.",
 ],
 "explain_parent": [
  "'There are a lot of services, and it can be confusing. I'll explain who does what and help you know where to go.'",
  "'The referral goes through your GP / school / us. Waiting times vary, so here's what we can do in the meantime.'",
  "SIGNPOST: GP; school principal; SENO; Citizens Information for general guidance.",
 ],
 "explain_teacher": [
  "'NEPS supports school; the CDNT supports children with complex disability needs; CAMHS is for moderate to severe mental health; Tusla is for child protection and family support.'",
  "'Before referring, check who's already involved.'",
  "'You don't need to wait for another service to put classroom supports in place.'",
 ],
 "explain_child": [
  "YOUNGER: 'There are different helpers for different things — some help with learning, some with feelings, some with bodies.'",
  "OLDER: 'I think [service] could help with [need]. Here's what they do and what might happen. What do you think?'",
  "ASK: 'Have you met other people who help you? What was that like?'",
 ],
 "red_flags": [
  "RED FLAG — a child at risk falling between services (e.g. rejected by both CAMHS and Primary Care): escalate with your supervisor; do not leave the child without a plan.",
  "RED FLAG — child protection concern: Tusla referral is required regardless of other services.",
  "BOUNDARY — do not refer outside your service's protocols or without consent (except for child protection) (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Why can't NEPS diagnose autism?' A: 'In Ireland, autism assessment is typically done by the CDNT, CAMHS or private practitioners. NEPS supports the school side.'",
  "Q: 'We were refused by CAMHS — what now?' A: 'Ask why, and whether Primary Care psychology or another service fits better. I can talk with you about options.'",
  "Q: 'Is AON the same as the CDNT?' A: 'No. AON is a statutory assessment under the Disability Act; the CDNT provides services. Ask the HSE Assessment Officer for details.'",
 ],
 "supervision": [
  "Build and review your local service map with your supervisor early in placement.",
  "Bring a case where the right referral was unclear.",
  "Discuss how your service manages children who fall between services.",
 ],
 "citations": [
  "Disability Act 2005 (Ireland).",
  "Health Service Executive. (current). CAMHS operational guideline. HSE. (Check for the current edition.)",
  "Health Service Executive. (current). Progressing Disability Services for Children and Young People. HSE. (Check current policy.)",
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications.",
 ],
})

# ---------------------------------------------------------------- 20
PRES.append({
 "name": "Multi-disciplinary meetings and your role in them",
 "neps": N55,
 "related_to": ["Autism", "Intellectual Disability", "Cerebral palsy", "ADHD", "Posttraumatic Stress Disorder", "Genetic syndromes"],
 "what_it_is": [
  "A practitioner competence: preparing for, contributing to and following up on meetings involving several professionals and the family — for example Student Support Plan reviews, CDNT team meetings, Meitheal meetings, transition meetings, Tusla child protection conferences, and case conferences in special schools.",
  "Part D lists it as 'Added' under 5.5. The EP's typical contribution is a psychological perspective on learning, behaviour and wellbeing; a formulation that links different views; and practical recommendations for school.",
  "Multi-agency working brings benefits (shared understanding, coordinated plans) and challenges (role confusion, power differences, information sharing, time). Atkinson et al. (2002) and Sloper (2004) reviewed the factors that make it work — clear roles, good communication, shared goals and leadership.",
  "Parents and the child are part of the team, not an audience. Their voice should shape the meeting and its outcomes.",
 ],
 "what_it_is_not": [
  "NOT a place to present assessment results for the first time to parents. Parents should hear significant findings before the meeting, privately.",
  "NOT the EP's job to chair every meeting or coordinate every service. Know who leads (CDNT key worker, Meitheal lead practitioner, school principal, Tusla social worker).",
  "NOT confidential by default. Agree at the start what will be recorded and shared, and with whom; consent under GDPR applies.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: transition meetings with preschool, CDNT, school, SENO; parents may be new to services and overwhelmed.",
  "SCHOOL AGE 6–12: Student Support Plan reviews, CDNT meetings, Meitheal, child protection conferences.",
  "ADOLESCENT 13–16: the young person should attend where appropriate; transition planning at 16 and 18 (Part D, 5.5).",
  "YOUNG ADULT / SPECIAL SETTING: adult services transitions; MDT around the setting (Part D, 5.5 Special Setting).",
 ],
 "assess": [
  "PREPARE: know the purpose of the meeting, who will attend, what decisions are expected, and what you are expected to contribute; clarify with the chair.",
  "GATHER: your assessment findings and formulation, the child's voice, and any questions for other professionals.",
  "PLAN: what you will say (brief, jargon-free, focused on what helps), and what you will not say (e.g. findings the parent has not yet heard).",
  "REFLECT afterwards: did the meeting reach clear actions? Were parents and the child heard?",
 ],
 "recommendations": [
  "BEFORE: meet parents to share findings; prepare a one-page summary; check consent for information sharing.",
  "DURING: summarise findings in plain language; link your view to others' (a formulation helps); ask for the child's and parents' views; agree specific, time-bound actions with named people.",
  "AFTER: check minutes for accuracy; follow up on your actions; record in the case file.",
  "Know your role boundary: offer a psychological perspective; do not advise on medication, diagnosis or other professions' areas.",
  "DO NOT agree to actions you cannot deliver, or allow the meeting to end without clear next steps.",
 ],
 "explain_parent": [
  "'Before the meeting, I'll go through my findings with you so there are no surprises.'",
  "'You're a key part of the meeting — your view of your child is as important as anyone's.'",
  "SIGNPOST: bring a support person if you like; ask for a copy of the minutes.",
 ],
 "explain_teacher": [
  "'Come with two or three specific examples of what you see and what helps — they're more useful than general impressions.'",
  "'Let's agree specific actions, who does what, by when.'",
  "'If anything is unclear, ask — other professionals use jargon too.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some grown-ups who help you are meeting to talk about how to make school good for you. I'll tell them what you told me.'",
  "OLDER: 'You can come to the meeting, or I can share your views. What do you want them to know?'",
  "ASK: 'What would you like the meeting to decide?' Record the child's words to share.",
 ],
 "red_flags": [
  "RED FLAG — child protection concerns raised in a meeting: they must be acted on — report to Tusla as soon as practicable; do not wait for minutes.",
  "RED FLAG — parents excluded or overwhelmed, or decisions made without them: raise it with the chair.",
  "BOUNDARY — contribute your professional view; do not speak for other disciplines or make decisions outside your role (PSI 2.2.2).",
 ],
 "questions": [
  "Q: 'Who's in charge of the meeting?' A: 'It depends on the meeting — the principal for school reviews, the key worker for CDNT meetings, the lead practitioner for Meitheal. Check beforehand.'",
  "Q: 'What if professionals disagree?' A: 'That's normal. A formulation can bring views together. The aim is a plan that helps the child, not agreement on everything.'",
  "Q: 'Can I bring someone with me?' (parent) A: 'Yes — a friend, relative or advocate can help.'",
 ],
 "supervision": [
  "Discuss your role before your first MDT meeting, and debrief after.",
  "Bring a meeting where you felt your contribution was unclear or overridden.",
  "Reflect on power dynamics — between professionals, and between professionals and families.",
 ],
 "citations": [
  "Atkinson, M., Wilkin, A., Stott, A., Doherty, P., & Kinder, K. (2002). Multi-agency working: A detailed study. National Foundation for Educational Research.",
  "Sloper, P. (2004). Facilitators and barriers for co-ordinated multi-agency services. Child: Care, Health and Development, 30(6), 571–580.",
  "National Educational Psychological Service. (2010). A continuum of support for post-primary schools: Guidelines for teachers. Department of Education and Skills. (Check for updates.)",
 ],
})
