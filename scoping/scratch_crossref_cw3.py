import json, time, urllib.parse, urllib.request

QUERIES = [
    "Hogarth note on aggregating opinions correlated",
    "Einhorn Hogarth Klempner quality of group judgment",
    "Soll Larrick strategies for revising judgment others opinions",
    "Larrick Soll intuitions about combining opinions averaging principle",
    "Mannes Soll Larrick wisdom of select crowds",
    "Budescu Chen identifying expertise extract wisdom of crowds",
    "Kurvers boosting medical diagnostics pooling independent judgments",
    "Mellers psychological strategies winning geopolitical forecasting tournament superforecasters",
    "Prelec Seung McCoy solution single question crowd wisdom surprisingly popular",
    "Grofman judgmental competence individuals groups dichotomous choice",
    "Ben-Yashar Nitzan optimal decision rule fixed size committees",
    "Berend Paroush when is Condorcet jury theorem valid",
    "confidence weighting hurts crowd accuracy miscalibration correlated",
    "when does confidence weighting fail collective judgment",
    "confidence weighted aggregation biased shared error",
    "wisdom of crowds confidence negative correlation accuracy",
    "weighted average judgments correlation between judges optimal number",
    "confidence sharing group perceptual decision correlated",
    "aggregation rules confidence database multi participant",
    "crowd aggregation methods comparison confidence equal weight",
    "Bayesian aggregation opinions correlated experts weights",
    "optimal number of judges correlated errors aggregation",
    "majority rule weighted competence heterogeneous jury optimal",
    "group accuracy confidence calibration correlated errors",
]

BASE = "https://api.crossref.org/works"

def q(query, rows=8):
    params = {"query.bibliographic": query, "rows": str(rows), "mailto": "research@example.com"}
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "novelty-check/1.0 (mailto:research@example.com)"})
    for _ in range(3):
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
    time.sleep(1.1)

json.dump(out, open("/Users/lukaswallrich/Documents/Coding/ai-jdm-paper4/scoping/scratch_crossref_cw3.json", "w"), indent=2)
print("\nSaved scratch_crossref_cw3.json")