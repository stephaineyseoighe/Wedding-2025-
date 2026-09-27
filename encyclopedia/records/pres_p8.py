# PRES batch 8 — descriptive (non-diagnostic) presentations, last batch.
# Context: Reference Part D, column N.
#   Item 1      sits under 5. OTHER (5.5 Involvement of other services) — Part D: "Added — your named
#               development area"; routes CAMHS | Tusla | Primary Care | NEPS | supervisor.
#   Items 2–14  sit under 5. OTHER (5.6 School and access factors) — Part D: "0 dx · 14 pres";
#               "None. Everything here is a presentation." Routes: NEPS | Educational Welfare (Tusla) |
#               SENO | State Examinations Commission | NCSE | Primary Care | community services.
# Part D, School Age, 5.6: "Classroom observation with the environment as the unit of analysis, not the
# child · Continuum of Support documentation · Student Support File · teaching approach."
# Items 12–14 are school/system-level: written from the EP's systemic and consultative role.
# 'Behaviour system fit', 'Knowing which service does what' and 'Multi-disciplinary meetings' are
# written in other batches and are cross-referenced, not repeated.

NEPS_55 = "5. OTHER (5.5 Involvement of other services)"
NEPS_56 = "5. OTHER (5.6 School and access factors)"

PRES = []

# ---------------------------------------------------------------- 1
PRES.append({
 "name": "Professional and service boundaries",
 "neps": NEPS_55,
 "related_to": ["ADHD", "Autism", "Depressive disorders", "Anxiety disorders", "Child protection and welfare concerns", "Eating disorders"],
 "what_it_is": [
  "Part D wording: 'Professional and service boundaries — what is not yours to do — your named development area'. A presentation about the ROLE, not the child: the case in front of you contains a question that belongs to another profession or service, and the risk is that you answer it anyway.",
  "The EP's lane in Irish schools: assess learning, behaviour and wellbeing in context; formulate; consult with teachers and parents; recommend at the right Continuum of Support level; refer; support whole-school work (NEPS, 2007; DES, 2017). Diagnosis of medical and psychiatric conditions and medication advice sit outside it (PSI 2.2.2).",
  "Boundaries run in two directions. OUTWARD: questions that belong to CAMHS, the CDNT, paediatrics, SLT, OT, Tusla, the SENO/NCSE, the SEC, An Garda Síochána or the courts. INWARD: questions that belong to the school — discipline, timetabling, staffing, enrolment — which the EP advises on but does not decide.",
  "The one boundary that never limits action is child protection. Under the Children First Act 2015, a mandated person who knows, believes or has reasonable grounds to suspect harm reports to Tusla as soon as practicable; telling the DLP does not discharge that duty, and supervision follows the action, never replaces it (DCYA, 2017).",
 ],
 "what_it_is_not": [
  "NOT 'refer everything on'. A boundary tells you whose decision it is; it does not stop you describing what you see, formulating, or recommending what the school can do now while a referral is pending.",
  "NOT a script for saying no. Most boundary questions arrive as a reasonable request ('Just tell us if it's autism'); the skill is naming what you CAN offer in the same breath.",
  "NOT fixed across services. What a NEPS psychologist does, what a CDNT psychologist does and what a private psychologist does differ; the boundary is set by your role in this service, your competence and your supervision, not by your title (check your service's scope with your supervisor).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: pressure to 'confirm' autism or global developmental delay for a preschool place or AIM support. Diagnosis sits with the CDNT or Assessment of Need process; you describe and signpost.",
  "SCHOOL AGE 6–12: 'Should he be on medication?'; 'Can you write that she needs an SNA?'; 'Can you tell us if the father should have access?' Each belongs elsewhere (GP/paediatrics or CAMHS; NCSE via SENO; the courts).",
  "ADOLESCENT 13–16: the young person discloses self-harm or a risk to themselves or others — same-day risk route, not a follow-up appointment; requests for 'therapy' beyond a brief consultation model; confidentiality with a young person versus the school's need to know.",
  "YOUNG ADULT 17–26: adult consent applies; CAMHS transition at 18; eligibility for DARE or adult disability services is decided by those bodies, not by your report.",
  "SPECIAL SETTING: many professionals in the room (CDNT, SNA, class teacher, nurse). The risk is the reverse — nobody owns the question. Part D: 'Multi-disciplinary team around the setting.'",
 ],
 "assess": [
  "READ FIRST: every report supplied with the referral and Form 2 section 2 (services involved). Part D, School Age: 'duplication is a common trainee error'. Do not repeat an assessment another service has done or is doing.",
  "NAME THE QUESTION BEHIND THE REFERRAL: write it in one line and ask 'whose question is this?' If the honest answer is 'the CDNT's' or 'the GP's', your task becomes description plus a well-written referral route.",
  "CHECK YOUR COMPETENCE: is this a presentation you have been trained and supervised in? If not, say so and bring it to supervision before acting (PSI, n.d.).",
  "SCREEN FOR RISK in every contact: disclosures, injuries, statements of intent. Risk overrides every other boundary question and is actioned the same day.",
 ],
 "recommendations": [
  "WRITE IN YOUR LANE: 'The pattern observed is consistent with difficulties in attention across settings; a referral to [GP/CAMHS/paediatrics] is recommended to consider whether further assessment is indicated.' Never 'He has ADHD' or 'Medication should be considered'.",
  "WRITE WHAT THE SCHOOL CAN DO NOW: every referral-on recommendation is paired with a Classroom Support or School Support recommendation, so the child is not waiting on a list with nothing in place.",
  "NAME THE DECISION-MAKER: 'SNA access is decided by the NCSE on the school's application'; 'Examination accommodations are decided by the SEC'; 'Diagnosis is a matter for the CDNT'. This protects the family from reading your report as a promise.",
  "RISK AND PROTECTION: record what was disclosed, what you did and when, and who you told (Tusla report, DLP informed, parent contact where safe) — then bring it to supervision.",
  "DO NOT advise on medication, diagnose, offer ongoing therapy outside your service model, comment on custody or access, or promise a resource another body allocates. REFER to the named service with a clear question.",
 ],
 "explain_parent": [
  "'I can't tell you whether it's autism — that assessment is done by the Children's Disability Network Team. What I can do is describe what I've seen in school and write it so it's useful to them.'",
  "'Questions about medication are for your GP or the doctor who sees him. I'll describe the difficulties clearly so they have the school picture.'",
  "'I can't decide if she gets an SNA — the school applies and the NCSE decides. What I can say is what help she needs during the day, and the school can use that.'",
 ],
 "explain_teacher": [
  "'I know it would be easier if I could give a diagnosis today. I can't — but I can give you a plan for Monday that doesn't depend on one.'",
  "'If she tells you something that worries you about her safety, you don't wait for me. Your DLP procedure and a Tusla report apply today.'",
 ],
 "explain_child": [
  "YOUNGER: 'My job is to find out how school can be easier for you. There are other helpers for other things, and I can help your mum and dad find them.'",
  "OLDER: 'What you tell me stays between us unless I'm worried about your safety or someone else's — then I have to tell someone who can help, and I'll tell you first where I can.'",
  "ASK: 'Who else is helping you at the moment?' Young people often know about a service that nobody put on the referral form.",
 ],
 "red_flags": [
  "RED FLAG — disclosure of abuse, neglect, self-harm or suicidal ideation: same-day risk and child protection route; report to Tusla as soon as practicable; informing the DLP does not discharge your duty as a mandated person (Children First Act 2015).",
  "WATCH — you find yourself writing a diagnostic sentence 'because the family needs it for a service'. Stop; describe, and name who can diagnose.",
  "BOUNDARY — a request to see a child repeatedly for 'counselling' outside your service's consultation model; discuss with your supervisor before agreeing.",
  "WATCH — a case where every service thinks another holds it. Name the gap in writing and raise it at supervision.",
 ],
 "questions": [
  "Q: 'Can you just tell us if it's ADHD? We know you can't write it.' A: 'I genuinely can't make that call — it's a medical and psychiatric diagnosis. What I can tell you is what I saw and whether it points towards a referral.'",
  "Q: 'The CDNT waiting list is two years. Can't you do the assessment?' A: 'I can describe his learning and plan school supports now, which don't need a diagnosis. The diagnostic question stays with the team; I'll write it up so the referral is strong.'",
  "Q: 'She told me something, but she asked me not to tell anyone.' A: 'You can't promise that. If it's a safety concern, the DLP procedure and a Tusla report apply today — I'll help you think it through, but don't wait for me.'",
  "Q: 'Will your report get him an SNA?' A: 'No report guarantees that. The NCSE decides on the school's application. I'll describe his care needs clearly.'",
 ],
 "supervision": [
  "Bring one case where you felt pulled to answer a question outside your role — what made it hard to hold, and what did you offer instead?",
  "Ask your supervisor to map this service's scope: what NEPS does, what it does not, and where local practice differs (e.g., therapeutic group work, early years).",
  "After any risk disclosure: bring the record of what you did and when. Supervision reviews the action; it does not replace it.",
 ],
 "citations": [
  "Department of Children and Youth Affairs. (2017). Children First: National guidance for the protection and welfare of children. Government Publications. — check for updates.",
  "Children First Act 2015, No. 36 of 2015 (Ireland).",
  "Psychological Society of Ireland. (n.d.). Code of professional ethics. PSI. (Check the current edition and its year before citing.)",
  "National Educational Psychological Service. (2007). Special educational needs: A continuum of support — Guidelines for teachers. Department of Education and Science.",
 ],
})

