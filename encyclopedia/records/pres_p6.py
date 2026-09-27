# PRES batch 6 — descriptive (non-diagnostic) presentations.
# Context: Reference Part D, column N (rows 507–650), present at every UCD Table 3 band.
#   Items 1–5   : 4. SOCIAL (4.1 Friendships and social skills)
#                 Part D dx: Autism (levels 1–3, specifiers) · Social (Pragmatic) Communication Disorder
#                 Routes: CDNT · NEPS for school supports · NEPS with SLT · whole-school policy support
#   Items 6–13  : 4. SOCIAL (4.2 Relationships with adults)
#                 Part D dx: Relational problems (Z-codes / ICD-11 Ch.24) · Gender Dysphoria (children; adolescents)
#                 Routes: Primary Care · CDNT · CAMHS · Specialist services · NEPS · school supports
#                 Part D School Age: "Observation across different adults — the difference between teachers is data"
#   Items 14–16 : 5. OTHER (5.1 Vision)   — dx: Visual impairment. Routes: Ophthalmology · Optometry · Visiting Teacher · CDNT · GP
#   Items 17–19 : 5. OTHER (5.2 Hearing)  — dx: Hearing impairment · Recurrent otitis media with effusion (glue ear)
#                 Routes: Audiology · Visiting Teacher · CDNT · GP
#   Item 20     : 5. OTHER (5.3 Medical condition or other diagnosis) — "your role is educational impact, not diagnosis"

NEPS_41 = "4. SOCIAL (4.1 Friendships and social skills)"
NEPS_42 = "4. SOCIAL (4.2 Relationships with adults)"
NEPS_51 = "5. OTHER (5.1 Vision)"
NEPS_52 = "5. OTHER (5.2 Hearing)"
NEPS_53 = "5. OTHER (5.3 Medical condition or other diagnosis)"

PRES = []

# ---------------------------------------------------------------- 1
PRES.append({
 "name": "Co-operation with peers in group work",
 "neps": NEPS_41,
 "related_to": ["Autism", "Social (Pragmatic) Communication Disorder", "ADHD", "DLD", "Social Anxiety Disorder (social phobia)"],
 "what_it_is": [
  "A description of how a pupil manages TASK-FOCUSED collaboration with classmates — sharing materials, dividing a job, accepting a role, contributing ideas, accepting someone else's idea, and finishing together. Part D lists it under 4.1 with the note 'Form 2 survey wording': it is the phrase teachers tick, so expect it on referral forms.",
  "Group work makes several demands at once: following fast, overlapping talk; holding a shared goal in mind; negotiating turns and roles; tolerating a plan that is not yours; and managing noise. The presentation is the same whichever demand breaks — the assessment is about which one.",
  "Johnson and Johnson (2009) show that cooperative learning works when there is POSITIVE INTERDEPENDENCE (the group succeeds only if each member contributes) and INDIVIDUAL ACCOUNTABILITY. Many classroom 'groups' have neither, so the pupil is being asked to co-operate in a task that is not designed for co-operation.",
  "Blatchford et al. (2003) found that pupils are frequently seated in groups but rarely taught HOW to work as a group; the SPRinG programme (Baines et al., 2016) teaches group-work skills explicitly — trust, communication, planning — before expecting them.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis and NOT evidence of autism by itself. It is common in autism and Social (Pragmatic) Communication Disorder, and it is also common in ADHD (turn-taking, impatience), DLD (cannot follow the talk), anxiety (cannot speak up) and in very able pupils who would rather do it alone.",
  "NOT unwillingness. A pupil who takes over, withdraws or disrupts in groups is usually showing you the skill that is missing, not a refusal. Ask them afterwards what the group was supposed to be doing — the answer is often revealing.",
  "NOT solved by putting the child in more groups. Unstructured group placement repeats the failure; taught, structured roles change it (Baines et al., 2016).",
 ],
 "by_age": [
  "EARLY YEARS 0–5: parallel and associative play are developmentally expected (Parten, 1932); true co-operative task work is emerging. Describe what the child does alongside others — joining, sharing materials, accepting an adult-set role — against same-age peers in the same room.",
  "SCHOOL AGE 6–12: the peak referral window. Group projects, Aistear-style stations and paired reading expose it. Look for taking over, opting out, arguing about roles, or doing the whole task alone and then being rejected by the group.",
  "ADOLESCENT 13–16: CBAs (Classroom-Based Assessments) at Junior Cycle and practical subjects rely on group work; peers now choose partners, so exclusion becomes visible. Social cost rises sharply.",
  "YOUNG ADULT 17–26: group assignments in further and higher education and team working in employment. Self-report of what the group demands and what the student avoids is the main evidence; disability services can arrange alternatives for assessed group work.",
  "SPECIAL SETTING: co-operation may be with one peer and heavily scaffolded — shared turn on an iPad, passing an object. Describe the level of adult support needed, not only whether co-operation happened.",
 ],
 "assess": [
  "Structured observation of the SAME pupil in (a) whole-class teaching, (b) a structured group task with assigned roles and (c) an unstructured group task. The difference between (b) and (c) is the key finding for recommendations.",
  "Record specifics: who speaks, who holds the materials, what the pupil does when their idea is not taken, how long they stay on the shared task. A simple interval record with a comparison peer keeps it descriptive.",
  "SRS-2 (parent and teacher) or SCQ where a social communication question has been raised — describe what the rating says about everyday social reciprocity; it does not diagnose. Screen language comprehension (CELF-5 UK subtests or SLT report) if the pupil may not be following the talk.",
  "Pupil interview: 'What is hard about working in a group? Who is easy to work with? What job do you like having?' Children often identify the demand precisely.",
 ],
 "recommendations": [
  "TEACH GROUP-WORK SKILLS before relying on them: explicit roles (reader, recorder, materials manager, timekeeper) with role cards, rotated so every pupil practises each (Baines et al., 2016). Start in pairs, move to threes.",
  "STRUCTURE THE TASK for interdependence: each member holds part of the information or one piece of the output (jigsaw-style), so contribution is required and visible (Johnson & Johnson, 2009).",
  "CHOOSE THE GROUP deliberately: place the pupil with one or two peers who are patient and skilled, not with the most dominant or the most vulnerable. Keep the group stable for a half-term so relationships can form.",
  "PRE-TEACH: tell the pupil in advance what the task is, what their role is and what 'done' looks like. For pupils who find it overwhelming, allow a defined quiet space within the group task.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support where a targeted social skills group or individual plan in the Student Support File is needed. Review at 6–8 weeks using the same observation.",
  "DO NOT record 'refuses to co-operate' as a behaviour finding without the observation that explains it. REFER via the family to CDNT (or Primary Care / CAMHS by local pathway) only if a wider social communication pattern is present across settings.",
 ],
 "explain_parent": [
  "'In class she does well on her own. Group tasks are harder because there's a lot going on at once — lots of talk, deciding who does what, and going along with someone else's plan.'",
  "'This is a skill that can be taught, and the school is going to teach it directly — giving her a clear job in the group, with a card that says what the job is.'",
  "'At home: board games that need a team, cooking together where she has one job. Afterwards, talk about what went well, not what went wrong.'",
 ],
 "explain_teacher": [
  "'Sitting in a group isn't the same as working as a group. Give him a named role with a card, and a task where the group needs his part to finish.'",
  "'Watch what happens when his idea isn't chosen — that's usually the moment it falls apart. Rehearse it beforehand: \"If the group picks another idea, you can say...\"'",
  "'Try a pair first. If he manages in a pair, build up to three before a whole group.'",
 ],
 "explain_child": [
  "YOUNGER: 'In a group, everyone has a job, like a team in a match. Today your job is the materials person — you look after the scissors and glue for everyone.'",
  "OLDER: 'Group work is hard for lots of people. It's usually one part that's tricky — speaking up, or letting someone else's idea win, or it being noisy. Which part is it for you?'",
  "ASK: 'Who in the class is easy to work with, and what do they do that makes it easy?' — gives you both the peer to pair with and the skill to teach.",
 ],
 "red_flags": [
  "WATCH — consistent exclusion by peers from groups (no one chooses them, groups rearrange to avoid them): check for bullying under the school's anti-bullying procedures, and for loneliness behind a calm surface.",
  "WATCH — distress, shutdowns or aggression specifically in group tasks: may indicate sensory overload or anxiety rather than a skill gap; adjust the environment before adding demands.",
  "BOUNDARY — a group-work difficulty is not an autism assessment. Diagnosis sits with CDNT or other diagnostic services; describe and refer via the family.",
 ],
 "questions": [
  "Q: 'He's grand on his own — do we even need to worry?' A: 'For attainment, maybe not. But group work is how friendships form in class and how Junior Cycle CBAs are done, so it's worth teaching now.'",
  "Q: 'Is this autism?' A: 'Difficulty in group work happens for many reasons — autism is one, but so are language, attention and anxiety. On its own it isn't a diagnosis. If there's a wider pattern at home and school, I'll talk with you about the referral route.'",
  "Q: 'Should she be let work on her own?' A: 'Sometimes, yes, when the goal is the content. When the goal is learning to work with others, we scaffold the group rather than remove her from it.'",
  "Q: 'Which is better — mixed-ability or similar-ability groups?' A: 'For her, the partners matter more than the ability mix. Choose patient, skilled peers and keep the group stable.'",
 ],
 "supervision": [
  "Bring an observation where you saw the pupil fail in a group — did you record the task design as well as the child? Was interdependence built in?",
  "Discuss how to phrase group-work difficulties in a report so the recommendations target the classroom structure, not only the child.",
 ],
 "citations": [
  "Baines, E., Blatchford, P., & Kutnick, P. (2016). Promoting effective group work in the primary classroom: A handbook for teachers and practitioners (2nd ed.). Routledge.",
  "Blatchford, P., Kutnick, P., Baines, E., & Galton, M. (2003). Toward a social pedagogy of classroom group work. International Journal of Educational Research, 39(1–2), 153–172.",
  "Johnson, D. W., & Johnson, R. T. (2009). An educational psychology success story: Social interdependence theory and cooperative learning. Educational Researcher, 38(5), 365–379.",
  "Parten, M. B. (1932). Social participation among pre-school children. The Journal of Abnormal and Social Psychology, 27(3), 243–269.",
 ],
})

# ---------------------------------------------------------------- 2
PRES.append({
 "name": "Turn-taking and shared play",
 "neps": NEPS_41,
 "related_to": ["Autism", "Social (Pragmatic) Communication Disorder", "ADHD", "DLD", "Global Developmental Delay"],
 "what_it_is": [
  "A description of how a child manages WAITING for a turn, GIVING UP an object or role, and SHARING a play theme with another child — the building blocks of play-based friendship in the early years and infant classes.",
  "Turn-taking has a developmental sequence: adult-led turn exchanges in infancy (back-and-forth vocalisation, peek-a-boo), then turn-taking with objects, then sharing a play theme with a peer. Parten (1932) described the shift from solitary and parallel play toward associative and co-operative play across the preschool years.",
  "It draws on several capacities at once: joint attention (noticing what the other child is doing), inhibition (waiting), understanding rules, and language for negotiating ('my turn', 'can I have it after?'). Difficulty can come from any of these.",
  "Kasari et al. (2006) showed that joint attention and symbolic play can be taught to young autistic children and that gains generalise to interaction — play skills are teachable, not fixed.",
 ],
 "what_it_is_not": [
  "NOT selfishness or poor parenting. Waiting for a turn is a developmental skill with wide variation in the early years; many three-year-olds cannot yet do it without adult help.",
  "NOT evidence of autism by itself. Difficulty is also seen in ADHD (waiting), DLD (lacking the words to negotiate), developmental delay (play is at an earlier stage), and in children who have had little experience of play with peers.",
  "NOT the same as not wanting to play with others. Some children want to play but do not know how to enter or keep a game going — the difference changes the recommendation.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: the core band. Snatching, not waiting, playing alongside rather than with peers, repeating one play script. Describe against peers in the same room and the Aistear theme 'Well-being' and 'Identity and Belonging' expectations (NCCA, 2009) — do not score.",
  "SCHOOL AGE 6–12: board games in class, yard games with rules, sharing equipment in PE. Losing a game or waiting in a queue may trigger distress. Friendship groups begin to form around shared play.",
  "ADOLESCENT 13–16: turn-taking in conversation (interrupting, monologuing) replaces turn-taking with objects; team sport and online gaming are where it shows.",
  "YOUNG ADULT 17–26: conversational turn-taking in seminars, workplaces and relationships; self-report and feedback from others are the main evidence.",
  "SPECIAL SETTING: turn-taking may be taught as a discrete skill with visual supports ('my turn / your turn' card, a turn timer). Describe the prompt level the child needs — physical, gestural, verbal, independent.",
 ],
 "assess": [
  "Structured play observation (free play and a turn-taking game with one peer): latency to accept waiting, what the child does while waiting, how they enter play, whether they follow a peer's play idea. Record the adult prompt level needed.",
  "Developmental history from parents: play at home with siblings, cousins; early joint attention (pointing to share, showing toys). ASQ-3 or Schedule of Growing Skills II can frame the wider developmental picture in early years.",
  "SRS-2 or SCQ (where age-appropriate) when a social communication question is raised — describe, do not diagnose; Vineland-3 socialisation domain for play and leisure in context.",
  "Check language: does the child have words for 'my turn', 'can I play', 'when you're finished'? SLT input where expressive language is limited.",
 ],
 "recommendations": [
  "TEACH TURN-TAKING WITH AN ADULT FIRST, then with one peer, then in a small group. Use visual supports: a 'my turn' card or object that passes between players; a sand timer for waiting.",
  "USE THE CHILD'S INTERESTS: set up turn-taking games around a preferred theme or toy. LEGO-based therapy (LeGoff, 2004) builds turn-taking into roles (engineer, supplier, builder) and suits many children in school age.",
  "COACH ENTRY TO PLAY: teach a script ('Can I play? I can be the ...') and have an adult stay close for the first minutes of yard time or free play, then fade.",
  "PRAISE THE WAITING specifically and immediately ('You waited for your turn — well done') rather than only correcting the grab.",
  "CONTINUUM LEVEL: Classroom Support in most cases; School Support for a targeted small-group play programme. Review in 6–8 weeks with the same observation.",
  "REFER via the family to CDNT (early years and school age) where turn-taking difficulty is part of a wider pattern — limited joint attention, restricted play, language delay. Do not wait for 'school readiness' to decide.",
 ],
 "explain_parent": [
  "'Waiting for a turn and sharing a game are skills children learn at different rates. Right now he's still learning them — which is why he grabs. It isn't naughtiness.'",
  "'We're going to teach it the way you'd teach any skill: first with an adult, then with one friend, with a card that shows whose turn it is.'",
  "'At home, simple turn games — rolling a ball back and forth, a matching game — and saying out loud \"my turn, your turn\" make a real difference.'",
 ],
 "explain_teacher": [
  "'Start with one child and an adult, not the whole group. Once she can wait with the adult, bring in one peer.'",
  "'A turn object or card makes waiting visible. It's much easier to wait when you can see the card coming back to you.'",
  "'Praise the wait, not just the finish. The thing we want more of is the waiting.'",
 ],
 "explain_child": [
  "YOUNGER: 'This is the turn card. When you have it, it's your turn. When you give it to your friend, it's their turn — and then it comes back to you.'",
  "OLDER: 'Waiting is hard for lots of people. What helps you wait — counting, holding something, knowing how long it'll be?'",
  "ASK: 'Who do you like playing with? What games do you like best?' — tells you the peer and the theme to build on.",
 ],
 "red_flags": [
  "WATCH — absent or very limited joint attention (not pointing to share, not following another's point), no pretend play by around the time peers are doing it, or regression of language or play skills: prompt the family to see the GP / PHN and consider a CDNT referral.",
  "WATCH — aggression toward peers when turns are required that is escalating or causing injury: plan supervision and safety in the setting now, while the formulation is developed.",
  "BOUNDARY — do not describe a child as 'autistic traits' in a report. Describe what you saw and refer via the family.",
 ],
 "questions": [
  "Q: 'Should we make him share?' A: 'Forcing a toy away teaches him that sharing is losing. A turn card and a short, predictable wait teaches him that the toy comes back.'",
  "Q: 'She's four — is this normal?' A: 'Some difficulty waiting is typical at four. What I look at is how she compares with others in her room and whether other things, like language and play, are developing too.'",
  "Q: 'Will he grow out of it?' A: 'Most children improve with age and practice. Teaching it directly now helps him make friends while friendships are forming.'",
 ],
 "supervision": [
  "Bring a play observation and discuss how you distinguished a skill gap from a motivation or sensory difference.",
  "Discuss how to report early-years play difficulties to parents without implying a diagnosis, and when to suggest a CDNT referral.",
 ],
 "citations": [
  "Kasari, C., Freeman, S., & Paparella, T. (2006). Joint attention and symbolic play in young children with autism: A randomized controlled intervention study. Journal of Child Psychology and Psychiatry, 47(6), 611–620.",
  "LeGoff, D. B. (2004). Use of LEGO© as a therapeutic medium for improving social competence. Journal of Autism and Developmental Disorders, 34(5), 557–571.",
  "National Council for Curriculum and Assessment. (2009). Aistear: The early childhood curriculum framework. NCCA.",
  "Parten, M. B. (1932). Social participation among pre-school children. The Journal of Abnormal and Social Psychology, 27(3), 243–269.",
 ],
})

