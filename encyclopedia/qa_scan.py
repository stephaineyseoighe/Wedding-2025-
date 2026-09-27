"""Automated QA over every written text: micro-skills, parts/, records/.

Flags: real names, doubled labels, US spellings, non-DD/MM dates, leftover
markdown, placeholders, duplicated bullets across entries, bad bullets, and
suspicious absolutes. Prints a report; exit code 0 always (it is a report).
"""
import glob, importlib.util, json, re, collections

def load(path):
    s = importlib.util.spec_from_file_location(path, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

texts = []   # (source, key, text)
def walk(src, key, v):
    if isinstance(v, str): texts.append((src, key, v))
    elif isinstance(v, dict):
        for k, x in v.items(): walk(src, key + "." + str(k), x)
    elif isinstance(v, list):
        for i, x in enumerate(v): walk(src, key + "[%d]" % i, x)

for p in ["micro_new.py"] + sorted(glob.glob("parts/*.py")):
    for k, d in load(p).MICRO.items(): walk(p, k[1], d)
for p in sorted(glob.glob("records/*.py")):
    m = load(p)
    for var in ("CONDS", "PRES", "TOOLS", "METHODS"):
        for r in getattr(m, var, []): walk(p, r["name"], r)

CHECKS = {
 "real name": re.compile(r"\b(grange|nathy'?s|michelle|CS2\d-\d+|boyle ns)\b", re.I),
 "doubled label": re.compile(r"PRESENTS AS:\s*PRESENTS AS|PASS TEST — PASS TEST", re.I),
 "US spelling": re.compile(r"\b(behavior|behaviors|behavioral(?! and brain| research| inhibition| consultation| assessment of| sleep)|color|center|organization|organize|recognize|recognized|emphasize|minimize|prioritize|analyze|analyzed|pediatric|pediatrician|labeled|labeling|program(?!me)s?\b(?![-\s]evaluation))\b"),
 "non-DD/MM date": re.compile(r"\b(0?[1-9]|1[0-2])/(1[3-9]|2\d|3[01])/(19|20)\d\d\b"),
 "markdown": re.compile(r"\*\*|^#+ |\]\(http", re.M),
 "placeholder": re.compile(r"\bTODO\b|\bTBD\b|XXX|lorem|\[insert|\[name\]", re.I),
 "bullet char at start": re.compile(r"^\s*[•▸]\s"),
 "certainty word": re.compile(r"\b(always diagnos|guarantee[sd]?|proves that|cures?\b)", re.I),
}
hits = collections.defaultdict(list)
for src, key, t in texts:
    for name, rx in CHECKS.items():
        m = rx.search(t)
        if m: hits[name].append("%s · %s · …%s…" % (src, key[:60], t[max(0, m.start()-40):m.end()+40].replace("\n", " ")))

# duplicated long sentences across different entries (templating)
sent = collections.defaultdict(set)
for src, key, t in texts:
    for s in re.split(r"(?<=[.!?])\s+", t):
        s = s.strip()
        if len(s) > 110: sent[s].add((src, key.split(".")[0].split("[")[0]))
dups = [(s, v) for s, v in sent.items() if len({k for _, k in v}) >= 4]

print("texts scanned: %d · characters: %d" % (len(texts), sum(len(t) for _, _, t in texts)))
for name in CHECKS:
    print("\n## %s: %d" % (name, len(hits[name])))
    for h in hits[name][:25]: print("  " + h)
print("\n## sentences repeated in ≥4 different entries: %d" % len(dups))
for s, v in sorted(dups, key=lambda x: -len(x[1]))[:15]:
    print("  (%d) %s" % (len({k for _, k in v}), s[:160]))
