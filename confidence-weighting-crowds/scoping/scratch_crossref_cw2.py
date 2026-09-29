import json, time, urllib.parse, urllib.request

QUERIES = [
    "confidence weighted majority voting group decisions",
    "when confidence weighting suboptimal collective",
    "confidence weighting does not improve crowd accuracy",
    "miscalibrated confidence weighting aggregation harm",
    "simple average beats confidence weighted average",
    "Bayesian combination correlated subjective probability estimates",
    "Condorcet jury theorem weighted votes optimal weights competence",
    "Nitzan Paroush optimal decision rules uncertain dichotomous choice",
    "Shapley Grofman optimizing group judgmental accuracy interdependencies",
    "reliability weighted majority crowdsourcing binary labels",
    "wisdom of crowds confidence weighted average calibration",
    "collective benefits of confidence sharing",
    "confidence weighted aggregation miscalibration",
    "individual confidence predicts accuracy group",
    "majority voting versus averaging binary judgments",
    "crowd aggregation confidence calibration robust",
    "optimal aggregation of correlated binary judgments",
    "confidence database secondary analysis aggregation",
    "Rahnev confidence database reanalysis",
    "group judgment accuracy confidence diversity correlated",
    "weighting by confidence fails",
    "limits of confidence weighted aggregation",
    "shared error correlation collective accuracy wisdom",
    "wisdom of crowds correlated errors shared information",
]

BASE = "https://api.crossref.org/works"

def q(query, rows=8):
    params = {"query.bibliographic": query, "rows": str(rows), "mailto": "research@example.com"}
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "novelty-check/1.0 (mailto:research@example.com)"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception:
            time.sleep(2)
    return None

out = {}
for query in QUERIES:
    d = q(query)
    print("\n" + "=" * 100)
    print("QUERY:", query)
    if not d:
        print("  FAILED"); continue
    recs = []
    for it in d["message"]["items"]:
        title = (it.get("title") or [""])[0]
        year = None
        for k in ("published-print", "published-online", "issued", "created"):
            if it.get(k, {}).get("date-parts"):
                year = it[k]["date-parts"][0][0]; break
        authors = it.get("author") or []
        first = (authors[0].get("family") or authors[0].get("given") or "") if authors else ""
        ctitle = (it.get("container-title") or [""])[0]
        rec = {"doi": it.get("DOI"), "title": title, "year": year, "first_author": first,
               "container": ctitle, "type": it.get("type"), "cited": it.get("is-referenced-by-count")}
        recs.append(rec)
        print(f"  [{year}] {first} | {title[:105]}")
        print(f"        DOI={rec['doi']} | {ctitle[:55]} | cited={rec['cited']} | {rec['type']}")
    out[query] = recs
    time.sleep(1.2)

with open("/Users/lukaswallrich/Documents/Coding/ai-jdm-paper4/scoping/scratch_crossref_cw2.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nSaved scratch_crossref_cw2.json")