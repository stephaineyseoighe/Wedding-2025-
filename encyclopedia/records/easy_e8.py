# Easy Read versions: tools, methods and referral areas.
# Keys are "<kind>::<name>" from src/entries.json.


def _build(headings, parts):
    out = []
    for h, bullets in zip(headings, parts):
        out.append(h)
        out.extend("• " + b for b in bullets)
    return "\n".join(out)


def tool(what, tells, cannot, words):
    return _build(["WHAT IT IS", "WHAT IT TELLS US", "WHAT IT CANNOT TELL US", "WORDS TO KNOW"],
                  [what, tells, cannot, words])


def method(what, why, how, words):
    return _build(["WHAT IT IS", "WHY WE DO IT", "HOW IT WORKS", "WORDS TO KNOW"],
                  [what, why, how, words])


def area(means, looks, do, words):
    return _build(["WHAT IT MEANS", "WHAT IT LOOKS LIKE", "WHAT YOU DO", "WORDS TO KNOW"],
                  [means, looks, do, words])


EASY = {}

# ---------------------------------------------------------------- TOOLS

EASY["tool::WIAT-III UK"] = tool(
    ["It is a test of reading, spelling, writing and maths.",
     "It has many parts. You only use the parts you need.",
     "It is for people aged 4 to 25."],
    ["It shows how a child reads, spells and writes compared with others their age.",
     "It is most useful next to a thinking test, such as the WISC-V.",
     "It can show if a child is slow, makes mistakes, or does not understand what they read."],
    ["It cannot say a child has a disorder on its own.",
     "You need to know what the child has been taught first.",
     "Check sight and hearing first. Problems there can give a wrong picture."],
    ["WIAT-III UK: Wechsler Individual Achievement Test, third edition, UK version.",
     "WISC-V: a test of thinking skills for children.",
     "Disorder: a long-lasting difficulty that has a name."])

EASY["tool::SRS-2"] = tool(
    ["It is a form that a parent or teacher fills in.",
     "It asks about how a child mixes and talks with other people.",
     "There are different forms for different ages. You must use the right one."],
    ["It shows how strong the social difficulties seem to be.",
     "Parent and teacher answers often differ. That tells you something too.",
     "A high score is a reason to send the child for more checks."],
    ["It cannot say if a child is autistic. It is not a diagnosis.",
     "Worry, attention difficulties and language difficulties can also give high scores.",
     "A normal score does not end the question. Some girls and some children hide their difficulties."],
    ["SRS-2: Social Responsiveness Scale, second edition.",
     "Diagnosis: when a trained professional names a condition.",
     "Autistic: a different way of thinking, sensing and connecting with people."])

EASY["tool::DASH"] = tool(
    ["It is a test of how fast a person writes by hand.",
     "It is for ages 9 to 25. There are two versions.",
     "The person does five short writing tasks. Each one is timed."],
    ["It shows how many words the person writes each minute.",
     "It shows if the person can speed up when asked to, or not.",
     "Slow writing can stop a pupil showing what they know."],
    ["It does not measure how neat the writing is.",
     "It cannot tell on its own why writing is slow.",
     "A score alone does not get extra help in State exams. Trying a laptop is useful evidence too."],
    ["DASH: Detailed Assessment of Speed of Handwriting.",
     "OT: occupational therapist. They help with movement and daily tasks.",
     "RACE: Reasonable Accommodations at the Certificate Examinations. This is extra help in State exams."])

EASY["tool::ABAS-3"] = tool(
    ["It is a form about everyday skills.",
     "Parents, teachers or the person fill it in.",
     "It asks what the person really does each day, not what they can do if asked."],
    ["It shows skills in three areas. These are thinking, getting on with people, and practical tasks.",
     "It helps plan for the future, such as leaving school.",
     "Home and school answers often differ. That is useful to know."],
    ["It is not a measure of how clever someone is.",
     "On its own it cannot show an intellectual disability. A thinking test is needed too.",
     "Scores may look low if adults do tasks for the person."],
    ["ABAS-3: Adaptive Behavior Assessment System, third edition.",
     "Adaptive behaviour: the everyday skills a person uses to look after themselves and get on in life.",
     "Intellectual disability: finding learning and everyday skills harder than most people do.",
     "SNA: special needs assistant in school."])

EASY["tool::DCD-Q"] = tool(
    ["It is a short form a parent fills in.",
     "It asks about a child's movement compared with other children.",
     "It is for ages 5 to 15."],
    ["It shows if movement difficulties are likely.",
     "Talking with the parent about daily life often tells you more than the score.",
     "A high score means you should send the child to an occupational therapist."],
    ["It cannot say a child has developmental coordination disorder.",
     "Only an occupational therapist or the children's disability team can say that.",
     "It works best with a movement test, such as the Movement ABC-2."],
    ["DCD-Q: Developmental Coordination Disorder Questionnaire.",
     "DCD: developmental coordination disorder. This means real, lasting difficulty with movement and coordination.",
     "Movement ABC-2: Movement Assessment Battery for Children, a test of movement.",
     "OT: occupational therapist. CDNT: Children's Disability Network Team.",
     "ADHD and DLD: attention and language conditions that often happen with DCD."])

EASY["tool::Movement ABC-2"] = tool(
    ["It is a test of how a child moves.",
     "The child does tasks with their hands, with a ball, and to test balance.",
     "There are three age groups. Each group has its own tasks."],
    ["It shows which kinds of movement are hard or easy for the child.",
     "The tester also notes effort, stance and feelings.",
     "It helps school plan for sport, handwriting, lunch and play."],
    ["It cannot say a child has a coordination disorder.",
     "An occupational therapist makes that decision.",
     "Other difficulties may also be part of the picture."],
    ["Movement ABC-2: Movement Assessment Battery for Children, second edition.",
     "OT: occupational therapist.",
     "DCD: developmental coordination disorder. Lasting difficulty with movement."])

EASY["tool::WISC-V UK"] = tool(
    ["It is a test of thinking skills for children aged 6 to 16.",
     "The tester must follow the rules and words in the book exactly.",
     "First ask if you need this test at all. Sometimes other ways answer the question better."],
    ["It compares the child with children the same age.",
     "It also shows what is easier or harder for this child.",
     "Scores are shown as a range, not one exact number."],
    ["It cannot say if a child has ADHD, autism, dyslexia or intellectual disability.",
     "Patterns in the scores are only ideas to check with other evidence.",
     "For a child new to English, low word scores may show less time with English, not less ability."],
    ["WISC-V UK: Wechsler Intelligence Scale for Children, fifth edition, UK version.",
     "ADHD: attention deficit hyperactivity disorder.",
     "Dyslexia: lasting difficulty with reading and spelling words.",
     "Intellectual disability: finding learning and everyday skills harder than most people do."])

EASY["tool::Griffiths III"] = tool(
    ["It is a test of how young children are developing, from birth to age 6.",
     "Only people with special training may use it.",
     "In Ireland, children's disability teams mostly use it. Educational psychologists mostly read the reports."],
    ["It looks at five areas. These include learning, language, hand skills, feelings and big movements.",
     "It helps plan for preschool and starting school.",
     "The pattern across areas matters more than one total score."],
    ["It is not a thinking test and it does not name a condition.",
     "A low score at age 3 does not mean an intellectual disability.",
     "An old report may not describe the child now. Ask what has changed."],
    ["CDNT: Children's Disability Network Team.",
     "NEPS: National Educational Psychological Service.",
     "AIM: Access and Inclusion Model. This is support for children in preschool.",
     "SLT: speech and language therapist.",
     "OT: occupational therapist."])