# ---------------------------------------------------------------- 3
PRES.append({
 "name": "Reading social cues and repair after conflict",
 "neps": NEPS_41,
 "related_to": ["Autism", "Social (Pragmatic) Communication Disorder", "ADHD", "DLD", "Oppositional Defiant Disorder"],
 "what_it_is": [
  "Two linked skills: READING CUES (facial expression, tone, body language, what is implied rather than said) and REPAIR (noticing a relationship has been damaged and doing something to fix it — apologising, explaining, making it up).",
  "Crick and Dodge's (1994) social information-processing model breaks a social moment into steps: encoding cues, interpreting them, choosing a goal, generating responses, deciding and acting. A child can go wrong at any step — the assessment asks which.",
  "HOSTILE ATTRIBUTION: some children read ambiguous events as deliberate ('he bumped me on purpose'), and respond aggressively (Crick & Dodge, 1994). Others miss the cue altogether. Same conflict, different step, different intervention.",
  "Milton (2012) describes the 'double empathy problem': misunderstanding between autistic and non-autistic people runs both ways. Cue-reading is partly a mismatch between communication styles, not only a deficit in one child.",
 ],
 "what_it_is_not": [
  "NOT lack of caring. Many children who misread cues are distressed by the conflict and want to repair it; they do not know how, or they miss the moment.",
  "NOT only autism. It is common in ADHD (acting before the cue is processed), DLD (missing implied meaning), after trauma (reading threat into neutral faces), and in children with limited social experience.",
  "NOT fixed by forced apology. A scripted 'sorry' without understanding teaches the child that repair is a ritual; restorative conversations that help both children understand what happened are more likely to lead to real repair.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: emotion recognition is emerging; conflicts over toys are frequent and adults do most of the repair. Note whether the child notices another child's distress at all.",
  "SCHOOL AGE 6–12: yard conflicts, misunderstood jokes, 'he was looking at me'. Children now expect peers to repair themselves; the child who cannot is gradually excluded.",
  "ADOLESCENT 13–16: sarcasm, irony, group chats and online messages without tone. Misreading can lead to serious fallouts or exploitation; repair is expected to be subtle.",
  "YOUNG ADULT 17–26: workplace and relationship cues; self-report and specific incidents are the evidence. Many adults describe learning cues explicitly and with effort.",
  "SPECIAL SETTING: repair may be taught as a concrete routine (visual 'fix it' steps) and cue-reading as explicit emotion vocabulary with photos. Record what the child does independently versus with prompting.",
 ],
 "assess": [
  "Incident analysis with the child: go through two or three recent conflicts step by step (what happened first, what did you think they meant, what did you do, what happened next) — maps onto Crick and Dodge's steps and shows where it breaks.",
  "Comic Strip Conversations (Gray, 1994) as an interview tool: drawing the event with speech and thought bubbles makes other people's thoughts visible and shows how the child interprets them.",
  "Yard and classroom observation (Part D, 4.1): record conflicts, what preceded them, and whether any repair attempt was made. SRS-2 parent and teacher describe everyday social reciprocity across settings.",
  "Check language (inference, non-literal language) via SLT or CELF-5 UK subtests, and ask about trauma history — both change how cues are read.",
 ],
 "recommendations": [
  "TEACH CUE-READING EXPLICITLY using real class situations, photos and video clips rather than only abstract emotion cards; link each cue to what to do next.",
  "USE RESTORATIVE CONVERSATIONS after conflict — what happened, who was affected, what is needed to put it right — with an adult facilitating until the child can do it with support. Many Irish schools use restorative practice; check the school's approach.",
  "PRE-TEACH REPAIR SCRIPTS: a few phrases for fixing things ('I didn't mean it like that', 'Can we start again?'), rehearsed when calm, not in the moment.",
  "WORK ON THE OTHER SIDE TOO: help peers and staff understand the child's communication style (Milton, 2012) — for example, that a flat face is not rudeness.",
  "CONTINUUM LEVEL: Classroom Support for whole-class social-emotional learning (SPHE); School Support for a targeted group or individual work; School Support Plus if conflict is frequent and outside agencies are involved.",
  "DO NOT recommend punitive consequences as the main response to misread-cue conflicts. REFER via the family to CDNT or SLT where a social communication difficulty or language difficulty is suspected.",
 ],
 "explain_parent": [
  "'Sometimes he reads things as unfriendly when they weren't meant that way, and he reacts. Then he doesn't know how to fix it. Both of those can be taught.'",
  "'After a fall-out, talking through what happened — what he thought, what the other child might have thought — helps more than asking \"why did you do that?\"'",
 ],
 "explain_teacher": [
  "'When she says \"he did it on purpose\", she's telling you how she read it. Start there, not with the consequence.'",
  "'A restorative chat afterwards, with you guiding it, teaches repair. A forced \"sorry\" doesn't.'",
  "'Sarcasm and hints may go straight past him — say what you mean directly.'",
 ],
 "explain_child": [
  "YOUNGER: 'Faces and voices give clues about how people feel. Let's be detectives and look for the clues together.'",
  "OLDER: 'Everyone misreads people sometimes. What matters is noticing it went wrong and knowing a way to fix it. Want to work out a couple of lines you could use?'",
  "ASK: 'When you had that fall-out, what did you think they were thinking?' — shows their interpretation without judgement.",
 ],
 "red_flags": [
  "WATCH — a child who is repeatedly the target in conflicts or is being set up by peers: check for bullying and for social exploitation (being dared, used as the fall guy).",
  "WATCH — reading threat everywhere, hypervigilance, extreme reactions to mild correction: consider trauma and the safeguarding route if there are welfare concerns.",
  "BOUNDARY — describe the social-cue difficulty; do not label it autism or ODD. Diagnosis sits with CDNT, CAMHS or other diagnostic services.",
 ],
 "questions": [
  "Q: 'Why does he think everyone's out to get him?' A: 'Some children read ambiguous situations as hostile — it's a known pattern (Crick & Dodge, 1994). It can be shifted by going through incidents with him and helping him check other explanations.'",
  "Q: 'Shouldn't she just say sorry?' A: 'An apology matters, but repair means understanding what happened. If she understands, the sorry will mean something.'",
  "Q: 'Is it his fault or the other children's?' A: 'Usually both sides have misread each other. We'll support him, and help the class understand him better too.'",
 ],
 "supervision": [
  "Bring an incident analysis and discuss where in the social information-processing sequence the child's difficulty seemed to lie, and how confident you are.",
  "Reflect on the double empathy problem: in your recommendations, whose behaviour are you asking to change?",
 ],
 "citations": [
  "Crick, N. R., & Dodge, K. A. (1994). A review and reformulation of social information-processing mechanisms in children's social adjustment. Psychological Bulletin, 115(1), 74–101.",
  "Gray, C. (1994). Comic strip conversations. Future Horizons.",
  "Milton, D. E. M. (2012). On the ontological status of autism: The 'double empathy problem'. Disability & Society, 27(6), 883–887.",
 ],
})

# ---------------------------------------------------------------- 4
PRES.append({
 "name": "Masking and the cost of it",
 "neps": NEPS_41,
 "related_to": ["Autism", "ADHD", "Social Anxiety Disorder (social phobia)", "Generalised Anxiety Disorder", "Emotionally Based School Avoidance (EBSA)"],
 "what_it_is": [
  "MASKING (also 'camouflaging') means hiding or compensating for differences in order to fit in socially — copying peers' expressions and phrases, rehearsing conversations, suppressing stimming or special interests, forcing eye contact. Hull et al. (2017) described three parts: masking, compensation and assimilation.",
  "THE COST is the point of this presentation: masking takes sustained effort, and adults describe exhaustion, anxiety, loss of a sense of self and delayed recognition of needs (Hull et al., 2017). Cassidy et al. (2018) found camouflaging associated with suicidality in autistic adults — an association, not a proven cause.",
  "In school it shows as a CONTRAST: the child is 'fine in school' and falls apart at home — meltdowns, shutdowns, refusing to talk, exhaustion after school. Parents and teachers then describe two different children, and each may doubt the other.",
  "Most research is on autistic people, particularly girls and women (e.g., Cook et al., 2018), but masking-like effort is also described in ADHD and in anxiety. Pearson and Rose (2021) argue it is best understood as a response to stigma and social context, not only a trait of the person.",
 ],
 "what_it_is_not": [
  "NOT dishonesty or manipulation, and NOT proof that the child is 'fine really'. Coping in school at a cost is still a need.",
  "NOT a diagnosis and NOT diagnostic evidence by itself. It is a description of effort and its consequence. Its presence does not confirm autism; its absence does not rule it out.",
  "NOT a parenting problem because behaviour only happens at home. Home is often where the child feels safe enough to stop masking — the distress was created across the whole day.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: rarely described as masking; more likely a quiet, compliant child in preschool who is dysregulated at home. Note the home–setting contrast and pass it on; do not interpret it yet.",
  "SCHOOL AGE 6–12: after-school collapse, holding it together all day, copying a friend's behaviour closely, reluctance to go to school on Monday mornings. Teachers may report no concerns at all.",
  "ADOLESCENT 13–16: sophisticated masking — scripted conversation, copying peers' style and interests. Exhaustion, anxiety, low mood and school avoidance may emerge. Many autistic girls are first identified at this point.",
  "YOUNG ADULT 17–26: burnout, identity questions, and self-identification before or after diagnosis. The CAT-Q (Hull et al., 2019) is a self-report measure of camouflaging for adults — a research tool, check use before relying on it clinically.",
  "SPECIAL SETTING: less often described, but children with good compliance may still be suppressing distress; watch for self-injury, withdrawal or behaviour change at home.",
 ],
 "assess": [
  "Gather BOTH sides of the contrast deliberately: teacher and parent descriptions of the same week. SRS-2 or SDQ from both raters; a big discrepancy is data, not error.",
  "Pupil interview in a low-demand way (drawing, 'a day in my life', scaling energy through the day): 'When during the day do you have to try hardest? When can you relax?'",
  "Look for the cost: energy, sleep, anxiety (RCADS or Beck Youth Inventories-2 in older children), school attendance patterns (Monday mornings, after PE or yard-heavy days).",
  "Observation in unstructured time: is the child copying peers, on the edge of groups, rehearsing, or visibly tired late in the day?",
 ],
 "recommendations": [
  "BELIEVE THE HOME REPORT: recommend that school and home treat each other's descriptions as valid; plan jointly. Say this explicitly in the report.",
  "REDUCE THE NEED TO MASK: build in legitimate breaks and a quiet space; allow stims and fidgets; reduce forced eye contact; value special interests in class. The aim is to lower the cost of the school day, not to 'stop' masking by force.",
  "PLAN RECOVERY TIME: lighter after-school expectations; homework adjustments where exhaustion is significant; avoid scheduling demanding tasks late in the day.",
  "BUILD SAFE RELATIONSHIPS: a named key adult with whom the pupil does not have to perform; peers with shared interests (clubs, lunchtime groups).",
  "CONTINUUM LEVEL: School Support, with a plan in the Student Support File; School Support Plus if anxiety, mood or attendance is affected and outside agencies are involved.",
  "REFER via the family to CDNT or the relevant autism assessment pathway where a social communication difference is suspected and not identified; to CAMHS or Primary Care Psychology where mood, anxiety or self-harm is present.",
 ],
 "explain_parent": [
  "'What you see at home is real. Many children hold it together all day in school and it spills out when they get home, because home is where they feel safe.'",
  "'School aren't wrong either — they genuinely don't see it. That's why we need to plan together.'",
  "'The goal isn't to stop her fitting in, it's to make school less exhausting so she has less to hold in.'",
 ],
 "explain_teacher": [
  "'He's working very hard to look like he's coping. The cost shows up at home. The difference between what you see and what his parents see is the important finding.'",
  "'A quiet space he can use without asking, and letting him fidget or doodle, will lower how much effort the day takes.'",
  "'Try not to insist on eye contact — he may be listening better without it.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some children try really, really hard in school to look OK, and then feel very tired at home. Does that sound like you?'",
  "OLDER: 'Lots of people put on a kind of act to fit in. It's tiring. It's not wrong, but you shouldn't have to do it all day. Where could you drop it a bit?'",
  "ASK: 'If your energy was a phone battery, what percentage are you at when you get home?' — gives you an everyday measure of the cost.",
 ],
 "red_flags": [
  "RED FLAG — self-harm, suicidal thoughts or talk of wanting to disappear: same-day risk route, inform the DLP and parents per procedure, report to Tusla where there is a child protection concern; supervision follows action.",
  "WATCH — sudden school avoidance, burnout, loss of skills or withdrawal after a period of apparent coping: may indicate the cost has become too high. Act early.",
  "BOUNDARY — masking is described, not diagnosed. Do not tell a family 'she's autistic because she masks'. Describe the pattern and refer.",
 ],
 "questions": [
  "Q: 'She's fine in school — are you saying we're wrong?' A: 'No. You're seeing what she can manage in school. Her parents are seeing what it costs. Both are true.'",
  "Q: 'Is masking a sign of autism?' A: 'It's often described in autistic people, especially girls, but it isn't a diagnostic sign on its own. If there's a wider pattern, the right service can look at it.'",
  "Q: 'Shouldn't we encourage him to fit in?' A: 'We want him to have friends and feel part of things. We don't want that to cost him his wellbeing. Lowering the demand to perform helps with both.'",
  "Q: 'Is it harmful?' A: 'Research in adults links heavy masking with exhaustion, anxiety and, in some studies, suicidality (Cassidy et al., 2018). It's an association, but it's why we take the cost seriously.'",
 ],
 "supervision": [
  "Bring a case with a large school–home discrepancy and discuss how you held both accounts without taking sides.",
  "Reflect on how gender and cultural expectations shape who is noticed and who masks unnoticed.",
  "Discuss risk: at what point did you, or would you, move from support planning to the same-day risk route?",
 ],
 "citations": [
  "Cassidy, S., Bradley, L., Shaw, R., & Baron-Cohen, S. (2018). Risk markers for suicidality in autistic adults. Molecular Autism, 9, Article 42.",
  "Cook, A., Ogden, J., & Winstone, N. (2018). Friendship motivations, challenges and the role of masking for girls with autism in contrasting school settings. European Journal of Special Needs Education, 33(3), 302–315.",
  "Hull, L., Petrides, K. V., Allison, C., Smith, P., Baron-Cohen, S., Lai, M.-C., & Mandy, W. (2017). 'Putting on my best normal': Social camouflaging in adults with autism spectrum conditions. Journal of Autism and Developmental Disorders, 47(8), 2519–2534.",
  "Hull, L., Mandy, W., Lai, M.-C., Baron-Cohen, S., Allison, C., Smith, P., & Petrides, K. V. (2019). Development and validation of the Camouflaging Autistic Traits Questionnaire (CAT-Q). Journal of Autism and Developmental Disorders, 49(3), 819–833.",
  "Pearson, A., & Rose, K. (2021). A conceptual analysis of autistic masking: Understanding the narrative of stigma and the illusion of choice. Autism in Adulthood, 3(1), 52–60.",
 ],
})

