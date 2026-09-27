# Part H METHODS records: Group intervention, Staff training, Transition planning.
# Format: SCHEMAS.md "METHODS". Paragraphs separated by blank lines.
# Agrees with Reference Part A macro 19 (Wellbeing interventions at class and group level),
# macro 29 (Deliver the good practice presentation) and Part D transition rows.


def J(*paras):
    return "\n\n".join(paras)


GROUP_INTERVENTION = {
 "name": "Group intervention",
 "competencies": "Competency 3 Intervention · Competency 4 Systemic Change · Competency 8 Research",
 "coru": "2.4 · 3.7 · 3.8 · 5.33 · 5.34 · 5.36 · 5.37 · 5.39 · 5.40",
 "psi": "1.2.10 · 1.3.4 · 1.4.3 · 2.2.2 · 2.3.2 · 2.3.3 · 3.3.2 · 3.3.3 · 4.2.2",

 "history": J(
  "Group work with children has three separate lineages, and the one you borrow from shapes what you think a group is for.",
  "GROUP PSYCHOTHERAPY — Yalom (The Theory and Practice of Group Psychotherapy, 1970; Yalom & Leszcz, 6th ed. 2020) named the therapeutic factors of groups: universality ('I'm not the only one'), instillation of hope, imparting information, altruism, interpersonal learning, group cohesiveness, among others. These are why a group can do what individual work cannot. Tuckman (1965, Psychological Bulletin) gave the forming–storming–norming–performing sequence still used to plan session arcs.",
  "EDUCATIONAL AND NURTURE GROUPS — Marjorie Boxall set up the first nurture groups in inner London (ILEA) in 1969-70 for children whose early experiences left them unready for class (Bennathan & Boxall, 2000). Circle of Friends came from North American inclusion work and was adapted in UK EP practice (Newton, Taylor & Wilson, 1996; Frederickson & Turner, 2003).",
  "MANUALISED CBT AND SEL PROGRAMMES — from the 1990s: FRIENDS (Barrett, Australia), Zippy's Friends (Partnership for Children, UK), Incredible Years small-group Dinosaur School (Webster-Stratton). Durlak et al. (2011) consolidated SEL evidence.",
  "IRELAND — NEPS has trained teachers in FRIENDS programmes and Incredible Years Teacher Classroom Management; Weaving Well-being and Zippy's Friends are used in Irish primary schools. Check which programmes your service currently supports before you offer one (Reference row 78)."),

 "evidence": J(
  "Uneven, and you must say which part of it you are relying on (PSI 4.2.2; Reference row 78).",
  "UNIVERSAL SEL — Durlak et al. (2011, Child Development, 213 programmes) found modest but real gains in social-emotional skills, behaviour and attainment. Implementation problems weakened outcomes; fidelity is the variable that predicts benefit (Durlak & DuPre, 2008).",
  "TARGETED ANXIETY AND DEPRESSION PREVENTION — Werner-Seidler et al. (2017, Clinical Psychology Review) meta-analysed school-based prevention: small effects for both depression and anxiety; for depression, targeted programmes outperformed universal ones. Effect sizes: check the paper before quoting.",
  "WHO DELIVERS MATTERS — Stallard et al. (2014, PACES trial, Lancet Psychiatry): universal FRIENDS delivered by health facilitators reduced anxiety; delivered by school staff it did not differ from usual PSHE. Training and support of the deliverer is part of the intervention (see Staff training, Part H).",
  "MINDFULNESS — Kuyken et al. (2022, MYRIAD) found universal school mindfulness no better than usual provision for adolescents. Do not present it as established.",
  "SOCIAL SKILLS GROUPS — modest effects, weak generalisation (Gresham, Sugai & Horner, 2001).",
  "HARM — Dishion, McCord & Poulin (1999) documented deviancy training in groups of adolescents with conduct difficulties. Read it before you run any group.",
  "IRISH TRIAL — Clarke, Bunting & Barry (2014) evaluated Zippy's Friends in disadvantaged Irish primary schools; read the outcomes and the implementation findings before citing."),

 "when_why": J(
  "WHEN IT IS NEEDED: the same need is shared by several children in one school (anxiety about transfer, friendship difficulty in one class, bereavement after a death in the community, emotional literacy in an infant class); consultation shows the school wants to build its own capacity; individual referrals in one area keep arriving (NEPS areas 3.1 anxiety, 4.1 friendships, 2.2 behaviour at break).",
  "WHY: a group reaches eight children for the cost of one assessment, and Yalom's universality factor ('other people feel this too') is only available in a group. It also leaves something behind: a trained co-facilitator and a set of materials (CORU 5.40).",
  "CHOOSE THE TIER FIRST (Reference row 78): universal (whole class), targeted/selective (children identified as at risk), indicated (individual). If a third of the class shares the difficulty, it is a classroom problem and a targeted group mislabels it as a child problem.",
  "WHEN IT IS NOT THE RIGHT CHOICE: a child at current risk of self-harm or in acute distress — individual work and the risk route first; a child whose difficulty would be amplified by grouping (conduct difficulties with similar peers); a school that cannot give a stable room, time slot and co-facilitator for the full programme; a request after a critical incident for a single-session 'debriefing' group — NEPS critical incident guidance favours psychological first aid and monitoring, not compulsory debriefing (check the current NEPS Critical Incident guidelines)."),

 "need_before": J(
  "A NAMED NEED AND A TIER, agreed with the school in consultation, with the reason it is a group need.",
  "A PROGRAMME OR PLAN with a stated evidence base and its core components identified from the manual — what must not be cut (Reference row 78, 'Adapt delivery').",
  "A CO-FACILITATOR from the school (class teacher, SET, guidance counsellor, SNA where appropriate) who commits to every session and will run it after you.",
  "MEMBERSHIP SCREENING: who is in, who is not, and why. Mix of presentations (not all withdrawn or all externalising). Size typically 6–8 for a targeted group; check the manual. Any child you screen out needs an alternative, not just exclusion.",
  "CONSENT from parents for a targeted group (it identifies the child), with a plain account of content, measures and what happens to data (PSI 1.3.4–1.3.5); child assent in their terms; opt-out arrangements for universal work.",
  "A DISCLOSURE PLAN: what you will say at session one about limits of confidentiality, who the DLP is, who follows up a child who becomes upset.",
  "PRE- AND POST-MEASURES chosen before session one: a brief validated child measure (SDQ, RCADS self-report where anxiety is the focus — check licensing and service approval), a fidelity checklist, and a staff view.",
  "LOGISTICS: a fixed room and slot that does not take a child from a subject they love or their only good lesson; 6–10 weekly sessions scheduled around school holidays."),

 "how": J(
  "STEP 1 — Consult: agree the need, tier, outcome and co-facilitator. Write one sentence of what success looks like at week 8.",
  "STEP 2 — Screen and invite: talk to each child individually before the group ('It's a group about... would you like to come?'). Meet or phone parents. Record the reason for inclusion.",
  "STEP 3 — Baseline: administer the pre-measure in the week before session one, not during it.",
  "STEP 4 — Session one: agree ground rules WITH the group (Reference row 78), state limits of confidentiality in child language, run a low-demand warm-up, and preview the whole programme.",
  "STEP 5 — Each session: same structure (check-in, recap, main activity, practice, closing round, take-home task). Divide roles with the co-facilitator in advance: one leads, one watches the room.",
  "STEP 6 — After each session (10 minutes): fidelity checklist, note adaptations and why, note any child to follow up. Contact the DLP the same day for any disclosure.",
  "STEP 7 — Hand over: from the midpoint, the co-facilitator leads more; by the final sessions you assist.",
  "STEP 8 — Close: final session marks the ending (certificate, what I learned, who I go to now). Post-measure in the same week.",
  "STEP 9 — Evaluate and report: pre/post, fidelity, staff and child views, with honest limits (small n, no control). Agree when the school will run it next."),

 "early_years": J(
  "EARLY YEARS 0–5 — group work at this age is mostly delivered by adults around the child, not with the child in a talking group.",
  "In ECCE settings and infant classes, the effective 'group intervention' is often an adult programme (Incredible Years parent or teacher programmes) or small-group play-based work led by setting staff: turn-taking games, emotion-naming with puppets, structured Lego or construction play.",
  "Keep sessions short (10–20 minutes), highly concrete, visual, and repeated. Measures: staff rating (SDQ 2–4 version) and structured play observation rather than self-report.",
  "Link to AIM supports already in place and to Aistear's Well-being theme so the setting keeps using it.",
  "Consent runs through parents and the setting's policy; a child's non-verbal refusal to join is respected (PSI 1.4.3)."),

 "school_age": J(
  "SCHOOL AGE 6–12 — the band where targeted groups are most often run in Irish primary schools.",
  "Common groups: anxiety management (FRIENDS for Life or similar CBT-informed programme), friendship and social skills, Circle of Friends around one child (with that child's and family's consent), emotional literacy (Weaving Well-being, Zippy's Friends at class level), nurture-type groups in some DEIS schools.",
  "Use pictures, role-play and a take-home task the parent sees. Keep the SET or class teacher as co-facilitator so skills are prompted in class between sessions — generalisation is the known weak point (Gresham et al., 2001).",
  "Measures: SDQ (teacher and parent), RCADS self-report from about 8 if anxiety is the target, simple goal ratings with the child.",
  "Sixth Class transfer groups in the spring term link to Transition planning (Part H)."),

 "adolescent": J(
  "ADOLESCENT 13–16 — groups work well when the young person chooses to be there and badly when they feel labelled.",
  "Name the group by its purpose, not the problem ('Exam stress skills', not 'Anxiety group'). Run it in the timetable slot students agree to; SPHE or Wellbeing time in Junior Cycle can host universal work.",
  "Co-facilitate with the guidance counsellor or a year head the students trust. Discuss social media and screenshots in the ground rules: what is said in the group stays there, and you cannot fully guarantee it (PSI 1.2.10).",
  "Deviancy training risk is highest in this band (Dishion et al., 1999): never group several students with conduct difficulties together without prosocial peers and strong structure.",
  "Self-report measures (RCADS, Beck Youth Inventories-2) are meaningful from this age; screen items that ask about self-harm and have a same-day response plan before you administer."),

 "worked_example": J(
  "WORKED EXAMPLE — Fourth Class, primary. Three separate referrals in one term for worry, stomach aches, avoidance of reading aloud.",
  "CONSULTATION FINDING: teacher reports about six children who 'freeze' in class; no whole-class pattern. TIER: targeted. PROGRAMME: a CBT-informed anxiety programme the service supports, 8 weekly 45-minute sessions, co-facilitated with the SET.",
  "SCREENING: seven invited, one declined; one child with daily school refusal is offered individual work instead (EBSA route), not the group.",
  "OPENING SCRIPT (session one): 'This group is for learning what worry does in our bodies and what helps. What we say here stays here — except if someone tells us they're being hurt or might hurt themselves. Then Ms [SET] or I have to tell the person in the school whose job is to keep children safe. We'd tell you first.'",
  "MEASURES: RCADS self-report and SDQ teacher version, week 0 and week 9; fidelity checklist per session; child rating of 'how brave I was this week' 1–5.",
  "RESULT (as you would write it): 'Five of six children reported lower anxiety at post-measure; one reported higher. With six children and no comparison group, this is practice evidence, not proof of effect. Fidelity: 7 of 8 sessions delivered as planned. The SET led sessions 5–8 and will run the programme with Third Class in spring.' The one child whose score rose is followed up individually."),

 "theory": J(
  "YALOM'S THERAPEUTIC FACTORS (Yalom & Leszcz, 2020) — universality, cohesion, interpersonal learning, altruism, imparting information. Plan activities that activate them, e.g. anonymous 'worry box' shared aloud shows universality without exposing anyone.",
  "GROUP DEVELOPMENT — Tuckman (1965): forming, storming, norming, performing (with 'adjourning' added by Tuckman & Jensen, 1977). Expect testing in sessions 2–3; plan the ending from session one.",
  "COGNITIVE-BEHAVIOURAL THEORY — thoughts, feelings, behaviour and body linked; graded exposure; problem solving. The model behind most anxiety programmes (Barrett; Kendall).",
  "SOCIAL LEARNING THEORY — Bandura (1977): modelling, rehearsal and reinforcement. Peers are models, which cuts both ways (Dishion et al., 1999).",
  "IMPLEMENTATION SCIENCE — Durlak & DuPre (2008); Fixsen et al. (2005): outcomes depend on fidelity, dosage, quality, participant responsiveness and adaptation. An effective programme badly delivered is an ineffective programme.",
  "ECOLOGICAL SYSTEMS — Bronfenbrenner (1979): skills learned in the group room generalise only if the classroom and home prompt them."),

 "frameworks": J(
  "NEPS CONTINUUM OF SUPPORT — universal groups sit at Classroom Support (for all); targeted groups at School Support (for some), with the group named in each child's Student Support Plan and review date; individual work at School Support Plus. State the level in the plan.",
  "WELLBEING POLICY STATEMENT AND FRAMEWORK FOR PRACTICE (Department of Education, 2018; revised 2019 — check for updates): the school self-evaluation frame for wellbeing promotion; your group should appear in the school's wellbeing plan, not sit beside it.",
  "WELL-BEING IN POST-PRIMARY SCHOOLS (2013) AND PRIMARY SCHOOLS (2015) — DES/HSE/DoH mental health promotion guidelines describing the multi-level model (school support for all, some, few).",
  "INTERACTIVE FACTORS FRAMEWORK (Frederickson & Cline, 2015) — choose group members by formulation, not by label: a shared affective factor (worry) with different cognitive and environmental factors.",
  "EVALUATION — Kirkpatrick-style levels for the staff side and pre/post child measures for outcomes; Goal-based outcomes (Law & Jacob, 2015, CORC) where standardised measures do not fit.",
  "PSI 2.3.2 AND 2.3.3 — clear objectives; stop if it is harmful or no longer needed."),

 "risk": J(
  "RED FLAG — DISCLOSURE IN THE GROUP. Acknowledge calmly, do not question further in front of peers ('Thank you for telling us. I'd like to talk with you straight after'). Speak with the child privately, record verbatim, inform the DLP the same day. As a mandated person under the Children First Act 2015 you report to Tusla as soon as practicable; telling the DLP does not discharge your own duty. Supervision follows action; it never replaces it.",
  "RED FLAG — a child mentions self-harm or wanting to die, in the group or on a measure. Same-day risk route: stay with the child or ensure a named adult does, inform the DLP and parents per the school and service protocol, and your supervisor.",
  "RED FLAG — a child becomes more distressed across sessions, or the post-measure rises. Review individually; PSI 2.3.3 requires you to stop an activity that is doing harm.",
  "HARM BY DESIGN — deviancy training (Dishion et al., 1999); labelling by group name; peers repeating disclosures in the yard. Mitigate through screening, naming and ground rules.",
  "BOUNDARY — a group is not therapy for a clinical disorder. A child who needs CAMHS, a CDNT or Primary Care Psychology is referred, not absorbed into a group (PSI 2.2.2).",
  "DATA — group measures are personal data: consent, secure storage, anonymised reporting."),

 "learn": J(
  "WHETHER THE CHILDREN CHANGED on the targeted outcome, at least on a brief measure, and whether any child got worse.",
  "WHETHER THE PROGRAMME WAS DELIVERED — the fidelity record separates 'the programme did not work' from 'the programme was not run'.",
  "WHAT THE CHILDREN THOUGHT — which activities they remember, what they use; often different from what adults valued.",
  "WHETHER THE SCHOOL CAN RUN IT — the co-facilitator's confidence and whether a next date is set.",
  "INDIVIDUAL INFORMATION — groups reveal children whose difficulty is larger than it looked and who need individual assessment or referral.",
  "WHAT YOU DO NOT LEARN: whether the programme caused the change (no control, small n, regression to the mean, maturation, other supports running); whether gains last; whether gains generalise to class and home unless you measure there. Say all three in the write-up (PSI 4.2.2, 4.2.5)."),

 "questions": J(
  "Q (principal): 'Can you run a group for our anxious kids and we'll take it from there?' — A: 'I'd love to, on one condition: a member of your staff co-facilitates every session and leads the second half. Otherwise it ends when I leave.'",
  "Q (parent): 'Will everyone know he's in the worry group?' — A: 'The group has a neutral name and runs at a time other groups also run. We talk with the children about keeping each other's stories private.'",
  "Q (teacher): 'Can we just do mindfulness with the class?' — A: 'The biggest recent trial with adolescents found it no better than usual lessons (Kuyken et al., 2022). If the aim is calm, there are options with stronger evidence; let's look at what you're trying to change first.'",
  "Q (child): 'Do I have to talk?' — A: 'No. You can pass any time. Listening counts.'",
  "Q (school): 'Why can't we put all the boys who fight in one group?' — A: 'Research shows that grouping young people with the same behaviour difficulties can make it worse, because they learn from each other (Dishion et al., 1999). A mixed group with strong structure is safer.'",
  "Q (supervisor): 'How will you know if it worked?' — A: 'Pre and post on a brief measure, fidelity per session, the SET's view, and whether it runs again next term.'"),

 "why_this": J(
  "WHY A GROUP OVER INDIVIDUAL WORK: shared need, universality effect, peer practice of social skills, and far more children reached per hour. Individual work is better for risk, complex or idiosyncratic needs, and children whose difficulty is not shared.",
  "WHY A MANUALISED PROGRAMME OVER A HOME-MADE ONE: defined core components, a literature, and a fidelity checklist. A home-made group has none of these and cannot be evaluated against anything (Reference row 78).",
  "WHY TARGETED OVER UNIVERSAL (OR VICE VERSA): targeted programmes showed larger effects for depression prevention in fewer children; universal work reaches everyone and avoids labelling but has small effects per child (Werner-Seidler et al., 2017). The shape of the need decides it, not preference.",
  "WHY CO-FACILITATION OVER DELIVERING ALONE: CORU 5.40; PACES shows who delivers changes outcomes; and it is the only route to sustainability.",
  "WHAT I WOULD CHOOSE INSTEAD: teacher consultation when the difficulty is classroom-wide; Staff training when the school wants to run the programme itself; individual solution-focused work when the child's goals are personal."),

 "next": J(
  "→ IF IT WORKED: agree when the school runs it again, who leads, and what support they need; add it to the school's wellbeing plan and Student Support Plans.",
  "→ IF ONE CHILD DID NOT BENEFIT OR WORSENED: individual review; consider assessment, consultation with parents, or referral (Primary Care Psychology, CAMHS, CDNT) via the usual route.",
  "→ IF FIDELITY WAS LOW: the finding is about delivery conditions (time, room, staff turnover); take it to consultation with the principal before running again.",
  "→ IF SKILLS DID NOT GENERALISE: add a classroom component — prompts, visuals, teacher praise for the target skill — via teacher consultation.",
  "→ WRITE IT UP as a short practice-based evaluation: it is evidence for Competency 3 and Competency 8 (Research) in one piece (Reference row 78).",
  "→ LOG IT: Log sheet against 19. Wellbeing interventions at class and group level; Appendix 5 tagged Intervention with outcomes."),

 "supervision": J(
  "BEFORE: bring the membership list with your reason for each child and each exclusion. Ask: 'Who here worries you, and why?'",
  "BEFORE: rehearse the confidentiality statement aloud with your supervisor, and agree who you contact if a disclosure happens on a day they are not in the school.",
  "DURING: bring fidelity sheets and one moment where you adapted delivery — was it surface adaptation or did you cut a core component?",
  "DURING: bring group process, not just content: who dominates, who is silent, how conflict was handled, how you felt when the group tested you.",
  "AFTER: bring the pre/post data and your draft interpretation; ask your supervisor to challenge any claim of effect.",
  "ALWAYS: if a child protection or self-harm concern arose, act the same day first, then bring it. Ask to be observed facilitating at least one session and complete Appendix 7."),

 "reflection": J(
  "WHAT GOOD LOOKS LIKE: 'I nearly included the boy with daily refusal because he was on the list. Screening showed the group would have exposed him before he was ready. He had individual work instead. In the group, the SET led from week 5 and I noticed I kept stepping back in — I have written down why I found letting go hard.'",
  "WHAT POOR LOOKS LIKE: 'I ran a six-week wellbeing group which the children enjoyed and the teacher said was great.' — no tier, no screening, no measure, no fidelity, no handover, enjoyment reported as effect.",
  "PROMPT 1 — Who did the group serve: the children, the school's wish to be seen to act, or my portfolio?",
  "PROMPT 2 — Which child did I find it hardest to include, and what did that say about the group I imagined?",
  "PROMPT 3 — Where did my adaptation protect engagement and where did it erode the programme?",
  "PROMPT 4 — What will be different in that school in six months because of this?",
  "CORU 5.44 — how did my own experience of groups (school, sport, therapy) shape how I ran this one?"),

 "timeline": J(
  "YEAR 1 — ROSCOMMON (03/02/2026–09/07/2026), DONE: check the Log sheet for any group you observed or co-facilitated; do not assume it counts as delivery unless you led part of it.",
  "YEAR 1 — CAVAN (05/10/2026–18/12/2026): plan backwards from 18/12/2026. An 8-week group must start by mid-October to fit a post-measure before the Christmas break, allowing for the October mid-term break (check the school calendar). So: consultation and screening in the first two weeks, baseline by the third. If that is not realistic, co-facilitate a shorter group and evaluate honestly.",
  "YEAR 1 TARGET (Reference row 78, Grade 4): tier chosen deliberately, membership screened, co-facilitated with school staff.",
  "YEAR 2: Grade 5 — pre/post and fidelity data, handover evidenced, and a written reflection on what you would change; whole-class and group delivery become routine.",
  "YEAR 3: a group evaluation written as practice-based research (Competency 8)."),

 "citations": [
  "Durlak, J. A., Weissberg, R. P., Dymnicki, A. B., Taylor, R. D., & Schellinger, K. B. (2011). The impact of enhancing students' social and emotional learning: A meta-analysis of school-based universal interventions. Child Development, 82(1), 405–432.",
  "Durlak, J. A., & DuPre, E. P. (2008). Implementation matters: A review of research on the influence of implementation on program outcomes and the factors affecting implementation. American Journal of Community Psychology, 41(3–4), 327–350.",
  "Dishion, T. J., McCord, J., & Poulin, F. (1999). When interventions harm: Peer groups and problem behavior. American Psychologist, 54(9), 755–764.",
  "Stallard, P., Skryabina, E., Taylor, G., Phillips, R., Daniels, H., Anderson, R., & Simpson, N. (2014). Classroom-based cognitive behaviour therapy (FRIENDS): A cluster randomised controlled trial to Prevent Anxiety in Children through Education in Schools (PACES). The Lancet Psychiatry, 1(3), 185–192.",
  "Werner-Seidler, A., Perry, Y., Calear, A. L., Newby, J. M., & Christensen, H. (2017). School-based depression and anxiety prevention programs for young people: A systematic review and meta-analysis. Clinical Psychology Review, 51, 30–47.",
  "Kuyken, W., Ball, S., Crane, C., Ganguli, P., Jones, B., Montero-Marin, J., et al. (2022). Effectiveness and cost-effectiveness of universal school-based mindfulness training compared with normal school provision in reducing risk of mental health problems and promoting well-being in adolescence: The MYRIAD cluster randomised controlled trial. Evidence-Based Mental Health, 25(3), 99–109.",
  "Clarke, A. M., Bunting, B., & Barry, M. M. (2014). Evaluating the implementation of a school-based emotional well-being programme: A cluster randomized controlled trial of Zippy's Friends for children in disadvantaged primary schools. Health Education Research, 29(5), 786–798.",
  "Yalom, I. D., & Leszcz, M. (2020). The theory and practice of group psychotherapy (6th ed.). Basic Books.",
 ],
}


