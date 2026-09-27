"""Validate a records/*.py file (CONDS, PRES, TOOLS or METHODS) against SCHEMAS.md.

    python3 check_records.py records/cond_dld.py
"""
import importlib.util, json, re, sys

BANDS = ["Early Years", "School Age", "Adolescent", "Young Adult", "Special Setting"]
CAT = json.load(open("src/tool_catalogue.json"))
BANNED = re.compile(r"(?<!Le )grange|nathy|CS2\d-\d|ukrainian report|michelle", re.I)

path = sys.argv[1]
spec = importlib.util.spec_from_file_location("rec", path)
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
bad, warn = [], []


def blist(rec, key, lo, hi=12, minchars=0):
    v = rec.get(key)
    if not isinstance(v, list) or not all(isinstance(x, str) and x.strip() for x in v):
        bad.append("%s: %s must be a list of non-empty strings" % (rec.get("name"), key)); return 0
    if not lo <= len(v) <= hi:
        bad.append("%s: %s has %d bullets (want %d–%d)" % (rec.get("name"), key, len(v), lo, hi))
    for x in v:
        if x.lstrip()[:1] in "•▸-*":
            bad.append("%s: %s bullet starts with a bullet character" % (rec.get("name"), key)); break
    n = sum(len(x) for x in v)
    if n < minchars:
        bad.append("%s: %s is thin (%d chars, want ≥%d)" % (rec.get("name"), key, n, minchars))
    return n


def text(rec, key, minchars):
    v = rec.get(key)
    if not isinstance(v, str) or len(v) < minchars:
        bad.append("%s: %s must be a string ≥%d chars (has %d)" % (rec.get("name"), key, minchars, len(v or "")))
        return 0
    return len(v)


def scan(rec):
    s = json.dumps(rec, ensure_ascii=False)
    if BANNED.search(s):
        bad.append("%s: contains a real school/case/person reference" % rec.get("name"))
    return len(s)


total = 0
if hasattr(mod, "CONDS"):
    for c in mod.CONDS:
        for k in ("name", "code", "neps", "coru", "psi", "law"):
            text(c, k, 3)
        for k, lo, mc in (("what_it_is", 4, 700), ("what_it_is_not", 4, 600), ("prevalence", 3, 400),
                          ("recommendations", 6, 900), ("explain_parent", 4, 500), ("explain_teacher", 4, 500),
                          ("explain_child", 4, 450), ("analogies", 3, 400), ("language", 3, 250),
                          ("red_flags", 4, 500), ("child_voice", 3, 450), ("questions", 5, 900),
                          ("supervision", 4, 400), ("reflection", 5, 700), ("citations", 4, 300),
                          ("differential", 3, 300), ("next", 3, 200), ("presentations", 3, 0)):
            blist(c, k, lo, 14, mc)
        co = c.get("cooccurring")
        if not isinstance(co, list) or not 3 <= len(co) <= 9 or not all(
                isinstance(x, dict) and x.get("name") and x.get("rate") and len(x.get("presents", "")) >= 40 for x in co):
            bad.append("%s: cooccurring must be 3–9 dicts with name, rate, presents (≥40 chars)" % c.get("name"))
        pw = c.get("pathway", {})
        for k in ("age", "who_diagnoses", "who_wrote_report", "refer_to", "sooner"):
            if len(pw.get(k, "")) < 60:
                bad.append("%s: pathway.%s missing or thin" % (c.get("name"), k))
        b = c.get("bands", {})
        if sorted(b) != sorted(BANDS):
            bad.append("%s: bands keys must be exactly %s" % (c.get("name"), BANDS))
        for band in BANDS:
            x = b.get(band, {})
            if not str(x.get("applies", "")).split(" ")[0].upper().rstrip("—") in ("YES", "RARELY", "N/A", "RETROSPECTIVE", "NO"):
                bad.append("%s/%s: applies must start YES/RARELY/N/A/RETROSPECTIVE/NO" % (c.get("name"), band))
            if len(x.get("see", "")) < 80 or len(x.get("prevalence", "")) < 20:
                bad.append("%s/%s: see or prevalence thin" % (c.get("name"), band))
            for t in x.get("tools", []):
                if t not in CAT and "MEASURES" not in t:
                    bad.append("%s/%s: tool %r not in catalogue and not described" % (c.get("name"), band, t))
        total += scan(c)
elif hasattr(mod, "PRES"):
    for p in mod.PRES:
        for k in ("name", "neps"):
            text(p, k, 3)
        for k, lo, mc in (("related_to", 1, 0), ("what_it_is", 3, 350), ("what_it_is_not", 2, 250), ("by_age", 3, 350),
                          ("assess", 3, 300), ("recommendations", 4, 500), ("explain_parent", 2, 200),
                          ("explain_teacher", 2, 200), ("explain_child", 2, 180), ("red_flags", 2, 180),
                          ("questions", 3, 350), ("supervision", 2, 180), ("citations", 2, 100)):
            blist(p, k, lo, 10, mc)
        total += scan(p)
elif hasattr(mod, "TOOLS"):
    for t in mod.TOOLS:
        text(t, "name", 2)
        for k, lo, hi, mc in (("before", 3, 5, 500), ("administer", 2, 5, 350), ("score", 2, 5, 250),
                              ("interpret", 3, 5, 500), ("errors", 4, 5, 150), ("read", 2, 4, 120)):
            blist(t, k, lo, hi, mc)
        total += scan(t)
elif hasattr(mod, "METHODS"):
    keys = ("history", "evidence", "when_why", "need_before", "how", "early_years", "school_age", "adolescent",
            "worked_example", "theory", "frameworks", "risk", "learn", "questions", "why_this", "next",
            "supervision", "reflection", "timeline")
    for m in mod.METHODS:
        for k in ("name", "competencies", "coru", "psi"):
            text(m, k, 3)
        for k in keys:
            text(m, k, 450 if k not in ("early_years", "school_age", "adolescent") else 300)
        blist(m, "citations", 4, 10, 300)
        total += scan(m)
else:
    bad.append("module defines none of CONDS, PRES, TOOLS, METHODS")

print("\n".join(bad) or "OK")
print("records: %d | total characters: %d" % (len(getattr(mod, "CONDS", getattr(mod, "PRES", getattr(mod, "TOOLS", getattr(mod, "METHODS", []))))), total))
sys.exit(1 if bad else 0)