# ---------------------------------------------------------------- 2
PRES.append({
 "name": "Classroom environment",
 "neps": NEPS_56,
 "related_to": ["ADHD", "Autism", "Hearing impairment", "Visual impairment", "Sensory modulation difficulties (over- or under-responsive)"],
 "what_it_is": [
  "Part D wording: 'Classroom environment — Context, not a diagnosis', and at School Age: 'Classroom observation with the environment as the unit of analysis, not the child'. The physical and organisational features of the room that make learning easier or harder for everyone, and for this child in particular.",
  "Covers: noise and acoustics; light and glare; temperature and air; visual clutter on walls; seating and sight-lines to the teacher and board; space to move; where resources are kept; routines and visual structure (timetables, signals); and group arrangement.",
  "Barrett et al. (2015) linked classroom design features (light, temperature, air quality, flexibility, colour and complexity) to measured progress in primary pupils in England. Fisher et al. (2014) found that young children in a heavily decorated room were more off-task and learned less in short lessons than in a sparse one.",
  "Shield and Dockrell (2003) reviewed the effects of noise on children's performance and wellbeing; poor acoustics matter most for children with hearing loss, language difficulties, EAL, or attention difficulties.",
 ],
 "what_it_is_not": [
  "NOT a judgement on the teacher's room. Many features (building age, class size, a prefab by the road) are outside the teacher's control; the EP describes the fit, not a fault.",
  "NOT only 'sensory'. Organisational features — where the child sits, how transitions are signalled, whether resources are reachable — often matter more than the lights.",
  "NOT a substitute for looking at the child. An adjusted room removes barriers; a child who still struggles in a well-arranged room needs their own formulation.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: Part D: 'Preschool room organisation · AIM supports · staff:child ratio.' Look at the flow between areas, noise at tidy-up, and where the child goes when overwhelmed.",
  "SCHOOL AGE 6–12: one room for most of the day, so its features have a large cumulative effect. Seating, board visibility, visual clutter and noise from group work are the common findings.",
  "ADOLESCENT 13–16: many rooms and many teachers in a day. The question is which rooms work and which don't — science labs, practical rooms and the canteen are frequent hot spots.",
  "YOUNG ADULT 17–26: lecture halls, workshops, workplaces. Self-advocacy about seating and noise becomes the skill.",
  "SPECIAL SETTING: Part D: 'This is the band. Setting organisation, staffing, curriculum and integration are the assessment.' Small rooms with several adults and high sensory load are common — check whether workstation and calm-space use is planned or reactive.",
 ],
 "assess": [
  "OBSERVE THE ROOM, NOT ONLY THE CHILD: sketch the layout — doors, windows, board, the child's seat, the teacher's usual position, noise sources. Note where the child looks when the teacher talks.",
  "TIME-SAMPLE ACROSS CONDITIONS: on-task behaviour during whole-class teaching versus group work versus independent work; note noise level and movement in each.",
  "ASK THE CHILD where they work best and worst in the room, and what distracts them — younger children can point on a drawing.",
  "CHECK SENSORY BASICS before interpreting: when was hearing and vision last tested? A child at the back with an undetected hearing loss looks like an attention problem.",
  "Use the Interactive Factors Framework (Frederickson & Cline, 2015) to keep environment, child and teaching in view together.",
 ],
 "recommendations": [
  "SEATING WITH A REASON: near the point of instruction, away from doors and noise sources, with a clear sight-line to the board and the teacher's face (essential for hearing loss and language difficulty); review after a trial rather than fixing it for the year.",
  "REDUCE VISUAL LOAD near the teaching wall; keep displays purposeful (Fisher et al., 2014). A visual timetable and a consistent signal for transitions help the whole class.",
  "NOISE: agree noise levels for different activities; soft furnishing or felt pads where practical; a quiet work spot available by routine, not as a sanction.",
  "CONTINUUM LEVEL: Classroom Support — these are whole-class adjustments. School Support where the Student Support Plan names specific adjustments (workstation, planned movement breaks, access to calm space).",
  "SPECIALIST: where acoustics or equipment are the issue for a child with hearing or visual impairment, ask the Visiting Teacher service and audiology/ophthalmology to advise; do not specify equipment yourself.",
  "DO NOT recommend isolating a child permanently at a separate desk as a behaviour strategy; any separate space must be planned, time-limited and reviewed.",
 ],
 "explain_parent": [
  "'Part of what I looked at was the classroom itself — where she sits, how noisy it gets, what's on the walls. Small changes there can make a real difference and help other children too.'",
  "'At home, homework might go better at a clear table away from the TV. It's the same idea.'",
 ],
 "explain_teacher": [
  "'When I watched, he was fine in whole-class teaching and lost it in group work — the noise in the room doubled. Could he try the table by the wall for group tasks for three weeks?'",
  "'The display behind you is lovely, but it's exactly where his eyes go when you talk. Could the teaching wall be kept plainer?'",
 ],
 "explain_child": [
  "YOUNGER: 'Show me on this picture of your classroom where it's easy to listen, and where it's hard.'",
  "OLDER: 'Which rooms in the school do you find easiest to work in? What's different about them?'",
  "ASK: 'If you could change one thing about your classroom, what would it be?'",
 ],
 "red_flags": [
  "WATCH — a child who covers ears, hides under tables or bolts from the room: consider sensory over-responsiveness, anxiety, or something happening in the room (bullying, a particular adult). Observe before concluding.",
  "WATCH — suspected hearing or visual difficulty: recommend GP referral to audiology or ophthalmology before any cognitive assessment.",
  "BOUNDARY — building works, room allocation and furniture are Board of Management decisions; the EP describes the need.",
 ],
 "questions": [
  "Q: 'We can't change the building — what's the point?' A: 'Most of what I'm suggesting is about where he sits, what's on the wall behind you and how you signal changes. Those are free.'",
  "Q: 'Won't moving her to the front single her out?' A: 'It can, if it's done as a punishment. Done as part of a seating plan for everyone, children rarely notice.'",
  "Q: 'Is this a sensory processing disorder?' A: 'I'm describing how he responds to this room. If there's a wider sensory question, the OT on the CDNT or Primary Care is the right person to look at it.'",
 ],
 "supervision": [
  "Bring an observation where you wrote about the room as well as the child. Did your recommendations change as a result?",
  "Discuss how to feed back environmental findings to a teacher without it sounding like criticism of their classroom.",
 ],
 "citations": [
  "Barrett, P., Davies, F., Zhang, Y., & Barrett, L. (2015). The impact of classroom design on pupils' learning: Final results of a holistic, multi-level analysis. Building and Environment, 89, 118–133.",
  "Fisher, A. V., Godwin, K. E., & Seltman, H. (2014). Visual environment, attention allocation, and learning in young children: When too much of a good thing may be bad. Psychological Science, 25(7), 1362–1370.",
  "Shield, B. M., & Dockrell, J. E. (2003). The effects of noise on children at school: A review. Building Acoustics, 10(2), 97–116.",
  "Frederickson, N., & Cline, T. (2015). Special educational needs, inclusion and diversity (3rd ed.). Open University Press.",
 ],
})

# ---------------------------------------------------------------- 3
PRES.append({
 "name": "Teaching match",
 "neps": NEPS_56,
 "related_to": ["Dyslexia", "Intellectual Disability", "Literacy difficulty not meeting SLD criteria", "Giftedness / exceptional ability", "ADHD"],
 "what_it_is": [
  "Part D wording: 'Teaching match — Context, not a diagnosis'. The fit between the level, pace and method of what is being taught and where the child actually is — too hard, too easy, too fast, or in a form the child cannot access.",
  "Gickling and Armstrong (1978) found that on-task behaviour, task completion and comprehension were best when material was at an 'instructional' level of difficulty and fell away when it was at 'frustration' level. Their instructional-level ratios are often quoted — check the source before quoting a figure.",
  "Haring et al. (1978) described an instructional hierarchy — acquisition, fluency, generalisation, adaptation — so the question is also STAGE: a child still acquiring a skill needs modelling and feedback; a child who is accurate but slow needs practice, not re-teaching.",
  "Rosenshine (2012) summarised principles of effective instruction (small steps, modelling, guided practice, checking for understanding, high success rate) — a useful checklist for what 'match' looks like in practice.",
 ],
 "what_it_is_not": [
  "NOT a judgement on teaching quality. A skilled teacher with 30 pupils and a wide range of need will have mismatches; the EP's job is to find this child's.",
  "NOT only 'too hard'. Work well below a child's level produces disengagement and behaviour that looks like a problem in the child (see 'Giftedness / exceptional ability').",
  "NOT the same as 'Instruction history' (what has been taught over time) or 'Curriculum demands' (what the programme requires). Teaching match is what happens in the lesson today.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: play-based activities pitched beyond the child's language or attention level; watch whether the child joins, watches, or wanders.",
  "SCHOOL AGE 6–12: the class reader or maths page is at frustration level; the child copies, avoids, or acts out. Often the first sign of an unidentified literacy difficulty.",
  "ADOLESCENT 13–16: subject teaching assumes reading and writing levels the pupil does not have; mismatch varies subject by subject. Part D: 'Subject-by-subject variation · streaming and subject choice'.",
  "YOUNG ADULT 17–26: course level and pace; lecture-based teaching without scaffolds.",
  "SPECIAL SETTING: the risk may be under-challenge — repeated activities the child has mastered. Check whether targets move.",
 ],
 "assess": [
  "WORK SAMPLE AT THE CHILD'S DESK: take the text or task the child was given today and have them read or do a short section. Note accuracy and how they respond to error.",
  "CURRICULUM-BASED PROBE: compare performance on class material with performance on easier material. If behaviour improves with easier material, match is part of the formulation.",
  "OBSERVE A LESSON for the instructional stage: is the child being taught something new (acquisition) while still needing practice on the last thing (fluency)?",
  "ASK THE TEACHER what the child can do independently, with help, and not yet — and compare with your own assessment.",
 ],
 "recommendations": [
  "PITCH TO SUCCESS: set independent work where the child can succeed most of the time with effort; keep harder material for supported teaching (Gickling & Armstrong, 1978; Rosenshine, 2012).",
  "MATCH THE STAGE: modelling and corrective feedback for new skills; brief, frequent practice for accurate-but-slow skills; varied examples for generalisation (Haring et al., 1978).",
  "DIFFERENTIATE ACCESS, NOT CONTENT, where possible: the same topic through an easier text, audio, or a partner reader, so the child stays with the class.",
  "CONTINUUM LEVEL: Classroom Support (differentiated tasks) to School Support (targeted teaching in the Student Support Plan at the child's instructional level).",
  "MEASURE: name what will show better match — e.g., proportion of independent tasks completed, accuracy on class text — and review after 6–8 weeks.",
  "DO NOT attribute off-task behaviour to attention or motivation until you have checked whether the work was at the child's level.",
 ],
 "explain_parent": [
  "'When the work is at the right level — hard enough to learn from but not so hard he can't start — he works well. The plan is to get more of his work into that zone.'",
  "'Some of the behaviour at school happens when the work is too hard. That's useful to know, because it's something we can change.'",
 ],
 "explain_teacher": [
  "'With the class reader she was getting about one word in five wrong and started rocking her chair. With the easier book she read for ten minutes. The book was the difference.'",
  "'He's accurate on number bonds but slow — so more re-teaching won't help. Short daily practice will.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some work is too easy, some is just right, some is too tricky. Show me which pile this goes in.'",
  "OLDER: 'Which subjects feel like the work is pitched right for you, and which feel like they're going too fast?'",
  "ASK: 'When the work is too hard, what do you do?'",
 ],
 "red_flags": [
  "WATCH — a child consistently working at frustration level across subjects: check for an unidentified learning, language or sensory difficulty rather than assuming effort.",
  "WATCH — behaviour escalating in one subject only: look at the match in that class before a whole-school behaviour plan.",
  "BOUNDARY — you describe the match; teaching methods and grouping are the school's professional decisions.",
 ],
 "questions": [
  "Q: 'Won't giving him easier work hold him back?' A: 'Independent work he can't do teaches him nothing. He's taught the harder material with support, and practises on work he can do.'",
  "Q: 'Isn't this just differentiation?' A: 'Yes — what I'm adding is a measure of where his level is, so the differentiation is aimed.'",
  "Q: 'Why does she behave for the SET and not in class?' A: 'In the SET group the work is at her level. That tells us the difficulty is partly the match, which is good news — it's changeable.'",
 ],
 "supervision": [
  "Bring a case where changing the task changed the behaviour. How did you present that to the school without it sounding like blame?",
  "Discuss how you would check instructional level at post-primary, where you might see only one or two subjects.",
 ],
 "citations": [
  "Gickling, E. E., & Armstrong, D. L. (1978). Levels of instructional difficulty as related to on-task behavior, task completion, and comprehension. Journal of Learning Disabilities, 11(9), 559–566.",
  "Haring, N. G., Lovitt, T. C., Eaton, M. D., & Hansen, C. L. (1978). The fourth R: Research in the classroom. Charles E. Merrill.",
  "Rosenshine, B. (2012). Principles of instruction: Research-based strategies that all teachers should know. American Educator, 36(1), 12–19, 39.",
 ],
})

