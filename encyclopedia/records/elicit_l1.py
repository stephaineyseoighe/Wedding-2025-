"""Elicit research evidence for condition entries 0-36 (auto-compiled from Elicit search_papers results)."""

def P(title, authors, year, venue, doi, typ, finding, easy, url=None):
    return {"title": title, "authors": authors, "year": year, "venue": venue, "doi": doi,
            "url": url or ("https://doi.org/" + doi if doi else ""), "type": typ,
            "finding": finding, "finding_easy": easy}

ELICIT = {}

ELICIT["condition::Autism"] = [
    P("School-Based Interventions for Increasing Autistic Pupils’ Social Inclusion in Mainstream Schools: A Systematic Review",
      "Yung‐Ting Tsou, L. Kovács, Angeliki Louloumari, Lex Stockmann, Els Blijd-Hoogewys, Alexander Koutamanis et al.", 2024,
      "Review Journal of Autism and Developmental Disorders", "10.1007/s40489-024-00429-2", "Systematic Review",
      "Across 56 studies, school-based interventions made school activities more accessible to autistic pupils, but reciprocity and friendship with peers did not necessarily improve. The review calls for a whole-school focus rather than only child social skills.",
      "School changes helped autistic pupils join in more. They did not always help them make friends."),
    P("A systematic review of school-based interventions targeting social communication behaviors for students with autism",
      "Bronwyn M Sutton, Amanda A. Webster, Marleen F. Westerveld", 2019, "Autism", "10.1177/1362361317753564", "Systematic Review",
      "The review of 22 studies found school-based interventions can increase how often autistic primary pupils start and respond to peer interaction, but most were resource-intensive and delivered away from the classroom by researchers or assistants.",
      "Help at school can make autistic children talk and play with other children more. Most of this help happened outside the classroom."),
    P("School-Based Peer-Related Social Competence Interventions for Children with Autism Spectrum Disorder: A Meta-Analysis and Descriptive Review of Single Case Research Design Studies",
      "Kelly Whalon, M. Conroy, Jose R. Martinez, Brittany L. Werch", 2015, "Journal of Autism and Developmental Disorders", "10.1007/s10803-015-2373-1", "Meta-Analysis",
      "Across 37 single-case studies of autistic children aged 3 to 12, school-based peer social skills interventions produced on average a moderate to strong effect, suggesting children benefit from social skill work with peers in school.",
      "Autistic children did better with other children when school taught social skills with classmates."),
]

ELICIT["condition::ADHD"] = [
    P("The Effects of Classroom Interventions on Off-Task and Disruptive Classroom Behavior in Children with Symptoms of Attention-Deficit/Hyperactivity Disorder: A Meta-Analytic Review",
      "Geraldina F. Gaastra, Y. Groen, Lara Tucha, O. Tucha", 2016, "PLoS ONE", "10.1371/journal.pone.0148841", "Meta-Analysis",
      "The review found teacher-delivered classroom interventions reduce off-task and disruptive behaviour in children with ADHD symptoms, with the largest effects for consequence-based and self-regulation approaches; classmates also appeared to benefit.",
      "Teachers can use simple classroom plans to help children with attention difficulties stay on task. Other children in the class can benefit too."),
    P("Attention Deficit Hyperactivity Disorders and Classroom-Based Interventions: Evidence-Based Status, Effectiveness, and Moderators of Effects in Single-Case Design Research",
      "Judith R. Harrison, Denise A. Soares, Stephen Rudzinski, Rachel Johnson", 2019, "Review of Educational Research", "10.3102/0034654319857038", "Meta-Analysis",
      "Across 27 single-case studies, classroom interventions for students with ADHD were moderately effective. Instructional and self-management interventions met evidence-based standards; behavioural ones worked best when chosen through functional assessment.",
      "Classroom help for pupils with attention difficulties works fairly well. Teaching methods and helping pupils manage themselves work best."),
    P("School-based randomized controlled trials for ADHD and accompanying impairments: a systematic review and meta-analysis",
      "Beliz Yegencik, Beth T. Bell, Emre Deniz", 2025, "Frontiers in Psychology", "10.3389/fpsyg.2025.1611145", "Meta-Analysis",
      "Pooling 22 school-based randomised trials, the review found improvements in inattention, academic performance and social skills and fewer externalising problems, but no significant effect on hyperactivity or impulsivity.",
      "School programmes helped children with attention difficulties focus, learn and get on with others. They did not calm restless behaviour much."),
]

ELICIT["condition::General Learning Disability (GLD) / Intellectual Disability"] = [
    P("Review of Interventions Supporting Secondary Students with Intellectual Disability in General Education Classes",
      "Emily M. Kuntz, E. Carter", 2019, "Research and Practice for Persons with Severe Disabilities", "10.1177/1540796919847483", "Systematic Review",
      "Across 40 studies in inclusive secondary classes, the review found systematic instruction, peer support, self-management, peer-mediated communication and placement changes had mostly positive effects, though study quality varied.",
      "Pupils with learning disability in mainstream secondary classes did well with clear teaching and help from classmates."),
    P("Systematic Review of Interventions Supporting Elementary Students With Intellectual Disability in General Education Classes",
      "Geonhwa Kim, Jennifer A. Kurth, Kathleen N. Tuck, Roxanne Loyless", 2025, "Research and Practice for Persons with Severe Disabilities", "10.1177/15407969251391663", "Systematic Review",
      "Reviewing 17 single-case studies in inclusive primary classes, the review found five approaches, with systematic instruction the most used; peer-mediated and self-directed strategies were rarely used with younger pupils.",
      "In mainstream primary classes, step-by-step teaching was used most. Help from classmates was used much less."),
    P("A systematic review of mathematics interventions for primary school students with intellectual disabilities",
      "Susanne Schnepel, Pirjo Aunio", 2021, "European Journal of Special Needs Education", "10.1080/08856257.2021.1943268", "Systematic Review",
      "The review of 20 studies found that systematic, explicit instruction with feedback and use of manipulatives are effective for teaching maths to primary pupils with intellectual disability, delivered in structured, high-intensity sequences.",
      "Children with learning disability learn maths best with clear step-by-step teaching, feedback and hands-on objects."),
]

