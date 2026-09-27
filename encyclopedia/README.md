# The Encyclopedia — build folder

`The_Encyclopedia.xlsx` is built, not edited by hand. Everything in it that was written
in this build lives as data in this folder, and every correction to the original text
is a logged rule.

## Rebuild

```bash
./build_all.sh                 # src/base.xlsx → The_Encyclopedia.xlsx
python3 verify_workbook.py     # integrity checks (must print ALL CHECKS PASSED)
python3 qa_scan.py             # names, labels, dates, spelling, templating report
```

`build_all.sh` runs, in order:

| Step | What it does |
|---|---|
| `fix_base.py` | Applies the corrections to the original text (ICD-11 codes in Part D, DLP/Tusla wording, tool ages, the GAI heuristic). Writes `CORRECTIONS.md`. |
| `make_catalogue.py` | Regenerates `src/tool_catalogue.json` from the corrected Part D tool cells. |
| `apply_micro.py` | Writes the micro-skills from `micro_new.py` and `parts/*.py` into Skill progression. |
| `build_tail.py` | Rebuilds Reference Parts G–J from `records/tools_*`, `methods_*`, `cond_*`, `pres_*`; marks taught tools in Part D. |
| `build_conditions.py` | Adds every condition in `records/cond_*` to the Conditions sheet, in all five age bands. |
| `add_examples.py` | Puts a worked example (fictional, not for submission) in column P beside every weekly and case reflection prompt in Appendix 4 and 5. |
| `build_merged.py` | Merges the Reference and Skill progression content into the Conditions sheet, keeping its 22-column layout, and adds the index and hyperlinks. |

`src/base.xlsx` is the workbook as uploaded (with the original 55 micro-skills) and is never modified.

## The merged Conditions sheet

One sheet, same 22 columns. Column A says what each row is; every content cell starts with its own heading.
Order: INDEX (clickable) → each of the 8 competencies with its CORU/PSI standards, three-year arc, MACRO SKILL
rows and their MICRO-SKILL rows → under Assessment: REFERRAL AREAs, TOOLs taught, the five AGE BAND groups
(Part D AREA rows, then CONDITION · CO-OCCURRING · PRESENTATION rows) and the 154 PRESENTATIONs with no
diagnosis → METHODs under their competency → the STANDARDS in full, the Interactive Factors prompt, the
three-year ROUTE, PAPERS and STATUS.

Hyperlinks: index → sections · standard codes → full text · co-occurring names → that condition in the same band ·
condition tool cells → the tool's teaching · area diagnoses → the condition · micro-skill "feeds into" → the
micro-skill named · citation cells → a Google Scholar search (no DOIs were invented) · Elicit research → the paper's DOI.

**Column W — EASY READ, in plain words.** Beside the professional text, not instead of it. Written for a
reader who is new to the topic, including a reader with an intellectual disability (Inclusion Ireland /
Mencap / NALA plain-English style): short sentences, one idea per line, headings in capitals, every short
form explained under WORDS TO KNOW. Every Easy Read text in `records/easy_*.py` was checked by
`python3 check_easy.py` (Flesch reading ease ≥ 60, sentences ≤ 14 words on average, 250–1,600 characters,
abbreviations explained). Easy Read leaves out figures, test names, codes, circular numbers and citations;
it keeps every hedge ("research is mixed") and every child-protection step in full (tell Tusla quickly;
telling the school's safeguarding person is not enough on its own). For anything you will quote or act on,
use the professional columns.

**Elicit research.** `records/elicit_*.py` holds recent papers (2012 on; mostly systematic reviews and
meta-analyses) found with Elicit for every condition, and for tools and methods. The papers are listed in the
condition's citation column (V) or the tool's column N as "RECENT RESEARCH — found with Elicit", with a
plain-words finding. Each one also has its own PAPER row with a DOI link. Every DOI came from Elicit; none
was typed from memory. The findings are one-line summaries of abstracts: read the paper before citing it.

Reference and Skill progression remain as separate sheets because the Log's formulas and dropdowns use them.
"Where I am now" is copied into the merged sheet at build time — keep updating it in Skill progression.

## Adding or changing content

- Micro-skills: edit `micro_new.py` or `parts/*.py`; check with `python3 check_part.py parts/<file>.py`.
- Tools, methods, conditions, presentations: edit `records/*.py` following `SCHEMAS.md`; check with
  `python3 check_records.py records/<file>.py`; `./accept.sh records/<file>.py "message"` validates,
  test-builds and commits.
- A wrong fact in the original workbook text: add a rule to `fix_base.py` (never edit `src/base.xlsx`).
- Model entries to copy the voice from: `python3 show_existing.py condition ADHD` (also `tool`, `method`, `band`).

## State at the end of this build (27/09/2026)

| Part | Done |
|---|---|
| Skill progression | 317 of 317 micro-skills, all eight competencies; median stage cell 422 characters |
| Part G · tools taught | 43 (every tool Part D names; variants taught inside their parent tool) |
| Part H · methods in full | 12 (the original 3 plus the 9 in Part J's priority list) |
| Part I · conditions | 73 conditions explained, plus 154 descriptive (non-diagnostic) presentations |
| Conditions sheet | 73 conditions × 5 UCD Table 3 age bands, each with co-occurring and presentation rows |
| Easy Read (column W) | 4,285 cells: every condition, presentation, tool, method, area, standard, macro and micro-skill, plus fixed explainers for other row types; median reading ease 80–91 by batch |
| Elicit research | 284 papers with DOIs, for all 73 conditions, 43 tools and 12 methods |
| Corrections to original text | 27 rules, 84 cells — see `CORRECTIONS.md` |

Not done: the "Cross-cutting" line in Part J (developmental re-ordering; BPS material) — still not started.

## Quality control

- Every record was validated for structure and length, then test-built into the workbook.
- Fifteen independent fact-check reviews covered every file written in this build. Each
  logged its changes (before → after → reason/source), the claims it confirmed, and what it
  could not resolve: see `review/`.
- `CHECK_BEFORE_QUOTING.md` gathers everything still unresolved. Those items are hedged in the
  text; confirm them against the source before quoting to a family, school or examiner.
- Standing caveats: PSI and CORU clause numbers come from the workbook's own Standard column and
  were not re-checked against the source texts; UCD Handbook sections are cited, but their contents
  were not available; whether a trainee is a mandated person must be confirmed in writing with UCD.

## What must never happen (from HANDOVER.md)

Nothing from the red learning columns in Appendix 4 and 5 goes into a submitted document.
Reflections and the reflective essay are yours to write — the workbook gives prompts and
structure only.