# ---------------------------------------------------------------- 4
PRES.append({
 "name": "Curriculum demands",
 "neps": NEPS_56,
 "related_to": ["Intellectual Disability", "DLD", "Dyslexia", "ADHD", "Autism"],
 "what_it_is": [
  "Part D wording: 'Curriculum demands — Context, not a diagnosis'. What the programme itself asks of the child at this stage — the language load, the reading and writing volume, the abstraction, the pace of coverage, the assessment format — set against the child's profile.",
  "In Ireland the frame is the Primary Curriculum Framework (NCCA, 2023) at primary, and the Framework for Junior Cycle (DES, 2015) at post-primary, which includes Level 1 and Level 2 Learning Programmes (L1LPs and L2LPs) for some pupils with general learning disabilities — check current NCCA eligibility guidance.",
  "Demands shift at known points: the move from learning to read to reading to learn in middle primary; the jump in subject vocabulary and written output at post-primary; exam-focused senior cycle. Many referrals cluster at these points.",
  "Sweller's (1988) cognitive load theory explains why the same child can manage a task in one form and not another: unnecessary complexity in how material is presented uses up working memory needed for the learning itself.",
 ],
 "what_it_is_not": [
  "NOT a within-child difficulty. A child who coped until Fourth Class may not have changed; the demands have.",
  "NOT the same as 'Teaching match' (how today's lesson is pitched). Curriculum demands are what the programme requires regardless of who teaches it.",
  "NOT a reason to lower expectations wholesale. The question is which demands are essential to the learning and which are barriers to it (e.g., copying from the board in history).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: Aistear sets a play-based framework; demands are mainly language, attention and social. Watch for formal tasks pushed down too early.",
  "SCHOOL AGE 6–12: vocabulary, reading comprehension and written output demands climb; maths moves from concrete to abstract. Children with DLD or dyslexia often surface here.",
  "ADOLESCENT 13–16: many subjects, each with its own vocabulary; more reading and writing per day; assessment through Classroom-Based Assessments and final exams. Subject choice and level (Higher/Ordinary) become live decisions.",
  "YOUNG ADULT 17–26: Leaving Certificate, LCA, further education and training, third level — course choice should follow the profile.",
  "SPECIAL SETTING: curriculum route (L1LP, L2LP, adapted mainstream) is itself the question; check the route is reviewed, not fixed at entry.",
 ],
 "assess": [
  "TASK ANALYSIS of one real demand: take tomorrow's history homework or maths page and list what it requires — reading level, vocabulary, steps, writing volume, time.",
  "COMPARE WITH THE PROFILE: set the task analysis beside the child's cognitive, language and attainment profile. Where they clash is the formulation.",
  "ASK ABOUT TIMING: when did concern start, and what changed in the curriculum at that point?",
  "AT POST-PRIMARY: ask for the pupil's timetable and look subject by subject; ask which subjects are going well and why.",
 ],
 "recommendations": [
  "SEPARATE THE ESSENTIAL FROM THE BARRIER: keep the learning objective; change the access route (audio, reduced copying, key-word glossary, graphic organisers).",
  "PRE-TEACH subject vocabulary before a new topic, particularly for pupils with language difficulty or EAL.",
  "REDUCE EXTRANEOUS LOAD: clear worked examples, one task per page, instructions in numbered steps (Sweller, 1988).",
  "CURRICULUM ROUTE: where a pupil has a general learning disability, recommend that the school consider L1LP/L2LP or reduced subject load against current NCCA and Department guidance — the decision is the school's with the family. Exemption from Irish follows its own circular and criteria — check the current version.",
  "CONTINUUM LEVEL: Classroom Support for access adjustments; School Support or School Support Plus for curriculum route decisions, recorded in the Student Support Plan.",
  "DO NOT recommend a curriculum route or subject level on the basis of a single score; describe the profile and the demands, and let the school decide with the family.",
 ],
 "explain_parent": [
  "'Nothing has gone wrong with him since last year — the work has changed. There's much more reading in every subject now, and that's where his difficulty shows.'",
  "'The school can keep him learning the same content with different ways in, like listening to the chapter before reading it.'",
 ],
 "explain_teacher": [
  "'Her maths reasoning is fine; the word problems are the barrier because of the reading load. Can we read them aloud and see what she does?'",
  "'The copying from the board is using up all his effort. Could he get the notes printed so he can spend the time on the geography?'",
 ],
 "explain_child": [
  "YOUNGER: 'Which work in school feels hardest? Show me one.'",
  "OLDER: 'Which subjects have the most reading or writing? Which ones do you actually like when you get past that?'",
  "ASK: 'If you could get the same information a different way — listening, pictures, videos — which would you pick?'",
 ],
 "red_flags": [
  "WATCH — a sudden drop at a known transition point (Third–Fourth Class, First Year) with no other explanation: consider an unidentified language or literacy difficulty.",
  "WATCH — a pupil placed on a reduced or alternative curriculum without review: check it still fits.",
  "BOUNDARY — curriculum route, subject level and exemption decisions belong to the school and family under Department guidance; the EP informs.",
 ],
 "questions": [
  "Q: 'Should she drop to Ordinary Level?' A: 'That's a decision for you and the school. What I can tell you is where her strengths are and which demands are hardest, subject by subject.'",
  "Q: 'Why was he fine in Second Class?' A: 'The reading demand jumped. His difficulty was there; the curriculum didn't need as much reading then.'",
  "Q: 'Is L2LP the right route?' A: 'It's designed for a specific group of learners with criteria set by the NCCA and Department. I'll describe his profile; the school applies the current guidance.'",
 ],
 "supervision": [
  "Bring a task analysis of one real curriculum demand and discuss how it changed your recommendations.",
  "Ask about local practice on L1LP/L2LP and Irish exemption questions — what the EP is and isn't asked to contribute.",
 ],
 "citations": [
  "National Council for Curriculum and Assessment. (2023). Primary curriculum framework: For primary and special schools. NCCA.",
  "Department of Education and Skills. (2015). Framework for Junior Cycle 2015. DES.",
  "Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257–285.",
  "National Council for Curriculum and Assessment. (2009). Aistear: The early childhood curriculum framework. NCCA. — check for the updated framework.",
 ],
})

# ---------------------------------------------------------------- 5
PRES.append({
 "name": "Attendance and transitions",
 "neps": NEPS_56,
 "related_to": ["Emotionally Based School Avoidance (EBSA)", "Anxiety disorders", "Autism", "Chronic illness", "Interrupted or missed schooling"],
 "what_it_is": [
  "Part D wording: 'Attendance and transitions — Context, not a diagnosis'. The pattern of the child's presence in school (days absent, late arrivals, partial days, reduced timetables) and how they manage everyday transitions — arrival, between lessons, after break, after holidays or illness.",
  "Attendance is described, not diagnosed: WHEN (days, times, after weekends or holidays), WHY (illness, family, avoidance, exclusion, reduced days), and what happens on the way in.",
  "Kearney and Graczyk (2014) proposed a tiered (response-to-intervention) model for attendance: universal promotion for all, targeted support for emerging absence, intensive planning for chronic absence — which maps onto the Continuum of Support.",
  "Statutory frame: under the Education (Welfare) Act 2000, s.21(4), the principal notifies Tusla Education Support Service (TESS) when a pupil's absences total not less than 20 days in a school year. Circular 0047/2021 (in effect from 01/01/2022) governs reduced school days and requires notification to TESS. The circular also required NCSE notification for pupils with SEN, but since 21/09/2023 the NCSE portal is closed; schools notify TESS only, which shares the information with the NCSE. Check current guidance.",
 ],
 "what_it_is_not": [
  "NOT the same as EBSA. Emotionally based school avoidance is one cause; illness, caring roles, family circumstances, bullying, exclusion and unmet learning need are others. Describe the pattern before naming a cause.",
  "NOT only whole days. Late arrival, missing the same lesson each week, or long periods in the office or SNA room are attendance data too.",
  "NOT solved by a reduced timetable on its own. A reduced day is a short-term measure with a plan to return, not an intervention (Circular 0047/2021 — check current wording).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool attendance is not compulsory; compulsory school age is 6 (Education (Welfare) Act 2000). Separation difficulty at drop-off is common and usually settles; persistence with distress is worth describing.",
  "SCHOOL AGE 6–12: Monday and post-holiday patterns; morning somatic complaints; the child who arrives but cannot enter the classroom. Parent capacity to get the child in is part of the picture.",
  "ADOLESCENT 13–16: selective lesson absence, lateness, leaving at lunch; peer and bullying factors; caring roles at home. Absence can accelerate quickly in First and Second Year.",
  "YOUNG ADULT 17–26: course non-attendance and dropping out; adult consent applies and school-based routes no longer do.",
  "SPECIAL SETTING: transport, medical appointments and health needs can drive absence; transitions within the day (bus to class, class to therapy) may be the main difficulty.",
 ],
 "assess": [
  "GET THE DATA: attendance records by day and session for the last year at least; plot them. Look for day-of-week, subject and post-holiday patterns.",
  "MAP THE MORNING: with the parent, walk through the morning from waking to the classroom door — where does it break down?",
  "PUPIL VOICE: what makes coming in harder or easier; which parts of the day are hardest; who they would go to. Scaling or a 'school day ladder' works for most ages.",
  "CHECK FUNCTION AND CAUSE: anxiety, avoidance of a specific demand, bullying, illness, caring roles, a parent's needs. Use the NEPS attendance guidance to structure this (NEPS, n.d. — check the year and current version on gov.ie).",
 ],
 "recommendations": [
  "UNIVERSAL: a warm, predictable arrival routine; a named adult at the door; attendance followed up on the first day of absence (Kearney & Graczyk, 2014).",
  "SCHOOL SUPPORT: an attendance plan in the Student Support Plan with a graded return where needed, a key adult, a safe base, and agreed responses to a difficult morning — reviewed fortnightly with the family.",
  "TRANSITIONS WITHIN THE DAY: visual timetable, warning before changes, a planned route between rooms for post-primary pupils, and a consistent re-entry routine after break.",
  "SCHOOL SUPPORT PLUS: where absence is persistent or linked to mental health, involve TESS (Educational Welfare Officer), and GP/Primary Care or CAMHS as indicated; the school meets its statutory notification duties.",
  "REDUCED DAYS: only with parental consent, a return-to-full-time plan, a time limit and notification as required (Circular 0047/2021 — check).",
  "DO NOT frame the parent as the problem in writing; describe what happens on school mornings and what support the family needs.",
 ],
 "explain_parent": [
  "'Looking at the dates, most of the missed days are Mondays and the day after holidays. That tells us the hard part is getting back into the routine, so that's where we'll start.'",
  "'The school is required to let the Educational Welfare service know when absence reaches certain levels. That isn't a punishment — they're also there to help.'",
 ],
 "explain_teacher": [
  "'The first five minutes of the day are the whole intervention for her. If the same person meets her at the door every morning, the rest follows more often.'",
  "'When he's absent, a same-day call saying \"we missed you\" works better than a letter a week later.'",
 ],
 "explain_child": [
  "YOUNGER: 'Let's draw your morning, from waking up to sitting in class. Where does it get hard?'",
  "OLDER: 'On a scale of 0–10, how hard is it to come in on a Monday? What would make it one point easier?'",
  "ASK: 'Is there a part of the school day, or a person, you're trying to avoid?'",
 ],
 "red_flags": [
  "RED FLAG — absence linked to disclosure or signs of abuse, neglect, domestic violence or self-harm: same-day child protection or risk route; Tusla report as soon as practicable.",
  "WATCH — a child missing from education with no registration for home education: this is a TESS matter (Education (Welfare) Act 2000).",
  "WATCH — absence driven by bullying: the school's Bí Cineálta procedures apply alongside any attendance plan.",
  "BOUNDARY — statutory attendance action belongs to TESS; the EP formulates and advises.",
 ],
 "questions": [
  "Q: 'Should we just let him stay home until he's ready?' A: 'Long breaks usually make return harder. A small, planned step back in — even an hour — tends to work better than waiting.'",
  "Q: 'Can we put her on a shorter day?' A: 'Only as a short step with a plan to return, your consent, and notification as the guidance requires. It isn't a long-term solution.'",
  "Q: 'Is the attendance officer going to take us to court?' A: 'The school must notify them at certain levels; their first job is to work with you. I'd rather they were involved early as support.'",
 ],
 "supervision": [
  "Bring an attendance chart you plotted and discuss what the pattern suggests — and what you might be missing.",
  "Discuss how to hold both the statutory duty and a supportive relationship with a family whose child is not attending.",
 ],
 "citations": [
  "Kearney, C. A., & Graczyk, P. (2014). A response to intervention model to promote school attendance and decrease school absenteeism. Child & Youth Care Forum, 43(1), 1–25.",
  "Education (Welfare) Act 2000, No. 22 of 2000 (Ireland).",
  "Department of Education. (2021). Circular 0047/2021: Guidelines for the use of reduced school days in schools. Department of Education. — check for updates.",
  "National Educational Psychological Service. (n.d.). Managing reluctant attendance and school avoidance behaviour: A good practice guide for primary schools. Department of Education. (Post-primary version also published — check the year on gov.ie before citing.)",
 ],
})

