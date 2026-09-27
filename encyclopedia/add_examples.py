"""Put a worked example beside every reflection prompt in 'Appendix 4 and 5'.

Adds column P ('LEARNING ONLY — worked example'), styled like the other learning
columns. Each weekly REFLECTION row gets a different weekly example, rotating
through the scaffold's eight focus areas; each CASE row gets a case-level example.
Every example is about a fictional trainee and is stamped not for submission.
"""
import copy, glob, importlib.util
from openpyxl import load_workbook

BOOK = "The_Encyclopedia.xlsx"
COL = 16  # P


def load():
    out, stamp = [], None
    for p in sorted(glob.glob("records/worked_examples*.py")):
        s = importlib.util.spec_from_file_location(p, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
        out.extend(m.EXAMPLES); stamp = stamp or getattr(m, "STAMP", None)
    return out, stamp


def text(e, stamp):
    return "\n\n".join([
        stamp,
        "TITLE:  %s\nFOCUS:  %s  ·  %s" % (e["title"], e["focus"], e["competency"]),
        "✗  THE WEAK VERSION\n" + e["weak"],
        "✓  THE STRONG VERSION\n" + e["strong"],
        "WHY THE STRONG VERSION WORKS\n" + e["why"],
        "WHAT CHANGED BETWEEN THEM\n" + e["changed"],
    ])


def rotate(weekly):
    """Order weekly examples so consecutive weeks show different focus areas."""
    by = {}
    for e in weekly:
        by.setdefault(e["focus"], []).append(e)
    order, keys = [], list(by)
    while any(by.values()):
        for k in keys:
            if by[k]:
                order.append(by[k].pop(0))
    return order


examples, stamp = load()
weekly = rotate([e for e in examples if e["type"] == "Weekly reflection"])
cases = [e for e in examples if e["type"] == "Case-level reflection"]

wb = load_workbook(BOOK)
ws = wb["Appendix 4 and 5"]
hdr = ws.cell(1, COL)
hdr.value = "LEARNING ONLY — worked example beside your prompt (fictional trainee · NOT for submission)"
hdr._style = copy.copy(ws.cell(1, 15)._style)
ws.column_dimensions["P"].width = 90

wi = ci = 0
for r in range(2, ws.max_row + 1):
    kind = ws.cell(r, 1).value
    if kind == "REFLECTION" and wi < len(weekly):
        e = weekly[wi]; wi += 1
    elif kind == "CASE" and ci < len(cases):
        e = cases[ci]; ci += 1
    else:
        continue
    c = ws.cell(r, COL)
    c.value = text(e, stamp)
    c._style = copy.copy(ws.cell(r, 15)._style)
    ws.row_dimensions[r].height = 409

refl = sum(1 for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value == "REFLECTION")
case = sum(1 for r in range(2, ws.max_row + 1) if ws.cell(r, 1).value == "CASE")
wb.save(BOOK)
print("worked examples: weekly %d of %d rows · case %d of %d rows" % (wi, refl, ci, case))