# ---------------------------------------------------------------- 5
PRES.append({
 "name": "Loneliness without observable difficulty",
 "neps": NEPS_41,
 "related_to": ["Autism", "Social Anxiety Disorder (social phobia)", "Major Depressive Disorder", "Generalised Anxiety Disorder", "Social (Pragmatic) Communication Disorder"],
 "what_it_is": [
  "LONELINESS is the subjective, distressing feeling that one's social relationships are fewer or less satisfying than wanted (Peplau & Perlman, 1982). It is about perceived quality, not the number of contacts.",
  "'Without observable difficulty' is the crucial part. Part D: 'the quiet ones get missed'. The pupil has someone to sit with, causes no concern, is not bullied — and still feels alone. Adults look for isolation; they rarely ask about loneliness.",
  "Qualter et al. (2015) review loneliness across the lifespan and describe it as a signal of unmet social need that can become self-perpetuating: lonely people become more alert to social threat, which makes connecting harder.",
  "Loneliness is associated with later depression and anxiety in children and adolescents (Loades et al., 2020). Asking about it is a screening opportunity, not intrusion.",
 ],
 "what_it_is_not": [
  "NOT the same as being alone. Some pupils prefer solitude and are content; others are always with a group and still lonely. Ask, do not infer from the yard.",
  "NOT a diagnosis and NOT depression, although it can precede or accompany low mood. It is a description of the child's experience.",
  "NOT only an autism issue. Bauminger and Kasari (2000) found autistic children reported more loneliness despite having friends, but loneliness occurs across every group — new arrivals, young carers, LGBTQ+ pupils, children who have moved school.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: loneliness is hard to measure at this age; look for a child who hovers at the edge of play, seeks adults rather than peers, or says no one plays with them.",
  "SCHOOL AGE 6–12: children can describe loneliness reliably from about age 5–6 (Asher & Paquette, 2003). A child who is 'never any trouble' and who says they have 'sort of' friends may be lonely.",
  "ADOLESCENT 13–16: the transition to post-primary breaks friendship groups; online contact may mask offline isolation. Watch for withdrawal from activities and low mood.",
  "YOUNG ADULT 17–26: leaving school, moving for college or work; loneliness is common and often hidden. Self-report is the main evidence.",
  "SPECIAL SETTING: children with limited speech may still experience loneliness; watch for changes in behaviour, seeking particular peers, or withdrawal, and ask carers who know the child well.",
 ],
 "assess": [
  "ASK DIRECTLY in pupil interview: 'Do you ever feel lonely in school? When? Is there someone you can talk to?' Children answer these questions honestly when asked privately.",
  "Child loneliness questionnaires exist as research measures; none is in the tool catalogue, so check availability and norms before relying on one. In practice use structured interview and scaling ('0 = never lonely, 10 = lonely all the time — where are you at break? in class? at home?').",
  "Sociometric mapping (Part D, 4.1): 'Who would you like to sit beside?' — a pupil nobody names, or who names no one, is a finding even if the yard looks fine.",
  "Screen mood (SDQ, RCADS, MFQ at older ages) because loneliness and low mood often go together.",
 ],
 "recommendations": [
  "MAKE IT ASKABLE: recommend that the class teacher or tutor asks every pupil, periodically and privately, how connected they feel — not only the pupils who show difficulty.",
  "STRUCTURE CONNECTION: lunchtime clubs built around interests, buddy systems, paired tasks with a stable partner, roles that bring the pupil into contact with others (library helper, green schools).",
  "KEY ADULT CHECK-IN: a short, regular check-in with one adult who asks about friendships as well as work.",
  "SUPPORT TRANSITIONS: at primary-to-post-primary transition, plan for at least one known peer in the class group or tutor group where possible.",
  "CONTINUUM LEVEL: Classroom Support (whole-class wellbeing, SPHE); School Support where an individual plan is needed. School Support Plus if low mood or risk is present.",
  "REFER via the family to Primary Care Psychology, Jigsaw (youth mental health, where available) or CAMHS when loneliness is accompanied by low mood, self-harm or risk. Check local services.",
 ],
 "explain_parent": [
  "'She's not having any trouble with other children that we can see — but she told me she often feels lonely. That's worth taking seriously, because it can affect mood.'",
  "'We're going to set up a couple of things in school to help her connect — a lunchtime club and a regular check-in with one teacher.'",
  "'At home, ask her about people she likes, not just whether she has friends. It's easier to answer.'",
 ],
 "explain_teacher": [
  "'He looks fine in the yard — he's always near a group. But he told me he feels on his own. The quiet ones get missed.'",
  "'Ask him privately, now and then, how things are with friends. And set up tasks where he's paired with the same person for a few weeks.'",
 ],
 "explain_child": [
  "YOUNGER: 'Sometimes people feel lonely even when there are lots of people around. Does that ever happen to you?'",
  "OLDER: 'Lonely doesn't mean you have no one. It means the people you have don't feel close enough right now. That's really common and it can change.'",
  "ASK: 'If you could change one thing about break time, what would it be?' — practical, specific, and less exposing than 'are you lonely?'",
 ],
 "red_flags": [
  "RED FLAG — loneliness with hopelessness, talk of being a burden, self-harm or suicidal thoughts: same-day risk route; inform the DLP and parents per procedure; report to Tusla where a child protection concern arises.",
  "WATCH — sudden withdrawal from friends and activities, or loneliness after a friendship breakdown or online conflict: check for bullying, including cyberbullying.",
  "BOUNDARY — loneliness is not a diagnosis; do not describe it as depression. Screen, describe, support and refer where needed.",
 ],
 "questions": [
  "Q: 'She has friends — how can she be lonely?' A: 'Loneliness is about how close those relationships feel, not how many there are (Peplau & Perlman, 1982).'",
  "Q: 'Isn't this just part of being a teenager?' A: 'Some of it is common. But persistent loneliness is linked with later low mood (Loades et al., 2020), so it's worth acting early.'",
  "Q: 'What can school actually do?' A: 'Build in structured chances to connect, check in regularly, and make sure there's one adult who asks.'",
 ],
 "supervision": [
  "Bring a case where the child was referred for something else and loneliness emerged in interview — how did you decide what to do with it?",
  "Discuss how to make loneliness screening routine without over-pathologising normal fluctuations in friendships.",
 ],
 "citations": [
  "Asher, S. R., & Paquette, J. A. (2003). Loneliness and peer relations in childhood. Current Directions in Psychological Science, 12(3), 75–78.",
  "Bauminger, N., & Kasari, C. (2000). Loneliness and friendship in high-functioning children with autism. Child Development, 71(2), 447–456.",
  "Loades, M. E., Chatburn, E., Higson-Sweeney, N., Reynolds, S., Shafran, R., Brigden, A., Linney, C., McManus, M. N., Borwick, C., & Crawley, E. (2020). Rapid systematic review: The impact of social isolation and loneliness on the mental health of children and adolescents in the context of COVID-19. Journal of the American Academy of Child & Adolescent Psychiatry, 59(11), 1218–1239.",
  "Peplau, L. A., & Perlman, D. (Eds.). (1982). Loneliness: A sourcebook of current theory, research and therapy. Wiley.",
  "Qualter, P., Vanhalst, J., Harris, R., Van Roekel, E., Lodder, G., Bangee, M., Maes, M., & Verhagen, M. (2015). Loneliness across the life span. Perspectives on Psychological Science, 10(2), 250–264.",
 ],
})

# ---------------------------------------------------------------- 6
PRES.append({
 "name": "Self-advocacy",
 "neps": NEPS_42,
 "related_to": ["Autism", "ADHD", "Dyslexia", "DLD", "Hearing impairment", "Visual impairment"],
 "what_it_is": [
  "The pupil's ability to UNDERSTAND their own needs and strengths, KNOW what supports or rights they are entitled to, COMMUNICATE those needs to the right adult, and act as a LEADER in their own plan. Test et al. (2005) set out these four components as a conceptual framework for students with disabilities.",
  "Part D lists it under 4.2 (Relationships with adults) as 'Not a DSM diagnosis': it is a skill set exercised with adults — asking a teacher for a copy of the notes, telling an exam centre about an accommodation, explaining a hearing aid to a substitute teacher.",
  "It is rights-based as well as skill-based. Article 12 of the UN Convention on the Rights of the Child gives children the right to express views in matters affecting them; Lundy (2007) argues that voice is not enough — children also need SPACE, AUDIENCE and INFLUENCE.",
  "It matters most at transitions: primary to post-primary, into Senior Cycle and State examinations (SEC Reasonable Accommodations at Certificate Examinations — RACE), and into further/higher education, where adults stop initiating support and the student must ask.",
 ],
 "what_it_is_not": [
  "NOT 'being demanding' or 'making excuses'. A student who asks for the accommodation in their plan is doing exactly what the plan needs.",
  "NOT something that develops automatically with age. It has to be taught and practised, starting with the pupil contributing to their own Student Support File.",
  "NOT only for older or highly verbal pupils. Younger children and those who use AAC can self-advocate through choices, symbols and help cards.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: expressing preferences and asking for help — using words, signs, pictures or a help card. Note whether adults wait for the child to ask or always anticipate.",
  "SCHOOL AGE 6–12: knowing what helps them learn ('I need the instructions written down'), contributing to their plan, asking a teacher for help. Pupil voice in the Student Support File is the concrete vehicle.",
  "ADOLESCENT 13–16: knowing their profile, understanding a diagnosis if they have one, asking subject teachers for supports, understanding RACE accommodations and how to raise them.",
  "YOUNG ADULT 17–26: registering with disability services in further/higher education (DARE and HEAR are access routes — check current criteria), disclosure decisions with employers, asking for reasonable accommodation under equality legislation.",
  "SPECIAL SETTING: choice-making, 'stop' and 'help' communication, a one-page profile the pupil helps create. Record the communication mode and the level of support.",
 ],
 "assess": [
  "Pupil interview about their own learning: 'What are you good at? What's hard? What helps? Who would you tell?' Can they describe their needs in their own words?",
  "Review the Student Support File: is there a pupil voice section, and is it the pupil's words or the adult's summary?",
  "Observation of a moment where help is needed: does the pupil ask, wait, copy, or give up? Which adults do they ask?",
  "Transition-specific checks: does the student know what RACE accommodations are, and whether they apply to them? Does the young adult know how to register with a disability service?",
 ],
 "recommendations": [
  "INVOLVE THE PUPIL in every Student Support Plan meeting or review in some form (attending part, a written or drawn contribution, a one-page profile). Record their views in their words.",
  "TEACH SELF-KNOWLEDGE: explain the pupil's profile to them in plain, strengths-first language, including what a diagnosis means if they have one, with parental agreement.",
  "PRACTISE ASKING: rehearse short scripts with a key adult ('Could I have a copy of the notes?'); use help cards for younger pupils; gradually move from adult-initiated to pupil-initiated support.",
  "PLAN FOR TRANSITIONS: a pupil 'passport' or profile for the next school, the next teacher, the exam centre, the college disability service.",
  "CONTINUUM LEVEL: Classroom Support for pupil voice routines; School Support where a targeted self-advocacy plan is part of the Student Support File.",
  "DO NOT make decisions about the pupil's supports without their voice. Where the pupil and adults disagree, record both views and explain how the decision was made (Lundy, 2007).",
 ],
 "explain_parent": [
  "'We'd like him to be able to explain what helps him learn and to ask for it. That's going to matter more and more as he moves up — in secondary school and exams, adults don't always offer.'",
  "'You can help by talking with him about what he's good at and what's hard, in a matter-of-fact way.'",
 ],
 "explain_teacher": [
  "'Let her write the \"what helps me\" part of the plan herself. It will be shorter than yours, and more useful.'",
  "'When she asks for the supports in her plan, that's a success, not a nuisance. Please make it easy for her.'",
 ],
 "explain_child": [
  "YOUNGER: 'You're the expert on you. What helps you when learning is tricky? Let's make a card you can show the teacher.'",
  "OLDER: 'Knowing what helps you and asking for it is a skill — like any skill, it gets easier with practice. What's one thing you'd like to be able to ask for?'",
  "ASK: 'If a new teacher came in tomorrow, what three things should they know about you?'",
 ],
 "red_flags": [
  "WATCH — a pupil who never asks for help, even when clearly stuck: may reflect anxiety, low self-worth, or past experiences where asking was punished.",
  "WATCH — a pupil who is unaware of their own diagnosis or profile in adolescence: discuss with parents how and when to share it; not knowing makes self-advocacy impossible.",
  "BOUNDARY — self-advocacy does not mean the pupil must disclose a diagnosis to peers or staff. Disclosure is their and their family's decision.",
 ],
 "questions": [
  "Q: 'Won't telling her about her diagnosis upset her?' A: 'Children often cope better knowing than guessing. How and when is your decision; I can help you plan the conversation.'",
  "Q: 'Isn't it our job to organise his supports?' A: 'It is, and it stays that way. We're also teaching him to understand them and ask for them, because by college he'll have to.'",
  "Q: 'What if he asks for something that isn't in the plan?' A: 'Listen, and bring it to the review. Sometimes the pupil knows something we missed.'",
 ],
 "supervision": [
  "Bring a Student Support File and discuss how authentically the pupil's voice is represented — whose words are they?",
  "Reflect on Lundy's (2007) model: in your own consultations, did the child have space, voice, audience and influence?",
 ],
 "citations": [
  "Lundy, L. (2007). 'Voice' is not enough: Conceptualising Article 12 of the United Nations Convention on the Rights of the Child. British Educational Research Journal, 33(6), 927–942.",
  "Test, D. W., Fowler, C. H., Wood, W. M., Brewer, D. M., & Eddy, S. (2005). A conceptual framework of self-advocacy for students with disabilities. Remedial and Special Education, 26(1), 43–54.",
  "United Nations. (1989). Convention on the Rights of the Child. United Nations.",
 ],
})

# ---------------------------------------------------------------- 7
PRES.append({
 "name": "LGBTQ+ identity support",
 "neps": NEPS_42,
 "related_to": ["Gender Dysphoria in adolescents", "Gender Dysphoria in children", "Major Depressive Disorder", "Generalised Anxiety Disorder", "Autism"],
 "what_it_is": [
  "Support for pupils who are lesbian, gay, bisexual, transgender, questioning or otherwise LGBTQ+, so they are safe, included and able to learn. Part D is explicit: 'Not a disorder'. Being LGBTQ+ is not a mental health condition and is not the reason for referral in itself.",
  "The EP role here is SCHOOL CLIMATE and WELLBEING: responding to homophobic and transphobic bullying, supporting the pupil's belonging, and noticing and responding to distress. Meyer's (2003) minority stress model explains elevated mental health difficulties in LGBTQ+ people as a consequence of stigma, prejudice and discrimination — not of the identity.",
  "Irish evidence: the LGBTIreland Report (Higgins et al., 2016) and the BeLonG To School Climate Surveys report experiences of homophobic and transphobic remarks and bullying in Irish schools, and higher levels of self-harm and distress among LGBTI young people than in comparison samples. Check the current reports for figures before quoting.",
  "Gender identity questions in children and adolescents are an area where clinical guidance is contested and changing. The Cass Review (2024) in England recommended a cautious, holistic approach and a clinical framework for decisions about social transition. Check current Irish (HSE and Department of Education) guidance before advising a school — this is an active area.",
 ],
 "what_it_is_not": [
  "NOT a psychological problem to be assessed or changed. Conversion practices are harmful and not endorsed by professional bodies; the EP never tries to change a young person's sexual orientation or gender identity.",
  "NOT a diagnosis. Gender Dysphoria is a separate clinical diagnosis made by specialist services, not by the EP, and most LGBTQ+ young people have no gender-related diagnosis at all.",
  "NOT a reason to assume distress. Many LGBTQ+ pupils are doing well; distress, where it exists, is usually about bullying, rejection or fear of rejection — the environment.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: not about sexual orientation. Gender-nonconforming play and preferences are common and are not a clinical concern in themselves. Support inclusive practice; avoid assumptions.",
  "SCHOOL AGE 6–12: family diversity (children with same-sex parents), homophobic language in the yard ('that's so gay'), and, for some children, questions about gender. Respond to language and inclusion; be cautious and consult on any request for social transition.",
  "ADOLESCENT 13–16: the core band. Coming out (or not), bullying, online exposure, family acceptance, identity exploration. Mental health risk is elevated in some young people; watch closely.",
  "YOUNG ADULT 17–26: further/higher education and work; adult LGBTQ+ services and supports. Many young adults describe the school years as the hardest period.",
  "SPECIAL SETTING: young people with intellectual disability and autistic young people are also LGBTQ+ and may have fewer ways to express it or find community; ensure RSE and inclusion reach them.",
 ],
 "assess": [
  "This is not something to be 'assessed'. Where there is a referral, the questions are: is the pupil safe? Is there bullying? How is their wellbeing? Who are their supports?",
  "Pupil interview on the pupil's terms: let them use their own words for their identity; ask what name and pronouns they use in which settings, and who knows. Do not disclose to anyone without their agreement unless there is a safeguarding need.",
  "Wellbeing screening where indicated: SDQ, RCADS or MFQ; risk screening for self-harm and suicidal ideation.",
  "School climate: anti-bullying records, homophobic and transphobic incidents, inclusion of LGBTQ+ identities in SPHE/RSE, the presence of a visible supportive adult.",
 ],
 "recommendations": [
  "RESPOND TO BULLYING: homophobic and transphobic bullying is named in Irish anti-bullying procedures; recommend the school applies its procedures (Department of Education, 2024 Bullying Prevention and Intervention procedures under Cineáltas — check current version).",
  "VISIBLE SAFE ADULTS: at least one named adult the pupil trusts; LGBTQ+ inclusive posters or signals; a student support group if the school has one (BeLonG To supports schools — check current offerings).",
  "CONFIDENTIALITY AND SAFEGUARDING: respect the pupil's control over who knows about their identity; do not 'out' a pupil. Where safeguarding requires sharing, explain to the pupil what will be shared and why. Record decisions.",
  "GENDER IDENTITY REQUESTS (name, pronouns, facilities, uniform): these are school decisions involving the pupil, parents and school management. Recommend the school checks current Department of Education and HSE guidance and seeks advice; the EP supports wellbeing and process, not clinical decisions about transition.",
  "CONTINUUM LEVEL: Classroom Support (inclusive RSE/SPHE, anti-bullying culture); School Support where the pupil needs an individual plan; School Support Plus where mental health risk means outside agencies are involved.",
  "REFER via the family to Primary Care Psychology, Jigsaw or CAMHS for mental health needs; to GP for onward referral to specialist gender services where the young person and family wish to seek assessment. Check current service pathways.",
 ],
 "explain_parent": [
  "'Your child isn't unwell because they're gay. What we want to make sure is that they feel safe and supported in school, and that they're coping.'",
  "'Some parents find this a big adjustment. It's OK to need time. What helps young people most is knowing their family is still on their side.'",
  "SIGNPOST: BeLonG To (youth organisation), LGBT Ireland family supports, GP; check current services before giving details.",
 ],
 "explain_teacher": [
  "'Please challenge \"that's so gay\" every time, calmly. Unchallenged language tells LGBTQ+ pupils the room isn't safe.'",
  "'Don't share what she's told you about her identity with other staff unless she agrees, or unless there's a safeguarding reason.'",
  "'On names and pronouns, follow the plan the school has agreed with the pupil and family, and check current guidance — this is not something to decide alone in the classroom.'",
 ],
 "explain_child": [
  "OLDER: 'You don't have to explain or label yourself to me. What I care about is whether you feel safe here and how you're doing.'",
  "OLDER: 'Who you tell is up to you. The only time I'd share anything is if I was worried you or someone else wasn't safe, and I'd tell you first.'",
  "ASK: 'Is there anything about school that makes it harder to be yourself? What would help?'",
 ],
 "red_flags": [
  "RED FLAG — self-harm, suicidal ideation or expressions of hopelessness: same-day risk route; inform the DLP and parents per procedure (with care where family rejection is part of the risk); report to Tusla where a child protection concern arises; supervision follows action.",
  "RED FLAG — rejection, threats or violence at home because of identity, or being made to leave home: child protection route to Tusla.",
  "WATCH — persistent homophobic or transphobic bullying, including online: apply anti-bullying procedures; monitor wellbeing.",
  "BOUNDARY — the EP does not assess or diagnose gender dysphoria and does not advise on medical transition. Refer via the family and GP.",
 ],
 "questions": [
  "Q: 'Is this just a phase?' A: 'For some young people identity changes over time, and for many it doesn't. Either way, what they need from school now is to be safe and respected.'",
  "Q: 'Should we tell the parents?' A: 'The pupil's wishes matter, and outing a young person can put them at risk. But safeguarding comes first. Talk with the DLP about this pupil's circumstances; don't decide alone.'",
  "Q: 'Should we use a new name and pronouns?' A: 'That's a decision for the school with the pupil and family, taking account of current guidance, which is changing. I can support the process and the pupil's wellbeing, but it isn't a clinical decision I make.'",
  "Q: 'Are LGBTQ+ young people more at risk?' A: 'Irish surveys report higher rates of self-harm and distress (Higgins et al., 2016), linked with stigma and bullying (Meyer, 2003). That's why a safe school environment matters so much.'",
 ],
 "supervision": [
  "Bring any case involving confidentiality versus parental involvement, after immediate safeguarding steps are taken.",
  "Reflect on your own views and values and how they might shape your practice; stay within current professional guidance and the EP role.",
  "Check the current state of Irish guidance on gender identity in schools before each case — it is changing.",
 ],
 "citations": [
  "Cass, H. (2024). Independent review of gender identity services for children and young people: Final report. NHS England.",
  "Higgins, A., Doyle, L., Downes, C., Murphy, R., Sharek, D., DeVries, J., Begley, T., McCann, E., Sheerin, F., & Smyth, S. (2016). The LGBTIreland report: National study of the mental health and wellbeing of lesbian, gay, bisexual, transgender and intersex people in Ireland. GLEN and BeLonG To.",
  "Meyer, I. H. (2003). Prejudice, social stress, and mental health in lesbian, gay, and bisexual populations: Conceptual issues and research evidence. Psychological Bulletin, 129(5), 674–697.",
  "Department of Education. (2024). Bullying prevention and intervention procedures for primary and post-primary schools [Check current title and version]. Government of Ireland.",
 ],
})

