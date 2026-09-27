"""Merge the Reference and Skill progression sheets into the Conditions sheet.

The Conditions layout is kept: the same 22 columns (A Level · B UCD competency ·
C Age band · D Type · E Name · F Code · G Applies · H–V fifteen content columns).
Because a column means different things on different row types, every content
cell starts with its own heading line — the convention the CO-OCCURRING rows use.

Order: INDEX → for each of the 8 competencies: COMPETENCY, STANDARD, ARC,
MACRO SKILL rows each followed by their MICRO-SKILL rows; Assessment also carries
REFERRAL AREA, TOOL, the five AGE BAND groups (Part D AREA rows, then the existing
condition blocks) and PRESENTATION rows; METHOD rows sit under their first
competency → the full STANDARDS text, the Interactive Factors prompt, the
three-year ROUTE, PAPERS and STATUS.

Hyperlinks: index → sections; codes → the standard's full text; co-occurring
names → that condition's row in the same band; condition tool cells → the TOOL row;
micro-skill 'feeds into' → the micro-skill it names; citation cells → a Google
Scholar search for the first reference; Part F papers keep their own links.

The original Reference and Skill progression sheets are left in place (the Log's
formulas and dropdowns depend on them).
"""
import re, urllib.parse
from openpyxl import load_workbook
from reclib import snapshot, clear, put, make, BANDS, BAND_FULL

BOOK = "The_Encyclopedia.xlsx"
import glob, importlib.util


def _load(pattern, var):
    out = {}
    for p in sorted(glob.glob("records/" + pattern)):
        sp = importlib.util.spec_from_file_location(p, p); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
        out.update(getattr(m, var))
    return out


EASY = _load("easy_*.py", "EASY")
ELICIT = _load("elicit_*.py", "ELICIT")
BAND_EASY = {
 "Early Years": "WHAT IT MEANS\n• This part is about young children, from birth to 5 years old.\n• Many children this age are still growing and learning fast.\n• Adults watch and help. They do not rush to give a label.",
 "School Age": "WHAT IT MEANS\n• This part is about children in primary school, aged 6 to 12.\n• This is when many difficulties with learning first show up.\n• The school and the psychologist work together to help.",
 "Adolescent": "WHAT IT MEANS\n• This part is about young people aged 13 to 16.\n• Most are in secondary school.\n• Their own views matter a lot when adults plan help.",
 "Young Adult": "WHAT IT MEANS\n• This part is about young adults aged 17 to 26.\n• Some are finishing school. Some are in college, training or work.\n• Adult services may start to help instead of children's services.",
 "Special Setting": "WHAT IT MEANS\n• This part is about children in a special class or a special school.\n• These classes are smaller and have extra help.\n• Children here often need more support to learn.",
}


def paper_line(p):
    return "▸  %s (%s). %s. %s.%s\n     %s" % (p["authors"], p["year"], p["title"], p.get("venue") or "",
                                              (" https://doi.org/" + p["doi"]) if p.get("doi") else (" " + p.get("url", "")),
                                              p["finding"])


def paper_url(p):
    return "https://doi.org/" + p["doi"] if p.get("doi") else p.get("url")


wb = load_workbook(BOOK)
C, R, S = wb["Conditions"], wb["Reference"], wb["Skill progression"]
NC = 23
norm = lambda s: " ".join(str(s or "").split())
strip_num = lambda s: re.sub(r"^\d+\.\s*", "", norm(s))


def scholar(ref):
    ref = re.sub(r"\s+", " ", str(ref)).strip(" →•▸")
    return "https://scholar.google.com/scholar?q=" + urllib.parse.quote(ref[:220])


def cell(head, body):
    body = norm(body) if body is None else str(body).strip()
    return "%s\n%s" % (head, body) if body and body != "—" else None