ELICIT["condition::Dyslexia / Specific Learning Disorder with impairment in reading"] = [
    P("Forty Years of Reading Intervention Research for Elementary Students with or At Risk for Dyslexia: A Systematic Review and Meta-Analysis",
      "Colby Hall, Katlynn Dahl-Leonard, Eunsoo Cho, E. Solari, Philip Capin, Carlin L. Conner et al.", 2022, "Reading Research Quarterly", "10.1002/rrq.477", "Meta-Analysis",
      "Across 53 studies of primary pupils with or at risk for dyslexia, reading intervention had a significant positive effect on reading. Higher dosage gave larger effects, and effects were smaller for comprehension than word reading.",
      "Extra reading help works for children with dyslexia. More hours of help works better."),
    P("Current State of the Evidence: Examining the Effects of Orton-Gillingham Reading Interventions for Students With or at Risk for Word-Level Reading Disabilities",
      "E. Stevens, Christy R. Austin, Clint Moore, Nancy Scammacca, Alexis N. Boucher, S. Vaughn", 2021, "The Exceptional Child", "10.1177/0014402921993406", "Meta-Analysis",
      "The meta-analysis found Orton-Gillingham interventions did not significantly improve foundational reading skills or comprehension for students with or at risk for word-level reading disabilities, though the average effect was positive.",
      "One well-known dyslexia method did not clearly help more than other teaching. More good studies are needed."),
    P("Reading Interventions for Students in Grades 3–12 With Significant Word Reading Difficulties",
      "Alexis N. Boucher, Bethany H. Bhat, Nathan H. Clemens, Sharon Vaughn, Katherine E. O’Donnell", 2023, "Journal of Learning Disabilities", "10.1177/00222194231207556", "Meta-Analysis",
      "For older students with significant word reading difficulties, the review found a small positive effect of intervention, larger on pseudoword reading, and more total hours of intervention were linked to better outcomes.",
      "Older pupils with big reading difficulties made small gains with extra help. More hours helped more."),
]

ELICIT["condition::Developmental Language Disorder (DLD)"] = [
    P("Efficacy of the Treatment of Developmental Language Disorder: A Systematic Review",
      "S. Rinaldi, M. C. Caselli, Valentina Cofelice, Simonetta D’Amico, Anna Giulia De Cagno, Giuseppina Della Corte et al.", 2021, "Brain Science", "10.3390/brainsci11030407", "Systematic Review",
      "The review found early intensive intervention at ages 3 to 4 improves phonological skills with gains maintained, and morpho-syntactic intervention improves expressive but not receptive skills; evidence for vocabulary treatment was weaker.",
      "Early speech and language therapy helps young children with language disorder. It helps talking more than understanding."),
    P("Vocabulary interventions for children with developmental language disorder: a systematic review",
      "Rafiah Ansari, S. Chiat, Martin Cartwright, Rosalind Herman", 2025, "Frontiers in Psychology", "10.3389/fpsyg.2025.1517311", "Systematic Review",
      "Across 16 studies of children aged 5 to 11 with DLD, interventions targeting both the sounds and meanings of words gave the most reliable vocabulary gains, but gains rarely transferred to untaught words and faded after therapy.",
      "Teaching both the sound and meaning of new words helps children with language disorder learn them. They may forget words that are not practised."),
    P("Efficacy, model of delivery, intensity and targets of pragmatic interventions for children with developmental language disorder: A systematic review",
      "Kristine M. Jensen de López, J. Kraljević, Emilie L Bang Struntze", 2022, "International journal of language and communication disorders", "10.1111/1460-6984.12716", "Systematic Review",
      "The review of 11 studies found pragmatic intervention for children with DLD is feasible in individual, small-group and large-group formats, mostly targeting conversation and narrative skills, but studies varied widely in intensity and outcomes.",
      "Children with language disorder can be taught how to use language in conversation. This can be done one-to-one or in groups."),
]

ELICIT["condition::Developmental Coordination Disorder (DCD / dyspraxia)"] = [
    P("Task-oriented interventions for children with developmental co-ordination disorder.",
      "M. Miyahara, S. Hillier, Liz Pridham, S. Nakagawa", 2017, "Cochrane Database of Systematic Reviews", "10.1002/14651858.CD010914.pub2", "Meta-Analysis",
      "This Cochrane review of 15 trials found some evidence that task-oriented interventions improve motor performance in children with DCD, but the evidence was very low to low quality and the authors had little confidence in the effect.",
      "Practising real everyday tasks may help children with coordination difficulties move better. The research is weak so far."),
    P("Effectiveness of interventions to improve participation outcomes for children with developmental coordination disorder: A systematic review",
      "Á. O'Dea, K. Robinson, S. Coote", 2019, "British Journal of Occupational Therapy", "10.1177/0308022619866116", "Systematic Review",
      "Reviewing 12 studies, the review found limited evidence on participation outcomes for children with DCD; one trial favoured the CO-OP approach on self-rated performance and satisfaction, and more high-quality research is needed.",
      "There is little research on helping children with coordination difficulties take part in daily life. One approach looked helpful."),
    P("Evaluating the Efficacy of Gross-Motor-Based Interventions for Children with Developmental Coordination Disorder: A Systematic Review",
      "M. Alghadier, A. Alhusayni", 2024, "Journal of Clinical Medicine", "10.3390/jcm13164609", "Systematic Review",
      "Across 11 studies with 492 children, the review found gross-motor interventions produced moderate to large improvements in motor function, especially activity-oriented approaches that use games, small groups and real-world tasks.",
      "Active games and movement practice helped children with coordination difficulties improve their movement skills."),
]

ELICIT["condition::Generalised Anxiety Disorder"] = [
    P("Effectiveness of psychological interventions for child and adolescent specific anxiety disorders: A systematic review of systematic reviews and meta-analyses",
      "Teresa Galán-Luque", 2023, "Revista de Psicología Clínica con Niños y Adolescentes", "10.21134/rpcna.2023.10.1.3", "Systematic Review",
      "This review of reviews found cognitive behavioural interventions effective in the short and long term for generalised anxiety disorder, specific phobias and separation anxiety in children and adolescents, although review quality was critically low.",
      "Talking therapy that changes thoughts and actions helps children with worry and fears. Better studies are still needed."),
    P("School-based Mental Health Interventions Targeting Depression or Anxiety: A Meta-analysis of Rigorous Randomized Controlled Trials for School-aged Children and Adolescents",
      "Qiyang Zhang, Jun Wang, Amanda J. Neitzel", 2022, "Journal of Youth and Adolescence", "10.1007/s10964-022-01684-4", "Meta-Analysis",
      "Across 29 rigorous trials, school-based programmes reduced anxiety and depression. Outcomes were better for anxiety, for cognitive behavioural therapy, for clinician delivery and for secondary school students.",
      "School mental health programmes can reduce worry and low mood. Programmes led by trained therapists worked best."),
]

