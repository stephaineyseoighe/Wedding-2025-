"""Print an existing finished entry in full, as a model for new writing.

    python3 show_existing.py tool WIAT-III UK      # Part G tool (6 teaching rows)
    python3 show_existing.py method Structured play observation   # Part H row
    python3 show_existing.py condition ADHD        # Part I row
    python3 show_existing.py band ADHD "School Age"  # Conditions sheet block for one band
"""
import sys
from openpyxl import load_workbook

kind, name = sys.argv[1], sys.argv[2]
wb = load_workbook("src/base.xlsx")
ref = wb["Reference"]
if kind in ("tool", "method", "condition"):
    hdr = {"tool": 671, "method": 715, "condition": 741}[kind]
    for r in range(670, ref.max_row + 1):
        if name in (str(ref.cell(r, 2).value), str(ref.cell(r, 3).value), str(ref.cell(r, 5).value)):
            print("---- row %d · %s · %s" % (r, ref.cell(r, 1).value, ref.cell(r, 4).value))
            for c in range(6, 33):
                v = ref.cell(r, c).value
                if v:
                    h = ref.cell(hdr, c).value if kind != "tool" else ref.cell(r, 4).value
                    print("\n[%s · %s]\n%s" % (ref.cell(r, c).column_letter, h, v))
else:
    ws = wb["Conditions"]
    band = sys.argv[3]
    for r in range(2, ws.max_row + 1):
        if str(ws.cell(r, 3).value).startswith(band) and (name in str(ws.cell(r, 5).value) or "WITH " + name in str(ws.cell(r, 4).value).upper()):
            print("==== row %d · %s · %s · %s · %s" % (r, ws.cell(r, 1).value, ws.cell(r, 4).value, ws.cell(r, 5).value, ws.cell(r, 7).value))
            for c in range(8, 23):
                print("\n[%s]\n%s" % (ws.cell(1, c).value, ws.cell(r, c).value))