# ---------------------------------------------------------------- 6
PRES.append({
 "name": "Transition planning (early years to primary, primary to post-primary, school leaver)",
 "neps": NEPS_56,
 "related_to": ["Autism", "Intellectual Disability", "Anxiety disorders", "DLD", "Physical disability"],
 "what_it_is": [
  "Part D wording: 'Transition planning (early years to primary, primary to post-primary, school leaver) — Not a diagnosis'. The planned movement of a child between settings, and the information, relationships and supports that need to travel with them.",
  "Three main points in Irish practice: PRESCHOOL TO PRIMARY (NCCA Mo Scéal templates share information from the ECCE setting); PRIMARY TO POST-PRIMARY (the NCCA Education Passport, including the Sixth Class report and the child's 'My Profile'); SCHOOL LEAVER (further education, training, third level via DARE, employment, or HSE adult day services).",
  "Evangelou et al. (2008) found successful primary–secondary transition linked to making new friends, growing in confidence, settling into routines, showing interest in school, and experiencing curriculum continuity — pupils with SEN were among those more likely to find it hard.",
  "Supports held in one setting (AIM, SNA access, a key adult, an informal understanding) do NOT transfer automatically — they have to be planned and, where resources are involved, re-applied for.",
 ],
 "what_it_is_not": [
  "NOT a single visit in June. Transition is a process that starts a year or more ahead for pupils with complex needs.",
  "NOT only about the child. Parents' anxiety, the receiving school's readiness and the information flow between settings are all part of it.",
  "NOT the same as 'Attendance and transitions', which is about everyday transitions and attendance patterns; this is about moving setting.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: ECCE to Junior Infants; AIM supports end at school entry; the receiving school needs the preschool's knowledge. Enrolment and, where needed, special class or SNA application begin early — check local timelines.",
  "SCHOOL AGE 6–12: Fifth and Sixth Class — post-primary applications, choosing a school with the right supports, special class places. Part D: map it before the child hits it.",
  "ADOLESCENT 13–16: First Year settling; change of school; move to or from a special class. Service transitions at 16 and 18 are live — Part D: 'map them before the young person hits them.'",
  "YOUNG ADULT 17–26: school leaving — CAO/DARE applications, further education, training, HSE school-leaver process for adult day services, CAMHS to adult mental health services. Check current DARE rules and dates each year.",
  "SPECIAL SETTING: school leaving at 18 from special school; transition to adult services requires early profiling and family planning — check local HSE process.",
 ],
 "assess": [
  "MAP THE SUPPORTS NOW: list every support the child has (formal and informal) and ask for each: will this continue after the move? Who has to act?",
  "PUPIL VOICE: what they are looking forward to, what worries them, what they want the new school to know. A one-page profile written with the child travels well.",
  "RECEIVING SETTING: what does it know, and what can it offer? Visit or phone where possible, with consent.",
  "PARENT PERSPECTIVE: their questions and their own experience of school — parental anxiety often shapes the child's.",
 ],
 "recommendations": [
  "START EARLY: for children with complex needs, begin transition planning at least a year ahead; name who is responsible in each setting.",
  "INFORMATION THAT TRAVELS: Mo Scéal or Education Passport completed carefully; with consent, a short summary of what works, not only what is wrong; a one-page profile in the child's words.",
  "GRADED FAMILIARISATION: visits, photographs of key places and people, the timetable in advance, a named key adult in the new school, a buddy system.",
  "RE-APPLY FOR RESOURCES in time: SNA access and special class places are applied for by the receiving school or through the SENO/NCSE; AIM does not continue into primary. Check timelines locally.",
  "CONTINUUM LEVEL: School Support for most planned transitions; School Support Plus where several services are involved and a transition meeting is needed.",
  "DO NOT assume a support will follow the child; DO NOT promise a placement or resource another body allocates.",
 ],
 "explain_parent": [
  "'The new school won't automatically know what works for him. We'll make sure a short, clear summary goes with him, with your consent.'",
  "'Things like SNA access don't transfer — the new school has to apply. That's why we start now rather than in June.'",
  "SIGNPOST: SENO for placement and SNA questions; the post-primary school's guidance counsellor; DARE information for third level; the local HSE disability service for adult services.",
 ],
 "explain_teacher": [
  "'Can you tell me what you know about her that isn't in any report — who she goes to, what calms her, what sets her off? That's what the new school needs most.'",
  "'A photo booklet of the new school and a named person there makes a big difference for him over the summer.'",
 ],
 "explain_child": [
  "YOUNGER: 'Soon you'll go to big school. Let's make a book with pictures of it so you know what it looks like.'",
  "OLDER: 'What do you want your new teachers to know about you? What don't you want them to know?'",
  "ASK: 'What are you most looking forward to, and what's the biggest worry?'",
 ],
 "red_flags": [
  "WATCH — a young person approaching 18 with no plan for adult services or post-school education: raise it in writing with the school and family.",
  "WATCH — refusal to attend the new setting or rapid decline after transfer: review early, before patterns set.",
  "BOUNDARY — placement, special class allocation, DARE eligibility and adult service places are decided by others; you advise and describe.",
 ],
 "questions": [
  "Q: 'Should he go to a special class or mainstream post-primary?' A: 'That's your decision with the schools and the SENO. I can describe what he needs and which settings are likely to provide it.'",
  "Q: 'Will his SNA come with him?' A: 'No, SNA access doesn't transfer — the new school applies. We'll make sure the information about his care needs is clear.'",
  "Q: 'What happens when she leaves school at 18?' A: 'There's a planning process with the local HSE disability service, and it needs to start well before. I'd ask the school to check the local timeline this year.'",
 ],
 "supervision": [
  "Bring the local facts you are unsure of — how HSE school-leaver profiling runs here, which post-primary schools have special classes, this year's DARE dates.",
  "Discuss consent for information-sharing between schools and how you decide what goes in a transition summary.",
 ],
 "citations": [
  "Evangelou, M., Taggart, B., Sylva, K., Melhuish, E., Sammons, P., & Siraj-Blatchford, I. (2008). What makes a successful transition from primary to secondary school? (Research Report DCSF-RR019). Department for Children, Schools and Families.",
  "National Council for Curriculum and Assessment. (n.d.). Mo Scéal: Supporting the transition from preschool to primary school. NCCA. (Check the current materials and date.)",
  "National Council for Curriculum and Assessment. (n.d.). Education Passport: Supporting the transfer from primary to post-primary school. NCCA. (Check the current materials and date.)",
 ],
})

# ---------------------------------------------------------------- 7
PRES.append({
 "name": "Assistive technology",
 "neps": NEPS_56,
 "related_to": ["Dyslexia", "Developmental Coordination Disorder (dyspraxia)", "Visual impairment", "Physical disability", "Autism"],
 "what_it_is": [
  "Part D wording: 'Assistive technology — Not a diagnosis'. The whole question of AT as an access factor: what the child has, whether it matches the need, whether it is actually used, and whether it continues across classes, home, exams and transitions. (For the specific omission of AT never tried, see 'Assistive technology not yet trialled'.)",
  "Ranges from low-tech (reading rulers, pencil grips, slant boards) through mainstream tools (built-in dictation, read-aloud, word prediction, keyboards) to specialist equipment (switch access, eye gaze, braille devices, FM/radio aids). AAC is covered separately in 'AAC and communication access'.",
  "Zabala's SETT framework asks about the STUDENT, ENVIRONMENTS, TASKS and only then TOOLS — the tool is chosen last, to fit the task and setting (Zabala, 2005).",
  "Phillips and Zhao (1993) found AT abandonment linked to lack of user involvement in selection, poor device performance, and changes in the user's needs or priorities — which is why use, not provision, is the thing to assess.",
 ],
 "what_it_is_not": [
  "NOT the device. A laptop in a cupboard is not assistive technology in any useful sense; the training, set-up and daily routine are part of it.",
  "NOT an EP equipment prescription. Specialist AT for physical, sensory or communication needs is assessed by OT, SLT, the Visiting Teacher service or specialist services; the EP describes the learning task it must support.",
  "NOT only for literacy. AT supports organisation (digital planners, reminders), attention (timers), communication and physical access.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: mostly low-tech and play-based; switch toys and cause-and-effect for children with physical needs; AAC questions via the CDNT SLT.",
  "SCHOOL AGE 6–12: keyboarding taught explicitly; read-aloud and dictation introduced for content access; rules about when AT is used in class need to be clear.",
  "ADOLESCENT 13–16: AT becomes central for volume of reading and writing; consistency across many subject teachers is the main challenge; exam use must match normal classroom practice (see RACE).",
  "YOUNG ADULT 17–26: third-level disability services and AT training; ownership of the device and skills passes to the young person.",
  "SPECIAL SETTING: switch access, eye gaze and specialist communication devices; staff training and device maintenance are often the gaps. Check who owns the device and who trains new staff.",
 ],
 "assess": [
  "INVENTORY: what AT does the pupil have, who provided it, when, and who trained them? Is it charged, set up and in the classroom?",
  "OBSERVE USE across settings: is it used in all subjects or only in the SET room? Does the teacher's routine make room for it?",
  "TASK MATCH (SETT): for the key tasks (reading texts, writing answers, organising work), does the tool reduce the barrier? Compare with and without on a short task.",
  "PUPIL VIEW: does the young person want to use it? Stigma and speed are the common reasons for refusal.",
 ],
 "recommendations": [
  "MATCH TOOL TO TASK: name the task each tool supports (e.g., read-aloud for history textbook; dictation for English essays) rather than recommending AT in general (Zabala, 2005).",
  "EMBED IN CLASS ROUTINE: agree across subject teachers when and how the AT is used; it must be normal classroom practice to count for exams and to become fluent.",
  "TRAINING PLAN: who teaches the pupil, who supports staff, and who maintains the device; include parents where the device goes home.",
  "FUNDING AND SPECIALIST INPUT: specialist equipment for pupils with physical or communicative disabilities is applied for by the school through the SENO under the Department's AT scheme — check the current circular and criteria. Ask OT/SLT/Visiting Teacher to advise on specialist devices.",
  "CONTINUUM LEVEL: School Support (AT use named in the Student Support Plan with review); School Support Plus where specialist equipment and external services are involved.",
  "DO NOT recommend a specific commercial product as though it were the only option, and DO NOT recommend a device without a plan for training, review and transition.",
 ],
 "explain_parent": [
  "'The laptop helps only if she uses it every day in every class. We're going to agree with her teachers when she uses it, so it becomes normal.'",
  "'If he's going to use it in the State exams later, it has to be how he normally works in school — that's another reason to start now.'",
  "SIGNPOST: the school's SET coordinator; SENO for specialist equipment; the CDNT OT/SLT for specialist devices.",
 ],
 "explain_teacher": [
  "'He has the tablet but uses it only in the SET room. Could your class be one where he uses it for all written work this term?'",
  "'The read-aloud function is already on the school laptops. It's a setting, not a purchase.'",
 ],
 "explain_child": [
  "YOUNGER: 'This can read the story to you while you follow with your finger. Want to try?'",
  "OLDER: 'Some people find dictation faster than typing or handwriting. What would make you actually want to use it in class?'",
  "ASK: 'What's annoying about the laptop? What would you change?'",
 ],
 "red_flags": [
  "WATCH — AT provided but unused for months: check training, set-up, stigma and whether the tool matches the task.",
  "WATCH — AT use stopped at transition to a new school or class: continuity was not planned.",
  "BOUNDARY — specialist AT assessment (seating, switches, eye gaze, AAC) belongs to OT, SLT and specialist services; funding decisions sit with the Department/SENO.",
 ],
 "questions": [
  "Q: 'Should we buy him a particular program?' A: 'Start with the built-in tools and see which tasks they help. If there's a specific need they don't meet, the school or OT can advise on specialist software.'",
  "Q: 'She refuses to use it in front of her friends.' A: 'That's common. Using it in every class, and letting other pupils use similar tools, usually reduces the stigma. Ask her what would help.'",
  "Q: 'Who fixes it when it breaks?' A: 'That needs to be written into the plan — who owns it, who maintains it, and who to contact.'",
 ],
 "supervision": [
  "Discuss the boundary between recommending the learning task AT should support and recommending specific equipment — where does this service draw it?",
  "Ask about the current Department AT scheme, how applications link with SENOs locally, and typical timescales.",
 ],
 "citations": [
  "Zabala, J. S. (2005). Ready, SETT, go! Getting started with the SETT framework. Closing the Gap, 23(6), 1–3.",
  "Phillips, B., & Zhao, H. (1993). Predictors of assistive technology abandonment. Assistive Technology, 5(1), 36–45.",
  "Wood, S. G., Moxley, J. H., Tighe, E. L., & Wagner, R. K. (2018). Does use of text-to-speech and related read-aloud tools improve reading comprehension for students with reading disabilities? A meta-analysis. Journal of Learning Disabilities, 51(1), 73–84.",
 ],
})