# ── snapshot the existing Conditions sheet ────────────────────────────────────
old = [snapshot(C, r, NC) for r in range(1, C.max_row + 1)]
lvl = [C.cell(r, 1).value for r in range(1, C.max_row + 1)]
T = {k: old[lvl.index(k)] for k in ("COMPETENCY", "STANDARD", "AGE BAND", "CONDITION", "CO-OCCURRING", "PRESENTATION")}
header, top_comp, top_std = old[0], old[1], [s for s, l in zip(old, lvl) if l == "STANDARD"]
bands, cur = {}, None
for s, l in zip(old, lvl):
    if l == "AGE BAND":
        cur = s["cells"][2][0]; bands[cur] = {"band": s, "rows": []}
    elif cur:
        bands[cur]["rows"].append(s)

BIG, LIGHT, BANNER, HEAD = T["CONDITION"], T["CO-OCCURRING"], T["AGE BAND"], T["COMPETENCY"]
rows = []           # list of (snapshot, anchor-key or None)


def add(snap, key=None):
    rows.append((snap, key))


# ── Reference Part A: competencies, standards, arc, macro skills, referral areas ──
comp_rows, macro_rows, area_rows = {}, {}, []
labels_A = {c: R.cell(30, c).value for c in range(13, 26)}
r = 26
while r < 146:
    a = R.cell(r, 1).value
    if a == "COMP":
        comp = R.cell(r, 2).value
        comp_rows[comp] = {"summary": R.cell(r, 5).value, "coru": R.cell(r + 1, 6).value,
                           "coru_txt": "\n\n".join(str(R.cell(r + 1, c).value) for c in range(13, 38) if R.cell(r + 1, c).value),
                           "psi": R.cell(r + 2, 6).value,
                           "psi_txt": "\n\n".join(str(R.cell(r + 2, c).value) for c in range(13, 38) if R.cell(r + 2, c).value),
                           "arc": [R.cell(r + 3, c).value for c in (13, 14, 15)]}
    elif a == "SKILL":
        macro_rows[strip_num(R.cell(r, 6).value)] = {
            "comp": R.cell(r, 2).value, "name": norm(R.cell(r, 6).value), "blocks": R.cell(r, 3).value,
            "cells": [(labels_A[c], R.cell(r, c).value) for c in range(13, 26)]}
    elif a == "AREA":
        area_rows.append({"comp": R.cell(r, 2).value, "macro": norm(R.cell(r, 4).value), "name": R.cell(r, 6).value,
                          "form": R.cell(r, 7).value,
                          "cells": [("DIAGNOSES", R.cell(r, 13).value), ("PRESENTATIONS", R.cell(r, 14).value),
                                    ("REFER TO", R.cell(r, 15).value)]
                                   + [(None, R.cell(r, c).value) for c in range(17, 22)]
                                   + [(None, R.cell(r, c).value) for c in range(33, 38)]})
    r += 1

# ── Skill progression: macro order and micro-skills ──────────────────────────
sp_labels = {c: S.cell(1, c).value for c in range(7, 22)}
sp_macros = []      # (comp, macro name, [micro rows])
for i in range(2, S.max_row + 1):
    a = S.cell(i, 1).value
    if a == "MACRO SKILL":
        sp_macros.append((S.cell(i, 2).value, norm(S.cell(i, 3).value), S.cell(i, 5).value, S.cell(i, 6).value, []))
    elif a == "MICRO-SKILL" and sp_macros:
        sp_macros[-1][4].append({c: S.cell(i, c).value for c in range(2, 22)})

# ── Reference Parts B, C, D, E, F, G, H, I, J ────────────────────────────────
def part_row(name):
    return next(x for x in range(1, R.max_row + 1) if R.cell(x, 1).value == name)


pB, pC, pD, pE, pF, pG, pH, pI, pJ = (part_row(p) for p in ("PART B", "PART C", "PART D", "PART E", "PART F",
                                                            "PART G", "PART H", "PART I", "PART J"))
