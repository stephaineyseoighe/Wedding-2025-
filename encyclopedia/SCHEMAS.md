# Record formats for Parts G, H, I and the Conditions sheet

Each writer produces a Python module in `records/` defining ONE list variable:
`CONDS`, `PRES`, `TOOLS` or `METHODS`. Builders turn records into workbook rows,
adding the headings and the `•` / `▸` bullets themselves. So:

- A "list of bullets" field is a Python list of strings. Each string is one bullet,
  written WITHOUT a leading bullet character. A bullet may contain line breaks.
- Write in the voice of the existing entries. See them with
  `python3 show_existing.py condition ADHD`, `... tool WIAT-III UK`,
  `... method "Solution-focused pupil interview"`, `... band ADHD "School Age"`.
- Validate with `python3 check_records.py records/<file>.py`.

Standard for every field: attributed claims (author, year); no invented figures,
rates, cut-offs, codes or clause content (write "check before quoting"); UK English;
DD/MM/YYYY; APA 7th citations; Irish context (NEPS Continuum of Support —
Classroom Support / School Support / School Support Plus; HSE CDNTs, CAMHS,
Primary Care, Tusla; NCSE; SENO); no real schools, children or case details.
Diagnosis is made by others (CAMHS, CDNT, paediatrics, psychiatry, SLT, OT); the
EP describes, formulates, recommends and refers — keep within PSI 2.2.2.

---

## CONDS — one diagnosed condition (Part I row + Conditions sheet blocks)

```python
CONDS = [{
 "name": "Developmental Language Disorder (DLD)",   # as shown in both sheets
 "code": "DSM-5-TR Language Disorder · ICD-11 6A01.2",  # check codes; if unsure say "ICD-11 code — check"
 "neps": "1. LEARNING (1.2 Language skills)",        # NEPS referral category and area
 "coru": "3.1 · 3.2 · 5.28 · 5.29 · 5.30 · 5.31 · 5.32",
 "psi":  "2.2.2 · 2.3.1 · 1.3.1 · 1.2.8",
 "law":  "Children First Act 2015 · EPSEN Act 2004 · Equal Status Acts 2000–2018 · GDPR",

 # Part I columns (each list: 4–8 bullets; each bullet 1–4 sentences)
 "what_it_is": [...],        # M  1 · What it actually is
 "what_it_is_not": [...],    # N  2 · the misconceptions, each corrected with evidence
 "prevalence": [...],        # O  3 · OVERALL / IRELAND / SEX RATIO etc. — attributed or "check"
 "cooccurring": [            # P  4 · also becomes the Conditions CO-OCCURRING rows (4–8 items)
     {"name": "SPECIFIC LEARNING DIFFICULTY", "rate": "elevated — rate not stated here, check", "presents": "..."},
 ],
 "recommendations": [...],   # Q  5 · what you actually write; name the Continuum level; REFER line; DO NOT line
 "explain_parent": [...],    # R  6 · quoted sentences you would say, plus SIGNPOST
 "explain_teacher": [...],   # S  7
 "explain_child": [...],     # T  8 · YOUNGER / OLDER versions, questions to ask
 "analogies": [...],         # U  9 · NAME: 'analogy' + who it works with
 "language": [...],          # V  10 · accepted terms, community preference, what to avoid
 "red_flags": [...],         # X  12 · RED FLAG — ... / BOUNDARY — ... / WATCH — ...
 "child_voice": [...],       # Y  13 · resources/methods for the child's voice — and why
 "questions": [...],         # Z  14 · Q: '...' A: '...'  (at least 5)
 "supervision": [...],       # AA 15 · what to bring to supervision
 "reflection": [...],        # AB 16 · ON ... — prompts; plus WHAT GOOD LOOKS LIKE / WHAT POOR LOOKS LIKE
 "citations": [...],         # AC 17 · full APA 7th references (4–10)

 # Conditions sheet only
 "pathway": {                # col 4
     "age": "typical age of identification, and why then",
     "who_diagnoses": "Ireland: ...",
     "who_wrote_report": "who could have written the report in front of you",
     "refer_to": "who you refer to",
     "sooner": "'Should we have come sooner?' — what you say",
 },
 "differential": [...],      # col 7 · WHAT ELSE COULD IT BE (co-occurring list is appended automatically)
 "next": [...],              # col 13 · WHAT TO DO NEXT (3–5 bullets)
 "presentations": [...],     # symptom-only presentations related to it (names, 4–10), for the PRESENTATION row

 # One entry for each of the five UCD Table 3 bands — keys exactly as below
 "bands": {
   "Early Years":     {"applies": "YES — ...", "prevalence": "...", "see": "...", "tools": ["ASQ-3 ..."]},
   "School Age":      {...},
   "Adolescent":      {...},
   "Young Adult":     {...},
   "Special Setting": {...},
 },
}]
```