STAFF_TRAINING = {
 "name": "Staff training",
 "competencies": "Competency 4 Systemic Change · Competency 5 Working with Others · Competency 3 Intervention",
 "coru": "5.4 · 5.8 · 5.20 · 5.35 · 5.38 · 5.40 · 5.41 · 3.9",
 "psi": "2.2.2 · 2.4.4 · 3.1.2 · 3.3.7 · 3.4.5 · 4.2.1 · 4.2.2 · 4.2.5",

 "history": J(
  "EP-led training of teachers grows out of Caplan's (1970) idea of indirect service: reach the child through the adults who see them daily. Training is consultation delivered to a group.",
  "JOYCE & SHOWERS (1980s; Student Achievement Through Staff Development, 3rd ed. 2002) studied which components of staff development transfer into classroom practice: theory, demonstration, practice with feedback, and in-classroom coaching. Their central finding, cited on Reference row 95: training alone rarely changes practice without follow-up coaching. (Specific transfer percentages are widely quoted from their work — check the source before quoting any figure.)",
  "KIRKPATRICK (1959; Kirkpatrick & Kirkpatrick, 2006) set out four levels for evaluating training: reaction, learning, behaviour, results. GUSKEY (2000) adapted this for education, adding organisational support and student learning outcomes.",
  "EVIDENCE SYNTHESES — Desimone (2009) proposed core features of effective PD; Kennedy (2016) and the EEF meta-analysis (Sims et al., 2021) shifted attention to mechanisms: building knowledge, motivating teachers, developing techniques and embedding practice.",
  "IRELAND — NEPS has long delivered programme training to teachers (e.g. Incredible Years Teacher Classroom Management, FRIENDS programmes); teacher professional learning is now largely provided by Oide (established 2023) and the NCSE Support Service. Check what they already offer before designing your own."),

 "evidence": J(
  "WHAT WORKS IN PD (the most useful summary for an EP): Sims et al. (2021, EEF systematic review and meta-analysis) found PD programmes that combine mechanisms from all four groups — build knowledge, motivate, develop technique, embed practice — are more effective. The EEF Effective Professional Development guidance report (2021) is the practitioner version (Reference row 95).",
  "ONE-OFF SESSIONS — Kennedy (2016, Review of Educational Research) found that how PD is structured matters more than its duration or content label; programmes that prescribe without building teacher understanding show weaker effects. A single input session should be treated as awareness-raising, not intervention, unless followed up.",
  "WHO DELIVERS AND HOW WELL — Stallard et al. (2014, PACES): the same programme delivered by trained school staff did not reproduce the health-led effect, which is an argument for better training and support, not against school delivery.",
  "IRISH EVIDENCE — Hickey et al. (2017) evaluated Incredible Years Teacher Classroom Management in Irish schools in a group randomised trial; read it for effects on teacher and child behaviour before citing.",
  "EVALUATION DATA ARE USUALLY LEVEL 1 — satisfaction forms tell you whether people liked it, not whether practice changed. Claim only what your level of evaluation supports (PSI 4.2.2)."),

 "when_why": J(
  "WHEN IT IS NEEDED: a pattern across cases (three referrals in one school showing the same misunderstanding, e.g. 'he can do it when he wants to' about a child with working memory difficulty); a school implementing something new (a group programme, a Student Support Plan format, a restorative approach); after a critical incident, where staff need to know what to expect and what to do; a request for CPD on a topic within your competence.",
  "WHY: it reaches more children than casework (Reference row 95) and is the most direct route to CORU 5.40 — building capacity among those who deliver interventions. It is also where the Year 1 review named a strength: interpersonal communication and delivery of training.",
  "WHEN IT IS NOT THE RIGHT CHOICE: when the difficulty is a system or resourcing problem (timetabling, SET allocation) — training teachers will not fix it; take it to consultation with the principal. When the request is really for case advice about one named child — that is consultation, not training, and confidentiality forbids it in a staff room. When the topic is outside your competence (medication, diagnosis, specialist therapy): decline or co-deliver with the right professional (PSI 2.2.2).",
  "WATCH FOR: training requested to show that something was done. Ask what the school wants to be different in a term's time."),

 "need_before": J(
  "A NEEDS ANALYSIS — ask the principal and two or three staff: what they want to be able to do, what they already know, what they have already had (Oide, NCSE, NEPS inputs), and what would make it a waste of time.",
  "AN OUTCOME AT KIRKPATRICK LEVEL 3 — what staff will do differently, e.g. 'every class teacher uses a visual schedule with the three pupils on School Support Plus'.",
  "EVIDENCE for every claim you will make: search properly, appraise five sources, use three (Reference row 95, Block 1). Cite in plain language on the slide.",
  "YOUR SUPERVISOR'S AGREEMENT to the topic and content; trainee-delivered training is under supervision.",
  "PRACTICAL DETAILS: audience size and roles (teachers, SNAs, SET, leadership), time slot (Croke Park hours and staff meetings are short — plan for 45–60 minutes), room, technology, whether SNAs are paid to attend.",
  "A ONE-PAGE HANDOUT with the actions; people keep one page (Reference row 95).",
  "AN EVALUATION FORM (three questions: what will you do differently, what was most useful, what was missing) and a follow-up plan, ideally a check-in 4–6 weeks later.",
  "CASE MATERIAL THAT IS FULLY ANONYMISED OR INVENTED — never a recognisable local child."),

 "how": J(
  "STEP 1 — Needs analysis and agreed outcome, in writing, with the principal.",
  "STEP 2 — Build the content backwards from the action: for each action, the minimum theory that makes it make sense (Reference row 95: 'every section should end with what to do').",
  "STEP 3 — Structure for adults (Knowles, 1980): start from their experience ('think of a pupil who...'), short input, a demonstration or video, practice (role-play, planning for one real pupil anonymously), then commitment.",
  "STEP 4 — Rehearse once in front of a non-psychologist and cut jargon.",
  "STEP 5 — Deliver: state at the start what you will and will not cover and that individual cases go to consultation afterwards. Stick to time.",
  "STEP 6 — Close with three things the school could do this term, and each person writing one thing they will try on Monday.",
  "STEP 7 — Collect the evaluation before people leave (two minutes).",
  "STEP 8 — Follow up: a check-in or coaching visit 4–6 weeks later with volunteers; this is the step Joyce & Showers show matters most.",
  "STEP 9 — Summarise feedback honestly, state which Kirkpatrick level you reached, file it for the portfolio."),

 "early_years": J(
  "EARLY YEARS 0–5 — audiences are ECCE staff, preschool leaders, infant teachers and parents.",
  "Topics that fit: emotional regulation and co-regulation, noticing early communication difficulty, supporting play, transition to primary school.",
  "Link content to Aistear (NCCA; updated framework 2024 — check) and Síolta, and to AIM supports — Level 3 of AIM funds training for early years staff (e.g. LINC); do not duplicate what the setting already has (check aim.gov.ie for current levels).",
  "Early years staff often work without non-contact time: short, practical, evening or on-site sessions work best, with demonstration rather than slides.",
  "Delivering here is one way to gain Early Years experience, but it only counts for UCD Table 3 if it is in the Appendix 1 before the placement starts."),

 "school_age": J(
  "SCHOOL AGE 6–12 — the typical audience is a whole primary staff at a Croke Park hour or a SET team.",
  "High-yield topics: working memory in class; anxiety and school avoidance; the NEPS Continuum of Support in practice; writing measurable Student Support Plan targets; behaviour as communication (ABC thinking without jargon); running a named wellbeing programme.",
  "Include SNAs where possible — they spend the most time with pupils on School Support Plus and are often excluded from training.",
  "Use one invented pupil case across the session so every section lands on the same child.",
  "Follow-up: one volunteer class teacher tries the key strategy and reports back at the next staff meeting — coaching in miniature."),

 "adolescent": J(
  "ADOLESCENT 13–16 — the audience at post-primary is larger, subject-specialist and time-poor; a year head team, the SEN department, or the pastoral/wellbeing team is usually a better target than the whole staff.",
  "Topics that fit: anxiety and emotionally based school avoidance; self-harm awareness and the school's response pathway (in line with the 2013 Well-Being in Post-Primary Schools guidelines and school policy); reasonable accommodations and RACE (explaining what the evidence requires, not deciding eligibility); supporting autistic students across subjects.",
  "Subject teachers respond to subject examples: show the same adaptation in maths, English and a practical subject.",
  "Where the topic is suicide or self-harm, check whether a recognised programme (e.g. safeTALK, ASIST, via the HSE National Office for Suicide Prevention — check current offerings) is more appropriate than a bespoke input."),

 "worked_example": J(
  "WORKED EXAMPLE — primary school; four referrals in a year where reports said 'lazy' or 'not trying' about pupils later found to have working memory difficulty.",
  "NEEDS ANALYSIS: principal wants 'something on memory'; two teachers say they have had theory before and want 'what to actually do'.",
  "OUTCOME AGREED: every teacher will use at least two of: chunked instructions, visual reminders, reduced copying from the board, a check-back prompt — with named pupils on School Support.",
  "SESSION (50 minutes, Croke Park hour): 5 min — 'think of a pupil who forgets instructions halfway'; 10 min — working memory in plain language (Gathercole & Alloway, 2008); 5 min — simulation (staff follow a five-step instruction with one repetition); 15 min — four strategies, each with a classroom demonstration; 10 min — pairs plan for one anonymised pupil; 5 min — one thing on Monday, evaluation form.",
  "SCRIPT AT THE START: 'I won't discuss individual children today — if one comes to mind, grab me after and we can set up a proper conversation.'",
  "FOLLOW-UP: three teachers volunteer; four weeks later you visit each for ten minutes.",
  "WRITE-UP: 'Reaction (Level 1): 18 of 21 forms returned. Behaviour (Level 3): three volunteer teachers were observed using at least two strategies at follow-up. No pupil outcome data (Level 4) — this was not measured.'"),

 "theory": J(
  "ADULT LEARNING — Knowles (1980): adults learn when material is relevant to their current problems, draws on their experience and is immediately applicable. Hence problem-centred sessions.",
  "TRANSFER OF TRAINING — Joyce & Showers (2002): knowledge, skill and classroom use are separate outcomes; coaching after training drives the last one.",
  "MECHANISMS OF PD — Sims et al. (2021): building knowledge, motivating staff, developing teaching techniques, embedding practice. A session with only knowledge-building mechanisms is predicted to change little.",
  "IMPLEMENTATION SCIENCE — Fixsen et al. (2005): training is one 'implementation driver' alongside coaching, staff selection, data systems and leadership support. Without the others, training decays.",
  "SELF-EFFICACY — Bandura (1977): teachers adopt strategies they believe they can carry out; mastery practice within the session builds this.",
  "CONSULTATION THEORY — Caplan (1970): indirect service, and consultee-centred work on lack of knowledge, skill, confidence or objectivity. Training addresses knowledge and skill; confidence and objectivity usually need consultation."),

 "frameworks": J(
  "KIRKPATRICK FOUR LEVELS (Kirkpatrick & Kirkpatrick, 2006) — reaction, learning, behaviour, results. State which level your evaluation reached.",
  "GUSKEY FIVE LEVELS (2000) — adds organisational support and change between learning and use. Useful when practice did not change: was it the training or the school's support?",
  "EEF EFFECTIVE PROFESSIONAL DEVELOPMENT (2021) — design checklist from the mechanisms; use it when planning.",
  "NEPS CONTINUUM OF SUPPORT — training that changes Classroom Support is where most children benefit; tie every action to a Continuum level.",
  "WELLBEING POLICY STATEMENT AND FRAMEWORK FOR PRACTICE (Department of Education, 2018/2019) — schools must engage in wellbeing promotion through school self-evaluation; frame wellbeing training as part of that cycle.",
  "ETHICS — PSI 2.4.4 (teaching based on careful preparation, current and scholarly), 4.2.1–4.2.2 (do not overclaim effectiveness), 3.3.7 (refuse to train anyone who will use it to harm), 4.2.3 (make clear in what capacity you are speaking)."),

 "risk": J(
  "RED FLAG — a staff member raises a child protection concern during or after the session ('that sounds like a child in my class...'). Take it out of the group, listen, and follow the Children First route that day: the staff member is also a mandated person, and telling the DLP does not discharge either of your duties to report to Tusla as soon as practicable. Supervision follows action; it never replaces it.",
  "RED FLAG — training on self-harm or suicide can distress staff with personal experience. Say at the start that the topic is difficult, that people may step out, and name the Employee Assistance Service (check the current provider for teachers). Stay after.",
  "BOUNDARY — you are not training staff to diagnose ('this checklist will tell you if a child has ADHD') or to deliver therapy. Screening tools, where discussed, are for referral decisions, and their limits are stated (PSI 2.2.2, 2.3.1).",
  "CONFIDENTIALITY — no identifiable case material; discourage discussion of named pupils in a group of staff.",
  "OVERCLAIMING — a staff audience will act on what you say. If evidence is mixed (mindfulness, sensory diets, brain-training), say so (PSI 4.2.2).",
  "HARMFUL PRACTICE — if asked to train restrictive or exclusionary practices without safeguards, decline and raise it in supervision (PSI 3.1.8)."),

 "learn": J(
  "WHAT STAFF ALREADY BELIEVE — the needs analysis and the opening exercise are data about the school's shared constructs of children (useful for later consultation).",
  "WHETHER THE CONTENT LANDED (Level 1–2) — the form and the questions asked.",
  "WHETHER PRACTICE CHANGED (Level 3) — only if you follow up. Without follow-up you learn nothing about behaviour change.",
  "WHO THE CHAMPIONS ARE — volunteers for follow-up are your co-facilitators for future groups and implementation.",
  "SYSTEM BARRIERS — what staff say they cannot do and why (time, SET allocation, class size) is data for consultation with leadership.",
  "WHAT YOU DO NOT LEARN: whether children benefited (Level 4) unless you designed a measure for it; whether change will last beyond one term; the views of staff who did not attend or did not return forms. Say so in the write-up."),

 "questions": J(
  "Q (principal): 'Can you do a half-hour on autism for the whole staff?' — A: 'I can. So it changes something, can we pick what you'd like staff to do differently afterwards, and can I come back in a month to see how it's going?'",
  "Q (teacher, during session): 'What about [named child]?' — A: 'That's an important question, and I don't want to discuss a child in front of the group. Can we find ten minutes after?'",
  "Q: 'Is there evidence for that?' — A: 'Yes — [author, year] found... in [setting]. It's moderate evidence, not certain. I'll put the reference on the handout.' Or honestly: 'Not strong evidence yet; here is why I still suggest it as something to try and review.'",
  "Q: 'We've had training on this before and nothing changed.' — A: 'That's common, and research explains it — training alone rarely changes practice without follow-up (Joyce & Showers, 2002). That's why I'm offering to come back.'",
  "Q (SNA): 'Is this for us too?' — A: 'Very much so — you often see the pupil most. The strategies apply to you directly.'",
  "Q (supervisor): 'What level of Kirkpatrick did you reach?' — A: 'Level 1 for everyone and Level 3 for three volunteers; no pupil outcomes.'"),

 "why_this": J(
  "WHY TRAINING OVER CASEWORK: the same need across many children; changes Classroom Support for everyone; the most direct route to CORU 5.40 (Reference row 95).",
  "WHY TRAINING PLUS FOLLOW-UP OVER A ONE-OFF: Joyce & Showers (2002) and Sims et al. (2021) — embedding mechanisms (follow-up, prompts, coaching) are what change practice.",
  "WHY TRAINING OVER CONSULTATION: consultation fits one teacher's problem about one child or class; training fits shared knowledge and skill gaps. If the gap is confidence or objectivity, consultation is better (Caplan, 1970).",
  "WHY A PRACTICE-DERIVED TOPIC OVER A GENERIC ONE: it comes from a pattern you saw across cases and it lands differently (Reference row 95).",
  "WHY NOT A MANUALISED PROGRAMME'S OFFICIAL TRAINING: if a recognised programme with accredited trainers exists (Incredible Years, FRIENDS, safeTALK), signpost it rather than improvising a version of it.",
  "WHAT I WOULD CHOOSE INSTEAD: teacher consultation for one class; Group intervention co-facilitated with staff when you want to model a programme live."),

 "next": J(
  "→ FOLLOW UP within 4–6 weeks: visits, a short survey, or an agenda item at the next staff meeting.",
  "→ IF PRACTICE CHANGED: consider a light-touch pupil-level check (e.g. SSP target progress for pupils on School Support) — moves you towards Level 4.",
  "→ IF IT DID NOT: ask Guskey's question — was it the training or the organisational support? Take system barriers to consultation with leadership.",
  "→ IF STAFF RAISED CASES: set up individual consultations through the school's referral route.",
  "→ USE THE CHAMPIONS: invite volunteers to co-facilitate a Group intervention or pilot the strategy.",
  "→ FILE IT: evaluation summary, slides and handout; Log sheet against 29. Deliver the good practice presentation; UCD Table 2 area 4 (Reference row 95).",
  "→ WRITE IT UP as a small practice-based evaluation — evidence for Competency 8."),

 "supervision": J(
  "BEFORE: bring the needs analysis and the agreed outcome. Ask: 'Is this topic within my competence, and is it the school's need or my interest?'",
  "BEFORE: bring the slides and handout; ask your supervisor to mark every claim without a citation and every word a teacher would not use.",
  "BEFORE: agree what you will do if a child protection concern or a named case comes up, and whether your supervisor attends.",
  "AFTER: bring the raw evaluation forms, not your summary, and read the critical ones together.",
  "AFTER: bring the moment you were least confident — a hostile question, a silence — and how you handled it.",
  "ASK to be observed delivering and complete Appendix 7; ask how your supervisor evaluates training in their own practice."),

 "reflection": J(
  "WHAT GOOD LOOKS LIKE: 'I planned 40 slides. My supervisor asked what one thing teachers should do on Monday; I couldn't say. I cut to 12 slides around four strategies. At follow-up two of three volunteers were using them; the third said copying from the board was a whole-school habit she could not change alone — so that went to the principal.'",
  "WHAT POOR LOOKS LIKE: 'I delivered training on anxiety which was well received (feedback forms very positive).' — no outcome, no follow-up, Level 1 reported as impact.",
  "PROMPT 1 — Which claim did I make most confidently, and how strong is the evidence for it really?",
  "PROMPT 2 — What did the questions tell me about how this staff sees children who struggle?",
  "PROMPT 3 — What did I leave out because I was afraid it would lose the room?",
  "PROMPT 4 — Whose voice was missing: SNAs, parents, pupils?",
  "CORU 5.44 — how did my own experience of being taught, and of teachers, shape how I pitched this?"),

 "timeline": J(
  "YEAR 1 — ROSCOMMON (03/02/2026–09/07/2026), DONE: check the Log sheet for any training or presentation; the good practice presentation (Reference row 95) is the Year 1 anchor.",
  "YEAR 1 — CAVAN (05/10/2026–18/12/2026): agree one practice-derived topic with your supervisor by early November, deliver before the end of November so a 4-week follow-up fits before 18/12/2026. Target Grade 4 on Reference row 95: practice-derived topic, pitched to the audience, resource left behind.",
  "YEAR 1 GRADE 5: evaluated, can report what changed, can say what you would do differently.",
  "YEAR 2: CPD training for professionals (Reference row 95); training linked to a Group intervention so staff are trained, coached and then deliver.",
  "YEAR 3: a training evaluation written up at Kirkpatrick Level 3 or 4 as practice-based research."),

 "citations": [
  "Joyce, B., & Showers, B. (2002). Student achievement through staff development (3rd ed.). Association for Supervision and Curriculum Development.",
  "Kirkpatrick, D. L., & Kirkpatrick, J. D. (2006). Evaluating training programs: The four levels (3rd ed.). Berrett-Koehler.",
  "Guskey, T. R. (2000). Evaluating professional development. Corwin Press.",
  "Sims, S., Fletcher-Wood, H., O'Mara-Eves, A., Cottingham, S., Stansfield, C., Van Herwegen, J., & Anders, J. (2021). What are the characteristics of effective teacher professional development? A systematic review and meta-analysis. Education Endowment Foundation.",
  "Kennedy, M. M. (2016). How does professional development improve teaching? Review of Educational Research, 86(4), 945–980.",
  "Desimone, L. M. (2009). Improving impact studies of teachers' professional development: Toward better conceptualizations and measures. Educational Researcher, 38(3), 181–199.",
  "Fixsen, D. L., Naoom, S. F., Blase, K. A., Friedman, R. M., & Wallace, F. (2005). Implementation research: A synthesis of the literature. University of South Florida, National Implementation Research Network.",
  "Hickey, G., McGilloway, S., Hyland, L., Leckey, Y., Kelly, P., Bywater, T., Comiskey, C., Lodge, A., Donnelly, M., & O'Neill, D. (2017). Exploring the effects of a universal classroom management training programme on teacher and child behaviour: A group randomised controlled trial and cost analysis. Journal of Early Childhood Research, 15(2), 174–194.",
 ],
}