standards, body = [], None
for x in range(pB, pC):
    if R.cell(x, 1).value in ("CORU", "PSI"): body = R.cell(x, 1).value
    elif R.cell(x, 4).value and "standard" in str(R.cell(x, 4).value).lower() or R.cell(x, 4).value == "PSI clause":
        standards.append({"body": body, "code": str(R.cell(x, 5).value), "text": R.cell(x, 6).value, "skills": R.cell(x, 7).value})
    elif R.cell(x, 2).value and not R.cell(x, 5).value is None and body:
        pass
domains = {}
for x in range(pB, pC):
    if R.cell(x, 2).value and R.cell(x, 5).value and "standard" in str(R.cell(x, 5).value): domains[x] = R.cell(x, 2).value

iff = [(R.cell(x, 4).value, R.cell(x, 5).value, R.cell(x, 6).value) for x in range(pC + 1, pD) if any(R.cell(x, c).value for c in (4, 5, 6))]
partD = {}          # band full name -> [area dicts]
band = cat = None
for x in range(pD + 1, pE):
    a = R.cell(x, 1).value
    if a == "BAND": band = norm(R.cell(x, 2).value)
    elif a == "CAT": cat = R.cell(x, 3).value
    elif R.cell(x, 4).value == "Everything for this area at this age":
        tools = [R.cell(x, c).value for c in range(17, R.max_column + 1) if R.cell(x, c).value]
        partD.setdefault(band, []).append({"cat": cat, "area": R.cell(x, 6).value, "count": R.cell(x, 5).value,
                                           "dx": R.cell(x, 13).value, "pres": R.cell(x, 14).value,
                                           "refer": R.cell(x, 15).value, "do": R.cell(x, 16).value, "tools": tools})
route = [[R.cell(x, c).value for c in range(2, 8)] for x in range(pE + 2, pF) if R.cell(x, 2).value]
papers = [(R.cell(x, 5).value, R.cell(x, 6).value, R.cell(x, 5).hyperlink.target if R.cell(x, 5).hyperlink else None)
          for x in range(pF + 1, pG) if R.cell(x, 4).value == "Paper"]
tools, x = [], pG + 1
while x < pH:
    if R.cell(x, 1).value == "TOOL":
        t = {"name": R.cell(x, 2).value, "sections": []}
        y = x + 1
        while y < pH and R.cell(y, 1).value != "TOOL" and R.cell(y, 2).value == t["name"]:
            pts = [R.cell(y, c).value for c in range(13, 20) if R.cell(y, c).value]
            t["sections"].append((R.cell(y, 4).value, pts)); y += 1
        tools.append(t); x = y
    else:
        x += 1
h_labels = {c: R.cell(pH + 1, c).value for c in range(13, 33)}
methods = [{"comp": R.cell(x, 2).value, "name": R.cell(x, 3).value, "coru": R.cell(x, 7).value, "psi": R.cell(x, 8).value,
            "f": {c: R.cell(x, c).value for c in range(13, 33)}} for x in range(pH, pI) if R.cell(x, 1).value == "METHOD"]
pres_label = next(x for x in range(pI, pJ) if str(R.cell(x, 5).value or "").startswith("PRESENTATIONS WITH NO DIAGNOSIS"))
p_labels = {c: R.cell(pres_label, c).value for c in range(13, 26)}
presentations = [{"name": R.cell(x, 3).value, "code": R.cell(x, 6).value, "f": {c: R.cell(x, c).value for c in range(13, 26)}}
                 for x in range(pres_label, pJ) if R.cell(x, 1).value == "PRESENTATION"]
status = [[R.cell(x, c).value for c in range(2, 9)] for x in range(pJ + 2, R.max_row + 1) if R.cell(x, 2).value]

# ── build the merged row list ────────────────────────────────────────────────
add(header)
index_at = len(rows)
INDEX = []          # (label, key) — filled as sections are created


