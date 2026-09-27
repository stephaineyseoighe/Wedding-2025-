"""Corrections to text that was already in the workbook before this build.

Each fix is a (sheet, pattern, replacement, reason) rule applied to every cell of
that sheet. Runs in build_all.sh straight after src/base.xlsx is copied, so the
pristine base is never edited and every correction is visible here.
Writes CORRECTIONS.md listing what changed and how many cells each rule touched.
"""
import re
from openpyxl import load_workbook

BOOK = "The_Encyclopedia.xlsx"
TUSLA = (" This does not replace your own duty: if you are a mandated person (confirm your status with UCD), "
         "a report must reach Tusla as soon as practicable — jointly with the DLP or by you (Children First Act 2015).")

RULES = [
    # ── ICD-11 codes in Part D (repeated in every age band) ──────────────────
    ("Reference", r"(Stereotypic Movement Disorder — DSM-5-TR / ICD-11 )6A04", r"\g<1>6A06",
     "6A04 is Developmental motor coordination disorder; stereotyped movement disorder is 6A06."),
    ("Reference", r"(Reactive Attachment Disorder — DSM-5-TR / ICD-11 )6B40–6B4Z", r"\g<1>6B44",
     "6B40–6B4Z is the whole stress-associated block; reactive attachment disorder is 6B44."),
    ("Reference", r"(Adjustment Disorder \(with depressed mood / anxiety / mixed / conduct / unspecified\) — DSM-5-TR / ICD-11 )6B40–6B4Z",
     r"\g<1>6B43", "Adjustment disorder is 6B43, not the block range."),
    ("Reference", r"(Acute Stress Disorder — DSM-5-TR / ICD-11 )6B40–6B4Z",
     r"\g<1>QE84 (acute stress reaction — in ICD-11 not a mental disorder)",
     "ICD-11 codes acute stress reaction as QE84 (factors influencing health), not within 6B4x."),
    ("Reference", r"(Disruptive Mood Dysregulation Disorder — DSM-5-TR / ICD-11 )6A70–6A7Z",
     r"\g<1>— no ICD-11 equivalent (nearest: 6C90.0 ODD with chronic irritability-anger)",
     "DMDD is DSM-5-TR only; 6A70–6A7Z is the depressive-disorders block."),
    ("Reference", r"(Premenstrual Dysphoric Disorder — DSM-5-TR / ICD-11 )6A70–6A7Z", r"\g<1>GA34.41",
     "ICD-11 places PMDD at GA34.41 (with a cross-listing under depressive disorders)."),
    ("Reference", r"Spina bifida — Medical / ICD-11 Ch\.08", "Spina bifida — Medical / ICD-11 LA02 (Ch.20 Developmental anomalies)",
     "Spina bifida is ICD-11 LA02 in Chapter 20, not Chapter 08 (nervous system)."),
    # ── tool facts in Part D and the Conditions sheet (see review/r8_tools.md) ──
    ("Reference", r"GAI instead of FSIQ where index scatter exceeds 23 points\.",
     "consider GAI alongside FSIQ where large index scatter comes from Working Memory or Processing Speed (the 23-point heuristic comes from Flanagan & Kaufman (2004), WISC-IV era — check the WISC-V manual and service practice).",
     "The GAI rule is a WISC-IV-era heuristic (Flanagan & Kaufman, 2004), not a WISC-V manual rule."),
    ("Reference", r"Where index scatter exceeds 23 points, report GAI rather than FSIQ and say why\.",
     "Where large index scatter comes from Working Memory or Processing Speed, consider reporting GAI alongside FSIQ and say why (the 23-point heuristic comes from Flanagan & Kaufman (2004), WISC-IV era — check the WISC-V manual and service practice).",
     "As above."),
    ("Reference", r"Use GAI where index scatter exceeds 23 points\.",
     "Consider GAI where large scatter comes from Working Memory or Processing Speed (the 23-point heuristic comes from Flanagan & Kaufman (2004), WISC-IV era — check the WISC-V manual and service practice).", "As above."),
    ("Conditions", r"Use GAI where index scatter exceeds 23 points\.",
     "Consider GAI where large scatter comes from Working Memory or Processing Speed (the 23-point heuristic comes from Flanagan & Kaufman (2004), WISC-IV era — check the WISC-V manual and service practice).", "As above."),
    ("Conditions", r"Where index scatter exceeds 23 points, report GAI rather than FSIQ and say why\.",
     "Where large index scatter comes from Working Memory or Processing Speed, consider reporting GAI alongside FSIQ and say why (the 23-point heuristic comes from Flanagan & Kaufman (2004), WISC-IV era — check the WISC-V manual and service practice).",
     "As above."),
    ("Reference", r"(Renfrew Action Picture Test\n\nAGE: )3:0–8:11", r"\g<1>3:0–8:5 (5th ed., 2019 — check the edition you hold)",
     "Current (5th, 2019) edition norms stop at about 8:5."),
    ("Conditions", r"(Renfrew Action Picture Test — AGE )3:0–8:11", r"\g<1>3:0–8:5 (5th ed., 2019 — check the edition you hold)", "As above."),
    ("Reference", r"(Phonological Assessment Battery \(PhAB2\)\n\nAGE: )5:0–14:11",
     r"\g<1>5:0–11:11 (PhAB2 Primary; the original PhAB covers 6:0–14:11)", "PhAB2 has only a Primary edition (5–11)."),
    ("Conditions", r"(Phonological Assessment Battery \(PhAB2\) — AGE )5:0–14:11",
     r"\g<1>5:0–11:11 (PhAB2 Primary; the original PhAB covers 6:0–14:11)", "As above."),
    ("Reference", r"(Dyscalculia Screener / DysCalculiUM\n\nAGE: )6:0\+ / 15\+", r"\g<1>6–14 (Screener) / 15+ (DysCalculiUM)",
     "The GL Dyscalculia Screener covers 6–14; it is not open-ended."),
    ("Reference", r"(Piers-Harris 3\n\nAGE: )7–18", r"\g<1>6–22 (3rd edition; 7–18 was the 2nd edition)",
     "Piers-Harris 3 (2018) is normed 6–22; 7–18 was Piers-Harris 2."),
    ("Conditions", r"(Piers-Harris 3 — AGE )7–18", r"\g<1>6–22 (3rd edition; 7–18 was the 2nd edition)", "As above."),
    ("Reference", r"(DASH-17\+\n\nAGE: )17:0–25:0", r"\g<1>17:0–25:11", "DASH-17+ norms run to 25:11."),
    ("Conditions", r"(DASH-17\+ — AGE )17:0–25:0", r"\g<1>17:0–25:11", "As above."),
    # ── safeguarding: the DLP route never discharges the mandated person's duty ──
    ("Reference", r"(you follow Children First and the school DLP route\.)", r"\1" + TUSLA,
     "The original sentence could be read as the DLP route being sufficient."),
    ("Reference", r"(and you follow the DLP route\.)", r"\1" + TUSLA, "As above."),
    ("Reference", r"(Follow the school's Designated Liaison Person route\.)", r"\1" + TUSLA, "As above."),
    ("Reference", r"(Tell your supervisor the same day and follow the school's DLP route\.)", r"\1" + TUSLA, "As above."),
    ("Reference", r"(Follow the school DLP route and NEPS protocol)(?! —)", r"\1 — and Tusla as soon as practicable if the threshold is met", "As above."),
    ("Reference", r"(Any concern goes straight to the supervisor and the DLP\.)",
     r"\1 A report to Tusla follows as soon as practicable where the threshold is met — the DLP does not discharge your own duty.",
     "As above."),
]

wb = load_workbook(BOOK)
log = ["# Corrections applied to the original workbook text", "",
       "Applied by fix_base.py on every build; src/base.xlsx is untouched.", "",
       "| Sheet | Rule | Cells changed | Reason |", "|---|---|---|---|"]
total = 0
for sheet, pat, rep, why in RULES:
    ws, rx, n = wb[sheet], re.compile(pat), 0
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and not c.value.startswith("=") and rx.search(c.value):
                c.value = rx.sub(rep, c.value); n += 1
    if n == 0:
        raise SystemExit("fix_base: rule matched nothing — %r" % pat)
    total += n
    log.append("| %s | `%s` | %d | %s |" % (sheet, pat.replace("|", "\\|")[:80], n, why))
wb.save(BOOK)
open("CORRECTIONS.md", "w").write("\n".join(log) + "\n")
print("fix_base: %d rules · %d cells corrected" % (len(RULES), total))
