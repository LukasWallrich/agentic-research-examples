"""Download the 180 per-study CSVs of the Confidence Database if absent.

Re-runnable: skips files already present with non-trivial size. Public CC0 data
from OSF node s46pr; no credentials required.
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "confidence_database")
FOLDER = "https://api.osf.io/v2/nodes/s46pr/files/osfstorage/5e9ecb6da0ea43006254b422/"


def list_files():
    url = FOLDER + "?page%5Bsize%5D=100"
    files = []
    while url:
        req = urllib.request.Request(url, headers={"User-Agent": "jdm4"})
        d = json.load(urllib.request.urlopen(req))
        for x in d["data"]:
            a = x["attributes"]
            if a.get("kind") == "file" and a.get("name", "").endswith(".csv"):
                files.append((a["name"], x["links"]["download"]))
        url = d["links"].get("next")
        time.sleep(0.2)
    return files


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, url in list_files():
        path = os.path.join(OUT, name)
        if os.path.exists(path) and os.path.getsize(path) > 1000:
            continue
        req = urllib.request.Request(url, headers={"User-Agent": "jdm4"})
        with urllib.request.urlopen(req) as r, open(path, "wb") as f:
            f.write(r.read())
        print("downloaded", name)
    print("files present:", len(os.listdir(OUT)))


if __name__ == "__main__":
    main()