# CONDS batch c10 — written expression, tics, stereotypic movements.
# 1 Specific Learning Disorder with impairment in written expression (dysgraphia)
# 2 Tic disorders and Tourette's Disorder
# 3 Stereotypic Movement Disorder
# Context: Reference Part D, 1. LEARNING (1.4 Literacy row M512; 1.6 Co-ordination row M514).
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c10.py
# Stance: the EP describes, formulates, recommends and refers; does not diagnose medical or
# psychiatric conditions and does not advise on medication (PSI 2.2.2).

CORU = "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32"
PSI = "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8"
LAW = ("Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · "
       "Equal Status Acts 2000–2018 · GDPR / Data Protection Act 2018")

CIT_DSM = ("American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders "
           "(5th ed., text rev.). https://doi.org/10.1176/appi.books.9780890425787")
CIT_ICD = ("World Health Organization. (2019). International classification of diseases for mortality and "
           "morbidity statistics (11th revision). https://icd.who.int/ [Check codes against the current browser.]")
CIT_NEPS = ("National Educational Psychological Service. (2007). Special educational needs: A continuum of "
            "support — Guidelines for teachers. Department of Education and Science.")
CIT_DES17 = ("Department of Education and Skills. (2017). Guidelines for primary schools: Supporting pupils with "
             "special educational needs in mainstream schools. Department of Education and Skills.")

CONDS = []

