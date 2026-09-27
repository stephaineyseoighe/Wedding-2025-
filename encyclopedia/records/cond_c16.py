# CONDS records: Hearing impairment, Visual impairment, Recurrent otitis media with effusion (glue ear).
# Format: SCHEMAS.md "CONDS". Validate with: python3 check_records.py records/cond_c16.py
# These are medical / sensory conditions, not DSM diagnoses. The EP does not diagnose them;
# the EP makes sure they have been ruled in or out BEFORE cognitive, language or literacy
# conclusions are drawn, adapts assessment, and writes for access.

_CORU = "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32"
_PSI = "2.2.2 · 2.3.1 · 2.3.3 · 1.3.1 · 1.2.8"

CONDS = [

# =====================================================================================
# 1. HEARING IMPAIRMENT
# =====================================================================================
{
 "name": "Hearing impairment (Deaf / hard of hearing)",
 "code": "Not a DSM diagnosis · sensory impairment (medical) · ICD-11: hearing loss codes sit in Chapter 10, Diseases of the ear or mastoid process (conductive / sensorineural / mixed) — ICD-11 code — check before quoting",
 "neps": "5. OTHER (5.2 Hearing) — and 1. LEARNING (1.2 Language skills · 1.4 Literacy) where access to spoken language is affected",
 "coru": _CORU,
 "psi": _PSI,
 "law": "EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Irish Sign Language Act 2017 · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR",

 "what_it_is": [
  "A reduction in the ability to detect or discriminate sound, measured by an audiologist and described on an audiogram by DEGREE (how loud a sound must be before it is heard, in dB HL), TYPE (conductive, sensorineural or mixed), LATERALITY (unilateral or bilateral) and CONFIGURATION (which frequencies are affected).",
  "DEGREE bands differ by source. The WHO (2021, World Report on Hearing) grades from mild through moderate, moderately severe, severe, profound and complete; the British Society of Audiology uses mild / moderate / severe / profound with different dB cut-offs. Always quote the band AND the source from the audiology report itself — do not re-grade from memory.",
  "TYPE matters for the school:\n▸ CONDUCTIVE — sound is blocked on the way in (e.g. glue ear, wax, ossicle problems). Often fluctuating and often treatable.\n▸ SENSORINEURAL — the cochlea or auditory nerve is affected. Usually permanent. Sound is quieter AND distorted, so turning up the volume does not fully fix it.\n▸ MIXED — both.",
  "Permanent childhood hearing impairment is usually identified through the Universal Newborn Hearing Screening Programme (HSE; national coverage completed in the early 2010s — check year before quoting) — but not all loss is present at birth. Progressive and acquired losses (e.g. after meningitis, congenital CMV, some genetic causes) appear later, which is why school-age prevalence is higher than birth prevalence (Fortnum et al., 2001).",
  "Amplification and access: hearing aids, bone-conduction aids, cochlear implants (Ireland: National Cochlear Implant Programme — check current service), and remote-microphone ('radio aid' / 'FM' / digital) systems that carry the teacher's voice directly to the aid. None of these restores typical hearing; all of them depend on the classroom (distance, noise, reverberation).",
  "It is also a LANGUAGE question. More than 90% of deaf children are born to hearing parents (Mitchell & Karchmer, 2004), so most do not have fluent access to a signed language at home from birth. The risk to development is less the hearing loss itself than the risk of limited access to ANY full language in early childhood — 'language deprivation' (Hall, 2017).",
  "Deaf (capital D) also names a cultural and linguistic identity: people whose first or preferred language is Irish Sign Language (ISL) and who see themselves as a linguistic minority rather than as impaired. The Irish Sign Language Act 2017 recognises ISL as a native and independent language of the State — check commencement and the Act's specific duties before quoting them.",
 ],

 "what_it_is_not": [
  "NOT the same as not listening. A child with mild or unilateral loss can hear you one-to-one in a quiet room and miss half of what is said in a noisy classroom. 'He hears when he wants to' is the most common misreading — and the most damaging. Listening in noise is a different task from listening in quiet.",
  "NOT fixed by hearing aids. Aids amplify; in sensorineural loss the signal is still distorted, and aids do little across distance and background noise. Bess et al. (1998) found that even 'minimal' sensorineural loss was associated with poorer educational and functional outcomes — check figures before quoting.",
  "NOT unimportant because it is 'only' one ear. Children with unilateral hearing loss show more educational and speech-language difficulty than hearing peers (Lieu, 2004) — they struggle to locate sound and to hear in noise. Rate not stated here — check.",
  "NOT a cognitive impairment. Non-verbal reasoning in deaf children without additional disabilities is broadly in line with hearing peers (Braden, 1994); low VERBAL scores reflect access to spoken language, not ability. A verbal IQ for a deaf child can measure hearing, not thinking.",
  "NOT something sign language 'holds back'. The fear that signing delays speech is not supported; early access to a full language — signed or spoken — protects language, cognitive and social development (Hall, 2017). Families choose communication approaches; the EP supports the choice with evidence, not preference.",
  "NOT a single group. A profoundly deaf ISL user, a child with a cochlear implant in an oral mainstream class, and a child with a moderate loss and hearing aids have very different needs. Describe the individual child's access, not 'deafness'.",
  "NOT something the EP diagnoses or grades. Audiology (HSE Community / Paediatric Audiology) and ENT do. The EP asks: has hearing been checked, when, what was found, and what does that mean for how I assess and what I recommend?",
 ],

 "prevalence": [
  "AT BIRTH: permanent childhood hearing impairment of moderate degree or worse is roughly 1 per 1,000 live births; Fortnum et al. (2001) reported about 1.07 per 1,000 at birth in a UK ascertainment study.",
  "BY SCHOOL AGE: prevalence rises — Fortnum et al. (2001) estimated about 1.65 per 1,000 at ages 9–16, reflecting late-onset, progressive and acquired losses. Screening at birth does not mean hearing is settled for life.",
  "MILD AND UNILATERAL LOSS: much more common than moderate-to-profound bilateral loss and much more often missed. Bess et al. (1998) estimated minimal sensorineural loss in about 5% of a US school sample — check exact figure and definition before quoting.",
  "PARENTS: more than 90% of deaf children have hearing parents (Mitchell & Karchmer, 2004).",
  "IRELAND: no Irish population prevalence figure is cited here — check before quoting. NCSE Visiting Teacher caseloads and HSE audiology figures reflect service contact, not prevalence.",
  "ADDITIONAL NEEDS: a substantial minority of deaf children have additional disabilities (e.g. from prematurity, CMV, syndromes). Rate not stated here — check before quoting.",
 ],

 "cooccurring": [
  {"name": "LANGUAGE DISORDER ASSOCIATED WITH HEARING LOSS",
   "rate": "CATALISE classifies language disorder with sensorineural hearing loss as 'associated with' rather than DLD (Bishop et al., 2017) — rate not stated here, check",
   "presents": "Limited vocabulary, simplified grammar and weak narrative, sometimes out of proportion to the degree of loss. Ask whether language is behind what the audiogram and the child's amplification history would predict — if so, SLT with hearing-impairment experience should assess."},
  {"name": "SOCIAL, EMOTIONAL AND MENTAL HEALTH DIFFICULTY",
   "rate": "elevated in deaf children and adults (Fellinger et al., 2012) — rate not stated here, check",
   "presents": "Isolation at break times, frustration, withdrawal, low mood, or behaviour that follows missed communication. Often linked to communication access at home and in school rather than to deafness itself. Screening tools normed on hearing children may not be valid — say so."},
  {"name": "ADHD (as differential as much as co-occurrence)",
   "rate": "rate not stated here — check; attention difficulty is hard to separate from access",
   "presents": "Looking around, missing instructions, following peers, fatigue by afternoon. A deaf child must watch faces, interpreters and the board at once — visual attention is doing the work of hearing. Do not attribute to ADHD until access has been fixed and observed."},
  {"name": "AUTISM",
   "rate": "reported as higher in deaf children than hearing peers — rate not stated here, check",
   "presents": "Social communication difference that can be masked or mimicked by limited language access. Assessment needs clinicians experienced with deaf children, and in the child's own language (ISL where relevant). Risk of both over- and under-identification."},
  {"name": "INTELLECTUAL DISABILITY / MULTIPLE DISABILITIES",
   "rate": "rate not stated here — check; linked to causes such as prematurity, CMV and some syndromes",
   "presents": "Global rather than language-specific delay across verbal and non-verbal tasks and adaptive functioning. Use non-verbal and adaptive measures, and be cautious — language deprivation can depress scores on 'non-verbal' tests that still need instructions to be understood."},
  {"name": "VISUAL IMPAIRMENT / DEAFBLINDNESS (dual sensory impairment)",
   "rate": "rare — rate not stated here, check (e.g. Usher syndrome, CHARGE syndrome, congenital rubella)",
   "presents": "A deaf child who relies on vision for signing, lipreading and the board loses the compensating sense. Night-vision or field loss in a deaf adolescent is a reason to ask about eye review. Refer for specialist dual-sensory advice."},
  {"name": "BALANCE / MOTOR DIFFICULTY",
   "rate": "associated with some causes of sensorineural loss (vestibular involvement) — rate not stated here, check",
   "presents": "Late walking, clumsiness in PE, difficulty on uneven ground or in the dark. Can be mistaken for DCD. Ask the audiology or ENT report whether vestibular function has been assessed."},
 ],

 "recommendations": [
  "START WITH ACCESS, NOT DEFICIT. State the child's hearing status from the audiology report (degree, type, laterality, date), what amplification they use and whether it is worn and working. If the most recent audiology is more than a year old, or there are new concerns, recommend review before anything else.",
  "SEATING AND LINE OF SIGHT: near the teacher, away from noise sources (corridor, projector fan, window onto the yard), with light on the speaker's face not behind them, and the better ear towards the teaching. A seat in the front row is not enough if the teacher teaches from the back.",
  "REMOTE MICROPHONE / RADIO AID: if prescribed, specify who charges and checks it, that the teacher wears it for ALL teaching talk, and that it is passed to peers during discussion. Unused equipment is the commonest gap.",
  "CLASSROOM ACOUSTICS: soft furnishings, felt pads on chair legs, doors closed, background noise reduced. Ask the Visiting Teacher about an acoustic check and whether the school is eligible for any works — check current Department / NCSE process.",
  "TEACHING: face the class when talking; do not talk while writing on the board; repeat peers' answers; pre-teach vocabulary; captions ON for all video; key instructions written as well as said; check understanding by asking the child to show or tell back, never 'did you hear?'",
  "COMMUNICATION APPROACH: follow the family's chosen approach (spoken English, ISL, or both). Where ISL is the child's language, recommendations must name who provides ISL access and how staff communicate directly with the child — check the Department's current ISL supports for pupils and eligibility.",
  "FATIGUE: build in listening breaks; concentrated listening and lipreading are exhausting ('listening fatigue'). Expect performance to drop late in the day and say so to the teacher.",
  "CONTINUUM LEVEL: Classroom Support for seating, acoustics and teaching adaptations; School Support for pre-teaching and targeted language work; School Support Plus where the Visiting Teacher, SLT or audiology are involved. Special class / special school for Deaf pupils is an option for some children — placement via SENO; check current provision and criteria.",
  "EXAMS: flag early for RACE (post-primary) — e.g. modified aural components or ISL — check the current SEC scheme. For primary, flag access needs for standardised tests.",
  "REFER: AUDIOLOGY via GP / HSE Primary Care if hearing has not been checked recently or there is a new concern. NCSE VISITING TEACHER SERVICE (Deaf / hard of hearing) — check current referral route. SLT (Primary Care or CDNT). CDNT where additional needs are complex.",
  "DO NOT report a Full Scale IQ for a deaf child without stating how instructions were given and whether verbal subtests measure access rather than ability; do not recommend 'more listening'; do not describe a communication choice as the cause of difficulty.",
 ],

 "explain_parent": [
  "'What I need from the audiology report is not just the result but what it means in a classroom — how far away he can hear the teacher, and how much the noise in a room of 28 children takes away.'",
  "'Hearing aids help a lot, but they don't make hearing typical. In a noisy room, across a distance, he will miss parts of what's said even when they're working perfectly — so the room and the teaching need to change as well.'",
  "'His non-verbal reasoning is right in line with children his age. The lower verbal scores show how much spoken English he has had access to, not how bright he is.'",
  "'However you communicate at home — spoken English, Irish Sign Language, or both — the most important thing is that he has full, easy access to a language every day. We'll build school support around what you've chosen.'",
  "'Tiredness at the end of the day is real. Listening and lipreading all day uses a lot of energy — it isn't laziness if homework is hard at 4 o'clock.'",
  "SIGNPOST: the child's audiologist; the NCSE Visiting Teacher; Chime (national charity for deafness and hearing loss) and the Irish Deaf Society (Deaf community and ISL) — check current names and services; ISL classes for families (check local availability).",
 ],

 "explain_teacher": [
  "'When she doesn't respond, the first hypothesis is that she didn't hear it — or heard it but couldn't make out the words. Check before you conclude anything else.'",
  "'Your voice gets weaker the further you are from her and the more noise there is. The radio aid solves the distance problem, but only if you're wearing it — and only for your voice. Repeat what other children say.'",
  "'Face her when you talk. Don't talk while writing on the board or walking round behind her. She's using your face as much as her ears.'",
  "'Captions on for every video, key instructions written down, new words taught before the lesson. These cost you almost nothing and they help half the class.'",
  "'\"Did you hear me?\" will get a yes. Ask her to tell you back or show you what she's going to do.'",
  "'Group work and class discussion are the hardest parts of the day for her — lots of voices, fast turn-taking, no warning who'll speak next. Name who's speaking and slow the pace.'",
 ],

 "explain_child": [
  "YOUNGER: 'Your ears work differently, so some sounds are quiet or fuzzy for you. Your hearing aids help. It's OK to tell your teacher when you didn't catch something — that's a clever thing to do, not a naughty thing.'",
  "OLDER: 'Your hearing means noisy rooms and people talking from far away are harder for you. That's about sound, not about how clever you are. You're allowed to ask for what helps — the radio aid, a good seat, captions, notes.'",
  "FOR A DEAF CHILD WHO SIGNS: explain through a qualified ISL interpreter or in ISL — not through an SNA with basic signing, and not by writing it down in English, which may be the child's second language.",
  "TEACH A SELF-ADVOCACY SENTENCE: 'Can you say that again, facing me?' or 'Can you write the key word?' Practise it. Many deaf children pretend to have understood to avoid standing out.",
  "ASK: 'Where in school is it hardest to hear? Where is it easiest?' and 'Does the radio aid get used?' — use a drawn map of the school if expressive language is limited.",
  "CHECK YOUR SETTING: quiet room, light on your face, sit opposite not beside, confirm aids are on and working before you start.",
 ],

 "analogies": [
  "THE CONVERSATION IN A BUSY RESTAURANT: 'You catch most of it when you lean in, but when the table next to you laughs you lose a sentence and fill in the gaps by guessing. Now do that all day, every day.' Good with parents and teachers; explains fatigue and errors.",
  "THE RADIO WITH THE TREBLE TURNED DOWN: 'For many children with hearing loss it isn't just quieter — the high sounds like s, f and th go. \"Fish\", \"fifth\" and \"fit\" start to sound the same.' Good for explaining sensorineural loss and phonics difficulty.",
  "THE PHONE CALL WITH A BAD LINE: 'Turning the volume up doesn't fix a crackly line — it makes the crackle louder too. That's why hearing aids help but don't solve it.' Good for teachers who assume aids = typical hearing.",
  "A FIRST LANGUAGE, NOT A FALLBACK: 'For a Deaf child who signs, ISL is like Polish for a Polish child — it's their language, and English is being learned on top.' Good with teachers and SNAs; reframes signing.",
 ],

 "language": [
  "'Deaf' (capital D) — a person who identifies with the Deaf community and uses ISL; 'deaf' (lower case) — the audiological fact of hearing loss; 'hard of hearing' — often used by people with mild–moderate loss who use spoken language. Ask the family and young person which they use and follow them.",
  "Many Deaf people prefer identity-first language ('a Deaf child', 'Deaf people') over 'person with hearing impairment'. 'Hearing impairment' is the medical and NEPS category term — use it for the category heading, and the family's preferred term for the child.",
  "NEVER use 'deaf and dumb', 'deaf-mute', 'suffers from deafness' or 'hearing-impaired' as a description of a Deaf ISL user — these are experienced as offensive or deficit-framing.",
  "Say 'uses ISL', 'uses spoken English', 'uses hearing aids / a cochlear implant' — describe the child's communication, not their 'problem'.",
  "Write 'Irish Sign Language (ISL)', not 'sign' or 'signing'. It is a full language with its own grammar, not signed English.",
 ],

 "red_flags": [
  "RED FLAG — SUDDEN hearing loss, or a sudden drop reported by the child or noticed by staff. Same-day advice from GP; sudden sensorineural loss is treated as urgent. Do not wait for a routine audiology appointment.",
  "RED FLAG — ear pain, discharge, or hearing aids suddenly 'not working' with no equipment fault — GP.",
  "RED FLAG — PROGRESSIVE decline (responses worsening over months, new speech errors). Some causes of sensorineural loss are progressive; re-refer to audiology and tell the Visiting Teacher.",
  "RED FLAG — disclosure, or signs of abuse, in a deaf child. Disabled children are at substantially greater risk of violence (Jones et al., 2012 — rate not quoted here, check) and deaf children may have no adult who shares their language. Follow Children First the same day; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty. Use a qualified ISL interpreter — never a family member or peer.",
  "BOUNDARY — you do not grade hearing, interpret an audiogram beyond what the report states, or advise on aids, implants or communication mode as a clinician. You describe classroom access and the child's learning, and refer. PSI 2.2.2.",
  "WATCH — assessment validity. A verbal battery administered in spoken English to a deaf child, or through an unqualified signer, may be invalid. Record exactly how instructions were delivered and report scores descriptively where the standardisation does not hold.",
  "WATCH — hearing aids or radio aid not worn in school. Find out why (discomfort, stigma, broken, not charged) before recommending anything else.",
 ],

 "child_voice": [
  "QUALIFIED ISL INTERPRETER for Deaf children who sign — good because it gives the child their own language rather than a watered-down channel. Book through a registered interpreter service (RISLI — Register of Irish Sign Language Interpreters; check current booking route) and brief them in advance on the purpose of the session.",
  "TALKING MATS — picture-symbol framework ('like / not sure / don't like') — good because it reduces the spoken-language demand of giving a view and works across communication modes. → https://www.talkingmats.com/",
  "A DRAWN MAP OF THE SCHOOL DAY OR BUILDING, where the child marks places where hearing is easy or hard — good because it locates the difficulty in the environment, which is where the recommendations will go.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — read it together face to face in good light, or with an interpreter — good because it is familiar in Irish schools and gives a baseline. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "ASK THE CHILD ABOUT THEIR EQUIPMENT AND IDENTITY — 'What do you want your teacher to know about your hearing?' — good because older children often have strong views about radio aids, visibility and Deaf identity that adults never ask.",
 ],

 "questions": [
  "Q: 'He passed the newborn hearing screen — surely his hearing is fine?' — A: 'The newborn screen is very good at picking up hearing loss present at birth, but some loss develops later or gets worse over time, and glue ear comes and goes. If there's any doubt now, a fresh audiology check is worth doing before we draw conclusions about language or learning.'",
  "Q: 'She has hearing aids — why does she still miss things?' — A: 'Aids make sounds louder, but they can't make them clearer if the inner ear is affected, and they struggle with distance and noise. That's why the seat, the radio aid and how the teacher talks all matter.'",
  "Q: 'Will signing stop him learning to talk?' — A: 'The research doesn't show that. What matters most is that he has full access to a language early. Many children use both. It's your family's choice, and school should support whatever you decide.'",
  "Q: 'Why are his verbal scores so low if he's bright?' — A: 'Verbal tests measure what he has picked up through hearing spoken English. With a hearing loss, that's less. His non-verbal scores are a better guide to his reasoning, and I've reported them separately for that reason.'",
  "Q: 'Can you diagnose his hearing loss / tell us what degree it is?' — A: 'No — that's audiology's job. What I can do is read their report with you, explain what it means in the classroom, and make sure the school's support matches it.'",
  "Q: 'Does she need a special school?' — A: 'Some Deaf children thrive in a signing environment with Deaf peers; others do well in mainstream with the right support. It depends on her language, her needs and what you want for her. The Visiting Teacher and the SENO can talk you through what's available — I can't promise a place.'",
  "Q: 'Is it the hearing or is it ADHD?' — A: 'We need to fix access first and then look again. If the attention difficulty is still there when she can hear and see the teaching properly, we look further. Otherwise we risk labelling a hearing problem as an attention problem.'",
 ],

 "supervision": [
  "Bring a case where hearing status was not recorded on the referral, and ask how your supervisor makes sure audiology is established before an assessment is booked.",
  "Ask how the local NCSE Visiting Teacher Service links with NEPS in this region — who contacts whom, and whether joint visits happen.",
  "Discuss which cognitive measures the service uses with deaf children, how instructions are delivered, and how scores are reported when standardisation does not hold.",
  "Ask about the service's process for booking ISL interpreters and what to do if one is not available.",
  "Reflect on your own assumptions about Deafness — medical model versus cultural-linguistic model — and how they show in your report language.",
 ],

 "reflection": [
  "ON HEARING STATUS — Did I know the date and result of the last audiology check before I started? If not, what did I assume?",
  "ON VALIDITY — How did the child receive instructions? Did I record it at the time? Did I report scores as normative when they should have been descriptive?",
  "ON LANGUAGE — Did I interpret low verbal scores as low ability, or as low access? Did my report make the difference clear to a reader who is not a psychologist?",
  "ON THE CHILD'S VOICE — Did I get the child's view in their own language, or did I settle for what the adults told me?",
  "ON IDENTITY — Did my language respect the family's view of deafness (medical or cultural)? Would a Deaf adult reading my report find it respectful?",
  "WHAT GOOD LOOKS LIKE: 'Audiology from six weeks ago confirmed a moderate bilateral sensorineural loss. I assessed in a quiet room with the radio aid on, used a non-verbal measure with pictorial instructions, and reported the verbal index as a measure of access. Recommendations named the radio aid, seating, captions and pre-teaching, with the Visiting Teacher as named contact.'",
  "WHAT POOR LOOKS LIKE: 'Verbal comprehension was in the very low range, indicating significant difficulties with verbal reasoning.' — no mention of hearing, no adaptation recorded, no Visiting Teacher or audiology link.",
 ],

 "citations": [
  "Bess, F. H., Dodd-Murphy, J., & Parker, R. A. (1998). Children with minimal sensorineural hearing loss: Prevalence, educational performance, and functional status. Ear and Hearing, 19(5), 339–354.",
  "Bishop, D. V. M., Snowling, M. J., Thompson, P. A., Greenhalgh, T., & CATALISE-2 consortium. (2017). Phase 2 of CATALISE: A multinational and multidisciplinary Delphi consensus study of problems with language development: Terminology. Journal of Child Psychology and Psychiatry, 58(10), 1068–1080.",
  "Braden, J. P. (1994). Deafness, deprivation, and IQ. Plenum Press.",
  "Fellinger, J., Holzinger, D., & Pollard, R. (2012). Mental health of deaf people. The Lancet, 379(9820), 1037–1044.",
  "Fortnum, H. M., Summerfield, A. Q., Marshall, D. H., Davis, A. C., & Bamford, J. M. (2001). Prevalence of permanent childhood hearing impairment in the United Kingdom and implications for universal neonatal hearing screening: Questionnaire based ascertainment study. BMJ, 323(7312), 536–540.",
  "Hall, W. C. (2017). What you don't know can hurt you: The risk of language deprivation by impairing sign language development in deaf children. Maternal and Child Health Journal, 21(5), 961–965.",
  "Jones, L., Bellis, M. A., Wood, S., Hughes, K., McCoy, E., Eckley, L., Bates, G., Mikton, C., Shakespeare, T., & Officer, A. (2012). Prevalence and risk of violence against children with disabilities: A systematic review and meta-analysis of observational studies. The Lancet, 380(9845), 899–907.",
  "Lieu, J. E. C. (2004). Speech-language and educational consequences of unilateral hearing loss in children. Archives of Otolaryngology–Head & Neck Surgery, 130(5), 524–530.",
  "Marschark, M., & Hauser, P. C. (2012). How deaf children learn: What parents and teachers need to know. Oxford University Press.",
  "Mitchell, R. E., & Karchmer, M. A. (2004). Chasing the mythical ten percent: Parental hearing status of deaf and hard of hearing students in the United States. Sign Language Studies, 4(2), 138–163.",
  "Irish Sign Language Act 2017. Government of Ireland (irishstatutebook.ie) — check commencement and current duties.",
  "World Health Organization. (2021). World report on hearing. WHO.",
 ],

 "pathway": {
  "age": "Permanent congenital loss is usually identified in the first weeks through newborn screening and confirmed by audiology in infancy. Later-onset, progressive, mild and unilateral losses are identified later — often at school entry or when classroom listening demands rise — and sometimes only after a referral for language, literacy, attention or behaviour.",
  "who_diagnoses": "Ireland: HSE Audiology (community and paediatric audiology; newborn screening follow-up) and ENT (hospital). Cochlear implant candidacy via the national programme — check current service. GP is usually the route in. The EP does not diagnose or grade hearing loss.",
  "who_wrote_report": "HSE audiologist (audiogram and report); ENT consultant; newborn hearing screening follow-up; NCSE Visiting Teacher (educational advice, not diagnosis); SLT; private audiology. An EP report may describe access and learning but must not be the source of a hearing diagnosis.",
  "refer_to": "Audiology via GP / Primary Care where hearing is not recently checked or there is a new concern; GP same day for sudden loss or ear pain / discharge. NCSE Visiting Teacher Service for children who are Deaf / hard of hearing (check current referral route). SLT (Primary Care or CDNT). CDNT where needs are complex. SENO for special class / school placement or SNA queries.",
  "sooner": "'Hearing loss — especially mild, one-sided or late-developing loss — is easy to miss because children adapt so well. Lots of families only find out when school demands go up. What matters now is that everyone knows, and the classroom is set up for him.'",
 },

 "differential": [
  "GLUE EAR (otitis media with effusion) — conductive, often fluctuating, usually resolving; history of repeated ear infections, blocked ears, snoring.",
  "AUDITORY PROCESSING DIFFICULTY — normal audiogram but difficulty in noise; a contested diagnosis, made by audiology — do not accept or give it on behaviour alone.",
  "DLD — language difficulty with normal hearing; if hearing loss is present, CATALISE calls it 'language disorder associated with hearing loss'.",
  "ADHD / attention difficulty — only after access has been fixed and the attention difficulty persists.",
  "SELECTIVE MUTISM / anxiety — child hears but does not speak in school; audiology still worth confirming.",
  "EAL — limited English with typical hearing; do not confuse limited English exposure with hearing-related limited access.",
 ],

 "next": [
  "Establish hearing status: date and result of last audiology, amplification prescribed and whether worn. Request audiology via GP if not recent.",
  "Contact the NCSE Visiting Teacher (with consent) before you assess, and read their advice.",
  "Plan the assessment: room, lighting, equipment check, mode of instruction (interpreter?), choice of non-verbal measure. Record adaptations at the time.",
  "Observe in the real classroom — noise, distance, where the teacher stands, whether the radio aid is used.",
  "Write recommendations on access (seating, acoustics, equipment, teaching) with named person and review date, at the right Continuum level.",
 ],

 "presentations": [
  "Listening in noise vs listening one-to-one",
  "Classroom acoustics and seating",
  "Hearing history during the years phonics was taught",
  "Listening fatigue",
  "Hearing aid / radio aid not worn in school",
  "Interpreter need and how it changes the assessment",
  "Following multi-step verbal instructions",
  "Participation in oral work and classroom talk",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — congenital loss identified via newborn screening; later-onset and fluctuating loss often first suspected here",
   "prevalence": "About 1 per 1,000 at birth for moderate or worse permanent loss (Fortnum et al., 2001).",
   "see": "Limited response to voice or name, late or unclear speech, reliance on watching faces, frustration, or 'selective' hearing. Check newborn screen outcome, PHN developmental checks and audiology follow-up. Early language access — spoken or ISL — is the priority. Never draw a language or cognitive conclusion before hearing is established.",
   "tools": ["Leiter-3", "Vineland-3", "Griffiths III", "Early communication observation with family's chosen mode — AGE 0–5 · MEASURES: how the child communicates (speech, sign, gesture) in natural play · CANNOT TELL YOU: hearing level or norm-referenced language · TIME: 30–45 min"],
  },
  "School Age": {
   "applies": "YES — main window for identifying mild, unilateral, progressive and missed losses",
   "prevalence": "Permanent loss about 1.65 per 1,000 by age 9–16 (Fortnum et al., 2001); mild / unilateral much more common — check figures.",
   "see": "Misses instructions in noise, follows peers, asks 'what?', tired by afternoon, weak phonics (high-frequency sounds lost), smaller vocabulary, isolation in group talk. Often referred for attention, behaviour or literacy. Verbal indices lower than non-verbal.",
   "tools": ["WNV (Wechsler Non-Verbal)", "Leiter-3", "WISC-V UK", "BPVS-3", "SDQ", "Vineland-3", "SIFTER (Screening Instrument for Targeting Educational Risk) — AGE primary · MEASURES: teacher rating of classroom listening-related risk (academics, attention, communication, participation, behaviour) · CANNOT TELL YOU: hearing level · TIME: 5–10 min (Anderson, 1989 — check current version)"],
  },
  "Adolescent": {
   "applies": "YES — subject demands, exams, identity and equipment refusal come to the fore",
   "prevalence": "Continues from childhood; some acquired / progressive losses first identified here — adolescent rate not stated here, check.",
   "see": "Lectures with fast teacher talk, multiple subject teachers (some wearing the radio aid, some not), oral Irish and language exams, social talk in noisy settings. Stigma may lead to refusing aids. Deaf identity, peer group and ISL may become more important. RACE applications and subject choice are the practical questions.",
   "tools": ["WISC-V UK", "Leiter-3", "WIAT-III UK", "Access arrangements evidence (RACE)", "RCADS self-report"],
  },
  "Young Adult": {
   "applies": "YES — lifelong; access in further / higher education and work",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Lecture capture, captioning, note-takers, ISL interpretation, DARE/DSS supports and workplace adjustments. The young person leads decisions about identity and access. EP role is time-limited; refer to disability services in the college.",
   "tools": ["WAIS-IV UK", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — special schools / classes for Deaf pupils, and deaf pupils with additional disabilities in other special settings",
   "prevalence": "Setting-dependent — not a population figure.",
   "see": "In a Deaf setting, the question is language access, progress and peer community. In other special settings, check whether hearing has been assessed at all (often hard with complex needs), whether aids are worn, and whether a total communication approach (sign, symbols, speech) is used consistently by every adult.",
   "tools": ["Vineland-3 / ABAS-3", "Communication Matrix / AAC review", "Adaptive measure in place of IQ"],
  },
 },
},

# =====================================================================================
# 2. VISUAL IMPAIRMENT
# =====================================================================================
{
 "name": "Visual impairment (blind / partially sighted, including cerebral visual impairment)",
 "code": "Not a DSM diagnosis · sensory impairment (medical) · ICD-11 9D90 Vision impairment including blindness — verify in the ICD-11 browser before quoting",
 "neps": "5. OTHER (5.1 Vision) — and 1. LEARNING (1.4 Literacy · 1.6 Co-ordination) where access to print and movement is affected",
 "coru": _CORU,
 "psi": _PSI,
 "law": "EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR",

 "what_it_is": [
  "A reduction in vision that cannot be corrected to typical levels by glasses or contact lenses, identified by ophthalmology and described by VISUAL ACUITY (detail at distance and near), VISUAL FIELD (how wide an area is seen), and other functions — contrast sensitivity, colour, eye movements, light sensitivity.",
  "The WHO (2019, World Report on Vision) grades distance vision impairment from mild through moderate and severe to blindness, using acuity bands (e.g. worse than 6/12, 6/18, 6/60, 3/60 in the better eye). Quote the band and the source from the eye report — do not re-grade from memory.",
  "UNCORRECTED REFRACTIVE ERROR (short- or long-sightedness, astigmatism) is NOT visual impairment in this sense — it is corrected by glasses — but it is common and is the first thing to rule out before literacy or non-verbal assessment. The Reference sheet lists it as a presentation for this reason.",
  "OCULAR causes (e.g. congenital cataract, albinism, retinal dystrophies, optic nerve hypoplasia, nystagmus) affect the eye and optic nerve. CEREBRAL (cortical) VISUAL IMPAIRMENT (CVI) is caused by damage to or differences in the brain's visual pathways — the eyes may look and test normally while the child cannot make sense of what is seen, especially in clutter (Philip & Dutton, 2014).",
  "CVI is widely described as the leading cause of childhood visual impairment in high-income countries and is common in children born preterm, with cerebral palsy or with hypoxic brain injury (Philip & Dutton, 2014). Williams et al. (2021) found CVI-related vision difficulties in a notable minority of mainstream primary pupils in England — check figure before quoting.",
  "Most children with severe visual impairment have additional impairments or medical conditions (Rahi & Cable, 2003 — check exact figure). The EP will meet visual impairment most often alongside other needs, not alone.",
  "Development follows a different route, not simply a slower one. Vision drives early joint attention, imitation, reaching, walking and concept formation; blind infants reach many milestones by other routes and later (Warren, 1994; Dale & Salt, 2007). Assessment tools built on sighted development can mislead.",
 ],

 "what_it_is_not": [
  "NOT the same as needing glasses. A child whose vision is fully corrected by glasses does not have a visual impairment — but a child who has not had an eye test may be failing at reading for that reason alone. Rule it out first.",
  "NOT ruled out by 'normal eyes'. In CVI the eye examination can be normal. A child who cannot find a named item on a busy page, loses their place, trips on steps or cannot find a parent in a crowd may have CVI. Ask whether a CVI assessment has been considered (ophthalmology / orthoptics).",
  "NOT a cognitive impairment. Blind children without additional disabilities have the same range of intelligence as sighted children. Low scores on visually-loaded subtests measure vision, not reasoning — and should not be given at all where the child cannot see the stimuli.",
  "NOT fixed by enlarging everything. Some children need large print; others (e.g. with field loss) need SMALLER print closer so the whole word fits in their field; some need high contrast, less clutter, or tactile / audio formats. The Visiting Teacher's functional vision assessment tells you which.",
  "NOT autism because of 'blindisms'. Rocking, eye-pressing and hand movements are common in blind children, and some social-communication differences reflect lack of visual access. Autism can co-occur, but needs specialist assessment by clinicians experienced with VI (Tadić et al., 2010).",
  "NOT only a reading issue. Mobility, independence, social interaction (not seeing faces or gestures), PE, practical subjects and fatigue matter as much. The 'expanded core curriculum' — orientation and mobility, independent living, social skills, assistive technology — is part of the child's education (Hatlen, 1996).",
  "NOT something the EP diagnoses. Ophthalmology, orthoptics and optometry do. The EP asks: when were eyes last checked, what was found, and what does that mean for how I assess and what I recommend?",
 ],

 "prevalence": [
  "CHILDHOOD SEVERE VI / BLINDNESS: uncommon. Rahi and Cable (2003, British Childhood Visual Impairment Study) estimated incidence in the UK — figure not quoted here, check before quoting.",
  "CVI: described as the most common cause of childhood visual impairment in high-income countries (Philip & Dutton, 2014); CVI-related vision difficulties were reported in a minority of mainstream primary pupils by Williams et al. (2021) — check exact figure.",
  "REFRACTIVE ERROR: common and rising (myopia in particular) — WHO (2019); rate for Irish children not stated here, check before quoting.",
  "IRELAND: no Irish population prevalence figure is cited here — check before quoting. NCSE Visiting Teacher (visual impairment) caseloads reflect service contact, not prevalence.",
  "ADDITIONAL NEEDS: most children with severe VI have additional impairments (Rahi & Cable, 2003) — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "INTELLECTUAL DISABILITY / MULTIPLE DISABILITIES (MDVI)",
   "rate": "most children with severe VI have additional impairments (Rahi & Cable, 2003) — rate not stated here, check",
   "presents": "Global delay across domains, often with medical and motor needs. It is very easy to under-estimate a child whose vision is not accounted for. Use adaptive measures and observation across settings; avoid visually-loaded tests."},
  {"name": "CEREBRAL PALSY / PREMATURITY (with CVI)",
   "rate": "CVI common in CP and preterm birth (Philip & Dutton, 2014) — rate not stated here, check",
   "presents": "Difficulty finding things in clutter, seeing moving objects, judging depth at steps, recognising faces, and visual fatigue — sometimes with normal acuity. Ask about CVI assessment in any child with CP or extreme prematurity who is struggling visually."},
  {"name": "AUTISM (and autistic-like features)",
   "rate": "reported as higher in congenitally blind children — rate not stated here, check",
   "presents": "Repetitive movements, echolalia, reduced joint attention, preference for routine. Some features follow from lack of visual access rather than autism. Needs assessment by a team experienced with VI; standard tools (e.g. ADOS-2) rely on eye contact and visual materials."},
  {"name": "HEARING IMPAIRMENT (deafblindness / multisensory impairment)",
   "rate": "rare — rate not stated here, check",
   "presents": "A blind child who relies on hearing loses the compensating sense. Check hearing in every child with VI, and vision in every deaf child. Refer for specialist dual-sensory advice."},
  {"name": "MOTOR AND MOBILITY DELAY",
   "rate": "common in congenital VI (Warren, 1994) — rate not stated here, check",
   "presents": "Late walking, cautious movement, difficulty with ball skills, stairs and unfamiliar spaces. Not DCD — the motor difficulty follows from limited visual guidance. Orientation and mobility / habilitation input is the route."},
  {"name": "ANXIETY AND SOCIAL ISOLATION",
   "rate": "rate not stated here — check",
   "presents": "Staying near adults at break, difficulty joining games, missing non-verbal cues, anxiety in new or crowded places, dependence on the SNA. Peer inclusion needs planning — it does not happen by itself."},
  {"name": "SLEEP DIFFICULTY",
   "rate": "circadian rhythm disturbance reported in children with no light perception — rate not stated here, check",
   "presents": "Tiredness, irregular sleep, daytime fatigue that looks like disengagement. Ask about sleep; refer to GP / paediatrics — do not advise on melatonin or medication."},
 ],

 "recommendations": [
  "START WITH ACCESS. State the child's vision status from the eye report (diagnosis, acuity, field, date) and the Visiting Teacher's functional vision advice. If the child has not had an eye examination in the last year, or there is new concern, recommend one before literacy or non-verbal assessment.",
  "PRINT AND MATERIALS: specify format from the functional vision assessment — font size, typeface, contrast, line spacing, reduced clutter, bold lines on paper, matte (non-glare) paper, or Braille / tactile / audio. Materials must arrive at the same time as the class's, not the next day.",
  "SEATING AND LIGHTING: position for the better eye and field, light behind the child not in their eyes, no glare on the whiteboard. Some children (e.g. with albinism or aniridia) are light-sensitive; others need extra task lighting.",
  "BOARD WORK: provide a personal copy or screen-share to a device; do not rely on copying from the board. Say aloud what you write.",
  "ASSISTIVE TECHNOLOGY: magnifiers, screen magnification, text-to-speech, screen reader, braille note-taker, camera to device — as advised by the Visiting Teacher. Apply through the Department's assistive technology scheme via the SENO — check current circular and criteria.",
  "CVI-SPECIFIC: reduce visual clutter on pages and walls, present one item at a time, use consistent layouts and colour-coding, give verbal descriptions of pictures, and allow extra time for visual search. Learn the child's particular pattern — CVI profiles differ widely.",
  "EXPANDED CORE CURRICULUM: plan time for touch-typing, braille, orientation and mobility, independent living skills and social skills (Hatlen, 1996). These are part of the child's education, not extras.",
  "FATIGUE: visual effort is tiring. Build in rest, alternate visual and non-visual tasks, and expect a drop in performance late in the day.",
  "CONTINUUM LEVEL: Classroom Support for seating, lighting and materials; School Support for targeted AT and literacy access; School Support Plus where the Visiting Teacher, ophthalmology, O&M or CDNT are involved. Some children attend a special school for blind / visually impaired pupils — placement via SENO; check current provision.",
  "EXAMS: flag early for RACE (e.g. modified / enlarged / Braille papers, reader, extra time) — check the current SEC scheme.",
  "REFER: GP / HSE optometry or ophthalmology if eyes not checked recently. NCSE VISITING TEACHER SERVICE (blind / visually impaired) — check current referral route. Vision Ireland (formerly NCBI) for family support and rehabilitation / mobility services — check current name and service. CDNT where needs are complex.",
  "DO NOT administer or report visually-dependent subtests where the child cannot see the stimuli; do not enlarge test stimuli and report the result as normative; do not attribute repetitive movements to autism without specialist assessment.",
 ],

 "explain_parent": [
  "'The most important question for me isn't the diagnosis itself but how she uses her vision in a real classroom — how close she needs to be, what size and contrast work, and when she gets tired. The Visiting Teacher is the expert on that.'",
  "'Her verbal reasoning is right in line with children her age. Some tests depend on seeing small pictures and patterns, and I didn't use those because they'd measure her eyes, not her thinking.'",
  "'Children who are blind or partially sighted often reach things like walking or pointing a bit later, or by a different route. That isn't the same as being behind in how clever they are.'",
  "'She'll need to learn some things other children pick up just by watching — like finding her way round a new building, or reading people's faces. Those skills can be taught directly, and they matter as much as reading.'",
  "'Being tired after school is real. Looking closely all day takes a lot of effort.'",
  "SIGNPOST: the child's ophthalmologist / orthoptist; the NCSE Visiting Teacher; Vision Ireland (formerly NCBI) for family and mobility supports; parent support groups for the specific eye condition — check current names and services.",
 ],

 "explain_teacher": [
  "'She can see some things and not others, and it changes with light, distance, clutter and tiredness. The Visiting Teacher's advice tells us exactly what works — let's start there.'",
  "'Give her her own copy of anything on the board, at the same time as everyone else. Copying from the board is one of the hardest things you can ask of her.'",
  "'Say what you're doing. \"I'm writing the date\", \"Look at the red box\" means nothing — \"the question in the box at the top of page 12\" does.'",
  "'Clutter is the enemy for children with CVI. Clear worksheets, one thing at a time, and a calm wall display near her seat.'",
  "'Plan break times. She may not see who's playing where. A buddy system or a structured game helps her join in without an adult hovering.'",
  "'If she's slower, it's because she's working harder to see — not because she's not trying. Extra time is fair access, not an advantage.'",
 ],

 "explain_child": [
  "YOUNGER: 'Your eyes (or the part of your brain that helps you see) work differently, so some things are hard to see. That's why you have big print / your magnifier. It's got nothing to do with how clever you are.'",
  "OLDER: 'Your vision means some tasks take more effort — the board, crowded pages, finding people in the yard. You're allowed to ask for what helps: your own copy, more light, less clutter, a break.'",
  "ADAPT YOUR OWN MATERIALS: no visual rating scales or picture cards unless the child can see them. Offer tactile or verbal alternatives.",
  "TEACH A SELF-ADVOCACY SENTENCE: 'Can I have my own copy?' or 'Can you tell me what's on the board?' Many children with VI avoid asking because it marks them out.",
  "ASK: 'When is it hardest to see in school? When is it easiest?' and 'What do you wish teachers knew?'",
  "CHECK YOUR SETTING: good light on the task, not in the child's eyes, sit where they can see you (or tell them where you are), and introduce yourself by voice each time.",
 ],

 "analogies": [
  "THE FOGGED-UP WINDSCREEN: 'You can drive, but you're going slower, leaning forward, and you're exhausted after twenty minutes.' Good with parents and teachers; explains fatigue and slowness.",
  "LOOKING THROUGH A TOILET-ROLL TUBE: 'He sees what's straight ahead clearly, but misses everything around it — so he'll miss the step or the child beside him.' Good for field loss.",
  "WHERE'S WALLY EVERY PAGE: 'For a child with CVI a busy worksheet is like a Where's Wally puzzle — the answer is in there, but finding it takes all her energy.' Good for teachers; explains clutter.",
  "THE PHONE WITH A CRACKED SCREEN: 'The information is all there, but some bits are hard to make out, and it depends on the light.' Good with children and adolescents.",
 ],

 "language": [
  "'Blind', 'partially sighted', 'visually impaired', 'has low vision' are all in use. Many blind adults prefer 'blind person' (identity-first); others prefer person-first. Ask the family and young person and follow them.",
  "Use 'cerebral visual impairment (CVI)' (sometimes 'cortical visual impairment' in older or US reports) — check what term the eye report uses and match it.",
  "Avoid 'suffers from', 'visually challenged', 'can't see' as a total statement when the child has useful vision. Describe functional vision: 'reads 18-point bold print at 20 cm'.",
  "It is fine to say 'see you later' or 'look at this' — blind people use these words too. What matters is adding a verbal description.",
 ],

 "red_flags": [
  "RED FLAG — a WHITE PUPIL (white reflex, including in a photograph), a new squint, or sudden loss of vision. Same-day GP / urgent ophthalmology advice. A white pupillary reflex can indicate retinoblastoma and needs urgent review.",
  "RED FLAG — headaches with vomiting, visual disturbance, or new clumsiness. Urgent GP — do not attribute to stress or behaviour.",
  "RED FLAG — a child who has never had an eye examination and is being assessed for literacy or learning difficulty. Stop and arrange one first.",
  "RED FLAG — disclosure or signs of abuse in a child with VI. Disabled children are at substantially greater risk of violence (Jones et al., 2012 — rate not quoted here, check), and a blind child may not be able to identify an abuser by sight. Follow Children First the same day; report to Tusla as soon as practicable; telling the DLP does not discharge a mandated person's duty.",
  "BOUNDARY — you do not measure acuity, interpret an eye report beyond what it states, or diagnose CVI. You describe functional access and learning, and refer. PSI 2.2.2.",
  "WATCH — assessment validity. Record exactly which subtests were omitted or adapted and why. Scores from enlarged or otherwise altered stimuli are descriptive, not normative.",
  "WATCH — progressive conditions (e.g. some retinal dystrophies). Ask whether vision is expected to change; recommendations such as braille or touch-typing may need to start before they are needed.",
 ],

 "child_voice": [
  "STRUCTURED VERBAL INTERVIEW — good because it removes the visual demand; allow time, and describe any materials you use aloud. Record verbatim.",
  "TALKING MATS WITH TACTILE OR HIGH-CONTRAST SYMBOLS — good because the framework still works when symbols are enlarged, tactile or objects of reference. → https://www.talkingmats.com/",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) IN ACCESSIBLE FORMAT — enlarged, high contrast, or read aloud — good because it is familiar and gives a comparable baseline. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "A WALK-ROUND OF THE SCHOOL WITH THE CHILD — good because the child shows you where movement, lighting and finding people are hard, which is where the recommendations go.",
  "ASK ABOUT EQUIPMENT AND IDENTITY — 'What do you think of your magnifier / braille / laptop? When do you use it and when don't you?' — good because stigma often drives non-use, and only the child knows.",
 ],

 "questions": [
  "Q: 'Her eyes are fine according to the optician — why would she have a vision problem?' — A: 'The eyes can be healthy while the part of the brain that makes sense of what's seen works differently. That's called CVI. It shows up as trouble finding things in a busy picture or crowd. It's worth asking the eye team whether they've considered it.'",
  "Q: 'Why didn't you do the puzzle tests?' — A: 'Those tests rely on seeing small details quickly. With her vision they'd measure her eyesight, not her reasoning, so the scores would be misleading. I used tasks she could access and said so in the report.'",
  "Q: 'Does he need braille?' — A: 'That's a decision for the Visiting Teacher and the eye team, based on how much useful vision he has and whether it's expected to change. I can say what I saw about his reading, but I'm not the right person to decide.'",
  "Q: 'She rocks and presses her eyes — is it autism?' — A: 'Those movements are quite common in children who are blind or have very low vision, and they don't mean autism on their own. If there are other social-communication concerns, it needs a team that's experienced with visual impairment to look at it.'",
  "Q: 'Should she be in a special school?' — A: 'Some children do well in a specialist setting; many thrive in mainstream with the right support. It depends on her needs and what you want. The Visiting Teacher and the SENO can explain the options — I can't promise a place.'",
  "Q: 'Is the extra time fair to the other children?' — A: 'Yes. Reading with low vision is slower and more tiring. The extra time gives her the same chance to show what she knows — it doesn't give her an advantage.'",
 ],

 "supervision": [
  "Bring a case where vision status was not established before assessment, and ask how the service checks this at referral.",
  "Ask which cognitive measures the service uses with children with VI, which subtests are omitted, and how the report explains that.",
  "Ask how CVI is recognised and referred locally — who assesses it, and what the waiting times are.",
  "Discuss how the local NCSE Visiting Teacher Service and NEPS work together, and how their functional vision advice should shape your recommendations.",
 ],

 "reflection": [
  "ON VISION STATUS — Did I know the date and outcome of the last eye check before I started? Did I read the Visiting Teacher's functional vision advice?",
  "ON TEST CHOICE — Did I use any visually-loaded tasks the child could not see? Did I record omissions and adaptations at the time and state them in the report?",
  "ON INTERPRETATION — Did I read slowness or 'poor visual processing' as a cognitive weakness when it could be vision?",
  "ON THE WHOLE CHILD — Did I look beyond reading to mobility, social inclusion, fatigue and independence?",
  "ON MY MATERIALS — Were my rating scales, pictures and questionnaires accessible to this child, or did I rely on adults because my tools excluded them?",
  "WHAT GOOD LOOKS LIKE: 'Ophthalmology confirmed bilateral optic nerve hypoplasia; the Visiting Teacher advised N24 bold on buff paper. I used the verbal and auditory working-memory subtests only, recorded the omissions, and reported them as descriptive. Recommendations covered materials, board access, AT, a structured break-time plan, and orientation and mobility.'",
  "WHAT POOR LOOKS LIKE: 'Visual Spatial and Processing Speed indices were in the extremely low range, suggesting significant difficulties with visual processing.' — no mention of eye condition, no adaptation recorded, no Visiting Teacher link.",
 ],

 "citations": [
  "Dale, N., & Salt, A. (2007). Early support developmental journal for children with visual impairment: The case for a new developmental framework for early intervention. Child: Care, Health and Development, 33(6), 684–690.",
  "Hatlen, P. (1996). The core curriculum for blind and visually impaired students, including those with additional disabilities. RE:view, 28(1), 25–32.",
  "Jones, L., Bellis, M. A., Wood, S., Hughes, K., McCoy, E., Eckley, L., Bates, G., Mikton, C., Shakespeare, T., & Officer, A. (2012). Prevalence and risk of violence against children with disabilities: A systematic review and meta-analysis of observational studies. The Lancet, 380(9845), 899–907.",
  "Philip, S. S., & Dutton, G. N. (2014). Identifying and characterising cerebral visual impairment in children: A review. Clinical and Experimental Optometry, 97(3), 196–208.",
  "Rahi, J. S., & Cable, N. (2003). Severe visual impairment and blindness in children in the UK. The Lancet, 362(9393), 1359–1365.",
  "Tadić, V., Pring, L., & Dale, N. (2010). Are language and social communication intact in children with congenital visual impairment at school age? Journal of Child Psychology and Psychiatry, 51(6), 696–705.",
  "Warren, D. H. (1994). Blindness and children: An individual differences approach. Cambridge University Press.",
  "Williams, C., Pease, A., Warnes, P., et al. (2021). Cerebral visual impairment-related vision problems in primary school children: A cross-sectional survey. Developmental Medicine & Child Neurology, 63(6), 683–689. — check full author list before citing.",
  "World Health Organization. (2019). World report on vision. WHO.",
 ],

 "pathway": {
  "age": "Congenital and severe VI is usually identified in infancy (neonatal eye checks, PHN developmental checks, parental concern about fixing and following). Milder VI, refractive error and CVI are often identified later — at school vision screening, when print gets smaller, or after a referral for literacy, attention or clumsiness. CVI in particular is frequently missed until school age.",
  "who_diagnoses": "Ireland: HSE ophthalmology (hospital paediatric ophthalmology), community ophthalmic services and orthoptists; optometrists for refractive error; HSE school vision screening — check which class and service locally. CVI is identified by ophthalmology / orthoptics, often with paediatric neurology or CDNT input. The EP does not diagnose visual impairment.",
  "who_wrote_report": "Paediatric ophthalmologist; orthoptist; optometrist (refraction); NCSE Visiting Teacher (functional vision assessment and educational advice, not diagnosis); CDNT; Vision Ireland (formerly NCBI) services. An EP report may describe access and learning but must not be the source of a visual diagnosis.",
  "refer_to": "GP / optometry / HSE ophthalmology where eyes not recently checked or there is new concern; same-day GP for white pupil, new squint or sudden loss. NCSE Visiting Teacher Service for children who are blind / visually impaired (check current referral route). CDNT where needs are complex. Vision Ireland for mobility and family support (check current services). SENO for AT, SNA or placement questions.",
  "sooner": "'Visual difficulties — especially CVI and milder problems — are often missed because children adapt and don't know they see differently. They assume everyone sees the way they do. What matters now is that school knows and adjusts.'",
 },

 "differential": [
  "UNCORRECTED REFRACTIVE ERROR — needs glasses; resolves with correction. Rule out first.",
  "CVI — normal or near-normal eye examination but difficulty with visual search, clutter, movement and faces.",
  "DYSLEXIA / reading difficulty — phonological difficulty with normal vision; the two can co-occur. Do not accept 'visual stress' or coloured overlays as a diagnosis of dyslexia.",
  "DCD — motor coordination difficulty not explained by vision; if vision is impaired, the motor difficulty may follow from it.",
  "ADHD / attention — 'not looking', 'losing place', 'off task' may reflect visual fatigue or field loss.",
  "AUTISM — social communication difference; some features overlap with lack of visual access.",
 ],

 "next": [
  "Establish vision status: date and outcome of last eye check, diagnosis, acuity and field, glasses prescribed and worn. Arrange an eye check via GP / optometry if not recent.",
  "Contact the NCSE Visiting Teacher (with consent) and read the functional vision assessment before choosing tools.",
  "Plan the assessment: lighting, position, accessible materials; select non-visual or verbal measures; record omissions and adaptations at the time.",
  "Observe in class and at break — materials, board, lighting, movement, social inclusion.",
  "Write recommendations on access (materials, AT, seating, lighting, expanded core curriculum) with named person and review date.",
 ],

 "presentations": [
  "Uncorrected refractive error",
  "Visual fatigue in extended reading",
  "Access to print — font, size, contrast, position in room",
  "Copying from the board",
  "Visual search and clutter (possible CVI)",
  "Orientation and mobility around the school",
  "Social inclusion at break time",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — congenital VI identified in infancy; CVI and milder VI may be suspected but not yet confirmed",
   "prevalence": "Severe childhood VI is uncommon (Rahi & Cable, 2003) — rate not quoted here, check.",
   "see": "Not fixing on faces, wandering eye movements or nystagmus, late reaching or walking, bringing objects very close, light-seeking or light-avoiding. Development follows different routes (Dale & Salt, 2007). Check PHN records and eye checks. Never assess visually-loaded tasks before vision is established.",
   "tools": ["Vineland-3", "Oregon Project for Preschool Children who are Blind or Visually Impaired — AGE 0–6 · MEASURES: developmental skills across domains with VI-specific norms/sequence · CANNOT TELL YOU: IQ or visual acuity · TIME: observational, over sessions — check current edition"],
  },
  "School Age": {
   "applies": "YES — main window for identifying refractive error, milder VI and CVI",
   "prevalence": "Rate not stated here — check; CVI-related difficulties reported in a minority of mainstream pupils (Williams et al., 2021).",
   "see": "Holding books close, losing place, slow copying, avoiding reading, clumsiness at steps, difficulty finding friends at break, fatigue and headaches. Often referred for literacy or attention. Confirm the date of the last eye check before any literacy or non-verbal assessment.",
   "tools": ["WISC-V UK", "BPVS-3", "Vineland-3", "SDQ", "Functional vision assessment (NCSE Visiting Teacher / orthoptist) — AGE all · MEASURES: how the child uses vision for real tasks (print size, distance, contrast, field, lighting, fatigue) · CANNOT TELL YOU: cognitive ability or diagnosis · TIME: varies — request the report"],
  },
  "Adolescent": {
   "applies": "YES — visual load of post-primary subjects, exams, independence and identity",
   "prevalence": "Continues from childhood; progressive conditions may worsen — rate not stated here, check.",
   "see": "Multiple teachers and rooms, dense texts, diagrams and practical subjects, exam access, travel independence, social inclusion and self-image. Some young people reject visible aids. RACE applications and subject choice are the practical questions.",
   "tools": ["WISC-V UK", "WIAT-III UK", "Access arrangements evidence (RACE)", "RCADS self-report"],
  },
  "Young Adult": {
   "applies": "YES — lifelong; access technology and supports in further / higher education and work",
   "prevalence": "Adult rate not stated here — check.",
   "see": "Screen readers, accessible course materials, mobility on campus, DARE / disability-service supports, and workplace adjustments. The young person leads. EP role is time-limited; refer to college disability services and Vision Ireland.",
   "tools": ["WAIS-IV UK", "Adult self-report measures via the service"],
  },
  "Special Setting": {
   "applies": "YES — a specialist school for blind / VI pupils, and many pupils with MDVI or CVI in other special settings",
   "prevalence": "Setting-dependent — not a population figure; CVI is common in children with CP and complex needs.",
   "see": "In special settings, vision is often never formally assessed because of other needs. Check for CVI, check glasses are worn, and audit the environment — lighting, clutter, contrast, consistent layout, tactile cues and objects of reference.",
   "tools": ["Vineland-3 / ABAS-3", "Communication Matrix / AAC review", "Adaptive measure in place of IQ"],
  },
 },
},

