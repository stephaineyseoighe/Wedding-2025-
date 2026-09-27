"""Print everything needed to write micro-skills for the named macro skills.

    python3 spec.py "Macro skill name" ["Another macro" ...]

Shows, per macro: the Reference sheet teaching (columns O–S), then every
micro-skill row still to write with its block, standard and verbatim pass test.
"""
import sys
from openpyxl import load_workbook

wb = load_workbook("The_Encyclopedia.xlsx")
sp, ref = wb["Skill progression"], wb["Reference"]
norm = lambda s: " ".join(str(s or "").split())

for macro in sys.argv[1:]:
    print("=" * 80, "\nMACRO:", macro)
    for r in range(1, ref.max_row + 1):
        d = norm(ref.cell(r, 4).value)
        if d.split(". ", 1)[-1] == norm(macro) and ref.cell(r, 15).value:
            for c, lab in zip(range(15, 20), ("WHY", "TEACHING", "READING", "ERRORS", "GRADES")):
                print("\n--- Reference %s ---\n%s" % (lab, ref.cell(r, c).value))
            break
    print("\n--- MICRO-SKILLS TO WRITE ---")
    for i in range(2, sp.max_row + 1):
        if sp.cell(i, 1).value == "MICRO-SKILL" and norm(sp.cell(i, 3).value) == norm(macro):
            s4 = str(sp.cell(i, 11).value or "")
            status = "WRITTEN" if not str(sp.cell(i, 7).value).startswith("NOT YET") else "TODO"
            print("\n[%s] micro: %s\n  block: %s\n  standard: %s\n  PASS TEST (verbatim): %s\n  competency: %s"
                  % (status, norm(sp.cell(i, 5).value), sp.cell(i, 4).value, sp.cell(i, 6).value,
                     s4.split("PASS TEST — ")[-1].strip(), sp.cell(i, 2).value))