# ---------------------------------------------------------------- 8
PRES.append({
 "name": "Reasonable Accommodations in State Examinations (RACE)",
 "neps": NEPS_56,
 "related_to": ["Dyslexia", "Specific Learning Disorder with impairment in written expression (dysgraphia)", "Developmental Coordination Disorder (dyspraxia)", "Visual impairment", "Hearing impairment"],
 "what_it_is": [
  "Part D wording: 'Reasonable Accommodations in State Examinations (RACE) — Not a diagnosis'. The State Examinations Commission's scheme is formally 'Reasonable Accommodations at the Certificate Examinations' — arrangements at Junior and Leaving Certificate that remove barriers to showing what a candidate knows, without changing what is assessed.",
  "WHO DOES WHAT: the school applies and, for learning-difficulty grounds, carries out the required testing; the SEC decides. The SEC's 2026 Instructions state that a psychological report is not required, a professional report's recommendation does not confer eligibility, and cognitive ability scores and diagnosis are not needed for learning-difficulty grounds (SEC, 2025, sections 4.1(b) and 9.1). Check the current year's edition.",
  "Accommodation families include reading support (reading assistance, exam reading pen, individual reader), writing support (word processor, recording device, scribe only in very exceptional circumstances), a spelling, grammar and punctuation waiver in language subjects, special centres and rest breaks, and supports on hearing, visual and physical grounds (SEC, 2025, section 5.1). Check the current list.",
  "It is a needs-based scheme: accommodations should reflect how the pupil normally works in school (SEC, 2025). For the evidence-gathering itself, see the Part G tool entry 'Access arrangements evidence (RACE)'.",
 ],
 "what_it_is_not": [
  "NOT an assessment and NOT secured by a report. Implying a psychological report is required, or will secure an accommodation, is wrong under the current Instructions.",
  "NOT a promise. No one outside the SEC can tell a family a pupil 'will get a reader'. Eligibility criteria (history, intervention, error rates, attainment, time windows) are set out in section 9 of the current Instructions and change — never quote them from memory.",
  "NOT for everything. The SEC states that trauma and life adversity are outside RACE's scope; other arrangements (special centres, rest breaks, deferred examinations where eligible) may apply (SEC, 2025, section 5.6). Check current wording.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: N/A.",
  "SCHOOL AGE 6–12: not directly relevant, but the habits RACE relies on — keyboarding, use of a reader or reading pen, recorded evidence of difficulty and intervention — are built here.",
  "ADOLESCENT 13–16: Junior Cycle applications. The recommendation that matters at 13–15 is often keyboard or recording-device training, since the SEC expects scribes at Junior Cycle to move towards word processors or recording devices by Leaving Certificate (SEC, 2025, section 4.1).",
  "YOUNG ADULT 17–26: Leaving Certificate; Junior Cycle accommodations are generally reactivated on the school's confirmation of continuing need. Third-level exam accommodations are separate — through the college disability service.",
  "SPECIAL SETTING: candidates in special schools and special classes may sit certificate exams or follow L1LP/L2LP routes; check which applies before discussing RACE.",
 ],
 "assess": [
  "START WITH THE STUDENT SUPPORT FILE: history of difficulty, interventions delivered and their effect, how the pupil is accommodated in class and house exams. That is the evidence the scheme builds on.",
  "TRIAL THE ACCOMMODATION IN SCHOOL: a reading pen, word processor or recording device in class and house exams, with a record of what happened. A pupil should not meet an accommodation for the first time in June.",
  "IF YOU HAVE TESTED (e.g., WIAT-III UK, WRAT-5, DASH), give dates and standard scores clearly so the school can check them against the SEC's time window and test list.",
  "PUPIL VIEW: does the young person want the accommodation? A reader in a separate room is not every candidate's preference.",
 ],
 "recommendations": [
  "DESCRIBE THE NEED, NOT THE ENTITLEMENT: 'Her reading accuracy and speed limit her access to exam questions; the school may wish to consider reading supports under the SEC scheme and trial them in house exams.'",
  "BUILD THE NORMAL WAY OF WORKING: recommend keyboarding or recording-device training early at post-primary so the pupil's normal practice matches what the scheme can offer.",
  "TIMING: flag to the school, early in the year, any testing you have done that may be relevant, so closing dates are not missed.",
  "APPEALS: tell families that decisions can be appealed to an Independent Appeals Committee and, after that, a complaint made to the Ombudsman or Ombudsman for Children (SEC, 2025, section 4.1); closing dates are strict — check current dates.",
  "CONTINUUM LEVEL: School Support — exam accommodations sit within the Student Support Plan and reflect everyday classroom access.",
  "DO NOT state eligibility thresholds, promise an accommodation, or recommend an accommodation the pupil has never used in school.",
 ],
 "explain_parent": [
  "'The school applies and the State Examinations Commission decides, using criteria it publishes each year. I can't promise an outcome, but I can help the school understand his needs and start trying supports now.'",
  "'A report from me isn't required and doesn't guarantee anything. What matters most is how he works in school every day.'",
  "SIGNPOST: the school's RACE coordinator or SET; examinations.ie for the current Instructions and appeal dates.",
 ],
 "explain_teacher": [
  "'Could she use the reading pen in your house exams this term? If it helps, that becomes part of her normal way of working, and the evidence is there if the school applies.'",
  "'My scores are dated — can you check they fall within the SEC's time window for this year's application?'",
 ],
 "explain_child": [
  "OLDER: 'Some students use a reading pen or a laptop in exams. It isn't a cheat — it's so the exam tests what you know, not how fast you read. Want to try it in your Christmas tests?'",
  "ASK: 'If you could have one thing that would make exams fairer for you, what would it be?'",
  "ASK: 'Would you rather be in the main hall or a separate room? Why?'",
 ],
 "red_flags": [
  "WATCH — a family told by anyone that a pupil 'will get' an accommodation: correct it gently and early to avoid a crisis in June.",
  "WATCH — exam distress or panic that looks like a mental health difficulty: consider GP/Primary Care referral; RACE may not be the right route.",
  "BOUNDARY — the SEC decides; the school applies; the EP describes need and supports trials. NEPS's role in the scheme is set out in the current Instructions — check it.",
 ],
 "questions": [
  "Q: 'Will he get extra time?' A: 'I can't say. The SEC has been reviewing and piloting changes to extra time — check the SEC website for the current position this year.'",
  "Q: 'Do we need a private psychological report?' A: 'The current SEC Instructions say a psychological report isn't required. The school carries out the testing it needs.'",
  "Q: 'She has a scribe for Junior Cert. Will she keep it?' A: 'The SEC expects students to move towards a word processor or recording device by Leaving Cert where possible, so now is the time to build those skills.'",
 ],
 "supervision": [
  "Bring any case where a family expects a specific accommodation, and rehearse how you will explain the process without promising.",
  "Ask how NEPS supports schools locally with RACE — training, complex cases, quality assurance — and where the trainee fits.",
 ],
 "citations": [
  "State Examinations Commission. (2025). Reasonable accommodations at the 2026 certificate examinations: Instructions for schools. SEC. — sections 4, 5, 6 and 9; check examinations.ie for the current year's edition and the RACE Review page.",
  "National Educational Psychological Service. (2010). A continuum of support for post-primary schools: Guidelines for teachers. Department of Education and Skills. (Check title and date.)",
 ],
})

