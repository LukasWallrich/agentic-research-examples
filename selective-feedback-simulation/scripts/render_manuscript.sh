#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../manuscript"
pandoc manuscript.md --standalone --citeproc --resource-path=. -o manuscript.html --mathjax
pandoc manuscript.md --standalone --citeproc --resource-path=. --include-in-header=formatting.tex -o manuscript.tex
if command -v xelatex >/dev/null; then
  engine="$(command -v xelatex)"
elif [[ -x "$HOME/Library/TinyTeX/bin/universal-darwin/xelatex" ]]; then
  engine="$HOME/Library/TinyTeX/bin/universal-darwin/xelatex"
elif command -v tectonic >/dev/null; then
  engine="$(command -v tectonic)"
else
  echo 'XeLaTeX or tectonic is required for the PDF.' >&2
  exit 1
fi
pandoc manuscript.md --standalone --citeproc --resource-path=. --include-in-header=formatting.tex --pdf-engine="$engine" -o manuscript.pdf
pandoc cover_letter.md --standalone -o cover_letter.html