# =====================================================================================
# 3. RECURRENT OTITIS MEDIA WITH EFFUSION (GLUE EAR)
# =====================================================================================
{
 "name": "Recurrent otitis media with effusion (glue ear)",
 "code": "Not a DSM diagnosis · medical (ear) condition causing conductive, usually fluctuating, hearing loss · ICD-11: Chapter 10, Diseases of the ear or mastoid process — ICD-11 code — check before quoting",
 "neps": "5. OTHER (5.2 Hearing) — and 1. LEARNING (1.2 Language skills · 1.4 Literacy) where history is linked to language or phonics difficulty",
 "coru": _CORU,
 "psi": _PSI,
 "law": "EPSEN Act 2004 · Disability Act 2005 (Assessment of Need) · Equal Status Acts 2000–2018 · Children First Act 2015 · GDPR",

 "what_it_is": [
  "Fluid collects in the middle ear behind the eardrum without signs of acute infection, damping sound conduction. The result is a CONDUCTIVE hearing loss, typically mild to moderate, that FLUCTUATES — better on some days or weeks, worse on others — and often affects both ears (Rosenfeld et al., 2016).",
  "It is very common in early childhood, peaking in the preschool years and usually resolving spontaneously; most episodes clear within about three months (Rosenfeld et al., 2016 — check exact figures). 'Recurrent' or 'persistent' glue ear is the group that matters for the EP.",
  "Higher-risk groups include children with Down syndrome and cleft palate, for whom NICE gives separate recommendations (NICE, 2008, CG60 — check for updates). Other associated factors include winter months, day-care attendance and passive smoking — check sources before quoting as risk factors.",
  "Management (medical, not EP): a period of active observation ('watchful waiting'); then, for persistent bilateral glue ear with significant hearing loss, ventilation tubes (grommets) or hearing aids may be offered. NICE (2008) sets out the criteria — check the current guideline rather than quoting thresholds from memory.",
  "Why the EP cares: a child who heard inconsistently during the years when speech sounds, vocabulary and phonics were being learned may carry a residue — in phonological awareness, speech sound accuracy, listening habits or attention — after the ears have cleared. The Reference sheet puts it bluntly: 'glue ear at 5 shows up at 8.'",
  "BUT the evidence on long-term effects is MIXED. Meta-analysis found small or negligible associations between early OME and later speech-language outcomes in most children (Roberts et al., 2004); a large trial of early versus delayed grommets found no developmental benefit from early insertion at 9–11 years (Paradise et al., 2007). Treat glue-ear history as a live hypothesis to test, not an explanation to assume.",
 ],

 "what_it_is_not": [
  "NOT the same as an ear infection. Acute otitis media is painful and feverish; glue ear is often silent — no pain, no fever — and noticed only as 'not listening', turning the TV up, or speech changes.",
  "NOT ruled out by a normal hearing test on one day. Because it fluctuates, one clear test does not mean hearing was clear last month or next month. Ask about the pattern over time, not just the last result.",
  "NOT a cause the EP can confirm for a literacy difficulty. A history of glue ear raises a hypothesis; the assessment has to show whether phonological, speech or language skills are actually weak now, and what helps. Many children with glue ear develop typical language and literacy (Roberts et al., 2004).",
  "NOT DLD by default. If language difficulty persists well after hearing has normalised, CATALISE would still consider DLD (a history of OME is not one of the 'associated with X' conditions that sensorineural loss is — check CATALISE-2 wording before quoting) (Bishop et al., 2017). SLT assessment decides.",
  "NOT a behaviour problem. 'Selective hearing', daydreaming, irritability and 'ignoring' are common in children with glue ear. Test hearing before accepting a behavioural explanation.",
  "NOT something the EP manages. Decisions on observation, grommets or hearing aids are for GP, audiology and ENT. The EP asks the history question, recommends audiology, and adapts the classroom.",
 ],

 "prevalence": [
  "OVERALL: very common. Rosenfeld et al. (2016, AAO-HNS guideline) state that most children have at least one episode of OME before school age — check exact figure before quoting.",
  "RESOLUTION: most episodes resolve spontaneously within about three months (Rosenfeld et al., 2016) — check figures before quoting.",
  "HIGHER RISK: children with Down syndrome and cleft palate have much higher rates and more persistent glue ear (NICE, 2008) — rate not stated here, check.",
  "IRELAND: no Irish prevalence figure is cited here — check before quoting. ENT waiting lists reflect service capacity, not prevalence.",
  "AGE: peaks in the preschool years and declines through the early primary years; persistence into later primary is less common — rate not stated here, check.",
 ],

 "cooccurring": [
  {"name": "SPEECH SOUND DIFFICULTY",
   "rate": "associated in some children — rate not stated here, check (see Roberts et al., 2004)",
   "presents": "Unclear speech, dropped word endings and confusion of similar-sounding consonants, especially high-frequency sounds like s, f and th. Refer to SLT; check hearing is currently clear."},
  {"name": "PHONOLOGICAL AND EARLY LITERACY DIFFICULTY",
   "rate": "hypothesised link; evidence mixed — rate not stated here, check",
   "presents": "Weak rhyme, blending and segmenting, and difficulty with letter-sound links taught during a period of fluctuating hearing. Ask when phonics was taught and when the ears were blocked. Assess current phonological skills directly."},
  {"name": "DLD (differential and possible co-occurrence)",
   "rate": "OME history does not by itself exclude DLD (see Bishop et al., 2017 — check wording) — rate not stated here, check",
   "presents": "Language difficulty that persists after hearing has normalised. Do not keep attributing it to 'the ears' — refer to SLT for language assessment."},
  {"name": "ATTENTION AND LISTENING BEHAVIOUR",
   "rate": "rate not stated here — check",
   "presents": "Drifting in whole-class talk, watching peers for cues, fatigue and irritability, 'switching off'. Can look like ADHD. Check current hearing and whether the pattern changes when hearing is clear or when the child is close to the teacher."},
  {"name": "DOWN SYNDROME",
   "rate": "glue ear very common and often persistent (NICE, 2008) — rate not stated here, check",
   "presents": "Hearing is easily overlooked because language delay is attributed to the syndrome. Every child with Down syndrome should have regular audiology; check when it was last done."},
  {"name": "CLEFT PALATE",
   "rate": "glue ear very common (NICE, 2008) — rate not stated here, check",
   "presents": "Hearing, speech (resonance) and language needs sit together. Usually under a cleft team; ask for their audiology and SLT reports."},
 ],

 "recommendations": [
  "ASK THE HISTORY QUESTION in every language, literacy, attention or behaviour referral: 'Has she had lots of ear infections, blocked ears, grommets, or been told she has glue ear? When? Did anyone check her hearing during junior and senior infants?'",
  "RECOMMEND AUDIOLOGY if there is current concern, a history of glue ear without a recent hearing test, or fluctuating responses. Route: GP / HSE Primary Care audiology — check local route. Do this BEFORE drawing conclusions about language or phonics.",
  "CLASSROOM, WHILE HEARING FLUCTUATES: seat near the teacher and away from noise; face the class when speaking; gain attention before instructions; key words written as well as spoken; check understanding by show or tell back; reduce background noise. These help whether the ears are clear or not.",
  "TELL STAFF THAT HEARING VARIES: 'Some weeks she will hear well, some weeks she won't — it's not inconsistency of effort.' Ask the teacher to note bad weeks (colds, winter) and share with the GP.",
  "PHONOLOGICAL AND PHONICS SUPPORT: if current assessment shows weak phonological awareness or phonics, recommend explicit, multisensory, cumulative phonics with visual support for sounds (mouth shapes, letter cards) — at School Support. Assess, don't assume.",
  "LANGUAGE: if vocabulary or language comprehension is weak, pre-teach vocabulary and refer to SLT; if it persists after hearing has normalised, the SLT should consider DLD.",
  "IF GROMMETS OR HEARING AIDS ARE PRESCRIBED: ask school to know which, whether aids are worn, and to report any return of symptoms (grommets can extrude and glue ear can return).",
  "CONTINUUM LEVEL: Classroom Support for seating, attention-gaining and visual support; School Support for phonological / phonics or vocabulary work; School Support Plus where SLT, audiology or ENT are involved.",
  "REFER: GP / audiology (hearing); ENT via GP (medical management); SLT (Primary Care) if speech or language difficulty persists. The Visiting Teacher Service may be involved where a hearing loss is persistent and significant — check current eligibility.",
  "DO NOT write 'glue ear caused his reading difficulty'. Write: 'A history of glue ear during the early school years is noted; current phonological skills are … ; this pattern is consistent with, but does not establish, an effect of early fluctuating hearing.'",
 ],

 "explain_parent": [
  "'Glue ear is when sticky fluid sits behind the eardrum and muffles sound — a bit like listening underwater. It's very common in young children and usually clears by itself.'",
  "'Because it comes and goes, he may have heard well some weeks and badly others — sometimes right when the class was learning letter sounds. That's why I'm asking about it.'",
  "'Lots of children who had glue ear learn to read without any problem. So I'm not assuming it explains things — I'm checking his sound skills now, so we know what to teach.'",
  "'If he's had a cold and suddenly isn't listening, that may be his ears, not his attitude. It's worth letting the school know.'",
  "'The GP can refer for a hearing test. Decisions about grommets are for the ENT doctor — not something I can advise on.'",
  "SIGNPOST: GP; HSE audiology; the child's SLT if involved; the HSE website information on glue ear (check current page).",
 ],

 "explain_teacher": [
  "'His hearing changes from week to week with glue ear. When he's not responding, try getting his attention first, standing closer, and seeing if it changes. That tells us something useful.'",
  "'Keep a quick note of the weeks he seems not to hear — especially after colds. It helps the GP decide on a referral.'",
  "'If he missed a lot of phonics in infants because of his ears, he might have gaps, not a learning difficulty. Explicit teaching of those sounds, with visual support, is the first step.'",
  "'Visual back-up for anything said: key words on the board, instructions written down, picture cues. It costs nothing and protects him on bad weeks.'",
  "'Don't let \"he hears when he wants to\" become the story. With glue ear, that's literally true — some days he can, some days he can't.'",
 ],

 "explain_child": [
  "YOUNGER: 'Sometimes your ears get a bit blocked, like when you're swimming underwater. Then it's hard to hear the teacher. If that happens, it's OK to put your hand up and say you didn't hear.'",
  "OLDER: 'You had glue ear when you were younger — your ears were blocked some of the time. You might have missed some of the sounds when you were learning to read. That's not your fault, and we can teach them now.'",
  "ASK: 'Are there days when it's harder to hear? What's it like when you have a cold?' — children often notice the pattern better than adults.",
  "TEACH A SELF-ADVOCACY SENTENCE: 'I didn't catch that — can you say it again?' Practise it so it feels normal.",
  "CHECK YOUR SETTING: quiet room, sit facing the child, and if the child has a cold or blocked ears on the day, consider rescheduling language-loaded tests.",
 ],

 "analogies": [
  "LISTENING UNDERWATER: 'On a bad glue-ear day, voices sound muffled and far away, like you're in the swimming pool.' Good with children and parents.",
  "THE RADIO THAT KEEPS GOING OUT OF TUNE: 'Some weeks the signal is perfect, some weeks it's crackly. If the crackly weeks happened when the class was learning letter sounds, he may have missed some.' Good with teachers; explains gaps and inconsistency.",
  "THE BUILDING WITH A FEW MISSING BRICKS: 'The wall is mostly fine, but a few bricks at the bottom — the sounds of letters — were never properly laid. We go back and put them in.' Good for explaining targeted phonics.",
  "EARPLUGS ON AND OFF: 'Imagine someone put earplugs in you at random for a week at a time during your first year at school.' Good with sceptical staff.",
 ],

 "language": [
  "'Glue ear' is the common term and is fine with families; 'otitis media with effusion (OME)' is the medical term — use it in the report with 'glue ear' in brackets.",
  "Say 'a history of glue ear' or 'fluctuating conductive hearing loss', not 'hearing problem' in general — specificity matters for the next reader.",
  "Avoid 'selective hearing', 'doesn't listen' or 'ignores instructions' in reports where hearing has not been checked — these are interpretations, and PSI 1.2.8 requires opinion to be labelled as such.",
  "Avoid causal language ('caused', 'due to') about glue ear and literacy unless a professional with the relevant evidence has concluded it — say 'consistent with' or 'may have contributed to'.",
 ],

 "red_flags": [
  "RED FLAG — ear pain with fever, discharge, swelling behind the ear, or the child is unwell. GP the same day — this is not glue ear alone.",
  "RED FLAG — sudden or one-sided hearing loss, or a loss that does not fluctuate. GP / audiology promptly — may be something other than glue ear (including sensorineural loss).",
  "RED FLAG — language regression (loss of skills the child had). Not glue ear. GP / paediatrics without delay.",
  "RED FLAG — Down syndrome or cleft palate with no recent audiology. Arrange review — glue ear is common and easily missed in these groups (NICE, 2008).",
  "BOUNDARY — you do not diagnose glue ear, interpret tympanometry, or advise on grommets, hearing aids or medication. You ask the history, recommend audiology, and adapt teaching. PSI 2.2.2.",
  "WATCH — assessment on a 'bad ear day'. If the child has a heavy cold, blocked ears or reports not hearing well, consider rescheduling language and phonological testing, or record it and interpret with caution.",
 ],

 "child_voice": [
  "A 'GOOD HEARING DAY / BAD HEARING DAY' SCALE — two faces or a thermometer — good because it lets the child report fluctuation, which adults often miss.",
  "DRAWING AND TALK ('draw where in school it's hard to hear') — good because it locates the difficulty in places and times, which is what the recommendations target.",
  "'MY THOUGHTS ABOUT SCHOOL' (NEPS) — good because it is familiar, and the reading and listening items give a baseline. → https://www.gov.ie/en/publication/52ee2-neps-resources-and-publications/",
  "ASK ABOUT PHONICS DIRECTLY — 'Which letter sounds feel tricky? Which are easy?' — good because older children can often identify the specific gaps, which guides targeted teaching.",
 ],

 "questions": [
  "Q: 'He had glue ear years ago — why does it matter now?' — A: 'If his hearing was up and down while he was learning letter sounds, he may have gaps in those early skills. It doesn't always happen, so I'm checking his sound skills now rather than assuming.'",
  "Q: 'Did the glue ear cause her dyslexia?' — A: 'I can't say that. Many children with glue ear read well, and dyslexia has its own causes. What I can say is whether her sound skills are weak now and what will help — that's the same whatever the cause.'",
  "Q: 'Should he have grommets?' — A: 'That's a decision for the ENT doctor, based on hearing tests over time. I can tell the GP what we're seeing in school, which may help.'",
  "Q: 'His hearing test last year was fine — do we need another?' — A: 'Glue ear comes and goes, so one clear test doesn't mean hearing is always clear. If there are new concerns, especially after colds, another check is reasonable.'",
  "Q: 'Is it glue ear or is he just not paying attention?' — A: 'Let's find out. If he responds much better when the teacher is close and has his attention first, and it varies with colds, that points towards hearing. A hearing test will help us be sure.'",
  "Q: 'He's 12 now — would glue ear still be relevant?' — A: 'Glue ear itself is much less common by then, but if it affected his early learning, gaps can still show. I'd ask about it as part of his history, and test his skills now.'",
 ],

 "supervision": [
  "Ask how your supervisor weighs a glue-ear history in a literacy referral — what they write, and how they avoid overclaiming causation.",
  "Bring a behaviour or attention referral where hearing had not been checked, and discuss how to raise it with the school.",
  "Ask about local audiology and ENT waiting times and what the school can do in the meantime.",
  "Discuss whether to test on a day the child has a cold or reports blocked ears — and how to record it if you do.",
 ],

 "reflection": [
  "ON THE HISTORY — Did I ask specifically about ear infections, glue ear and grommets, and when they happened relative to junior / senior infants?",
  "ON CAUSATION — Did I write that glue ear caused the difficulty, or did I describe it as a hypothesis consistent with the current profile?",
  "ON CURRENT HEARING — Did I know whether hearing was clear on the day I tested?",
  "ON THE BEHAVIOUR FRAME — When the school said he 'hears when he wants to', did I test that, or accept it?",
  "ON THE RECOMMENDATIONS — Would my recommendations help this child on both good and bad hearing weeks?",
  "WHAT GOOD LOOKS LIKE: 'Mum described repeated ear infections and grommets in senior infants. Current phonological awareness was below average, with blending relatively intact and segmenting weak. I wrote that the history was consistent with, but did not establish, a contribution from early fluctuating hearing, recommended audiology to confirm hearing now, and set targeted phonics with visual support.'",
  "WHAT POOR LOOKS LIKE: 'Her reading difficulties are due to glue ear.' — no current hearing check, no phonological assessment, no audiology recommendation.",
 ],

 "citations": [
  "Bishop, D. V. M., Snowling, M. J., Thompson, P. A., Greenhalgh, T., & CATALISE-2 consortium. (2017). Phase 2 of CATALISE: A multinational and multidisciplinary Delphi consensus study of problems with language development: Terminology. Journal of Child Psychology and Psychiatry, 58(10), 1068–1080.",
  "Browning, G. G., Rovers, M. M., Williamson, I., Lous, J., & Burton, M. J. (2010). Grommets (ventilation tubes) for hearing loss associated with otitis media with effusion in children. Cochrane Database of Systematic Reviews, 2010(10), CD001801.",
  "National Institute for Health and Care Excellence. (2008). Otitis media with effusion in under 12s: Surgical management (Clinical guideline CG60). NICE — check for updates.",
  "Paradise, J. L., Feldman, H. M., Campbell, T. F., et al. (2007). Tympanostomy tubes and developmental outcomes at 9 to 11 years of age. New England Journal of Medicine, 356(3), 248–261. — check full author list before citing.",
  "Roberts, J. E., Rosenfeld, R. M., & Zeisel, S. A. (2004). Otitis media and speech and language: A meta-analysis of prospective studies. Pediatrics, 113(3), e238–e248.",
  "Rosenfeld, R. M., Shin, J. J., Schwartz, S. R., et al. (2016). Clinical practice guideline: Otitis media with effusion (update). Otolaryngology–Head and Neck Surgery, 154(1 Suppl), S1–S41. — check full author list before citing.",
 ],

 "pathway": {
  "age": "Most common in the preschool years (roughly 1–5) and usually resolving; persistent or recurrent cases are often identified at the PHN developmental checks, by GP after repeated ear infections, or in junior / senior infants when a teacher notices 'not listening'. The EP more often meets it RETROSPECTIVELY — as a history question in a literacy, language or attention referral at 7–10.",
  "who_diagnoses": "Ireland: GP (otoscopy, initial concern); HSE audiology (hearing test, tympanometry); ENT (hospital) for persistent cases and grommets. The EP does not diagnose glue ear.",
  "who_wrote_report": "GP letter; HSE audiologist (audiogram and tympanogram); ENT consultant (grommet surgery, follow-up); SLT (speech / language impact). An EP report may note the history but should not be the source of the diagnosis.",
  "refer_to": "GP (first step; for ENT referral); HSE audiology via GP / Primary Care; SLT (Primary Care) if speech or language concerns persist; same-day GP for pain, discharge or fever.",
  "sooner": "'Glue ear is so common and usually so mild that it's easy to miss — lots of children have it without anyone knowing. Asking about it now means we can check whether there are gaps to fill, and fill them.'",
 },

 "differential": [
  "PERMANENT HEARING LOSS (sensorineural or mixed) — does not fluctuate; audiology distinguishes.",
  "DLD — language difficulty persisting after hearing normalises; SLT assessment.",
  "DYSLEXIA / phonological difficulty — may exist independently of glue-ear history; assess current skills.",
  "ADHD / attention difficulty — attention difficulty that does not vary with hearing or proximity.",
  "EAL — limited English exposure rather than limited hearing.",
 ],

 "next": [
  "Ask the glue-ear history question: infections, blocked ears, grommets, hearing tests — and when, relative to infant classes.",
  "Check the date of the last hearing test; recommend audiology via GP if not recent or there is current concern.",
  "Assess current phonological, speech and language skills directly; do not infer them from the history.",
  "Write classroom recommendations that work on good and bad hearing weeks, at the right Continuum level.",
 ],

 "presentations": [
  "Hearing history during the years phonics was taught",
  "Listening in noise vs listening one-to-one",
  "Classroom acoustics and seating",
  "Phonological awareness difficulty",
  "Following multi-step verbal instructions",
  "Sustained attention in whole-class vs one-to-one",
 ],

 "bands": {
  "Early Years": {
   "applies": "YES — peak age for glue ear",
   "prevalence": "Very common; most children have at least one episode before school age (Rosenfeld et al., 2016 — check figure).",
   "see": "Turning up the TV, not responding to name, speech unclear or late, irritability, frequent colds and snoring. Often silent — no pain. Check PHN records and hearing tests. Always establish hearing before any language conclusion.",
   "tools": ["Preschool Language Scales-5 (PLS-5)", "Renfrew Action Picture Test", "Ages & Stages Questionnaires (ASQ-3)"],
  },
  "School Age": {
   "applies": "YES — still present in some infants-class children; history is the key question at 7–10",
   "prevalence": "Declines through the early primary years — rate not stated here, check.",
   "see": "In infants: 'not listening', inconsistent responses, speech errors. By 7–10: a literacy, language or attention referral where the history reveals glue ear in infants. Assess current phonological and language skills and recommend audiology if not recent.",
   "tools": ["Phonological Assessment Battery (PhAB2)", "CELF-5 UK", "BPVS-3", "YARC (York Assessment of Reading for Comprehension)", "WIAT-III UK"],
  },
  "Adolescent": {
   "applies": "RETROSPECTIVE ONLY — glue ear itself uncommon; history may still inform a literacy or language profile",
   "prevalence": "Active glue ear uncommon at this age — rate not stated here, check.",
   "see": "A teenager with long-standing literacy or spelling weakness and a glue-ear history in infants. Assess current skills; do not attribute causation. Current hearing should still be checked if there are concerns.",
   "tools": ["WIAT-III UK", "CELF-5 UK", "Access arrangements evidence (RACE)"],
  },
  "Young Adult": {
   "applies": "RETROSPECTIVE ONLY — history question only",
   "prevalence": "Not applicable as an active condition — history only.",
   "see": "Relevant only as part of a developmental history in a literacy or language assessment. Check current hearing if there are concerns; the history does not by itself explain adult difficulties.",
   "tools": [],
  },
  "Special Setting": {
   "applies": "YES — glue ear is common and persistent in Down syndrome and cleft palate, and often missed in complex needs",
   "prevalence": "Much higher in Down syndrome and cleft palate (NICE, 2008) — rate not stated here, check.",
   "see": "Hearing is easily overlooked when language delay is attributed to the primary condition. Check audiology is regular, ask about hearing aids or grommets, and make sure the communication environment (visual support, reduced noise) works on bad hearing days.",
   "tools": ["Communication Matrix / AAC review", "Vineland-3 / ABAS-3"],
  },
 },
},

]