# ---------------------------------------------------------------- 9
PRES.append({
 "name": "SNA and resource teaching allocation",
 "neps": NEPS_56,
 "related_to": ["Autism", "Intellectual Disability", "Physical disability", "ADHD", "Self-care and independence skills at school"],
 "what_it_is": [
  "Part D wording: 'SNA and resource teaching allocation — Not a diagnosis'. How additional adults are allocated to schools and then deployed around this child: Special Education Teaching (SET) time, and Special Needs Assistant (SNA) support.",
  "SET ALLOCATION: since 2017 schools receive special education teaching allocations based on their educational profile, not on individual diagnoses or assessments, and deploy them by need using the Continuum of Support (Circulars 0013/2017 primary and 0014/2017 post-primary — check current versions; DES, 2017). An individual report is not needed to access SET support.",
  "SNA ALLOCATION: the SNA scheme supports schools to meet the CARE needs of pupils with SEN (Circular 0030/2014 — check current version); the NCSE allocates SNA support to schools. SNAs support care needs; they are not teachers.",
  "DEPLOYMENT MATTERS AS MUCH AS ALLOCATION: the Deployment and Impact of Support Staff (DISS) project in England found pupils with the most support from teaching assistants often made less progress, linked to how support was deployed, not to the assistants themselves (Webster et al., 2016).",
 ],
 "what_it_is_not": [
  "NOT something the EP allocates. SET allocation is set nationally; SNA allocation is an NCSE decision. Allocating an SNA is an NCSE decision against its own criteria, so describe the need rather than name the resource.",
  "NOT 'more adult = better'. Constant one-to-one adult proximity can reduce peer interaction, teacher contact and independence (Webster et al., 2016).",
  "NOT static. Schemes are under review (NCSE, 2018, proposed a new school inclusion model); check the current allocation model before advising.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool additional capacity comes through AIM, not SNA; school SNA access begins on school entry and the school must apply. Check AIM levels with Better Start.",
  "SCHOOL AGE 6–12: common questions about SNA 'for' a child; the task is describing care needs (toileting, feeding, mobility, safety, significant medical needs) and planning SNA support to fade where possible.",
  "ADOLESCENT 13–16: SNA proximity becomes socially costly; independence and discreet support are priorities. SET time spread across subjects.",
  "YOUNG ADULT 17–26: school supports end; college disability services and adult services have their own allocation routes.",
  "SPECIAL SETTING: higher staffing is built into special classes and schools; the question is deployment — who does what, at what times, including breaks and transitions.",
 ],
 "assess": [
  "ASK HOW SUPPORT IS USED, NOT JUST HOW MUCH: a typical day — when is the SNA with the child, what do they do, who teaches the child?",
  "OBSERVE: is the child taught mainly by the teacher or the SNA? How often do they interact with peers? Does the adult hover or step back?",
  "CARE NEEDS: describe them concretely (toileting frequency and support; mobility; safety episodes; medical procedures) so the school can use the description.",
  "SET PLANNING: which targets does SET time address, in which format (in-class, small group, individual), and how is progress measured?",
 ],
 "recommendations": [
  "DESCRIBE NEEDS PRECISELY: 'He needs adult assistance with toileting approximately twice daily and supervision at transitions due to safety concerns' — not 'He needs an SNA'.",
  "TEACHER TEACHES: the pupil with the greatest need should get at least as much teacher time as peers; SNA support is for care and access, not substitute teaching (Webster et al., 2016).",
  "INDEPENDENCE PLAN: SNA support written with a fading plan and review dates in the Student Support Plan.",
  "SET TIME AIMED: targets from the Student Support Plan, delivered in a named format with a progress measure and review (DES, 2017).",
  "CONTINUUM LEVEL: School Support to School Support Plus — allocation and deployment decisions recorded in the Student Support File.",
  "DO NOT write 'requires a full-time SNA' or specify hours; DO NOT imply a report is needed to access SET support.",
 ],
 "explain_parent": [
  "'I can't decide whether he gets an SNA — the NCSE decides on the school's application. What I can do is describe his care needs clearly so the school can use that.'",
  "'An SNA is there to help with care needs, like toileting or safety, not to teach. His teacher is still his teacher — that's the best thing for his learning.'",
 ],
 "explain_teacher": [
  "'When the SNA sits beside him all day, he talks to her and not to the other children. Could she step back during group work and circulate?'",
  "'The school's SET allocation doesn't depend on my report — you can prioritise him now based on his needs.'",
 ],
 "explain_child": [
  "YOUNGER: 'Who helps you in class? What do they help with? What can you do by yourself?'",
  "OLDER: 'How do you feel about having an SNA near you in class? What would you like to do on your own?'",
  "ASK: 'Which help do you actually want, and which do you not need anymore?'",
 ],
 "red_flags": [
  "WATCH — a child taught almost entirely by an SNA or in withdrawal: flag the risk to learning and inclusion.",
  "WATCH — care needs described vaguely in the Student Support File: this makes review and fading impossible.",
  "BOUNDARY — you do not allocate SNA access, SET hours or special class places; you describe needs.",
 ],
 "questions": [
  "Q: 'Can you put in the report that she needs an SNA?' A: 'I'll describe her care needs clearly — that's what the NCSE uses. Naming the resource isn't my decision.'",
  "Q: 'Does he need a diagnosis to get resource teaching?' A: 'No. Since 2017 schools allocate SET time according to need. He can be supported now.'",
  "Q: 'Wouldn't one-to-one all day be best?' A: 'Research suggests constant one-to-one adult support can reduce time with the teacher and other children. We'd rather plan support that helps him do more himself.'",
 ],
 "supervision": [
  "Bring a report paragraph describing care needs; ask your supervisor whether it would be useful to the school and fair to the child.",
  "Ask about the current SNA and SET allocation models and any pilot or review in progress.",
 ],
 "citations": [
  "Department of Education and Skills. (2017). Guidelines for primary schools: Supporting pupils with special educational needs in mainstream schools. DES.",
  "Department of Education and Skills. (2017). Circular 0013/2017: Special education teaching allocation (primary) — and Circular 0014/2017 (post-primary). Check current versions.",
  "Department of Education and Skills. (2014). Circular 0030/2014: The Special Needs Assistant (SNA) scheme to support teachers in meeting the care needs of some children with special educational needs. DES. — check for updates.",
  "National Council for Special Education. (2018). Comprehensive review of the Special Needs Assistant scheme: A new school inclusion model to deliver the right supports at the right time to students with additional care needs. NCSE.",
  "Webster, R., Russell, A., & Blatchford, P. (2016). Maximising the impact of teaching assistants: Guidance for school leaders and teachers (2nd ed.). Routledge.",
 ],
})

# ---------------------------------------------------------------- 10
PRES.append({
 "name": "Home learning environment",
 "neps": NEPS_56,
 "related_to": ["DLD", "Vocabulary gap from limited exposure", "Literacy difficulty not meeting SLD criteria", "Homework completion and follow-through", "Housing and economic problems — DSM-5-TR Z-codes"],
 "what_it_is": [
  "Part D wording: 'Home learning environment — Context, not a diagnosis'. The learning activities, routines, language and resources in the child's home — reading together, talk, play with letters and numbers, space and time for homework, access to books and devices.",
  "The Effective Provision of Pre-School Education (EPPE) project found that what parents DO with children (reading, songs, letters, numbers, library visits) predicted early attainment more strongly than parental occupation or education (Sylva et al., 2004; Melhuish et al., 2008).",
  "Desforges and Abouchaar (2003) concluded that 'at-home' parental involvement has a significant positive effect on attainment, across social classes and ethnic groups — engagement at home matters more than attendance at school events.",
  "It is context for formulation, not a finding about the parent. Every home has strengths; the question is what the home can add, not what it lacks.",
 ],
 "what_it_is_not": [
  "NOT the same as socio-economic status. Many families with limited income provide rich learning at home (Melhuish et al., 2008); income affects resources, not care or aspiration.",
  "NOT a place for judgement in reports. Describe routines and resources neutrally and with the parent's agreement; avoid terms like 'unstimulating' or 'chaotic'.",
  "NOT only about English. Home languages other than English are a strength; parents should be encouraged to talk, read and play in the language they know best.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: talk, shared reading, songs and play are the core; screen time and adult conversation matter. Signpost to library and parent programmes.",
  "SCHOOL AGE 6–12: homework routines, reading together, conversation about school. Shift work, siblings and space can make routines hard.",
  "ADOLESCENT 13–16: study space, device access, and parents' confidence with subjects; parental interest and expectations continue to matter even when direct help declines.",
  "YOUNG ADULT 17–26: study space and financial pressures (part-time work, caring roles); family support for course choice.",
  "SPECIAL SETTING: carry-over of routines, communication systems (visuals, AAC) and self-care skills between school and home; home–school communication books.",
 ],
 "assess": [
  "ASK OPEN QUESTIONS with the parent: 'Tell me about an ordinary evening' — homework, meals, play, reading, screens, sleep.",
  "ASK ABOUT STRENGTHS FIRST: what the family enjoys together, languages spoken, what the child talks about at home.",
  "PRACTICAL BARRIERS: space, internet and devices, parents' own literacy or language, shift work, caring for siblings — with sensitivity.",
  "CHILD'S VIEW: 'Where do you do your homework? Who helps you? What do you like doing at home?'",
 ],
 "recommendations": [
  "BUILD ON WHAT HAPPENS: suggest small additions to existing routines (reading during bedtime, talking about the day at dinner) rather than new programmes.",
  "HOME LANGUAGE: encourage parents to read and talk in their strongest language; it supports, not competes with, English.",
  "SCHOOL-LED ACCESS: homework club, library access, lending of books or devices; home–school communication that works for the family (texts, not long letters).",
  "SIGNPOST: Home School Community Liaison (HSCL) coordinator in DEIS schools; local library programmes; parent programmes where available (check locally).",
  "CONTINUUM LEVEL: Classroom Support and School Support — home learning suggestions are part of the Student Support Plan where agreed with the family.",
  "DO NOT make recommendations the family cannot carry out; DO NOT describe home conditions in a report without the parent's knowledge.",
 ],
 "explain_parent": [
  "'You don't need special materials. Ten minutes of reading together, or talking about what he saw today, helps his language and reading more than extra worksheets.'",
  "'Talk and read with her in your own language — it helps her English too.'",
  "SIGNPOST: HSCL coordinator; the local library; parent programmes (check locally).",
 ],
 "explain_teacher": [
  "'Homework is hard at home because of the evening routine — could he do some in the homework club instead?'",
  "'His mum reads with him in Polish every night. That's a real strength — could he bring a Polish book in for shared reading time?'",
 ],
 "explain_child": [
  "YOUNGER: 'What do you like doing at home? Who do you play with? Do you have a favourite book?'",
  "OLDER: 'Where do you study at home? What gets in the way?'",
  "ASK: 'Who at home knows the most about what you're learning?'",
 ],
 "red_flags": [
  "RED FLAG — signs of neglect (hunger, poor hygiene, untreated medical needs, no adult supervision): follow child protection procedures; report to Tusla as soon as practicable.",
  "WATCH — a young person with significant caring responsibilities at home: consider young carer supports.",
  "BOUNDARY — you describe; parenting capacity assessment belongs to Tusla or other services, not the EP.",
 ],
 "questions": [
  "Q: 'Am I doing enough?' A: 'You're already doing the most important things — talking with her and showing interest. Let's find one small addition that fits your routine.'",
  "Q: 'Should we speak only English at home?' A: 'No. Using your strongest language helps her language and learning. English will come through school.'",
  "Q: 'We don't have a quiet room.' A: 'That's common. The school may have a homework club, or a regular time and place — even the kitchen table after dinner — can work.'",
 ],
 "supervision": [
  "Discuss how you describe home factors in reports without judgement or deficit language.",
  "Bring a case where home learning suggestions didn't fit the family's evenings, work or language — what would you change, and who did you ask?",
 ],
 "citations": [
  "Sylva, K., Melhuish, E., Sammons, P., Siraj-Blatchford, I., & Taggart, B. (2004). The Effective Provision of Pre-School Education (EPPE) project: Final report. DfES / Institute of Education.",
  "Melhuish, E. C., Phan, M. B., Sylva, K., Sammons, P., Siraj-Blatchford, I., & Taggart, B. (2008). Effects of the home learning environment and preschool center experience upon literacy and numeracy development in early primary school. Journal of Social Issues, 64(1), 95–114.",
  "Desforges, C., & Abouchaar, A. (2003). The impact of parental involvement, parental support and family education on pupil achievement and adjustment: A literature review (Research Report RR433). Department for Education and Skills.",
 ],
})