# ---------------------------------------------------------------- 8
PRES.append({
 "name": "Cultural and linguistic identity",
 "neps": NEPS_42,
 "related_to": ["English as an Additional Language and bilingual development (DLD vs EAL)", "DLD", "Posttraumatic Stress Disorder (including Complex PTSD)", "Selective Mutism", "Relational problems (parent-child, sibling, upbringing away from parents)"],
 "what_it_is": [
  "How a pupil's culture, ethnicity, religion and language(s) shape their experience of school, their relationships with staff and peers, and how they are understood and assessed. Part D: 'Not a disorder'. It sits under 4.2 because the relationship with adults — who understands me, who pronounces my name — is where it is most felt.",
  "In Ireland this includes pupils who are newcomers from many countries, children of Irish Travellers (whose ethnic identity was formally recognised by the State in 2017), Roma children, pupils in Irish-medium schools (Gaelscoileanna, Gaeltacht schools), and Deaf pupils who use Irish Sign Language (recognised under the Irish Sign Language Act 2017).",
  "Berry (1997) describes acculturation strategies — integration, assimilation, separation, marginalisation. Integration (holding both identities) is generally associated with better adaptation; marginalisation with the poorest.",
  "Cummins (2000) distinguished conversational fluency (BICS) from academic language proficiency (CALP): pupils may sound fluent within a year or two while academic language takes much longer. Misreading this is one of the commonest assessment errors in EAL.",
 ],
 "what_it_is_not": [
  "NOT a special educational need in itself. Learning English as an additional language is not a learning difficulty (NEPS and NCCA guidance; check current documents).",
  "NOT a reason to lower expectations. Stereotyped expectations of particular groups affect outcomes; set expectations from what the child shows, not from background.",
  "NOT only a matter for pupils from outside Ireland. Travellers, Irish speakers and Deaf pupils have distinct cultural and linguistic identities that schools can overlook.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: home language development, a silent period in a new language setting (common and usually temporary), and whether home language is valued. Encourage parents to keep using the home language.",
  "SCHOOL AGE 6–12: gap between conversational and academic English; name pronunciation; religious and cultural practices (fasting, holidays); being the family's interpreter.",
  "ADOLESCENT 13–16: identity negotiation between home and peer culture; racism and discrimination; exam access in an additional language; Irish language exemption questions (check current Department of Education circular).",
  "YOUNG ADULT 17–26: access to further/higher education, recognition of qualifications, identity consolidation; experiences of racism in work and study.",
  "SPECIAL SETTING: pupils with additional needs from minority backgrounds may have parents unfamiliar with Irish systems; interpreting, cultural understanding of disability and communication modes (including ISL) all matter.",
 ],
 "assess": [
  "Background interview with parents (with a trained interpreter — never a child): languages spoken, schooling history, migration journey, family's understanding of the concern.",
  "Language history: dominant language, age of exposure to English (or Irish), progress in home language. A difficulty present in BOTH languages is more suggestive of an underlying language need than one only in English.",
  "Cautious use of standardised tests: most norms are not representative of EAL pupils; consider non-verbal measures (WNV, Leiter-3) and dynamic assessment. Report the limits explicitly.",
  "Pupil voice about belonging: 'Do adults here say your name right? Is there anyone who speaks your language? What do you miss?'",
 ],
 "recommendations": [
  "VALUE THE IDENTITY VISIBLY: learn and use the pupil's name correctly; reflect languages and cultures in the classroom; invite the pupil's knowledge into lessons.",
  "SUPPORT ACADEMIC LANGUAGE: plan for CALP as well as conversational English — pre-teach subject vocabulary, use visuals and graphic organisers, allow home-language use for thinking (Cummins, 2000).",
  "WORK WITH FAMILIES through interpreters and cultural mediators where available; do not rely on the child to interpret, especially for sensitive matters.",
  "RESPOND TO RACISM through the school's anti-bullying and equality procedures; record and follow up identity-based bullying.",
  "CONTINUUM LEVEL: Classroom Support for most; School Support where language support or wellbeing supports are targeted.",
  "DO NOT diagnose or imply DLD, intellectual disability or autism on the basis of English-only assessment. REFER via the family to SLT or CDNT only where there is evidence of difficulty in the home language as well.",
 ],
 "explain_parent": [
  "'Keep using your home language at home. It doesn't hold back English — it helps. Children who keep their first language strong usually do better in the second.'",
  "'Your child is learning in English all day. It takes years to fully learn the kind of English school needs. What we're seeing so far fits with that.'",
  "SIGNPOST: local integration supports, Traveller or migrant family organisations, interpreters through the school or HSE — check local availability.",
 ],
 "explain_teacher": [
  "'She sounds fluent in the yard, but school English is a different, harder kind. Pre-teach the key words before each topic.'",
  "'Please ask her how to say her name and practise it. It matters more than it seems.'",
  "'Don't use a younger sibling to interpret for parents — book an interpreter.'",
 ],
 "explain_child": [
  "YOUNGER: 'You can speak two languages — that's a special skill. Your brain is doing lots of extra work.'",
  "OLDER: 'Being between two cultures can be a lot. Some things about school here might feel strange. What's been hardest? What's been OK?'",
  "ASK: 'Is there anything about who you are or where you're from that you wish teachers understood?'",
 ],
 "red_flags": [
  "WATCH — racist bullying or harassment: apply anti-bullying and equality procedures; monitor wellbeing.",
  "WATCH — signs of trauma from migration or displacement (hypervigilance, sleep difficulty, withdrawal): consider psychological supports and referral; follow the child protection route if there are welfare concerns.",
  "BOUNDARY — do not diagnose language disorder on English-only evidence. Describe progress in context and refer where evidence supports it.",
 ],
 "questions": [
  "Q: 'Should they stop speaking their language at home so English improves?' A: 'No. Keeping the home language supports learning English and protects the relationship with family (Cummins, 2000).'",
  "Q: 'He's been here two years — shouldn't he be caught up?' A: 'Everyday English comes fairly quickly. School English takes much longer, often several years. That's typical, not a sign of a difficulty.'",
  "Q: 'How can we tell if it's EAL or a language disorder?' A: 'Look at the home language. If there's a difficulty there too, that's more concerning. That's a question for SLT, with an interpreter.'",
 ],
 "supervision": [
  "Bring any assessment with an EAL pupil and discuss how you reported the limits of norms and the influence of language on scores.",
  "Reflect on your own cultural assumptions — about parenting, disability, eye contact, what 'engaged' looks like — and how they shaped your observations.",
 ],
 "citations": [
  "Berry, J. W. (1997). Immigration, acculturation, and adaptation. Applied Psychology, 46(1), 5–34.",
  "Cummins, J. (2000). Language, power and pedagogy: Bilingual children in the crossfire. Multilingual Matters.",
  "Irish Sign Language Act 2017. Government of Ireland.",
 ],
})

# ---------------------------------------------------------------- 9
PRES.append({
 "name": "Attitude towards staff",
 "neps": NEPS_42,
 "related_to": ["Oppositional Defiant Disorder", "ADHD", "Relational problems (parent-child, sibling, upbringing away from parents)", "Posttraumatic Stress Disorder (including Complex PTSD)", "Autism"],
 "what_it_is": [
  "A description of how a pupil relates to adults in school — warm, wary, dismissive, hostile, over-familiar, indifferent. Part D gives it as 'Form 2 survey wording': it is the phrase teachers tick on the referral form, so it is often the starting point of the referral rather than the finding.",
  "Pianta (1999) frames the teacher–child relationship as a system with three features that can be described: CLOSENESS, CONFLICT and DEPENDENCY. 'Attitude' usually refers to high conflict or low closeness — it is a property of the relationship, not only of the child.",
  "Hamre and Pianta (2001) found that conflictual teacher–child relationships in the first year of school predicted later academic and behavioural outcomes; Roorda et al. (2011) found across studies that positive relationships were associated with engagement and achievement. The relationship is an intervention target.",
  "Part D (School Age, 4.2): 'Observation across different adults — the difference between teachers is data.' A pupil whose 'attitude' is good with two adults and poor with one is telling you something about that relationship.",
 ],
 "what_it_is_not": [
  "NOT a fixed personality trait. The same pupil can have very different relationships with different staff; the pattern is the finding.",
  "NOT only a behaviour problem for the code of behaviour. The attitude usually has a history — past experiences with adults, feeling unfairly treated, feeling unable to do the work.",
  "NOT a diagnosis. It sometimes sits beside ODD, trauma or ADHD, but the description stands alone and is often more useful than a label.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: wariness of new adults, clinginess to one, or indiscriminate friendliness toward strangers. Indiscriminate friendliness may warrant attention to early care history.",
  "SCHOOL AGE 6–12: 'cheeky', ignoring instructions, preferring one teacher, conflict with SNAs or substitute teachers. Class teacher relationship is dominant — one year's relationship can shape the next.",
  "ADOLESCENT 13–16: many subject teachers means many relationships; attitude varies widely by subject and teacher. Adolescent resistance to authority is developmentally expected in part; describe severity and pattern.",
  "YOUNG ADULT 17–26: attitudes to tutors, lecturers, supervisors and employers; self-report and specific incidents.",
  "SPECIAL SETTING: relationships with many adults (teachers, SNAs, therapists); consider communication difficulties and sensory needs behind apparent hostility.",
 ],
 "assess": [
  "Observe the pupil with at least two different adults, ideally one described as 'difficult' and one 'good'. Record adult behaviour too — tone, proximity, praise-to-correction ratio.",
  "Teacher consultation: 'When is the relationship at its best? What happened the first time it went wrong?' The Student–Teacher Relationship Scale (Pianta, 2001) is one way to describe closeness and conflict — check availability.",
  "Pupil interview: 'Which teachers do you get on with? What do they do differently?' Pupils usually describe very specific adult behaviours.",
  "Consider underlying drivers: unmet learning need (work too hard), language difficulty (misunderstanding), trauma history, feeling singled out.",
 ],
 "recommendations": [
  "INVEST IN THE RELATIONSHIP DELIBERATELY: brief daily positive contact from the teacher not linked to work or behaviour ('banking time', a concept from Pianta's work — check source for detail); greet at the door; notice interests.",
  "USE THE ADULTS IT WORKS WITH: identify what the successful adults do and share it; consider the pupil's key adult as a link.",
  "REPAIR AFTER CONFLICT: the adult initiates repair ('That was a hard morning. Tomorrow's a fresh start.'); avoid carrying yesterday into today.",
  "ADDRESS THE UNDERLYING NEED: if the work is too hard or the language too complex, the attitude often follows the demand. Adjust the demand.",
  "CONTINUUM LEVEL: Classroom Support; School Support where a relationship plan is needed; School Support Plus if behaviour is escalating and outside agencies are involved.",
  "DO NOT write 'poor attitude' in a report as a finding. Describe observed interactions and the conditions under which they differ.",
 ],
 "explain_parent": [
  "'He gets on well with some teachers and not others. That tells us it's about the relationship, which is good news — relationships can change.'",
  "'We're going to work on building one good relationship first, and use what works there with other teachers.'",
 ],
 "explain_teacher": [
  "'She's fine with Ms X and struggles with others — including you. It's not personal; it's worth finding out what Ms X is doing.'",
  "'Two minutes a day of positive contact that has nothing to do with work can change how the whole day goes.'",
  "'After a clash, you starting the repair tomorrow is powerful. It shows the relationship survives conflict.'",
 ],
 "explain_child": [
  "YOUNGER: 'Some grown-ups in school are easier to get on with than others. Who are the easy ones? What do they do?'",
  "OLDER: 'You get on with some teachers and not others — that's normal. What do the good ones do that makes a difference?'",
  "ASK: 'If you could tell one teacher one thing, what would it be?'",
 ],
 "red_flags": [
  "WATCH — fear of adults, flinching, or extreme reactions to adult proximity: consider trauma; follow the child protection route if there are welfare concerns.",
  "WATCH — indiscriminate friendliness toward unknown adults: may reflect early care experiences and presents a safeguarding vulnerability; discuss with the DLP.",
  "BOUNDARY — 'attitude' is not a diagnosis. Describe relationships and refer only if there is a wider mental health or developmental question.",
 ],
 "questions": [
  "Q: 'Isn't it just that she's rude?' A: 'She might be rude with some adults. The question is why with them and not with others — that's where we can change something.'",
  "Q: 'Why should I have to build a relationship — shouldn't he just respect me?' A: 'Respect helps. But the research shows the relationship itself predicts behaviour and learning (Hamre & Pianta, 2001). It's the most efficient lever we have.'",
  "Q: 'Is this ODD?' A: 'Difficulty with adults is part of ODD, but one poor relationship isn't. If there's a pattern across settings and adults, we can talk about a referral.'",
 ],
 "supervision": [
  "Bring an observation of the pupil with two different adults and discuss how to feed back differences sensitively to staff.",
  "Reflect on your own relationship with the pupil — did your attitude shift after hearing the referral?",
 ],
 "citations": [
  "Hamre, B. K., & Pianta, R. C. (2001). Early teacher–child relationships and the trajectory of children's school outcomes through eighth grade. Child Development, 72(2), 625–638.",
  "Pianta, R. C. (1999). Enhancing relationships between children and teachers. American Psychological Association.",
  "Pianta, R. C. (2001). Student–Teacher Relationship Scale: Professional manual. Psychological Assessment Resources.",
  "Roorda, D. L., Koomen, H. M. Y., Spilt, J. L., & Oort, F. J. (2011). The influence of affective teacher–student relationships on students' school engagement and achievement: A meta-analytic approach. Review of Educational Research, 81(4), 493–529.",
 ],
})

