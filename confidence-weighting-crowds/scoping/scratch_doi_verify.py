import json, time, urllib.request, http.client

DOIS = [
    "10.1186/s41235-021-00279-0",
    "10.1037/dec0000187",
    "10.1017/jdm.2026.10035",
    "10.1017/jdm.2023.39",
    "10.1007/bf00118940",
    "10.2307/2526438",
    "10.3758/s13423-022-02063-7",
    "10.1287/mnsc.2018.3047",
    "10.1016/j.econlet.2026.112855",
    "10.1038/s41562-019-0813-1",
    "10.31234/osf.io/j9t6p_v2",
    "10.31234/osf.io/xnk4p",
    "10.2139/ssrn.5205685",
    "10.1038/s44159-022-00054-y",
    "10.1016/0167-2681(94)00068-p",
    "10.2139/ssrn.4387641",
    "10.1038/s41598-020-80500-0",
    "10.1007/s11238-008-9120-4",
    "10.1016/j.jebo.2021.03.029",
]

def fetch(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": "novelty-check/1.0 (mailto:research@example.com)"})
    for a in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())["message"]
        except Exception as e:
            err = e
            time.sleep(2)
    return {"__error__": str(err)}

import urllib.parse
out = {}
for doi in DOIS:
    m = fetch(doi)
    rec = {"doi": doi}
    if "__error__" in m:
        rec["error"] = m["__error__"]
        print("\n" + "!" * 90)
        print("DOI", doi, "ERROR:", m["__error__"])
    else:
        title = (m.get("title") or [""])[0]
        year = None
        for k in ("published-print", "published-online", "issued", "created"):
            if m.get(k, {}).get("date-parts"):
                year = m[k]["date-parts"][0][0]; break
        authors = [f"{a.get('family','')}, {a.get('given','')}" for a in (m.get("author") or [])]
        abstract = m.get("abstract", "")
        import re
        abstract = re.sub("<[^>]+>", " ", abstract)
        abstract = re.sub(r"\s+", " ", abstract).strip()
        ctitle = (m.get("container-title") or [""])[0]
        rec.update({"title": title, "year": year, "authors": authors, "container": ctitle,
                    "type": m.get("type"), "cited": m.get("is-referenced-by-count"),
                    "abstract": abstract[:1600], "url": m.get("URL")})
        print("\n" + "=" * 90)
        print(f"DOI: {doi}")
        print(f"TITLE: {title}")
        print(f"AUTHORS: {'; '.join(authors[:8])}")
        print(f"YEAR: {year} | VENUE: {ctitle} | TYPE: {m.get('type')} | CITED: {m.get('is-referenced-by-count')}")
        if abstract:
            print(f"ABSTRACT: {abstract[:1400]}")
    out[doi] = rec
    time.sleep(1.0)

json.dump(out, open("/Users/lukaswallrich/Documents/Coding/ai-jdm-paper4/scoping/scratch_doi_verify.json", "w"), indent=2)
print("\nSaved scratch_doi_verify.json")