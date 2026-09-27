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

`src/base.xlsx` is the workbook as uploaded (with the original 55 micro-skills) and is never modified.

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