# ---------------------------------------------------------------- 10
PRES.append({
 "name": "Trust and the effect of one key adult",
 "neps": NEPS_42,
 "related_to": ["Relational problems (parent-child, sibling, upbringing away from parents)", "Posttraumatic Stress Disorder (including Complex PTSD)", "Reactive Attachment Disorder", "Emotionally Based School Avoidance (EBSA)", "Autism"],
 "what_it_is": [
  "Two sides of one pattern: a pupil who finds it hard to TRUST adults in school, and the observation that ONE trusted adult can change how the pupil copes. Part D places it under 4.2 alongside relational problems.",
  "Attachment theory (Bowlby, 1969) proposes that early relationships shape expectations of whether adults are reliable and safe. Bomber (2007) and Geddes (2006) translate this for schools: children with insecure attachment histories may test, avoid or cling to adults, and a 'key adult' provides the reliable relationship they need to learn.",
  "In Ireland, the My World Survey (Dooley & Fitzgerald, 2012) highlighted the 'One Good Adult' — young people who reported having a supportive adult in their lives reported better mental health. It is one of the most widely used messages in Irish youth mental health.",
  "Resilience research (Werner & Smith, 1992) found that at-risk children who did well often had at least one supportive adult outside the family — frequently a teacher.",
 ],
 "what_it_is_not": [
  "NOT dependency to be discouraged. A strong relationship with a key adult is the intervention; independence grows from security, not from withdrawal of support.",
  "NOT a diagnosis of attachment disorder. Reactive Attachment Disorder is a rare clinical diagnosis made by specialist services; 'attachment difficulties' as a school description is broader and should not be confused with it.",
  "NOT a replacement for therapeutic or specialist input when that is needed. The key adult supports; they do not treat.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: key person approach in early years settings; separation difficulties; clinging to or avoiding carers. Consistency of the key person matters most.",
  "SCHOOL AGE 6–12: the class teacher or SNA often becomes the key adult by default; the pupil copes with them and falls apart with substitutes or at year change.",
  "ADOLESCENT 13–16: fewer natural key adults in post-primary; year head, tutor, guidance counsellor or chaplain may be chosen. The young person chooses — not the timetable.",
  "YOUNG ADULT 17–26: mentors, tutors, employers; the principle remains, but supports are less structured.",
  "SPECIAL SETTING: key adult relationships are often strong; planning for staff changes and absences is essential to avoid distress.",
 ],
 "assess": [
  "Map the adults: 'Who in school do you trust? Who would you go to if something was wrong?' (pupil interview; drawings or relationship maps for younger children).",
  "Observe the pupil with the key adult and with other adults: what changes? How does the pupil cope when the key adult is absent?",
  "Background history with parents and records (with consent): changes of carer, bereavement, care history, trauma, which shape trust.",
  "Ask staff: 'Who does this pupil respond to? What does that person do?'",
 ],
 "recommendations": [
  "NAME A KEY ADULT deliberately (not only by default), ideally someone the pupil already trusts, with protected time for brief, regular contact (Bomber, 2007).",
  "PLAN FOR ABSENCE AND TRANSITION: a second known adult; forewarning of absences; a planned handover at year change or transition to post-primary.",
  "SUPPORT THE KEY ADULT: time, supervision or consultation, and clarity about boundaries. Holding a distressed pupil's trust is demanding work.",
  "EXTEND TRUST GRADUALLY: the key adult helps the pupil build a second and third relationship, rather than being the only one.",
  "CONTINUUM LEVEL: School Support; School Support Plus if trauma, care involvement or outside agencies are involved.",
  "REFER via the family (or social worker if in care) to CAMHS, Primary Care Psychology or Tusla-linked supports where trauma or attachment needs require specialist input.",
 ],
 "explain_parent": [
  "'She trusts a small number of adults, and when one of them is there, she copes far better. We want to build on that.'",
  "'Having one good adult in school is one of the strongest things we know helps young people. We're going to make sure she has that deliberately, and a back-up.'",
 ],
 "explain_teacher": [
  "'He trusts you. That's not a problem to fix — it's what's keeping him in school. Let's plan how you can help him trust one more person.'",
  "'When you're off, tell him in advance if you can, and make sure he knows who to go to.'",
 ],
 "explain_child": [
  "YOUNGER: 'Who's a grown-up in school that makes you feel safe? What do they do?'",
  "OLDER: 'Most people have one or two people they trust. In school, who's yours? And who'd be your back-up?'",
  "ASK: 'What does a good adult do that makes it easier to trust them?'",
 ],
 "red_flags": [
  "RED FLAG — any disclosure of abuse or neglect to the key adult: child protection route; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty.",
  "WATCH — an adult–pupil relationship with blurred boundaries (secrecy, contact outside school, gifts): safeguarding concern; raise with the DLP.",
  "WATCH — acute distress when the key adult leaves: plan transitions early.",
 ],
 "questions": [
  "Q: 'Isn't he too dependent on me?' A: 'Security usually comes before independence. We'll build a second relationship alongside yours, not replace yours.'",
  "Q: 'Does she have an attachment disorder?' A: 'That's a rare diagnosis made by specialist services. What I can say is that she finds trusting adults hard, and that we know what helps.'",
  "Q: 'What happens when I'm gone next year?' A: 'We plan for it now — a gradual handover to the next teacher, with you still there as a link for a while if possible.'",
 ],
 "supervision": [
  "Bring a case where one relationship is holding a pupil in school and discuss how to protect it and extend it.",
  "Reflect on boundaries: how does the key adult get support, and how do you know when the relationship needs more help than school can provide?",
 ],
 "citations": [
  "Bomber, L. M. (2007). Inside I'm hurting: Practical strategies for supporting children with attachment difficulties in schools. Worth Publishing.",
  "Bowlby, J. (1969). Attachment and loss: Vol. 1. Attachment. Hogarth Press.",
  "Dooley, B., & Fitzgerald, A. (2012). My World Survey: National study of youth mental health in Ireland. Headstrong and UCD School of Psychology.",
  "Geddes, H. (2006). Attachment in the classroom: The links between children's early experience, emotional well-being and performance in school. Worth Publishing.",
  "Werner, E. E., & Smith, R. S. (1992). Overcoming the odds: High risk children from birth to adulthood. Cornell University Press.",
 ],
})

# ---------------------------------------------------------------- 11
PRES.append({
 "name": "Response to authority and to being corrected",
 "neps": NEPS_42,
 "related_to": ["Oppositional Defiant Disorder", "ADHD", "Posttraumatic Stress Disorder (including Complex PTSD)", "Autism", "Conduct Disorder"],
 "what_it_is": [
  "A description of what happens when an adult gives a direction, sets a limit, or corrects the pupil: compliance, argument, shutdown, escalation, laughing it off, tears. The pattern — and what triggers the worst response — is the finding.",
  "Being corrected touches on SHAME. Some pupils experience correction as a threat to their sense of self; their reaction is defensive rather than defiant. Bomber (2007) describes shame-based responses in children with attachment or trauma histories.",
  "Rejection sensitivity (Downey & Feldman, 1996) — anxious expectation of rejection — makes some pupils read mild correction as rejection and respond intensely. Hattie and Timperley (2007) show that feedback aimed at the self is less effective than feedback aimed at the task or process.",
  "Greene's Collaborative & Proactive Solutions approach (Greene, 2014) reframes it: 'kids do well if they can'. Poor response to correction reflects lagging skills (flexibility, frustration tolerance, problem-solving) and unsolved problems, not unwillingness.",
 ],
 "what_it_is_not": [
  "NOT simply defiance. Defiance is one explanation; shame, anxiety, misunderstanding, sensory overload and a sense of unfairness are others.",
  "NOT evidence of ODD by itself. ODD is a diagnosis made by specialist services with specific criteria; a difficult response to correction is common in many pupils without it.",
  "NOT fixed by escalating sanctions. More correction to a shame-sensitive pupil usually increases the reaction.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: tantrums at limits are common; look at intensity, recovery time and whether the child can accept comfort afterwards.",
  "SCHOOL AGE 6–12: arguing, sulking, tearing up work after correction, 'it's not fair'. Public correction in front of peers is often the trigger.",
  "ADOLESCENT 13–16: challenge to authority is partly developmental. Watch for escalation to suspensions and the pattern across teachers — some adults may never trigger it.",
  "YOUNG ADULT 17–26: response to feedback at college or work; difficulty accepting criticism can threaten placements and employment.",
  "SPECIAL SETTING: check communication — does the pupil understand the correction? Consider sensory and demand-avoidant profiles.",
 ],
 "assess": [
  "ABC observation of correction episodes: how was the correction given (public or private, tone, words), what did the pupil do, and what happened next? Functional behaviour assessment (ABC) is in the tool catalogue for this purpose.",
  "Compare adults: which adults can correct the pupil without escalation, and what do they do differently? (Part D, 4.2: the difference between teachers is data.)",
  "Pupil interview after calm: 'What goes on in your head when a teacher tells you off?' The answer distinguishes shame, unfairness, anxiety and anger.",
  "Consider language comprehension, ADHD, trauma history and learning difficulty (correction may be frequent because the work is too hard).",
 ],
 "recommendations": [
  "CORRECT PRIVATELY AND BRIEFLY where possible: a quiet word or a pre-agreed signal, not public correction in front of peers.",
  "SEPARATE THE BEHAVIOUR FROM THE PERSON: task-focused feedback ('the next step is...') rather than self-focused ('you're being lazy') (Hattie & Timperley, 2007).",
  "PLAN FOR REPAIR: after correction, the adult reconnects quickly — a neutral or positive contact soon after tells the pupil the relationship is intact.",
  "SOLVE PROBLEMS COLLABORATIVELY: identify the recurring situations where correction happens and work with the pupil on them (Greene, 2014).",
  "CONTINUUM LEVEL: Classroom Support to School Support; School Support Plus where escalation leads to suspension or outside agency involvement.",
  "DO NOT recommend repeated suspension without a planned reintegration. REFER via the family to CAMHS or Primary Care where there is a wider mental health or diagnostic question.",
 ],
 "explain_parent": [
  "'When he's corrected, especially in front of others, he seems to feel ashamed, and he reacts to cover it up. It looks like defiance, but it's often embarrassment.'",
  "'At home, a quiet correction and a quick reconnection afterwards — \"we're fine, let's move on\" — tends to work better than a long telling-off.'",
 ],
 "explain_teacher": [
  "'Try correcting her quietly at her desk or with a signal. Public correction almost always escalates.'",
  "'Two minutes after, say something neutral or kind. It tells her you're not holding on to it.'",
  "'Mr Y can correct him without a blow-up — it might be worth asking how he does it.'",
 ],
 "explain_child": [
  "YOUNGER: 'When a teacher says stop, what happens in your body? Hot? Fast? Let's think of something that helps.'",
  "OLDER: 'Getting corrected feels rubbish for everyone. For some people it feels massive — like it's about them, not what they did. Does that sound familiar?'",
  "ASK: 'What's the best way for a teacher to tell you you've got something wrong?'",
 ],
 "red_flags": [
  "WATCH — extreme reactions to mild correction, hypervigilance, or fear of adults: consider trauma; follow the child protection route if there are welfare concerns.",
  "WATCH — self-harm or statements like 'I'm useless' after correction: assess risk the same day; inform the DLP and parents per procedure.",
  "BOUNDARY — do not describe the pupil as 'oppositional' or 'ODD' in a report. Describe the pattern and refer if needed.",
 ],
 "questions": [
  "Q: 'So we shouldn't correct him?' A: 'You should — it's how he learns. The question is how: privately, briefly, about the task, and with a quick reconnection afterwards.'",
  "Q: 'Isn't this just a cheeky teenager?' A: 'Some of it is typical. What stands out is the intensity and how it varies between teachers — that's what we can work with.'",
  "Q: 'Is this ODD?' A: 'That's a diagnosis made by specialist services. What I see is a pupil who finds correction very hard, and there are clear things we can change.'",
 ],
 "supervision": [
  "Bring an ABC record of correction episodes and discuss what function the response seems to serve.",
  "Reflect on how you feed back to a teacher that their correction style may be contributing, without blame.",
 ],
 "citations": [
  "Bomber, L. M. (2007). Inside I'm hurting: Practical strategies for supporting children with attachment difficulties in schools. Worth Publishing.",
  "Downey, G., & Feldman, S. I. (1996). Implications of rejection sensitivity for intimate relationships. Journal of Personality and Social Psychology, 70(6), 1327–1343.",
  "Greene, R. W. (2014). Lost at school: Why our kids with behavioral challenges are falling through the cracks and how we can help them (Rev. ed.). Scribner.",
  "Hattie, J., & Timperley, H. (2007). The power of feedback. Review of Educational Research, 77(1), 81–112.",
 ],
})

# ---------------------------------------------------------------- 12
PRES.append({
 "name": "Relationship with the SNA and dependence on adult proximity",
 "neps": NEPS_42,
 "related_to": ["Autism", "Intellectual Disability", "Physical disability", "ADHD", "Generalised Anxiety Disorder"],
 "what_it_is": [
  "A description of how a pupil relates to a Special Needs Assistant (SNA) or other adult who is close by for much of the day — and whether that closeness has become something the pupil cannot manage without, even for tasks they could do.",
  "In Ireland the SNA scheme exists to support the CARE needs of pupils with significant needs arising from a disability; the SNA's role is not teaching (Department of Education and Skills Circular 0030/2014 — check for any later circular). The NCSE's Comprehensive Review of the SNA Scheme (NCSE, 2018) recommended a broader model of support; check current policy before advising.",
  "Giangreco et al. (1997) described the unintended effects of close adult proximity: separation from the class teacher and peers, dependence on adults, reduced peer interaction, loss of personal control, and stigma. The UK Deployment and Impact of Support Staff (DISS) project found pupils with most TA support often made less progress than similar pupils with less, largely because of how support was deployed (Blatchford et al., 2012; Webster et al., 2016).",
  "The presentation is about DEPLOYMENT and INDEPENDENCE, not about the quality of the SNA. Many SNAs are highly skilled; the question is whether the arrangement builds or restricts independence.",
 ],
 "what_it_is_not": [
  "NOT a criticism of the SNA. Dependence usually reflects how the role has been set up — seating, expectations, lack of planning time with the teacher — rather than the individual.",
  "NOT a reason to remove the SNA abruptly. Sudden withdrawal can cause distress and loss of care support; fading must be planned.",
  "NOT the SNA's job to teach or to hold responsibility for the pupil's learning. The class teacher retains responsibility for teaching all pupils in the class.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: in early years settings, AIM (Access and Inclusion Model) supports may provide additional staff; watch for the adult doing tasks for the child rather than with them.",
  "SCHOOL AGE 6–12: the SNA sits beside the pupil; the pupil waits for the SNA to start, checks with the SNA rather than the teacher, and peers go through the SNA to reach the pupil.",
  "ADOLESCENT 13–16: adult proximity becomes stigmatising; the pupil may reject the SNA publicly or become more dependent. Care needs may continue but proximity should be adapted.",
  "YOUNG ADULT 17–26: personal assistants, disability supports in further/higher education; the principle of maximising independence remains.",
  "SPECIAL SETTING: higher staffing ratios; plan specifically for independence targets and for peer interaction without adult mediation.",
 ],
 "assess": [
  "Observation with a simple interval record: proximity of the SNA (beside / nearby / across the room), who initiates, who the pupil turns to for help, peer interactions with and without the SNA present.",
  "Ask the SNA and teacher separately: 'What does [pupil] do without support? What would happen if you stepped back for ten minutes?' Often both underestimate the pupil.",
  "Pupil interview: 'What does the SNA help you with? What could you do by yourself? How do you feel about having an SNA?'",
  "Review the care needs basis for the SNA allocation and whether the pupil's needs have changed.",
 ],
 "recommendations": [
  "CLARIFY ROLES: the class teacher plans and teaches; the SNA supports the pupil's care needs as set out in current Department of Education circulars. Recommend joint planning time between teacher and SNA where possible.",
  "PLAN INDEPENDENCE: set specific independence targets in the Student Support Plan (e.g., starts task without prompting, moves between classes alone) and plan how support will be faded.",
  "CHANGE PROXIMITY: the SNA positioned nearby rather than beside; supports the group rather than the individual where appropriate; steps back for peer interaction.",
  "PROMOTE PEER CONNECTION: create opportunities for peers to interact with the pupil directly, not through the adult.",
  "CONTINUUM LEVEL: School Support or School Support Plus depending on the level of need and agency involvement.",
  "DO NOT recommend removing or reducing SNA support without consultation with the school, parents and SENO. SNA allocation is decided by the NCSE/SENO process, not by the EP.",
 ],
 "explain_parent": [
  "'The SNA is doing a great job with her care needs. What we'd like to do now is help her do more things for herself, with the SNA stepping back bit by bit.'",
  "'This isn't about taking away support — it's about making sure the support helps her grow more independent.'",
 ],
 "explain_teacher": [
  "'He goes to the SNA for everything, including things you're teaching. Try asking him directly, and let the SNA sit a little further back during your input.'",
  "'Ten minutes of planning with the SNA each week would make a big difference — so she knows what the lesson's about and when to step back.'",
 ],
 "explain_child": [
  "YOUNGER: 'Your SNA helps you with some things. What things can you do all by yourself? Let's show everyone.'",
  "OLDER: 'Having an adult near you all the time can be helpful, and it can also be annoying. What do you want help with, and what would you rather do yourself?'",
  "ASK: 'If you could change one thing about how the SNA helps you, what would it be?'",
 ],
 "red_flags": [
  "WATCH — distress or regression when the SNA is absent: plan a known back-up and a gradual approach to independence.",
  "WATCH — the pupil being socially isolated from peers because the adult is always present: plan peer interaction.",
  "BOUNDARY — the EP does not decide SNA allocation. Recommendations about support levels go through the school and SENO.",
 ],
 "questions": [
  "Q: 'Will this mean we lose the SNA?' A: 'I don't make decisions about SNA allocation — that's the NCSE process through the SENO. What I'm suggesting is how the support is used, so it builds independence.'",
  "Q: 'Isn't more support always better?' A: 'Research suggests the way support is used matters more than how much there is (Webster et al., 2016). Close support all day can reduce independence and peer contact.'",
  "Q: 'The SNA knows him better than anyone — shouldn't she teach him?' A: 'Her knowledge is valuable, and the teacher should draw on it. But teaching stays with the teacher.'",
 ],
 "supervision": [
  "Bring an observation of SNA proximity and discuss how you feed it back without undermining the SNA.",
  "Check your understanding of the current SNA circular and scheme — it may have changed since you last looked.",
 ],
 "citations": [
  "Blatchford, P., Russell, A., & Webster, R. (2012). Reassessing the impact of teaching assistants: How research challenges practice and policy. Routledge.",
  "Department of Education and Skills. (2014). Circular 0030/2014: The Special Needs Assistant (SNA) scheme to support teachers in meeting the care needs of some children with special educational needs, arising from a disability. Department of Education and Skills.",
  "Giangreco, M. F., Edelman, S. W., Luiselli, T. E., & MacFarland, S. Z. C. (1997). Helping or hovering? Effects of instructional assistant proximity on students with disabilities. Exceptional Children, 64(1), 7–18.",
  "National Council for Special Education. (2018). Comprehensive review of the Special Needs Assistant scheme: A new school inclusion model to deliver the right supports at the right time to students with additional care needs. NCSE.",
  "Webster, R., Russell, A., & Blatchford, P. (2016). Maximising the impact of teaching assistants: Guidance for school leaders and teachers (2nd ed.). Routledge.",
 ],
})