# ---------------------------------------------------------------- 11
PRES.append({
 "name": "Community context",
 "neps": NEPS_56,
 "related_to": ["Social exclusion, discrimination, acculturation difficulty — DSM-5-TR Z-codes", "Housing and economic problems — DSM-5-TR Z-codes", "Interrupted or missed schooling", "Care-experienced children (foster, kinship, residential, aftercare)"],
 "what_it_is": [
  "Part D wording: 'Community context — Context, not a diagnosis'. The neighbourhood, community and wider systems around the child and school — economic disadvantage, rural isolation, housing, transport, cultural and ethnic community, local services and their waiting lists.",
  "Bronfenbrenner's (1979) ecological model places the child within nested systems (microsystem, mesosystem, exosystem, macrosystem): community context sits in the outer systems but shapes what happens at home and in school.",
  "In Ireland, DEIS (Delivering Equality of Opportunity in Schools) targets additional supports — including Home School Community Liaison (HSCL) and the School Completion Programme — to schools serving communities at risk of educational disadvantage (DES, 2017 — check current DEIS plan).",
  "Community context also includes strengths: extended family, sports clubs, Family Resource Centres, youth services, church or cultural groups, and Traveller and Roma organisations.",
 ],
 "what_it_is_not": [
  "NOT a reason to lower expectations for a child. Community disadvantage is a context for support, not a prediction of outcome.",
  "NOT a stereotype. Describe the specific barriers and resources for THIS family; avoid generalising about any community.",
  "NOT within the EP's power to change directly — but the EP can link families and schools with community supports and name systemic barriers.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: access to preschool, public health nurse, community childcare, early intervention; transport in rural areas.",
  "SCHOOL AGE 6–12: after-school clubs, homework clubs, sports, local services; waiting lists for CDNT, Primary Care and CAMHS vary by area.",
  "ADOLESCENT 13–16: youth services, peer groups, risk (antisocial behaviour, substance use), community belonging; Traveller young people's experience of school.",
  "YOUNG ADULT 17–26: access to further education, training, employment and transport; community supports for young people leaving care (aftercare).",
  "SPECIAL SETTING: travel distances to special schools; isolation from local peers; community inclusion in clubs and activities.",
 ],
 "assess": [
  "ASK what supports the family already uses and which are available locally — sports, youth services, community groups, Family Resource Centres.",
  "MAP SERVICES: who is involved, what waiting lists apply, and what barriers (transport, cost, language) affect access.",
  "LISTEN FOR DISCRIMINATION OR EXCLUSION: experiences of racism, anti-Traveller discrimination, or community tension that affect the child.",
  "CHECK WITH THE SCHOOL: DEIS status, HSCL and School Completion Programme availability.",
 ],
 "recommendations": [
  "LINK TO COMMUNITY SUPPORTS: HSCL coordinator, School Completion Programme, Family Resource Centres, youth services — check local availability.",
  "MEITHEAL: where a family would benefit from coordinated support across services, the school can suggest Tusla's Meitheal model with the family's consent — check local practice.",
  "INCLUSION IN THE COMMUNITY: identify one community activity that could build belonging (club, youth group, library) and practical steps to access it.",
  "SYSTEMIC ADVOCACY: where many referrals from one school reflect the same community barrier (e.g., no local service), raise this with your supervisor and service management.",
  "CONTINUUM LEVEL: School Support Plus where several agencies are involved; otherwise community links sit alongside School Support.",
  "DO NOT describe a community in deficit terms in a report; DO NOT recommend services without checking they exist locally.",
 ],
 "explain_parent": [
  "'There may be local supports we haven't talked about — the school's Home School Community Liaison coordinator knows what's available here.'",
  "'Would a local club or group be something he'd enjoy? Belonging somewhere outside school helps too.'",
  "SIGNPOST: HSCL; Family Resource Centre; local youth service; Meitheal via Tusla (check locally).",
 ],
 "explain_teacher": [
  "'The CAMHS waiting list here is long, so let's plan what the school can do in the meantime.'",
  "'He's very involved in the local GAA club — that's a place he's successful and trusted. Can we build on that in school, maybe in PE or a leadership role?'",
 ],
 "explain_child": [
  "YOUNGER: 'What do you like doing near your house? Who are your friends there?'",
  "OLDER: 'What's it like where you live? Is there anything you'd like to be involved in that you can't get to?'",
  "ASK: 'Where do you feel you belong?'",
 ],
 "red_flags": [
  "RED FLAG — community exploitation, gang involvement, or risk from others in the community: safeguarding and child protection routes; Tusla and An Garda Síochána as appropriate.",
  "WATCH — experiences of racism or discrimination affecting attendance or wellbeing: school anti-bullying and inclusion procedures apply.",
  "BOUNDARY — you link and recommend; you do not coordinate other services' provision or promise access.",
 ],
 "questions": [
  "Q: 'There's nothing for kids around here.' A: 'That's a real barrier. Let's ask the HSCL coordinator what exists nearby, and see if school activities can fill some of the gap.'",
  "Q: 'Why are you asking about our community?' A: 'Because what's around a child — people, clubs, services — can help or make things harder. I'm looking for strengths as well as barriers.'",
  "Q: 'What is Meitheal?' A: 'It's a Tusla model where the family and services come together to plan support. It's voluntary and led by the family.'",
 ],
 "supervision": [
  "Bring a case where community factors shaped your formulation and discuss how you wrote about them.",
  "Ask about local services, waiting lists and community resources — what does your supervisor recommend to families in this area?",
 ],
 "citations": [
  "Bronfenbrenner, U. (1979). The ecology of human development: Experiments by nature and design. Harvard University Press.",
  "Department of Education and Skills. (2017). DEIS plan 2017: Delivering equality of opportunity in schools. DES. — check for the current plan.",
  "Tusla. (n.d.). Meitheal: A national practice model for all agencies working with children, young people and their families. Tusla. — check the current version.",
 ],
})

# ---------------------------------------------------------------- 12
PRES.append({
 "name": "Continuum of Support level and whether it was actually implemented",
 "neps": NEPS_56,
 "related_to": ["Instruction history", "Literacy difficulty not meeting SLD criteria", "Behaviour that challenges", "Numeracy difficulty not meeting SLD criteria"],
 "what_it_is": [
  "Part D wording: 'Continuum of Support level and whether it was actually implemented — Added'. A SYSTEMIC question about the case: at what level of the NEPS Continuum of Support (Classroom Support, School Support, School Support Plus) is the child — and was the support at that level actually delivered, as planned, long enough to judge its effect?",
  "The Continuum is a problem-solving model: identify the concern, gather information, plan, intervene, review; move up or down levels according to response (NEPS, 2007; NEPS, 2010; DES, 2017). The Student Support File is the record of that cycle.",
  "Durlak and DuPre (2008), reviewing over 500 studies, concluded that the level of implementation affects outcomes; they report that in some of the meta-analyses reviewed, mean effect sizes were two to three times higher when programmes were carefully implemented than when they had serious implementation problems (prevention and promotion programmes, not school SEN support specifically — check the paper before quoting the figure). 'We tried that' may mean it was never delivered as intended.",
  "For the EP, the answer changes interpretation: poor progress despite well-implemented support is more significant than poor progress without it (see 'Instruction history').",
 ],
 "what_it_is_not": [
  "NOT a gatekeeping test to refuse involvement. It is information for the formulation and for planning — the EP can help a school implement the Continuum, not only judge it.",
  "NOT satisfied by a document existing. A Student Support Plan with vague targets, no review date and no progress data is a record of intention, not implementation.",
  "NOT a criticism of individual teachers. Implementation depends on time, staffing, leadership and training — systemic factors the EP can help to address.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: the Continuum applies from school entry; in preschool, AIM levels provide a parallel structure. Check what AIM support was in place before school.",
  "SCHOOL AGE 6–12: the core application. Classroom Support by the class teacher; School Support with SET involvement; School Support Plus with NEPS or external services.",
  "ADOLESCENT 13–16: post-primary continuum (NEPS, 2010); many teachers means implementation across subjects is harder to check. Year head, SEN coordinator and guidance counsellor are key sources.",
  "YOUNG ADULT 17–26: the Continuum does not apply after school; retrospective questions about support history may still matter.",
  "SPECIAL SETTING: individualised planning is the norm; the question is whether plans are reviewed and targets moved.",
 ],
 "assess": [
  "READ THE STUDENT SUPPORT FILE: dates, level, concerns, targets, strategies, reviews. Look for gaps between plan and review, and whether targets are measurable.",
  "ASK HOW IT WAS DELIVERED: 'What did the intervention actually look like, how often, for how long, who delivered it?' Compare with what was planned.",
  "LOOK FOR DATA: pre- and post-measures, progress monitoring, reviews with parents and pupil. Absence of data is itself a finding.",
  "PUPIL AND PARENT VIEW: did they know about the plan? Did they take part in review?",
 ],
 "recommendations": [
  "STATE THE LEVEL IN THE REPORT and whether support at that level has been implemented as planned; say how this affects interpretation of assessment results.",
  "WHERE IMPLEMENTATION WAS INCOMPLETE: recommend a specific, time-limited plan at the appropriate level (named strategy, frequency, duration, person, measure, review date) before drawing conclusions (Durlak & DuPre, 2008).",
  "SUPPORT THE CYCLE: offer consultation to set measurable targets and a review structure; model a review meeting where helpful.",
  "SYSTEMIC FEEDBACK: where a pattern of incomplete implementation appears across cases in one school, raise it with the principal as a whole-school issue (see 'Whole-school policy and practice').",
  "CONTINUUM LEVEL: recommend the level the evidence supports — move up only when support at the current level has been delivered and reviewed.",
  "DO NOT recommend a higher level or further assessment to compensate for support that has not been delivered.",
 ],
 "explain_parent": [
  "'The school has a plan for her. What I'm checking is what's actually been done and how she responded — that tells us what to do next.'",
  "'If the help hasn't been in place long enough to know if it works, the fairest thing is to give it a proper try first.'",
 ],
 "explain_teacher": [
  "'Can you show me the Student Support Plan and the reviews? I'm not checking up on you — I need to know what's been tried to interpret my assessment.'",
  "'The plan says daily reading intervention, but with the staffing changes it happened twice a week. That matters for how we read his progress.'",
 ],
 "explain_child": [
  "YOUNGER: 'Who helps you with your reading? How often do you go?'",
  "OLDER: 'Do you know about your support plan? Did anyone ask you what should be in it?'",
  "ASK: 'What help has actually been useful?'",
 ],
 "red_flags": [
  "WATCH — a child at School Support Plus with no documented School Support phase: check what was tried and why the level changed.",
  "WATCH — the same plan unchanged for more than a year: review is not happening.",
  "BOUNDARY — the EP advises on the Continuum; the school's principal and SEN team are responsible for implementation.",
 ],
 "questions": [
  "Q: 'We've tried everything — why do you want us to try more?' A: 'Can we look at what was tried and for how long? Sometimes a strategy that didn't work had too little time or wasn't delivered the way it was planned.'",
  "Q: 'Why can't you just assess him now?' A: 'I will. But without knowing what support he's had, the results can be misleading. Both pieces together give the right answer.'",
  "Q: 'What counts as a proper try?' A: 'A named strategy, delivered regularly for a set period — usually six to ten weeks — with a measure before and after.'",
 ],
 "supervision": [
  "Bring a Student Support File you have reviewed and discuss how you would give feedback on implementation without undermining the school.",
  "Discuss the local service's expectations about Continuum evidence before individual casework.",
 ],
 "citations": [
  "National Educational Psychological Service. (2007). Special educational needs: A continuum of support — Guidelines for teachers. Department of Education and Science.",
  "National Educational Psychological Service. (2010). A continuum of support for post-primary schools: Guidelines for teachers. Department of Education and Skills. (Check title and date.)",
  "Department of Education and Skills. (2017). Guidelines for primary schools: Supporting pupils with special educational needs in mainstream schools. DES.",
  "Durlak, J. A., & DuPre, E. P. (2008). Implementation matters: A review of research on the influence of implementation on program outcomes and the factors affecting implementation. American Journal of Community Psychology, 41(3–4), 327–350.",
 ],
})