ELICIT["condition::Emotionally Based School Avoidance (EBSA)"] = [
    P("Treatment for School Refusal Among Children and Adolescents",
      "Brandy R. Maynard, D. Heyne, Kristen Esposito Brendel, Jeffery J. Bulanda, A. Thompson, Terri D. Pigott", 2018, "Research on Social Work Practice", "10.1177/1049731515598619", "Meta-Analysis",
      "Across eight studies with 435 young people, psychosocial treatments for school refusal significantly improved attendance but did not significantly reduce anxiety in the short term.",
      "Therapy helped children who refuse school go to school more. It did not reduce their worry straight away."),
    P("School partnered approaches to emotionally based school avoidance in UK primary and secondary school‐age learners: A systematic review",
      "Caitlin McDonald, Aneeza Pervez", 2025, "British Educational Research Journal", "10.1002/berj.4205", "Systematic Review",
      "The review found too few and too weak UK studies to judge which school-partnered EBSA interventions work; a recurrent theme was a punitive education culture in response to absence.",
      "There is not enough research to know what school help works for anxious children who miss school. Punishing absence came up often."),
    P("What school-based interventions work to improve attendance in secondary school students with persistent absence? A systematic review",
      "A. Middleton, Martha Watson, Joanna K. Anderson", 2026, "Frontiers in child and adolescent psychiatry", "10.3389/frcha.2025.1603680", "Systematic Review",
      "Reviewing 16 studies, the review found favourable but inconsistent results for mentoring, family involvement, school counselling, incentives and school-based healthcare for persistently absent secondary students; the evidence base remains limited.",
      "Mentors, family links and school counselling may help teenagers who miss a lot of school. The research is still limited."),
]

ELICIT["condition::Separation Anxiety Disorder"] = [
    P("Evaluation of Cognitive-Behavioral Therapy Efficacy in the Treatment of Separation Anxiety Disorder in Childhood and Adolescence: a Systematic Review of Randomized Controlled Trials",
      "Ludovica Giani, M. Caputi, B. Forresi, G. Michelini, Simona Scaini", 2021, "International Journal of Cognitive Therapy", "10.1007/s41811-021-00129-3", "Systematic Review",
      "The review of nine trials supports CBT for separation anxiety. Preschoolers benefited more from disorder-specific protocols and older children from transdiagnostic ones, and parent sessions helped especially with younger children.",
      "Talking therapy helps children who are very scared to be apart from parents. Involving parents helps younger children most."),
    P("Effectiveness of psychological interventions for child and adolescent specific anxiety disorders: A systematic review of systematic reviews and meta-analyses",
      "Teresa Galán-Luque", 2023, "Revista de Psicología Clínica con Niños y Adolescentes", "10.21134/rpcna.2023.10.1.3", "Systematic Review",
      "This review of reviews found cognitive behavioural interventions effective in the short and long term for separation anxiety disorder, alongside generalised anxiety and specific phobias, although the quality of included reviews was critically low.",
      "Talking therapy that changes thoughts and actions helps children with separation fears. Better studies are still needed."),
]

ELICIT["condition::Social Anxiety Disorder (social phobia)"] = [
    P("Efficacy and acceptability of psychological interventions for social anxiety disorder in children and adolescents: a meta-analysis of randomized controlled trials",
      "Lining Yang, Xinyu Zhou, Juncai Pu, Lanxiang Liu, P. Cuijpers, Yuqing Zhang et al.", 2018, "European Child and Adolescent Psychiatry", "10.1007/s00787-018-1189-x", "Meta-Analysis",
      "Across 17 trials, psychological interventions such as CBT were more effective than control conditions for social anxiety in young people and improved quality of life and functioning, though heterogeneity was high.",
      "Talking therapy helps young people who are very shy or scared in social situations. It also helps daily life."),
    P("School-based cognitive-behavioural therapy for children and adolescents with social anxiety disorder and social anxiety symptoms: A systematic review",
      "Zoie Wai Man Tse, Shaista Emad, Md.Kamrul Hasan, I. Papathanasiou, Ibad Ur Rehman, K. Lee", 2023, "PLoS ONE", "10.1371/journal.pone.0283329", "Systematic Review",
      "Across seven studies, school-based CBT programmes such as FRIENDS, Super Skills for Life and SASS had minor effects in reducing social anxiety, with evidence quality limited and funding and staffing named as barriers.",
      "Therapy groups in school helped social worry a little. Schools need staff and money to run them well."),
    P("The state of psychological treatments for social anxiety disorder in children and adolescents: An Umbrella Review",
      "Mª del Mar Diaz-Castela", 2023, "Revista de Psicología Clínica con Niños y Adolescentes", "10.21134/rpcna.2023.10.1.2", "Review",
      "This umbrella review of six reviews found CBT effective in the short and long term for social anxiety in young people, with exposure and social skills training the most effective components.",
      "Therapy works for social worry. Facing fears step by step and learning social skills help most."),
]

ELICIT["condition::Posttraumatic Stress Disorder (PTSD), including Complex PTSD"] = [
    P("Psychological and psychosocial treatments for children and young people with post-traumatic stress disorder: a network meta-analysis.",
      "Ifigeneia Mavranezouli, Odette Megnin-Viggars, C. Daly, S. Dias, S. Stockton, R. Meiser-Stedman et al.", 2019, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.13094", "Meta-Analysis",
      "Across 32 trials, trauma-focused CBT, particularly individual forms, appeared most effective for PTSD in young people; EMDR was effective to a lesser extent and supportive counselling did not appear effective.",
      "Trauma-focused talking therapy works best for children after a frightening event. General counselling did not seem to help."),
    P("A systematic review and meta-analysis of school-based interventions for PTSD and trauma-related symptoms: what effective elements they have in common?",
      "Kirsten Rowlinson, L. Grummitt, Isabelle Lynch, Chloe Conroy, Ivana Kihas, Erin V Kelly et al.", 2026, "Child and Adolescent Mental Health", "10.1111/camh.70100", "Meta-Analysis",
      "Across 45 studies, school-based trauma programmes had a medium to large effect in reducing PTSD symptoms. Common elements were psychoeducation, CBT, coping skills, group format, trained facilitators and parent involvement.",
      "School trauma programmes can reduce trauma symptoms. Good ones teach coping skills and involve parents."),
    P("Psychological Treatments for Symptoms of Posttraumatic Stress Disorder in Children, Adolescents, and Young Adults: A Meta-Analysis",
      "Jana Gutermann, Franziska Schreiber, Simone Matulis, Laura Schwartzkopff, Julia Deppe, R. Steil", 2016, "Clinical Child and Family Psychology Review", "10.1007/s10567-016-0202-5", "Meta-Analysis",
      "Across 135 studies, CBT yielded the largest effects on PTSD symptoms in young people, especially when delivered individually with parents involved; age and caretaker involvement moderated effects.",
      "Talking therapy helps young people with trauma symptoms. It works best one-to-one with a parent involved."),
]