# =====================================================================================
# 1. SPECIFIC LEARNING DISORDER — WRITTEN EXPRESSION
# =====================================================================================
CONDS.append({
 "name": "Specific Learning Disorder with impairment in written expression (dysgraphia)",
 "code": "DSM-5-TR Specific Learning Disorder, with impairment in written expression (F81.81) · ICD-11 6A03.1 Developmental learning disorder with impairment in written expression — check codes before quoting",
 "neps": "1. LEARNING (1.4 Literacy — reading, spelling, written expression) — and 1.6 Co-ordination where handwriting is the barrier",
 "coru": CORU,
 "psi": PSI,
 "law": LAW + " · State Examinations Commission RACE scheme (check current year's instructions)",

 "what_it_is": [
  "A DSM-5-TR Specific Learning Disorder (SLD) in which WRITTEN EXPRESSION is substantially and quantifiably below age expectation, has persisted for at least six months despite targeted intervention, began in the school years, and is not better explained by intellectual disability, sensory impairment, other neurological or mental disorder, language of instruction, or inadequate instruction (APA, 2022).",
  "DSM-5-TR lists three sub-skills under this specifier:\n▸ spelling accuracy\n▸ grammar and punctuation accuracy\n▸ clarity or organisation of written expression.\nNote what is NOT listed: handwriting. So poor handwriting on its own does not fit this specifier and points first to DCD or a motor explanation — an inference from the listed sub-skills, not a sentence to quote from the manual (APA, 2022).",
  "'Dysgraphia' is used in two incompatible ways, and you must know which one a report means:\n▸ TRANSCRIPTION dysgraphia — handwriting (legibility, speed, letter formation) and/or spelling. Berninger and Wolf (2016) use 'dysgraphia' for impaired handwriting.\n▸ COMPOSITION difficulty — generating, organising and revising ideas in written language; often language-based (DLD, 'OWL-LD' in Berninger & Wolf, 2016).",
  "The 'Simple View of Writing' (Berninger et al., 2002) is the working model: TRANSCRIPTION (handwriting + spelling) and EXECUTIVE functions (planning, reviewing) support TEXT GENERATION, all within working memory. If transcription is effortful, it uses the capacity that composition needs — so poor handwriting can make ideas look poor.",
  "In practice the question is always: WHERE in the writing process does it break down? Letter formation, handwriting speed, spelling, sentence construction, vocabulary, organisation of ideas, or getting started (executive / motivational). Each has a different recommendation.",
  "Specifiers: DSM-5-TR asks for severity (mild / moderate / severe) based on how much support is needed and whether accommodations allow the person to function (APA, 2022). A report that gives the specifier without describing the sub-skill profile is of little use in school.",
  "In Ireland, 'specific learning difficulty' (lower case, educational) and 'SLD' (DSM diagnosis) are used loosely and interchangeably. Access to supports in school depends on NEED under the Continuum of Support, not on a diagnostic label (NEPS, 2007; DES, 2017).",
 ],

 "what_it_is_not": [
  "NOT the same as messy handwriting. Poor handwriting alone is usually a motor (DCD) or instructional question. DSM-5-TR's written expression specifier covers spelling, grammar/punctuation and organisation, not handwriting (APA, 2022). Many reports use 'dysgraphia' for handwriting only — read carefully.",
  "NOT explained by 'not trying'. Writing is the most effortful school task; Connelly, Dockrell and Barnett (2005) showed slow handwriting constrained exam essay quality even in undergraduates. Output that is short or reluctant is often a capacity problem, not a motivation one.",
  "NOT diagnosable from one writing sample or one standardised score. DSM-5-TR requires persistence for six months DESPITE targeted intervention, and a clinical synthesis of history, school reports and standardised measures (APA, 2022). Ask what has been taught, for how long, and with what result.",
  "NOT separate from language. Weak oral language — vocabulary, syntax, narrative — shows up in writing. Children with DLD write less and with more errors (Dockrell, Lindsay & Connelly, 2009). A 'writing difficulty' may be a language disorder; compare oral and written versions of the same content.",
  "NOT fixed by a laptop alone. Assistive technology removes the handwriting barrier but not spelling, sentence construction or planning; and typing is itself a skill that has to be taught before it is faster than handwriting.",
  "NOT confined to children who also have dyslexia, though spelling difficulty is shared. A child can read adequately and still have a significant spelling or composition difficulty.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR gives 5–15% for Specific Learning Disorder across reading, writing and mathematics in school-age children across languages and cultures (APA, 2022). A separate figure for the written expression specifier is not stated here — check before quoting.",
  "IRELAND: no Irish population prevalence figure for written expression difficulty is cited here — check before quoting. School support caseloads reflect identification practice, not prevalence.",
  "CO-OCCURRENCE: written expression difficulty frequently co-occurs with reading difficulty (dyslexia), ADHD, DCD and DLD — rates vary by definition and sample; not stated here, check before quoting.",
  "SEX RATIO: boys are more often identified with writing difficulties; exact ratio not stated here — check before quoting.",
  "AGE: difficulties are visible from the start of formal writing, but identification often waits until demands rise (3rd–6th class, and again at Junior Cycle when extended writing and timed exams begin).",
  "DEFINITION DRIVES THE FIGURE: whether handwriting is included, and which cut-off is used, changes any rate dramatically. Always ask which definition a quoted figure used.",
 ],

 "cooccurring": [
  {"name": "DYSLEXIA (SLD WITH IMPAIRMENT IN READING)",
   "rate": "common — spelling difficulty is shared; rate not stated here, check",
   "presents": "Poor spelling constraining written output, with slow word reading. Spelling is shared ground; assess reading separately and say which difficulty drives the writing problem."},
  {"name": "DCD / DYSPRAXIA",
   "rate": "elevated — rate not stated here, check",
   "presents": "Slow, effortful, poorly formed handwriting with fatigue; ideas stronger orally than on paper. Use DASH and an OT view; a transcription difficulty may be motor rather than a learning disorder."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "Difficulty starting, planning and sustaining writing; careless errors; unfinished work. Executive demands of writing are high — separate 'can't organise' from 'can't transcribe'."},
  {"name": "DLD",
   "rate": "elevated (Dockrell et al., 2009) — rate not stated here, check",
   "presents": "Short texts, simple or ungrammatical sentences, limited vocabulary — mirrored in speech. This is a language disorder showing in writing; SLT involvement changes the recommendations."},
  {"name": "ANXIETY AND WRITING AVOIDANCE",
   "rate": "secondary; rate not stated here, check",
   "presents": "Refusal to start, tearing up work, toilet trips in writing lessons, 'I can't think of anything'. Often referred as behaviour. Ask what happens just before the avoidance."},
  {"name": "AUTISM",
   "rate": "writing difficulty reported — rate not stated here, check",
   "presents": "Difficulty with open-ended or imaginative writing prompts, perspective-taking in narrative, and handwriting. Structured, factual tasks may be much stronger — note the contrast."},
 ],

 "recommendations": [
  "NAME THE BREAKDOWN POINT. Write the profile, not the label: e.g. 'handwriting speed well below peers on DASH; spelling at a similar level to reading; oral composition well organised' → transcription, not composition. Every recommendation follows from this.",
  "IF TRANSCRIPTION (handwriting): explicit, short, frequent handwriting instruction — letter formation families and fluency practice. Santangelo and Graham (2016) found explicit handwriting instruction improved legibility and fluency and also the quality of writing. OT input where DCD is suspected.",
  "IF TRANSCRIPTION (spelling): structured, cumulative spelling instruction linked to phonics and morphology, not weekly lists memorised for a Friday test. Allow 'have a go' spelling in drafts so ideas are not censored by fear of error.",
  "IF COMPOSITION: teach planning and revising strategies explicitly. Self-Regulated Strategy Development (SRSD; Harris & Graham) has the strongest evidence among writing interventions in meta-analyses (Graham et al., 2012) — e.g. POW + TREE for opinion writing. Specify genre, mnemonic, and who models it.",
  "SCAFFOLDS in every classroom: graphic organisers, sentence starters, word banks, oral rehearsal before writing ('say it, then write it'), and separating drafting from editing. Mark content and spelling separately.",
  "TECHNOLOGY: touch-typing programme with daily short practice and a named adult; speech-to-text and word prediction trialled and evaluated (write what 'success' means before the trial). Do not recommend a device without a plan for teaching its use.",
  "REDUCE UNNECESSARY TRANSCRIPTION: printed notes rather than board copying; alternatives for showing learning (oral, diagrams, typed).",
  "RACE (post-primary): build evidence early — handwriting speed (DASH), spelling and a record of what is used in class. Eligibility for spelling/grammar waiver, word processor or reader/scribe is decided by the State Examinations Commission against its current criteria — check the current year's instructions; do not promise an outcome.",
  "CONTINUUM LEVEL: Classroom Support for scaffolds and marking changes; School Support for targeted handwriting, spelling or SRSD groups; School Support Plus where the profile is severe or co-occurring (OT, SLT, EP casework). Review every 6–8 weeks against a written sample.",
  "REFER: OT (HSE Primary Care or CDNT — check local route) where handwriting / motor difficulty is suspected; SLT where oral language is also weak; GP / optometry if vision is unchecked.",
  "DO NOT diagnose 'dysgraphia' from a handwriting sample, and do not recommend visual-perceptual or 'brain training' programmes as treatments for writing — train the writing skills themselves (Santangelo & Graham, 2016; Graham et al., 2012). PSI 4.2.2 applies.",
 ],

 "explain_parent": [
  "'Writing is one of the hardest things school asks of a child — you have to think of ideas, find the words, spell them, form the letters and remember what you were saying, all at once. For her, one or more of those steps takes so much effort that there's little left for the rest.'",
  "'For your son it's mainly the handwriting and spelling — the getting-it-onto-paper part. When he tells me the story, it's well organised and interesting. That tells us his ideas are there.'",
  "'It isn't laziness. Short or messy writing is often what happens when a child is working harder than everyone else.'",
  "'What helps is teaching the specific part that's hard — handwriting, spelling, or planning — directly and often, and letting her show what she knows in other ways in the meantime. Typing will help, but it has to be taught first.'",
  "'At home, let her tell you the story first and write down a few key words for her. Praise the ideas before the spelling.'",
  "SIGNPOST: Dyslexia Association of Ireland → https://dyslexia.ie/ (spelling and literacy); Dyspraxia/DCD Ireland → https://www.dyspraxia.ie/ (handwriting / motor) — check current services; HSE Primary Care or CDNT OT route via GP.",
 ],

 "explain_teacher": [
  "'Let's work out which part of writing is breaking down — handwriting speed, spelling, sentences, or organising ideas. Can you give me one piece of independent writing and tell me what he said about the same topic out loud?'",
  "'If the oral version is much better than the written one, the barrier is transcription — handwriting or spelling. Scaffold that, and reduce copying.'",
  "'If both oral and written versions are thin and disorganised, it's more likely language or planning — explicit strategy teaching like SRSD, graphic organisers and talk before writing will help more than a laptop.'",
  "'Please mark ideas and spelling separately. Red pen all over a page teaches a child that writing is where they fail.'",
  "'Start touch-typing now if handwriting is the barrier — it takes months to become faster than handwriting, and you'll need that record for RACE later.'",
  "'Keep dated samples every half term. That is the evidence that the support is working — or that we need to step up the Continuum.'",
 ],

 "explain_child": [
  "YOUNGER: 'Writing has lots of jobs at once — thinking, spelling, and making your hand do the letters. For you, the hand job (or the spelling job) is extra hard, so it uses up energy that should go on your great ideas. We're going to make that job easier.'",
  "OLDER: 'Your ideas are strong — you showed me that when you talked it through. The problem is getting them down fast enough and spelled right. Typing, planning sheets and a few strategies will let the marks show what you actually know.'",
  "ASK: 'When you have to write, which bit is hardest — thinking what to say, spelling, or your hand getting tired?' Children can usually tell you, and their answer often matches the assessment.",
  "ASK: 'What happens in your head when the teacher says \"write a story\"?' — gets at blank-page anxiety and planning difficulty.",
  "TRY TOGETHER: let them dictate a paragraph to you, then read it back. 'Those are YOUR words. That's how good your writing can be.'",
 ],

 "analogies": [
  "THE TOO-MANY-TABS LAPTOP: 'Writing is like running five programs at once. If handwriting is using most of the memory, the \"ideas\" program slows down.' Works with teachers and older pupils; explains why transcription limits composition (Berninger et al., 2002).",
  "WRITING WITH OVEN GLOVES ON: 'Imagine writing a great letter wearing oven gloves. Your message would look worse than it is.' Good with parents of children with transcription difficulty.",
  "THE BUILDER WITHOUT A PLAN: 'She has plenty of bricks — words and ideas — but no plan for the house, so the walls go up in the wrong order.' Good for composition / organisation difficulty; leads naturally to graphic organisers.",
  "SPEAKING IN A SECOND LANGUAGE: 'You know what you want to say, but you're so busy getting the grammar right that the point gets lost.' Good with adolescents and with teachers of Irish or modern languages.",
 ],

 "language": [
  "DSM-5-TR term: 'Specific Learning Disorder with impairment in written expression' (APA, 2022). ICD-11: 'developmental learning disorder with impairment in written expression' (WHO, 2019). 'Dysgraphia' is common in reports and among parents but has no single agreed meaning — define it every time you use it.",
  "Use 'transcription' (handwriting, spelling) and 'composition' / 'text generation' (ideas, language, organisation) as your working vocabulary — it makes recommendations obvious.",
  "In Irish school documents, 'specific learning difficulty' and 'SLD' may mean dyslexia, a general learning difficulty or a DSM diagnosis. Ask what the writer meant.",
  "Avoid 'lazy', 'untidy', 'careless' and 'poor effort' in reports, even when quoting. Describe what the writing looks like and under what conditions it was produced (PSI 1.2.8).",
 ],

 "red_flags": [
  "RED FLAG — LOSS of previously acquired writing or motor skill, new tremor, or deterioration in handwriting with other neurological signs. Not a learning disorder. Urgent GP / paediatric referral.",
  "RED FLAG — written content that discloses harm, self-harm, suicidal thinking or abuse (journals, stories, 'free writing'). Same-day risk / child protection route; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's own duty.",
  "RED FLAG — writing refusal with marked distress, school avoidance or low mood. Follow up the emotional presentation in its own right; do not treat it only as a literacy problem.",
  "BOUNDARY — the EP can identify a specific learning difficulty educationally and may, within service policy, describe a profile consistent with SLD. Motor (DCD) and language (DLD) diagnoses belong to OT/medical and SLT colleagues. Check your service's policy on using DSM-5-TR SLD language in reports. PSI 2.2.2.",
  "WATCH — vision and hearing. Unchecked vision, or reduced hearing affecting phonological learning, can masquerade as spelling or copying difficulty. Ask when they were last checked.",
  "WATCH — instruction history. A child who has moved schools, missed long periods, or is learning through Irish or EAL may have an opportunity gap, not a disorder. DSM-5-TR excludes inadequate instruction (APA, 2022).",
 ],

 "child_voice": [
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free, already in schools. Good because it gets at attitude to writing without asking about it directly. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "ORAL-VERSUS-WRITTEN TASK — ask the child to tell you, then write, the same short piece. Good because it is assessment and voice at once: the child sees their own ideas valued.",
  "WRITING ATTITUDE SCALING — 'How do you feel when the teacher says \"take out your copies\"?' on a 1–10 scale or faces. Good because avoidance often starts before a word is written.",
  "PUPIL-SELECTED PORTFOLIO — the child chooses the piece they are proudest of and the one they found hardest, and explains why. Good because it builds metacognition and self-advocacy for RACE and later accommodation.",
  "ASSISTIVE TECHNOLOGY TRIAL FEEDBACK — the young person rates speech-to-text or typing after two weeks. Good because the tool only helps if they will use it in front of peers.",
 ],

 "questions": [
  "Q: 'Is dysgraphia the same as dyslexia?' — A: 'No, though they often come together because spelling is part of both. Dyslexia is mainly about reading and spelling words. Written expression difficulty is about getting ideas down in writing — through handwriting, spelling, sentences or organisation.'",
  "Q: 'His handwriting is terrible — does he have dysgraphia?' — A: 'Handwriting on its own is usually a motor-skills question, and an OT is the right person to look at that. What I'll look at is whether the handwriting is getting in the way of him showing what he knows, and whether spelling or organising his ideas is also a difficulty.'",
  "Q: 'Should she just use a laptop?' — A: 'Probably, in time — but typing needs to be taught first, and a laptop won't fix spelling or planning. I'd start a typing programme now and keep teaching the writing strategies alongside.'",
  "Q: 'Will he get a spelling waiver in the Leaving Cert?' — A: 'That's decided by the State Examinations Commission against its current criteria, and the school makes the application. Keeping dated samples and handwriting-speed evidence from now on is the best thing we can do. I can't promise the outcome.'",
  "Q: 'Can you diagnose it?' — A: 'I can describe exactly where her writing breaks down and whether it fits the pattern of a specific learning difficulty, and in some services that's described in a report. Handwriting as a motor difficulty needs an OT, and language needs an SLT. I'll make those links if they're needed.'",
  "Q: 'Her stories are great when she tells them — why can't she write them?' — A: 'That's exactly the right question, and it's good news. It tells us the ideas and language are there; the bottleneck is getting them onto paper. That's the part we target.'",
  "Q: 'He won't write anything — is it behaviour?' — A: 'Sometimes, but usually it's avoidance of something that feels impossible. Let's look at what he can do when the writing load is taken away — if he produces good ideas orally, we know where to start.'",
 ],

 "supervision": [
  "Ask what the service's policy is on the EP using DSM-5-TR 'Specific Learning Disorder' language in reports, versus describing a specific learning difficulty educationally.",
  "Bring a writing sample with an oral-versus-written comparison and discuss how to write the transcription / composition profile.",
  "Discuss which WIAT-III UK writing subtests to use and how to report essay composition scores when handwriting speed is low.",
  "Clarify how RACE evidence is gathered in this area and what the EP's role is (usually advisory; the school applies).",
  "Bring a 'behaviour in writing lessons' referral and discuss the formulation of avoidance.",
 ],

 "reflection": [
  "ON THE DEFINITION — Did I say what I meant by 'dysgraphia', or did I let a report's loose use stand?",
  "ON THE BREAKDOWN POINT — Can I name where writing breaks down for this child, with evidence from more than one source (sample, test, oral comparison, teacher report)?",
  "ON INSTRUCTION — Did I establish what has been taught and for how long before I concluded a persistent difficulty?",
  "ON TECHNOLOGY — Did I recommend a device, or a plan for teaching and evaluating its use?",
  "ON THE CHILD — Did the child's ideas appear in my report, or only their errors?",
  "WHAT GOOD LOOKS LIKE: 'Oral retell well sequenced; written version a third of the length with simplified vocabulary; DASH free-writing speed well below age expectation. Transcription is the barrier. Recommendations: daily touch-typing, dictation for extended pieces, separate marking of content and spelling. Review in 8 weeks with a matched sample.'",
  "WHAT POOR LOOKS LIKE: 'Written expression is weak. Dysgraphia is likely. A laptop is recommended.' — undefined term, no profile, no teaching plan.",
 ],

 "citations": [
  CIT_DSM,
  "Berninger, V. W., & Wolf, B. J. (2016). Dyslexia, dysgraphia, OWL LD, and dyscalculia: Lessons from science and teaching (2nd ed.). Paul H. Brookes.",
  "Berninger, V. W., Vaughan, K., Abbott, R. D., Begay, K., Coleman, K. B., Curtin, G., Hawkins, J. M., & Graham, S. (2002). Teaching spelling and composition alone and together: Implications for the simple view of writing. Journal of Educational Psychology, 94(2), 291–304.",
  "Graham, S., McKeown, D., Kiuhara, S., & Harris, K. R. (2012). A meta-analysis of writing instruction for students in the elementary grades. Journal of Educational Psychology, 104(4), 879–896.",
  "Santangelo, T., & Graham, S. (2016). A comprehensive meta-analysis of handwriting instruction. Educational Psychology Review, 28(2), 225–265.",
  "Connelly, V., Dockrell, J. E., & Barnett, J. (2005). The slow handwriting of undergraduate students constrains overall performance in exam essays. Educational Psychology, 25(1), 99–107.",
  "Dockrell, J. E., Lindsay, G., & Connelly, V. (2009). The impact of specific language impairment on adolescents' written text. Exceptional Children, 75(4), 427–446.",
  "Barnett, A., Henderson, S. E., Scheib, B., & Schulz, J. (2007). Detailed Assessment of Speed of Handwriting (DASH). Pearson.",
  CIT_NEPS,
  CIT_ICD,
 ],

 "pathway": {
  "age": "Usually 8–12. Early writing is expected to be effortful, so difficulty is often not treated as persistent until 3rd–4th class, when writing becomes the main way of showing learning. A second wave is identified at Junior Cycle and before RACE applications, when extended timed writing exposes slow handwriting or weak organisation that strong oral ability had masked.",
  "who_diagnoses": "Ireland: the EP (NEPS or private) usually identifies a specific learning difficulty in literacy/writing educationally, and may use DSM-5-TR SLD language depending on service policy — check. Handwriting as a motor difficulty is assessed by OT (HSE Primary Care, CDNT or private); language by SLT. No medical diagnosis is required for school supports.",
  "who_wrote_report": "NEPS or private EP; school's special education teacher (standardised attainment tests); OT (handwriting / DCD); SLT (language); occasionally a psychiatrist or paediatrician using DSM-5-TR in a wider report. Check who used the word 'dysgraphia' and what they meant by it.",
  "refer_to": "Usually no external referral is needed — the response is school-based on the Continuum of Support. OT via Primary Care or CDNT if a motor difficulty is suspected; SLT if oral language is also weak; GP / optometry if vision is unchecked; GP urgently if any regression.",
  "sooner": "'Writing difficulties often only become obvious when the writing load goes up — it's very common for it to show up now rather than in the infant classes. What matters is that we know where it breaks down, so the support can be specific.'",
 },

 "differential": [
  "DCD / MOTOR DIFFICULTY — handwriting only, with other motor signs; OT question; handwriting is not one of the DSM-5-TR written-expression sub-skills.",
  "DLD — oral language as weak as written; SLT question; writing is the visible end of a language disorder.",
  "DYSLEXIA — spelling and word reading; assess reading separately.",
  "INADEQUATE INSTRUCTION OR OPPORTUNITY — school moves, absence, EAL or Irish-medium transition; exclusion under DSM-5-TR (APA, 2022).",
  "ATTENTION / EXECUTIVE DIFFICULTY — difficulty starting and sustaining writing, not transcription or language per se.",
  "VISION OR HEARING — copying and spelling errors that follow a sensory pattern; check.",
 ],

 "next": [
  "Collect a dated independent writing sample AND an oral version of the same content; compare.",
  "Establish instruction history — what has been taught, how, for how long, with what result.",
  "Assess the sub-skills that the comparison points to (handwriting speed, spelling, sentence and text level).",
  "Write targeted recommendations at the right Continuum level with a review date and a matched sample to compare.",
  "Refer to OT or SLT only where the profile shows motor or language difficulty beyond writing.",
 ],

 "presentations": [
  "Handwriting speed and legibility under time pressure",
  "Spelling as a barrier to written output",
  "Presentation and care of written work",
  "Fine motor difficulty (handwriting, pencil grip)",
  "Assistive technology not yet trialled",
  "Literacy difficulty not meeting SLD criteria",
  "Instruction history — what has actually been taught",
 ],

 "bands": {
  "Early Years": {
   "applies": "N/A — formal writing has not started; SLD requires difficulty persisting despite instruction in the school years (APA, 2022)",
   "prevalence": "Not applicable at this age — no diagnosis made.",
   "see": "Watch for early markers rather than label: pencil grasp and fine motor difficulty, poor interest in mark-making, weak phonological awareness, and language delay. Refer early for language (SLT) or motor (OT) concerns; these are the roots of later writing difficulty.",
   "tools": ["Beery VMI", "Movement ABC-2", "Ages & Stages Questionnaires (ASQ-3)"],
  },
  "School Age": {
   "applies": "YES — main identification window (3rd–6th class)",
   "prevalence": "Within DSM-5-TR's 5–15% for all SLD (APA, 2022); written expression figure not stated here — check.",
   "see": "Short, effortful written work that falls far below oral ability; poor spelling in free writing despite passing weekly spelling tests; run-on or fragmented sentences; difficulty starting; slow copying; avoidance in writing lessons. Often referred as work avoidance.",
   "tools": ["WIAT-III UK", "DASH", "Beery VMI", "Phonological Assessment Battery (PhAB2)", "CELF-5 UK", "WISC-V UK"],
  },
  "Adolescent": {
   "applies": "YES — exam access and subject demands dominate",
   "prevalence": "Persistence into adolescence is common — rate not stated here, check.",
   "see": "Handwriting speed limits exam answers; essays short or disorganised; poor spelling across subjects; avoidance of homework and written tasks; frustration or disengagement. RACE evidence and assistive technology become priorities; self-advocacy matters.",
   "tools": ["WIAT-III UK", "DASH", "Access arrangements evidence (RACE)", "WRAT-5"],
  },
  "Young Adult": {
   "applies": "YES — relevant to further and higher education access",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Note-taking and assignment writing under time pressure; reliance on assistive technology; may first be identified at third level. EP role usually limited to access evidence; refer to college disability service.",
   "tools": ["DASH-17+", "WAIS-IV UK", "WRAT-5"],
  },
  "Special Setting": {
   "applies": "RARELY — as a separate diagnosis; writing difficulty is usually part of a broader profile (ID, autism, physical disability)",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "The question is usually access: alternative recording (scribing, symbols, AAC, keyboard), and whether writing goals are functional. SLD is only relevant where the difficulty exceeds what the broader profile explains.",
   "tools": ["Vineland-3 / ABAS-3", "Beery VMI", "Communication Matrix / AAC review"],
  },
 },
})