def banner(text, key, sub=None, template=BANNER):
    vals = {1: "SECTION", 5: text}
    if sub: vals[8] = sub
    add(make(template, vals), key); INDEX.append((text, key))


COMPS = ["1. Assessment", "2. Formulation", "3. Intervention", "4. Systemic Change", "5. Working with Others",
         "6. Ethical Practice", "7. Supervision", "8. Research"]
method_home = {}
for m in methods:
    n = re.search(r"Competency (\d)", str(m["comp"]))
    method_home.setdefault(COMPS[int(n.group(1)) - 1] if n else COMPS[0], []).append(m)

micro_key = {}
for comp in COMPS:
    cr = comp_rows.get(comp, {})
    macros = [m for m in sp_macros if m[0] == comp]
    n_micro = sum(len(m[4]) for m in macros)
    if comp == COMPS[0]:
        v, st, hl = top_comp["cells"][4]
        n_cond = len({s["cells"][4][0] for b in bands.values() for s in b["rows"] if s["cells"][0][0] == "CONDITION"})
        top_comp["cells"][4] = ("%d macro skills · %d micro-skills · %d conditions × 5 age bands · %d tools · %d presentations"
                                % (len(macros), n_micro, n_cond, len(tools), len(presentations)), st, hl)
        add(top_comp, "comp:" + comp)
        for s in top_std: add(s)
    else:
        add(make(HEAD, {1: "COMPETENCY", 2: comp, 5: "%d macro skills · %d micro-skills" % (len(macros), n_micro)}), "comp:" + comp)
        if cr.get("coru_txt"):
            add(make(T["STANDARD"], {1: "STANDARD", 2: comp, 4: "CORU", 5: cr["coru"], 8: cr["coru_txt"]}))
        if cr.get("psi_txt"):
            add(make(T["STANDARD"], {1: "STANDARD", 2: comp, 4: "PSI", 5: cr["psi"], 8: cr["psi_txt"]}))
    INDEX.append((comp, "comp:" + comp))
    if cr.get("arc"):
        add(make(LIGHT, {1: "ARC", 2: comp, 5: "Three-year arc — what good looks like each year",
                         8: cell("YEAR 1", cr["arc"][0]), 9: cell("YEAR 2", cr["arc"][1]), 10: cell("YEAR 3", cr["arc"][2])}))
    for (_, mname, mcount, mstd, micros) in macros:
        ref = macro_rows.get(mname, {})
        vals = {1: "MACRO SKILL", 2: comp, 4: "Macro skill", 5: mname, 6: mstd, 7: mcount}
        for k, (lab, v) in enumerate(ref.get("cells", [])):
            vals[8 + k] = cell(lab.upper(), v)
        add(make(BIG, vals), "macro:" + mname)
        for mi in micros:
            mv = {1: "MICRO-SKILL", 2: comp, 3: mi[17], 4: mi[4], 5: norm(mi[5]), 6: mi[6], 7: mi[15]}
            for c in range(7, 22):
                mv[c + 1] = cell(str(sp_labels[c]).upper(), mi.get(c)) if c != 15 else cell("WHERE I AM NOW (as at build — update in Skill progression)", mi.get(c))
            add(make(BIG, mv, height=300), "micro:" + norm(mi[5]))
            micro_key[norm(mi[5])] = "micro:" + norm(mi[5])

    if comp == COMPS[0]:
        banner("REFERRAL AREAS — what the NEPS form asks, who they go to, what you assess", "areas")
        for a in area_rows:
            vals = {1: "REFERRAL AREA", 2: comp, 4: a["form"], 5: a["name"], 6: a["macro"]}
            for k, (lab, v) in enumerate(a["cells"]):
                vals[8 + k] = cell(lab, v) if lab else v
            add(make(BIG, vals, height=300))
        banner("TOOLS — taught tool by tool (before · administer · score · interpret · errors · read)", "tools")
        for t in tools:
            vals = {1: "TOOL", 2: comp, 4: "Tool taught", 5: t["name"]}
            for k, (title, pts) in enumerate(t["sections"]):
                vals[8 + k] = str(title).upper() + "\n" + "\n\n".join("▸  " + str(p) for p in pts)
            add(make(BIG, vals, height=300), "tool:" + t["name"])
        for full in [BAND_FULL[b] for b in BANDS]:
            g = bands[full]
            add(g["band"], "band:" + full); INDEX.append((full, "band:" + full))
            pd_key = next((k for k in partD if k.split("(")[0].strip() == full.split("(")[0].strip()), None)
            for a in partD.get(pd_key, []):
                vals = {1: "AREA", 2: comp, 3: full, 4: a["cat"], 5: a["area"], 6: a["count"],
                        8: a["dx"], 9: a["pres"], 10: a["refer"], 11: a["do"]}
                for k, tv in enumerate(a["tools"][:11]):
                    vals[12 + k] = "TOOL\n" + str(tv)
                add(make(BIG, vals, height=250))
            for s in g["rows"]:
                key = None
                if s["cells"][0][0] == "CONDITION":
                    key = "cond:%s:%s" % (full, s["cells"][4][0])
                add(s, key)
        banner("PRESENTATIONS WITH NO DIAGNOSIS — described, formulated and recommended for", "pres")
        for p in presentations:
            vals = {1: "PRESENTATION", 2: comp, 3: "All bands", 4: "NO DIAGNOSIS", 5: p["name"], 6: p["code"]}
            for k, c in enumerate(range(13, 26)):
                vals[8 + k] = cell(str(p_labels[c]).upper(), p["f"][c])
            add(make(BIG, vals, height=300), "pres:" + str(p["name"]))
    for m in method_home.get(comp, []):
        f, L = m["f"], lambda c: str(h_labels[c]).upper()
        joined = lambda *cs: "\n\n".join(filter(None, (cell(L(c), f[c]) for c in cs)))
        vals = {1: "METHOD", 2: comp, 4: "Method in full", 5: m["name"], 6: m["coru"], 7: m["psi"],
                8: joined(13), 9: joined(14), 10: joined(15), 11: joined(16), 12: joined(17), 13: joined(18, 19, 20),
                14: joined(21), 15: joined(22, 23), 16: joined(24), 17: joined(25), 18: joined(26), 19: joined(27, 28),
                20: joined(29, 30), 21: joined(31), 22: joined(32)}
        add(make(BIG, vals), "method:" + str(m["name"]))
        INDEX.append(("Method · " + str(m["name"]), "method:" + str(m["name"])))