ELICIT["condition::Reactive Attachment Disorder (RAD)"] = [
    P("Annual Research Review: Attachment disorders in early childhood – clinical presentation, causes, correlates and treatment",
      "C. Zeanah, M. Gleason", 2014, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.12347", "Review",
      "The review found considerable evidence for two separate disorders: reactive attachment disorder, where children lack attachments despite being able to form them, and disinhibited social engagement disorder. Little is known about effective interventions.",
      "Some children who had very poor early care do not form close bonds. We still know little about what help works best."),
]

ELICIT["condition::Disinhibited Social Engagement Disorder (DSED)"] = [
    P("Social competencies of children with disinhibited social engagement disorder: A systematic review",
      "C. Davidson, S. Islam, E. Venturini, Anja Lowit, C. Gillberg, H. Minnis", 2024, "JCPP Advances", "10.1002/jcv2.12226", "Systematic Review",
      "Across 16 studies, children with DSED consistently had poorer social competencies and more peer problems than comparison children and may have low self-esteem about social acceptance; findings on communication skills were mixed.",
      "Children who are too friendly with strangers often have problems with friends too. They may feel less liked."),
    P("Meta-Analyses of the Associations Between Disinhibited Social Engagement Behaviors and Child Attachment Insecurity or Disorganization",
      "Lory Zephyr, C. Cyr, Sébastien Monette, Maude Archambault, Stine Lehmann, H. Minnis", 2021, "Research on Child and Adolescent Psychopathology", "10.1007/s10802-021-00777-1", "Meta-Analysis",
      "Across 24 studies, disinhibited social engagement behaviour showed small links with attachment insecurity and disorganisation, stronger with observational measures, suggesting attachment-informed interventions could help but other factors matter too.",
      "Being over-friendly with strangers is only partly linked to how a child bonds with carers. Other things matter too."),
]

ELICIT["condition::English as an Additional Language and bilingual development (DLD vs EAL)"] = [
    P("The Use of Language Sample Analysis to Differentiate Developmental Language Disorder From Typical Language in Bilingual Children: A Systematic Review and Meta-Analysis.",
      "J. Ortiz, Jessica M Nolasco, Yi Ting Huang, Jason C. Chow", 2024, "Journal of Speech, Language and Hearing Research", "10.1044/2024_JSLHR-24-00212", "Meta-Analysis",
      "Across 35 studies, language sample analysis distinguished bilingual children with DLD from those with typical language, with morphosyntactic accuracy measures showing the largest differences; classification accuracy needs more study.",
      "Listening to how a bilingual child talks can help show if they have a language disorder or are still learning a new language."),
    P("Language Sample Analysis in Bilingual Children: A Meta-Analysis of Diagnostic Accuracy.",
      "J. Ortiz, Jason C. Chow, Jessica M Nolasco, Yi Ting Huang", 2026, "American Journal of Speech-Language Pathology", "10.1044/2025_AJSLP-25-00201", "Meta-Analysis",
      "Across nine studies, the diagnostic accuracy of language sample analysis for DLD in bilingual children ranged from poor to good. Integrated measures combining it with other methods were most accurate, so it is best used within a wider battery.",
      "One test alone is not enough to spot language disorder in bilingual children. Using several methods together works best."),
    P("Using Nonword Repetition to Identify Developmental Language Disorder in Monolingual and Bilingual Children: A Systematic Review and Meta-Analysis.",
      "Salomé Schwob, Laurane Eddé, L. Jacquin, Mégane Leboulanger, M. Picard, Patricia Ramos Oliveira et al.", 2021, "Journal of Speech, Language and Hearing Research", "10.1044/2021_JSLHR-20-00552", "Meta-Analysis",
      "Across 46 studies, nonword repetition discriminated children with and without DLD in both monolingual and bilingual contexts, but materials should suit the child's language background and be combined with other tools such as parent questionnaires.",
      "Repeating made-up words can help spot language disorder in children who speak one or more languages. It should be used with other checks."),
]

_VIS = P("Treatment of Depression in Children and Adolescents",
      "M. Viswanathan, Sara M. Kennedy, J. McKeeman, R. Christian, M. Coker-Schwimmer, J. Middleton et al.", 2020, "", "10.23970/ahrqepccer224", "Systematic Review",
      "Across 60 studies, the review found CBT, some SSRIs and their combination may improve symptoms in adolescents with major depression, while CBT or family therapy may help children with any depressive disorder, including persistent depressive disorder.",
      "Talking therapy and some medicines can help teenagers with depression. Family therapy may help younger children.")

ELICIT["condition::Major Depressive Disorder"] = [
    P("Practitioner Review: Effectiveness of indicated school-based interventions for adolescent depression and anxiety - a meta-analytic review.",
      "Brioney Gee, S. Reynolds, Ben Carroll, F. Orchard, Tim Clarke, David Martin et al.", 2020, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.13209", "Meta-Analysis",
      "Across 45 trials, indicated school-based interventions had a small effect on adolescent depression symptoms immediately after, maintained only in the short term. Interventions delivered by school staff did not show significant effects.",
      "School programmes for teenagers with low mood help a little at first. The help does not last long."),
    P("Effectiveness of psychological treatments for depression in childhood and adolescence: A review of reviews",
      "J. Espada", 2023, "Revista de Psicología Clínica con Niños y Adolescentes", "10.21134/rpcna.2023.10.1.6", "Systematic Review",
      "This review of eight reviews found psychological treatments for youth depression produce significant but modest effects. Interpersonal therapy and CBT were the main effective options for adolescents; data for younger children were insufficient.",
      "Talking therapies help teenagers with depression a bit. We know less about what helps younger children."),
    _VIS,
]

ELICIT["condition::Persistent Depressive Disorder (dysthymia)"] = [
    P("The Formation and Development of the Concept of Dysthymia in Child Psychiatry",
      "V. E. Pashkovskiy", 2026, "Psychiatry", "10.30629/2618-6667-2026-24-1-86-100", "Review",
      "The review reports that dysthymia in children and adolescents often presents covertly, masked as personality traits, behaviour or somatic complaints, has a prolonged course affecting school adaptation, and is often inadequately treated.",
      "Long-lasting low mood in children is easy to miss. It can affect school for a long time."),
    _VIS,
]

