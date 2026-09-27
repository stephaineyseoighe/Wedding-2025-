"""Rebuild Reference Parts G, H, I and J from the existing rows plus records/.

Run on a workbook that has not had it applied (build_all.sh starts from src/base.xlsx).
Existing rows are kept exactly; new tools, methods, conditions and presentations are
appended to their parts; Part J is updated; Part D tool cells get the Part G marker.
"""
import re
from openpyxl import load_workbook
from reclib import load, dots, arrows, first_url, snapshot, clear, put, make, BANDS, BAND_CAPS

BOOK = "The_Encyclopedia.xlsx"
wb = load_workbook(BOOK)
ws = wb["Reference"]
NC = ws.max_column
START, END = 670, ws.max_row

# ── snapshot the existing tail, split into its parts ──────────────────────────
rows = {r: snapshot(ws, r, NC) for r in range(START, END + 1)}
kind = {r: ws.cell(r, 1).value for r in rows}
heads = [r for r in rows if kind[r] in ("PART G", "PART H", "PART I", "PART J")]
g0, h0, i0, j0 = heads
G = [rows[r] for r in range(g0, h0) if any(v for v, _, _ in rows[r]["cells"])]
H = [rows[r] for r in range(h0, i0) if any(v for v, _, _ in rows[r]["cells"])]
I = [rows[r] for r in range(i0, j0) if any(v for v, _, _ in rows[r]["cells"])]
J = [rows[r] for r in range(j0, END + 1)]
blank = rows[h0 - 1]
T_TOOL, T_SECT = rows[g0 + 1], rows[g0 + 2]
T_METH, T_CITE = rows[h0 + 2], rows[h0 + 3]
T_ILAB, T_COND, T_ICITE = rows[i0 + 1], rows[i0 + 2], rows[i0 + 3]
existing_tools = {ws.cell(r, 2).value for r in rows if kind[r] == "TOOL"}
existing_methods = {ws.cell(r, 3).value for r in rows if kind[r] == "METHOD"}
existing_conds = {ws.cell(r, 3).value for r in rows if kind[r] == "CONDITION"}


def cites(template, name, refs):
    return [make(template, {3: name, 4: "Citation", 6: ref}, links={6: first_url(ref)} if first_url(ref) else None)
            for ref in refs]


# ── Part G · tools ────────────────────────────────────────────────────────────
SECTIONS = (("before", "1 · Before you open the kit", "points"), ("administer", "2 · Administering it", "points"),
            ("score", "3 · Scoring it", "points"), ("interpret", "4 · Interpreting it", "points"),
            ("errors", "5 · The errors that cost marks", "points"), ("read", "6 · What to read", "readings"))