- `applies`: begins YES / RARELY / N/A / RETROSPECTIVE ONLY, then a short reason.
- `prevalence`: one line for this band. `see`: 2–4 sentences on what it looks like at this band.
- `tools`: names from `src/tool_catalogue.json` (exact keys) valid at that band; `[]` if none.
  A tool not in the catalogue may be given as `"Name — AGE x · MEASURES: … · CANNOT TELL YOU: … · TIME: …"`.
- Part I column W ("what you see at each age") is built from the five `see` lines.

## PRES — one descriptive (non-diagnostic) presentation (Part I row, lighter)

```python
PRES = [{
 "name": "Working memory difficulty",
 "neps": "1. LEARNING (1.1 Attention, concentration and work skills)",
 "related_to": ["ADHD", "DLD", "Dyslexia"],      # diagnoses it often sits beside
 "what_it_is": [...], "what_it_is_not": [...],   # 3–5 bullets each
 "by_age": [...],             # how it shows at each band (3–5 bullets)
 "assess": [...],             # what you do to describe it (3–5)
 "recommendations": [...],    # what you write (4–6), with Continuum level
 "explain_parent": [...], "explain_teacher": [...], "explain_child": [...],   # 2–4 each
 "red_flags": [...],          # 2–4
 "questions": [...],          # 3–5 Q/A
 "supervision": [...],        # 2–4
 "citations": [...],          # 2–5 APA
}]
```

## TOOLS — one Part G tool (six teaching rows)

```python
TOOLS = [{
 "name": "WISC-V UK",
 "before":    [...],   # 3–5 points · 1 · Before you open the kit
 "administer":[...],   # 3–5 · 2 · Administering it
 "score":     [...],   # 2–5 · 3 · Scoring it
 "interpret": [...],   # 3–5 · 4 · Interpreting it
 "errors":    [...],   # 4–5 one-line errors that cost marks
 "read":      [...],   # 2–4 readings (manual first, then APA sources)
}]
```
Each point is one cell (one column); 1–4 sentences. No norms, cut-offs or
reliability figures unless you are certain and attribute them; otherwise "check the manual".

## METHODS — one Part H method (one wide row)

```python
METHODS = [{
 "name": "Classroom observation",
 "competencies": "Competency 1 Assessment · Competency 2 Formulation",
 "coru": "3.1 · 3.2 · 5.28 ...", "psi": "1.2.8 · 2.3.1 ...",
 "history": str, "evidence": str, "when_why": str, "need_before": str,
 "how": str,                      # step by step: STEP 1 — ... STEP 2 — ...
 "early_years": str, "school_age": str, "adolescent": str,
 "worked_example": str,           # with a short script
 "theory": str, "frameworks": str, "risk": str, "learn": str,
 "questions": str,                # Q/A
 "why_this": str, "next": str, "supervision": str, "reflection": str, "timeline": str,
 "citations": [...],              # 4–8 full APA references
}]
```
Each string field 500–1500 characters, paragraphs separated by blank lines.