ELICIT["condition::Oppositional Defiant Disorder (ODD)"] = [
    P("Psychosocial Interventions for Disruptive Behavior in Children and Adolescents: A Meta-analysis.",
      "S. Selph, E. Brodt, Tracy Dana, Andrea C. Skelly, C. Atchison, Rongwei Fu et al.", 2026, "Pediatrics", "10.1542/peds.2025-072476", "Meta-Analysis",
      "Across 64 trials, parent-only and multicomponent interventions involving a parent, caregiver or teacher plus the child reduced disruptive behaviour in preschool and school-aged children immediately after treatment; long-term and adolescent evidence was limited.",
      "Programmes for parents, and for parents, teachers and child together, reduce difficult behaviour in young children."),
    P("Psychosocial Interventions for Child Disruptive Behaviors: A Meta-analysis",
      "R. Epstein, C. Fonnesbeck, Shannon A Potter, Katherine H Rizzone, M. McPheeters", 2015, "Pediatrics", "10.1542/peds.2015-2577", "Meta-Analysis",
      "The meta-analysis found child-only, parent-only and multicomponent interventions all more effective than control conditions for disruptive behaviour disorders, with interventions including a parent component likely to have the largest effect.",
      "Help for children with difficult behaviour works. Help that includes parents works best."),
    P("The Efficacy of Parent Training Interventions for Disruptive Behavior Disorders in Treating Untargeted Comorbid Internalizing Symptoms in Children and Adolescents: A Systematic Review",
      "Eleni Zarakoviti, R. Shafran, D. Papadimitriou, S. Bennett", 2021, "Clinical Child and Family Psychology Review", "10.1007/s10567-021-00349-1", "Systematic Review",
      "Across 12 studies of programmes such as Incredible Years and Triple P, parent training reduced disruptive behaviour in 11 studies and also reduced co-occurring anxiety or low mood symptoms in seven.",
      "Parenting programmes reduced difficult behaviour. They often helped children's worry and sadness too."),
]

ELICIT["condition::Conduct Disorder (CD)"] = [
    P("Practitioner Review: Psychological treatments for children and adolescents with conduct disorder problems – a systematic review and meta‐analysis",
      "M. Bakker, C. Greven, J. Buitelaar, J. Glennon", 2017, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.12590", "Meta-Analysis",
      "Across 17 trials, psychological treatments had a small effect in reducing parent-, teacher- and observer-rated conduct problems, but no effect on self-report, and no one treatment was supported over another.",
      "Therapy helps a little with serious behaviour problems. No single type of therapy was clearly best."),
    P("A scoping review of randomized controlled trials of parenting and family-based interventions for 10 - 17 year-olds with severe and persistent conduct problems.",
      "Vera J. Lee, S. Watson, Aron Shlonsky, M. Tarren‐Sweeney", 2024, "Journal of Evidence-Based Social Work", "10.1080/26408066.2024.2409094", "Review",
      "Of 25 trials of family-based interventions for 10 to 17 year olds with severe conduct problems, only 10 showed a treatment effect; Multisystemic Therapy and Functional Family Therapy had uncertain effectiveness.",
      "Family programmes for teenagers with serious behaviour problems do not always work. More research is needed."),
    P("A Meta-Analysis of Long-Term Outpatient Treatment Effects for Children and Adolescents with Conduct Problems",
      "S. Fossum, B. Handegård, F. Adolfsen, S. Vis, R. Wynn", 2015, "Journal of Child and Family Studies", "10.1007/s10826-015-0221-8", "Meta-Analysis",
      "Across 56 studies, treatment effects on conduct problems lasted after treatment ended but changes at follow-up were small; CBT approaches showed larger later changes, and few studies included teenagers.",
      "Help for behaviour problems can last after it ends. The extra gains later are small."),
]

ELICIT["condition::Disruptive Mood Dysregulation Disorder (DMDD)"] = [
    P("Practitioner Review: Definition, recognition, and treatment challenges of irritability in young people.",
      "A. Stringaris, P. Vidal-Ribas, M. Brotman, E. Leibenluft", 2018, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.12823", "Review",
      "The review describes DMDD as capturing children whose main problem is severe irritability, distinct from bipolar disorder, and reports indirect evidence that parent management training and CBT are the best-supported psychological treatments.",
      "Some children are very cross and angry most of the time. Parent training and talking therapy look most helpful."),
    P("Psychosocial Treatment of Irritability in Youth",
      "K. Kircanski, Michal Clayton, E. Leibenluft, M. Brotman", 2018, "Current Treatment Options in Psychiatry", "10.1007/s40501-018-0141-5", "Review",
      "The review reports no well-established treatments specifically for DMDD, describes parent management training and CBT for disruptive behaviour, and presents early data on a new exposure-based CBT for severe irritability.",
      "There is no proven treatment yet for very angry, irritable children. New therapies are being tested."),
]

ELICIT["condition::Selective Mutism"] = [
    P("A systematic review and meta‐analysis of nonpharmacological interventions for children and adolescents with selective mutism",
      "Gino Hipolito, Emma Pagnamenta, Helen Stacey, E. Wright, V. Joffe, K. Murayama et al.", 2023, "JCPP Advances", "10.1002/jcv2.12166", "Meta-Analysis",
      "Across 25 studies, outcomes for non-drug interventions were variable. Combined systems and behavioural approaches had a large effect on speaking behaviour compared with waitlist, but evaluation remains limited.",
      "Plans that involve home and school and build up speaking step by step look helpful for children who do not speak in school."),
    P("Treatment of selective mutism based on cognitive behavioural therapy, psychopharmacology and combination therapy – a systematic review",
      "K. Østergaard", 2018, "Nordic Journal of Psychiatry", "10.1080/08039488.2018.1439530", "Systematic Review",
      "The review found CBT, and to a lesser extent medication, showed promising results for selective mutism, but small samples, few randomised trials and short follow-up limit the evidence.",
      "Talking therapy looks promising for children who do not speak in some places. The research is still small."),
]

ELICIT["condition::Specific Phobia"] = [
    P("One-Session Treatment of Specific Phobias in Children: Recent Developments and a Systematic Review.",
      "Thompson E. Davis, T. Ollendick, Lars-Göran Öst", 2019, "Annual Review of Clinical Psychology", "10.1146/annurev-clinpsy-050718-095608", "Systematic Review",
      "The review describes One-Session Treatment, a single massed session of graduated exposure with modelling and skills training, as a well-established evidence-based treatment for specific phobias in young people, supported by almost two decades of research.",
      "One long session of facing a fear step by step can help children with a strong fear of one thing."),
    P("Brief, Non-Pharmacological, Interventions for Pediatric Anxiety: Meta-Analysis and Evidence Base Status",
      "R. Stoll, A. Pina, J. Schleider", 2020, "Journal of Clinical Child & Adolescent Psychology", "10.1080/15374416.2020.1738237", "Meta-Analysis",
      "Across 76 trials, brief non-drug interventions had a small overall effect on child anxiety, with effects varying widely; about three hours of in-vivo exposure in one session showed capacity for change in specific phobia.",
      "Short programmes can help children with anxiety. Facing a fear in one session can help with a single strong fear."),
]