banner("THE STANDARDS IN FULL — CORU Standards of Proficiency and PSI Code clauses", "standards")
for s in standards:
    add(make(LIGHT, {1: "STANDARD", 4: s["body"], 5: "%s %s" % (s["body"], s["code"]), 8: s["text"],
                     9: cell("SKILLS IN THIS WORKBOOK THAT USE IT", s["skills"])}, height=60), "std:%s %s" % (s["body"], s["code"]))
banner("INTERACTIVE FACTORS PROMPT — in full, with Irish equivalents", "iff")
for d, e, f in iff:
    add(make(LIGHT, {1: "IFF", 4: d, 5: e, 8: f}, height=45))
banner("THE THREE-YEAR ROUTE — what each body requires and where you stand", "route")
for row in route:
    add(make(LIGHT, {1: "ROUTE", 3: row[0], 4: row[1], 5: row[2], 8: cell("WHAT IT REQUIRES IN FULL", row[3]),
                     9: cell("WHERE YOU STAND", row[5] if len(row) > 5 else None)}, height=90))
banner("PAPERS BEHIND THE TOOL CHOICES", "papers")
for cit, note, url in papers:
    add(make(LIGHT, {1: "PAPER", 5: cit, 8: note}, height=45, links={5: url or scholar(cit)}))