# ---------------------------------------------------------------- 13
PRES.append({
 "name": "Whole-school policy and practice",
 "neps": NEPS_56,
 "related_to": ["Behaviour that challenges", "Emotionally Based School Avoidance (EBSA)", "Continuum of Support level and whether it was actually implemented", "Staff training need identified through casework"],
 "what_it_is": [
  "Part D wording: 'Whole-school policy and practice — Added — your systemic change development area'. The school's policies, procedures and culture that shape how children are supported: SEN policy, code of behaviour, anti-bullying procedures, wellbeing, attendance, child protection, and how these are actually practised.",
  "Irish frames: Wellbeing Policy Statement and Framework for Practice (DES, 2019 — check current version); code of behaviour guidelines (NEWB, 2008); Bí Cineálta anti-bullying procedures (Department of Education, 2024); Child Protection Procedures for Primary and Post-Primary Schools (check current version); School Self-Evaluation.",
  "The EP's role: consultation and systemic work — noticing patterns across cases, helping schools review policies, supporting implementation (Wagner, 2000).",
  "Implementation research (Fixsen et al., 2005) suggests that policies change practice only when supported by training, coaching, leadership and data — a written policy on its own rarely changes classrooms.",
 ],
 "what_it_is_not": [
  "NOT the EP writing the school's policies. Policies belong to the Board of Management; the EP advises on psychological aspects and evidence.",
  "NOT a critique of a school based on one case. Systemic observations come from patterns across cases or from the school's own request.",
  "NOT separate from casework. Individual referrals often reveal systemic issues (e.g., three referrals about lunchtime point to yard supervision).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool policies under Tusla regulations and AIM; inclusion policies in ECCE settings.",
  "SCHOOL AGE 6–12: SEN policy, code of behaviour, anti-bullying, wellbeing; how whole-class strategies are shared across teachers.",
  "ADOLESCENT 13–16: consistency across many teachers; pastoral structures (year heads, tutors, guidance); policies on phones, suspension and reduced timetables.",
  "YOUNG ADULT 17–26: college and workplace policies on disability and accommodation; not usually EP practice.",
  "SPECIAL SETTING: policies on behaviours of concern, restrictive practice, intimate care, communication — check current Department guidance.",
 ],
 "assess": [
  "READ KEY POLICIES with the school's permission: SEN, behaviour, anti-bullying, wellbeing. Look at what is written and how it is used.",
  "NOTICE PATTERNS ACROSS CASES: similar referrals, similar gaps in support, repeated concerns about a particular time or place.",
  "ASK STAFF how the policy works in practice — what helps, what gets in the way.",
  "PUPIL AND PARENT VOICE: student council, parent association, surveys — ask what the school feels like to them.",
 ],
 "recommendations": [
  "START WITH THE SCHOOL'S PRIORITIES: agree a systemic focus with the principal in the NEPS planning meeting; frame recommendations within the school's own development planning.",
  "EVIDENCE-INFORMED POLICY: align with the Wellbeing Framework, Bí Cineálta and the Continuum of Support; suggest review points based on data (incidents, attendance, referrals).",
  "IMPLEMENTATION SUPPORT: pair any policy change with training, coaching and follow-up (Fixsen et al., 2005).",
  "CONSULTATION MODEL: offer consultation to staff groups rather than individual assessment where the pattern is systemic (Wagner, 2000).",
  "CONTINUUM LEVEL: whole-school (universal) level — 'Support for All' in the Continuum and Wellbeing Framework.",
  "DO NOT offer systemic recommendations in an individual child's report without agreement from the school; DO NOT promise outcomes of policy change.",
 ],
 "explain_parent": [
  "'Some of what's happening for him is about how the school handles break times for everyone. The school is looking at that, and it should help him and others.'",
  "'You can ask to see the school's anti-bullying and behaviour policies — schools are required to have them.'",
 ],
 "explain_teacher": [
  "'Three referrals this term mention transitions between lessons. Would it help to look at that as a whole-school question?'",
  "'The policy is good on paper. What would make it easier to use on a busy Tuesday?'",
 ],
 "explain_child": [
  "YOUNGER: 'What are the school rules? Which ones help? Which ones are hard?'",
  "OLDER: 'If you were principal for a day, what would you change about how the school works?'",
  "ASK: 'Do you know who to go to if something is wrong in school?'",
 ],
 "red_flags": [
  "RED FLAG — a policy or practice that places children at risk (e.g., restrictive practice outside guidance, failure to follow child protection procedures): raise with the principal and your supervisor; follow child protection routes where needed.",
  "WATCH — use of suspension, reduced days or exclusion with no planned return: check against current guidance and the child's right to education.",
  "BOUNDARY — policy decisions belong to the Board of Management; the EP advises.",
 ],
 "questions": [
  "Q: 'Can you write our wellbeing policy?' A: 'I can help you think through the evidence and review a draft, but the policy is the school's own.'",
  "Q: 'Why are you talking about school policy when we referred one child?' A: 'Because what you've described is happening for several children. A whole-school change may help all of them faster.'",
  "Q: 'We already have a policy — isn't that enough?' A: 'The research says policy changes practice when staff get training and follow-up, and when data shows whether it's working.'",
 ],
 "supervision": [
  "Bring a pattern you have noticed across cases in one school and plan how to raise it at the planning meeting.",
  "Discuss the boundary between advising on policy and taking responsibility for it.",
  "Reflect on your systemic change development area — what small piece of systemic work could you lead this placement?",
 ],
 "citations": [
  "Department of Education and Skills. (2019). Wellbeing policy statement and framework for practice 2018–2023 (revised). Government of Ireland. — check for the current version.",
  "Department of Education. (2024). Bí Cineálta: Procedures to prevent and address bullying behaviour for primary and post-primary schools. Department of Education. (Check for updates.)",
  "National Educational Welfare Board. (2008). Developing a code of behaviour: Guidelines for schools. NEWB.",
  "Wagner, P. (2000). Consultation: Developing a comprehensive approach to service delivery. Educational Psychology in Practice, 16(1), 9–18.",
  "Fixsen, D. L., Naoom, S. F., Blase, K. A., Friedman, R. M., & Wallace, F. (2005). Implementation research: A synthesis of the literature. University of South Florida.",
 ],
})

# ---------------------------------------------------------------- 14
PRES.append({
 "name": "Staff training need identified through casework",
 "neps": NEPS_56,
 "related_to": ["Autism", "ADHD", "Anxiety disorders", "Behaviour that challenges", "Whole-school policy and practice"],
 "what_it_is": [
  "Part D wording: 'Staff training need identified through casework — Added'. A systemic finding: individual cases reveal that staff lack knowledge, skills or confidence in a specific area (e.g., autism, anxiety, behaviour, literacy intervention), and that addressing this would help many children.",
  "Joyce and Showers (2002) found that training with theory and demonstration alone produced little transfer to classroom practice; adding practice, feedback and in-class coaching greatly increased transfer.",
  "Guskey (2002) argued that teacher beliefs often change AFTER they see improved outcomes from trying a new practice — so training should be linked to trial and feedback, not just presentation.",
  "In Ireland, professional learning is provided by Oide (established 2023), the NCSE Support Service, NEPS (e.g., Incredible Years Teacher Classroom Management, FRIENDS programmes), Middletown Centre for Autism and others — check current offerings.",
 ],
 "what_it_is_not": [
  "NOT a criticism of staff. A training need is a system gap, often caused by changing pupil needs, staff turnover, or lack of access to training.",
  "NOT solved by a one-off talk. A single staff presentation without follow-up rarely changes practice (Joyce & Showers, 2002).",
  "NOT the EP's sole responsibility to deliver. The EP identifies, advises on and may contribute to training; other services may be better placed to deliver it.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: preschool staff training through AIM (e.g., LINC) and Better Start; EP role may be indirect.",
  "SCHOOL AGE 6–12: common needs — autism, anxiety, behaviour management, literacy intervention, trauma-informed practice.",
  "ADOLESCENT 13–16: subject teachers' understanding of SEN; mental health awareness; consistent approaches across many staff.",
  "YOUNG ADULT 17–26: not usually EP practice; college staff awareness training through disability services.",
  "SPECIAL SETTING: staff turnover and SNA training needs; specialised areas (AAC, behaviours of concern, intimate care) — check current guidance.",
 ],
 "assess": [
  "NOTICE THE PATTERN: similar questions from several staff; repeated recommendations not implemented because of skill gaps; staff saying 'we don't know how'.",
  "ASK STAFF what they feel confident about and what they want to learn — a short survey or conversation in consultation.",
  "LOOK AT PREVIOUS TRAINING: what was attended, when, and whether it was followed up.",
  "LINK TO OUTCOMES: which children would benefit, and how would you know?",
 ],
 "recommendations": [
  "NAME THE NEED SPECIFICALLY: 'Staff would benefit from training in structured teaching approaches for autistic pupils' — not 'staff need autism training'.",
  "MATCH TO PROVIDER: NEPS, Oide, NCSE Support Service, Middletown Centre for Autism, local services — check availability and waiting lists.",
  "BUILD IN FOLLOW-UP: training plus coaching, peer observation or consultation (Joyce & Showers, 2002); agree a review point.",
  "PRIORITISE with the principal in the NEPS planning meeting, alongside casework.",
  "CONTINUUM LEVEL: whole-school (universal) level — improves Classroom Support for all pupils.",
  "DO NOT offer training beyond your competence; DO NOT name staff in written feedback about training needs.",
 ],
 "explain_parent": [
  "'The school is arranging training for staff in this area, which should help your child and other children too.'",
  "'You can ask the school what training staff have had, and how they're following it up — it's a fair question, and schools usually welcome it.'",
 ],
 "explain_teacher": [
  "'Several of you have asked similar questions about anxious pupils. Would a short training session followed by a consultation group be useful?'",
  "'Training works best with follow-up — let's plan a session and then check in after a few weeks to see how it's going in class.'",
 ],
 "explain_child": [
  "YOUNGER: 'Teachers are learning new ways to help children. What do you think they should learn?'",
  "OLDER: 'If teachers could understand one thing better about students like you, what would it be?'",
  "ASK: 'What does a teacher do that really helps?'",
 ],
 "red_flags": [
  "RED FLAG — staff using practices that cause harm (e.g., restrictive practice outside guidance) because of a training gap: raise with the principal and your supervisor promptly.",
  "WATCH — the same recommendation failing in several cases: check whether a training gap underlies it.",
  "BOUNDARY — training delivery is by agreement with the school and your service; do not deliver training outside your competence or service remit.",
 ],
 "questions": [
  "Q: 'Can you come in and do a talk on ADHD?' A: 'I can, and it will work better if we plan follow-up — a check-in or consultation group a few weeks later. Research shows that's what changes practice.'",
  "Q: 'We've had training and it didn't change anything.' A: 'That's common — training alone rarely changes practice without follow-up (Joyce & Showers, 2002). Let's plan the follow-up this time.'",
  "Q: 'Who should do the training?' A: 'It depends on the topic. NEPS, Oide, the NCSE Support Service and Middletown all offer different things — I'll help you find the best fit.'",
 ],
 "supervision": [
  "Bring a pattern across cases that suggests a training need, and plan how to raise it with the school.",
  "Discuss what training you could deliver as a trainee, with support, and what should be referred to others.",
 ],
 "citations": [
  "Joyce, B., & Showers, B. (2002). Student achievement through staff development (3rd ed.). Association for Supervision and Curriculum Development.",
  "Guskey, T. R. (2002). Professional development and teacher change. Teachers and Teaching, 8(3), 381–391.",
  "Teaching Council. (2016). Cosán: Framework for teachers' learning. Teaching Council.",
 ],
})
