"""Validate records/easy_*.py (EASY dict) or records/elicit_*.py (ELICIT dict).

    python3 check_easy.py records/easy_e1.py
"""
import importlib.util, json, re, sys, statistics

path = sys.argv[1]
s = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
E = json.load(open("src/entries.json"))
valid = {"%s::%s" % (k, e["name"]) for k, v in E.items() for e in v}
bad = []


def syllables(w):
    w = w.lower(); g = re.findall(r"[aeiouy]+", w)
    n = len(g) - (1 if w.endswith("e") and len(g) > 1 else 0)
    return max(1, n)


def flesch(t):
    sents = [x for x in re.split(r"[.!?\n]+", t) if re.search(r"[A-Za-z]", x)]
    words = re.findall(r"[A-Za-z']+", t)
    if not sents or not words: return 0, 0
    wps = len(words) / len(sents)
    return 206.835 - 1.015 * wps - 84.6 * sum(map(syllables, words)) / len(words), wps


if hasattr(m, "EASY"):
    scores = []
    for key, txt in m.EASY.items():
        if key not in valid: bad.append("unknown key %r" % key); continue
        if not 250 <= len(txt) <= 1600: bad.append("%s: length %d (want 250–1600)" % (key, len(txt)))
        body = txt.split("WORDS TO KNOW")[0]
        f, wps = flesch(body); scores.append(f)
        if wps > 14: bad.append("%s: sentences too long (%.1f words average, want ≤14)" % (key, wps))
        if f < 60: bad.append("%s: reading ease %.0f (want ≥60)" % (key, f))
        acr = set(re.findall(r"\b[A-Z]{2,}[a-z]?\b", body)) - {"I", "OK", "WHAT", "WHO", "WHEN", "HOW", "WHY", "WORDS", "TO", "KNOW",
                                                               "IT", "IS", "YOU", "HELPS", "MIGHT", "NOTICE", "WILL", "LEARN", "DO",
                                                               "CAN", "MATTERS", "THIS", "MEANS", "FOR", "THE", "A", "AND", "NOT", "IF",
                                                               "IMPORTANT", "ASK", "HELP", "WHERE", "GO"}
        glossary = txt.split("WORDS TO KNOW")[1] if "WORDS TO KNOW" in txt else ""
        for a in acr:
            if a not in glossary: bad.append("%s: abbreviation %s not explained under WORDS TO KNOW" % (key, a))
    print("entries %d · median reading ease %.0f" % (len(m.EASY), statistics.median(scores) if scores else 0))
elif hasattr(m, "ELICIT"):
    for key, papers in m.ELICIT.items():
        if key not in valid: bad.append("unknown key %r" % key); continue
        if not 1 <= len(papers) <= 3: bad.append("%s: %d papers (want 1–3)" % (key, len(papers)))
        for p in papers:
            for f in ("title", "authors", "year", "finding", "finding_easy"):
                if not p.get(f): bad.append("%s: paper missing %s" % (key, f))
            if not (p.get("doi") or p.get("url")): bad.append("%s: paper has no doi or url" % key)
            if int(p.get("year") or 0) < 2012: bad.append("%s: paper older than 2012" % key)
    print("entries %d · papers %d" % (len(m.ELICIT), sum(len(v) for v in m.ELICIT.values())))
print("\n".join(bad[:60]) or "OK")
sys.exit(1 if bad else 0)
