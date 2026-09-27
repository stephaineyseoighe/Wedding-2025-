# The Encyclopedia — handover brief

**For:** Stephainey Seoighe, Year 1 TEP, UCD DEdPsych
**Purpose:** continue building `The_Encyclopedia.xlsx` in Claude Code, where long agentic
sessions can do the writing that a chat turn cannot.

---

## How to start in Claude Code

Put this folder and `The_Encyclopedia.xlsx` in the same directory, open Claude Code there,
and give it this file. Then say:

> Read HANDOVER.md. Continue writing micro-skills into micro.py, working down the
> priority order. Write ten, rebuild, show me the count, then continue.

---

## What the workbook is

An Excel encyclopedia for placement. Eight sheets:

| Sheet | What it holds | State |
|---|---|---|
| **Log** | 400 rows, cascading dropdowns, 84 Roscommon days pre-filled | done |
| **Reference** | Parts A–J. 55 macro skills with full teaching, 230 CORU/PSI standards in full, Interactive Factors prompt, tools by age band, three-year route, methods, conditions, completion map | A–F done, G/H partial |
| **Conditions** | Competency → CORU/PSI → age band → diagnosed condition → co-occurring → symptom-only. 17 columns | 4 of 45 conditions |
| **Skill progression** | 317 micro-skills, five stages of independence across, target dates | **55 of 317 written** |
| **Appendix 4 and 5** | 84 placement days + red learning columns + weekly reflection scaffolds | done |
| Cavan plan, Sources, Start here | — | done |

---

## The standard — read this before writing anything

Everything is written **for a person who must be able to open the file, find the row, and
be the expert in the room**, with no other source. That means:

- **No templating.** An earlier version generated the five stage columns from a sentence
  stem with the micro-skill name slotted in. It was rejected, correctly. Median cell was
  112 characters. Written properly it is ~300.
- **Bullets and arrows, never blocks of prose.** Read on a tablet.
- **Every claim attributed.** Not "Vygotsky said children are a head taller in play" but
  "Vygotsky (lecture 1933; in English, Mind in Society, 1978, p.102)".
- **Say what you do not know.** "Rate not stated in source — check before quoting" is
  correct. Inventing a figure is not.
- **UK English, DD/MM/YYYY, APA 7th.**

---

## The micro-skill format — copy this exactly

In `micro.py`, keyed `(macro skill name, micro-skill name)`:

```python
("Macro skill name","Micro-skill name"): {
"why":   "Why this micro-skill matters. 2–4 sentences. Name the consequence of getting it wrong.",
"s1":    "WATCH FOR — what to look at specifically.\n\nWRITE DOWN — what to record.\n\nASK AFTERWARDS — the one question that gets the tacit knowledge.",
"s2":    "YOU TAKE — the part you do.\n\nTHEY HOLD — the part the supervisor keeps.\n\nWHY THAT SPLIT — the reasoning.",
"s3":    "YOU RUN IT — what you do.\n\nWHAT THEY ARE WATCHING FOR — the specific failure mode.\n\nSTEPPING IN LOOKS LIKE — what intervention looks like.",
"s4":    "YOU DO IT ALONE — what that means here.\n\nPASS TEST — [use the pass test from fullstack.json verbatim].\n\nEVIDENCE TO FILE — which appendix, which log tag.\n\nWHAT FAILURE LOOKS LIKE — concrete.",
"s5":    "YOU CAN TEACH IT — what teaching it requires you to explain.\n\nWHEN IT GOES WRONG — what to do.",
"error": "The single error that costs marks. One sentence.",
"feeds": "→ Feeds into [named next micro-skill or competency].",
"evidence":"Appendix X · Log sheet tagged N. Competency"},
```

Source data for names, pass tests and standards: `fullstack.json`.
Structure is `[competency, macro skill, standards string, [blocks]]`, and each block is
`[name, what, how, time, [micro-skills]]`, each micro-skill `[name, pass test, standard]`.

