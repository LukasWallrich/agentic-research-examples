#!/usr/bin/env bash
# Build refs.bib from dois.txt (key DOI per line) via doi.org content negotiation, and print
# Crossref/DataCite title and first author for each entry so every reference can be checked.
# An optional third column overrides the year (Crossref gives the online-first year, which can
# differ from the year of the journal volume).
set -euo pipefail
cd "$(dirname "$0")"
: > refs.bib
while read -r key doi year; do
  [ -z "$key" ] && continue
  bib=$(curl -sL -H "Accept: application/x-bibtex; charset=utf-8" "https://doi.org/$doi")
  if ! grep -q "^ *@" <<<"$bib"; then echo "FAILED $key $doi" >&2; continue; fi
  # replace the generated citation key with ours
  bib=$(sed -E "1s/^[[:space:]]*@([a-zA-Z]+)\{[^,]*,/@\1{$key,/" <<<"$bib")
  [ -n "${year:-}" ] && bib=$(sed -E "s/year=\{[0-9]{4}\}/year={$year}/" <<<"$bib")
  printf '%s\n\n' "$bib" >> refs.bib
  title=$(grep -m1 -i "title *=" <<<"$bib" | sed -E 's/.*title *= *\{(.*)\},?/\1/' | cut -c1-90)
  echo "$key | $doi | $title"
done < dois.txt
sed -i '' 's|<b>lmerTest</b>|lmerTest|' refs.bib