ELICIT["condition::Panic Disorder and Agoraphobia"] = [
    P("Moderators of intensive CBT for adolescent panic disorder: the of fear and avoidance",
      "R. M. Elkins, K. Gallo, Donna B. Pincus, Jonathan S. Comer", 2015, "Child and Adolescent Mental Health", "10.1111/CAMH.12122", "RCT",
      "In a trial of 54 adolescents with panic disorder with or without agoraphobia, intensive CBT reduced symptoms compared with waitlist, with larger effects for those with fewer feared and avoided situations at the start.",
      "A short, intensive talking therapy helped teenagers with panic attacks. It helped most when they avoided fewer places."),
    P("Intensive Treatments for Adolescents with Panic Disorder and Agoraphobia: Helping Youth Move beyond Avoidance",
      "Donna B. Pincus, M. Elkins, Christina Hardway", 2014, "Journal of Experimental Psychopathology", "10.5127/pr.033313", "Review",
      "The review reports that CBT for adolescent panic disorder delivered intensively over eight consecutive days gives reductions in symptoms comparable to weekly treatment and shows promise for comorbid conditions.",
      "Therapy for panic can work in eight days in a row. It works about as well as weekly therapy."),
    P("Assessment and management of anxiety disorders in children and adolescents",
      "C. Creswell, P. Waite, P. Cooper", 2014, "Archives of Disease in Childhood", "10.1136/archdischild-2013-303768", "Review",
      "The review covers assessment and treatment of childhood anxiety disorders including panic disorder and agoraphobia, reporting CBT as the evidence-based psychological treatment and that routine prescribing is not recommended.",
      "Talking therapy is the main help for anxious children, including those with panic. Medicine is not usually the first step."),
]

ELICIT["condition::Adjustment Disorder"] = [
    P("Adjustment disorder in the pediatric population",
      "George Alvarado", 2021, "Pediatric Medicine", "10.21037/PM-20-76", "Review",
      "The review notes adjustment disorder is a useful but variably used diagnosis in children, at times underused because of concerns about validity and a lack of diagnosis-specific treatments, and reviews psychotherapy and medication options.",
      "Some children struggle for a while after a big change or stress. There is little research on help made just for this."),
]

ELICIT["condition::Acute Stress Disorder"] = [
    P("Early psychological intervention following recent trauma: A systematic review and meta-analysis",
      "N. Roberts, N. Kitchiner, J. Kenardy, Catrin E Lewis, J. Bisson", 2019, "European Journal of Psychotraumatology", "10.1080/20008198.2019.1695486", "Meta-Analysis",
      "Across 61 studies, early interventions offered to everyone exposed to trauma showed no clinically important benefit, but for people with symptoms, trauma-focused CBT had the strongest evidence, with largest benefits for those with acute stress disorder or PTSD.",
      "Help for everyone after a frightening event did not make a real difference. Trauma-focused therapy helped people who had strong symptoms."),
    P("Trauma and post-traumatic stress disorder in children and adolescents",
      "G. Kolaitis", 2017, "European Journal of Psychotraumatology", "10.1080/20008198.2017.1351198", "Review",
      "The review reports that acute stress reaction is a predictor of later PTSD in young people, that resilience is the rule after disasters with PTSD roughly halving within six months, and that CBT with parental involvement is effective.",
      "Most children recover after a frightening event. Strong early stress can be a sign that more help is needed."),
]

ELICIT["condition::Prolonged Grief Disorder"] = [
    P("Interventions for Prolonged Grief Disorder in Children and Adolescents: A Systematic Review",
      "Sarah Bondy, H. Scott", 2025, "Journal of Child and Adolescent Trauma", "10.1007/s40653-024-00677-8", "Systematic Review",
      "Across ten studies, interventions for prolonged grief in young people were generally positive in reducing symptoms. Most shared psychoeducation and involved the surviving parent, a key difference from adult treatment.",
      "Help for children with long-lasting, painful grief usually works. Involving the parent who is still alive is important."),
    P("Interventions for Young Bereaved Children: A Systematic Review and Implications for School Mental Health Providers",
      "C. Chen, Andrea Panebianco", 2017, "Child and Youth Care Forum", "10.1007/s10566-017-9426-x", "Systematic Review",
      "The review of 17 studies found play-based therapies were most common for bereaved preschool children and that involving parents was a critical ingredient, but empirical evidence of positive outcomes was limited.",
      "Play therapy is often used with young children after a death in the family. Parents are key to helping them cope."),
]

ELICIT["condition::Speech Sound Disorder"] = [
    P("A systematic review and classification of interventions for speech-sound disorder in preschool children.",
      "Y. Wren, Sam Harding, J. Goldbart, S. Roulstone", 2018, "International journal of language and communication disorders", "10.1111/1460-6984.12371", "Systematic Review",
      "Reviewing 26 studies of preschool children with speech sound disorder, the review found cognitive-linguistic and production approaches most often reported, with the highest-graded evidence for auditory-perceptual and integrated approaches, though most evidence was lower-graded.",
      "Several kinds of speech therapy are used with young children who mix up sounds. Stronger research is still needed."),
    P("Intervention studies with group design targeting expressive phonology for children with developmental speech and language disorder: A systematic review and meta-analysis.",
      "Sari Kunnari, Susana Sanduvete Chaves, S. Chacón-Moscoso, D. Alves, Martina Ozbič, K. Petinou et al.", 2024, "International journal of language and communication disorders", "10.1111/1460-6984.13110", "Meta-Analysis",
      "Across 23 group-design studies of children with developmental speech and/or language disorder, interventions had medium to high average effects on speech production accuracy, though reporting quality needs to improve.",
      "Speech therapy helps children say sounds more clearly."),
    P("Intervention Effects on Phonological Processing in Children With Developmental Speech and/or Language Disorder: A Systematic Review and Meta‐Analysis of Studies With Group Design",
      "Marja R. Laasonen, Susana Sanduvete‐Chaves, S. Chacón-Moscoso, D. Alves, Martina Ozbič, K. Petinou et al.", 2026, "International journal of language and communication disorders", "10.1111/1460-6984.70252", "Meta-Analysis",
      "Across 22 studies, oral language interventions produced large improvements in phonological awareness and phonological short-term memory in children with speech and/or language disorders, which may indirectly support reading.",
      "Speech and language therapy can help children hear and remember sounds in words. This may help reading later."),
]