# ---------------------------------------------------------------- 13
PRES.append({
 "name": "Help-seeking from adults",
 "neps": NEPS_42,
 "related_to": ["Social Anxiety Disorder (social phobia)", "Major Depressive Disorder", "Autism", "DLD", "Posttraumatic Stress Disorder (including Complex PTSD)"],
 "what_it_is": [
  "A description of whether, when and how a pupil asks adults for help — with schoolwork (academic help-seeking) and with personal or emotional difficulties (help-seeking for wellbeing or safety).",
  "Ryan et al. (2001) describe academic help-seeking as a self-regulated learning strategy; pupils AVOID seeking help when they fear looking incompetent, when the classroom emphasises ability comparison, or when they have low confidence.",
  "For emotional and mental health difficulties, young people commonly report barriers such as stigma, embarrassment, difficulty recognising symptoms and preferring self-reliance (Gulliver et al., 2010). Rickwood et al. (2005) describe help-seeking as a process: awareness, expression, availability of sources, and willingness to disclose.",
  "Part D places it under 4.2 because help-seeking depends on the relationship with the adult. Pupils seek help from adults they trust and who respond well.",
 ],
 "what_it_is_not": [
  "NOT the same as not needing help. Many pupils who never ask are struggling.",
  "NOT only a pupil skill. The classroom climate and the adult's response when asked shape whether the pupil asks again.",
  "NOT a diagnosis. Low help-seeking sits beside anxiety, low mood, language difficulty and past experiences of not being helped.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: seeking comfort and help from carers and staff; some children do not seek comfort when hurt, which is worth noting.",
  "SCHOOL AGE 6–12: hands up versus sitting stuck, copying peers, asking the same adult every time, not telling about bullying.",
  "ADOLESCENT 13–16: help-seeking for emotional difficulties falls as self-reliance rises; peers and online sources may be preferred. Guidance counsellors, year heads and tutors are the school routes.",
  "YOUNG ADULT 17–26: using college supports, GP and counselling services; many young adults do not seek help until crisis.",
  "SPECIAL SETTING: teach a help signal or symbol; ensure pupils with limited speech have a reliable way to ask for help and to tell about pain or distress.",
 ],
 "assess": [
  "Observe a task where help is likely to be needed: what does the pupil do when stuck? Who do they ask? What happens when they ask?",
  "Pupil interview: 'If you were stuck on work, what would you do? If you were upset or worried, who would you tell?' A pupil who names no one is a finding.",
  "Screen for anxiety and mood (RCADS, MFQ, Beck Youth Inventories-2) where emotional help-seeking is limited; check language comprehension where academic help-seeking is limited.",
  "Ask staff: 'When she does ask, how is it received?'",
 ],
 "recommendations": [
  "NORMALISE ASKING: teachers model asking for help, praise questions, and use routines where everyone asks (e.g., '3 before me', help cards, exit tickets) so asking is not exposing.",
  "PROVIDE PRIVATE ROUTES: a help card on the desk, a worry box, a named adult, the guidance counsellor. Make the route explicit and easy.",
  "RESPOND WELL: when the pupil asks, respond warmly and helpfully; a poor response teaches the pupil not to ask again.",
  "TEACH WHO TO ASK FOR WHAT: map out the adults and services for different needs (work, friendships, feeling unsafe) with the pupil.",
  "CONTINUUM LEVEL: Classroom Support for classroom routines; School Support for an individual plan; School Support Plus where mental health needs involve outside agencies.",
  "REFER via the family to Primary Care Psychology, Jigsaw or CAMHS where emotional difficulties are present and help-seeking is limited.",
 ],
 "explain_parent": [
  "'She tends not to ask for help, even when she's stuck. We want to make asking easier and safer for her.'",
  "'At home, noticing and praising when she does ask for something — even small things — helps.'",
  "'If she has something worrying her, she may find it easier to talk side by side — in the car, on a walk — than face to face. Let her know you'd rather hear it than not.'",
 ],
 "explain_teacher": [
  "'He won't put his hand up. A help card on the desk lets him ask without everyone seeing.'",
  "'When he asks, the first response matters. If it goes well, he'll ask again. If he's told \"you should have been listening\", he probably won't.'",
  "'Build asking into the lesson for everyone — a check-in at the desk during independent work — so he gets help without having to ask in front of the class.'",
 ],
 "explain_child": [
  "YOUNGER: 'When you're stuck, you can show this card and a teacher will come. Asking for help is what clever people do.'",
  "OLDER: 'Lots of people find it hard to ask for help. Who are the adults you could go to for different kinds of things?'",
  "ASK: 'What makes it hard to ask for help? What would make it easier?'",
 ],
 "red_flags": [
  "RED FLAG — a pupil who has no one to tell about worries and shows signs of distress, self-harm or abuse: same-day risk or child protection route; report to Tusla as soon as practicable.",
  "WATCH — a pupil who does not seek comfort when hurt or upset: consider early care history; discuss with the DLP if there are welfare concerns.",
  "BOUNDARY — help-seeking difficulties are described, not diagnosed. Screen for underlying needs and refer where appropriate.",
 ],
 "questions": [
  "Q: 'If she needs help, why doesn't she just ask?' A: 'Lots of pupils worry about looking stupid, or have been ignored before. We need to make asking easier and safer.'",
  "Q: 'He tells me everything is fine — should I believe him?' A: 'Listen, and also watch. Some young people say they're fine when they're not. A regular check-in helps.'",
  "Q: 'Where should teenagers go for help?' A: 'In school, a trusted teacher, year head or guidance counsellor. Outside, the GP, Jigsaw or other youth services. Check local services.'",
 ],
 "supervision": [
  "Bring a case where the pupil named no trusted adult and discuss how you built a route for help.",
  "Reflect on how accessible you are to pupils — do they feel able to ask you for help? What in your manner, timing or setting makes that easier or harder?",
 ],
 "citations": [
  "Gulliver, A., Griffiths, K. M., & Christensen, H. (2010). Perceived barriers and facilitators to mental health help-seeking in young people: A systematic review. BMC Psychiatry, 10, Article 113.",
  "Rickwood, D., Deane, F. P., Wilson, C. J., & Ciarrochi, J. (2005). Young people's help-seeking for mental health problems. Australian e-Journal for the Advancement of Mental Health, 4(3), 218–251.",
  "Ryan, A. M., Pintrich, P. R., & Midgley, C. (2001). Avoiding seeking help in the classroom: Who and why? Educational Psychology Review, 13(2), 93–114.",
 ],
})

# ---------------------------------------------------------------- 14
PRES.append({
 "name": "Uncorrected refractive error",
 "neps": NEPS_51,
 "related_to": ["Visual impairment", "Dyslexia", "ADHD", "DCD", "Specific Learning Disorder with impairment in written expression (dysgraphia)"],
 "what_it_is": [
  "A focusing problem of the eye — MYOPIA (short-sightedness: distance blurred), HYPEROPIA (long-sightedness: near work effortful or blurred), ASTIGMATISM (distortion at all distances) — that could be corrected with glasses but currently is not. Either it has not been detected, glasses were prescribed and are not worn, or the prescription is out of date.",
  "Part D's instruction is blunt: 'rule out before assessing literacy'. At School Age: 'Confirm date of last vision check before any literacy or non-verbal assessment.' An uncorrected child's scores on reading, copying, visual-perceptual and non-verbal reasoning tasks cannot be interpreted.",
  "Kulp et al. (2016, VIP-HIP study) found that preschool children with uncorrected moderate hyperopia scored lower on a test of early literacy than children without it. Hyperopia is easy to miss because distance vision (the eye chart on the wall) may be fine.",
  "The EP does not test vision. The EP's job is to ASK — when was the last eye test, is there a prescription, are glasses worn in class — and to hold the assessment until the answer is known.",
 ],
 "what_it_is_not": [
  "NOT dyslexia, and NOT a cause of dyslexia. The joint statement of the American Academy of Pediatrics and ophthalmology bodies (Handler et al., 2011) is clear that dyslexia is a language-based difficulty; vision problems can co-exist and must be corrected, but correcting them does not cure dyslexia.",
  "NOT ruled out by a school screening 'pass'. Screening tests usually check distance acuity and may miss hyperopia and astigmatism; they also happen only at set ages. Check current HSE school vision screening arrangements rather than assuming.",
  "NOT 'visual stress' or a need for coloured overlays. These are different, contested ideas (see 'Visual fatigue in extended reading').",
 ],
 "by_age": [
  "EARLY YEARS 0–5: children rarely complain — they assume everyone sees as they do. Watch for rubbing eyes, closing one eye, holding books very close, turning the head, avoiding puzzles and drawing. Part D: vision screening history, Public Health Nurse checks.",
  "SCHOOL AGE 6–12: myopia often emerges in these years: squinting at the board, copying errors from the board but not from a book, headaches after school. Hyperopia shows as avoidance of reading and poor sustained near work.",
  "ADOLESCENT 13–16: glasses are often prescribed but not worn because of appearance. Part D: exam access arrangements and the SEC RACE process may be relevant if visual needs persist after correction.",
  "YOUNG ADULT 17–26: out-of-date prescriptions and heavy screen use; access through adult optometry and college disability services (Part D: access technology and DSA-type evidence — check Irish equivalents).",
  "SPECIAL SETTING: refractive error is more common in some groups (for example, children with Down syndrome and cerebral palsy — check current sources) and harder to detect when the child cannot report. Environmental access audit (Part D).",
 ],
 "assess": [
  "ASK before any assessment: date of the last eye test (optometrist, ophthalmologist, school screening), result, whether glasses were prescribed, whether they are worn in class and at home, and whether they are brought to the assessment.",
  "Observe: distance copying versus near copying, head posture, squinting, eye rubbing, closeness to page. A marked difference between copying from the board and copying from the page is a clue.",
  "If there is ANY doubt, postpone literacy, visual-perceptual (Beery VMI) and non-verbal testing (WISC-V UK Visual Spatial and Fluid Reasoning, WNV, Leiter-3) until vision is checked, and record why.",
  "Where assessment must go ahead, report the limitation explicitly: 'Scores on visually presented tasks should be interpreted with caution; vision status unconfirmed.'",
 ],
 "recommendations": [
  "REFER FIRST: recommend an eye examination by an optometrist or via the GP / HSE community ophthalmic services before further literacy or cognitive assessment. Check current HSE eye services and school screening for the child's age.",
  "WEAR THE GLASSES: if glasses are prescribed, recommend a simple plan for wearing them in class — where they are kept, who reminds, how to handle teasing. A child with glasses in their bag is uncorrected.",
  "SEATING interim: near the board, facing it, with good lighting, until correction is in place.",
  "REVIEW: once corrected, re-observe reading and copying after several weeks before concluding that a literacy difficulty remains.",
  "CONTINUUM LEVEL: Classroom Support in most cases. School Support where a literacy difficulty remains after correction.",
  "DO NOT recommend coloured overlays or vision therapy as a treatment for reading difficulty. DO NOT report a literacy or non-verbal profile as valid when vision status is unknown.",
 ],
 "explain_parent": [
  "'Before I assess his reading, I need to know his eyes are seeing the page clearly. When was his last eye test?'",
  "'Some children are long-sighted — they can see the board fine but close work like reading is hard work. A school screening doesn't always pick that up, so a full eye test with an optometrist is worth doing.'",
  "'If he has glasses, can we make a plan so he wears them in school? A lot of children quietly take them off.'",
 ],
 "explain_teacher": [
  "'Does she copy well from a book but badly from the board? That's worth telling the parents — it might be her eyes.'",
  "'If he has glasses, please check he's wearing them. It sounds basic, but it's one of the commonest things we miss.'",
 ],
 "explain_child": [
  "YOUNGER: 'Your eyes are like cameras. Sometimes cameras need a special lens to make the picture sharp. Glasses are your special lens.'",
  "OLDER: 'Lots of people don't wear their glasses in school because of how they look. I get that. But if you can't see clearly, reading is much harder than it needs to be. What would make it easier to wear them?'",
  "ASK: 'Is the board blurry from your seat? Do your eyes get tired or sore when you read?'",
 ],
 "red_flags": [
  "RED FLAG — sudden loss or change in vision, double vision, a new squint, eye pain, or a white reflection in the pupil in photographs: urgent medical review via GP or emergency services the same day.",
  "WATCH — headaches with reading, frequent eye rubbing, closing one eye: refer for an eye examination.",
  "BOUNDARY — the EP does not test vision or advise on glasses or eye treatment. Ask, observe, refer, and delay assessment where needed.",
 ],
 "questions": [
  "Q: 'She passed the school eye test — isn't that enough?' A: 'School screening mostly checks distance vision at certain ages. Long-sightedness or astigmatism can be missed. A full eye test is the only way to be sure.'",
  "Q: 'Will glasses fix his reading?' A: 'If his eyes are the problem, glasses will help. If there's a reading difficulty as well, it'll still be there, but now we can see it clearly.'",
  "Q: 'Can you not just assess her and we'll sort the eyes later?' A: 'I could, but the results might be wrong. It's better to wait a few weeks and get a result we can trust.'",
 ],
 "supervision": [
  "Bring a case where vision status was unclear and discuss how you decided whether to go ahead with assessment.",
  "Check your report template: does it have a line confirming vision and hearing status before cognitive or literacy results?",
 ],
 "citations": [
  "Handler, S. M., Fierson, W. M., Section on Ophthalmology, Council on Children with Disabilities, American Academy of Ophthalmology, American Association for Pediatric Ophthalmology and Strabismus, & American Association of Certified Orthoptists. (2011). Learning disabilities, dyslexia, and vision. Pediatrics, 127(3), e818–e856.",
  "Kulp, M. T., Ciner, E., Maguire, M., Moore, B., Pentimonti, J., Pistilli, M., Cyert, L., Candy, T. R., Quinn, G., & Ying, G.-S. (2016). Uncorrected hyperopia and preschool early literacy: Results of the Vision in Preschoolers–Hyperopia in Preschoolers (VIP-HIP) study. Ophthalmology, 123(4), 681–689.",
 ],
})

# ---------------------------------------------------------------- 15
PRES.append({
 "name": "Visual fatigue in extended reading",
 "neps": NEPS_51,
 "related_to": ["Visual impairment", "Dyslexia", "ADHD", "Acquired brain injury", "Migraine"],
 "what_it_is": [
  "A description of a pupil whose reading or near work deteriorates over time — accurate at first, then slower, more errors, losing place, rubbing eyes, complaining of blur, headache or tiredness. The key feature is DECLINE WITH DURATION, not difficulty from the first line.",
  "Possible visual contributors include uncorrected hyperopia, accommodative difficulties (focusing at near) and convergence insufficiency (difficulty keeping both eyes aligned at near). The Convergence Insufficiency Treatment Trial (CITT Study Group, 2008) showed that convergence insufficiency is a recognised condition with treatment options — but diagnosis is by an optometrist or orthoptist.",
  "Digital eye strain (Sheppard & Wolffsohn, 2018) describes eye discomfort and fatigue with prolonged screen use; it is relevant as more reading moves to devices.",
  "'Visual stress' (Meares-Irlen syndrome) is a contested concept. Griffiths et al. (2016) reviewed the evidence for coloured overlays and lenses and found it weak; the Handler et al. (2011) statement does not support them for dyslexia. Describe the fatigue; do not attribute it to visual stress.",
 ],
 "what_it_is_not": [
  "NOT dyslexia. A pupil with dyslexia may also tire with reading, but the difficulty is in decoding from the start. Visual fatigue affects a reader who decodes adequately but cannot sustain it.",
  "NOT laziness or loss of motivation, though it can look like both. The pupil who stops after ten minutes may simply be uncomfortable.",
  "NOT something the EP diagnoses. The EP describes the pattern and refers for an eye examination.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: rarely relevant; sustained near work is limited. Avoidance of close tasks is the nearest sign.",
  "SCHOOL AGE 6–12: emerges as reading demands grow (longer texts in 3rd–6th class). Reading aloud declines across a page; the child rubs eyes or complains of headache.",
  "ADOLESCENT 13–16: long exam papers, extended reading across many subjects, screen use. Performance declines in later questions; RACE accommodations may be relevant if needs persist after correction.",
  "YOUNG ADULT 17–26: long reading lists, screen-based study, work. Adult optometry, access technology, and college disability services.",
  "SPECIAL SETTING: pupils with neurological conditions (e.g., after brain injury) may have visual fatigue and cannot always report it; watch behaviour change during visual tasks.",
 ],
 "assess": [
  "Timed observation of reading: note accuracy and fluency at the start versus after 5–10 minutes; note eye rubbing, blinking, moving closer, losing place.",
  "Compare short and long texts on reading measures (e.g., Neale Analysis or YARC passages) — a decline across longer passages is a clue, not a diagnosis.",
  "Ask the pupil: 'What happens to your eyes or the words after you've been reading for a while?' Symptoms such as words moving or doubling should be reported to an optometrist.",
  "Confirm vision status (last eye test, prescription, wearing glasses) as for uncorrected refractive error.",
 ],
 "recommendations": [
  "REFER for a full eye examination (optometrist or via GP / HSE eye services), mentioning the symptoms of fatigue with near work. Check local services.",
  "BUILD IN BREAKS: short reading blocks with brief breaks (look into the distance, move around).",
  "REDUCE UNNECESSARY LOAD: larger or clearer print, well-spaced text, good lighting, and reducing glare on screens and whiteboards.",
  "USE ALTERNATIVES for long texts where appropriate: audio versions, text-to-speech, reader.",
  "CONTINUUM LEVEL: Classroom Support; School Support where a plan is needed, or RACE application where needs persist after correction (check current SEC guidance).",
  "DO NOT recommend coloured overlays or tinted lenses as a reading intervention (Griffiths et al., 2016). If a family uses them, record it without endorsing.",
 ],
 "explain_parent": [
  "'He reads well at first, and then it gets harder as he goes on. That makes me wonder whether his eyes are getting tired. I'd like an optometrist to check how his eyes work together at close distance.'",
  "'Coloured overlays are sometimes suggested. The research on them isn't strong, so I'd get a full eye exam first.'",
 ],
 "explain_teacher": [
  "'Watch what happens after ten minutes of reading — does she slow down, lose her place, rub her eyes? That pattern is worth noting.'",
  "'Short reading blocks and good print make a real difference while we get her eyes checked.'",
 ],
 "explain_child": [
  "YOUNGER: 'Do your eyes feel tired or sore when you read for a long time? Do the words ever look blurry or move?'",
  "OLDER: 'Reading for a long time can be tiring for your eyes. If the words get blurry or double, or you get headaches, that's worth telling someone — it might be fixable.'",
 ],
 "red_flags": [
  "RED FLAG — sudden onset of double vision, severe headaches, or visual change: urgent medical review the same day.",
  "WATCH — persistent headaches with reading, frequent eye rubbing, closing one eye: refer for eye examination.",
  "BOUNDARY — the EP does not diagnose visual conditions or recommend vision therapy. Describe, refer.",
 ],
 "questions": [
  "Q: 'Will coloured overlays help?' A: 'Some children say they prefer them, but the research evidence isn't strong (Griffiths et al., 2016). An eye examination is the first step.'",
  "Q: 'Is this dyslexia?' A: 'Dyslexia is about decoding words. What I'm seeing is reading that starts well and gets worse — that's more like tiredness. They can happen together, so we'll look at both.'",
  "Q: 'Can screens cause it?' A: 'Long screen use can cause eye strain (Sheppard & Wolffsohn, 2018). Breaks help.'",
 ],
 "supervision": [
  "Bring a reading assessment where performance declined across passages and discuss how you interpreted it.",
  "Discuss how to respond when a family has been advised to use coloured overlays by another professional — respectful, evidence-based, and within your role.",
 ],
 "citations": [
  "Convergence Insufficiency Treatment Trial Study Group. (2008). Randomized clinical trial of treatments for symptomatic convergence insufficiency in children. Archives of Ophthalmology, 126(10), 1336–1349.",
  "Griffiths, P. G., Taylor, R. H., Henderson, L. M., & Barrett, B. T. (2016). The effect of coloured overlays and lenses on reading: A systematic review of the literature. Ophthalmic and Physiological Optics, 36(5), 519–544.",
  "Handler, S. M., Fierson, W. M., Section on Ophthalmology, Council on Children with Disabilities, American Academy of Ophthalmology, American Association for Pediatric Ophthalmology and Strabismus, & American Association of Certified Orthoptists. (2011). Learning disabilities, dyslexia, and vision. Pediatrics, 127(3), e818–e856.",
  "Sheppard, A. L., & Wolffsohn, J. S. (2018). Digital eye strain: Prevalence, measurement and amelioration. BMJ Open Ophthalmology, 3(1), Article e000146.",
 ],
})