TRANSITION_PLANNING = {
 "name": "Transition planning",
 "competencies": "Competency 3 Intervention · Competency 5 Working with Others · Competency 4 Systemic Change",
 "coru": "1.16 · 2.14 · 2.16 · 3.1 · 3.7 · 5.14 · 5.34 · 5.39 · 5.40",
 "psi": "1.2.5 · 1.3.4 · 1.4.1 · 2.2.2 · 3.4.2 · 3.4.3 · 3.4.5 · 4.2.5",

 "history": J(
  "ECOLOGICAL TRANSITIONS — Bronfenbrenner (1979) defined an ecological transition as a change in a person's role or setting, and argued development is shaped by how well the settings (mesosystem) connect. Transition planning is the practice of building those connections.",
  "SCHOOL START — Rimm-Kaufman & Pianta (2000) proposed the ecological and dynamic model of transition: outcomes depend on the relationships between child, family, preschool, school and community over time, not on the child's 'readiness' alone.",
  "PRIMARY TO POST-PRIMARY — in Ireland, the ESRI study Moving Up (Smyth, McCoy & Darmody, 2004) followed first-year students and documented what eases or complicates the move; Growing Up in Ireland has since added national cohort data (check the relevant GUI reports). In England, Evangelou et al. (2008) identified features of a successful transfer.",
  "POST-SCHOOL — Kohler's Taxonomy for Transition Programming (1996; 2.0, 2016) and Test et al. (2009) set out evidence-based predictors of post-school outcomes for students with disabilities. In Ireland, McGuckin et al. (2013, NCSE Research Report 14) studied transitions to further and higher education.",
  "IRISH POLICY — NCCA transfer documents (Mo Scéal, 2018, preschool to primary; the Education Passport, from 2014, primary to post-primary); HSE New Directions (2012) for adult day services. Part D lists transition planning at every band as context, not a diagnosis."),

 "evidence": J(
  "Transition planning is a PROCESS, not a manualised intervention; the evidence is mostly observational and qualitative. Say that (PSI 4.2.2).",
  "SCHOOL START — Rimm-Kaufman & Pianta (2000) and later work support multiple, relationship-based transition practices (visits, information sharing, contact with families) over single events; causal evidence is limited.",
  "PRIMARY TO POST-PRIMARY — Evangelou et al. (2008) found that most pupils settle well, and that successful transfer is associated with new friendships, confidence, settling into routines, interest in school and curriculum continuity; pupils with SEN and those bullied at school were more likely to struggle. Irish ESRI work (Smyth et al., 2004) reports similar themes; check specific proportions before quoting.",
  "POST-SCHOOL — Test et al. (2009) systematically identified predictors such as work experience in school, self-determination, inclusion in general education, parental involvement and interagency collaboration. Correlational, US-based: use as a planning checklist, not as proof.",
  "IRISH POST-SCHOOL — McGuckin et al. (2013) described uneven information, late planning and dependence on individual staff. Scanlon, Shevlin and colleagues have published further Irish work — check current NCSE research.",
  "PRACTICAL LESSON across all three: late planning and information that does not travel are the commonest failures."),

 "when_why": J(
  "WHEN: any child with SEN or significant wellbeing needs approaching a change of setting — (1) PRESCHOOL → PRIMARY (school start, including choice of mainstream class, special class or special school); (2) PRIMARY → POST-PRIMARY (Sixth Class to First Year); (3) POST-SCHOOL (further education, training, higher education, employment, HSE adult day or rehabilitative training services) — plus service transitions (CDNT to adult disability services; CAMHS to adult mental health services, usually at 18 — check local arrangements).",
  "WHY: transitions concentrate risk. Supports held in one setting (AIM, SNA access, a trusted key adult, an informal understanding with a teacher) do not transfer automatically. Anxiety, school avoidance and deterioration cluster around them (Part D: 'Anticipatory anxiety about transitions').",
  "THE EP ROLE: formulation and information that the next setting can use; advice on placement and supports (not the placement decision, which rests with parents, schools and the NCSE); linking agencies; the child's voice in the plan.",
  "WHEN NOT: transition planning is not a reason to re-assess a child who has a current, adequate report; update the functional picture instead. It does not replace the school's own transfer process — support it."),

 "need_before": J(
  "TIMING — start a year ahead: preschool → primary in the autumn before school entry; primary → post-primary from Fifth Class (school applications often close in the autumn of Fifth or Sixth Class — check local admission policies under the Education (Admission to Schools) Act 2018); post-school by Transition Year or Fifth Year at the latest (Reference Part D: 'post-school transition planning starts here').",
  "CONSENT — parental consent (and the young person's, increasingly, from 16; and theirs alone for decisions at 18+, see Assisted Decision-Making) to share reports and the Student Support File with the receiving setting (PSI 1.2.5).",
  "THE CURRENT PICTURE — Student Support File and Plan, most recent psychological and CDNT/CAMHS reports, AIM supports in place (for preschool), current Continuum level.",
  "THE PEOPLE — parents; the child or young person; current and receiving setting leads (SET coordinator, guidance counsellor, year head); the SENO (NCSE) where special class/school placement or SNA access is in question; CDNT key worker; for post-school, the HSE disability services contact and the guidance counsellor.",
  "THE SYSTEM FACTS, CHECKED THIS YEAR: AIM levels (aim.gov.ie); NCSE processes; DARE/HEAR rules (accesscollege.ie); CAO dates; HSE school-leaver profiling arrangements in the local area. These change annually.",
  "AN ADAPTIVE PICTURE for post-school planning with significant needs: Vineland-3 or ABAS-3 (adult forms where age-appropriate)."),

 "how": J(
  "STEP 1 — MAP: what supports exist now, which will not transfer, what the receiving setting offers. Write it as a two-column table: now / next.",
  "STEP 2 — HEAR THE CHILD: what they know, fear and hope about the move (visual scale, solution-focused questions, a 'my profile' page in their words). Their voice goes in the document that travels.",
  "STEP 3 — PLANNING MEETING (sending and receiving setting, parents, young person where appropriate, relevant professionals): agree actions, owners, dates. You bring the formulation in two paragraphs, not the full report.",
  "STEP 4 — INFORMATION THAT TRAVELS: with consent, the current Student Support Plan, a one-page profile (strengths, what helps, triggers, how to communicate), and relevant reports. Check who at the receiving end reads it and when.",
  "STEP 5 — PREPARATION: extra visits, photos or video of the new setting, a named key adult, map and timetable practice, a social story for younger children, a buddy.",
  "STEP 6 — THE FIRST WEEKS: a check-in point in week 2–4 and a review by half-term, with the receiving setting owning it.",
  "STEP 7 — CLOSE THE LOOP: confirm the receiving setting has the information and that any referral you made has been picked up (PSI 3.4.3)."),

 "early_years": J(
  "PRESCHOOL → PRIMARY (EARLY YEARS 0–5).",
  "AIM (Access and Inclusion Model) supports in ECCE are tiered in levels — universal (inclusive culture, information, training such as LINC) and targeted (Better Start early years specialist advice, equipment and minor alterations, therapeutic input, additional capacity funding). They END at school entry; nothing transfers automatically. Check current level definitions at aim.gov.ie.",
  "MO SCÉAL (NCCA, 2018): preschool-to-primary transfer templates, completed by the preschool with parents and the child. Encourage their use and add your formulation to them.",
  "PLACEMENT QUESTIONS: mainstream class with supports, an early intervention class (for some autistic children aged 3–5), a special class or special school. The SENO advises on and supports access to special class and school places; the decision about the offer rests with schools and parents. Do not promise placements.",
  "DEFERRING SCHOOL ENTRY: a frequent parent question. Compulsory school age in Ireland is 6 (Education (Welfare) Act 2000). Respond with the child's needs and the supports available at each option, not a general rule; evidence on deferral is mixed — check before citing.",
  "CDNT and AON (Disability Act 2005) reports should travel with consent. This is also an Early Years evidence opportunity if planned into Appendix 1."),

 "school_age": J(
  "PRIMARY → POST-PRIMARY (SCHOOL AGE 6–12, Fifth and Sixth Class).",
  "EDUCATION PASSPORT (NCCA): Sixth Class end-of-year report, the pupil's 'My Profile' and the parent's 'My Child's Profile', sent to the post-primary school once enrolment is confirmed. Encourage a richer version for pupils with SEN, with consent.",
  "STUDENT SUPPORT FILE: should transfer with consent; check that the post-primary SEN coordinator actually receives and reads it.",
  "SUPPORTS THAT DO NOT TRANSFER AUTOMATICALLY: SNA access (allocated to schools, not pupils — the post-primary school applies to the NCSE), special class place (separate application), assistive technology, RACE (applied for by the post-primary school at Junior Cycle and Leaving Certificate — check current SEC rules).",
  "PREPARATION: extra induction visits, a timetable and map, a named key adult, locker and bell practice, early warning to subject teachers about the student's profile. Transfer of friendships predicts settling (Evangelou et al., 2008).",
  "WATCH: anticipatory anxiety and avoidance peak in the spring and summer before transfer; a small transition group (see Group intervention) can help."),

 "adolescent": J(
  "POST-SCHOOL (ADOLESCENT 13–16 into YOUNG ADULT) — plan from Transition Year / Fifth Year; for students in special schools and special classes, earlier.",
  "HIGHER EDUCATION: DARE (Disability Access Route to Education) offers reduced-points places to school leavers whose disability affected their education; HEAR (Higher Education Access Route) is a separate, socio-economic scheme. Both via the CAO. DARE 2026 (accesscollege.ie): under 23 on 01/01/2026; CAO by 01/02/2026; documents by a March deadline. For dyslexia, a psychological report of any age, plus two literacy attainment scores at or below the 10th percentile (SS 81 or below) from testing on or after 01/02/2024. The school completes an Educational Impact Statement. Rules change yearly — check the current handbook.",
  "FURTHER EDUCATION AND TRAINING: ETB PLC courses, the National Learning Network, the Fund for Students with Disabilities, AHEAD for information.",
  "ADULT SERVICES: for students with significant intellectual disability or complex needs, the HSE school-leaver profiling process for adult day services and Rehabilitative Training (usually a referral by the principal before the final year — check the local CHO process), under HSE New Directions. Current adaptive measures (Vineland-3 / ABAS-3 adult forms) and a functional, vocational report are what these services need (Part D).",
  "SERVICE TRANSITIONS: CAMHS to adult mental health services and children's to adult disability services at 18 — map these before the young person reaches them (Reference row 93)."),

 "worked_example": J(
  "WORKED EXAMPLE — Sixth Class autistic pupil on School Support Plus, attending mainstream with SNA access; transferring to a large post-primary school in September.",
  "MAP (now / next): SNA access / school must apply to the NCSE; one teacher / eleven subject teachers; quiet room at lunch / unknown; mother emails teacher daily / no equivalent route.",
  "CHILD'S VOICE (visual scale, 1–5 worry): bells 5, getting lost 5, lunch in canteen 4, new subjects 1 ('I like science'). Goes into his one-page profile in his words.",
  "PLANNING MEETING in March with the post-primary SEN coordinator, parents, SET, the pupil for the last ten minutes. Actions: three extra visits in May–June with photos; timetable and map in June; a named key adult (SEN coordinator) with a daily check-in for the first four weeks; a lunchtime club as a quiet option; subject teachers briefed on the profile before September; review by the October mid-term.",
  "SCRIPT TO THE PUPIL: 'You told me bells and getting lost are the worst. So we're going to walk the building three times before summer and you'll get the map to keep. What else would help?'",
  "WHAT YOU WRITE: 'Transition supports agreed on [DD/MM/YYYY]; owners and dates as above. Review: [school] to contact parents by [DD/MM/YYYY]. With consent, the Student Support File and this report have been shared with [post-primary SEN coordinator].'"),

 "theory": J(
  "ECOLOGICAL SYSTEMS — Bronfenbrenner (1979): the mesosystem (links between home, sending and receiving setting) is what planning strengthens. A transition is harder when settings do not talk.",
  "ECOLOGICAL AND DYNAMIC MODEL OF TRANSITION — Rimm-Kaufman & Pianta (2000): relationships over time, not readiness at a point.",
  "STAGE–ENVIRONMENT FIT — Eccles and colleagues (e.g. Eccles et al., 1993, American Psychologist): the move to secondary school often reduces autonomy and teacher closeness at the age adolescents most need them; mismatch predicts decline in motivation.",
  "UNCERTAINTY AND ANXIETY — intolerance of uncertainty is a factor in anxiety and is prominent for many autistic young people; predictability (visits, visuals, timetables) reduces uncertainty, which is why preparation works.",
  "SELF-DETERMINATION — Wehmeyer (and Test et al., 2009): young people who take part in planning their own transition have better post-school outcomes; it is also their right.",
  "CAPACITY AND AUTONOMY — the Assisted Decision-Making (Capacity) Act 2015 (commenced 26/04/2023) presumes capacity at 18; post-school planning must include the young adult as the decision-maker, with support where needed."),

 "frameworks": J(
  "NEPS CONTINUUM OF SUPPORT — the Student Support File is the document that carries a pupil's Continuum history; transition actions go in the Student Support Plan with a review date.",
  "NCSE — SENOs, special class and school placement, SNA allocation; NCSE guidance for parents on moving from primary to post-primary (check the current edition on ncse.ie).",
  "NCCA — Aistear (updated 2024 — check), Mo Scéal (2018), Education Passport; Level 1 and Level 2 Learning Programmes at Junior Cycle for some students with general learning disability.",
  "DISABILITY ACT 2005 AND EPSEN ACT 2004 — Assessment of Need (to age 18, CDNT); EPSEN sections on individual education plans and transition are not fully commenced — check before citing any section as a duty.",
  "HSE NEW DIRECTIONS (2012) — adult day services framework; HSE school-leaver and Rehabilitative Training profiling.",
  "HIGHER EDUCATION — DARE and HEAR (accesscollege.ie; each year's handbook).",
  "INTERNATIONAL — Kohler's Taxonomy for Transition Programming 2.0 (2016): student-focused planning, student development, interagency collaboration, family engagement, programme structure — a usable checklist for a post-school plan.",
  "ADMA 2015 — supported decision-making from 18."),

 "risk": J(
  "RED FLAG — deterioration around a transition: new or increased self-harm, suicidal talk, sudden refusal to attend, eating or sleep collapse. Same-day risk route: ensure the young person is safe with a named adult, inform the DLP, parents and your supervisor per protocol; refer urgently (GP, CAMHS or emergency services as risk requires).",
  "RED FLAG — child protection information must travel through the proper route. If you hold a concern, the Children First Act 2015 duty is yours: report to Tusla as soon as practicable; telling the DLP does not discharge it; a transfer of school does not end it. Supervision follows action; it never replaces it.",
  "RED FLAG — the 'service gap' at 16–18: a young person discharged from CAMHS or a CDNT with no adult service picking up. Do not close your involvement until contact has begun with the receiving service (PSI 3.4.3).",
  "BOUNDARY — you advise; you do not allocate placements, SNA access, DARE eligibility or HSE funding, and you do not promise them. You do not diagnose to meet an eligibility rule (PSI 2.2.2).",
  "DATA — share only what the receiving setting needs, with consent (PSI 1.2.1, 1.2.5); at 18 consent is the young adult's.",
  "EXPECTATIONS — writing a report 'for DARE' that overstates impact harms the young person and the profession (PSI 4.2.2)."),

 "learn": J(
  "WHAT WILL BE LOST at the transition — the supports and relationships that currently hold the child, many of them informal and undocumented.",
  "WHAT THE CHILD OR YOUNG PERSON FEARS AND WANTS — often specific (bells, canteen, being called on) and fixable.",
  "WHETHER THE RECEIVING SETTING CAN MEET THE NEED — and what it will need to put in place and by when.",
  "WHICH AGENCIES ARE INVOLVED AND WHO IS MISSING — gaps between CDNT, CAMHS, adult services and education become visible only when you map them.",
  "WHAT THE FAMILY'S CAPACITY IS to navigate applications (CAO, DARE, HSE profiling, NCSE) — an equity issue.",
  "WHAT YOU DO NOT LEARN: how the child will actually cope (only the review tells you); whether a placement or support will be granted (decided elsewhere); outcomes years later. Plan the review, and say in writing that the plan is a prediction to be checked."),

 "questions": J(
  "Q (parent, preschool): 'Should we hold her back a year?' — A: 'Let's look at what she'd need in each option, and what support would be there. Some children benefit from another year, some don't; I'd rather decide on her needs than a general rule.'",
  "Q (parent): 'Will his SNA go with him to secondary?' — A: 'Not automatically. SNA support is allocated to schools, so the post-primary school applies. I'll make sure the information it needs is in the report, with your consent.'",
  "Q (young person): 'Do I have to tell college I'm dyslexic?' — A: 'It's your choice. If you want DARE or supports in college, you'll need to share evidence; the disability service keeps it confidential.'",
  "Q (school): 'Can you do a new assessment for DARE?' — A: 'For dyslexia DARE accepts a psychological report of any age, but it needs recent attainment scores — check this year's rules. Often what's needed is updated attainment testing, not a full reassessment.'",
  "Q (parent of 17-year-old with intellectual disability): 'What happens when school ends?' — A: 'There's an HSE process for school leavers that the school principal usually starts before the final year. Let's check with the school now which stage it's at.'",
  "Q (young adult, 18): 'Can you send my report to the college?' — A: 'Yes, with your consent — now that you're 18 it's your decision, not your parents'.'"),

 "why_this": J(
  "WHY A PLANNED PROCESS OVER A HANDOVER LETTER: information that is sent is not the same as information that is read and acted on; relationships and preparation carry the move (Rimm-Kaufman & Pianta, 2000).",
  "WHY THE EP OVER THE SCHOOL ALONE: the EP holds the formulation, knows the agencies, and can translate a report into what the next setting should do. The school holds the relationship and the process.",
  "WHY EARLY OVER LATE: school applications, NCSE processes, CAO/DARE deadlines and HSE profiling all have lead times; late planning is the commonest failure (McGuckin et al., 2013).",
  "WHY THE YOUNG PERSON AT THE CENTRE: self-determination predicts post-school outcomes (Test et al., 2009) and from 18 the decisions are theirs (ADMA 2015).",
  "WHAT I WOULD CHOOSE INSTEAD OR ALONGSIDE: teacher consultation with the receiving school; a transition Group intervention for several Sixth Class pupils; Solution-focused pupil interview to get the child's voice; a full reassessment only where the current picture is out of date for the question being asked."),

 "next": J(
  "→ AFTER THE MEETING: circulate actions, owners and dates within a week; file consent for every document shared.",
  "→ BEFORE THE MOVE: check each action is done; confirm the receiving setting holds the Student Support File and one-page profile.",
  "→ WEEKS 2–6 AFTER: receiving setting reviews; you or your supervisor check in if the case stays open.",
  "→ IF IT IS GOING BADLY: early consultation with the receiving school; consider EBSA planning; escalate risk the same day if needed.",
  "→ POST-SCHOOL: confirm the DARE/CAO, FET or HSE profiling step is underway; confirm adult services contact has begun before closing (PSI 3.4.3).",
  "→ LOG IT: Log sheet — the Part D transition row for the band; Competencies 3 and 5. Preschool and school-leaver work is Early Years and Young Adult evidence only if planned in the Appendix 1 in advance."),

 "supervision": J(
  "BRING the now/next map and ask: 'What have I missed that will not transfer?'",
  "BRING the local facts you are unsure of — the NCSE process in this area, which post-primary schools have special classes, how HSE school-leaver profiling runs locally, this year's DARE rules. Your supervisor will know or know who does.",
  "ASK how your supervisor handles a parent who wants a placement or eligibility you cannot recommend — and practise the wording.",
  "BRING consent questions: who can consent at 16 and at 18; what can be shared without it.",
  "BRING the child's voice material and check it is theirs, not a paraphrase of the adults'.",
  "IF A RISK OR CHILD PROTECTION ISSUE AROSE around the transition, act the same day, then bring it."),

 "reflection": J(
  "WHAT GOOD LOOKS LIKE: 'I wrote a thorough report, but at the planning meeting the SEN coordinator said she would not see it until September. We agreed a one-page profile she would get in June and a check-in in week two. I now ask who will read what I send, and when, before I write it.'",
  "WHAT POOR LOOKS LIKE: 'Report sent to new school with parental consent. Transition should be supported.' — no map, no owners, no dates, no child voice, no review.",
  "PROMPT 1 — What did the child say they were worried about, and did it make it into the plan in their words?",
  "PROMPT 2 — Which support did I assume would continue, and did I check?",
  "PROMPT 3 — Whose job did I quietly take on because the system had a gap, and is that sustainable?",
  "PROMPT 4 — How did the family's resources shape what happened, and what did I do about it?",
  "CORU 5.44 — what are my own beliefs about 'good' post-school outcomes (college versus work versus day service), and whose goals did the plan serve?"),

 "timeline": J(
  "YEAR 1 — ROSCOMMON (03/02/2026–09/07/2026), DONE: check the Log sheet for any spring/summer transfer work; Sixth Class transfer is a common spring task.",
  "YEAR 1 — CAVAN (05/10/2026–18/12/2026): autumn is the planning season, not the transfer season. Useful work: Fifth/Sixth Class pupils whose post-primary applications are due; preschool children entering school in September 2027 (link with AIM and Mo Scéal); Leaving Certificate students applying via CAO/DARE by 01/02/2027 (check the 2027 dates). Early Years and Young Adult work counts for UCD Table 3 only if it is in the Appendix 1 before placement starts — plan it now.",
  "YEAR 2 — PRIMARY CARE AND DISABILITY: CDNT-to-adult and CAMHS-to-adult transitions; HSE school-leaver profiling; adaptive measures for adult services.",
  "YEAR 3: lead a transition plan end to end, including review after the move."),

 "citations": [
  "Bronfenbrenner, U. (1979). The ecology of human development: Experiments by nature and design. Harvard University Press.",
  "Rimm-Kaufman, S. E., & Pianta, R. C. (2000). An ecological perspective on the transition to kindergarten: A theoretical framework to guide empirical research. Journal of Applied Developmental Psychology, 21(5), 491–511.",
  "Smyth, E., McCoy, S., & Darmody, M. (2004). Moving up: The experiences of first-year students in post-primary education. Liffey Press / Economic and Social Research Institute.",
  "Evangelou, M., Taggart, B., Sylva, K., Melhuish, E., Sammons, P., & Siraj-Blatchford, I. (2008). What makes a successful transition from primary to secondary school? (Research Report DCSF-RR019). Department for Children, Schools and Families.",
  "Test, D. W., Mazzotti, V. L., Mustian, A. L., Fowler, C. H., Kortering, L., & Kohler, P. (2009). Evidence-based secondary transition predictors for improving postschool outcomes for students with disabilities. Career Development for Exceptional Individuals, 32(3), 160–181.",
  "McGuckin, C., Shevlin, M., Bell, S., & Devecchi, C. (2013). Moving to further and higher education: An exploration of the experiences of students with special educational needs (NCSE Research Report No. 14). National Council for Special Education.",
  "Health Service Executive. (2012). New directions: Review of HSE day services and implementation plan 2012–2016. HSE.",
  "Disability Access Route to Education. (2025). DARE handbook 2026. Irish Higher Education Institutions / CAO. https://accesscollege.ie",
 ],
}


METHODS = [GROUP_INTERVENTION, STAFF_TRAINING, TRANSITION_PLANNING]