ELICIT["condition::Childhood-Onset Fluency Disorder (stuttering)"] = [
    P("Psychosocial features of stuttering for school-age children: A systematic review.",
      "Georgina Johnson, M. Onslow, Sarah Horton, Elaina Kefalianos", 2023, "International journal of language and communication disorders", "10.1111/1460-6984.12887", "Systematic Review",
      "Across 22 studies of children aged 6 to 12 who stutter, impact of stuttering, anxiety and speech satisfaction showed potential treatment effects; CBT and two behavioural treatments were associated with reduced anxiety.",
      "Children who stutter can feel worried about talking. Some therapies help reduce this worry."),
    P("Treatment for School-Age Children Who Stutter: A Systematic Review of Japanese Literature.",
      "Daichi Iimura, Kohei Kakuta, Takuya Oe, Hiroaki Kobayashi, N. Sakai, Shoko Miyamoto", 2022, "Language, Speech & Hearing Services in Schools", "10.1044/2021_LSHSS-21-00044", "Systematic Review",
      "Reviewing 40 mostly case-series studies, the review classified treatments for school-age stuttering into speech therapy, psychological therapy and changes to the child's environment, and called for more rigorous evidence.",
      "Help for school children who stutter includes speech therapy, talking therapy and changes around the child. Better research is needed."),
]

ELICIT["condition::Social (Pragmatic) Communication Disorder"] = [
    P("Practitioner review: Social (pragmatic) communication disorder conceptualization, evidence and clinical implications.",
      "C. Norbury", 2014, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.12154", "Review",
      "The review concludes SPCD is probably best seen as a dimensional symptom profile across neurodevelopmental disorders, with high comorbidity, few well-validated assessment measures and few rigorously tested interventions.",
      "Some children find the social use of language hard. There are few good tests or proven programmes for this yet."),
    P("‘Look at me when I am talking to you’: evidence and assessment of social pragmatics interventions for children with autism and social communication disorders",
      "Cheryl D. Tierney, M. Kurtz, Ann Panchik, Kathleen Pitterle", 2014, "Current opinion in pediatrics", "10.1097/MOP.0000000000000075", "Review",
      "The review reports emerging evidence for peer mentoring, social skills groups and video modelling in children with autism and social communication disorders; social stories help but generalise poorly, and individualised programmes work best.",
      "Friends as mentors, social skills groups and videos can help children learn social talk. Plans that fit the child work best."),
]

ELICIT["condition::Global Developmental Delay (GDD)"] = [
    P("Effectiveness of Early Intervention Programs for Young Children with Global Developmental Delay: A Systematic Review",
      "Sarah Almuhanna, Omar A Alshehri, Bandar Mohammed B. alsaadoon, Mohammad Hassan Mohammed Alawad, A. Alnasyan, S. Abuabat et al.", 2025, "Galen medical journal", "10.31661/gmj.vi.3906", "Systematic Review",
      "Across six studies, all early intervention programmes for children with GDD reported gains in at least one developmental area, with greater gains when started early and sustained and when caregivers were involved, but certainty of evidence was low.",
      "Early help for young children with delays in many areas can help them progress. Starting early and involving parents helps most."),
    P("Screening for developmental delay among children aged 1-4 years: a systematic review.",
      "Rachel Warren, Meghan Kenny, T. Bennett, D. Fitzpatrick-Lewis, M. Ali, D. Sherifali et al.", 2016, "CMAJ Open", "10.9778/cmajo.20140121", "Systematic Review",
      "The review found only two studies; screening with the Ages and Stages Questionnaire led to more and faster referrals to early intervention, but the evidence on benefits of screening for developmental delay in children aged 1 to 4 was inconclusive.",
      "Checking all young children for delays led to faster referrals. We do not yet know if it improves later outcomes."),
]

ELICIT["condition::Borderline Intellectual Functioning (BIF)"] = [
    P("Treatment, Education, and Prognosis of Slow Learners (Borderline Intelligence)",
      "So Hee Lee", 2024, "Soa--ch'ongsonyon chongsin uihak = Journal of child & adolescent psychiatry", "10.5765/jkacap.240014", "Review",
      "Reviewing ten studies, the review found borderline intelligence is linked to comorbid anxiety, depression and ADHD and to academic and social challenges, and that addressing neglect and comorbid conditions and intervening early in childhood are important.",
      "Children who learn a bit more slowly than others often have other difficulties too. Early help is important."),
    P("Exploring the Clinical Characteristics and Comorbid Disorders of Borderline Intellectual Functioning",
      "Minae Kim, K. Cheon", 2024, "Soa--ch'ongsonyon chongsin uihak = Journal of child & adolescent psychiatry", "10.5765/jkacap.240012", "Review",
      "The review reports that borderline intellectual functioning is underdiagnosed and linked to greater risk of academic failure, need for special educational support, emotional problems and poorer social and adaptive functioning.",
      "Children in this group are often missed. They may need extra help at school and with feelings."),
]

ELICIT["condition::Specific Learning Disorder with impairment in mathematics (dyscalculia)"] = [
    P("Interventions for Children With Mathematical Difficulties A Meta-Analysis",
      "Sabrina Chodura, Joerg-Tobias Kuhn, H. Holling", 2015, "", "10.1027/2151-2604/A000211", "Meta-Analysis",
      "Across 35 controlled studies, interventions for children with mathematical difficulties had a high mean effect, with significant effects for direct or assisted instruction, fostering basic arithmetic and one-to-one settings; computer versus face-to-face delivery made no difference.",
      "Extra maths help works well for children who find maths very hard. Clear teaching of basic sums works best."),
    P("A systematic review of interventions for children presenting with dyscalculia in primary schools",
      "Thato Monei, Athena Pedro", 2017, "Educational Psychology in Practice", "10.1080/02667363.2017.1289076", "Systematic Review",
      "Reviewing literature from 2004 to 2014, the review provides an evidence base of interventions that can be used in primary schools for children with dyscalculia, presenting various instructional methods with a holistic focus.",
      "There are school methods that can help primary children with serious maths difficulties."),
]

ELICIT["condition::Specific Learning Disorder with impairment in written expression (dysgraphia)"] = [
    P("Level and Trend of Writing Sequences: A Review and Meta-Analysis of Writing Interventions for Students With Disabilities",
      "Shawn M. Datchuk, Kyle Wagner, Bridget O. Hier", 2020, "The Exceptional Child", "10.1177/0014402919873311", "Meta-Analysis",
      "Across 18 single-case studies, writing interventions such as direct instruction and self-regulated strategy development produced gradual improvement in correct writing sequences for students with disabilities and writing difficulties.",
      "Clear teaching and planning strategies help pupils with writing difficulties write more words correctly over time."),
    P("Integrated Reading and Writing Interventions for Students with Learning Disabilities: A Review of the Literature",
      "E. Kang, J. McKenna, Sarah V. Arden, Stephen P. Ciullo", 2016, "Learning Disabilities Research & Practice", "10.1111/ldrp.12091", "Systematic Review",
      "The review of ten studies, mostly in grades 4 to 8, found encouraging results for interventions that integrate reading and writing for students with learning disabilities, though only four met design standards.",
      "Teaching reading and writing together looks helpful for pupils with learning difficulties. More good studies are needed."),
]

