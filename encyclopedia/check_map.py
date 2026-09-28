"""Validate a topic-mapping file: records/map_pres.py (PRES_TOPICS) or records/map_skills_*.py (SKILL_TOPICS).

    python3 check_map.py records/map_skills_a.py
"""
import collections, importlib.util, json, sys

p = sys.argv[1]
s = importlib.util.spec_from_file_location("m", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
I = json.load(open("src/map_inputs.json"))
topics = set(I["topics"])
err = []
if hasattr(m, "PRES_TOPICS"):
    D, names = m.PRES_TOPICS, {x["name"] for x in I["presentations"]}
    for k, v in D.items():
        if k not in names: err.append("unknown presentation %r" % k)
        if not isinstance(v, list) or len(v) > 3: err.append("%r: need a list of 0–3 topics" % k)
        err += ["%r: unknown topic %r" % (k, t) for t in v if t not in topics]
    miss = names - set(D)
    if miss: err.append("%d presentations missing, e.g. %r" % (len(miss), sorted(miss)[:3]))
    print("presentations %d · linked %d · unlinked %d" % (len(D), sum(1 for v in D.values() if v), sum(1 for v in D.values() if not v)))
elif hasattr(m, "SKILL_TOPICS"):
    D, keys = m.SKILL_TOPICS, {x["key"] for x in I["skills"]}
    for k, v in D.items():
        if k not in keys: err.append("unknown skill key %r" % k)
        if not isinstance(v, list): err.append("%r: need a list" % k); continue
        if "ALL" in v and len(v) > 1: err.append("%r: 'ALL' must stand alone" % k)
        if len(v) > 15: err.append("%r: %d topics — use ['ALL'] or narrow it" % (k, len(v)))
        err += ["%r: unknown topic %r" % (k, t) for t in v if t != "ALL" and t not in topics]
    comps = collections.Counter(x["competency"] for x in I["skills"] if x["key"] in D)
    print("skills %d · ALL %d · specific %d · none %d · %s" % (len(D), sum(1 for v in D.values() if v == ["ALL"]),
          sum(1 for v in D.values() if v and v != ["ALL"]), sum(1 for v in D.values() if not v), dict(comps)))
else:
    err.append("no PRES_TOPICS or SKILL_TOPICS")
print("\n".join(err[:30]) if err else "OK")
sys.exit(1 if err else 0)
