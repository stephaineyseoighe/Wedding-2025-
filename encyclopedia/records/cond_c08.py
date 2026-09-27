# CONDS records: Speech Sound Disorder, Childhood-Onset Fluency Disorder (stuttering),
# Social (Pragmatic) Communication Disorder.
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c08.py

CONDS = [

# =====================================================================================
# 1. SPEECH SOUND DISORDER
# =====================================================================================
{
 "name": "Speech Sound Disorder",
 "code": "DSM-5-TR Speech Sound Disorder (F80.0) · ICD-11 6A01.0 Developmental speech sound disorder — check codes before quoting",
 "neps": "1. LEARNING (1.2 Language skills) — and 1.4 Literacy where phonological difficulty affects reading and spelling",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A persistent difficulty PRODUCING speech sounds that reduces intelligibility or prevents the child from getting a message across, with onset in the early developmental period, and not attributable to a congenital or acquired condition such as cerebral palsy, cleft palate, hearing loss or brain injury (APA, 2022, DSM-5-TR criteria — read the full criteria before quoting).",
  "It is an umbrella for several different underlying problems. Dodd (2014) describes four groups — this is the distinction to hold:\n▸ ARTICULATION DISORDER — difficulty making a particular sound (e.g. a lisped /s/), consistent across words.\n▸ PHONOLOGICAL DELAY — error patterns typical of a younger child (e.g. 'tat' for 'cat').\n▸ CONSISTENT PHONOLOGICAL DISORDER — unusual, non-developmental error patterns, used consistently.\n▸ INCONSISTENT PHONOLOGICAL DISORDER — the same word said differently on different attempts.",
  "CHILDHOOD APRAXIA OF SPEECH (CAS) sits alongside these: a difficulty PLANNING the movements for speech, with inconsistent errors, groping, vowel errors and disrupted prosody (ASHA, 2007). It is less common, usually more severe, and needs specialist SLT input. Do not use the label yourself.",
  "PHONOLOGICAL (sound-system) difficulties are the ones that matter most for school: the child's difficulty is in how speech sounds are stored and organised, not just in moving the tongue. That underlying representation is the same system that phonological awareness and early reading draw on (Stackhouse & Wells, 1997).",
  "Most speech errors in young children are DEVELOPMENTAL and resolve. SSD is identified when errors persist beyond the age expected, are unusual, or reduce intelligibility enough to affect communication, learning or participation. Age norms for individual sounds vary by study and by accent — the SLT holds them.",
  "The EP's role: describe the IMPACT (on being understood, on participation, on literacy, on wellbeing), make classroom adjustments, look at phonological awareness and early literacy, and refer to SLT. Diagnosis and therapy sit with the SLT.",
 ],

 "what_it_is_not": [
  "NOT a language disorder. SSD concerns the SOUNDS of speech; DLD concerns understanding and using language (vocabulary, grammar, narrative). They often co-occur, and unclear speech can hide a language difficulty underneath — so assess both rather than assuming one (Bishop et al., 2017).",
  "NOT an accent or dialect. Irish English features are not errors — for example, dental stops for 'th' ('tree' for 'three') are a normal feature of many Irish English accents (Hickey, 2007). A child's speech is judged against the speech of their community, not against a textbook standard.",
  "NOT EAL. A child learning English will carry over sound patterns from their home language. SSD shows in the home language too — ask the family, or an interpreter, whether the child is understood at home by speakers of that language.",
  "NOT laziness or 'baby talk' the child could drop if they tried. A child with a phonological disorder often cannot HEAR the difference between their error and the target in their own speech. Telling them to 'say it properly' does not work and teaches them that talking is risky.",
  "NOT necessarily a literacy problem — but a risk factor for one. Risk is highest when speech difficulty persists into school age, when errors are unusual rather than delayed, and when language difficulty co-occurs (Bishop & Adams, 1990; Nathan et al., 2004; Hayiou-Thomas et al., 2017).",
  "NOT something to 'wait and see' once it is affecting intelligibility at school entry. Early SLT referral is the default when a child is hard to understand for unfamiliar adults.",
  "NOT something the EP diagnoses. The SLT assesses speech (e.g. with a structured articulation and phonology assessment) and decides the type. The EP describes impact and refers.",
 ],

 "prevalence": [
  "OVERALL (early years): Eadie et al. (2015), an Australian community cohort, reported SSD in about 3.4% of 4-year-olds — check the paper before quoting the exact figure and definition used.",
  "PERSISTENT (school age): Wren et al. (2016), using the UK ALSPAC cohort, estimated persistent SSD at about 3.6% of 8-year-olds — check before quoting. Most speech errors resolve before this age; those that persist are more likely to be atypical.",
  "IRELAND: no Irish population prevalence study is cited here — check before quoting. SSD is a large part of HSE Primary Care SLT caseloads, but caseload reflects referral and service capacity, not prevalence.",
  "SEX RATIO: more boys than girls are identified (Eadie et al., 2015; Wren et al., 2016) — exact ratio not stated here, check.",
  "CAS: much less common than other SSD types; population rate not stated here — check (ASHA, 2007 notes the evidence is limited).",
  "CO-OCCURRENCE WITH LANGUAGE DIFFICULTY is common in clinical and community samples (Eadie et al., 2015) — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "DEVELOPMENTAL LANGUAGE DISORDER (DLD)",
   "rate": "common — rate not stated here, check (Eadie et al., 2015)",
   "presents": "unclear speech that draws attention away from weak vocabulary, grammar or comprehension. When the speech clears, the language difficulty is still there. The co-occurring language difficulty is the strongest predictor of later literacy difficulty (Hayiou-Thomas et al., 2017)."},
  {"name": "DYSLEXIA / LITERACY DIFFICULTY",
   "rate": "elevated risk, highest when speech difficulty persists past about 5;6 or co-occurs with DLD (Bishop & Adams, 1990; Nathan et al., 2004) — rate not stated here, check",
   "presents": "weak phonological awareness (rhyme, segmenting, blending), spelling that mirrors the child's own speech errors ('tat' for 'cat'), and slow acquisition of letter–sound links in Junior and Senior Infants."},
  {"name": "CHILDHOOD-ONSET FLUENCY DISORDER (STUTTERING)",
   "rate": "co-occurs in some children — rate not stated here, check",
   "presents": "repetitions, prolongations or blocks alongside sound errors. Both need SLT; the fluency difficulty usually drives more of the anxiety about talking."},
  {"name": "SOCIAL AND EMOTIONAL DIFFICULTY",
   "rate": "reduced participation and peer difficulty reported (McCormack et al., 2009) — rate not stated here, check",
   "presents": "reluctance to speak in class, answering in single words, withdrawal from group work, frustration when not understood, or being teased about how they talk."},
  {"name": "ADHD",
   "rate": "elevated in some samples — rate not stated here, check",
   "presents": "fast, impulsive speech that reduces intelligibility further, and poor attention to SLT home practice. Separate the speech difficulty from attention by listening to a slow, structured naming task."},
  {"name": "DCD / MOTOR DIFFICULTY",
   "rate": "reported in some children, particularly with CAS features — rate not stated here, check",
   "presents": "broader motor planning difficulty (handwriting, dressing, PE) alongside speech. Where speech and motor difficulties both appear, CDNT rather than single-discipline input may be the right route."},
  {"name": "HEARING LOSS / GLUE EAR (as cause to rule out)",
   "rate": "must be excluded — if present, the difficulty is attributable to hearing, not SSD in DSM terms",
   "presents": "fluctuating clarity, missing final consonants and quiet sounds (s, f, th), and variable attention to speech. Audiology before any conclusion."},
 ],

 "recommendations": [
  "NAME THE IMPACT, not the error pattern. 'Unfamiliar adults understand about half of what he says in class; he has stopped offering answers' is actionable. The detailed error analysis belongs in the SLT report.",
  "RESPOND TO THE MESSAGE, NOT THE SOUND. Model the correct word naturally ('Yes, a CAT — a big cat') rather than asking the child to repeat it. Direct correction in front of peers reduces talking and does not fix a phonological error.",
  "REPAIR STRATEGIES WHEN NOT UNDERSTOOD: ask the child to show, point, draw or say it another way; repeat back what you did understand; take the burden of the breakdown ('I didn't catch that — my ears are slow today'). Agree the strategy with the child in advance.",
  "PHONOLOGICAL AWARENESS AND EARLY LITERACY: explicit, systematic teaching of rhyme, syllable and phoneme awareness, linked to letters, in small groups at School Support. Phonological awareness training combined with letter–sound teaching has the strongest evidence for children at risk (Hulme & Snowling, 2009 — check the specific study cited). Monitor spelling for errors that mirror speech.",
  "CO-ORDINATE WITH THE SLT: ask for the SLT report and current targets; include one or two in the Student Support Plan with a named adult, a short daily practice slot and a review date. Ask the SLT which sounds are being worked on so the teacher can praise them in context.",
  "PROTECT PARTICIPATION: offer non-verbal and small-group ways to contribute; do not require reading aloud to the class unless the child is comfortable; give the child a role that does not depend on being understood first time.",
  "WATCH FOR TEASING and address it as a bullying and inclusion issue at whole-class level, not by removing the child from speaking situations.",
  "CONTINUUM LEVEL: Classroom Support for communication-friendly adjustments; School Support for targeted phonological awareness and literacy work; School Support Plus where SLT is involved or literacy is not responding.",
  "REFER: SLT via HSE Primary Care (single-need SSD) or CDNT where there are multiple or complex needs (e.g. suspected CAS with motor difficulty, or co-occurring autism or ID) — check local criteria. AUDIOLOGY via GP / Primary Care if hearing has not been checked recently.",
  "DO NOT recommend 'more practice saying the words' or speech drills designed by school staff without SLT input, and do not describe an accent or dialect feature as an error in a report.",
 ],

 "explain_parent": [
  "'Speech sound disorder means she finds it hard to make some speech sounds, or to organise the sounds in words the way other children her age do. It isn't about how clever she is, and it isn't about how well she understands.'",
  "'Lots of young children mix up sounds and grow out of it. We think about a speech sound disorder when it goes on longer than expected or makes it hard for people outside the family to understand her.'",
  "'It isn't anything you did. You don't need to correct her every time. What helps most is saying the word back the right way, naturally — \"Oh, the SPOON\" — and answering what she meant.'",
  "'The sounds in speech are the same building blocks she'll use for reading and spelling, so we'll keep an eye on how she's getting on with letters and sounds, and the school can do extra work on that.'",
  "'The speech and language therapist is the person who works on the sounds themselves. My part is how it affects her at school — being understood, joining in, and the early reading.'",
  "SIGNPOST: the child's SLT; HSE Primary Care SLT (self- or GP referral — check local process); the Irish Association of Speech and Language Therapists (IASLT) for information on private SLT → https://www.iaslt.ie/ (check current address).",
 ],

 "explain_teacher": [
  "'He can't just decide to say it properly. With this kind of speech difficulty, children often can't hear the difference between what they said and what they meant. Correcting him in front of the class won't fix it and will stop him talking.'",
  "'Answer what he meant, and say the word back correctly without asking him to repeat it. That's the model he needs.'",
  "'If you don't understand him, take the blame for the breakdown and give him another way — show me, point, draw it. Agree a signal with him in advance so it doesn't become a scene.'",
  "'Keep an eye on phonological awareness and spelling. If his spellings look like his speech — \"tat\" for \"cat\" — that's the speech difficulty showing up on paper, and it needs explicit sound work, not just more spellings.'",
  "'Ask the SLT which sounds he's working on. Noticing and praising one target sound in class is worth more than a general \"speak clearly\".'",
  "'Watch the playground. Children who are hard to understand are often left out or teased, and that tends to show before academic problems do.'",
 ],

 "explain_child": [
  "YOUNGER: 'Some sounds are tricky for your mouth, and that's okay. Lots of children have tricky sounds. Your speech helper is going to play games with you to help. If someone doesn't understand, you can show them or say it another way.'",
  "OLDER: 'Your brain sorts speech sounds a bit differently, so some words come out different from how you mean them. It's not about being clever. Your speech and language therapist helps with the sounds, and your teacher knows to give you time.'",
  "TEACH A REPAIR SENTENCE: 'Let me show you' or 'I'll say it a different way' — practise it so the child has a plan for when they are not understood.",
  "ASK: 'Are there times at school when people don't understand you? What happens then?' and 'Has anyone ever said anything about how you talk?' — the second question is how you find teasing.",
  "CHECK YOUR OWN LISTENING: if you cannot understand the child, say so honestly and use pictures or drawing. Pretending to understand is quickly noticed and is worse than asking.",
 ],

 "analogies": [
  "THE FILING CABINET WITH MIXED-UP FOLDERS: 'The sounds are all in there, but some are filed in the wrong drawer, so when she reaches for \"k\" she pulls out \"t\".' Good with parents; explains why it is not effort and why it links to spelling.",
  "THE FOREIGN WORD YOU CAN'T QUITE SAY: 'Think of a word in another language you've tried to say — you know you're getting it wrong, but you can't hear exactly how.' Good with teachers; explains why repetition drills do not work.",
  "THE BLURRY PHOTO: 'He has the picture of the word, but it's a bit blurry, so it comes out blurry and it's harder to use for spelling too.' Good for explaining the literacy link to parents.",
  "THE LEARNER DRIVER (for CAS): 'She knows where she wants to go, but every move of the gears has to be thought about, so it comes out jerky and different each time.' Good for explaining motor planning to staff.",
 ],

 "language": [
  "'Speech sound disorder (SSD)' is the current umbrella term (APA, 2022). Older or informal reports may say 'articulation disorder', 'phonological disorder', 'speech delay' or 'unclear speech' — use the SLT's term and explain it.",
  "Use 'childhood apraxia of speech (CAS)' only where an SLT has used it; 'verbal dyspraxia' and 'developmental verbal dyspraxia' are older UK and Irish terms for a similar presentation (ASHA, 2007 discusses terminology).",
  "Distinguish 'speech' (sounds) from 'language' (meaning and structure) every time. Parents and schools often use them interchangeably; reports should not.",
  "Avoid 'baby talk', 'lazy speech' and 'poor pronunciation'. These imply choice. Describe what happens: 'replaces k and g with t and d at the start of words'.",
  "Do not describe accent or dialect features as difficulties. If you are unsure whether a feature is local, ask the SLT or a local teacher.",
 ],

 "red_flags": [
  "RED FLAG — LOSS of speech sounds or words the child previously had, or new slurred speech. Not SSD. Medical referral via GP / paediatrics without delay.",
  "RED FLAG — hearing never checked or history of recurrent ear infections / glue ear. Audiology before any conclusion.",
  "RED FLAG — nasal-sounding speech, food or fluid coming through the nose, or visible structural difference in the mouth. Refer to GP; this may be a structural cause (e.g. palatal) needing medical and SLT assessment.",
  "RED FLAG — a child who is very hard to understand and trying to tell you something that could be a disclosure. Children with communication difficulties are more vulnerable and less able to disclose. Use drawing, pointing and time; follow Children First procedures the same day; report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's own duty.",
  "BOUNDARY — you do not diagnose SSD or CAS or set speech targets; the SLT does. You describe impact, assess phonological awareness and literacy, and refer. PSI 2.2.2.",
  "WATCH — a child who has stopped talking in class. This may be a response to being misunderstood or teased, or may point to selective mutism or anxiety. Find out when and where they do talk.",
 ],

 "child_voice": [
  "TALKING MATS — picture symbols sorted under 'like / not sure / don't like'. Good because it lets a child with low intelligibility give a clear view without having to be understood in speech. → https://www.talkingmats.com/",
  "DRAWING AND POINTING ('draw where talking is easy / hard at school') — good because it locates the difficulty in real settings and the drawing carries the meaning if the words do not.",
  "SCALING WITH FACES OR A LADDER ('how much do people understand you?') — good because it needs a point, not a sentence, and gives you a follow-up question.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — adapt by reading it aloud and accepting pointing answers. Good because it is Irish, free and familiar to staff. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "PARENT AS INTERPRETER, WITH CARE — a parent can often understand speech that you cannot. Good for accuracy, but check the child's own words where possible and be aware the parent may soften what the child says about home.",
 ],

 "questions": [
  "Q: 'Will he grow out of it?' — A: 'Many children's speech sounds do sort themselves out, and therapy helps a lot. Whether and how quickly depends on the type of difficulty, which is what the speech and language therapist looks at. What we can do at school is make sure he's understood and keep an eye on his early reading.'",
  "Q: 'Why does it matter for reading? He can see the letters.' — A: 'Reading uses the sounds in words, not just the letters. If the sounds are a bit mixed up in how he stores them, linking letters to sounds can be harder. That's why we'll do extra sound work and watch his spelling.'",
  "Q: 'Should I make her say it properly?' — A: 'No — just say the word back correctly and carry on the conversation. Making her repeat it usually doesn't work and can put her off talking. The therapist will give you specific practice to do at home.'",
  "Q: 'Is it because we speak Portuguese at home?' — A: 'No. Speaking two languages doesn't cause a speech sound disorder. If there's a real difficulty, it'll show up in Portuguese too — so how he sounds in Portuguese is really useful for us to know.'",
  "Q: 'Is it the same as dyspraxia?' — A: 'Not quite. Some children have difficulty planning speech movements — sometimes called verbal dyspraxia or apraxia of speech — and that's one type. Most speech sound difficulties are about how sounds are organised, not movement. The therapist will say which it is.'",
  "Q: 'Can you assess his speech?' — A: 'The speech sounds themselves are for the speech and language therapist. I can look at how it's affecting him in class, check his sound awareness and early reading, and make sure the referral is in.'",
 ],

 "supervision": [
  "Ask how your supervisor assesses phonological awareness in Junior and Senior Infants, and what they would use (e.g. PhAB2 or informal tasks) at which age.",
  "Bring a case where you were unsure whether a speech feature was local accent or error, and discuss how to check.",
  "Ask about the local SLT route — Primary Care versus CDNT, waiting times, and whether the service accepts school or EP referrals directly.",
  "Discuss how to write about a child's literacy risk without over-predicting — what the evidence does and does not say about SSD and later reading.",
  "Bring a case where a child had stopped talking in class, and discuss how to separate a speech-related withdrawal from anxiety or selective mutism.",
 ],

 "reflection": [
  "ON SPEECH VS LANGUAGE — Did I check language as well as speech, or did the unclear speech become the whole story?",
  "ON ACCENT — Did I judge the child's speech against their community's speech, or against my own?",
  "ON LITERACY — Did I look at phonological awareness and spelling for speech-like errors, or did I leave literacy to a later referral?",
  "ON THE CHILD'S VOICE — Did I find a way to get the child's view that did not depend on me understanding their speech? Did I pretend to understand?",
  "ON PARTICIPATION — Did I ask whether the child still offers answers in class and whether anyone comments on how they talk?",
  "WHAT GOOD LOOKS LIKE: 'Senior Infants referral for \"unclear speech and slow phonics\". Audiology was clear. His spellings matched his speech errors exactly. I recommended small-group phonological awareness with letter links, a repair strategy agreed with him, and SLT referral. The report separated speech, language and literacy.'",
  "WHAT POOR LOOKS LIKE: 'Speech is unclear; school to encourage him to speak slowly and clearly.' — no hearing check, no language check, no literacy link, no SLT referral, and a recommendation that puts the burden on the child.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Speech Sound Disorder.",
  "American Speech-Language-Hearing Association. (2007). Childhood apraxia of speech [Technical report]. ASHA.",
  "Bishop, D. V. M., & Adams, C. (1990). A prospective study of the relationship between specific language impairment, phonological disorders and reading retardation. Journal of Child Psychology and Psychiatry, 31(7), 1027–1050.",
  "Dodd, B. (2014). Differential diagnosis of pediatric speech sound disorder. Current Developmental Disorders Reports, 1(3), 189–196.",
  "Eadie, P., Morgan, A., Ukoumunne, O. C., Ttofari Eecen, K., Wake, M., & Reilly, S. (2015). Speech sound disorder at 4 years: Prevalence, comorbidities, and predictors in a community cohort of children. Developmental Medicine & Child Neurology, 57(6), 578–584.",
  "Hayiou-Thomas, M. E., Carroll, J. M., Leavett, R., Hulme, C., & Snowling, M. J. (2017). When does speech sound disorder matter for literacy? The role of disordered speech errors, co-occurring language impairment and family risk of dyslexia. Journal of Child Psychology and Psychiatry, 58(2), 197–205.",
  "Hickey, R. (2007). Irish English: History and present-day forms. Cambridge University Press.",
  "McCormack, J., McLeod, S., McAllister, L., & Harrison, L. J. (2009). A systematic review of the association between childhood speech impairment and participation across the lifespan. International Journal of Speech-Language Pathology, 11(2), 155–170.",
  "Nathan, L., Stackhouse, J., Goulandris, N., & Snowling, M. J. (2004). The development of early literacy skills among children with speech difficulties: A test of the 'critical age hypothesis'. Journal of Speech, Language, and Hearing Research, 47(2), 377–391.",
  "Wren, Y., Miller, L. L., Peters, T. J., Emond, A., & Roulstone, S. (2016). Prevalence and predictors of persistent speech sound disorder at eight years old: Findings from a population cohort study. Journal of Speech, Language, and Hearing Research, 59(4), 647–673.",
  "Stackhouse, J., & Wells, B. (1997). Children's speech and literacy difficulties: A psycholinguistic framework. Whurr.",
  "Hulme, C., & Snowling, M. J. (2009). Developmental disorders of language learning and cognition. Wiley-Blackwell.",
 ],

 "pathway": {
  "age": "Usually noticed at 2–4 by parents or preschool staff because the child is hard to understand; SLT referral often follows around 3–4. Many children are identified at school entry (Junior Infants), when unfamiliar adults cannot understand them and phonics teaching begins. Milder residual errors (e.g. /s/, /r/) may be noticed later and matter less for literacy.",
  "who_diagnoses": "Ireland: a Speech and Language Therapist — usually HSE Primary Care SLT for single-need SSD; CDNT where there are multiple or complex needs (e.g. suspected CAS with motor difficulty, or co-occurring autism or ID). Assessment of Need (Disability Act 2005) may route through either. Private SLT reports are common. Check local routes — they vary by area.",
  "who_wrote_report": "HSE Primary Care SLT; CDNT SLT (often within a multidisciplinary report); private SLT; early-intervention or preschool SLT reports. Occasionally an ENT, cleft or paediatric team report where there is a structural or medical cause. An EP report may describe intelligibility and literacy impact but should not be the source of an SSD diagnosis.",
  "refer_to": "SLT via Primary Care or CDNT (check local criteria). Audiology via GP / Primary Care if hearing not recently checked. GP / paediatrics for any loss of speech, new slurring, nasal speech or structural concern. CDNT where motor, social-communication or learning difficulties also suspected.",
  "sooner": "'Lots of young children have unclear speech that sorts itself out, so it's very common to wait and see. You're here now, the therapist can still do a great deal, and we can make sure school is doing the sound work that helps with reading.'",
 },

 "differential": [
  "ACCENT / DIALECT — local features (e.g. Irish English 'th' realisations) are not errors (Hickey, 2007).",
  "EAL — transfer from the home language; SSD shows in the home language too.",
  "HEARING LOSS (including fluctuating glue ear) — audiology first.",
  "STRUCTURAL OR NEUROLOGICAL CAUSE (cleft palate, dysarthria in cerebral palsy) — then it is not SSD in DSM terms; medical and SLT team.",
  "CHILDHOOD APRAXIA OF SPEECH — a type of SSD with motor planning difficulty; specialist SLT decision.",
  "DLD — language rather than speech; commonly co-occurs.",
  "SELECTIVE MUTISM — the child speaks clearly at home but not in school; an anxiety presentation.",
 ],

 "next": [
  "Check hearing history and date of last audiology; request if not recent.",
  "Get the SLT report if one exists and read current targets; if none, refer.",
  "Screen phonological awareness and early letter–sound knowledge, and look at spelling samples for speech-like errors.",
  "Observe oral participation in class and ask about teasing.",
  "Write communication and phonological-awareness recommendations with named adult, frequency and review date at the right Continuum level.",
 ],

 "presentations": [
  "Participation in oral work and classroom talk",
  "Literacy difficulty not meeting SLD criteria",
  "Reading stamina and avoidance of reading aloud",
  "Spelling as a barrier to written output",
  "English as an Additional Language (EAL)",
  "Bilingual language development",
  "Bullying",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — the main window for identification and SLT intervention",
   "prevalence": "About 3.4% of 4-year-olds in one community cohort (Eadie et al., 2015) — check before quoting.",
   "see": "Speech hard to understand for adults outside the family; sounds replaced or left out ('tat' for 'cat', 'nana' for 'banana'); frustration when not understood. Many errors are developmental — the SLT judges which are not. Check hearing and home-language exposure first.",
   "tools": ["Preschool Language Scales-5 (PLS-5)", "Renfrew Action Picture Test", "Ages & Stages Questionnaires (ASQ-3)",
             "Diagnostic Evaluation of Articulation and Phonology (DEAP; Dodd et al., 2002) — AGE 3:0–6:11 (check manual) · MEASURES: articulation, phonology, consistency, oro-motor skills — SLT tool · CANNOT TELL YOU: language, literacy or classroom impact · TIME: 20–40 min (check)"],
  },
  "School Age": {
   "applies": "YES — persistent SSD and its literacy consequences are seen here",
   "prevalence": "About 3.6% persistent SSD at 8 years in one UK cohort (Wren et al., 2016) — check before quoting.",
   "see": "Reduced intelligibility with unfamiliar adults, reluctance to speak in class, slow progress with phonics and spelling that mirrors speech errors. Residual errors (e.g. /s/, /r/) may remain with little learning impact. Watch for teasing and withdrawal.",
   "tools": ["Phonological Assessment Battery (PhAB2)", "CELF-5 UK", "WIAT-III UK", "DASH", "Renfrew Action Picture Test"],
  },
  "Adolescent": {
   "applies": "RARELY — most SSD has resolved; residual errors or CAS may persist",
   "prevalence": "Adolescent rate not stated here — check. Persistence is less common than for DLD.",
   "see": "Residual sound errors (e.g. lisp) that affect confidence more than learning; occasionally persisting CAS with ongoing intelligibility difficulty. Self-consciousness, avoiding oral presentations and oral language exams. RACE and oral exam arrangements may be questions — check current SEC guidance.",
   "tools": ["WIAT-III UK", "Access arrangements evidence (RACE)", "RCADS self-report"],
  },
  "Young Adult": {
   "applies": "RARELY — residual errors only, or persisting CAS",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Residual errors may affect confidence in interviews, presentations and phone use. Persisting CAS or severe SSD may need adult SLT and communication access in further education. The EP role is usually time-limited here.",
   "tools": ["WAIS-IV UK", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — often as part of a wider profile (ID, CAS, physical disability)",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Speech intelligibility difficulties are common where there is ID, a genetic syndrome or motor disability — then it is usually 'associated with' that condition rather than SSD. Check that AAC, signing or a total communication approach is used consistently across staff, so the child is not reliant on speech alone.",
   "tools": ["Communication Matrix / AAC review", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 2. CHILDHOOD-ONSET FLUENCY DISORDER (STUTTERING)
# =====================================================================================
{
 "name": "Childhood-Onset Fluency Disorder (stuttering)",
 "code": "DSM-5-TR Childhood-Onset Fluency Disorder (Stuttering) (F80.81) · ICD-11 6A01.1 Developmental speech fluency disorder — check codes before quoting",
 "neps": "1. LEARNING (1.2 Language skills) — and 3. EMOTIONAL (3.2 Anxiety) where fear of speaking drives avoidance",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "A disturbance in the normal flow and timing of speech, inappropriate for age, with onset in childhood (APA, 2022). Core features: repetitions of sounds and syllables ('b-b-b-ball'), prolongations ('sssssun'), blocks (silent or audible stoppages), and broken words. Read the full DSM-5-TR criteria before quoting.",
  "It usually brings SECONDARY behaviours the child develops to push through or avoid stuttering: physical tension, eye blinks, head movements, word substitution, circumlocution, pretending not to know an answer, and avoiding speaking situations altogether.",
  "The visible stutter is only part of it. The ICEBERG model (Sheehan, 1970) distinguishes what listeners hear from what sits below the surface — fear, shame, anticipation and avoidance. In school, what is under the surface often matters more for participation than how much the child stutters.",
  "Onset is usually between about 2 and 5 years, often after a period of typical speech, and can be sudden (Yairi & Ambrose, 2013; Reilly et al., 2013). Many young children who start to stutter recover without treatment; those who continue into school age are less likely to recover fully.",
  "It is NEUROLOGICAL and strongly HERITABLE, not caused by anxiety, trauma or parenting (Yairi & Ambrose, 2013). Anxiety can make it worse, and social anxiety is a common consequence in older children and adults (Iverach & Rapee, 2014).",
  "Stuttering VARIES: by situation, listener, time pressure, fatigue and the word being said. Many people who stutter are fluent when singing, reading in unison or talking to a pet. Variability is part of the condition, not evidence that the child 'can control it'.",
  "The EP's role: describe impact on participation, learning and wellbeing; advise the school on listening and oral work; watch for bullying, anxiety and avoidance; refer to SLT. Diagnosis and therapy sit with the SLT.",
 ],

 "what_it_is_not": [
  "NOT caused by nervousness or by anything the parents did. Older ideas blaming parents are not supported (Yairi & Ambrose, 2013). Say this clearly — parents often feel guilty.",
  "NOT normal disfluency. All young children, and adults, say 'um', revise sentences and repeat whole words or phrases ('I want — I want that'). Stuttering-like disfluencies are part-word repetitions, prolongations and blocks, often with tension. The SLT makes the call.",
  "NOT helped by 'slow down', 'take a breath' or 'start again'. These well-meant instructions tell the child their talking is wrong and increase pressure. They are among the first things to change in school.",
  "NOT a sign of low ability. Children who stutter have the same range of ability as other children. Oral answers, reading aloud and oral exams can UNDER-represent what they know.",
  "NOT cluttering. Cluttering involves a rapid or irregular rate with collapsed syllables and reduced intelligibility, often with less awareness; it can co-occur with stuttering (Ward, 2006). SLT distinction.",
  "NOT always the goal to eliminate. Many adults who stutter, and a growing part of the stuttering community, emphasise communicating effectively and without shame rather than being fluent (Constantino et al., 2022). Ask the child and family what their goals are.",
  "NOT something the EP diagnoses. The SLT assesses fluency and decides on therapy. The EP describes impact and refers.",
 ],

 "prevalence": [
  "INCIDENCE (ever stuttered): Yairi and Ambrose (2013), reviewing the epidemiology, put lifetime incidence at around 5–8% — check before quoting. Reilly et al. (2013) found a cumulative incidence of about 11% by age 4 in an Australian community cohort — check.",
  "PREVALENCE (currently stuttering): around 1% in the general population is widely cited; higher in preschool children (Yairi & Ambrose, 2013) — check before quoting.",
  "RECOVERY: most preschool children who start to stutter recover — often cited as around 80% (Yairi & Ambrose, 2013) — check before quoting. Recovery is less likely the longer it persists; predictors are debated.",
  "SEX RATIO: close to even at onset, becoming increasingly male with age because girls recover more often; around 4:1 in adults is often cited (Yairi & Ambrose, 2013) — check before quoting.",
  "IRELAND: no Irish population prevalence study is cited here — check before quoting. Roughly: in a typical primary school of several hundred pupils, expect a handful who stutter.",
  "FAMILY HISTORY: common — a family history of stuttering is frequently reported (Yairi & Ambrose, 2013); rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "SOCIAL ANXIETY",
   "rate": "elevated in adolescents and adults who stutter (Iverach & Rapee, 2014) — rate not stated here, check",
   "presents": "fear of speaking situations, avoiding answering, phone use and introductions, and anticipatory worry before oral work. The anxiety is usually a consequence of experiences of stuttering, not its cause. Treat it seriously in its own right."},
  {"name": "BULLYING AND PEER DIFFICULTY",
   "rate": "children who stutter are at increased risk of being teased or bullied — rate not stated here, check",
   "presents": "imitation or laughter when the child speaks, exclusion, reluctance to go to school or to the yard. Often not reported to adults. Ask directly."},
  {"name": "SPEECH SOUND DISORDER / DLD",
   "rate": "co-occur in some children — rate not stated here, check",
   "presents": "fluency difficulty alongside unclear speech or weak language. Separate true stuttering from the pauses and restarts of word-finding difficulty in DLD."},
  {"name": "ADHD",
   "rate": "elevated in some samples — rate not stated here, check",
   "presents": "fast, impulsive speech with more disfluency under time pressure, and difficulty using SLT techniques consistently. Assess attention separately, not through oral tasks alone."},
  {"name": "EMOTIONALLY BASED SCHOOL AVOIDANCE",
   "rate": "not established — rate not stated here, check",
   "presents": "absence on days with oral presentations, reading aloud or oral Irish; late arrival to avoid roll call. Look at the pattern of absence against the timetable."},
  {"name": "LOW MOOD / LOW SELF-ESTEEM",
   "rate": "reported in adolescents who stutter — rate not stated here, check",
   "presents": "negative self-talk about talking, withdrawal from friends and activities. Screen mood; follow the risk route if self-harm or suicidal thoughts are disclosed."},
 ],

 "recommendations": [
  "NAME THE PARTICIPATION IMPACT, not only the stutter. 'Has not answered a question voluntarily since September; avoids reading aloud; absent on presentation days' is actionable.",
  "LISTENING BEHAVIOUR FOR ALL STAFF: keep natural eye contact, wait, do not finish words or sentences, do not say 'slow down' or 'take a breath', respond to WHAT was said, not how. Slightly slower adult speech and fewer rapid-fire questions help without drawing attention (practice common in parent–child interaction approaches, e.g. Kelman & Nicholas, 2020).",
  "NEGOTIATE ORAL WORK WITH THE CHILD, don't decide for them: ask what helps — being asked first or later, answering questions with short answers, reading in pairs or unison, presenting to a smaller group, or a pre-agreed signal. Do not silently excuse them from all speaking; that sends its own message.",
  "ROLL CALL, READING ALOUD, ORAL IRISH: raise each explicitly in the plan. Offer alternatives (hand up for roll call, choral or paired reading). For State exams, ask the school to check current SEC RACE guidance on oral components — do not assume what is available.",
  "BULLYING: address imitation and teasing under the school's anti-bullying procedures, and consider (with the child's agreement) a class talk about stuttering led by the child, SLT or teacher.",
  "CO-ORDINATE WITH THE SLT: ask for the report and current approach (e.g. a parent–child interaction approach for younger children, or fluency-shaping or stuttering-modification techniques for older ones) so the school does not contradict it. Do not ask the child to use techniques in class unless the SLT and child have agreed that.",
  "WELLBEING: include the child's own goals, and monitor anxiety and mood. Where social anxiety is established, refer via GP to Primary Care Psychology or CAMHS depending on severity.",
  "CONTINUUM LEVEL: Classroom Support for listening behaviour and negotiated oral work; School Support for a plan with named adult and review date; School Support Plus where SLT is involved, anxiety or bullying is significant, or attendance is affected.",
  "REFER: SLT via HSE Primary Care (or CDNT where needs are complex) — check local route. Early referral matters in the preschool years. GP urgently for sudden onset in an older child or after illness or head injury.",
  "DO NOT recommend 'encourage him to slow down', 'avoid asking him questions' or exempting the child from all oral work without their input.",
 ],

 "explain_parent": [
  "'Stuttering is a difference in how the brain times and co-ordinates speech. It isn't caused by anything you did, and it isn't a sign that she's anxious or behind.'",
  "'It's very common for young children to start stuttering, and lots of them stop without treatment — but we don't wait for that; the speech and language therapist is the right person to see now.'",
  "'It's normal for it to come and go — worse when she's tired, excited or rushed, and gone for days at a time. That doesn't mean she's doing it on purpose.'",
  "'What helps at home is listening to what she's saying rather than how — not finishing her words, not telling her to slow down, and giving her time. The therapist will give you specific things to try.'",
  "'At school, my focus is making sure she keeps putting her hand up, isn't being teased, and that oral work doesn't become something she dreads.'",
  "SIGNPOST: the child's SLT; HSE Primary Care SLT; the Irish Stammering Association (check current contact details); STAMMA (the British Stammering Association) → https://stamma.org/ for parent and school information.",
 ],

 "explain_teacher": [
  "'Please don't finish his words or tell him to slow down or take a breath. It's kindly meant, but it tells him his talking is a problem. Just wait, keep looking at him naturally, and answer what he said.'",
  "'Ask him privately what helps with reading aloud, roll call and answering in class. He'll know. Don't decide for him — and don't just stop asking him questions.'",
  "'The stutter you hear isn't the whole picture. A child who stutters less in class might be avoiding words, swapping answers or saying \"I don't know\". Fewer stutters isn't always good news.'",
  "'It varies a lot — fluent one day, a lot of stuttering the next. That's the condition, not effort.'",
  "'Watch for imitation and teasing, especially in the yard and online. Deal with it as bullying.'",
  "'For oral Irish, presentations and State exams, the school should check current arrangements early rather than assume.'",
 ],

 "explain_child": [
  "YOUNGER: 'Sometimes words get stuck or bumpy when you talk. That happens to lots of people, and it's okay. You can take all the time you need. Your speech helper has games that help.'",
  "OLDER: 'Stuttering is how your brain times speech — it's not about being nervous or not clever. Lots of people stutter, including well-known actors, singers and presenters. What helps in class is up to you, and your teachers want to know.'",
  "ASK: 'When is talking easy for you? When is it hard?' and 'Has anyone ever copied or laughed at how you talk?'",
  "ASK: 'Is there anything you've stopped doing because of stuttering — like putting your hand up, or ordering food?' — this is how you find avoidance.",
  "MODEL IT IN THE SESSION: wait, don't finish words, keep eye contact, and let the child see that you are listening to what they say. Your behaviour in the session is itself an intervention.",
 ],

 "analogies": [
  "THE ICEBERG (Sheehan, 1970): 'What you hear is the tip. Underneath is worry, word-swapping and avoiding — and that's often the bigger part.' Good with teachers and adolescents; explains why fewer stutters can mean more avoidance.",
  "THE TRAFFIC LIGHTS: 'The brain's signals for speech sometimes get stuck on red for a moment. Pressing the horn — rushing or telling him to hurry — doesn't make the light change faster.' Good with parents and younger children.",
  "LEFT-HANDEDNESS: 'It's just how some brains are wired. You wouldn't tell a left-handed child to try harder with their right hand.' Good for moving parents and staff away from effort and control explanations.",
  "SINGING VS TALKING: 'Lots of people who stutter can sing fluently, because singing uses timing differently.' Good for explaining variability and that it is not about knowing the words.",
 ],

 "language": [
  "'Stuttering' and 'stammering' mean the same thing. 'Stammering' is more common in Ireland and the UK; 'stuttering' in DSM-5-TR and US literature. Use the term the child and family use.",
  "Many people prefer 'person who stutters' or 'stammerer' — preferences vary, and some reclaim identity-first language. Ask.",
  "Avoid 'suffers from a stutter', 'afflicted' and 'speech impediment'. These frame it as defect and suffering.",
  "Describe what happens and its impact: 'stutters on initial sounds, with blocks under time pressure; avoids reading aloud' rather than 'poor fluency'.",
  "Do not call a child's fluent speech 'good talking' in their hearing. It implies stuttering is bad talking. Praise content and participation instead.",
 ],

 "red_flags": [
  "RED FLAG — SUDDEN onset of stuttering in an older child, adolescent or adult, or after a head injury, illness or seizure. May be neurogenic. GP / paediatrics without delay.",
  "RED FLAG — sudden onset linked to a distressing event, or stuttering alongside other signs of trauma. Consider psychological factors, and follow Children First procedures the same day if abuse is suspected; report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's own duty.",
  "RED FLAG — disclosure of self-harm or suicidal thoughts, or severe low mood in an adolescent who stutters. Same-day risk route per service procedure; supervision follows action, never replaces it.",
  "RED FLAG — sustained bullying, or school avoidance linked to speaking demands. Act on the bullying under the school's procedures and address attendance early.",
  "BOUNDARY — you do not diagnose stuttering or choose the therapy approach; the SLT does. You do not advise on medication. PSI 2.2.2.",
  "WATCH — the 'fluent' child who is avoiding. Word substitution, 'I don't know' and silence can hide a significant stutter. Ask the child and family.",
 ],

 "child_voice": [
  "WRITTEN OR TYPED RESPONSES — offer the option of writing answers or using a tablet. Good because it removes time pressure and lets the child say what they think without negotiating the stutter; many older children prefer it.",
  "SCALING OF SPEAKING SITUATIONS ('how hard is roll call / reading aloud / answering / yard, 0–10?') — good because it maps avoidance precisely and gives you a hierarchy the child owns.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it is Irish and familiar; add a question about speaking in class. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "TALKING MATS — good for younger children or those who avoid speaking with new adults; sorting symbols is low-pressure. → https://www.talkingmats.com/",
  "TIME — the simplest resource. Allow long pauses without filling them. Good because hurrying the child in a consultation reproduces exactly what they experience in class.",
 ],

 "questions": [
  "Q: 'Did something happen to cause it?' — A: 'Almost always, no. Stuttering is to do with how the brain times speech, and it often runs in families. It can start around a busy time, which is why people link it to events — but it isn't caused by them.'",
  "Q: 'Should I tell her to slow down?' — A: 'It's natural to want to, but it usually adds pressure. What helps more is you speaking a bit more slowly yourself, giving her time, and listening to what she says rather than how. The therapist will give you specifics.'",
  "Q: 'He's fine at home — why does he stutter at school?' — A: 'Stuttering really does vary with the situation — who's listening, time pressure, how important it feels. It's very common to be more fluent at home. It doesn't mean he's putting it on.'",
  "Q: 'Should we stop asking him to read aloud?' — A: 'Ask him first. Some children want to keep reading, some want to read in pairs or first, some want a break for now. Deciding for him — either way — can send the wrong message.'",
  "Q: 'Will she grow out of it?' — A: 'Many young children do, especially if it started recently. If it's gone on for a while, it's more likely to stay in some form — and with support, lots of people who stutter talk confidently and do whatever they want. The therapist can say more about her pattern.'",
  "Q: 'Can he be exempt from oral Irish?' — A: 'That's decided under the current Department and State Examinations Commission rules, which I'd want the school to check rather than assume. Often the more useful question is what arrangements would let him show what he knows.'",
 ],

 "supervision": [
  "Ask how the service responds when stuttering is part of an attendance or anxiety referral, and who leads — SLT, EP or Primary Care Psychology.",
  "Discuss how to recommend oral-work arrangements without teaching avoidance.",
  "Bring a case where you noticed yourself finishing a child's words or rushing, and talk about what it tells you about pace in consultation.",
  "Ask what the service's practice is on State exam arrangements and oral Irish for pupils who stutter, and where the current guidance sits.",
  "Ask about local SLT fluency provision — whether there is a specialist fluency clinician in the area, and waiting times.",
 ],

 "reflection": [
  "ON MY OWN LISTENING — Did I wait, or did I finish words, fill silences or look away? What did the child experience in my session?",
  "ON THE ICEBERG — Did I ask about avoidance, word substitution and anticipation, or only about what I could hear?",
  "ON GOALS — Whose goal was fluency? Did I ask the child what they wanted to be different?",
  "ON BULLYING AND MOOD — Did I ask directly about teasing and about how the child feels about talking?",
  "ON ORAL WORK — Did my recommendations increase participation, or did they quietly remove the child from speaking?",
  "WHAT GOOD LOOKS LIKE: 'Fifth class, referred for \"refusing to read aloud\". He scaled roll call at 9/10 and reading aloud at 8. We agreed hand-up for roll call and paired reading, the teacher stopped saying \"take your time\", and the class did a talk on stammering he chose to help with. Four weeks later he was answering questions again.'",
  "WHAT POOR LOOKS LIKE: 'He should be encouraged to slow down and take a breath before speaking, and not be asked questions in front of the class.' — both recommendations increase pressure and avoidance, and neither came from the child.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Childhood-Onset Fluency Disorder (Stuttering).",
  "Yairi, E., & Ambrose, N. (2013). Epidemiology of stuttering: 21st century advances. Journal of Fluency Disorders, 38(2), 66–87.",
  "Reilly, S., Onslow, M., Packman, A., Cini, E., Conway, L., Ukoumunne, O. C., Bavin, E. L., Prior, M., Eadie, P., Block, S., & Wake, M. (2013). Natural history of stuttering to 4 years of age: A prospective community-based study. Pediatrics, 132(3), 460–467.",
  "Iverach, L., & Rapee, R. M. (2014). Social anxiety disorder and stuttering: Current status and future directions. Journal of Fluency Disorders, 40, 69–82.",
  "Sheehan, J. G. (1970). Stuttering: Research and therapy. Harper & Row.",
  "Ward, D. (2006). Stuttering and cluttering: Frameworks for understanding and treatment. Psychology Press.",
  "Kelman, E., & Nicholas, A. (2020). Palin Parent-Child Interaction therapy for early childhood stammering (2nd ed.). Routledge.",
  "Constantino, C., Campbell, P., & Simpson, S. (2022). Stuttering and the social model. Journal of Communication Disorders, 96, 106200.",
 ],

 "pathway": {
  "age": "Onset usually between about 2 and 5, often noticed by parents within days or weeks (Yairi & Ambrose, 2013; Reilly et al., 2013). Many preschool children recover; SLT referral is still recommended early so the family gets advice and the child is monitored. Children who continue stuttering into primary school are identified by teachers when reading aloud and oral answering begin. Onset after childhood is unusual and needs medical review.",
  "who_diagnoses": "Ireland: a Speech and Language Therapist — HSE Primary Care SLT in most cases; CDNT where there are multiple or complex needs. Some areas have SLTs with a fluency specialism — check local provision. Private SLT reports are common. The EP does not diagnose.",
  "who_wrote_report": "HSE Primary Care SLT; CDNT SLT; private SLT; occasionally a specialist fluency clinic. A psychology report (Primary Care Psychology or CAMHS) may address co-occurring anxiety but not the stutter itself.",
  "refer_to": "SLT via Primary Care (or CDNT if complex) — check local criteria. GP → Primary Care Psychology (mild–moderate) or CAMHS (severe) where anxiety or mood is significant. GP / paediatrics urgently for sudden onset in an older child or after injury or illness.",
  "sooner": "'Lots of young children stutter for a while and it goes away, so it's very common to wait. You're here now, and whatever age he is, the therapist can help — and school can make a big difference to how he feels about talking.'",
 },

 "differential": [
  "TYPICAL DISFLUENCY — whole-word and phrase repetitions, fillers and revisions in a young child; no tension or avoidance. SLT judgement.",
  "CLUTTERING — rapid, irregular rate with collapsed syllables; can co-occur (Ward, 2006).",
  "WORD-FINDING DIFFICULTY IN DLD — pauses, fillers and restarts from searching for words rather than stuttering.",
  "TICS / TOURETTE SYNDROME — vocal tics or blocking tics can resemble stuttering; GP / paediatrics.",
  "NEUROGENIC OR PSYCHOGENIC STUTTERING — onset after brain injury or illness, or linked to a distressing event, typically later in life; medical review.",
  "SELECTIVE MUTISM / SOCIAL ANXIETY — not speaking in some settings; can co-occur with stuttering.",
 ],

 "next": [
  "Get the SLT report if one exists and find out the current therapy approach; if none, refer.",
  "Ask the child to scale speaking situations and ask directly about teasing.",
  "Check attendance against the timetable for oral-work days.",
  "Write listening-behaviour and negotiated oral-work recommendations with named adult and review date at the right Continuum level.",
  "Screen anxiety and mood in older children; refer on if needed.",
 ],

 "presentations": [
  "Participation in oral work and classroom talk",
  "Reading stamina and avoidance of reading aloud",
  "Bullying",
  "Peer relationship difficulties and social isolation",
  "Anticipatory anxiety about transitions",
  "Word-finding difficulty",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — onset usually 2–5; many recover, SLT advice early",
   "prevalence": "Cumulative incidence about 11% by age 4 in one community cohort (Reilly et al., 2013) — check before quoting.",
   "see": "Sound and syllable repetitions, prolongations and blocks, sometimes appearing suddenly; may come and go. Some children show tension or frustration; many seem unaware. Parents are often worried and may blame themselves. Refer to SLT rather than 'wait and see'.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Preschool Language Scales-5 (PLS-5)"],
  },
  "School Age": {
   "applies": "YES — persistent stuttering and its participation impact seen here",
   "prevalence": "Current prevalence around 1% across ages is often cited (Yairi & Ambrose, 2013) — school-age rate not stated here, check.",
   "see": "Stuttering in reading aloud, roll call and answering; secondary behaviours (tension, blinks, word swaps); avoidance growing through the senior classes. Teasing may start. Oral Irish and presentations become flashpoints.",
   "tools": ["SDQ", "RCADS", "Piers-Harris 3"],
  },
  "Adolescent": {
   "applies": "YES — persistence more likely; social anxiety and avoidance peak",
   "prevalence": "Adolescent rate not stated here — check. Sex ratio more male than at onset (Yairi & Ambrose, 2013).",
   "see": "Avoidance of speaking in class, oral exams, phones and new social situations; possible social anxiety and low mood. Bullying, including online. RACE and oral exam arrangements need to be raised early — check current SEC guidance.",
   "tools": ["RCADS self-report", "Beck Youth Inventories-2", "MFQ (Mood and Feelings Questionnaire)", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "YES — persistent stuttering continues; focus is communication confidence and access",
   "prevalence": "Adult prevalence around 1% is often cited (Yairi & Ambrose, 2013) — check before quoting.",
   "see": "Interview, presentation and phone demands in further education and work; social anxiety is common (Iverach & Rapee, 2014). Adult SLT and peer support (self-help groups) are the routes; the EP role is usually time-limited.",
   "tools": ["Adult self-report measures via the service", "WAIS-IV UK"],
  },
  "Special Setting": {
   "applies": "RARELY — as the primary need; more often alongside another condition",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "Disfluency may occur alongside ID, autism or a genetic syndrome (e.g. some syndromes are associated with cluttering-like or stuttering-like speech — check). Ensure staff listening behaviour is consistent and that AAC or signing is offered where speech is effortful.",
   "tools": ["Communication Matrix / AAC review", "Vineland-3 / ABAS-3"],
  },
 },
},

