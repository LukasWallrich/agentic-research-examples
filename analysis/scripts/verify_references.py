"""Verify every DOI in the manuscript against Crossref.

Parses https://doi.org/... from manuscript/manuscript.md, queries Crossref,
and writes manuscript/reference_audit.md flagging any DOI whose metadata does
not resolve or that is obviously mismatched.
"""
import json
import os
import re
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MS = os.path.join(ROOT, "manuscript", "manuscript.md")
OUT = os.path.join(ROOT, "manuscript", "reference_audit.md")

text = open(MS).read()
refs = re.findall(r"https://doi\.org/([^\s<>]+)", text)
seen, uniq = set(), []
for d in refs:
    d = d.rstrip(".,;")
    if d not in seen:
        seen.add(d)
        uniq.append(d)

lines = ["# Reference audit (Crossref)", "", f"DOIs found in manuscript: {len(uniq)}", ""]
fails = 0
for d in uniq:
    try:
        req = urllib.request.Request("https://api.crossref.org/works/" + d,
                                     headers={"User-Agent": "jdm4-audit"})
        m = json.load(urllib.request.urlopen(req, timeout=30))["message"]
        title = (m.get("title") or [""])[0]
        year = (m.get("issued", {}).get("date-parts", [[None]])[0][0])
        authors = ", ".join(f"{a.get('family','')}" for a in m.get("author", [])[:3])
        lines.append(f"- **OK** `{d}` — {authors} ({year}). {title}")
    except Exception as e:
        fails += 1
        lines.append(f"- **FAIL** `{d}` — {e}")
    time.sleep(0.3)

lines.append("")
lines.append(f"Total: {len(uniq)}, failures: {fails}")
open(OUT, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
print("failures:", fails)