---

## Priority order — work down this

**1. Finish Assessment (29 left)**
- Synthesise findings from multiple sources (6)
- Phonological and literacy measures (7)
- Social communication screening measures (5)
- Behavioural and emotional rating scales (6)
- Adapt standardised procedure and record the adaptation (5)

**2. Ethical Practice (all micro-skills)** — highest risk area, and it covers consent,
child protection, competence boundaries and workload.

**3. Formulation** — named development area.

**4. Intervention** — named development area, and no referral area maps to it.

**5. Working with Others**

**Leave until Year 2:** Systemic Change, Research, Supervision.
Rationale: these are not what Cavan (Oct–Dec 2026) will demand, and a usable file now
beats a complete file in March.

---

## After the micro-skills

**Part I conditions** — 41 left, 17 columns each, five age bands. Format in `conditions.py`
and `cond3.py`. Priority: ADHD is done; next DLD, DCD, anxiety, EBSA, trauma/attachment,
then by caseload. Source material: `2026-04-23_Unsorted_ep_clinical_reference 1.html` in
Google Drive holds 45 profiles by DSM category — re-cut by age band, don't copy.

**Part G tools** — 65 left. Format in `toolteach.py`: before / administer / score /
interpret / errors / read.

**Part H methods** — 9 more. Format in `methods.py` + `EXTRA`. 20 columns.

---

## How to rebuild

```bash
python3 xlbuild26.py      # run TWICE — two-pass, first pass writes rowmap.json
python3 xlbuild26.py
python3 condsheet.py      # Conditions sheet
python3 progression.py    # Skill progression sheet
python3 appx.py           # Appendix 4 and 5 sheet
```

Then verify:

```bash
python3 -c "
from openpyxl import load_workbook
import statistics
wb=load_workbook('The_Encyclopedia.xlsx'); ws=wb['Skill progression']; M=ws.max_row
mic=[i for i in range(2,M+1) if ws.cell(i,1).value=='MICRO-SKILL']
rich=[i for i in mic if not str(ws.cell(i,7).value).startswith('NOT YET')]
L=[len(str(ws.cell(i,c).value or '')) for i in rich for c in range(8,13)]
print('written: %d of %d | median stage cell: %d'%(len(rich),len(mic),statistics.median(L)))
"
```

**Median below 250 means it has been templated. Stop and rewrite.**

---

## Facts to hold — do not get these wrong

- **84 Roscommon placement days**, 03/02/2026–09/07/2026. The 75-day minimum was met on
  06/07/2026. There is **no deficit**. An earlier session built a plan against a
  non-existent 37-day shortfall and wasted itself.
- **Outstanding:** Michelle's countersignature on Appendix 4; six PENDING days
  (05/02, 25/03, 26/03, 01/04, 02/04, 22/05); three unexplained gaps (03/03, 04/03,
  09/04); four Appendix 7 trainee sections blank.
- **PSI 3.3.6 is NOT met** — requires mainstream primary, post-primary AND special
  education. One post-primary day (St Nathy's, 15/04/2026), no special education.
- **Table 3 Early Years and Young Adult are unevidenced** and cannot be added
  retrospectively — they must be in the Appendix 1 before a placement starts.
- **Age bands are UCD Table 3**, not PSI or CORU.
- **CORU registration is not open** for psychologists, and UCD needs separate CORU
  approval (PSI Accreditation 2.1.6). PSI accreditation does not deliver it.
- **Cavan starts 05/10/2026**, four days a week, to 18/12/2026.

---

## What must never happen

The red columns in **Appendix 4 and 5** are a learning companion. Appendix 4 is a
countersigned record of what actually happened. **Nothing from the red columns goes into
the submitted document.**

The weekly reflections are **hers to write**. Scaffold, prompts and worked examples are
fine. Ghost-written reflections submitted as her own are not.