seen_p = set()
for key, papers in ELICIT.items():
    for p in papers:
        pid = p.get("doi") or p.get("url") or p["title"]
        if pid in seen_p: continue
        seen_p.add(pid)
        add(make(LIGHT, {1: "PAPER", 4: "Found with Elicit · " + str(p.get("type") or ""), 5: "%s (%s). %s. %s." % (p["authors"], p["year"], p["title"], p.get("venue") or ""),
                         6: key.split("::", 1)[1], 8: cell("WHAT IT FOUND", p["finding"]),
                         23: cell("IN PLAIN WORDS", p["finding_easy"])}, height=60, links={5: paper_url(p)}))
banner("WHAT IS COMPLETE AND WHAT IS NOT", "status")
for row in status:
    add(make(LIGHT, {1: "STATUS", 5: row[0], 8: cell("WHAT IT COVERS", row[1]), 9: cell("DONE", row[3]),
                     10: cell("REMAINING", row[4]), 11: cell("PRIORITY ORDER", row[5])}, height=60))

# ── index rows (inserted after the header) ───────────────────────────────────
idx = [make(BANNER, {1: "INDEX", 5: "INDEX — click a line to jump. Row types: COMPETENCY · STANDARD · MACRO SKILL · MICRO-SKILL · REFERRAL AREA · TOOL · AGE BAND · AREA · CONDITION · CO-OCCURRING · PRESENTATION · METHOD · STANDARD · IFF · ROUTE · PAPER · STATUS"})]
for label, key in INDEX:
    idx.append((make(LIGHT, {1: "INDEX", 5: label}, height=15), key))
rows = rows[:index_at] + [(idx[0], None)] + [(s, ("→" + k)) for s, k in idx[1:]] + rows[index_at:]

# ── row numbers for anchors ──────────────────────────────────────────────────
pos = {}
for n, (s, k) in enumerate(rows, start=1):
    if k and not k.startswith("→"): pos[k] = n
loc = lambda key: "'Conditions'!A%d" % pos[key] if key in pos else None
std_keys = {k.split(":", 1)[1]: k for k in pos if k.startswith("std:")}


def std_link(text):
    for body, code in re.findall(r"(CORU|PSI)(?: SoP| Code)?\s*([\d.]+\d)", str(text or "")):
        k = std_keys.get("%s %s" % (body, code))
        if k: return loc(k)
    m = re.search(r"\b(\d\.\d{1,2}(?:\.\d{1,2})?)\b", str(text or ""))
    if m:
        for body in ("CORU", "PSI"):
            k = std_keys.get("%s %s" % (body, m.group(1)))
            if k: return loc(k)


tool_names = sorted((k.split(":", 1)[1] for k in pos if k.startswith("tool:")), key=len, reverse=True)


STOP = {"and", "the", "with", "disorder", "disorders", "difficulty", "difficulties", "of", "or", "in", "a", "impairment",
        "presentation", "combined", "not", "as", "co", "occurrence", "specific", "dsm", "icd"}


def words(text):
    return {w for w in re.findall(r"[a-z0-9]{3,}", text.lower()) if w not in STOP}


def best_condition(band_full, text):
    """Condition row in the same band sharing the most distinctive words with text (≥1 word, ties → shortest name)."""
    tw, best, score = words(text), None, 0
    if not tw: return None
    generic = {"anxiety": "Generalised Anxiety Disorder", "depression": "Major Depressive Disorder",
               "depressive": "Major Depressive Disorder", "mood": "Major Depressive Disorder"}
    if len(tw) == 1 and next(iter(tw)) in generic:
        k = "cond:%s:%s" % (band_full, generic[next(iter(tw))])
        if k in pos: return k
    for key in pos:
        if key.startswith("cond:%s:" % band_full):
            nm = key.split(":", 2)[2]
            sc = len(tw & words(nm))
            need = 1 if len(tw) <= 2 else 2
            if sc >= need and (sc > score or (sc == score and best and len(nm) < len(best.split(":", 2)[2]))):
                best, score = key, sc
    return best