EASY["tool::Ages & Stages Questionnaires (ASQ-3)"] = tool(
    ["It is a set of questions a parent fills in about their young child.",
     "It is for children from 1 month to about 5 and a half years.",
     "It is a quick check, called a screen. It is not a full test."],
    ["It looks at talking, movement, hand skills, problem solving and getting on with people.",
     "It shows if a child may need more checks.",
     "Parent worries in the last section are very important. Always follow them up."],
    ["A low result does not prove a delay. It means send the child for more checks.",
     "A good result does not end a worry. Screens can miss children.",
     "Being born early, illness or learning two languages can lower scores."],
    ["ASQ-3: Ages and Stages Questionnaires, third edition.",
     "Screen: a quick check to see who might need more help.",
     "GP: family doctor. PHN: public health nurse.",
     "CDNT: Children's Disability Network Team."])

EASY["tool::Bayley-4"] = tool(
    ["It is a test of how babies and toddlers are developing.",
     "It is for children from a few weeks old to three and a half years.",
     "Trainee educational psychologists rarely use it. They usually read the reports."],
    ["It looks at thinking, language and movement.",
     "Parents also answer questions on feelings and everyday skills.",
     "The pattern shows which kind of help may be needed."],
    ["It shows development now. It does not predict the future well.",
     "It cannot show intelligence or intellectual disability.",
     "Check if the child was born early and if the scores allow for that."],
    ["Bayley-4: Bayley Scales of Infant and Toddler Development, fourth edition.",
     "CDNT: Children's Disability Network Team.",
     "SLT: speech and language therapist. OT: occupational therapist.",
     "AIM: Access and Inclusion Model. This is support in preschool."])

EASY["tool::WPPSI-IV UK"] = tool(
    ["It is a test of thinking skills for young children, aged 2 and a half to 7.",
     "It has easier tasks and more toys and pictures than the test for older children.",
     "First ask if a test is needed. Often talking with staff is enough."],
    ["It gives a picture of a young child's thinking now.",
     "Notes on how the child behaved often matter more than the scores.",
     "It can help with big decisions, such as a school place."],
    ["Scores at this age can change a lot over time.",
     "Differences between parts of the test are not reliable yet.",
     "For a child new to English, low word scores show less time with English."],
    ["WPPSI-IV UK: Wechsler Preschool and Primary Scale of Intelligence, fourth edition, UK version.",
     "WISC-V UK: the thinking test for older children.",
     "NEPS: National Educational Psychological Service.",
     "CDNT: Children's Disability Network Team."])

EASY["tool::CELF-5 UK"] = tool(
    ["It is a language test for ages 5 to 21.",
     "Speech and language therapists usually use it.",
     "Educational psychologists mostly read the reports and watch the child in class."],
    ["It shows how well a child understands language.",
     "It shows how well a child uses language to speak.",
     "Low language can also explain low word scores on thinking tests."],
    ["It does not show how a child uses language with people in real life.",
     "The score alone does not say a child has a language disorder.",
     "Check hearing first."],
    ["CELF-5 UK: Clinical Evaluation of Language Fundamentals, fifth edition, UK version.",
     "SLT: speech and language therapist.",
     "DLD: developmental language disorder. This is a lasting difficulty with learning language.",
     "Educational psychologist: a psychologist who helps with learning and school."])

EASY["tool::BPVS-3"] = tool(
    ["It is a quick test of which words a child understands.",
     "The child hears a word and points to one of four pictures.",
     "It is for ages 3 to 16. The child does not need to speak."],
    ["It shows if a child knows fewer English words than others their age.",
     "Knowing fewer words can explain trouble understanding what they read."],
    ["It does not show why the child knows fewer words.",
     "It is not a test of intelligence or of all language.",
     "For a child new to English, a low score shows less time with English, not a difficulty.",
     "An average score does not rule out a language difficulty."],
    ["BPVS-3: British Picture Vocabulary Scale, third edition.",
     "DLD: developmental language disorder.",
     "SLT: speech and language therapist.",
     "Intelligence: how well a person learns, thinks and solves problems."])