tools = [t for t in load("TOOLS", "tools_*.py") if t["name"] not in existing_tools]
for t in tools:
    G.append(make(T_TOOL, {1: "TOOL", 2: t["name"], 5: "5 teaching sections"}))
    for key, title, unit in SECTIONS:
        pts = t[key]
        vals = {2: t["name"], 4: title, 5: "%d %s" % (len(pts), unit if len(pts) != 1 else unit[:-1])}
        links = {}
        for k, p in enumerate(pts):
            url = first_url(p) if key == "read" else None
            vals[13 + k] = p.replace(url, "").rstrip(" /—-") + "\n\n→ click to open" if url else p
            if url: links[13 + k] = url
        longest = max(len(p) for p in pts)
        G.append(make(T_SECT, vals, height=max(60, min(409, 15 * (longest // 38 + 2))), links=links))

# ── Part H · methods ──────────────────────────────────────────────────────────
MKEYS = ("history", "evidence", "when_why", "need_before", "how", "early_years", "school_age", "adolescent",
         "worked_example", "theory", "frameworks", "risk", "learn", "questions", "why_this", "next",
         "supervision", "reflection", "timeline")
methods = [m for m in load("METHODS", "methods_*.py") if m["name"] not in existing_methods]
for m in methods:
    vals = {1: "METHOD", 2: m["competencies"], 3: m["name"], 4: "Method in full", 5: m["name"],
            6: "Everything about this method is on this row. Scroll right.", 7: m["coru"], 8: m["psi"]}
    for k, key in enumerate(MKEYS):
        vals[13 + k] = m[key].strip()
    vals[13 + len(MKEYS)] = arrows(m["citations"])
    H.append(make(T_METH, vals))
    H.extend(cites(T_CITE, m["name"], m["citations"]))

# ── Part I · conditions, then presentations ──────────────────────────────────
conds = [c for c in load("CONDS", "cond_*.py") if c["name"] not in existing_conds]
for c in conds:
    b = c["bands"]
    co = ["%s — %s. PRESENTS AS: %s" % (x["name"].upper(), x["rate"].rstrip("."), x["presents"]) for x in c["cooccurring"]]
    vals = {1: "CONDITION", 3: c["name"], 4: "Condition explained", 5: c["name"], 6: c["code"],
            13: dots(c["what_it_is"]), 14: dots(c["what_it_is_not"]),
            15: dots(c["prevalence"] + ["%s: %s" % (BAND_CAPS[k], b[k]["prevalence"]) for k in BANDS]),
            16: dots(co), 17: dots(c["recommendations"]), 18: dots(c["explain_parent"]),
            19: dots(c["explain_teacher"]), 20: dots(c["explain_child"]), 21: dots(c["analogies"]),
            22: dots(c["language"]), 23: dots(["%s: %s" % (BAND_CAPS[k], b[k]["see"]) for k in BANDS]),
            24: dots(c["red_flags"]), 25: dots(c["child_voice"]), 26: dots(c["questions"]),
            27: dots(c["supervision"]), 28: dots(c["reflection"]), 29: arrows(c["citations"])}
    I.append(make(T_COND, vals))
    I.extend(cites(T_ICITE, c["name"], c["citations"]))

pres = load("PRES", "pres_*.py")
if pres:
    labels = ["1 · What it is", "2 · What it is NOT", "3 · How it shows at each age", "4 · Often sits beside",
              "5 · How you describe it — assessment", "6 · RECOMMENDATIONS — what you write",
              "7 · Explaining it to a PARENT", "8 · Explaining it to a TEACHER", "9 · Explaining it to the CHILD",
              "10 · RED FLAGS", "11 · QUESTIONS YOU WILL BE ASKED — and the answer", "12 · Bring to supervision",
              "13 · Citations"]
    lab = {5: "PRESENTATIONS WITH NO DIAGNOSIS — described, formulated and recommended for; nobody diagnoses them →"}
    lab.update({13 + k: x for k, x in enumerate(labels)})
    I.append(make(T_ILAB, lab))
    for p in pres:
        vals = {1: "PRESENTATION", 3: p["name"], 4: "Presentation explained", 5: p["name"],
                6: "No DSM code — a description, not a diagnosis · " + p["neps"],
                13: dots(p["what_it_is"]), 14: dots(p["what_it_is_not"]), 15: dots(p["by_age"]),
                16: dots(p["related_to"]), 17: dots(p["assess"]), 18: dots(p["recommendations"]),
                19: dots(p["explain_parent"]), 20: dots(p["explain_teacher"]), 21: dots(p["explain_child"]),
                22: dots(p["red_flags"]), 23: dots(p["questions"]), 24: dots(p["supervision"]),
                25: arrows(p["citations"])}
        I.append(make(T_COND, vals, height=300))
        I.extend(cites(T_ICITE, p["name"], p["citations"]))

# ── Part J · the completion map ──────────────────────────────────────────────
def jrow(label):
    for s in J:
        if str(s["cells"][1][0]).startswith(label):
            return s


def setj(label, col, value):
    s = jrow(label)
    v, st, hl = s["cells"][col - 1]
    s["cells"][col - 1] = (value, st, hl)


n_tools = len(existing_tools) + len(tools)
n_meth = len(existing_methods) + len(methods)
n_cond = len(existing_conds) + len(conds)
setj("Part G", 5, "%d tools taught" % n_tools)
setj("Part G", 6, "None at the level of Part D — every tool Part D names is taught (variants such as self-report forms are taught inside their parent tool)")
setj("Part H", 5, "%d methods" % n_meth)
setj("Part H", 6, "None of the nine named — add further methods as practice demands")
setj("Part I", 5, "%d conditions explained · %d non-diagnostic presentations" % (n_cond, len(pres)))
setj("Part I", 6, "None at the level of Part D — sub-types (other specified / unspecified) are covered inside their parent entry")

# ── write the tail back ──────────────────────────────────────────────────────
clear(ws, START, NC)
r = START
for part in (G, H, I):
    for s in part:
        put(ws, r, s); r += 1
    put(ws, r, blank); r += 1
for s in J:
    put(ws, r, s); r += 1
ws.auto_filter.ref = "A26:%s%d" % (ws.cell(1, NC).column_letter, r - 1)

# ── Part D · mark tools that now have full teaching ──────────────────────────
MARK = "\n\n*** FULL TEACHING — PART G ***"
taught = existing_tools | {t["name"] for t in tools}
marked = 0
for rr in range(507, 651):
    for cc in range(17, NC + 1):
        v = ws.cell(rr, cc).value
        if not v or "AGE:" not in str(v) or MARK.strip() in str(v):
            continue
        first = str(v).split("\n")[0].strip()
        if any(first == t or first.startswith(t) or t.startswith(first + " ") or t.split(" (")[0] == first.split(" (")[0]
               for t in taught):
            ws.cell(rr, cc).value = str(v) + MARK; marked += 1

wb.save(BOOK)
print("Part G +%d tools (%d) · Part H +%d methods (%d) · Part I +%d conditions (%d) +%d presentations · Part D marked %d · last row %d"
      % (len(tools), n_tools, len(methods), n_meth, len(conds), n_cond, len(pres), marked, r - 1))