# ── write back with hyperlinks ───────────────────────────────────────────────
clear(C, 1, NC)
from openpyxl.worksheet.hyperlink import Hyperlink
links = 0


def link(r, c, location=None, target=None):
    """Internal jump (location like 'Conditions'!A12) or external URL."""
    global links
    if location:
        C.cell(r, c).hyperlink = Hyperlink(ref=C.cell(r, c).coordinate, location=location); links += 1
    elif target:
        C.cell(r, c).hyperlink = Hyperlink(ref=C.cell(r, c).coordinate, target=target); links += 1


for n, (s, k) in enumerate(rows, start=1):
    put(C, n, s)
    kind = C.cell(n, 1).value
    if k and k.startswith("→"):
        link(n, 5, location=loc(k[1:]))
    elif kind in ("MACRO SKILL", "MICRO-SKILL"):
        link(n, 6, location=std_link(C.cell(n, 6).value))
        if kind == "MICRO-SKILL":
            feeds = str(C.cell(n, 15).value or "")
            hits = [(feeds.find(nm), nm) for nm in micro_key if len(nm) > 12 and nm in feeds and nm != norm(C.cell(n, 5).value)]
            if hits:
                link(n, 15, location=loc(micro_key[min(hits)[1]]))
    elif kind == "CO-OCCURRING":
        best = best_condition(C.cell(n, 3).value, str(C.cell(n, 5).value or ""))
        if best: link(n, 5, location=loc(best))
    elif kind == "CONDITION":
        tv = str(C.cell(n, 15).value or "")
        hits = [(tv.find(t), t) for t in tool_names if t in tv]
        if hits: link(n, 15, location=loc("tool:" + min(hits)[1]))
        cites = str(C.cell(n, 22).value or "").split("\n")
        first = next((x for x in cites[1:] if len(x.strip(" ▸→•")) > 20), None)
        if first: link(n, 22, target=scholar(first))
    elif kind in ("METHOD", "PRESENTATION", "TOOL"):
        last = max((c for c in range(8, 23) if C.cell(n, c).value), default=None)
        if last:
            refs = [x for x in str(C.cell(n, last).value).split("\n") if re.search(r"\(\d{4}", x)]
            if refs: link(n, last, target=scholar(refs[0]))
    elif kind == "AREA":
        dx = str(C.cell(n, 8).value or "")
        blocks = [b.strip() for b in dx.split("\n\n")[1:] if b.strip()]
        best = best_condition(C.cell(n, 3).value, blocks[0].split(" — ")[0]) if blocks else None
        if best: link(n, 8, location=loc(best))

# ── Easy Read column W and Elicit evidence ───────────────────────────────────
import copy as _copy
ROW_EASY = {
    "STANDARD": "WHAT THIS ROW IS\n• This row counts the rules that go with this skill area.\n• The rules come from CORU and the PSI.\n• Each rule is listed in the rows below. Each one has its own plain-words version.\n\nWORDS TO KNOW\n• CORU: the body that will register psychologists in Ireland.\n• PSI: the Psychological Society of Ireland.",
    "ARC": "WHAT THIS ROW IS\n• The course lasts three years.\n• This row shows how you grow in this skill area each year.\n• Each year asks a bit more of you than the year before.\n• Read across the row to see what good work looks like in each year.",
    "IFF": "WHAT THIS ROW IS\n• This row is a question to think about during a piece of work.\n• It comes from a guide called the Interactive Factors Framework.\n• The guide helps you look at the whole child.\n• It looks at the child, the family, the school and the wider world.\n• It also asks how these things affect each other.\n• There is no right answer. The question helps you think.",
    "ROUTE": "WHAT THIS ROW IS\n• This row shows one step on the way to becoming a psychologist.\n• It says what the college or the rules ask for.\n• It also says where you are now.\n• Check the dates and numbers with your course team before you rely on them.",
    "STATUS": "WHAT THIS ROW IS\n• This row says how much of one part of this workbook is finished.\n• It is a to-do list for the workbook.\n• It is not about any child.",
}
EASY_KIND = {"CONDITION": "condition", "MICRO-SKILL": "micro", "MACRO SKILL": "macro", "TOOL": "tool", "METHOD": "method",
             "REFERRAL AREA": "area", "AREA": "area"}