# =====================================================================================
# 3. SOCIAL (PRAGMATIC) COMMUNICATION DISORDER
# =====================================================================================
{
 "name": "Social (Pragmatic) Communication Disorder",
 "code": "DSM-5-TR Social (Pragmatic) Communication Disorder (F80.82) · ICD-11 has no separate diagnosis — nearest is 6A01.22 Developmental language disorder with impairment of mainly pragmatic language — check before quoting",
 "neps": "4. SOCIAL (4.1 Friendships and social skills) — and 1. LEARNING (1.2 Language skills)",
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · GDPR",

 "what_it_is": [
  "Persistent difficulty in the SOCIAL USE of verbal and non-verbal communication, introduced in DSM-5 (APA, 2013; retained in DSM-5-TR, 2022). DSM-5-TR lists four areas — read the full criteria before quoting:\n▸ using communication for social purposes (greeting, sharing information) in a way that fits the context;\n▸ changing communication to match the listener or setting (e.g. talking differently to a young child than to an adult, or in class than in the yard);\n▸ following conversation rules — turn-taking, rephrasing when misunderstood, using verbal and non-verbal signals;\n▸ understanding what is not said directly — inference, idioms, humour, sarcasm, ambiguous meanings.",
  "The difficulties must limit communication, social participation, relationships, learning or work; start in early development (though may not be obvious until demands rise); and not be better explained by structural language difficulty, intellectual disability, global developmental delay, autism or another condition (APA, 2022).",
  "THE KEY DISTINCTION FROM AUTISM: SPCD requires the ABSENCE of restricted, repetitive patterns of behaviour, interests or activities — now OR in the developmental history. If a child has social-communication difficulty AND restricted/repetitive behaviours (current or past), autism is considered instead (APA, 2022). This is the line the diagnosis depends on.",
  "It is CONTESTED. Norbury (2014) reviewed the evidence and concluded that the validity of SPCD as a category distinct from autism and from language disorder was not yet established, and called for more research. Others have found that children meeting SPCD criteria may look like a milder or sub-threshold form of autism (Mandy et al., 2017), while earlier work described a group with pragmatic difficulty outside autism (Gibson et al., 2013). Hold the label lightly and describe the child.",
  "It has a history: 'semantic-pragmatic disorder' and later 'pragmatic language impairment' described children whose use of language was more affected than its structure (Bishop, 2000). Older reports may use these terms.",
  "The EP's role: describe social communication in real contexts (class, yard, group work), the impact on learning, relationships and wellbeing, recommend adjustments and social-communication support, and refer. Diagnosis sits with the SLT, usually within a multidisciplinary (often CDNT) assessment that has considered autism.",
 ],

 "what_it_is_not": [
  "NOT 'mild autism' by definition — but NOT clearly separate from it either. The honest position is that the boundary is uncertain and debated (Norbury, 2014; Swineford et al., 2014). Say that to families rather than presenting SPCD as a settled, distinct entity.",
  "NOT a structural language disorder. A child whose conversation goes wrong because they cannot understand complex sentences or find words has DLD. SPCD concerns USE when structure is adequate — though the two often co-occur, and pragmatic difficulty is common in DLD (Norbury, 2014).",
  "NOT shyness, introversion or quietness. A shy child knows the rules of conversation and holds back; a child with SPCD may talk freely but miss the listener's cues, go off-topic or misread intent.",
  "NOT explained by ADHD alone. Interrupting, blurting and topic-hopping in ADHD come from impulsivity and attention; the child usually knows the rule. Assess both; they can co-occur.",
  "NOT cultural difference. Norms for eye contact, turn-taking, directness and humour vary across cultures and communities. Judge against the child's own community — interpreter and family input matter.",
  "NOT a label that automatically opens autism-specific supports. In Ireland, some provision (e.g. autism special classes) has been tied to an autism diagnosis — check current NCSE criteria. This is a practical consequence families may raise; do not let it drive your description.",
  "NOT something the EP diagnoses. The EP describes and formulates; SLT and the multidisciplinary team decide.",
 ],

 "prevalence": [
  "OVERALL: not established. Because SPCD was introduced in 2013 and its boundaries are debated, population estimates vary with the definition and sample — rate not stated here, check before quoting (Swineford et al., 2014).",
  "IRELAND: no Irish prevalence figure is cited here — check before quoting. Anecdotally the diagnosis appears less often in Irish reports than autism; do not quote this as a finding.",
  "OVERLAP: pragmatic difficulties are common in children with DLD, ADHD and other conditions; SPCD as a stand-alone diagnosis is less common than the difficulties themselves (Norbury, 2014) — rate not stated here, check.",
  "AGE: DSM-5-TR notes that the diagnosis is rarely made before about age 4, as it requires adequate speech and language (APA, 2022) — check the text before quoting.",
  "SEX RATIO: not established — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "DEVELOPMENTAL LANGUAGE DISORDER (DLD)",
   "rate": "common overlap (Norbury, 2014) — rate not stated here, check",
   "presents": "pragmatic difficulties alongside weak vocabulary, grammar or comprehension. If structural language difficulty explains the social communication difficulty, it is DLD rather than SPCD; often both are described. Get the SLT's view on which is primary."},
  {"name": "ADHD",
   "rate": "elevated — rate not stated here, check",
   "presents": "interrupting, topic-shifting and missing cues. Ask whether the child knows the rule when calm and one-to-one — if yes, attention and impulsivity are more likely the driver."},
  {"name": "ANXIETY",
   "rate": "elevated — rate not stated here, check",
   "presents": "worry about social situations after repeated misunderstandings, avoidance of group work and the yard, or clinging to adults. Often a consequence of social failure rather than the cause."},
  {"name": "PEER DIFFICULTY AND BULLYING",
   "rate": "common — rate not stated here, check",
   "presents": "being left out, misreading teasing as friendliness or friendliness as hostility, conflict after misunderstood jokes. Adolescents may be targeted because they take things literally."},
  {"name": "READING COMPREHENSION DIFFICULTY",
   "rate": "reported — rate not stated here, check",
   "presents": "accurate decoding but weak inference, especially about characters' intentions, feelings and figurative language. Test inference directly rather than assuming comprehension is fine."},
  {"name": "AUTISM (as differential, not co-occurrence)",
   "rate": "by definition exclusive in DSM-5-TR — SPCD is not diagnosed if autism criteria are met",
   "presents": "social-communication difficulty WITH restricted/repetitive behaviours, interests or sensory differences, now or in the history. A careful developmental history is essential — past RRBs count. Refer for multidisciplinary assessment; do not settle the question in an EP report."},
 ],

 "recommendations": [
  "DESCRIBE THE COMMUNICATION IN CONTEXT, not the label. 'Takes \"pull your socks up\" literally; talks at length about his topic without noticing peers have moved away; misreads teasing' is actionable. Observe in class AND in unstructured time.",
  "TEACH THE HIDDEN RULES EXPLICITLY: turn-taking, how to join a group, how to change topic, what to say when you don't understand. Small-group work at School Support, with practice in real situations, not only in a withdrawal room.",
  "SAY WHAT YOU MEAN: staff avoid unexplained idiom and sarcasm in instructions, or explain them ('\"hold your horses\" means wait'). Teach figurative language as vocabulary.",
  "SUPPORT INFERENCE AND PERSPECTIVE-TAKING in literacy: explicit 'why did the character…' and 'what might she be thinking…' questions with visual supports.",
  "STRUCTURE UNSTRUCTURED TIME: clubs, structured yard games, a buddy or peer-mediated approach, a clear place to go. Unstructured time is where SPCD causes most harm.",
  "REPAIR AFTER CONFLICT: use a calm, visual debrief of misunderstandings (e.g. comic-strip-style drawing of who said what and what each person thought). Frame it as learning, not blame.",
  "INTERVENTION EVIDENCE: the Social Communication Intervention Project (Adams et al., 2012) is one of few trials of SLT-led intervention for pragmatic difficulty — results were mixed on primary outcomes; check the paper before citing effects. Co-ordinate with the SLT rather than inventing a programme.",
  "CONTINUUM LEVEL: Classroom Support for clear language and structured unstructured time; School Support for small-group social-communication teaching; School Support Plus where SLT/CDNT is involved, peer difficulty is severe, or wellbeing is affected.",
  "REFER: SLT via Primary Care, or CDNT where autism is being considered or needs are complex — check local route. Where autism is a question, the referral should ask explicitly for autism to be considered, with the developmental history.",
  "DO NOT write 'SPCD' or 'not autism' as your conclusion, and do not recommend generic 'social skills training' without saying what skill, where, how often and how it will transfer.",
 ],

 "explain_parent": [
  "'Social communication disorder means she finds the unwritten rules of conversation harder — taking turns, knowing when someone's joking, changing how she talks for different people. Her words and sentences are fine; it's using them socially that's hard.'",
  "'You'll hear different opinions about this diagnosis. It's fairly new — 2013 — and researchers still disagree about how different it is from autism. What matters most is a clear picture of what she finds hard and what helps.'",
  "'The main difference the diagnostic manuals draw is that in autism there are also repetitive behaviours, strong narrow interests or sensory differences. The team will have asked about those when she was younger too.'",
  "'None of this is caused by parenting. And these are skills we can teach directly — the rules other children pick up without being told.'",
  "'If you're worried the label changes what support she can get, that's a fair question, and one to ask the school and the SENO. My job is to describe her needs so support follows the needs.'",
  "SIGNPOST: the child's SLT or CDNT key worker; the SENO for school provision questions; the HSE Primary Care SLT route.",
 ],

 "explain_teacher": [
  "'He isn't being rude or cheeky. He's missing the unwritten rules — when to stop, when you're joking, what a look means. Tell him the rule plainly and he'll often follow it.'",
  "'Say what you mean. \"Can you close the door?\" might get \"Yes\" and no action. \"Please close the door\" works.'",
  "'The yard and group work are where it goes wrong. Structure helps — a job, a club, a clear role in the group.'",
  "'When something goes wrong between him and another child, go through it calmly afterwards: what each person said, what each person thought. Drawing it out helps.'",
  "'Check his reading comprehension for inference — why characters do things, what they're feeling. He may decode perfectly and still miss the point.'",
  "'Watch for teasing he doesn't recognise as teasing, and \"friends\" who aren't.'",
 ],

 "explain_child": [
  "YOUNGER: 'Everyone has hidden rules for talking and playing — like taking turns, or knowing when someone is joking. Some people's brains don't pick those up by themselves, so we learn them on purpose. You're not doing anything wrong.'",
  "OLDER: 'Social communication is all the unwritten stuff — sarcasm, reading faces, knowing when to change the subject. Some people find it harder to pick up. It's not about being clever or kind; you just learn it a different way, and you can ask people what they meant.'",
  "TEACH A CHECKING SENTENCE: 'Are you joking?' or 'Do you mean that literally?' — practise it. Children with pragmatic difficulties often do not know they are allowed to ask.",
  "ASK: 'Who do you like spending time with?' and 'What happens at break?' and 'Has anyone ever said something that confused you — you weren't sure if they meant it?'",
  "BE LITERAL YOURSELF in the session: plain questions, no sarcasm, explain any idiom you use. Watch whether the child picks up on your non-verbal cues — that is data too.",
 ],

 "analogies": [
  "THE INVISIBLE RULEBOOK: 'Everyone else seems to have been handed a rulebook for conversations, but his copy was never delivered — so we're writing one out for him.' Good with parents, teachers and older children; non-blaming.",
  "THE FOREIGN CULTURE: 'Imagine moving to a country where you speak the language well, but nobody tells you the customs — when to shake hands, what's a joke, how close to stand.' Good with teachers; separates language structure from language use.",
  "SUBTITLES WITHOUT TONE: 'She gets the words but not the tone of voice or the look that goes with them — like reading a text message and missing the sarcasm.' Good with adolescents; very familiar.",
  "THE REFEREE: 'In conversation there's a referee blowing the whistle for turns and topic changes — she can't hear the whistle, so we make it visible.' Good for explaining visual supports for turn-taking to younger children and staff.",
 ],

 "language": [
  "'Social (pragmatic) communication disorder (SPCD)' is the DSM-5-TR term (APA, 2022). Also seen: 'social communication disorder (SCD)'. ICD-11 has no separate category; the nearest is DLD with mainly pragmatic impairment — say so if a report uses ICD.",
  "Older terms: 'semantic-pragmatic disorder' and 'pragmatic language impairment (PLI)' (Bishop, 2000). Explain them if they appear in file history.",
  "Present it with appropriate uncertainty: 'SPCD, a DSM-5 diagnosis whose relationship to autism is still debated (Norbury, 2014)'. Do not present it as either 'nearly autism' or 'definitely not autism'.",
  "Avoid 'rude', 'odd', 'inappropriate' and 'lacks social skills' in reports. Describe the behaviour and the context: 'continued talking about trains after peers turned away'.",
  "Describe strengths — honesty, knowledge, rule-following, loyalty — alongside difficulties.",
 ],

 "red_flags": [
  "RED FLAG — LOSS of social or language skills the child previously had (regression). Not SPCD. Medical referral via GP / paediatrics without delay.",
  "RED FLAG — history or current evidence of restricted/repetitive behaviours, intense interests or sensory differences in a child with an SPCD label. Autism may not have been adequately considered — raise it and refer to CDNT.",
  "RED FLAG — vulnerability to exploitation: a child or adolescent who takes things literally and wants friends may be targeted, including online and sexually. Children First procedures the same day if abuse or exploitation is suspected; report to Tusla as soon as practicable — telling the DLP does not discharge a mandated person's own duty.",
  "RED FLAG — social isolation with low mood, self-harm or suicidal thoughts in an adolescent. Same-day risk route per service procedure.",
  "BOUNDARY — you do not diagnose SPCD or rule autism in or out. You describe social communication in context and refer for multidisciplinary assessment. PSI 2.2.2.",
  "WATCH — cultural and linguistic difference, and trauma or attachment difficulties, which can both produce social-communication differences. Get the history before interpreting.",
 ],

 "child_voice": [
  "FRIENDSHIP INTERVIEW / DRAWING ('draw you and the people you like at school') — good because it shows who the child thinks their friends are, which may differ from what adults see.",
  "COMIC-STRIP CONVERSATIONS (Gray, 1994) — simple drawings with speech and thought bubbles. Good because they make hidden thoughts visible and let the child explain their view of a social event without having to read cues in real time.",
  "SCALING ('how easy is break time / group work / class?') — good because it gives a concrete answer to an abstract question and a hierarchy for planning.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it is Irish and familiar; add prompts about break and friends. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "OBSERVATION IN THE YARD — good because the child's voice includes what they do when no adult is structuring it; often the most revealing data.",
 ],

 "questions": [
  "Q: 'Is it autism or not?' — A: 'The diagnostic manual says social communication disorder is diagnosed when there are social communication difficulties WITHOUT the repetitive behaviours, narrow interests or sensory differences seen in autism, now or earlier. Researchers still debate how separate the two really are. The team's job is to look at the whole history; mine is to describe what she needs.'",
  "Q: 'Will this diagnosis get him the same support as autism?' — A: 'Not always — some provision in Ireland has been linked to an autism diagnosis. That's a question for the school and SENO under the current criteria. What I can do is describe his needs clearly so support is based on them.'",
  "Q: 'Isn't he just shy?' — A: 'Shy children usually know the rules and hold back. He talks readily but misses cues — like when someone wants to change topic. That's a different thing, and it responds to being taught directly.'",
  "Q: 'Why didn't anyone notice before?' — A: 'Social demands rise with age. In infants, play is simple and adults organise it. By fourth or fifth class, friendships run on jokes, hints and unspoken rules — that's when these difficulties show.'",
  "Q: 'Can you diagnose it?' — A: 'No — it's diagnosed by a speech and language therapist, usually as part of a team that has also thought about autism. I can describe how communication is going in class and the yard, and make the referral with that information.'",
 ],

 "supervision": [
  "Bring a case with an SPCD label and discuss whether autism appears to have been fully considered, and how to raise that without undermining a colleague's report.",
  "Ask how your supervisor writes about contested diagnoses — what hedging is appropriate in a report for parents and schools.",
  "Discuss how to observe social communication in unstructured time and what to record.",
  "Ask about local practice: does the CDNT diagnose SPCD, and what are the implications for NCSE provision in this area?",
  "Bring a case where cultural or linguistic difference might explain social-communication differences, and discuss how to separate difference from difficulty.",
 ],

 "reflection": [
  "ON THE AUTISM BOUNDARY — Did I ask about restricted and repetitive behaviours and sensory differences in the history, or only about current social communication?",
  "ON CERTAINTY — Did I present SPCD as more settled than the evidence allows? Did I state the debate honestly and simply?",
  "ON STRUCTURE VS USE — Did I check structural language (or ask the SLT) before attributing difficulties to pragmatics?",
  "ON CONTEXT — Did I observe the child in the yard or group work, or only in a quiet room with me — where pragmatic difficulties often disappear?",
  "ON CULTURE — Did I judge the child's communication against their own community's norms?",
  "WHAT GOOD LOOKS LIKE: 'Referral: \"rude to teachers, no friends\". Observation showed literal interpretation and topic persistence in the yard; parent history had no repetitive behaviours or sensory differences. I described the communication, recommended explicit teaching of conversation rules and structured break time, and referred to CDNT noting both SPCD and autism should be considered.'",
  "WHAT POOR LOOKS LIKE: 'Presentation is consistent with SPCD rather than autism.' — an EP drawing a diagnostic conclusion on a contested boundary, without developmental history of RRBs and without multidisciplinary input.",
 ],

 "citations": [
  "American Psychiatric Association. (2022). Diagnostic and statistical manual of mental disorders (5th ed., text rev.) — Social (Pragmatic) Communication Disorder.",
  "Norbury, C. F. (2014). Practitioner review: Social (pragmatic) communication disorder conceptualization, evidence and clinical implications. Journal of Child Psychology and Psychiatry, 55(3), 204–216.",
  "Swineford, L. B., Thurm, A., Baird, G., Wetherby, A. M., & Swedo, S. (2014). Social (pragmatic) communication disorder: A research review of this new DSM-5 diagnostic category. Journal of Neurodevelopmental Disorders, 6(1), 41.",
  "Gibson, J., Adams, C., Lockton, E., & Green, J. (2013). Social communication disorder outside autism? A diagnostic classification approach to delineating pragmatic language impairment, high functioning autism and specific language impairment. Journal of Child Psychology and Psychiatry, 54(11), 1186–1197.",
  "Mandy, W., Wang, A., Lee, I., & Skuse, D. (2017). Evaluating social (pragmatic) communication disorder. Journal of Child Psychology and Psychiatry, 58(10), 1166–1175.",
  "Bishop, D. V. M. (2000). Pragmatic language impairment: A correlate of SLI, a distinct subgroup, or part of the autistic continuum? In D. V. M. Bishop & L. B. Leonard (Eds.), Speech and language impairments in children: Causes, characteristics, intervention and outcome (pp. 99–113). Psychology Press.",
  "Adams, C., Lockton, E., Freed, J., Gaile, J., Earl, G., McBean, K., Nash, M., Green, J., Vail, A., & Law, J. (2012). The Social Communication Intervention Project: A randomized controlled trial of the effectiveness of speech and language therapy for school-age children who have pragmatic and social communication problems with or without autism spectrum disorder. International Journal of Language & Communication Disorders, 47(3), 233–244.",
  "Gray, C. (1994). Comic strip conversations. Future Horizons.",
  "World Health Organization. (2019). International classification of diseases (11th rev.) — 6A01.2 Developmental language disorder (sub-codes).",
 ],

 "pathway": {
  "age": "Rarely identified before about 4, because adequate speech and language are needed first (APA, 2022 — check text). Most often noticed in middle to late primary, when friendships start to depend on jokes, hints and shared unspoken rules, or at the move to post-primary. Usually arrives in school via a CDNT or SLT report following an assessment in which autism was considered.",
  "who_diagnoses": "Ireland: a Speech and Language Therapist, usually within a multidisciplinary assessment (often CDNT) that has also considered autism; sometimes private SLT or multidisciplinary teams. Assessment of Need (Disability Act 2005) may be the route. The EP does not diagnose — and should not settle the autism question.",
  "who_wrote_report": "CDNT multidisciplinary report; HSE Primary Care SLT; private SLT or private multidisciplinary assessment; occasionally a CAMHS report. Check whether the report documents a developmental history of restricted/repetitive behaviours — that is where the SPCD/autism line is drawn.",
  "refer_to": "SLT via Primary Care, or CDNT where autism is being considered or needs are complex — check local criteria. GP → Primary Care Psychology or CAMHS where anxiety or mood is significant. GP / paediatrics for any regression.",
  "sooner": "'These difficulties often don't show until friendships get more complicated, around the middle of primary school. It's very common not to notice earlier — and these are skills that can be taught at any age.'",
 },

 "differential": [
  "AUTISM — social-communication difficulty PLUS restricted/repetitive behaviours, interests or sensory differences, current or past. The boundary is debated (Norbury, 2014). Refer to CDNT.",
  "DLD — structural language difficulty explaining the social difficulty; get SLT view.",
  "ADHD — impulsivity and inattention driving conversational difficulty; child usually knows the rule.",
  "SOCIAL ANXIETY / SHYNESS — knows the rules, avoids using them.",
  "TRAUMA / ATTACHMENT DIFFICULTY — relational difficulty rooted in early experience; take a careful history.",
  "CULTURAL OR LINGUISTIC DIFFERENCE — different pragmatic norms, not disorder.",
  "INTELLECTUAL DISABILITY — broader difficulty; adaptive functioning also affected.",
 ],

 "next": [
  "Observe the child in unstructured time (yard, group work) as well as in class.",
  "Get the SLT or CDNT report and check whether restricted/repetitive behaviours were considered in the history.",
  "Check structural language and inference in reading comprehension.",
  "Write social-communication recommendations with named adult, frequency, setting and review date at the right Continuum level.",
  "Refer to CDNT if autism has not been adequately considered.",
 ],

 "presentations": [
  "Peer relationship difficulties and social isolation",
  "Turn-taking and shared play",
  "Reading social cues and repair after conflict",
  "Co-operation with peers in group work",
  "Bullying",
  "Loneliness without observable difficulty",
  "Masking and the cost of it",
 ],

 "bands": {
  "Early Years": {
   "applies": "RARELY — diagnosis rarely made before about 4 (APA, 2022 — check)",
   "prevalence": "Not established for this band — rate not stated here, check.",
   "see": "Social communication difficulties in preschool are usually described rather than labelled, and autism assessment is the more common route. Note turn-taking, joint attention, response to name and play, and refer to CDNT where concerns are significant.",
   "tools": ["Ages & Stages Questionnaires (ASQ-3)", "Preschool Language Scales-5 (PLS-5)", "SCQ (Social Communication Questionnaire)"],
  },
  "School Age": {
   "applies": "YES — the main window for identification",
   "prevalence": "Not established — estimates vary with definition (Swineford et al., 2014); check before quoting.",
   "see": "Talking at rather than with peers, going off-topic, missing jokes and sarcasm, literal interpretation, conflict in the yard and group work, weak inference in reading. Appears as friendships become more verbal and subtle (middle to senior primary).",
   "tools": ["CELF-5 UK", "SRS-2", "SCQ", "SDQ", "YARC (York Assessment of Reading for Comprehension)",
             "Children's Communication Checklist-2 (CCC-2; Bishop, 2003) — AGE 4–16 (check manual) · MEASURES: parent/professional ratings of structural and pragmatic language · CANNOT TELL YOU: diagnosis, or whether autism is present · TIME: 10–15 min informant"],
  },
  "Adolescent": {
   "applies": "YES — difficulties often most visible as social demands peak",
   "prevalence": "Not established — rate not stated here, check.",
   "see": "Difficulty with sarcasm, banter, group chats and shifting peer norms; isolation or being targeted; literal reading of rules leading to conflict with staff. Vulnerability online. Anxiety and low mood become concerns.",
   "tools": ["SRS-2", "RCADS self-report", "MFQ (Mood and Feelings Questionnaire)", "CELF-5 UK"],
  },
  "Young Adult": {
   "applies": "YES — persists; affects further education, work and relationships",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Difficulty with workplace and course social norms, interviews and group projects. Adults may seek autism assessment later; the boundary question remains. The EP role is usually time-limited here.",
   "tools": ["SRS-2 adult form", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "RARELY — as a stand-alone diagnosis; pragmatic difficulties usually sit within autism or ID",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "In special settings, pragmatic difficulty is more often described as part of autism or ID. If a pupil carries an SPCD label, check whether the class approach (e.g. an autism class) matches their profile and whether the label was reviewed.",
   "tools": ["Vineland-3 / ABAS-3", "Communication Matrix / AAC review"],
  },
 },
},

]
