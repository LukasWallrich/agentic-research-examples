import json, time, urllib.parse, urllib.request, sys

QUERIES = [
    "confidence weighting wisdom of crowds",
    "confidence weighted aggregation of judgments",
    "confidence weighted majority voting",
    "weighted majority voting correlated votes Condorcet jury theorem",
    "optimal weights Condorcet jury theorem heterogeneous jurors",
    "miscalibration wisdom of crowds",
    "confidence calibration collective decision making",
    "correlated errors wisdom of crowds aggregation",
    "confidence weighting harmful equal weighting aggregation",
    "aggregating forecasts simple average outperforms optimal weights",
    "forecast combination puzzle equal weights",
    "Confidence Database meta-analysis confidence accuracy",
    "collective decision making confidence perceptual crowd",
    "shared bias crowd aggregation correlated judgments",
    "weighted majority accuracy informative weights",
    "confidence weighted consensus crowd",
    "interacting minds confidence weighted group decision",
    "wisdom of crowds confidence heterogeneity",
    "overconfidence wisdom of crowds aggregation",
    "expertise weighting crowd judgment",
]

BASE = "https://api.crossref.org/works"

def q(query, rows=8):
    params = {
        "query.bibliographic": query,
        "rows": str(rows),
        "mailto": "research@example.com",
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "novelty-check/1.0 (mailto:research@example.com)"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            time.sleep(2)
    return None

out = {}
for query in QUERIES:
    d = q(query)
    print("\n" + "=" * 100)
    print("QUERY:", query)
    if not d:
        print("  FAILED")
        continue
    items = d["message"]["items"]
    recs = []
    for it in items:
        title = (it.get("title") or [""])[0]
        year = None
        for k in ("published-print", "published-online", "issued", "created"):
            if it.get(k, {}).get("date-parts"):
                year = it[k]["date-parts"][0][0]
                break
        authors = it.get("author") or []
        first = ""
        if authors:
            first = (authors[0].get("family") or authors[0].get("given") or "")
        ctitle = (it.get("container-title") or [""])[0]
        rec = {
            "doi": it.get("DOI"),
            "title": title,
            "year": year,
            "first_author": first,
            "container": ctitle,
            "type": it.get("type"),
            "cited": it.get("is-referenced-by-count"),
        }
        recs.append(rec)
        print(f"  [{year}] {first} | {title[:105]}")
        print(f"        DOI={rec['doi']} | {ctitle[:60]} | cited={rec['cited']} | {rec['type']}")
    out[query] = recs
    time.sleep(1.2)

with open("/Users/lukaswallrich/Documents/Coding/ai-jdm-paper4/scoping/scratch_crossref_cw.json", "w") as f:
    json.dump(out, f, indent=2)
print("\nSaved to scratch_crossref_cw.json")