# =====================================================================================
# 2. TIC DISORDERS AND TOURETTE'S DISORDER
# =====================================================================================
CONDS.append({
 "name": "Tic disorders and Tourette's Disorder",
 "code": "DSM-5-TR Tourette's Disorder (F95.2) · Persistent (Chronic) Motor or Vocal Tic Disorder (F95.1) · Provisional Tic Disorder (F95.0) · ICD-11 8A05 Tic disorders (8A05.0 Primary tics or tic disorders: 8A05.00 Tourette syndrome · 8A05.01 Chronic motor tic disorder · 8A05.02 Chronic phonic tic disorder · 8A05.03 Transient motor tics) — classified under Diseases of the nervous system and cross-listed with neurodevelopmental disorders; check sub-codes before quoting",
 "neps": "1. LEARNING (1.6 Co-ordination) — and 3. EMOTIONAL / 4. SOCIAL where co-occurring anxiety, OCD or peer difficulty dominate",
 "coru": CORU,
 "psi": PSI,
 "law": LAW,

 "what_it_is": [
  "TICS are sudden, rapid, recurrent, non-rhythmic motor movements or vocalisations (APA, 2022). SIMPLE tics: blinking, grimacing, shoulder shrugging, sniffing, throat clearing. COMPLEX tics: sequences of movements, touching, jumping, words or phrases, echolalia, and (in a minority) coprolalia.",
  "DSM-5-TR tic disorders, all with onset before 18 and not attributable to a substance or other medical condition (APA, 2022):\n▸ TOURETTE'S DISORDER — multiple motor tics AND at least one vocal tic, not necessarily at the same time, persisting more than 1 year since first tic onset.\n▸ PERSISTENT (CHRONIC) MOTOR OR VOCAL TIC DISORDER — motor OR vocal tics, not both, for more than 1 year.\n▸ PROVISIONAL TIC DISORDER — tics present for less than 1 year.",
  "Tics WAX AND WANE: they change in type, frequency and severity over weeks and months, often with no obvious reason. A new tic replacing an old one is typical, not a sign of deterioration.",
  "Most people feel a PREMONITORY URGE — an uncomfortable sensation (itch, pressure, tension) that the tic relieves. Tics can often be SUPPRESSED briefly, which is why they are mistaken for voluntary behaviour; suppression takes effort and attention away from learning.",
  "Tics typically worsen with stress, excitement, tiredness and — for many — relaxation after holding them in all day (e.g. after school); they may reduce during focused, engaging activity — widely reported in clinical guidance (e.g. Andrén et al., 2022); pattern varies between individuals.",
  "Typical course: onset around 4–6 years, peak severity around 10–12 years, with improvement in adolescence for many (Leckman et al., 1998). A substantial minority continue into adulthood — check the proportion before quoting.",
  "The impact in school often comes less from the tics themselves than from CO-OCCURRING conditions (ADHD, OCD, anxiety, learning difficulty) and from peer and adult reactions (Hirschtritt et al., 2015).",
 ],

 "what_it_is_not": [
  "NOT mainly about swearing. Coprolalia affects a minority of people with Tourette's — exact proportion not stated here, check before quoting. Media portrayal has made it the popular image; most tics are simple motor and vocal tics.",
  "NOT deliberate, attention-seeking or 'a habit'. Tics are neurological. Brief suppression is possible but effortful, and asking a child to 'stop it' increases stress and often tics.",
  "NOT rare in its transient form. Brief tics in childhood are common and many resolve within a year (Provisional Tic Disorder) — rate varies widely by study; check before quoting. A single tic is not a reason for alarm or a diagnosis.",
  "NOT treated by ignoring the child — but also NOT improved by drawing attention to tics. The balance is: don't comment on tics, do respond to the child's needs (breaks, a safe space, peer education if the child wants it).",
  "NOT the same as FUNCTIONAL TIC-LIKE BEHAVIOURS. A marked rise in sudden-onset, complex, tic-like movements and vocalisations, mainly in adolescent girls and often linked to social media exposure, was reported from 2020 (Heyman et al., 2021; Pringsheim et al., 2021). These differ in onset, course and management — a specialist question, not an EP diagnosis.",
  "NOT something that always needs medication. First-line treatment where tics cause impairment is BEHAVIOURAL — CBIT / habit reversal — with medication decided by a doctor (Pringsheim et al., 2019; Andrén et al., 2022). The EP does not advise on medication (PSI 2.2.2).",
 ],

 "prevalence": [
  "TOURETTE'S: Knight et al. (2012), meta-analysis, estimated about 0.77% of children; Scharf et al. (2015), meta-analysis, gave a range of roughly 0.3–0.9% across studies — check both before quoting.",
  "PROVISIONAL / TRANSIENT TICS: common in school-age children; published figures vary widely by method — not stated here, check before quoting.",
  "IRELAND: no Irish population prevalence study is cited here — check before quoting.",
  "SEX RATIO: more boys than girls, commonly cited around 3–4:1 for Tourette's (APA, 2022 notes a male predominance) — check exact ratio before quoting. Functional tic-like behaviours show the opposite pattern (mostly adolescent girls; Pringsheim et al., 2021).",
  "CO-OCCURRENCE: Hirschtritt et al. (2015), in a large clinical sample, found most people with Tourette's had at least one co-occurring psychiatric condition, most commonly ADHD and OCD (roughly half each) — check exact figures before quoting. Clinical samples overstate population rates.",
  "AGE: onset typically 4–6, peak around 10–12, improvement in adolescence for many (Leckman et al., 1998).",
 ],

 "cooccurring": [
  {"name": "ADHD",
   "rate": "around half in clinical samples (Hirschtritt et al., 2015) — check before quoting",
   "presents": "Impulsivity, restlessness and inattention that often cause more school impairment than the tics. Assess separately; attention difficulty is not 'distraction by tics'."},
  {"name": "OCD AND OBSESSIVE-COMPULSIVE BEHAVIOURS",
   "rate": "around half in clinical samples (Hirschtritt et al., 2015) — check before quoting",
   "presents": "Need for things to feel 'just right', evening-up, repeated touching, checking. Can be hard to separate from complex tics; CAMHS question. Ask what the urge is for — tics relieve a sensation; compulsions reduce anxiety about a feared outcome."},
  {"name": "ANXIETY",
   "rate": "elevated — rate not stated here, check",
   "presents": "Anticipatory worry about tics in class, exams, or social situations; stress increases tics, which increases worry. A cycle worth formulating."},
  {"name": "LEARNING DIFFICULTIES / HANDWRITING",
   "rate": "elevated — rate not stated here, check",
   "presents": "Slow written work, especially when hand or arm tics interfere; difficulty sustaining attention while suppressing. Assess learning separately."},
  {"name": "AUTISM",
   "rate": "elevated — rate not stated here, check",
   "presents": "Tics alongside stereotypies and repetitive behaviours; distinguishing them needs careful description (onset, rhythmicity, urge, function). Specialist question."},
  {"name": "ANGER / RAGE ATTACKS AND LOW MOOD",
   "rate": "reported in clinical samples — rate not stated here, check",
   "presents": "Explosive outbursts, often at home after holding tics and demands in all day; low mood in adolescence linked to teasing and self-image. Screen for mood and risk."},
 ],

 "recommendations": [
  "DO NOT DRAW ATTENTION TO TICS. Staff do not comment, imitate, ask the child to stop or react visibly. This is the single most important recommendation in most reports; write it plainly.",
  "PLAN FOR SUPPRESSION COSTS: a discreet 'time-out' card or agreed signal to leave the room briefly; a safe space to release tics; seating near the door or at the back if the child prefers. Tired, tic-heavy afternoons may need lighter demands.",
  "PEER EDUCATION ONLY WITH CONSENT: a class talk about tics can transform peer reactions, but only if the young person (and parents) want it and have a say in content. Some prefer privacy.",
  "EXAMS AND ASSESSMENT: for school exams, a separate room and rest breaks may help; for State examinations, the school applies to the SEC under RACE — check current criteria for what is available for tic disorders. Oral work and presentations may need adjustment.",
  "ADDRESS CO-OCCURRING NEEDS: ADHD, OCD, anxiety and learning difficulties often matter more than the tics; each needs its own assessment and plan.",
  "BULLYING: name it in the plan — Tourette's is a common target of teasing. The school's anti-bullying procedures apply; monitor break times.",
  "BEHAVIOURAL THERAPY (CBIT / habit reversal training, exposure and response prevention for tics) is recommended first-line where tics cause impairment (Pringsheim et al., 2019; Andrén et al., 2022). It is delivered by TRAINED clinicians (CAMHS, psychology services, some private practitioners). The EP can recommend referral, not deliver it without training.",
  "CONTINUUM LEVEL: Classroom Support for staff awareness and adjustments; School Support where tics affect learning or peer relationships; School Support Plus with CAMHS / paediatric involvement or significant co-occurring conditions.",
  "REFER: GP → paediatrics / paediatric neurology for diagnosis and review; CAMHS where OCD, significant anxiety, low mood or self-injurious tics are present (check local acceptance criteria); psychology for CBIT where available.",
  "DO NOT recommend reward charts for tic-free periods, punishment for tics, or 'tic-free' goals set by the school. DO NOT advise on medication. PSI 2.2.2.",
 ],

 "explain_parent": [
  "'Tics are movements or sounds that the brain produces on its own, usually with an itchy or uncomfortable feeling beforehand that the tic relieves. They're not a habit and they're not naughtiness.'",
  "'They come and go — you'll see weeks when they're worse, and a tic that disappears and a new one that turns up. That's the normal pattern, not a sign things are getting worse.'",
  "'He can sometimes hold them in for a while, which is why school may not see much. That takes a lot of effort, and it often all comes out when he gets home. That's a sign he feels safe with you.'",
  "'Many children's tics are at their worst around 10–12 and settle in the teenage years (Leckman et al., 1998). For those who need more, there is a behavioural therapy called CBIT that has good evidence, delivered by trained clinicians.'",
  "'What often matters more for school are things that come with tics — attention, worries, or needing things to feel just right. Those deserve their own attention.'",
  "SIGNPOST: GP for referral to paediatrics; Tourette's Support NI & ROI → https://tourettessupportni.org/ ; Tourettes Action (UK) school resources → https://www.tourettes-action.org.uk/ ; the Tourette Syndrome Association of Ireland was the older Irish charity but current activity is not confirmed — check which Irish organisation is currently active before signposting.",
 ],

 "explain_teacher": [
  "'Please don't comment on tics, look at the child when they happen, or ask him to stop. Attention and stress tend to make them worse.'",
  "'He may be holding tics in during class, which takes real effort and leaves less for learning. A discreet signal to step out for a couple of minutes helps.'",
  "'Tics wax and wane — a bad week is not him being difficult. If there's a sudden change, let the family know rather than assuming it's behavioural.'",
  "'Vocal tics in a quiet test or assembly can be mortifying. Plan ahead: a seat near the door, or a separate room for tests.'",
  "'If the class asks, a simple answer works: \"It's called a tic — it's something his brain does, it's not catching, and the kind thing is to ignore it.\" Only do a class talk if he's agreed to it.'",
  "'Watch the yard and changing rooms. Teasing about tics is common and he may not tell you.'",
 ],

 "explain_child": [
  "YOUNGER: 'Tics are like a sneeze or a hiccup — your body does them by itself. Sometimes you get a funny feeling first. It's not your fault and you're not in trouble for them.'",
  "OLDER: 'Tics come from how the brain handles movement and urges. Lots of people have them, and they often get easier in the teenage years. Holding them in is tiring — it's okay to have a plan for when you need a break.'",
  "ASK: 'Do you get a feeling before a tic? What's it like?' — respects their expertise and helps later work if they're referred for CBIT.",
  "ASK: 'Who in school knows about your tics? Who would you like to know? Is there anything you'd like teachers to do, or stop doing?'",
  "ASK: 'Has anyone said anything about your tics that upset you?' — children often don't volunteer teasing.",
 ],

 "analogies": [
  "THE SNEEZE: 'Try to hold in a sneeze — you can for a bit, but the urge builds until it comes out, often bigger.' Works with teachers, parents and children; explains premonitory urge and suppression cost.",
  "THE MOSQUITO BITE: 'Being told not to scratch an itch doesn't make it go away — it's all you can think about.' Good for explaining why 'stop it' makes things worse.",
  "THE WEATHER: 'Tics are like weather — there are stormy weeks and calm weeks, and you can't always tell why.' Good with parents for waxing and waning.",
  "HOLDING YOUR BREATH: 'You can hold it for a while, but you can't do your maths at the same time.' Good for teachers — explains why suppression affects learning.",
 ],

 "language": [
  "'Tourette's', 'Tourette syndrome' (ICD-11, WHO, 2019) and 'Tourette's Disorder' (DSM-5-TR, APA, 2022) are all used. 'Tic disorder' is the umbrella term.",
  "Say 'tics', not 'twitches', 'habits' or 'noises'. Avoid 'suffers from Tourette's'.",
  "Avoid jokes or casual references to swearing — they reinforce the stereotype the young person lives with.",
  "Many young people and adults prefer 'I have Tourette's' or 'I'm a person with tics'; ask them.",
 ],

 "red_flags": [
  "RED FLAG — SUDDEN ONSET of many complex tics or tic-like attacks, especially in an adolescent, with rapid escalation. May be functional tic-like behaviour or another neurological condition (Pringsheim et al., 2021). Prompt GP / paediatric referral; do not label.",
  "RED FLAG — tics causing self-injury (e.g. head-hitting, eye-poking, violent neck jerks) or pain. Medical review; CAMHS / neurology as appropriate.",
  "RED FLAG — low mood, hopelessness, self-harm or suicidal talk in a young person with tics, especially if bullied. Same-day risk route; follow service protocol; CAMHS.",
  "RED FLAG — sudden dramatic onset of OCD symptoms and/or tics with other acute changes (eating restriction, regression, urinary symptoms) after an infection. Medical question (PANDAS/PANS is a contested, specialist area) — GP / paediatrics; do not speculate.",
  "BOUNDARY — diagnosis is made by a paediatrician, neurologist or psychiatrist. Medication is a medical decision. CBIT is delivered by trained clinicians. The EP describes impact, formulates, recommends and refers. PSI 2.2.2.",
  "WATCH — punishment for tics in school (detentions, removal from class for 'noises'). Name it and address it; it breaches the child's right to reasonable accommodation (Equal Status Acts 2000–2018 — check with the school's policy).",
 ],

 "child_voice": [
  "TIC DIARY OR RATING (with the child, not about them) — the young person records when tics are better or worse over a fortnight. Good because it identifies stress points in the day and gives the child ownership; also useful if referred for CBIT.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — Irish, free. Good because it surfaces peer and classroom concerns without focusing on tics. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "ONE-PAGE PROFILE written with the child — 'what people like about me / what's important to me / how to support me' including what staff should do when tics happen. Good because it puts the child's own instructions in front of staff.",
  "SCALING 'how hard is it holding tics in' across lessons on a 1–10 scale. Good because suppression effort is invisible to staff and the child can show where it is highest.",
  "YOUNG PEOPLE'S MATERIALS from Tourettes Action (UK) → https://www.tourettes-action.org.uk/ — good for self-understanding and deciding what to tell peers (check suitability for an Irish audience).",
 ],

 "questions": [
  "Q: 'Can't he just stop?' — A: 'He can sometimes hold them in for a short while, but it's like holding in a sneeze — it takes effort and the urge builds. Asking him to stop usually makes things harder.'",
  "Q: 'Will it get worse?' — A: 'Tics usually come and go. For many children they're at their most noticeable around 10–12 and ease in the teenage years (Leckman et al., 1998). The doctor following him can give you a better picture for him.'",
  "Q: 'Should he be on medication?' — A: 'That's a decision for his doctor, not me. What I can say is that the guidelines recommend behavioural therapy — CBIT — as a first option when tics are causing difficulty, and I can recommend a referral for that.'",
  "Q: 'Should we tell the class?' — A: 'Only if he wants to. For some children a short explanation makes a huge difference to how others react; others want privacy. Let's ask him and plan it together.'",
  "Q: 'Can you diagnose Tourette's?' — A: 'No, that's done by a paediatrician or neurologist. I can describe how the tics and anything alongside them are affecting school, and help the school respond.'",
  "Q: 'Is this caused by stress at home?' — A: 'No. Tics are neurological. Stress, excitement and tiredness can make them more noticeable, which is why they're often worse after school — that's not a sign that home is the problem.'",
  "Q: 'She suddenly has lots of tics after watching videos online — is it Tourette's?' — A: 'Sudden onset of complex tic-like movements in a teenager can be something different, which specialists call functional tic-like behaviours. It needs a medical assessment — please see the GP soon. It's real and it's treatable.'",
 ],

 "supervision": [
  "Clarify the local pathway for tic assessment — GP → paediatrics or paediatric neurology — and where CBIT is available (CAMHS, psychology, private), if anywhere locally.",
  "Discuss how to separate complex tics from compulsions or stereotypies when writing a descriptive report.",
  "Bring a case where the school's behaviour policy was being applied to vocal tics, and plan how to raise it.",
  "Discuss whether you should seek CBIT training later in your career, and what competence is required before delivering it (PSI competence boundaries).",
  "Discuss how to respond to a request for a class talk: consent, content, who delivers it.",
 ],

 "reflection": [
  "ON ATTENTION TO TICS — Did I write 'do not draw attention to tics' clearly enough that a substitute teacher would act on it?",
  "ON CO-OCCURRENCE — Did I look beyond the tics to attention, anxiety, OCD and learning, or did the tics take over the report?",
  "ON THE CHILD'S VOICE — Did I ask the young person what they want staff and peers to know, or decide for them?",
  "ON THE BOUNDARY — Did I stay clear of medication and diagnosis, and refer for CBIT rather than suggest I could deliver it?",
  "ON STEREOTYPE — Did any part of my conversation with staff assume swearing or deliberate behaviour?",
  "WHAT GOOD LOOKS LIKE: 'Staff agreed not to comment on tics and introduced a discreet exit card; the pupil rated suppression effort highest in Irish and maths before lunch, so those lessons were moved to include a movement break. Referral for CBIT via GP recommended; ADHD screen planned separately.'",
  "WHAT POOR LOOKS LIKE: 'Pupil has Tourette's. Staff should be understanding.' — no specific actions, no co-occurrence, no child voice.",
 ],

 "citations": [
  CIT_DSM,
  "Leckman, J. F., Zhang, H., Vitale, A., Lahnin, F., Lynch, K., Bondi, C., Kim, Y.-S., & Peterson, B. S. (1998). Course of tic severity in Tourette syndrome: The first two decades. Pediatrics, 102(1), 14–19.",
  "Knight, T., Steeves, T., Day, L., Lowerison, M., Jette, N., & Pringsheim, T. (2012). Prevalence of tic disorders: A systematic review and meta-analysis. Pediatric Neurology, 47(2), 77–90.",
  "Scharf, J. M., Miller, L. L., Gauvin, C. A., Alabiso, J., Mathews, C. A., & Ben-Shlomo, Y. (2015). Population prevalence of Tourette syndrome: A systematic review and meta-analysis. Movement Disorders, 30(2), 221–228.",
  "Hirschtritt, M. E., Lee, P. C., Pauls, D. L., Dion, Y., Grados, M. A., Illmann, C., King, R. A., Sandor, P., McMahon, W. M., Lyon, G. J., Cath, D. C., Kurlan, R., Robertson, M. M., Osiecki, L., Scharf, J. M., Mathews, C. A., & the Tourette Syndrome Association International Consortium for Genetics. (2015). Lifetime prevalence, age of risk, and genetic relationships of comorbid psychiatric disorders in Tourette syndrome. JAMA Psychiatry, 72(4), 325–333.",
  "Piacentini, J., Woods, D. W., Scahill, L., Wilhelm, S., Peterson, A. L., Chang, S., Ginsburg, G. S., Deckersbach, T., Dziura, J., Levi-Pearl, S., & Walkup, J. T. (2010). Behavior therapy for children with Tourette disorder: A randomized controlled trial. JAMA, 303(19), 1929–1937.",
  "Pringsheim, T., Okun, M. S., Müller-Vahl, K., Martino, D., Jankovic, J., Cavanna, A. E., Woods, D. W., Robinson, M., Jarvie, E., Roessner, V., Oskoui, M., Holler-Managan, Y., & Piacentini, J. (2019). Practice guideline recommendations summary: Treatment of tics in people with Tourette syndrome and chronic tic disorders. Neurology, 92(19), 896–906.",
  "Andrén, P., Jakubovski, E., Murphy, T. L., Woitecki, K., Tarnok, Z., Zimmerman-Brenner, S., van de Griendt, J., Debes, N. M., Viefhaus, P., Robinson, S., Roessner, V., Ganos, C., Szejko, N., Müller-Vahl, K. R., Cath, D., Hartmann, A., & Verdellen, C. (2022). European clinical guidelines for Tourette syndrome and other tic disorders — version 2.0. Part II: Psychological interventions. European Child & Adolescent Psychiatry, 31(3), 403–423. [Check for updates.]",
  "Heyman, I., Liang, H., & Hedderly, T. (2021). COVID-19 related increase in childhood tics and tic-like attacks. Archives of Disease in Childhood, 106(5), 420–421.",
  "Pringsheim, T., Ganos, C., McGuire, J. F., Hedderly, T., Woods, D., Gilbert, D. L., Piacentini, J., Dale, R. C., & Martino, D. (2021). Rapid onset functional tic-like behaviors in young females during the COVID-19 pandemic. Movement Disorders, 36(12), 2707–2713. [Check author list before quoting.]",
 ],

 "pathway": {
  "age": "Tics usually begin around 4–6 years; diagnosis of Tourette's needs tics for more than a year, so it is commonly confirmed around 6–10, often when tics peak (around 10–12; Leckman et al., 1998). Milder presentations may never be formally diagnosed. Sudden adolescent onset of complex tic-like behaviour is a different question and needs prompt medical review.",
  "who_diagnoses": "Ireland: paediatrician (hospital or community), paediatric neurologist, or child psychiatrist (CAMHS) — usually via GP referral. CAMHS involvement is more likely where OCD, anxiety or mood difficulties are prominent (check local acceptance criteria). CDNT may be involved where there are complex co-occurring disabilities.",
  "who_wrote_report": "Paediatrician or paediatric neurologist; CAMHS psychiatrist or psychologist; private psychiatrist; occasionally a GP letter. The EP report describes school impact and co-occurring learning or emotional needs, not the tic diagnosis.",
  "refer_to": "GP (for paediatric / neurology referral); CAMHS where OCD, anxiety, low mood or self-harm are present; psychology services offering CBIT (check what exists locally); urgent GP review for sudden-onset or self-injurious tics.",
  "sooner": "'Tics very often come and go for a while before anyone is sure what they are, and a diagnosis needs them to have been there for over a year. Waiting to see was reasonable. What matters now is that school knows how to respond.'",
 },

 "differential": [
  "FUNCTIONAL TIC-LIKE BEHAVIOURS — sudden onset, often adolescent girls, complex from the start, social media link reported (Pringsheim et al., 2021); specialist assessment.",
  "COMPULSIONS (OCD) — driven by anxiety or a feared outcome rather than a sensory urge; CAMHS question.",
  "STEREOTYPIES — earlier onset (often under 3), rhythmic, longer episodes, often with excitement or absorption, usually no premonitory urge (Singer, 2009).",
  "OTHER MOVEMENT DISORDERS OR SEIZURES — medical question; any loss of awareness, regression or new neurological sign → GP urgently.",
  "MEDICATION OR SUBSTANCE EFFECTS — exclusion criterion (APA, 2022); a doctor's question.",
  "HABITS AND FIDGETING — not experienced as an urge and easily stopped; describe rather than label.",
 ],

 "next": [
  "Describe the tics (type, frequency, when better and worse) from teacher, parent and child, without making the child the centre of attention.",
  "Write the 'do not draw attention' plan with specific adjustments and a named adult.",
  "Screen for co-occurring ADHD, anxiety, OCD, learning difficulty and bullying; assess or refer as needed.",
  "Recommend GP → paediatric referral if not already diagnosed, and CBIT where tics impair and a service exists.",
 ],

 "presentations": [
  "Fine motor difficulty (handwriting, pencil grip)",
  "Anticipatory anxiety about transitions",
  "Performance anxiety in oral work",
  "Test and exam anxiety",
  "Peer relationship difficulties and social isolation",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — tics often begin at 4–6 but a Tourette's diagnosis needs over a year of tics",
   "prevalence": "Transient tics common at this age — rate not stated here, check.",
   "see": "Blinking, grimacing, sniffing or throat clearing that parents notice before school does. Usually monitored rather than diagnosed. Reassure, avoid attention to tics, and advise GP review if persistent or distressing.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "SDQ (2–4 version)"],
  },
  "School Age": {
   "applies": "YES — main diagnosis window; tics usually at their peak",
   "prevalence": "Tourette's about 0.77% of children (Knight et al., 2012) — check before quoting.",
   "see": "Motor and vocal tics that wax and wane; suppression in class with release at home; teasing; co-occurring attention difficulty, worries or 'just right' behaviours; handwriting interference from hand tics. Often referred for 'noises' or behaviour.",
   "tools": ["Conners-4", "SDQ", "RCADS", "BRIEF-2", "WIAT-III UK", "DASH"],
  },
  "Adolescent": {
   "applies": "YES — tics ease for many; co-occurring conditions and social impact dominate; watch for sudden-onset functional tic-like behaviours",
   "prevalence": "Improvement in adolescence for many (Leckman et al., 1998); persistence rate not stated here — check.",
   "see": "Self-consciousness, avoidance of oral work, exam worries, low mood; OCD or anxiety may become more prominent than tics. Sudden onset of complex tic-like attacks in an adolescent girl warrants prompt medical review.",
   "tools": ["RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "Conners-4 self-report", "Access arrangements evidence (RACE)", "Beck Youth Inventories-2"],
  },
  "Young Adult": {
   "applies": "YES — a minority continue with tics into adulthood",
   "prevalence": "Adult persistence rate not stated here — check.",
   "see": "Tics may persist in a milder form; the impact is on further education, employment and social confidence. EP role limited to educational access; refer to adult services.",
   "tools": ["Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — but distinguishing tics from stereotypies and other repetitive behaviours is harder",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Tics may co-exist with stereotypies, self-injury or autism-related repetitive behaviour. Describe carefully (onset, rhythm, urge, function) and leave the classification to the medical team.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3"],
  },
 },
})

# =====================================================================================
# 3. STEREOTYPIC MOVEMENT DISORDER
# =====================================================================================
CONDS.append({
 "name": "Stereotypic Movement Disorder",
 "code": "DSM-5-TR Stereotypic Movement Disorder (F98.4; specify with / without self-injurious behaviour) · ICD-11 6A06 Stereotyped movement disorder (6A06.0 without self-injury · 6A06.1 with self-injury) — check codes before quoting (6A04 is DCD, not SMD)",
 "neps": "1. LEARNING (1.6 Co-ordination) — and 2. BEHAVIOUR where self-injury or disruption is the referral",
 "coru": CORU,
 "psi": PSI,
 "law": LAW + " · Department of Education guidance on restrictive practices (check current version)",

 "what_it_is": [
  "Repetitive, seemingly driven and apparently purposeless motor behaviour — e.g. hand shaking or waving, body rocking, head banging, self-biting, hitting own body — that interferes with social, academic or other activities or may result in self-injury, with onset in the early developmental period (APA, 2022).",
  "DSM-5-TR requires that it is not attributable to a substance or neurological condition and not better explained by another neurodevelopmental or mental disorder (APA, 2022). Specifiers:\n▸ WITH or WITHOUT SELF-INJURIOUS BEHAVIOUR\n▸ ASSOCIATED WITH a known medical or genetic condition, neurodevelopmental disorder or environmental factor\n▸ SEVERITY — mild (easily suppressed), moderate (needs explicit protective measures and behavioural modification), severe (continuous monitoring and protective measures to prevent serious injury).",
  "Stereotypies are COMMON in autism and intellectual disability, and are part of autism criterion B. When autism is present, a separate SMD diagnosis is usually reserved for stereotypies that cause self-injury or become a focus of treatment (APA, 2022 — check wording before quoting).",
  "They also occur in TYPICALLY DEVELOPING children ('primary' or 'complex motor stereotypies'): e.g. arm flapping or hand waving when excited or absorbed, starting before age 3, often persisting (Harris et al., 2008; Singer, 2009).",
  "Stereotypies typically serve a FUNCTION for the person — regulation, sensory input, expressing excitement, coping with boredom or stress, blocking out overload. Many autistic adults describe 'stimming' as useful and self-regulating (Kapp et al., 2019).",
  "SELF-INJURIOUS stereotypy is a different clinical matter: it can cause lasting harm (eye injury, head injury, skin damage). In children with developmental disability, self-injury is more common in certain genetic syndromes and with greater degree of disability (Oliver & Richards, 2015).",
 ],

 "what_it_is_not": [
  "NOT a problem to be stopped just because it looks unusual. Harmless stereotypy that does not interfere with learning or relationships should not be suppressed; suppression can increase distress and remove a regulation strategy (Kapp et al., 2019). The question is IMPACT, not appearance.",
  "NOT tics. Stereotypies usually start earlier (often under 3), are rhythmic and patterned, last longer per episode, occur with excitement or absorption, and usually lack a premonitory urge; tics are sudden, brief, variable and wax and wane (Singer, 2009).",
  "NOT necessarily a sign of autism. Primary motor stereotypies occur in children with typical development; autism needs the full social-communication picture (Harris et al., 2008).",
  "NOT 'attention-seeking' by default. Self-injury and stereotypy can be maintained by social attention, escape from demands, sensory (automatic) reinforcement, or pain — the function must be ASSESSED, not assumed (Hanley et al., 2003).",
  "NOT solved by restraint, protective equipment or punishment as a first response. Restrictive practices carry physical and psychological risk and must follow current policy, be a last resort, and be recorded (check current Department of Education and HSE guidance).",
  "NOT the same as compulsions or self-harm in the adolescent-mental-health sense. Self-injurious stereotypy in developmental disability is usually repetitive and rhythmic; self-harm linked to distress in adolescents is a different risk pathway — assess separately.",
 ],

 "prevalence": [
  "OVERALL: DSM-5-TR reports that simple stereotypies (e.g. rocking) are common in young typically developing children, and that complex stereotypies occur in a smaller proportion — exact figures not stated here, check before quoting (APA, 2022).",
  "INTELLECTUAL DISABILITY: stereotypy and self-injury are more common with greater degree of ID and in some genetic syndromes (e.g. Lesch-Nyhan, Smith-Magenis, Cornelia de Lange) (Oliver & Richards, 2015) — rates vary; check before quoting.",
  "AUTISM: repetitive motor mannerisms are part of criterion B and are very common — rate not stated here, check.",
  "IRELAND: no Irish prevalence figure is cited here — check before quoting.",
  "SENSORY IMPAIRMENT AND DEPRIVATION: stereotypies (e.g. eye pressing) are more frequent in children with visual impairment and in children who experienced severe early deprivation — rates not stated here, check.",
  "COURSE: primary motor stereotypies in typically developing children often persist for years but tend to reduce in visibility; many children learn to manage where and when (Harris et al., 2008).",
 ],

 "cooccurring": [
  {"name": "AUTISM",
   "rate": "very common — stereotypy is part of criterion B; rate not stated here, check",
   "presents": "Hand flapping, rocking, spinning, finger movements, often with excitement, anxiety or sensory overload. Usually covered by the autism diagnosis; SMD added only where self-injury or treatment focus warrants."},
  {"name": "INTELLECTUAL DISABILITY / GLD",
   "rate": "elevated, higher with greater degree of ID (Oliver & Richards, 2015) — check",
   "presents": "Body rocking, hand mouthing, head hitting; stereotypy may increase in unstimulating environments or with pain. Functional assessment essential."},
  {"name": "GENETIC SYNDROMES",
   "rate": "syndrome-specific — check",
   "presents": "Characteristic patterns: self-biting (Lesch-Nyhan), hand wringing with regression (Rett syndrome), self-hugging and self-injury (Smith-Magenis). Medical / genetics question; do not speculate in the report."},
  {"name": "ADHD",
   "rate": "reported in primary motor stereotypy samples — rate not stated here, check",
   "presents": "Stereotypies alongside restlessness and inattention in typically developing children; assess attention separately."},
  {"name": "TICS / TOURETTE'S",
   "rate": "can co-occur — rate not stated here, check",
   "presents": "Both types of movement in one child; describe each separately (onset, rhythm, urge, context) for the medical team."},
  {"name": "ANXIETY",
   "rate": "reported — rate not stated here, check",
   "presents": "Increase in stereotypy with transitions, noise or uncertainty; may be the visible sign of distress in a child with limited verbal communication."},
  {"name": "VISUAL OR HEARING IMPAIRMENT",
   "rate": "elevated — rate not stated here, check",
   "presents": "Eye pressing, rocking or light-gazing; sensory-seeking in the absence of typical input. Check sensory services involvement."},
 ],

 "recommendations": [
  "START WITH IMPACT: write whether the movement (a) causes injury, (b) prevents learning or participation, (c) causes social difficulty the child cares about, or (d) none of these. Only (a)–(c) justify intervention. Say so explicitly.",
  "DO NOT SUPPRESS HARMLESS STEREOTYPY. Recommend staff allow it, and build movement and sensory breaks into the day. If the child or family wants to manage where it happens (e.g. in public), work WITH them on times and places, not prohibition.",
  "FUNCTION-BASED ASSESSMENT for self-injury or disruptive stereotypy: ABC recording over at least 1–2 weeks across settings, interviews, and scatterplots; hypothesis about function (attention, escape, access to items, automatic / sensory, pain). Structured functional analysis is a specialist, supervised procedure (Hanley et al., 2003).",
  "INTERVENTION FOLLOWS FUNCTION: e.g. teaching a communication response that achieves the same outcome (functional communication training), offering alternative sensory input, enriching the environment, adjusting demands. Positive Behaviour Support frameworks bring this together.",
  "PAIN AND HEALTH: a new or increased self-injury in a child with limited communication must prompt a medical check (ear infection, dental pain, constipation, reflux, seizures). Write this in the report.",
  "SAFETY PLAN for self-injury: agreed, least-restrictive responses; any protective equipment or physical intervention only as prescribed by the clinical team and in line with current Department of Education / HSE guidance on restrictive practices — check the current documents and the school's policy.",
  "CONTINUUM LEVEL: Classroom Support for acceptance and movement breaks; School Support where stereotypy interferes with learning; School Support Plus for self-injury, with CDNT / specialist input and a written behaviour support plan.",
  "REFER: CDNT (psychology, OT, SLT) for children with a disability; GP / paediatrics for medical review, new self-injury or any regression; genetics via paediatrics where a syndrome is suspected; CAMHS where there is co-occurring mental health difficulty and local criteria are met.",
  "DO NOT recommend punishment, aversives, or blanket 'hands down' / 'quiet hands' instructions for harmless stereotypy. DO NOT recommend restraint or seclusion. PSI 2.2.2 and PSI 4.2.2 apply.",
 ],

 "explain_parent": [
  "'The rocking and hand movements are called stereotypies. Lots of children do them — especially when they're excited, concentrating, or overwhelmed. For many, they help the child feel settled.'",
  "'If they're not hurting her and not stopping her learning, we don't need to stop them. Stopping them can make her more stressed.'",
  "'The head-banging is different, because it can hurt him. We need to find out what it's doing for him — is it when he's in pain, when a task is too hard, when he wants something? Once we know that, we can teach him another way to get that need met.'",
  "'Because he can't always tell us when something hurts, any new or increased head-banging should be checked by the GP — ears, teeth, tummy.'",
  "'You know him best. What have you noticed makes it better or worse?'",
  "SIGNPOST: CDNT (via Assessment of Need or direct referral — check local route); GP; AsIAm (autism, Ireland) → https://asiam.ie/ ; Inclusion Ireland (intellectual disability) → https://inclusionireland.ie/ — check current services.",
 ],

 "explain_teacher": [
  "'If the flapping or rocking isn't hurting anyone and isn't stopping learning, let it be. It's usually helping him regulate. Please don't say \"quiet hands\".'",
  "'Build movement breaks into the day before he needs them, and give him a place where it's fine to move.'",
  "'The self-injury is different. I need your help recording what happens just before, during and after each episode for two weeks — time, activity, who was there, what we did. That's how we find out what it's for.'",
  "'If it's increased suddenly, tell the family and suggest a GP check — pain is a common, missed cause in children who can't tell us.'",
  "'Any physical intervention or protective equipment has to be in the agreed plan and follow the school policy and current guidance, and has to be recorded. It's never a first response.'",
 ],

 "explain_child": [
  "YOUNGER (or limited verbal): use visuals and a calm tone — 'Moving hands is okay. Moving is good.' Show a picture of a movement break space. For self-injury, model and teach an alternative ('Help, please' card; squeeze toy) rather than saying 'No'.",
  "OLDER: 'Lots of people move their hands or rock when they're excited or thinking hard — some people call it stimming. It's not wrong. We'll talk about any times you'd like to do it more privately, if that matters to you.'",
  "ASK (if the child can answer): 'How does it feel when you do that? When do you most want to? Is there anywhere in school you'd like to go when you need to?'",
  "ASK AUTISTIC ADOLESCENTS directly about their view of stimming — many describe it as helpful and are distressed by being stopped (Kapp et al., 2019).",
 ],

 "analogies": [
  "TAPPING YOUR FOOT: 'Most of us jiggle a leg, twirl hair or click a pen when we're concentrating or nervous. His movements do the same job — they're just more visible.' Works with teachers and peers.",
  "THE PRESSURE VALVE: 'The movement lets off steam. If you block the valve, the pressure goes somewhere else.' Good for explaining why suppressing harmless stereotypy can backfire.",
  "THE SMOKE ALARM: 'Self-injury is like an alarm going off — our job is to find the fire, not just take out the battery.' Good for explaining functional assessment and checking for pain.",
 ],

 "language": [
  "'Stereotypic Movement Disorder' (DSM-5-TR); 'stereotyped movement disorder' (ICD-11). 'Stereotypies' or 'motor stereotypies' describe the movements.",
  "'Stimming' is the term many autistic people use and prefer; it is non-pathologising. Use it when talking with autistic young people and families who use it.",
  "Avoid 'self-stimulatory behaviour' as a deficit label, 'odd' or 'bizarre' movements, and 'challenging behaviour' for harmless stereotypy. Reserve 'behaviour that challenges' for behaviour that causes harm or significantly restricts participation.",
  "Describe precisely: what, how often, how long, where, with whom, and what follows. Precision replaces judgement (PSI 1.2.8).",
 ],

 "red_flags": [
  "RED FLAG — self-injury causing tissue damage, eye injury or head injury. Same-day action: medical attention; review the safety plan; inform parents; clinical team (CDNT / paediatrics).",
  "RED FLAG — NEW or sharply INCREASED self-injury or stereotypy, especially in a child with limited communication. Check pain and illness first (GP); consider changes at home or school.",
  "RED FLAG — LOSS of skills (hand use, speech, walking) with new hand-wringing or stereotypies, particularly in a young girl — Rett syndrome and other regressive conditions need urgent paediatric review.",
  "RED FLAG — unexplained injuries attributed to 'self-injury', or injuries in unusual places. Consider child protection; follow Children First procedures and report to Tusla as soon as practicable if you have reasonable grounds for concern — telling the DLP does not discharge a mandated person's own duty; supervision follows action. Do not let the diagnosis close the question.",
  "RED FLAG — restrictive practices (restraint, seclusion, mechanical restraint) not in an agreed plan, or not recorded. Raise with the principal and follow current guidance; child safeguarding may apply.",
  "BOUNDARY — diagnosis by psychiatrist, paediatrician or CDNT team; structured functional analysis only under specialist supervision; medication is a medical matter. The EP describes, formulates function and recommends. PSI 2.2.2.",
 ],

 "child_voice": [
  "OBSERVATION OF WHAT THE CHILD SEEKS — for non-speaking children, the child's voice is in what they move toward and away from. Good because the function of stereotypy is often the child's communication.",
  "TALKING MATS (symbol-based) — for children with limited verbal language, sort 'things I like / not sure / don't like' about school activities and spaces. Good because it gives non-verbal children a structured way to express preferences (check training requirements).",
  "COMMUNICATION PASSPORT / ONE-PAGE PROFILE with the family and child — 'how I show you I'm happy, excited, upset, in pain'. Good because it teaches new staff to read stereotypy as communication.",
  "AUTISTIC-LED RESOURCES on stimming (e.g. AsIAm, Ireland → https://asiam.ie/). Good because older young people can see their own experience validated and decide what, if anything, they want to change.",
  "PREFERENCE ASSESSMENT — offering choices of sensory activities and noting what the child selects. Good because it identifies alternatives that meet the same sensory need.",
 ],

 "questions": [
  "Q: 'Should we stop him flapping?' — A: 'If it's not hurting him or stopping him learning, no. It usually helps him regulate. We'd rather make sure there's space for it.'",
  "Q: 'Does rocking mean she's autistic?' — A: 'Not on its own. Lots of children with typical development have movements like this. Autism is about a wider pattern of social communication and other differences. If you're concerned, the GP or CDNT is the route.'",
  "Q: 'Why is he hitting his head?' — A: 'We don't know yet, and that's the right question. It might be pain, frustration, wanting to escape something, wanting something, or a sensation he's seeking. Recording what happens before and after each episode will tell us, and a GP check rules out pain.'",
  "Q: 'Can we use a helmet?' — A: 'Protective equipment is sometimes part of a plan, but it's a clinical decision made with the team, following current guidance, and it's never the whole answer — we still need to find out why it's happening.'",
  "Q: 'Will he grow out of it?' — A: 'Many children's stereotypies become less visible as they get older, and many learn when and where to do them. Some continue into adulthood, and for many people that's fine.'",
  "Q: 'Can you diagnose Stereotypic Movement Disorder?' — A: 'No — that's for the psychiatrist, paediatrician or CDNT team. I can describe what's happening, what it seems to do for her, and what school can do.'",
 ],

 "supervision": [
  "Clarify what functional assessment methods are within your competence now, and what requires specialist supervision (e.g. structured functional analysis).",
  "Bring ABC data and discuss your hypothesis about function before writing recommendations.",
  "Discuss the current Department of Education and HSE guidance on restrictive practices and the school's policy — check the current documents together.",
  "Discuss how to handle a request from a school to 'stop' harmless stereotypy, and how to reframe it.",
  "Discuss when injuries raise a child protection question and the reporting steps.",
 ],

 "reflection": [
  "ON THE GOAL — Did I ask whether the movement needs to change at all, and whose goal that is?",
  "ON FUNCTION — Did I gather data before hypothesising, or assume 'attention-seeking' or 'sensory'?",
  "ON PAIN — Did I recommend a medical check for new or increased self-injury?",
  "ON RESTRICTION — Did I check what restrictive practices are in use, and whether they are planned, recorded and in line with current guidance?",
  "ON VOICE — How did the child's own communication — including their movements — shape the plan?",
  "WHAT GOOD LOOKS LIKE: 'Two weeks of ABC data showed head-hitting clustered at the start of table-top tasks and stopped when the task was removed. Hypothesis: escape. Plan: teach a \"break\" card, shorten and preview tasks, GP check (ear infection found and treated). Harmless flapping left alone.'",
  "WHAT POOR LOOKS LIKE: 'Stereotypic behaviours noted. Staff to discourage these and redirect.' — no impact analysis, no function, suppresses harmless stimming.",
 ],

 "citations": [
  CIT_DSM,
  "Harris, K. M., Mahone, E. M., & Singer, H. S. (2008). Nonautistic motor stereotypies: Clinical features and longitudinal follow-up. Pediatric Neurology, 38(4), 267–272.",
  "Singer, H. S. (2009). Motor stereotypies. Seminars in Pediatric Neurology, 16(2), 77–81.",
  "Oliver, C., & Richards, C. (2015). Practitioner review: Self-injurious behaviour in children with developmental delay. Journal of Child Psychology and Psychiatry, 56(10), 1042–1054.",
  "Hanley, G. P., Iwata, B. A., & McCord, B. E. (2003). Functional analysis of problem behavior: A review. Journal of Applied Behavior Analysis, 36(2), 147–185.",
  "Kapp, S. K., Steward, R., Crane, L., Elliott, D., Elphick, C., Pellicano, E., & Russell, G. (2019). 'People should be allowed to do what they like': Autistic adults' views and experiences of stimming. Autism, 23(7), 1782–1792.",
  CIT_ICD,
  CIT_NEPS,
 ],

 "pathway": {
  "age": "Onset is in early childhood — typically before age 3 (APA, 2022; Harris et al., 2008). Formal SMD diagnosis is uncommon; it is usually made when self-injury is present or when stereotypy is the focus of intervention, often in a child already known to disability services. Primary stereotypies in typically developing children may be identified at any age when parents seek reassurance.",
  "who_diagnoses": "Ireland: paediatrician, child psychiatrist, or CDNT multidisciplinary team (psychology with medical input). Genetic assessment via paediatrics where a syndrome is suspected. Assessment of Need (Disability Act 2005) may be the route. Check local practice.",
  "who_wrote_report": "CDNT psychologist or team; paediatrician; CAMHS psychiatrist; genetics service; private clinical psychologist or behaviour analyst (check qualifications and scope). The EP report adds school function and learning context.",
  "refer_to": "CDNT for children with a disability; GP / paediatrics for new or increased self-injury, suspected pain, or any regression (urgent); genetics via paediatrics; CAMHS if co-occurring mental health difficulty meets criteria; Tusla if child protection concerns.",
  "sooner": "'These movements are very common and often harmless, so it was reasonable to watch and wait. What we're looking at now is whether any of them are causing harm or getting in the way — and if so, why.'",
 },

 "differential": [
  "TICS — later onset, sudden, brief, variable, premonitory urge, wax and wane (Singer, 2009).",
  "AUTISM — stereotypy as part of criterion B; full developmental assessment needed.",
  "COMPULSIONS (OCD) — driven by anxiety or intrusive thoughts; older children; CAMHS question.",
  "BODY-FOCUSED REPETITIVE BEHAVIOURS (hair pulling, skin picking) — classified separately in DSM-5-TR (obsessive-compulsive and related disorders).",
  "SEIZURES OR NEUROLOGICAL CONDITIONS (including Rett syndrome) — any loss of awareness, regression or new neurological sign → urgent medical review.",
  "PAIN OR ILLNESS in a child with limited communication — always rule out.",
 ],

 "next": [
  "Describe the movements and their impact: injury, learning, social — or none.",
  "If impact: collect ABC data across settings for 1–2 weeks and form a hypothesis about function.",
  "Recommend a GP check for any new or increased self-injury.",
  "Write a function-based plan at the right Continuum level; leave harmless stereotypy alone.",
  "Refer to CDNT / paediatrics as needed; check restrictive practices against current guidance.",
 ],

 "presentations": [
  "Motor-based sensory difficulties",
  "Sensory modulation difficulties (over- or under-responsive)",
  "Sensory discrimination difficulties",
  "Self-care and independence skills at school",
  "AAC and communication access",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — onset typically before age 3",
   "prevalence": "Simple stereotypies common in young children (APA, 2022) — rate not stated here, check.",
   "see": "Hand flapping or waving when excited, rocking, head banging at sleep time. Often harmless and transient. The question is whether it is part of a broader developmental picture (autism, ID, sensory impairment) or an isolated primary stereotypy; refer for developmental review if other concerns.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Griffiths III", "Vineland-3", "SCQ (Social Communication Questionnaire)"],
  },
  "School Age": {
   "applies": "YES — stereotypies often continue; school impact and peer reactions become the focus",
   "prevalence": "Rate not stated here — check.",
   "see": "Flapping, pacing or rocking during excitement, absorption or stress; teasing from peers; staff unsure whether to stop it. Self-injury more likely where there is ID or limited communication. Describe impact before planning anything.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3", "SRS-2", "SDQ"],
  },
  "Adolescent": {
   "applies": "YES — often less visible; self-awareness and self-determination matter",
   "prevalence": "Rate not stated here — check.",
   "see": "Many young people manage where and when they stim; some feel self-conscious or are bullied. Their own view of whether anything should change must lead the plan. In ID, self-injury may change with puberty, pain or transitions.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3", "ABAS-3"],
  },
  "Young Adult": {
   "applies": "YES — may persist; relevant in adult disability services",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Stereotypy often accepted as part of the person; self-injury managed through adult disability services. EP involvement rare beyond transition planning.",
   "tools": ["ABAS-3 adult form", "Vineland-3 adult"],
  },
  "Special Setting": {
   "applies": "YES — most common setting for referral about stereotypy and self-injury",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Stereotypy and self-injury in children with autism, moderate to profound ID, or genetic syndromes. The work is functional assessment, communication, environment and safety planning with the class team and CDNT, within current restrictive practice guidance.",
   "tools": ["Functional behaviour assessment (ABC)", "Vineland-3 / ABAS-3", "Communication Matrix / AAC review", "Adaptive measure in place of IQ"],
  },
 },
})