EASY["tool::Conners-4"] = tool(
    ["It is a set of forms about attention, activity and behaviour.",
     "Parents and teachers fill it in. Young people aged 8 or more can fill in their own.",
     "It is for ages 6 to 18. A different form is used for younger children."],
    ["It shows how people see the child's attention and activity at home and school.",
     "Parents and teachers often see the child differently. That is useful to know.",
     "Some questions ask about safety. Always read these."],
    ["It cannot say a child has ADHD.",
     "Only doctors or mental health teams make that decision.",
     "Worry, hard life events, language and sleep problems can also raise scores.",
     "Do not give advice on medicine."],
    ["Conners-4: Conners fourth edition.",
     "ADHD: attention deficit hyperactivity disorder.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "GP: family doctor."])

EASY["tool::BRIEF-2"] = tool(
    ["It is a set of forms about everyday self-control and organising.",
     "Parents, teachers and older pupils fill it in.",
     "It is for ages 5 to 18."],
    ["It shows how planning, focus, feelings and self-control look in daily life.",
     "Its best use is planning help, such as breaking tasks into steps.",
     "Home, school and the young person may see things differently."],
    ["It does not measure how the child does on a task test.",
     "It cannot say a child has ADHD or any other condition.",
     "Check the special questions that show if the answers can be trusted."],
    ["BRIEF-2: Behavior Rating Inventory of Executive Function, second edition.",
     "Executive function: the brain skills for planning, focusing and controlling what you do.",
     "ADHD: attention deficit hyperactivity disorder."])

EASY["tool::SDQ"] = tool(
    ["It is a short set of questions about feelings and behaviour.",
     "Parents and teachers fill it in. Young people aged 11 or more can fill in their own.",
     "It also asks how much the difficulties affect daily life."],
    ["It gives a quick first look at feelings, behaviour, attention and friendships.",
     "It also shows the child's kind and helpful side.",
     "The questions on how much life is affected are very important."],
    ["It cannot name a condition.",
     "It does not replace talking with the child and hearing their view.",
     "If a young person says they are hurting themselves or others, act the same day."],
    ["SDQ: Strengths and Difficulties Questionnaire.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "GP: family doctor.",
     "NEPS: National Educational Psychological Service."])

EASY["tool::RCADS"] = tool(
    ["It is a set of questions about worry and low mood.",
     "Young people aged about 8 to 18 fill it in. Parents have their own form.",
     "Stay in the room while the young person fills it in."],
    ["It shows which kinds of worry or sadness are strongest.",
     "It shows how strong the feelings seem to be.",
     "It can show if the young person needs more help."],
    ["It cannot name a condition. It is a quick check.",
     "Read the answers before the young person leaves. Some questions are about safety.",
     "If there is a worry about harm, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own."],
    ["RCADS: Revised Child Anxiety and Depression Scale.",
     "Tusla: the child and family agency in Ireland.",
     "Safeguarding person: the person in school who deals with child protection. Also called the DLP, designated liaison person.",
     "Depression: low mood that lasts and affects daily life."])

EASY["tool::BASC-3"] = tool(
    ["It is a large set of forms about behaviour, feelings and school skills.",
     "Parents, teachers and the young person can fill it in.",
     "It is useful when you do not yet know what is causing the behaviour."],
    ["It shows problems and strengths side by side.",
     "It checks if the answers can be trusted.",
     "It shows skills to build on, like social skills and study skills."],
    ["It cannot name a condition, such as ADHD or depression.",
     "It shows a pattern. You still need to work out why.",
     "Some questions are about safety. Check them the same day."],
    ["BASC-3: Behavior Assessment System for Children, third edition.",
     "ADHD: attention deficit hyperactivity disorder.",
     "Depression: low mood that lasts and affects daily life."])

EASY["tool::ADOS-2"] = tool(
    ["It is a planned session of play and talk. A trained person watches how the child talks, plays and connects.",
     "Only people with special training may use it.",
     "In Ireland, specialist teams usually use it."],
    ["It shows what the child did during about one hour.",
     "The notes can help plan support in school, such as picture timetables.",
     "It is one part of a team decision about autism."],
    ["On its own, it cannot show autism or rule it out.",
     "Some children hide their difficulties. Worry or language needs can change the result.",
     "School observations may differ. Talk to the team about this."],
    ["ADOS-2: Autism Diagnostic Observation Schedule, second edition.",
     "Autism: a different way of thinking, sensing and connecting with people.",
     "CDNT: Children's Disability Network Team.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "HSE: Health Service Executive."])

EASY["tool::SCQ (Social Communication Questionnaire)"] = tool(
    ["It is a short yes or no form a parent fills in.",
     "It asks about how a child talks, plays and connects with people.",
     "It is a quick check for children aged 4 and older."],
    ["A high score means the child should have a full assessment.",
     "The answers can help plan support in school now."],
    ["It cannot say a child is autistic.",
     "A low score does not rule out autism. Some children hide their difficulties.",
     "It tells you nothing about school. It only uses parent answers.",
     "Language needs, worry or hearing loss can also raise scores."],
    ["SCQ: Social Communication Questionnaire.",
     "Assessment: a careful look at a person's needs and strengths.",
     "Autistic: a different way of thinking, sensing and connecting with people.",
     "CDNT: Children's Disability Network Team."])

EASY["tool::Vineland-3"] = tool(
    ["It is a way to find out about everyday skills.",
     "It is often an interview with a parent or carer. There are also forms.",
     "It asks what the person usually does, not what they can do."],
    ["It shows skills in talking, daily living and getting on with people.",
     "It helps plan for the future, such as life after school.",
     "Home and school answers often differ. That shows where skills are used."],
    ["On its own, it cannot show an intellectual disability. A thinking test is needed too.",
     "It cannot name a condition.",
     "Scores can look low if adults do tasks for the person. Ask who does the task."],
    ["Vineland-3: Vineland Adaptive Behavior Scales, third edition.",
     "Intellectual disability: finding learning and everyday skills harder than most people do.",
     "SNA: special needs assistant in school."])

EASY["tool::TEA-Ch2"] = tool(
    ["It is a test of attention using game-like tasks.",
     "It is for ages 5 to 15.",
     "The child does it in a quiet room with an adult."],
    ["It shows different kinds of attention.",
     "These include keeping focus, picking out what matters, and switching between rules.",
     "It helps plan help, such as short tasks and movement breaks."],
    ["It cannot say a child has ADHD.",
     "Good scores do not mean the child has no attention difficulty in class.",
     "Worry, tiredness or not understanding the rules can lower scores."],
    ["TEA-Ch2: Test of Everyday Attention for Children, second edition.",
     "ADHD: attention deficit hyperactivity disorder.",
     "Attention: being able to focus on something."])

EASY["tool::Leiter-3"] = tool(
    ["It is a thinking test that uses no spoken words.",
     "The tester shows the child what to do with gestures.",
     "It helps when a child has language, hearing or English difficulties."],
    ["It shows how a child solves puzzles without words.",
     "It also looks at attention and memory.",
     "An average score with weak language can point to a language need."],
    ["It does not show how a child thinks with words.",
     "It is not a full intelligence score.",
     "On its own, it cannot show an intellectual disability."],
    ["Leiter-3: Leiter International Performance Scale, third edition.",
     "Intellectual disability: finding learning and everyday skills harder than most people do.",
     "SLT: speech and language therapist."])

EASY["tool::WNV (Wechsler Non-Verbal)"] = tool(
    ["It is a thinking test that uses pictures and very few words.",
     "It is for ages 4 to 21.",
     "You must write down why you chose it."],
    ["It shows how a child solves problems without much language.",
     "It can help when a child is new to English or has language or hearing needs.",
     "It shows strengths to build on, like learning from pictures."],
    ["It does not show how a child thinks with words.",
     "It is not the child's full intelligence score.",
     "It is not free of culture. Some children know these tasks less well."],
    ["WNV: Wechsler Nonverbal Scale of Ability.",
     "Non-verbal: without words.",
     "Intelligence: how well a person learns, thinks and solves problems."])

EASY["tool::BAS-3"] = tool(
    ["It is a thinking test made in the UK.",
     "It is for ages 3 to 17.",
     "It can suit younger children, or children who find long tests hard."],
    ["It gives an overall thinking score and scores for different areas.",
     "It shows memory and speed of working.",
     "It helps plan help in class, such as short instructions."],
    ["An overall score can hide big differences between areas.",
     "Its quick reading and maths tasks are not a full check.",
     "Its scores are based on UK children, not Irish children."],
    ["BAS-3: British Ability Scales, third edition.",
     "UK: United Kingdom."])

EASY["tool::Beery VMI"] = tool(
    ["It is a test where the child copies shapes.",
     "The shapes get harder as the test goes on.",
     "Occupational therapists often use it too."],
    ["It shows how well the eyes and hands work together.",
     "This matters for handwriting and copying from the board.",
     "Extra parts can show if the eyes or the hands cause the difficulty."],
    ["On its own, it cannot say if the problem is seeing or moving.",
     "It cannot say a child has a coordination disorder.",
     "Check eyesight and attention first."],
    ["Beery VMI: Beery-Buktenica Developmental Test of Visual-Motor Integration.",
     "OT: occupational therapist.",
     "DCD: developmental coordination disorder. Lasting difficulty with movement."])

EASY["tool::Preschool Language Scales-5 (PLS-5)"] = tool(
    ["It is a language test for young children, from birth to about age 8.",
     "Speech and language therapists usually use it.",
     "Educational psychologists mostly read the reports."],
    ["It shows how well a child understands words.",
     "It shows how well a child uses words to talk.",
     "A child who talks a lot may still not understand well."],
    ["It cannot say a child has a language disorder on its own.",
     "For a child new to English, a low score shows their English, not a disorder.",
     "Check hearing first."],
    ["PLS-5: Preschool Language Scales, fifth edition.",
     "SLT: speech and language therapist.",
     "DLD: developmental language disorder. A lasting difficulty with learning language.",
     "AIM: Access and Inclusion Model. This is support in preschool."])

EASY["tool::Schedule of Growing Skills II"] = tool(
    ["It is a quick check of how a young child is developing.",
     "It is for children up to age 5.",
     "It uses watching, play and what the parent says."],
    ["It shows where the child's skills are in nine areas.",
     "These include movement, hands, seeing, hearing, talking and self-care.",
     "An uneven pattern helps decide who to ask for help."],
    ["It shows where a child is, not why.",
     "It is not a thinking test and it cannot name a condition.",
     "It cannot tell the future. Young children change a lot."],
    ["PHN: public health nurse.",
     "CDNT: Children's Disability Network Team.",
     "SLT: speech and language therapist.",
     "AIM: Access and Inclusion Model. This is support in preschool."])

EASY["tool::Renfrew Action Picture Test"] = tool(
    ["It is a short test where a child talks about pictures.",
     "It takes about 10 minutes.",
     "Speech and language therapists often use it."],
    ["It shows how much information the child gives.",
     "It shows how the child puts sentences together.",
     "It helps teachers plan, such as giving time to answer."],
    ["It does not show how well a child understands language.",
     "One short task is not enough to decide on a language difficulty.",
     "For a child new to English, it does not show their full language ability."],
    ["SLT: speech and language therapist.",
     "Language difficulty: trouble understanding or using words and sentences."])

EASY["tool::YARC (York Assessment of Reading for Comprehension)"] = tool(
    ["It is a reading test. The child reads short stories out loud.",
     "Then the child answers questions about each story.",
     "It is for ages 4 to 16."],
    ["It shows three things. These are how correctly, how fast, and how well the child understands.",
     "It can show if the problem is reading the words or understanding them.",
     "Each pattern needs a different kind of help."],
    ["It does not test sounds in words. Another test is needed for that.",
     "It cannot show a difficulty without knowing what the child has been taught.",
     "If understanding is weak, check spoken language first."],
    ["YARC: York Assessment of Reading for Comprehension.",
     "Comprehension: understanding what you read or hear."])

EASY["tool::Neale Analysis of Reading Ability"] = tool(
    ["It is a reading test. The child reads short stories out loud.",
     "It is for ages 6 to 12.",
     "The tester can read out words the child does not know."],
    ["It shows how correctly and how fast the child reads.",
     "It shows how well the child understands the story.",
     "The kinds of mistakes the child makes are often very useful."],
    ["It does not test spelling or writing.",
     "On its own, it cannot show dyslexia.",
     "Its scores are based on children tested a long time ago. So they are less exact."],
    ["Dyslexia: lasting difficulty with reading and spelling words."])

EASY["tool::Phonological Assessment Battery (PhAB2)"] = tool(
    ["It is a test of how a child hears and works with sounds in words.",
     "It also tests how fast a child can name things.",
     "It is made in the UK. It is for primary school age. An older version covers older pupils."],
    ["It can show if trouble with sounds is making reading hard.",
     "It helps pick the right help, such as sound and phonics teaching or reading practice."],
    ["It does not test understanding of reading or knowing words.",
     "On its own, it cannot confirm dyslexia.",
     "Learning through Irish, or being new to English, can affect scores."],
    ["PhAB2: Phonological Assessment Battery, second edition.",
     "Phonological: to do with the sounds in words.",
     "Dyslexia: lasting difficulty with reading and spelling words.",
     "UK: United Kingdom."])

EASY["tool::CTOPP-2"] = tool(
    ["It is a test of how a child hears and works with sounds in words.",
     "It also tests memory for sounds and how fast a child can name things.",
     "Its scores are based on children in America."],
    ["It can show which sound skills are weak.",
     "It can help explain why reading words is hard."],
    ["On its own, it cannot confirm dyslexia.",
     "It cannot say which help will work best.",
     "Irish children speak and learn differently from American children. The report must say this."],
    ["CTOPP-2: Comprehensive Test of Phonological Processing, second edition.",
     "Phonological: to do with the sounds in words.",
     "Dyslexia: lasting difficulty with reading and spelling words."])

EASY["tool::Sandwell Early Numeracy Test"] = tool(
    ["It is a test of early number skills.",
     "The child uses cards and counters with the tester.",
     "There are two versions: one for ages 4 to 8, and one for ages 8 to 14."],
    ["It shows skills like counting, knowing numbers and number words.",
     "It shows where teaching should start.",
     "Watching how the child gets the answer is very useful."],
    ["It does not test harder maths methods.",
     "It cannot say a child has dyscalculia.",
     "Worry about maths, missed school or language needs can lower scores."],
    ["Numeracy: number and maths skills.",
     "Dyscalculia: lasting difficulty with understanding numbers."])

EASY["tool::Dyscalculia Screener / DysCalculiUM"] = tool(
    ["These are two different quick checks for number difficulty.",
     "One is on a computer for school children.",
     "The other is for older students and adults."],
    ["It shows how quickly a person understands small amounts and numbers.",
     "It shows if more checks are needed."],
    ["It cannot say a person has dyscalculia.",
     "It cannot tell worry apart from difficulty. A worried child can get a low result.",
     "On its own, it cannot get extra help in exams or college."],
    ["Dyscalculia: lasting difficulty with understanding numbers.",
     "Screener: a quick check to see who might need more help."])

EASY["tool::Piers-Harris 3"] = tool(
    ["It is a set of questions a young person answers about themselves.",
     "It asks how they see themselves in different parts of life.",
     "These include school, friends, looks, feelings and behaviour."],
    ["It shows how the young person feels about themselves.",
     "Talking about some answers afterwards is often very useful."],
    ["It does not show if low self-view is the cause or the result. Usually it is the result.",
     "It is not a test of depression or of risk.",
     "If a child talks about harm or abuse, act the same day. Tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own."],
    ["Depression: low mood that lasts and affects daily life.",
     "Tusla: the child and family agency in Ireland.",
     "Safeguarding person: the person in school who deals with child protection. Also called the DLP, designated liaison person."])

EASY["tool::WAIS-IV UK"] = tool(
    ["It is a thinking test for people aged 16 to 90.",
     "It is often used for young adults leaving school.",
     "At 18 or older, the young person gives their own permission."],
    ["It shows skills like reasoning, word knowledge, memory and speed.",
     "It can link slow speed or weak memory to real needs, like timed exams."],
    ["It cannot say how someone will manage a course or a job.",
     "It cannot say a person has ADHD, autism or a learning difficulty.",
     "On its own, it cannot show an intellectual disability."],
    ["WAIS-IV UK: Wechsler Adult Intelligence Scale, fourth edition, UK version.",
     "ADHD: attention deficit hyperactivity disorder.",
     "Intellectual disability: finding learning and everyday skills harder than most people do."])

EASY["tool::WRAT-5"] = tool(
    ["It is a short test of reading words, spelling and maths.",
     "It is for people aged 5 to over 85.",
     "Schools can use it for extra help in State exams. Ask first if the pupil has done it already."],
    ["It gives a quick picture of a person's level.",
     "The kinds of reading mistakes are useful to teachers."],
    ["It does not test reading speed, sounds in words or writing.",
     "It is short, so it gives less information.",
     "On its own, it cannot show dyslexia."],
    ["WRAT-5: Wide Range Achievement Test, fifth edition.",
     "Dyslexia: lasting difficulty with reading and spelling words.",
     "RACE: extra help in State exams."])

EASY["tool::MFQ (Mood and Feelings Questionnaire)"] = tool(
    ["It is a set of questions about low mood over the last two weeks.",
     "Young people about 8 to 18 fill it in. Parents have their own form.",
     "Some questions ask about death and self-harm. Plan what to do first."],
    ["It shows how strong low mood seems to be.",
     "It can show change over time."],
    ["It cannot say a person has depression.",
     "A low score is not proof that all is well.",
     "Read it before the young person leaves. If there is risk, act the same day.",
     "If there is a child protection worry, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own."],
    ["MFQ: Mood and Feelings Questionnaire.",
     "Depression: low mood that lasts and affects daily life.",
     "Tusla: the child and family agency in Ireland.",
     "Safeguarding person: the DLP, designated liaison person, in school."])

EASY["tool::Beck Youth Inventories-2"] = tool(
    ["They are five short sets of questions for young people aged 7 to 18.",
     "They ask about self-view, worry, low mood, anger and behaviour.",
     "Only use the sets you need."],
    ["They show how the young person says they feel.",
     "They can show change over time."],
    ["They cannot name a condition.",
     "Always check answers with parents, teachers and what you see.",
     "Some questions are about safety. Read them before the young person leaves.",
     "If there is harm or abuse, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own."],
    ["Tusla: the child and family agency in Ireland.",
     "Safeguarding person: the DLP, designated liaison person, in school.",
     "CAMHS: Child and Adolescent Mental Health Services."])

EASY["tool::AQ-10 / AQ-50"] = tool(
    ["They are forms people fill in about themselves.",
     "They ask about thinking and social life linked to autism.",
     "They are mainly for adults aged 16 or more. There are also versions for younger people."],
    ["A high score can be a reason to ask for a full assessment.",
     "Talking about some answers afterwards is useful."],
    ["They cannot say a person is autistic.",
     "A low score does not rule out autism. Some people hide their difficulties.",
     "They do not suit people who find reading or thinking about themselves hard.",
     "Worry, low mood and ADHD can also raise scores."],
    ["AQ: Autism-Spectrum Quotient. AQ-10 has 10 questions. AQ-50 has 50.",
     "Autism: a different way of thinking, sensing and connecting with people.",
     "ADHD: attention deficit hyperactivity disorder."])

EASY["tool::Communication Matrix / AAC review"] = tool(
    ["It is a way to map how a person communicates.",
     "It is for people at the earliest stages of communication.",
     "It counts every way, such as sounds, looks, signs, pictures and devices."],
    ["It shows what the person can say and why. For example, to say no or to ask for things.",
     "It shows if adults respond the same way each time.",
     "It helps pick the next thing to teach."],
    ["It is not a test with scores or ages.",
     "Only a speech and language therapist should choose or change the device.",
     "Check the person can say no, stop and hurt. If there is a worry about abuse, tell Tusla (the child and family agency) quickly. Telling the school's safeguarding person is not enough on its own."],
    ["AAC: augmentative and alternative communication. Ways to talk other than speech, like pictures or devices.",
     "SLT: speech and language therapist.",
     "Tusla: the child and family agency in Ireland.",
     "Safeguarding person: the DLP, designated liaison person."])

EASY["tool::Access arrangements evidence (RACE)"] = tool(
    ["It is not a test. It is gathering proof for extra help in State exams.",
     "The school applies. The State Examinations Commission decides.",
     "The rules change each year. Always check the newest rules."],
    ["It shows how the pupil usually works in school.",
     "Trying supports, like a reading pen or laptop, gives good evidence.",
     "A psychologist's report is not needed to apply."],
    ["No one can promise a pupil will get extra help.",
     "A report does not decide who gets help.",
     "Families can appeal a decision. There are strict dates."],
    ["RACE: Reasonable Accommodations at the Certificate Examinations.",
     "SEC: State Examinations Commission.",
     "Accommodation: a change that makes an exam fair, like a reader or extra time."])

# ---------------------------------------------------------------- METHODS

EASY["method::Structured play observation"] = method(
    ["You watch a young child play, in a planned way.",
     "You write down what the child does in a set way.",
     "It is not a test. It has no scores to compare with other children."],
    ["It shows the child in their real setting, like preschool.",
     "It is useful for children under 5, or children with little language.",
     "It shows how a child joins in, plays and gets on with others."],
    ["Write down what you will look for before you start.",
     "Watch for about 20 to 30 minutes. Also watch another child in the same room.",
     "Use it with what parents and staff tell you. It is not enough on its own.",
     "If there is a safety worry, stop and follow the child protection steps."],
    ["Observation: carefully watching and writing down what happens.",
     "Assessment: a careful look at a person's needs and strengths."])

EASY["method::Parent developmental history interview"] = method(
    ["It is a talk with a parent about their child's life so far.",
     "You ask about birth, early skills, health, school and family.",
     "It takes about an hour."],
    ["It shows which difficulty came first. This helps you understand the child.",
     "Parents often have good ideas about what is going on.",
     "It is needed at the start of most assessments."],
    ["Ask the parent to bring the child's health book and old reports.",
     "Start by asking what the child is like. Then ask about when worries began.",
     "Always ask about hearing when the child was small.",
     "If the talk moves to trauma, stop. Be careful if there is a child protection worry."],
    ["Developmental history: the story of how a child has grown and learned.",
     "Trauma: harm from very frightening or upsetting events.",
     "PHN: public health nurse."])

EASY["method::Classroom observation"] = method(
    ["You watch a pupil in class in a planned way.",
     "You write down what happens in a set way.",
     "It is not a test with scores."],
    ["It shows the pupil in the real place where help must work.",
     "It also shows the classroom, like seating, tasks and adult help.",
     "It gives a starting point to check if help works later."],
    ["Agree one clear question with the teacher first.",
     "Write down exactly what behaviour you will count.",
     "Watch another typical pupil too, to compare.",
     "One visit is not enough to know what is usual. Watch more than once if you can."],
    ["Observation: carefully watching and writing down what happens.",
     "Behaviour: what a person does or says."])

EASY["method::ABC functional analysis"] = method(
    ["It is a way to understand why a behaviour keeps happening.",
     "You write down what happened before, the behaviour, and what happened after.",
     "A is before. B is the behaviour. C is what came after."],
    ["Behaviour often gets the child something, or helps them avoid something.",
     "Help that does not fit the reason can make behaviour worse.",
     "It helps you find a better way for the child to meet the same need."],
    ["Pick one behaviour and describe it clearly.",
     "Talk with the teacher. Staff write down each time it happens for about a week.",
     "Say the reason is likely, not certain.",
     "If behaviour may show upset, harm or abuse, keep the child safe first."],
    ["ABC: antecedent, behaviour, consequence. Antecedent means what happens before.",
     "Consequence: what happens after.",
     "Function: the reason or need behind a behaviour.",
     "SNA: special needs assistant."])

EASY["method::Report writing"] = method(
    ["It is writing down what you found after working with a child.",
     "Parents, teachers and other professionals will read it, sometimes years later."],
    ["It answers the question that was asked.",
     "It helps people plan the right support.",
     "The rules say reports must be clear, accurate and suit the reader."],
    ["Use plain words and short sentences.",
     "Check all scores and names twice.",
     "Include the child's own words.",
     "Do not name a condition you cannot diagnose. Child protection information goes a different way, not in the report."],
    ["Diagnose: when a trained professional names a condition.",
     "CORU: the body that registers health and social care professionals in Ireland.",
     "Formulation: a shared explanation of why things are happening for the child."])

EASY["method::Graduated return (EBSA)"] = method(
    ["It is a plan to help a pupil come back to school step by step.",
     "It is for pupils who have missed lots of school because of worry or upset."],
    ["Staying home eases the worry for now. But it makes the next day harder.",
     "Small steps the pupil can manage help break this cycle.",
     "Waiting for the pupil to feel ready often makes it harder."],
    ["Hear the parent, the pupil and the teacher separately.",
     "Choose a trusted adult in school with the pupil.",
     "Check health and safety first, including self-harm and child protection.",
     "The principal must tell TESS when a child misses 20 school days or more in a school year."],
    ["EBSA: emotionally based school avoidance. Missing school because of worry or upset.",
     "TESS: Tusla Education Support Service. It helps with school attendance.",
     "Tusla: the child and family agency in Ireland.",
     "NEPS: National Educational Psychological Service."])

EASY["method::Solution-focused pupil interview"] = method(
    ["It is a short talk with a pupil about what is going well and what they hope for.",
     "It looks at solutions, not at problems.",
     "It takes about 20 to 30 minutes."],
    ["It puts the pupil's own view into the plan.",
     "It gives goals the school can act on.",
     "Research says it is a reasonable way to help. It is not a proven treatment."],
    ["Explain first what stays private, and when you must tell someone.",
     "Ask about times things went a bit better. Ask how they did that.",
     "Use a line from 0 to 10. Ask what one step up would look like.",
     "If there is a safety worry or trauma, stop and follow the right steps."],
    ["Solution-focused: looking at what works and what you want, not only at the problem.",
     "Trauma: harm from very frightening or upsetting events."])

EASY["method::Parent feedback session"] = method(
    ["It is a meeting where you tell parents what you found.",
     "You talk together about what it means and what to do next."],
    ["Parents have a right to understand the results in plain words.",
     "Parents carry out plans at home and speak up for their child for years.",
     "A parent who feels confused or judged may pull away from the school."],
    ["First ask what the parent hopes to hear and what worries them most.",
     "Describe the child in plain words before any numbers.",
     "Share a real strength. Ask the parent to say the plan in their own words.",
     "If a child protection worry comes up, follow those steps first. Book an interpreter. Never use a family member or a child."],
    ["Feedback: telling someone what you found.",
     "Assessment: a careful look at a person's needs and strengths."])

EASY["method::Group intervention"] = method(
    ["It is help given to a small group of children together.",
     "The children share the same need, like worry or making friends."],
    ["It reaches more children at once.",
     "Children learn they are not the only ones who feel this way.",
     "A school staff member learns to run the group after you."],
    ["Agree the need with the school first. Pick a programme with good evidence.",
     "Choose group members with care. Some children may do worse in a group.",
     "Get parent permission. Plan what to do if a child tells you something worrying.",
     "Check progress before and after."],
    ["Intervention: planned help to make things better.",
     "Evidence: facts from research that show something works."])

EASY["method::Transition planning"] = method(
    ["It is planning for a big move. For example, starting school, moving to secondary school, or leaving school.",
     "It links the old setting and the new one."],
    ["Support in one place does not move by itself to the next place.",
     "Worry and school avoidance often grow around big moves.",
     "Planning late is a common problem."],
    ["Start about a year before the move.",
     "Get permission to share reports with the new setting.",
     "Map what support there is now and what there will be next.",
     "Ask the child what they know, fear and hope."],
    ["Transition: moving from one stage or place to another.",
     "Setting: a place like a preschool, school or college."])

EASY["method::Staff training"] = method(
    ["It is teaching school staff new skills or ideas.",
     "It reaches children through the adults who see them every day."],
    ["It can help more children than working with one child at a time.",
     "It can build what the school can do by itself."],
    ["Ask staff what they need first.",
     "Agree what staff will do differently afterwards.",
     "One session alone rarely changes practice. Follow up after some weeks.",
     "Never use a real child that someone could recognise."],
    ["Training: teaching people how to do something.",
     "Practice: the way people usually do their work."])

EASY["method::Teacher consultation"] = method(
    ["It is a planned talk with a teacher about a pupil.",
     "You work out together what is going on and what might help.",
     "The teacher can choose to take the advice or not."],
    ["Teachers know the child and what has been tried.",
     "It helps more children through the adults who see them each day.",
     "Agreeing the problem clearly helps plans work."],
    ["Agree a clear question together.",
     "Write down who will do what, and by when.",
     "Set a date to check how it went.",
     "Safety worries are never just talked over. Follow the child protection steps."],
    ["Consultation: talking together to solve a problem.",
     "Pupil: a child or young person at school."])

# ---------------------------------------------------------------- REFERRAL AREAS

EASY["area::1.1 Attention, concentration and work skills"] = area(
    ["This is about focus, staying on task and getting work done.",
     "Some children have ADHD. Many have no diagnosis at all."],
    ["Finding it hard to plan, start, or keep track of work.",
     "Slow work, lost books, or homework not done.",
     "Focusing better one-to-one than in a big class."],
    ["Watch the child in class and compare with another child.",
     "Use forms from parents and teachers, and tests of memory and attention.",
     "Under 5, describe what you see. Do not score it.",
     "Look at family, school, health and feelings too. Refer to CAMHS, the GP or Primary Care when needed."],
    ["ADHD: attention deficit hyperactivity disorder.",
     "Diagnosis: when a trained professional names a condition.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "GP: family doctor."])

EASY["area::1.2 Language skills"] = area(
    ["This is about understanding and using spoken language.",
     "It includes language disorders, stammering and not speaking in some places."],
    ["Finding it hard to follow instructions with many steps.",
     "Trouble finding words or telling a story in order.",
     "Learning English as a new language is not a disorder. But it can look like one."],
    ["Always find out what languages the child hears at home first.",
     "Use word tests, watch the child in class, and read speech and language reports.",
     "Work with the speech and language therapist. Book an interpreter if needed."],
    ["SLT: speech and language therapist.",
     "DLD: developmental language disorder. A lasting difficulty with learning language.",
     "AAC: ways to communicate other than speech, like pictures or devices.",
     "NEPS: National Educational Psychological Service."])

EASY["area::1.6 Co-ordination — fine motor / handwriting, gross motor / PE skills"] = area(
    ["This is about movement. It includes hand skills like writing, and big movements like sport.",
     "It includes coordination difficulties, tics and sensory needs."],
    ["Messy or slow handwriting, or a hard pencil grip.",
     "Trouble with balance, ball games or getting dressed.",
     "Being very bothered by, or not noticing, noise or touch."],
    ["Use movement and handwriting tests and parent forms.",
     "Watch how the child sits and holds a pencil.",
     "An occupational therapist usually makes the diagnosis. Refer to them.",
     "Think about laptops or other help for exams."],
    ["OT: occupational therapist. They help with movement and daily tasks.",
     "CDNT: Children's Disability Network Team.",
     "Tics: sudden movements or sounds a person cannot easily stop.",
     "Diagnosis: when a trained professional names a condition."])

EASY["area::2.1 Behaviour in class"] = area(
    ["This is about behaviour in the classroom that worries staff.",
     "Some children have a diagnosis. Most do not."],
    ["Behaviour that challenges, or big feelings that are hard to calm.",
     "Trouble moving between tasks or classes.",
     "Behaviour can be a sign that a learning need has not been met. Always check this."],
    ["Write down what happens before and after the behaviour for a week.",
     "Watch the child in class. Use forms from parents and teachers.",
     "In young children, most behaviour is part of growing up.",
     "Check if the class or school system is working for this pupil."],
    ["ABC: antecedent, behaviour, consequence. What happens before, the behaviour, and after.",
     "Diagnosis: when a trained professional names a condition.",
     "CAMHS: Child and Adolescent Mental Health Services."])

EASY["area::2.2 Behaviour during break times and around the school"] = area(
    ["This is about behaviour in the yard, corridors and free time.",
     "It can include risk-taking, harmful behaviour, or problems with drugs or gaming."],
    ["Behaviour that is worse when there is less structure.",
     "Friends or groups pulling a child into trouble.",
     "Sexual or harmful behaviour in children. This needs care and the right service."],
    ["Watch the child in the yard. Compare yard and classroom. The difference matters.",
     "Talk with older pupils and read school records.",
     "Checking for drug use is not the psychologist's job. Refer on.",
     "Where there is a child safety worry, refer to Tusla."],
    ["Tusla: the child and family agency in Ireland.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "NEPS: National Educational Psychological Service."])

EASY["area::5.4 Concerns about early development"] = area(
    ["This is about worries in babies and young children, up to about age 6.",
     "There are no diagnoses here. It describes what is happening."],
    ["A child reaching early steps later than expected, like walking or talking.",
     "Early bonding between parent and baby.",
     "Support in preschool, and starting primary school."],
    ["Talk with parents about the child's story so far. Read the public health nurse's notes.",
     "At this age the psychologist mostly gives advice. They rarely test.",
     "The children's disability team often leads.",
     "Plan this age group carefully. It is the hardest to cover."],
    ["PHN: public health nurse.",
     "CDNT: Children's Disability Network Team.",
     "AIM: Access and Inclusion Model. Support in preschool.",
     "SENO: special educational needs organiser."])

EASY["area::1.3 Comprehension and general ability"] = area(
    ["This is about how a child understands, thinks and learns overall.",
     "It includes intellectual disability and very high ability."],
    ["Finding schoolwork hard at the current level.",
     "Trouble understanding what adults ask.",
     "Uneven thinking skills, or missed school."],
    ["Use a thinking test that suits the child's age.",
     "Add an everyday skills measure if intellectual disability is a question.",
     "Where a test is hard to access, use picture-based tests.",
     "For older pupils, plan for life after school."],
    ["Intellectual disability: finding learning and everyday skills harder than most people do.",
     "CDNT: Children's Disability Network Team.",
     "NEPS: National Educational Psychological Service."])

EASY["area::1.4 Literacy — reading (fluency / comprehension), writing and spelling"] = area(
    ["This is about reading, writing and spelling.",
     "It includes dyslexia and writing difficulties."],
    ["Slow reading, or avoiding reading aloud.",
     "Spelling that gets in the way of writing.",
     "Slow or messy handwriting when time is short."],
    ["First check what the child has been taught.",
     "Use reading, spelling and writing tests, and school test results.",
     "Do not test young children for dyslexia. Look at early sound and letter skills instead.",
     "Try laptops or other help. Check hearing and vision."],
    ["Dyslexia: lasting difficulty with reading and spelling words.",
     "SLT: speech and language therapist. OT: occupational therapist.",
     "SENO: special educational needs organiser.",
     "NEPS: National Educational Psychological Service."])

EASY["area::1.5 Maths skills — concepts and computation"] = area(
    ["This is about understanding numbers and doing sums.",
     "It includes dyscalculia."],
    ["Trouble remembering number facts.",
     "Worry about maths.",
     "Word problems where reading is the real barrier."],
    ["Use maths tests and look closely at the child's real work.",
     "Keep reading separate from the maths.",
     "With young children, watch counting in play. There is no test.",
     "For older pupils, think about calculators and everyday money and time skills."],
    ["Dyscalculia: lasting difficulty with understanding numbers.",
     "NEPS: National Educational Psychological Service."])

EASY["area::4.1 Friendships and social skills"] = area(
    ["This is about making friends and getting on with others.",
     "It includes autism and social communication difficulties."],
    ["Being alone, or being bullied.",
     "Trouble taking turns, or fixing things after a fall-out.",
     "Some children hide their difficulties. Quiet, lonely children get missed."],
    ["Watch in the yard and in class.",
     "Use parent and teacher forms and talk with the pupil about friends.",
     "Autism assessment is done by a team.",
     "Support the school with plans and policy."],
    ["Autism: a different way of thinking, sensing and connecting with people.",
     "CDNT: Children's Disability Network Team.",
     "SLT: speech and language therapist.",
     "NEPS: National Educational Psychological Service."])

EASY["area::3.1 Confidence and self-esteem"] = area(
    ["This is about how a child feels about themselves.",
     "There are no diagnoses here."],
    ["Giving up easily, or fear of getting things wrong.",
     "Feeling bad about schoolwork but fine in other parts of life.",
     "Low self-esteem can come from a learning difficulty no one has noticed."],
    ["With young children, ask adults. Children this young cannot fill in forms.",
     "With older pupils, use their own answers and talks.",
     "Watch for low mood underneath.",
     "Check which came first: the learning difficulty or the low confidence."],
    ["Self-esteem: how much you value and like yourself.",
     "NEPS: National Educational Psychological Service."])

EASY["area::3.2 Anxiety"] = area(
    ["This is about strong worry or fear.",
     "Some children have an anxiety disorder. Others do not."],
    ["Worry about tests, speaking in class, or changes.",
     "Tummy aches or headaches at school.",
     "Worry caused by a learning need that has not been met.",
     "In young children, upset when a parent leaves."],
    ["Use worry questionnaires and talk with the pupil.",
     "Watch the pupil at the worried moment, not a random time.",
     "Look at school attendance too.",
     "Refer to Primary Care for mild worry, or CAMHS for severe worry. Ask the GP to rule out health causes."],
    ["Anxiety: strong worry or fear.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "GP: family doctor.",
     "EBSA: emotionally based school avoidance."])

EASY["area::3.3 Obsessive-compulsive and related"] = area(
    ["This is about unwanted thoughts and repeated actions that are hard to stop.",
     "It includes hair-pulling and skin-picking."],
    ["Checking work again and again.",
     "Rituals when moving between activities.",
     "Strict routines. These may be linked to autism instead. Check this first."],
    ["Get reports from parents and teachers.",
     "Describe how it affects schoolwork and attendance.",
     "Diagnosis is done by health services, not the educational psychologist.",
     "Routines are normal in young children."],
    ["OCD: obsessive-compulsive disorder.",
     "Ritual: an action done the same way every time.",
     "CAMHS: Child and Adolescent Mental Health Services."])

EASY["area::3.4 Mood"] = area(
    ["This is about low mood and depression.",
     "Low mood can be there without a diagnosis."],
    ["Losing interest in things the child used to enjoy.",
     "Pulling away from friends.",
     "In young people, low mood can look like crossness or refusing."],
    ["Get reports from parents and teachers. Talk with the pupil.",
     "Use a mood questionnaire.",
     "Always check for risk and safety.",
     "Refer to Primary Care for mild low mood, or CAMHS for more serious low mood."],
    ["Depression: low mood that lasts and affects daily life.",
     "Diagnosis: when a trained professional names a condition.",
     "CAMHS: Child and Adolescent Mental Health Services."])

EASY["area::5.1 Vision"] = area(
    ["This is about eyesight and how it affects learning."],
    ["A child who needs glasses but does not have them.",
     "Tired eyes after reading for a long time.",
     "Print that is too small, or a poor seat in the room."],
    ["Check when the child last had an eye test. Do this before any reading test.",
     "Never give sight-based tasks before sight is checked.",
     "Work with the Visiting Teacher service.",
     "Think about seating, print size and exam help."],
    ["Visiting Teacher: a teacher who supports children with sight or hearing needs.",
     "CDNT: Children's Disability Network Team.",
     "GP: family doctor.",
     "NEPS: National Educational Psychological Service."])

EASY["area::5.2 Hearing"] = area(
    ["This is about hearing and how it affects learning.",
     "It includes hearing loss and glue ear."],
    ["Hearing well one-to-one but not in a noisy class.",
     "Glue ear when young can show up later as reading difficulty."],
    ["Always check hearing before deciding about language or reading.",
     "Ask about glue ear in the early school years.",
     "Look at the room's noise and where the child sits.",
     "Refer to audiology. Work with the Visiting Teacher service."],
    ["Glue ear: fluid in the ear that makes hearing muffled.",
     "Audiology: the service that tests hearing.",
     "CDNT: Children's Disability Network Team.",
     "GP: family doctor."])

EASY["area::5.3 Medical condition or other diagnosis"] = area(
    ["This is about health needs that affect school.",
     "Examples are epilepsy, brain injury and some conditions a child is born with.",
     "It also takes in sleep, eating and toilet problems."],
    ["Tiredness and low energy.",
     "Medicine that makes it hard to focus or learn.",
     "Missed lessons from time in hospital, and coming back after being sick."],
    ["Read health reports, with permission.",
     "Your job is the effect on school, not the diagnosis.",
     "Think about help in exams and subject choices.",
     "Work with health teams. For young children, the disability team often leads."],
    ["Diagnosis: when a trained professional names a condition.",
     "CDNT: Children's Disability Network Team.",
     "OT: occupational therapist.",
     "PHN: public health nurse."])

EASY["area::3.5 Trauma, attachment and loss"] = area(
    ["This is about the effects of very upsetting events, loss or early relationships.",
     "It includes grief and trauma. Some children have a diagnosis. Many do not."],
    ["Children affected by hard early life experiences.",
     "Children who have lost someone.",
     "Children who have had to leave their home country."],
    ["Do not interview children about trauma. Do not screen young children for trauma. Refer.",
     "Help the school work in a trauma-informed way.",
     "Talk to your supervisor first.",
     "A stable setting and steady staff can help."],
    ["Trauma: harm from very frightening or upsetting events.",
     "Attachment: the bond between a child and the adults who care for them.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "NEPS: National Educational Psychological Service."])

EASY["area::3.6 School attendance"] = area(
    ["This is about missing school.",
     "There are no diagnoses here."],
    ["Missing school because of worry or upset.",
     "Skipping school is different. It needs a different plan.",
     "Late arrival, part days, illness, or parents keeping the child home."],
    ["Get the real attendance record.",
     "Hear the parent, the pupil and the teacher separately. They often differ.",
     "Make a step-by-step plan to return.",
     "Work with Tusla's education welfare service."],
    ["EBSA: emotionally based school avoidance. Missing school because of worry or upset.",
     "Tusla: the child and family agency in Ireland.",
     "NEPS: National Educational Psychological Service."])

EASY["area::5.6 School and access factors"] = area(
    ["This is about the school, not the child.",
     "It looks at how the class, teaching and school systems work for the pupil."],
    ["A classroom or teaching style that does not suit the pupil.",
     "Help that was planned but never given.",
     "Support like laptops, exam help and special needs assistants."],
    ["Watch the classroom. Look at the setting, not only the child.",
     "Check school support records.",
     "Find where staff need training.",
     "Help change whole-school policy and practice."],
    ["RACE: extra help in State exams.",
     "SNA: special needs assistant.",
     "SENO: special educational needs organiser.",
     "NCSE: National Council for Special Education.",
     "NEPS: National Educational Psychological Service."])

EASY["area::5.5 Involvement of other services"] = area(
    ["This is about working with other services around a child.",
     "It includes serious mental health conditions, child protection and family difficulties."],
    ["Children in care or with family, housing or money problems.",
     "Children who see violence at home.",
     "Many services involved at the same time."],
    ["Read every report before you plan. Do not repeat a test another service has done.",
     "Know which service does what, and what is not your job.",
     "Plan for changes in services at 16 and 18.",
     "Child protection goes to Tusla. Talk to your supervisor."],
    ["Tusla: the child and family agency in Ireland.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "NEPS: National Educational Psychological Service."])

EASY["area::4.2 Relationships with adults"] = area(
    ["This is about how a child gets on with adults in school.",
     "It includes trust, speaking up, and identity."],
    ["How the pupil responds to being corrected.",
     "Relying a lot on one adult, such as the special needs assistant.",
     "Getting on well with some teachers but not others. That difference is useful to know."],
    ["Watch the pupil with different adults.",
     "Ask the pupil which adults help them.",
     "Help older pupils learn to speak up for themselves.",
     "Respect gender, cultural and language identity."],
    ["SNA: special needs assistant.",
     "LGBTQ+: lesbian, gay, bisexual, transgender, queer and other identities.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "CDNT: Children's Disability Network Team."])

EASY["area::3.7 Risk and safeguarding"] = area(
    ["This is about keeping children safe from harm.",
     "It is not something you assess. You act."],
    ["A child tells you about harm, or you see signs of risk.",
     "A worry about abuse or neglect."],
    ["Stop the assessment. Tell your supervisor and the school's safeguarding person the same day.",
     "Tell Tusla (the child and family agency) quickly when the concern meets the level for reporting.",
     "Telling the school's safeguarding person is not enough on its own. You still have your own duty.",
     "Know the crisis steps before you need them."],
    ["Tusla: the child and family agency in Ireland.",
     "Safeguarding person: the DLP, designated liaison person, in the school.",
     "CAMHS: Child and Adolescent Mental Health Services.",
     "Supervisor: the senior psychologist who guides your work."])