C.cell(1, 23).value = "EASY READ — in plain words"
C.cell(1, 23)._style = _copy.copy(C.cell(1, 22)._style)
C.column_dimensions["W"].width = 60
easy_n = elicit_n = 0
for n in range(2, C.max_row + 1):
    kind, name = C.cell(n, 1).value, str(C.cell(n, 5).value or "").strip()
    txt = None
    if kind in EASY_KIND:
        txt = EASY.get("%s::%s" % (EASY_KIND[kind], name))
    elif kind == "PRESENTATION" and C.cell(n, 3).value == "All bands":
        txt = EASY.get("presentation::" + name)
    elif kind == "PRESENTATION":
        txt = "WHAT IT MEANS\n• These are things a child can find hard, without having a diagnosis.\n• A diagnosis is a name a doctor or specialist gives to a condition.\n• You do not need a diagnosis to get help.\n• Adults describe what they see and plan help for it."
    elif kind == "COMPETENCY":
        txt = EASY.get("competency::" + str(C.cell(n, 2).value))
    elif kind == "STANDARD":
        txt = EASY.get("standard::" + name) or (ROW_EASY["STANDARD"] if C.cell(n, 2).value else None)
    elif kind in ROW_EASY:
        txt = ROW_EASY[kind]
    elif kind == "AGE BAND":
        txt = next((v for k, v in BAND_EASY.items() if str(C.cell(n, 3).value).startswith(BAND_FULL[k].split(" (")[0])), None)
    elif kind == "CO-OCCURRING":
        parent = str(C.cell(n, 4).value or "").replace("CO-OCCURS WITH ", "").title()
        txt = ("WHAT IT MEANS\n• Some children have more than one thing going on.\n• This row is about a child with %s who also has %s.\n"
               "• Adults check each one on its own.\n• Click the name to read about %s." % (parent, name.title(), name.title()))
    if txt:
        c = C.cell(n, 23); c.value = txt; c._style = _copy.copy(C.cell(n, 22)._style); easy_n += 1
    ekey = {"CONDITION": "condition", "TOOL": "tool", "METHOD": "method"}.get(kind)
    papers = ELICIT.get("%s::%s" % (ekey, name)) if ekey else None
    if papers:
        col = 22 if kind in ("CONDITION", "METHOD") else 14
        head = "RECENT RESEARCH — found with Elicit (click the cell for the first paper; every paper is also in the PAPERS section)"
        C.cell(n, col).value = ((str(C.cell(n, col).value) + "\n\n") if C.cell(n, col).value else "") + head + "\n" + "\n\n".join(paper_line(p) for p in papers)
        if col == 14: C.cell(n, col)._style = _copy.copy(C.cell(n, 13)._style)
        C.cell(n, col).hyperlink = Hyperlink(ref=C.cell(n, col).coordinate, target=paper_url(papers[0]))
        elicit_n += 1
print("easy read cells: %d · rows with Elicit research: %d · Elicit papers: %d" % (easy_n, elicit_n, len(seen_p)))

C.freeze_panes = "E2"
wb.save(BOOK)
kinds = {}
for n in range(1, C.max_row + 1):
    kinds[C.cell(n, 1).value] = kinds.get(C.cell(n, 1).value, 0) + 1
links = sum(1 for row in C.iter_rows() for c in row if c.hyperlink)
print("merged Conditions sheet: %d rows · %d hyperlinks · %s" % (C.max_row, links,
      " · ".join("%s %d" % (k, v) for k, v in kinds.items() if k and k != "Level")))