# ---------------------------------------------------------------- 16
PRES.append({
 "name": "Access to print",
 "neps": NEPS_51,
 "related_to": ["Visual impairment", "Dyslexia", "Physical disability", "Cerebral palsy", "Acquired brain injury"],
 "what_it_is": [
  "Part D's full title: 'Access to print — font, size, contrast, position in room.' It describes whether a pupil can physically SEE and USE the printed and displayed material of the classroom — worksheets, textbooks, whiteboards, screens, exam papers — regardless of reading ability.",
  "Print access depends on the pupil's vision (acuity, visual field, contrast sensitivity), the MATERIAL (font, size, spacing, contrast, layout, glare) and the ENVIRONMENT (distance, angle, lighting). Legge (2007) describes a 'critical print size' below which reading speed drops sharply — larger print helps up to a point, and then gives no further benefit.",
  "For pupils with a diagnosed visual impairment, the Visiting Teacher Service for children with visual impairment (Department of Education) advises on print access, modified materials and technology — Part D lists 'Visiting Teacher involvement' as a School Age action. Check current service arrangements.",
  "Access to print is also relevant for pupils without visual impairment — dense worksheets, low-contrast photocopies and cluttered layouts disadvantage pupils with dyslexia, attention difficulties and processing difficulties.",
 ],
 "what_it_is_not": [
  "NOT a reading intervention. Making print accessible removes a barrier; it does not teach reading.",
  "NOT simply 'bigger is better'. Enlarging beyond what the pupil needs can reduce the amount visible at once and slow reading; the right size is individual and should be advised by the Visiting Teacher or optometrist.",
  "NOT a diagnosis. It is a description of the fit between the pupil and the materials.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: picture books, displays and environmental print; high contrast, uncluttered images, position relative to light.",
  "SCHOOL AGE 6–12: worksheets, textbooks, board work. Photocopies of photocopies lose contrast; small font in maths workbooks; board position and glare.",
  "ADOLESCENT 13–16: dense subject textbooks, exam papers, diagrams, maps. RACE accommodations may include modified or enlarged papers — check current SEC guidance.",
  "YOUNG ADULT 17–26: digital texts, lecture slides, online materials; access technology (screen readers, magnification). Disability services in further/higher education.",
  "SPECIAL SETTING: environmental access audit (Part D): lighting, contrast, clutter, signage, tactile and symbol support.",
 ],
 "assess": [
  "Confirm vision status and any diagnosis first (eye report, Visiting Teacher reports). The EP does not assess visual function.",
  "Observe the pupil with real classroom materials: position, distance, head posture, time taken to find information on the page, errors of misreading.",
  "Try simple adjustments in session: larger font, clearer layout, better lighting, a tablet with zoom. Note what changes performance.",
  "Ask the pupil: 'What makes things easier or harder to see? Where do you like to sit?'",
 ],
 "recommendations": [
  "INVOLVE THE VISITING TEACHER (for pupils with diagnosed visual impairment) for advice on print size, format and technology. Referral routes: check current Department of Education arrangements.",
  "IMPROVE MATERIALS for all: clear sans-serif font, adequate size and spacing, high contrast (black on white or cream), uncluttered layout, original rather than photocopied copies.",
  "POSITION AND LIGHTING: seat the pupil where they can see the board and teacher clearly, avoiding glare and facing away from windows; provide personal copies of board work.",
  "TECHNOLOGY: tablets with zoom, text-to-speech, digital texts; check eligibility for the Department of Education's assistive technology scheme (check current circular).",
  "CONTINUUM LEVEL: Classroom Support for general material adjustments; School Support or School Support Plus for pupils with visual impairment, with Visiting Teacher involvement.",
  "DO NOT recommend specific print sizes or optical aids yourself. That is for the Visiting Teacher, optometrist or ophthalmologist.",
 ],
 "explain_parent": [
  "'The school is going to look at how materials are presented to her — size, spacing, contrast — so she can see them easily. That takes away one barrier to learning.'",
  "'The Visiting Teacher can advise on exactly what size and format suits her eyes.'",
 ],
 "explain_teacher": [
  "'Could you give him his own copy of what's on the board, and make sure worksheets are originals, not photocopies of photocopies?'",
  "'Clear, well-spaced print helps him, and probably helps half the class too.'",
 ],
 "explain_child": [
  "YOUNGER: 'Is it easy to see the board from your seat? Where would be the best place for you to sit?'",
  "OLDER: 'What kind of print or screen makes reading easiest for you? You're the one who knows.'",
 ],
 "red_flags": [
  "WATCH — a pupil who struggles with print despite adjustments: may need a (re)assessment of vision; refer via parents to optometry or ophthalmology.",
  "WATCH — changes in visual function in pupils with known eye conditions: medical review.",
  "BOUNDARY — the EP describes access needs; the Visiting Teacher and eye specialists advise on specific formats and aids.",
 ],
 "questions": [
  "Q: 'Should we just enlarge everything to A3?' A: 'Sometimes that helps, but not always — too big can be harder. The Visiting Teacher can advise the right size for her.'",
  "Q: 'Does this help other children?' A: 'Often, yes. Clear, uncluttered, well-spaced print is easier for everyone.'",
  "Q: 'Can he use a tablet in class?' A: 'Possibly — zoom and text-to-speech can help. The school can check eligibility under the assistive technology scheme.'",
 ],
 "supervision": [
  "Bring a case of a pupil with visual impairment and discuss how you worked with the Visiting Teacher.",
  "Reflect on your own assessment materials — are they accessible to pupils with visual difficulties?",
 ],
 "citations": [
  "Handler, S. M., Fierson, W. M., Section on Ophthalmology, Council on Children with Disabilities, American Academy of Ophthalmology, American Association for Pediatric Ophthalmology and Strabismus, & American Association of Certified Orthoptists. (2011). Learning disabilities, dyslexia, and vision. Pediatrics, 127(3), e818–e856.",
  "Legge, G. E. (2007). Psychophysics of reading in normal and low vision. Lawrence Erlbaum Associates.",
 ],
})

# ---------------------------------------------------------------- 17
PRES.append({
 "name": "Listening in noise vs listening one-to-one",
 "neps": NEPS_52,
 "related_to": ["Hearing impairment", "Recurrent otitis media with effusion (glue ear)", "DLD", "ADHD", "Autism", "Auditory processing disorder"],
 "what_it_is": [
  "A pupil who understands well in a quiet one-to-one setting (including your assessment room) but struggles in the classroom, yard or canteen. The CONTRAST between settings is the finding — and it means your quiet-room assessment may underestimate their classroom difficulty.",
  "Classrooms are noisy and reverberant. Children need a better signal-to-noise ratio than adults to understand speech, and children with hearing loss, language difficulties, attention difficulties or learning in an additional language need it more still (Crandell & Smaldino, 2000; Klatte et al., 2013).",
  "Even mild or unilateral hearing loss can make listening in noise effortful. Bess et al. (1998) found children with minimal sensorineural hearing loss had higher rates of grade retention and lower functional scores than peers — check the study for detail before quoting.",
  "Auditory processing disorder (APD) is a contested diagnosis made by audiologists. The British Society of Audiology (2018) position statement describes APD and recommends a broad, multidisciplinary approach; check current guidance.",
 ],
 "what_it_is_not": [
  "NOT 'selective listening' or not paying attention. The pupil may be trying hard and still losing much of what is said.",
  "NOT ruled out by a normal hearing screen in infancy or by a 'normal' audiogram. Hearing can change (glue ear fluctuates), and difficulty in noise can occur with normal hearing thresholds.",
  "NOT a diagnosis of APD. Only audiology can assess and diagnose APD, and the EP should not suggest it without an audiology referral.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: noisy preschool rooms; child seems not to respond to name or instructions in group but responds one-to-one. Glue ear is common at this age — ask about ear infections.",
  "SCHOOL AGE 6–12: misunderstands instructions in class but does fine in the resource room; tired after school; watches peers before starting. Part D: confirm audiology status before assessing language or literacy.",
  "ADOLESCENT 13–16: many classrooms, practical subjects with machinery noise, group discussion. Part D: audiology status, FM (remote microphone) system use, acoustics.",
  "YOUNG ADULT 17–26: lecture halls, group work, workplaces. Access technology and course arrangements (Part D).",
  "SPECIAL SETTING: many pupils have sensory needs, hearing loss or communication difficulties. Acoustic environment and total communication approaches (Part D).",
 ],
 "assess": [
  "CONFIRM AUDIOLOGY STATUS FIRST (Part D): date and result of the last hearing test; history of glue ear or grommets; any hearing aids or remote microphone system and whether they are used.",
  "Observe in the classroom at a noisy time and in a quiet setting: compare response to instructions, need for repetition, watching peers, fatigue.",
  "Ask teacher and parent: 'Is there a difference between how he understands one-to-one and in a group? At home in a quiet room versus at a family gathering?'",
  "When reporting language or verbal cognitive scores from a quiet room, state explicitly that performance in noise may be lower. Consider DLD (CELF-5 UK or SLT), attention (ADHD) and EAL as contributors.",
 ],
 "recommendations": [
  "REFER to audiology via the GP (or the HSE school/community audiology route) if hearing has not been tested recently or if listening in noise is a concern. Check local pathways.",
  "REDUCE NOISE AND IMPROVE THE SIGNAL: seat near the teacher, away from noise sources; reduce background noise (soft furnishings, closing doors, turning off projector fans); face the pupil when speaking.",
  "SUPPORT WITH VISUALS: written instructions, key words on the board, visual timetable, so meaning does not depend only on hearing.",
  "CHECK UNDERSTANDING: ask the pupil to repeat back key instructions; give a quiet check-in after whole-class input.",
  "CONTINUUM LEVEL: Classroom Support for acoustics and seating; School Support where a plan is needed; Visiting Teacher involvement where there is a diagnosed hearing loss.",
  "DO NOT suggest a diagnosis of APD or recommend remote microphone systems yourself — these come from audiology and the Visiting Teacher.",
 ],
 "explain_parent": [
  "'In my quiet room he understood everything. In a busy classroom, it's much harder for him to pick out the teacher's voice. I'd like his hearing checked properly.'",
  "'Even small or temporary hearing problems, like glue ear, can make noisy rooms really hard.'",
 ],
 "explain_teacher": [
  "'She understands one-to-one but loses a lot in the noise of the classroom. Seating her near you and facing her when you talk will help.'",
  "'Written instructions on the board mean she's not relying only on what she hears.'",
 ],
 "explain_child": [
  "YOUNGER: 'Is it easy or hard to hear the teacher when the class is noisy? What helps?'",
  "OLDER: 'Lots of people find it hard to follow in noisy rooms. It's not your fault. Where do you hear best? What would help?'",
 ],
 "red_flags": [
  "RED FLAG — sudden hearing loss, ear pain with discharge, or a change in hearing: urgent medical review via GP the same day.",
  "WATCH — a child who is increasingly withdrawn, tired or frustrated in noisy settings: may reflect listening fatigue and hearing difficulty.",
  "BOUNDARY — the EP does not test hearing or diagnose APD. Ask, observe, refer, and interpret results with caution.",
 ],
 "questions": [
  "Q: 'He hears fine at home — why would he have a problem in class?' A: 'At home it's usually quieter and people face him. In class there's a lot of background noise. Hearing in noise is much harder, especially for children.'",
  "Q: 'Does she have auditory processing disorder?' A: 'That's something only audiology can assess. What I can say is she finds listening in noise hard, and there are clear things the class can do to help.'",
  "Q: 'Can a microphone system help?' A: 'For some children, yes. That's a decision for audiology and the Visiting Teacher.'",
 ],
 "supervision": [
  "Bring an assessment where you worried quiet-room scores overestimated classroom functioning and discuss how you reported it.",
  "Check your pre-assessment routine: do you confirm hearing status before language or literacy testing every time?",
 ],
 "citations": [
  "Bess, F. H., Dodd-Murphy, J., & Parker, R. A. (1998). Children with minimal sensorineural hearing loss: Prevalence, educational performance, and functional status. Ear and Hearing, 19(5), 339–354.",
  "British Society of Audiology. (2018). Position statement and practice guidance: Auditory processing disorder (APD). BSA.",
  "Crandell, C. C., & Smaldino, J. J. (2000). Classroom acoustics for children with normal hearing and with hearing impairment. Language, Speech, and Hearing Services in Schools, 31(4), 362–370.",
  "Klatte, M., Bergström, K., & Lachmann, T. (2013). Does noise affect learning? A short review on noise effects on cognitive performance in children. Frontiers in Psychology, 4, Article 578.",
 ],
})