ELICIT["condition::Tic disorders and Tourette's Disorder"] = [
    P("Practitioner Review: Treatments for Tourette syndrome in children and young people - a systematic review.",
      "C. Whittington, M. Pennant, T. Kendall, C. Glazebrook, P. Trayner, M. Groom et al.", 2016, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.12556", "Systematic Review",
      "Across 40 trials, habit reversal training and CBIT reduced tics with moderate certainty, as did clonidine and guanfacine; antipsychotics also helped but carry more risk of harm, and physical and dietary treatments lacked evidence.",
      "Behaviour therapy that teaches a child to notice and manage tics helps. Some medicines help too."),
    P("Clinical effectiveness and patient perspectives of different treatment strategies for tics in children and adolescents with Tourette syndrome: a systematic review and qualitative analysis.",
      "C. Hollis, M. Pennant, José Cuenca, C. Glazebrook, T. Kendall, C. Whittington et al.", 2016, "Health Technology Assessment", "10.3310/hta20040", "Systematic Review",
      "The review found habit reversal training or CBIT, antipsychotics and noradrenergic agents effective for tics. Families reported delays in diagnosis, poor access to behavioural therapy and a lack of information provided to schools.",
      "Behaviour therapy and some medicines reduce tics. Families said schools often lacked information about tics."),
]

ELICIT["condition::Stereotypic Movement Disorder"] = [
    P("Effects of Physical Exercise Interventions on Stereotyped Motor Behaviours in Children with ASD: A Meta-Analysis",
      "Elizabeth J. Teh, Ranjith Vijayakumar, Timothy Xing Jun Tan, M. Yap", 2021, "Journal of Autism and Developmental Disorders", "10.1007/s10803-021-05152-z", "Meta-Analysis",
      "Across 22 studies of autistic children, physical exercise significantly reduced stereotyped motor behaviours, and higher exercise intensity predicted better results; age, duration and setting did not.",
      "Exercise, especially harder exercise, reduced repeated body movements in autistic children."),
    P("Primary motor stereotypies",
      "Lana Zrnić", 2024, "Specijalna Edukacija i Rehabilitacija", "10.5937/specedreh23-46951", "Review",
      "The review reports that primary motor stereotypies in typically developing children can disrupt daily activities and social development, their cause is unknown, and behavioural therapies are the possible treatments, though research is scarce.",
      "Some children repeat the same movements a lot. Behaviour therapy may help, but there is little research."),
]

ELICIT["condition::Obsessive-Compulsive Disorder"] = [
    P("Psychological Treatment of Obsessive-Compulsive Disorder in Children and Adolescents: a Meta-Analysis",
      "A. Rosa-Alcázar, J. Sánchez-Meca, Ángel Rosa-Alcázar, Marina Iniesta-Sepúlveda, José Olivares-Rodríguez, J. Parada-Navas", 2015, "The Spanish Journal of Psychology", "10.1017/sjp.2015.22", "Meta-Analysis",
      "Across 46 studies, CBT showed large effects in reducing obsessive-compulsive symptoms in young people. The most promising programmes combined exposure and response prevention, cognitive strategies and relapse prevention.",
      "Talking therapy that helps children face fears without doing rituals works well for this condition."),
    P("Standard individual cognitive behaviour therapy for paediatric obsessive–compulsive disorder: A systematic review of effect estimates across comparisons",
      "Gudmundur Skarphedinsson, Ketil Hanssen-Bauer, H. Kornør, E. Heiervang, N. Landrø, Brynhildur Axelsdóttir et al.", 2015, "Nordic Journal of Psychiatry", "10.3109/08039488.2014.941395", "Systematic Review",
      "Across 13 trials, individual CBT for paediatric OCD was superior to waitlist and placebo therapy but not significantly different from medication or combined treatment; waitlist comparisons may inflate effect estimates.",
      "One-to-one talking therapy helps children with unwanted thoughts and rituals. It works about as well as medicine."),
]

ELICIT["condition::Body Dysmorphic Disorder"] = [
    P("Practitioner Review: Assessment and treatment of body dysmorphic disorder in young people.",
      "G. Krebs, Daniel Rautio, Lorena Fernández de la Cruz, A. Hartmann, A. Jassi, Alexandra Martin et al.", 2024, "Journal of Child Psychology and Psychiatry and Allied Disciplines", "10.1111/jcpp.13984", "Review",
      "The review reports BDD usually develops in the teenage years, affects about 2% of adolescents, and is underdiagnosed; screening is crucial, and CBT with or without SSRIs is the recommended treatment.",
      "Some teenagers worry a lot about a flaw in how they look that others hardly notice. It is often missed. Talking therapy helps."),
    P("The management of body dysmorphic disorder in adolescents: A systematic literature review",
      "Tania Ghosh, Erik Blair", 2025, "Open Health", "10.1515/ohe-2025-0057", "Systematic Review",
      "Reviewing six papers on UK adolescent BDD care, the review found CBT reported as the most effective treatment and called for research into how schools can influence body image and for better professional awareness.",
      "Talking therapy is the main help for teenagers with this worry. Schools may be able to help with body image."),
]

ELICIT["condition::Trichotillomania and Excoriation (skin-picking) Disorder"] = [
    P("Trichotillomania and its treatment: an updated review and recommendations",
      "Megan C DuBois, Bridget Feler, Christopher A. Flessner, Martin E. Franklin", 2025, "Expert Review of Neurotherapeutics", "10.1080/14737175.2025.2557395", "Review",
      "The review reports trichotillomania typically begins in childhood or adolescence, pediatric research is sparse, and habit reversal training is the efficacious treatment; many families struggle to find knowledgeable local providers.",
      "Hair pulling often starts in childhood. Habit reversal therapy helps, but it can be hard to find."),
    P("Trichotillomania in Children − How can a Dermatologist Deal with it?",
      "S. Thakkar, Nimisha D. Desai", 2023, "Indian Journal of Paediatric Dermatology", "10.4103/ijpd.ijpd_104_22", "Review",
      "The review notes trichotillomania in children reflects underlying psychological difficulties, that careful psychological evaluation and empathetic mental health referral are needed, and that habit reversal therapy is the mainstay treatment.",
      "Children who pull out their hair may be struggling inside. Habit reversal therapy is the main help."),
]

del P, _VIS