# ---------------------------------------------------------------- 18
PRES.append({
 "name": "Classroom acoustics and seating",
 "neps": NEPS_52,
 "related_to": ["Hearing impairment", "Recurrent otitis media with effusion (glue ear)", "DLD", "ADHD", "Autism"],
 "what_it_is": [
  "A description of the LISTENING ENVIRONMENT — background noise, reverberation (echo), distance from the speaker, and the pupil's seat — and its effect on a pupil's access to spoken teaching. It is a systemic presentation: the target of change is the room, not only the child.",
  "Shield and Dockrell (2008) found that higher levels of environmental and classroom noise were associated with lower attainment in primary school children in London; Dockrell and Shield (2006) showed that noise affected performance on verbal tasks, and more so for children with special educational needs.",
  "Standards for classroom acoustics set limits on background noise and reverberation (e.g., ANSI/ASA S12.60 in the US). In Ireland, the Department of Education publishes technical guidance on the acoustic design of schools (Technical Guidance Document — check the current document and version). Older buildings, prefabs and open-plan areas may fall well short.",
  "Seating is the cheapest intervention: distance from the teacher, face visibility for lip-reading, and distance from noise sources (corridor doors, projector fans, heaters, windows onto a road or yard).",
 ],
 "what_it_is_not": [
  "NOT only relevant to pupils with hearing loss. Noise affects all children, and especially those with language difficulties, attention difficulties, EAL and autism (Klatte et al., 2013).",
  "NOT solved by 'sitting at the front' alone. The front row can be close to a noisy projector or whiteboard; the best seat depends on the room.",
  "NOT the EP's job to measure acoustics. The EP notices, describes and recommends; acoustic measurement is for the relevant engineers or the Visiting Teacher/audiology.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: noisy play rooms, hard floors, lots of voices. Adults' voices compete with play noise; small groups and quiet corners help.",
  "SCHOOL AGE 6–12: large classes, hard surfaces, open windows, prefabs. Seat choices, group work noise and whole-class instruction matter most.",
  "ADOLESCENT 13–16: moving between rooms with different acoustics — labs, workshops, PE halls, canteens. Pupils may choose seats for social reasons that are acoustically poor.",
  "YOUNG ADULT 17–26: lecture halls, open-plan workplaces. Self-advocacy about seating and remote microphone use becomes important.",
  "SPECIAL SETTING: many pupils have hearing, sensory or communication needs; acoustic treatment and quiet spaces are especially important (Part D: acoustic environment and total communication).",
 ],
 "assess": [
  "Walk the room at a working time: note noise sources (heaters, fans, corridor, yard, road), hard surfaces, the pupil's seat relative to the teacher and noise sources, and lighting on the teacher's face.",
  "Observe the pupil in different seats or rooms if possible: does their response change?",
  "Ask the teacher: 'Where does the noise come from in this room? When is it worst?' Ask the pupil: 'Where do you hear best?'",
  "Confirm hearing status and any audiology/Visiting Teacher advice on seating and remote microphone systems.",
 ],
 "recommendations": [
  "SEATING: near the main teaching position, with a clear view of the teacher's face, away from noise sources (doors, windows, heaters, projectors). Flexible seating when the teaching position moves.",
  "REDUCE NOISE: soft furnishings, felt pads on chair legs, closing doors and windows during instruction, switching off noisy equipment, clear class routines for noise levels.",
  "TEACHER PRACTICE: face the class when speaking; avoid talking while writing on the board; repeat pupils' answers so everyone hears; use visual supports.",
  "SYSTEMIC: raise acoustic concerns with school management; where a pupil has hearing loss, the Visiting Teacher can advise on acoustics and remote microphone systems. Check Department of Education technical guidance for building works.",
  "CONTINUUM LEVEL: Classroom Support (whole-class benefit); School Support where a pupil needs an individual plan; Visiting Teacher involvement for diagnosed hearing loss.",
  "DO NOT assume a soundfield system is the answer without advice; evidence and suitability vary — check current guidance and the Visiting Teacher's view.",
 ],
 "explain_parent": [
  "'The classroom is quite noisy — that's common. We're going to look at where he sits and how noise can be reduced, so he can hear the teacher more easily.'",
  "'These changes help lots of children, not just him.'",
 ],
 "explain_teacher": [
  "'Her seat is right beside the door and the radiator. Could she move nearer to where you usually teach, facing you?'",
  "'Try not to talk while writing on the board — she needs to see your face.'",
  "'Felt pads on chair legs sound small, but they cut a lot of noise.'",
 ],
 "explain_child": [
  "YOUNGER: 'Where in the classroom can you hear the teacher best? Where is it noisiest?'",
  "OLDER: 'Some seats are better for hearing than others. Where would you choose, if it was just about hearing?'",
 ],
 "red_flags": [
  "WATCH — a pupil whose performance drops in particular rooms (prefabs, labs): consider acoustics and hearing.",
  "WATCH — a pupil with known hearing loss not using prescribed devices: explore why (discomfort, embarrassment, device faults) and involve the Visiting Teacher.",
  "BOUNDARY — the EP does not measure acoustics or prescribe equipment; describe and recommend advice from the right people.",
 ],
 "questions": [
  "Q: 'Can we not just put him at the front?' A: 'The front helps if it's away from noise and he can see your face. Sometimes the front is next to the noisiest thing in the room.'",
  "Q: 'Is it worth changing the room for one child?' A: 'Quieter rooms help every child's learning (Shield & Dockrell, 2008), so it's rarely just for one.'",
  "Q: 'What about a soundfield system?' A: 'Some schools use them. Whether it's right here depends on the room and the pupil — the Visiting Teacher or audiology can advise.'",
 ],
 "supervision": [
  "Bring a classroom sketch with noise sources and seating, and discuss how you presented acoustic issues to school management.",
  "Reflect on systemic recommendations: how do you recommend environmental change without seeming to criticise the teacher?",
 ],
 "citations": [
  "Dockrell, J. E., & Shield, B. M. (2006). Acoustical barriers in classrooms: The impact of noise on performance in the classroom. British Educational Research Journal, 32(3), 509–525.",
  "Klatte, M., Bergström, K., & Lachmann, T. (2013). Does noise affect learning? A short review on noise effects on cognitive performance in children. Frontiers in Psychology, 4, Article 578.",
  "Shield, B. M., & Dockrell, J. E. (2008). The effects of environmental and classroom noise on the academic attainments of primary school children. The Journal of the Acoustical Society of America, 123(1), 133–144.",
 ],
})

# ---------------------------------------------------------------- 19
PRES.append({
 "name": "Hearing history during the years phonics was taught",
 "neps": NEPS_52,
 "related_to": ["Recurrent otitis media with effusion (glue ear)", "Hearing impairment", "Dyslexia", "DLD", "Speech Sound Disorder"],
 "what_it_is": [
  "A HISTORY question, not a current presentation: did the pupil have fluctuating or reduced hearing — most often glue ear (otitis media with effusion) — during the years when phonics and phonological awareness were taught (typically Junior and Senior Infants and 1st class)? Part D: 'glue ear at 5 shows up at 8'.",
  "The hypothesis: if a child could not hear speech sounds reliably when letter–sound links were being taught, gaps in phonological awareness and phonics may persist after hearing recovers, appearing later as reading or spelling difficulty. Part D (School Age, 5.2): 'a history of glue ear during infant classes is a live hypothesis for literacy difficulty.'",
  "The evidence is MIXED. Roberts et al. (2004) meta-analysed prospective studies and found little or no association between otitis media and later speech and language outcomes overall. Some children are affected; many are not. Treat it as a hypothesis to test, not a conclusion.",
  "NICE (2008) guidance on OME in children under 12 recommends active observation for a period and, where hearing loss persists, consideration of grommets or hearing aids; the Rosenfeld et al. (2016) clinical guideline gives the US view. Management is a medical decision — check current guidance.",
 ],
 "what_it_is_not": [
  "NOT a diagnosis and NOT an explanation that rules out dyslexia. A child can have both a glue ear history and dyslexia.",
  "NOT relevant only if hearing is poor now. The point is that past hearing may explain present gaps even if current hearing is normal.",
  "NOT a reason to delay literacy support. Whatever the cause, the phonics gap should be taught.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: glue ear is common in early childhood; watch for inattention to speech, loud TV, speech sound errors. Part D: newborn screening and PHN records, glue ear history.",
  "SCHOOL AGE 6–12: the core band. Reading and spelling difficulty with weak phonological awareness in a child with a history of ear infections, grommets, or hearing problems in infants.",
  "ADOLESCENT 13–16: history is harder to recover; ask parents directly and check any available records. Spelling may still show gaps.",
  "YOUNG ADULT 17–26: retrospective only; relevant for understanding a literacy profile in an adult assessment.",
  "SPECIAL SETTING: glue ear is more common in some groups (e.g., children with Down syndrome, cleft palate — check current sources); hearing should be reviewed regularly.",
 ],
 "assess": [
  "Take a careful HEARING HISTORY with parents: ear infections, grommets, audiology appointments, times when the child seemed not to hear, and when these occurred relative to school years.",
  "Check current hearing status (audiology) before assessing language or literacy (Part D).",
  "Assess phonological awareness and phonics directly (PhAB2, relevant WIAT-III UK subtests, DASH for spelling where relevant) and look for specific sound confusions.",
  "Formulate cautiously: 'A history of glue ear during the infant years may have contributed to gaps in phonological knowledge; this is one hypothesis alongside others.'",
 ],
 "recommendations": [
  "TEACH THE GAP: systematic, explicit phonics and phonological awareness teaching targeted at the specific gaps found, regardless of cause.",
  "REFER to audiology via GP if current hearing has not been checked recently or if there are ongoing concerns.",
  "RECORD THE HISTORY in the Student Support File so future assessments consider it.",
  "SUPPORT LISTENING: good acoustics and seating if hearing fluctuates (see Classroom acoustics and seating).",
  "CONTINUUM LEVEL: Classroom Support to School Support for targeted literacy intervention; review progress after a defined period.",
  "DO NOT attribute a literacy difficulty solely to past glue ear, and do not rule out dyslexia on that basis.",
 ],
 "explain_parent": [
  "'You mentioned he had lots of ear infections around the time he started school. That's exactly when children learn the sounds letters make. If he wasn't hearing clearly then, he may have missed some of it.'",
  "'It doesn't mean something is wrong now, and it doesn't rule out other things. It means we teach the sounds he's missing, directly.'",
 ],
 "explain_teacher": [
  "'She had glue ear in infants. Some of her spelling errors look like sounds she never learned clearly. Direct phonics teaching on those sounds should help.'",
  "'Make sure her hearing has been checked recently — glue ear can come back.'",
 ],
 "explain_child": [
  "YOUNGER: 'When you were small, your ears had some gunk in them that made sounds fuzzy. Now we're going to practise the sounds you might have missed.'",
  "OLDER: 'You might have missed some sounds when you were learning to read because of ear problems. That's not your fault — and it's something we can fill in now.'",
 ],
 "red_flags": [
  "WATCH — ongoing hearing problems, ear pain or discharge: refer via GP.",
  "WATCH — literacy difficulty that does not respond to targeted teaching: consider dyslexia and other factors; do not stop at the glue ear hypothesis.",
  "BOUNDARY — the EP takes the history and forms a hypothesis; diagnosis and management of ear conditions sit with GP, audiology and ENT.",
 ],
 "questions": [
  "Q: 'Did glue ear cause his reading problems?' A: 'It might have contributed. Research is mixed (Roberts et al., 2004). What matters is we teach the sounds he's missing now.'",
  "Q: 'His hearing is fine now — why does it matter?' A: 'Because the gap from back then can still be there. Knowing the history helps us understand it.'",
  "Q: 'Could it be dyslexia instead?' A: 'It could be, or both. We'll see how he responds to targeted teaching.'",
 ],
 "supervision": [
  "Bring a case where hearing history formed part of your formulation and discuss how you weighed it against other explanations.",
  "Check your background interview template: does it ask about ear infections and hearing in the infant years?",
 ],
 "citations": [
  "National Institute for Health and Care Excellence. (2008). Otitis media with effusion in under 12s: Surgery (Clinical guideline CG60). NICE.",
  "Roberts, J. E., Rosenfeld, R. M., & Zeisel, S. A. (2004). Otitis media and speech and language: A meta-analysis of prospective studies. Pediatrics, 113(3), e238–e248.",
  "Rosenfeld, R. M., Shin, J. J., Schwartz, S. R., Coggins, R., Gagnon, L., Hackell, J. M., Hoelting, D., Hunter, L. L., Kummer, A. W., Payne, S. C., Poe, D. S., Veling, M., Vila, P. M., Walsh, S. A., & Corrigan, M. D. (2016). Clinical practice guideline: Otitis media with effusion (update). Otolaryngology–Head and Neck Surgery, 154(1 Suppl), S1–S41.",
 ],
})

# ---------------------------------------------------------------- 20
PRES.append({
 "name": "Physical disability (non-cerebral palsy)",
 "neps": NEPS_53,
 "related_to": ["Spina bifida", "Muscular dystrophy", "Acquired brain injury", "Cerebral palsy", "Genetic syndromes (Down, Fragile X, 22q11.2, Williams, Prader-Willi, Angelman, Rett)"],
 "what_it_is": [
  "An umbrella for physical disabilities OTHER than cerebral palsy that affect mobility, dexterity, stamina or physical access to school: limb difference, juvenile idiopathic arthritis, osteogenesis imperfecta, arthrogryposis, spinal cord injury, and others; spina bifida and muscular dystrophy are listed separately in Part D as diagnoses. Part D labels it 'Medical' — the condition is diagnosed and managed by paediatrics, orthopaedics, rheumatology, neurology and the CDNT.",
  "Part D (School Age, 5.3): 'Medical report with consent · impact on school day (fatigue, medication timing, absence) · your role is educational impact, not diagnosis.' The EP's question is: what does this condition mean for learning, participation, wellbeing and relationships in THIS school?",
  "The ICF-CY (WHO, 2007) frames disability as the interaction of body function, activity, participation and environment. Rosenbaum and Gorter (2012) translate this into the 'F-words' — function, family, fitness, fun, friends, future — a useful checklist for planning.",
  "Many pupils with physical disabilities have typical cognitive ability; others have associated learning, attention or processing needs (some conditions, e.g., spina bifida with hydrocephalus, have known cognitive profiles — check condition-specific sources). Do not assume either way.",
 ],
 "what_it_is_not": [
  "NOT a cognitive or learning difficulty by default. Physical and cognitive abilities are separate; low expectations are one of the biggest barriers.",
  "NOT the EP's to diagnose or manage. Medical, physiotherapy and OT input come from the relevant services.",
  "NOT only about access to buildings. Participation in PE, yard, trips, friendships and identity matter as much.",
 ],
 "by_age": [
  "EARLY YEARS 0–5: CDNT involvement is common; access to preschool (AIM supports may apply), play participation, early independence skills. Part D: medical history from parent and PHN, developmental history.",
  "SCHOOL AGE 6–12: physical access, fine motor for writing, PE participation, fatigue, absences for appointments or surgery, SNA care support. Friendships and yard inclusion.",
  "ADOLESCENT 13–16: identity, body image, independence, peer relationships and sometimes progressive conditions. Part D: medical report, exam accommodations (RACE), subject choices.",
  "YOUNG ADULT 17–26: transition from paediatric to adult services, further/higher education disability supports, independent living. Part D: adult services, course accommodations.",
  "SPECIAL SETTING: care plans, nursing support, therapy integration, adaptive equipment (Part D). Adaptive functioning measures (Vineland-3 / ABAS-3) may be used in place of or alongside standard tests.",
 ],
 "assess": [
  "Obtain medical, OT and physiotherapy reports with consent: diagnosis, functional implications, fatigue, medication, prognosis (stable or progressive), and any cognitive implications named by the medical team.",
  "Observe participation across the day: classroom, transitions, yard, PE, toileting and lunch. Note where the pupil is included, excluded, or dependent.",
  "Choose assessment tools that minimise motor demands where cognitive assessment is needed (e.g., avoid timed motor-heavy subtests or interpret them cautiously; consider WNV, Leiter-3 or motor-free measures). Report adaptations and their effect.",
  "Pupil interview: participation, friendships, how they feel about their body and supports, what they want to do that they can't. Adaptive measures (ABAS-3, Vineland-3) describe everyday functioning.",
 ],
 "recommendations": [
  "PLAN ACCESS with the school, OT and physiotherapy: physical environment, seating, equipment, toileting, emergency evacuation, trips. The SNA scheme supports care needs (check current Department of Education circular).",
  "ADAPT THE CURRICULUM, not the expectation: alternative recording (keyboard, scribe, speech-to-text), extra time where motor or fatigue demands are high, adapted PE. Check eligibility for assistive technology supports and RACE accommodations.",
  "PLAN FOR FATIGUE AND ABSENCE: rest breaks, scheduling demanding tasks when energy is highest, catch-up plans after hospital stays (see 'Chronic illness affecting school' and 'Missed curriculum from hospital admissions').",
  "PROMOTE PARTICIPATION AND FRIENDSHIP: inclusive PE and yard games, peer awareness (with the pupil's consent), involvement in clubs and trips.",
  "CONTINUUM LEVEL: School Support or School Support Plus, with CDNT, OT, physiotherapy and medical services involved; SENO for resource allocation.",
  "DO NOT make assumptions about cognitive ability from physical presentation, and DO NOT give medical advice. REFER back to the CDNT or medical team where new concerns arise.",
 ],
 "explain_parent": [
  "'My role is to look at how her physical needs affect her learning and school day, and what school can do. The medical side stays with her doctors and therapists.'",
  "'We'll plan for the practical things — access, equipment, fatigue — and also for friendships and joining in, which matter just as much.'",
 ],
 "explain_teacher": [
  "'His physical disability doesn't tell us anything about his ability to learn. Please keep expectations high, and adapt how he shows what he knows.'",
  "'He tires more quickly than others. Put the harder work earlier in the day where you can.'",
  "'In PE and yard, the question is how he can join in, not whether.'",
 ],
 "explain_child": [
  "YOUNGER: 'What things in school are easy for you? What things are tricky because of your body? What would help?'",
  "OLDER: 'You know your body and what you need better than anyone. What do you want teachers to understand? What do you want to do that you're not getting to do?'",
 ],
 "red_flags": [
  "WATCH — deterioration in physical function, new pain, or loss of skills: medical review via the family and the medical team.",
  "WATCH — low mood, isolation or bullying related to disability: address through school supports and refer via the family to Primary Care Psychology, CDNT psychology or CAMHS as appropriate.",
  "RED FLAG — any indication of neglect of care needs or abuse (pupils with disabilities are at increased risk): child protection route; report to Tusla as soon as practicable.",
  "BOUNDARY — the EP describes educational impact and recommends; diagnosis and medical management sit with medical and therapy services.",
 ],
 "questions": [
  "Q: 'Does his condition affect his learning?' A: 'Some conditions have learning implications and some don't. His medical team can tell us about his condition; my assessment tells us about his learning.'",
  "Q: 'Should she be excused from PE?' A: 'It's better to adapt PE so she can take part. The physiotherapist can advise what's safe.'",
  "Q: 'Who pays for the equipment?' A: 'Some comes through the HSE and CDNT, some through Department of Education schemes. The school and SENO can check current routes.'",
 ],
 "supervision": [
  "Bring a case where you adapted assessment for motor demands and discuss how you reported the adaptation and its effect on validity.",
  "Reflect on your own assumptions about physical disability and ability, and how you ensure the pupil's voice is central.",
 ],
 "citations": [
  "Department of Education and Skills. (2014). Circular 0030/2014: The Special Needs Assistant (SNA) scheme to support teachers in meeting the care needs of some children with special educational needs, arising from a disability. Department of Education and Skills.",
  "Rosenbaum, P., & Gorter, J. W. (2012). The 'F-words' in childhood disability: I swear this is how we should think! Child: Care, Health and Development, 38(4), 457–463.",
  "World Health Organization. (2007). International classification of functioning, disability and health: Children and youth version (ICF-CY). WHO.",
 ],
})
